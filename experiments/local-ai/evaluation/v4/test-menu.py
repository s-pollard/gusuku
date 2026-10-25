#!/usr/bin/env python3
"""Interactive v4 model/test menu. Run: python3 test-menu.py

Select an exact Hermes model ID/alias, optional provider and reasoning effort.
Select a task; its launcher displays the prompt and opens a fresh Hermes chat.
Exit Hermes with /quit to return here. Requested model settings are passed as
CLI arguments and recorded; they are not proof of the backend actually served.
"""
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
EFFORTS = ['', 'none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra']


def state_path():
    base = Path(os.environ.get('XDG_STATE_HOME', str(Path.home() / '.local/state')))
    return base / 'homelab-ai-evaluation' / 'menu.json'


def load_state():
    try:
        value = json.loads(state_path().read_text())
        if not isinstance(value, dict) or not isinstance(value.get('models'), list):
            raise ValueError('Unexpected saved-menu format.')
        for model in value['models']:
            validate_model(model)
        if not isinstance(value.get('last_tests', {}), dict):
            raise ValueError('Unexpected last-test settings.')
        return value
    except FileNotFoundError:
        return {'models': []}


def save_state(value):
    path = state_path()
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    # Menu settings contain model identifiers, not credentials.
    temporary = path.with_name('menu.json.tmp')
    with temporary.open('w') as stream:
        temporary.chmod(0o600)
        json.dump(value, stream, indent=2)
        stream.write('\n')
    temporary.replace(path)


def validate_model(model):
    for field in ['model', 'provider', 'reasoning']:
        value = model.get(field)
        if not isinstance(value, str) or any(ord(c) < 32 for c in value):
            raise ValueError('Invalid saved model settings.')
    if not model['model'].strip() or model['reasoning'] not in EFFORTS:
        raise ValueError('Model name or reasoning effort is invalid.')


def group_name(model):
    validate_model(model)
    slug = re.sub(r'[^A-Za-z0-9._-]+', '-', model['model']).strip('.-')[:42] or 'model'
    signature = hashlib.sha256(json.dumps(model, sort_keys=True).encode()).hexdigest()[:10]
    return slug + '-' + signature


def display_model(model):
    return (model['model'] + ' | provider: ' + (model['provider'] or 'configured default')
            + ' | reasoning: ' + (model['reasoning'] or 'configured default'))


def choose_model(state):
    while True:
        print('\nMODEL SELECTION')
        for number, model in enumerate(state['models'], 1):
            print(f'  {number}. {display_model(model)}')
        print('  N. Add a model / settings combination\n  Q. Quit')
        choice = input('Model: ').strip()
        if choice.lower() == 'q':
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(state['models']):
            return state['models'][int(choice) - 1]
        if choice.lower() != 'n':
            print('Choose a listed number or N.')
            continue
        print('Use the exact Hermes model ID or configured alias. Do not enter API keys or URLs.')
        model = {'model': input('Model ID / alias: ').strip(),
                 'provider': input('Provider name [Enter = existing configured provider]: ').strip(),
                 'reasoning': input('Reasoning [Enter = configured default; e.g. medium]: ').strip().lower()}
        try:
            validate_model(model)
        except ValueError as exc:
            print(exc)
            continue
        if model not in state['models']:
            state['models'].append(model)
            save_state(state)
        return model


def tasks():
    bank = json.loads((HERE / 'tasks.json').read_text())['tasks']
    return ([{'id': 'C00', 'title': 'Exact ready control', 'core': True},
             {'id': 'C01', 'title': 'JSON output control', 'core': True}] + bank)


def task_environment(model):
    validate_model(model)
    env = os.environ.copy()
    env.update(HOMELAB_EVAL_MODEL=model['model'],
               HERMES_INFERENCE_MODEL=model['model'],
               HOMELAB_EVAL_PROVIDER=model['provider'],
               HOMELAB_EVAL_REASONING=model['reasoning'])
    return env


def run_task(task, model, evidence=False):
    group = group_name(model)
    command = [sys.executable, '-B', str(HERE / 'run-test.py'), task]
    if evidence:
        command.append('--evidence')
    else:
        command += ['--group', group]
        parent = HERE.parent / 'runs' / group
        parent.mkdir(parents=True, exist_ok=True)
        selection = {**model, 'group': group,
                     'selection_updated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     'backend_verified': False}
        (parent / 'model-selection.json').write_text(json.dumps(selection, indent=2) + '\n')
    print('\n' + display_model(model), flush=True)
    print('Preparing ' + task + '. Exit Hermes with /quit to return to this menu.', flush=True)
    result = subprocess.run(command, env=task_environment(model), cwd=HERE)
    if result.returncode:
        print(f'Launcher returned {result.returncode}; preserve the message. No automatic grade.')
    else:
        print('Returned to menu. Attempt preserved; grading waits for final logs.')
    return result.returncode


def next_task(shown, last):
    ids = [task['id'] for task in shown]
    if not last:
        return ids[0] if ids else None
    if last not in ids or ids.index(last) + 1 == len(ids):
        return None
    return ids[ids.index(last) + 1]


def main():
    try:
        for name in ['run-test.py', 'run-practical.py', 'eval_clipboard.py', 'tasks.json']:
            if not (HERE / name).is_file():
                raise ValueError('Missing ' + name + '; download the complete launcher update.')
        for name in ['run-test.py', 'run-practical.py']:
            spec = importlib.util.spec_from_file_location('menu_check_' + name.replace('.', '_'), HERE / name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if getattr(module, 'MODEL_OVERRIDE_API', None) != 1:
                raise ValueError('Update all launcher files together; ' + name + ' predates model selection.')
        state = load_state()
        model = choose_model(state)
        bank = tasks()
        full = False
        last = state.get('last_tests', {}).get(group_name(model)) if model else None
        while model:
            shown = bank if full else [task for task in bank if task['core']]
            parent = HERE.parent / 'runs' / group_name(model)
            print('\nHOMELAB AI EVALUATION — ' + display_model(model))
            print('Profile: ' + ('full bank' if full else 'Core24 + controls'))
            print('Runs: ' + str(parent))
            suggested = next_task(shown, last)
            print('Last selected: ' + (last or 'none recorded') + ' | Next in this profile: ' + (suggested or 'none'))
            for number, task in enumerate(shown, 1):
                count = sum(p.is_dir() for p in parent.glob(task['id'] + '-attempt*')) if parent.exists() else 0
                suffix = f' [{count} prepared attempt(s)]' if count else ''
                marker = '  <-- LAST SELECTED' if task['id'] == last else ''
                print(f" {number:2d}. {task['id']}  {task['title']}{suffix}{marker}")
            print('\nChoose number or task ID. A=all tasks, C=core, M=model, E=incident evidence, Q=quit')
            choice = input('Test [Enter = next]: ').strip().upper()
            if not choice:
                if not suggested:
                    print('No next test in this profile; choose an ID or change profile.')
                    continue
                choice = suggested
            if choice == 'Q':
                break
            if choice in {'A', 'C'}:
                full = choice == 'A'
                continue
            if choice == 'M':
                model = choose_model(state)
                last = state.get('last_tests', {}).get(group_name(model)) if model else None
                continue
            if choice == 'E':
                incident = input('Incident ID' + (f' [{last}]' if last and last.startswith('M') else '') + ': ').strip().upper()
                if not incident and last and last.startswith('M'):
                    incident = last
                if not any(t['id'] == incident and incident.startswith('M') for t in bank):
                    print('Choose an M incident ID.')
                    continue
                run_task(incident, model, evidence=True)
                continue
            if choice.isdigit() and 1 <= int(choice) <= len(shown):
                choice = shown[int(choice) - 1]['id']
            if not any(t['id'] == choice for t in bank):
                print('Unknown test ID or menu option.')
                continue
            last = choice
            state.setdefault('last_tests', {})[group_name(model)] = choice
            save_state(state)
            run_task(choice, model)
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print('Menu error: ' + str(exc), file=sys.stderr)
        return 1
    except (EOFError, KeyboardInterrupt):
        print('\nMenu closed. Existing attempts are preserved.')
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
