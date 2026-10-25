#!/usr/bin/env python3
"""Launch a versioned homelab AI test: run-test.py E01 (or C00, M01, P02).

C/E/M: new run, original prompt, isolated empty tool workspace, interactive
Hermes, and terminal transcript when util-linux script is available.
P: delegates to run-practical.py. L: records INFRA_BLOCKED and shows the brief;
this launcher does not provision live infrastructure.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
MODEL_OVERRIDE_API = 1


def validate(task):
    limits = {'C': (0, 1), 'E': (1, 24), 'P': (1, 26),
              'M': (1, 12), 'L': (1, 8)}
    if not re.fullmatch(r'[CEPML][0-9]{2}', task):
        raise ValueError('Use a task ID such as C00, E01, P02, M01 or L01.')
    low, high = limits[task[0]]
    if not low <= int(task[1:]) <= high:
        raise ValueError('Task ID is outside the v4 bank.')


def fresh_run(task, group=None):
    if group and not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', group):
        raise ValueError('Use a simple model label for --group.')
    parent = HERE.parent / 'runs'
    if group:
        parent /= group
    parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(1, 100000):
        run = parent / f'{task}-attempt{attempt:02d}'
        try:
            run.mkdir()
            return run
        except FileExistsError:
            continue
    raise ValueError('No free attempt directory.')


def section(task):
    text = (HERE / 'evaluator-guide.md').read_text()
    found = re.search(r'^## ' + re.escape(task) + r'(?: —[^\n]*)?\n',
                      text, re.MULTILINE)
    if not found:
        raise ValueError('No matching evaluator packet.')
    end = re.search(r'^#{1,2} ', text[found.end():], re.MULTILINE)
    return text[found.start():found.end() + end.start() if end else len(text)]


def helper():
    path = HERE / 'run-practical.py'
    if not path.is_file():
        raise ValueError('Download run-practical.py beside this launcher first.')
    spec = importlib.util.spec_from_file_location('v4_practical_launcher', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ready():
    for binary in ['podman', 'hermes']:
        if not shutil.which(binary):
            raise ValueError(f'{binary} is missing from PATH.')
    result = subprocess.run(
        ['podman', 'info', '--format', '{{.Host.Security.Rootless}}'],
        capture_output=True, text=True, check=True)
    if result.stdout.strip() != 'true':
        raise ValueError('Run rootless Podman without sudo.')
    subprocess.run(['podman', 'image', 'exists',
                    'localhost/homelab-ai-eval:v4'], check=True)


def launch_command(transcript):
    command = ['hermes', 'chat', '--toolsets', 'terminal,file']
    help_result = subprocess.run(['hermes', 'chat', '--help'],
                                 capture_output=True, text=True, check=True)
    command += model_arguments(help_result.stdout)
    ignore_rules = '--ignore-rules' in help_result.stdout
    if ignore_rules:
        command.append('--ignore-rules')
    # Do not use --toolsets '' or 'none': versions may fall back to defaults.
    # Tools stay visible for a compliance test, but C/E/M forbid calling them.
    if shutil.which('script'):
        return (['script', '-q', '-e', '-f', '-c', shlex.join(command),
                 str(transcript)], command, ignore_rules, True)
    return command, command, ignore_rules, False


def model_arguments(help_text):
    values = [("HOMELAB_EVAL_MODEL", "--model"),
              ("HOMELAB_EVAL_PROVIDER", "--provider"),
              ("HOMELAB_EVAL_REASONING", "--reasoning")]
    args = []
    for key, flag in values:
        value = os.environ.get(key, "").strip()
        if value:
            if flag not in help_text:
                raise ValueError("Installed Hermes does not advertise " + flag)
            args += [flag, value]
    return args


def requested_model():
    return {"model": os.environ.get("HOMELAB_EVAL_MODEL") or "configured default",
            "provider": os.environ.get("HOMELAB_EVAL_PROVIDER") or "configured default",
            "reasoning": os.environ.get("HOMELAB_EVAL_REASONING") or "configured default",
            "backend_verified": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task')
    parser.add_argument('--group', help='Separate model/configuration run label.')
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--evidence', action='store_true',
                        help='Operator-only M evidence; does not launch Hermes.')
    args = parser.parse_args()
    task = args.task.upper()
    try:
        validate(task)
        if args.evidence:
            if task[0] != 'M':
                raise ValueError('--evidence is only for incident simulations.')
            print('EVALUATOR ONLY. Return only facts for relevant requested probes.\n')
            print(section(task))
            return 0
        if task[0] == 'P':
            command = [sys.executable, '-B', str(HERE / 'run-practical.py'), task]
            if args.group:
                command += ['--group', args.group]
            if args.prepare_only:
                command.append('--prepare-only')
            helper()  # Validate dependency before starting a subprocess.
            return subprocess.run(command).returncode
        source = HERE / 'prompts' / (task + '.txt')
        prompt = source.read_bytes()
        module = helper() if task[0] != 'L' else None
        if not args.prepare_only and task[0] != 'L':
            ready()
        run = fresh_run(task, args.group)
        (run / 'candidate-prompt.txt').write_bytes(prompt)
        record = {'suite': 'homelab-ai-v4.0', 'task': task,
                  'run': str(run), 'prompt_sha256': hashlib.sha256(prompt).hexdigest(),
                  'manual_title': '/title ' + run.name,
                  'automatic_full_grade': False, 'requested_inference': requested_model()}
        record_path = run / 'launcher-record.json'
        if task[0] == 'L':
            record['status'] = 'INFRA_BLOCKED'
            record_path.write_text(json.dumps(record, indent=2) + '\n')
            (run / 'live-preparation-brief.md').write_text(section(task))
            print(f'Live infrastructure is not supplied. Brief saved at {run}.\n')
            print(section(task))
            return 2
        (run / 'lab').mkdir()
        record.update(mode='simulation' if task[0] == 'M' else 'control' if task[0] == 'C' else 'evidence',
                      tools_visible=['terminal', 'file'], tools_authorized=False,
                      tool_workspace='empty isolated /lab; no evaluator files',
                      network='none', status='PREPARED')
        record_path.write_text(json.dumps(record, indent=2) + '\n')
        print(f'\n{task}: {run}\n', flush=True)
        if args.prepare_only:
            return 0
        print('Copy this complete prompt:\n', flush=True)
        print(prompt.decode(), flush=True)
        print('Requested model/settings: ' + json.dumps(requested_model()), flush=True)
        print(f'Optional chat title: /title {run.name}', flush=True)
        if task[0] == 'M':
            print('Keep this incident in one chat. In another Aso terminal, view\n'
                  f'operator evidence with: python3 {HERE / "run-test.py"} {task} --evidence\n'
                  'Return only relevant requested facts, not the full evidence packet.',
                  flush=True)
        input('Press Enter to open fresh Hermes, then paste the prompt... ')
        command, hermes_command, ignore_rules, captured = launch_command(run / 'hermes-terminal.log')
        record.update(status='STARTED', command=hermes_command,
                      ignore_rules=ignore_rules, terminal_transcript=captured,
                      started_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        record_path.write_text(json.dumps(record, indent=2) + '\n')
        start = time.monotonic()
        env = module.environment(run)
        if ignore_rules:
            env['HERMES_IGNORE_RULES'] = '1'
        result = subprocess.run(command, env=env, cwd=run / 'lab')
        record.update(status='SESSION_CLOSED' if result.returncode == 0 else 'RUNTIME_ERROR',
                      exit_code=result.returncode,
                      session_wall_seconds=round(time.monotonic() - start, 3),
                      ended_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        record_path.write_text(json.dumps(record, indent=2) + '\n')
        print(f'\nSaved run: {run}. Keep native Hermes exports for final review.')
        return result.returncode
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'Launcher error: {exc}', file=sys.stderr)
        return 1
    except (EOFError, KeyboardInterrupt):
        print('\nCancelled; any prepared run remains intact.', file=sys.stderr)
        return 130


if __name__ == '__main__':
    raise SystemExit(main())
