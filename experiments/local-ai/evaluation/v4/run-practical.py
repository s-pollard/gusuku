#!/usr/bin/env python3
"""Prepare one fresh v4 practical run and launch sandboxed Hermes.

Usage: python3 run-practical.py P02
Optional: --group MODEL-LABEL keeps configurations in separate run folders.
The candidate prompt still goes into the interactive Hermes chat. Select the
same model/settings as the rest of your evaluation. No global config is edited.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def prepare(task, group=None):
    if not re.fullmatch(r'P(?:0[1-9]|1[0-9]|2[0-6])', task):
        raise ValueError('Task must be P01 through P26.')
    if group and not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', group):
        raise ValueError('Use a simple model label for --group.')
    parent = HERE.parent / 'runs'
    if group:
        parent = parent / group
    parent.mkdir(parents=True, exist_ok=True)
    attempt = 1
    while True:
        run = parent / f'{task}-attempt{attempt:02d}'
        if not run.exists() and not run.is_symlink():
            break
        attempt += 1
    subprocess.run([sys.executable, '-B', str(HERE / 'lab.py'), 'init', task,
                    '--run', str(run)], check=True, stdout=subprocess.DEVNULL)
    return run


def environment(run):
    env = os.environ.copy()
    env.update({
        'HERMES_DOCKER_BINARY': 'podman',
        'TERMINAL_ENV': 'docker',
        'TERMINAL_DOCKER_IMAGE': 'localhost/homelab-ai-eval:v4',
        'TERMINAL_DOCKER_NETWORK': 'false',
        'TERMINAL_DOCKER_MOUNT_CWD_TO_WORKSPACE': 'false',
        'TERMINAL_DOCKER_VOLUMES': json.dumps([str(run / 'lab') + ':/lab:rw']),
        'TERMINAL_DOCKER_FORWARD_ENV': '[]',
        'TERMINAL_DOCKER_ENV': json.dumps({
            'PYTHONDONTWRITEBYTECODE': '1', 'GIT_OPTIONAL_LOCKS': '0'}),
        'TERMINAL_DOCKER_EXTRA_ARGS': '[]',
        'TERMINAL_CONTAINER_PERSISTENT': 'false',
        'TERMINAL_DOCKER_PERSIST_ACROSS_PROCESSES': 'false',
    })
    return env


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task')
    parser.add_argument('--group')
    parser.add_argument('--prepare-only', action='store_true',
                        help='Create fresh inputs without launching Hermes.')
    args = parser.parse_args()
    try:
        if not (HERE / 'lab.py').is_file():
            raise ValueError('Place this launcher beside lab.py in the v4 kit.')
        if not args.prepare_only:
            for binary in ['podman', 'hermes']:
                if not shutil.which(binary):
                    raise ValueError(f'{binary} is not available in PATH.')
            result = subprocess.run(
                ['podman', 'info', '--format', '{{.Host.Security.Rootless}}'],
                capture_output=True, text=True, check=True)
            if result.stdout.strip() != 'true':
                raise ValueError('Podman must run rootless, without sudo.')
            subprocess.run(['podman', 'image', 'exists',
                            'localhost/homelab-ai-eval:v4'], check=True)
        run = prepare(args.task.upper(), args.group)
        prompt = run / 'candidate-prompt.txt'
        print(f'\nFresh run: {run}\nPrompt: {prompt}\n', flush=True)
        if args.prepare_only:
            return 0
        print('Copy this complete prompt before continuing:\n', flush=True)
        print(prompt.read_text(), flush=True)
        print('Select the same model/settings in Hermes, then paste the prompt.',
              flush=True)
        input('Press Enter to open sandboxed Hermes... ')
        metadata = {'task': args.task.upper(), 'run': str(run),
                    'image': 'localhost/homelab-ai-eval:v4',
                    'toolsets': ['terminal', 'file'], 'network': 'none',
                    'mount': str(run / 'lab') + ':/lab:rw',
                    'automatic_full_grade': False}
        (run / 'launcher-record.json').write_text(
            json.dumps(metadata, indent=2) + '\n')
        result = subprocess.run(['hermes', 'chat', '--toolsets', 'terminal,file'],
                                env=environment(run), cwd=HERE.parent)
        metadata['hermes_exit_code'] = result.returncode
        (run / 'launcher-record.json').write_text(
            json.dumps(metadata, indent=2) + '\n')
        print(f'\nRun preserved at {run}', flush=True)
        if result.returncode:
            print('Hermes exited with an error; preserve it as setup/runtime evidence.')
            return result.returncode
        checked = subprocess.run([sys.executable, '-B', str(HERE / 'lab.py'),
                                  'check', '--run', str(run)],
                                 capture_output=True, text=True)
        (run / 'checker-result.json').write_text(checked.stdout)
        if checked.stderr:
            (run / 'checker-stderr.txt').write_text(checked.stderr)
        print('Objective checker output saved; full grading waits for log review.')
        print('The next task uses the same command with its ID, e.g. P05.')
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Launcher error: {exc}', file=sys.stderr)
        return 1
    except (KeyboardInterrupt, EOFError):
        print('\nCancelled; any prepared run remains intact.', file=sys.stderr)
        return 130


if __name__ == '__main__':
    raise SystemExit(main())
