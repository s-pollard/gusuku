#!/usr/bin/env python3
"""Create a new dated tar.gz of evaluation attempts, with index and SHA256 manifest.

Does not read global Hermes history/configuration. Quit active runs before export.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import tarfile
import uuid
import eval_save

HERE = Path(__file__).resolve().parent


def export(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    runs = eval_save.attempts(root)
    if not runs:
        raise ValueError('No evaluation attempts found.')
    records = []
    files = []
    skipped = []
    for run in runs:
        record = eval_save.read_record(run)
        records.append({'path': str(run.relative_to(root)), **record})
        # Never follow candidate-controlled symlinks into host files.
        for directory, dirs, names in os.walk(run, followlinks=False):
            base = Path(directory)
            for name in list(dirs):
                path = base / name
                if path.is_symlink():
                    skipped.append(str(path.relative_to(root)))
                    dirs.remove(name)
            for name in names:
                path = base / name
                if path.is_symlink() or not path.is_file():
                    skipped.append(str(path.relative_to(root)))
                else:
                    files.append(path)
    if any(r.get('status') == 'STARTED' for r in records):
        raise ValueError('A run is STARTED/unclosed. Quit its launcher first; inspect its record if it was killed.')
    output.parent.mkdir(parents=True, exist_ok=True)
    digest_rows = []
    # Exclusive creation: an existing export is never overwritten.
    with output.open('xb') as raw:
        try:
            with tarfile.open(fileobj=raw, mode='w:gz', dereference=False) as archive:
                for path in sorted(files):
                    name = 'runs/' + str(path.relative_to(root))
                    # O_NOFOLLOW rejects files replaced by symlinks after enumeration.
                    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
                    with os.fdopen(fd, 'rb') as stream:
                        info = archive.gettarinfo(str(path), arcname=name)
                        if not info.isfile():
                            raise ValueError('Run changed during export; quit active runs and retry.')
                        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
                        stream.seek(0)
                        archive.addfile(info, stream)
                    digest_rows.append(digest + '  ' + name)
                index = {'schema':1, 'exported_at':eval_save.now(), 'attempts':records,
                         'skipped_symlinks_or_special_files':skipped,
                         'notes':['SESSION_CLOSED means Hermes exited, not a verified task pass.',
                                  'No global Hermes session store or credentials included.']}
                for name, data in [('index.json', json.dumps(index, indent=2).encode()),
                                   ('SHA256SUMS', ('\n'.join(digest_rows)+'\n').encode())]:
                    info = tarfile.TarInfo(name); info.size=len(data); info.mode=0o600
                    archive.addfile(info, io.BytesIO(data))
        except BaseException:
            output.unlink(missing_ok=True)
            raise
    with output.open('rb') as stream:
        checksum = hashlib.file_digest(stream, 'sha256').hexdigest()
    output.with_name(output.name+'.sha256').write_text(checksum+'  '+output.name+'\n')
    return len(records)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runs', type=Path, default=HERE.parent/'runs')
    args=parser.parse_args()
    stamp=eval_save.now().replace(':','').replace('-','').split('.')[0]
    output=HERE.parent/'evaluation-exports'/f'v4-runs-{stamp}-{uuid.uuid4().hex[:6]}.tar.gz'
    try:
        count=export(args.runs,output)
    except (OSError, ValueError, tarfile.TarError) as exc:
        parser.exit(1, f'Export error: {exc}\n')
    print(f'Exported {count} attempts: {output}\nChecksum: {output}.sha256')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
