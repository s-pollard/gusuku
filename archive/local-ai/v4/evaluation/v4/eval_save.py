"""Attempt-local durable records and terminal capture; never read global Hermes history."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import time
import uuid

SCHEMA = 1


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def save(run, record, status=None, **fields):
    run = Path(run)
    record.update(fields)
    if 'save_schema' not in record:
        prompt = run / 'candidate-prompt.txt'
        kit = Path(__file__).parent
        digest = hashlib.sha256()
        for name in ('tasks.json', 'lab.py', 'fixtures.py', 'eval_save.py', 'run-test.py', 'run-practical.py'):
            source = kit / name
            if source.is_file():
                digest.update(name.encode() + b'\0' + source.read_bytes())
        record.update(save_schema=SCHEMA, attempt_id=str(uuid.uuid4()),
                      created_at=now(), suite='homelab-ai-v4.0', kit_sha256=digest.hexdigest(),
                      prompt_sha256=hashlib.sha256(prompt.read_bytes()).hexdigest(),
                      native_hermes_session_id=None, backend_verified=False,
                      task_completion_verified=False, automatic_full_grade=False)
    if status:
        record['status'] = status
    record['updated_at'] = now()
    path = run / 'launcher-record.json'
    temp = run / '.launcher-record.tmp'
    with temp.open('w') as stream:
        json.dump(record, stream, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temp.replace(path)
    with (run / 'events.jsonl').open('a') as stream:
        stream.write(json.dumps({'at':record['updated_at'], 'status':record.get('status'),
                                 'attempt_id':record['attempt_id']}) + '\n')
        stream.flush()
        os.fsync(stream.fileno())


def capture(run, record, command, env, cwd):
    if not shutil.which('script'):
        raise ValueError('util-linux script is required to save the complete terminal transcript.')
    transcript = Path(run) / 'hermes-terminal.log'
    save(run, record, 'STARTED', command=command, started_at=now(),
         terminal_transcript=True, transcript_file=transcript.name,
         transcript_format='raw terminal output; may contain ANSI controls',
         native_session_note='Native session ID is not automatically linked; terminal transcript is saved here.')
    start = time.monotonic()
    result = subprocess.run(['script', '-q', '-e', '-f', '-c', shlex.join(command),
                             str(transcript)], env=env, cwd=cwd)
    save(run, record, 'SESSION_CLOSED' if result.returncode == 0 else 'RUNTIME_ERROR',
         exit_code=result.returncode, ended_at=now(),
         session_wall_seconds=round(time.monotonic()-start, 3))
    return result


def failure(run, record, exc, interrupted=False):
    if run is not None:
        save(run, record, 'INTERRUPTED' if interrupted else 'LAUNCHER_ERROR',
             ended_at=now(), error=str(exc) or type(exc).__name__)


def attempts(root):
    import re
    root = Path(root)
    if not root.is_dir():
        return []
    parents = [root] + [p for p in root.iterdir() if p.is_dir() and not p.is_symlink()]
    return sorted(p for parent in parents for p in parent.iterdir()
                  if re.fullmatch(r'[CEPML]\d{2}-attempt\d+', p.name)
                  and p.is_dir() and not p.is_symlink())


def read_record(run):
    try:
        return json.loads((run / 'launcher-record.json').read_text())
    except (OSError, ValueError):
        return {'status': 'LEGACY_OR_UNRECORDED'}


def status_summary(parent, task):
    from collections import Counter
    counts = Counter(read_record(p).get('status', 'UNKNOWN')
                     for p in Path(parent).glob(task + '-attempt*')
                     if p.is_dir() and not p.is_symlink())
    labels = {'PREPARED': 'prepared', 'STARTED': 'started/unclosed',
              'SESSION_CLOSED': 'closed', 'RUNTIME_ERROR': 'runtime error',
              'LAUNCHER_ERROR': 'launcher error', 'INTERRUPTED': 'interrupted',
              'INFRA_BLOCKED': 'blocked'}
    return ', '.join(f'{n} {labels.get(k, k.lower())}' for k,n in sorted(counts.items()))
