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
import eval_save

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


def downloaded_models(roots=None):
    """List GGUF filename-based IDs without reading weights or changing libraries."""
    home = Path.home()
    if roots is None:
        hermes_home = Path(os.environ.get('HERMES_HOME', str(home / '.hermes')))
        roots = [hermes_home / 'models', home / 'Models']
    found = {}
    for root in map(Path, roots):
        if not root.is_dir():
            continue
        try:
            for path in sorted(root.rglob('*.gguf')):
                relative = path.relative_to(root)
                if 'assets' in {part.lower() for part in relative.parts[:-1]}:
                    continue
                if path.name.lower().startswith(('mmproj', 'projector')):
                    continue
                try:
                    if not path.is_file():
                        continue
                except OSError:
                    continue
                item = found.setdefault(path.stem, {'model': path.stem, 'paths': []})
                location = str(path.absolute())
                if location not in item['paths']:
                    item['paths'].append(location)
        except OSError:
            continue
    return sorted(found.values(), key=lambda item: item['model'].casefold())


def choose_reasoning():
    print('Reasoning:')
    for number, effort in enumerate(EFFORTS):
        print(f'  {number}. {effort or "Configured default"}')
    while True:
        answer = input('Reasoning [Enter = configured default]: ').strip().lower()
        if not answer:
            return ''
        if answer.isdigit() and 0 <= int(answer) < len(EFFORTS):
            return EFFORTS[int(answer)]
        if answer in EFFORTS:
            return answer
        print('Choose a listed number or effort name.')


def choose_model(state):
    while True:
        print('\nMODEL SELECTION')
        entries = []
        if state['models']:
            print('Saved model/settings combinations:')
        for model in state['models']:
            entries.append(('saved', model))
            print(f'  {len(entries)}. {display_model(model)}')
        saved_ids = {model['model'] for model in state['models']}
        local = [item for item in downloaded_models() if item['model'] not in saved_ids]
        if local:
            print('Downloaded GGUF files (requested IDs come from filenames):')
        for item in local:
            entries.append(('downloaded', item))
            locations = f" [{len(item['paths'])} locations]" if len(item['paths']) > 1 else ''
            print(f"  {len(entries)}. {item['model']}{locations}")
        if not local and not state['models']:
            print('No main GGUF files found in the model directories.')
        print('  R. Refresh downloaded files\n  N. Enter another model / alias manually\n  Q. Quit')
        choice = input('Model: ').strip()
        if choice.lower() == 'q':
            return None
        if choice.lower() == 'r':
            continue
        if choice.isdigit() and 1 <= int(choice) <= len(entries):
            kind, value = entries[int(choice) - 1]
            if kind == 'saved':
                return value
            print('Selected file name: ' + value['model'])
            for location in value['paths']:
                print('  ' + location)
            print('Using the existing configured provider. Hermes must accept this ID;\n'
                  'file discovery alone does not verify the model served by your backend.')
            model = {'model': value['model'], 'provider': '', 'reasoning': choose_reasoning()}
            state['models'].append(model)
            save_state(state)
            return model
        if choice.lower() != 'n':
            print('Choose a listed number, R or N.')
            continue
        print('Use the exact Hermes model ID or configured alias. Do not enter API keys or URLs.')
        model = {'model': input('Model ID / alias: ').strip(),
                 'provider': input('Provider name [Enter = existing configured provider]: ').strip(),
                 'reasoning': choose_reasoning()}
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



SECTION_NAMES = {'K': 'Core24 + controls', 'A': 'All tasks', 'C': 'Controls',
                 'E': 'Evidence / planning', 'P': 'Practical',
                 'M': 'Incident simulations', 'L': 'Live lab contracts'}


def screen_choice(shown, model, section, last, parent, positions):
    """Restore terminal modes before any launcher, prompt or child process runs."""
    import curses

    def draw(screen):
        screen.keypad(True)
        try:
            curses.curs_set(0)
        except curses.error:
            pass
        index = min(positions.get(section, 0), max(0, len(shown) - 1))
        counts = {t['id']: eval_save.status_summary(parent, t['id']) for t in shown}
        while True:
            height, width = screen.getmaxyx()
            screen.erase()

            def line(row, text, selected=False):
                if 0 <= row < height and width > 1:
                    try:
                        screen.addnstr(row, 0, text, width - 1,
                                       curses.A_REVERSE if selected else curses.A_NORMAL)
                    except curses.error:
                        pass

            line(0, 'HOMELAB AI EVALUATION')
            line(1, display_model(model))
            line(2, 'Section: ' + SECTION_NAMES[section] + ' | Last selected: ' + (last or 'none'))
            line(3, 'Runs: ' + str(parent))
            visible = max(1, height - 9)
            start = min(max(0, index - visible // 2), max(0, len(shown) - visible))
            for offset, task in enumerate(shown[start:start + visible]):
                n = start + offset
                suffix = f" [{counts[task['id']]}]" if counts[task['id']] else ''
                marker = '  LAST SELECTED' if task['id'] == last else ''
                line(5 + offset, f" {'>' if n == index else ' '} {task['id']}  {task['title']}{suffix}{marker}", n == index)
            line(height - 3, 'C controls | E planning | P practical | M incidents | L live | A all | K core')
            line(height - 2, 'S model | V incident evidence | U export runs | Q quit | : type test ID/number')
            line(height - 1, f'Up/Down select | Enter launch | PgUp/PgDn scroll  ({index + 1}/{len(shown)})')
            screen.refresh()
            key = screen.get_wch()
            if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_PPAGE, curses.KEY_NPAGE,
                       curses.KEY_HOME, curses.KEY_END):
                if key == curses.KEY_HOME:
                    index = 0
                elif key == curses.KEY_END:
                    index = len(shown) - 1
                else:
                    delta = {curses.KEY_UP: -1, curses.KEY_DOWN: 1,
                             curses.KEY_PPAGE: -visible, curses.KEY_NPAGE: visible}[key]
                    index = max(0, min(len(shown) - 1, index + delta))
                positions[section] = index
            elif key in ('\n', '\r', curses.KEY_ENTER):
                positions[section] = index
                return shown[index]['id']
            elif isinstance(key, str) and key.upper() in 'CE PMLAKSVQU'.replace(' ', ''):
                positions[section] = index
                return key.upper()
            elif key == ':' or (isinstance(key, str) and key.isdigit()):
                value = key if key != ':' else ''
                while True:
                    line(height - 1, ' ' * max(0, width - 1))
                    line(height - 1, 'Test ID/number: ' + value)
                    screen.refresh()
                    typed = screen.get_wch()
                    if typed in ('\n', '\r', curses.KEY_ENTER):
                        if value:
                            return value.upper()
                        break
                    if typed == '\x1b':
                        break
                    if typed in (curses.KEY_BACKSPACE, '\x7f', '\b'):
                        value = value[:-1]
                    elif isinstance(typed, str) and typed.isalnum() and len(value) < 12:
                        value += typed
            # KEY_RESIZE redraws using the new terminal dimensions.
    return curses.wrapper(draw)


def main():
    try:
        for name in ['run-test.py', 'run-practical.py', 'eval_clipboard.py', 'eval_save.py', 'export-runs.py', 'tasks.json']:
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
        section = 'K'
        positions = {}
        fullscreen = sys.stdin.isatty() and sys.stdout.isatty() and os.environ.get('TERM', '') not in ('', 'dumb')
        last = state.get('last_tests', {}).get(group_name(model)) if model else None
        while model:
            shown = ([task for task in bank if task['core']] if section == 'K' else
                     bank if section == 'A' else
                     [task for task in bank if task['id'].startswith(section)])
            parent = HERE.parent / 'runs' / group_name(model)
            suggested = next_task(shown, last)
            if fullscreen:
                choice = screen_choice(shown, model, section, last, parent, positions)
            else:
                print('\nHOMELAB AI EVALUATION — ' + display_model(model))
                print('Section: ' + {'K': 'Core24 + controls', 'A': 'All tasks',
                      'C': 'Controls', 'E': 'Evidence / planning', 'P': 'Practical',
                      'M': 'Incident simulations', 'L': 'Live lab contracts'}[section])
                print('Runs: ' + str(parent))
                suggested = next_task(shown, last)
                print('Last selected: ' + (last or 'none recorded') + ' | Next in this profile: ' + (suggested or 'none'))
                for number, task in enumerate(shown, 1):
                    count = eval_save.status_summary(parent, task['id'])
                    suffix = f' [{count}]' if count else ''
                    marker = '  <-- LAST SELECTED' if task['id'] == last else ''
                    print(f" {number:2d}. {task['id']}  {task['title']}{suffix}{marker}")
                print('\nSections: C=controls, E=evidence/planning, P=practical, M=incidents, L=live lab')
                print('A=all tasks, K=Core24, S=select model, V=view incident evidence, U=export runs, Q=quit')
                print('Choose a section, test number or full task ID (such as P02).')
                choice = input('Test [Enter = next]: ').strip().upper()
            if not choice:
                if not suggested:
                    print('No next test in this profile; choose an ID or change profile.')
                    continue
                choice = suggested
            if choice == 'U':
                subprocess.run([sys.executable, '-B', str(HERE / 'export-runs.py')], cwd=HERE)
                if fullscreen:
                    input('Press Enter to return to the test menu: ')
                continue
            if choice == 'Q':
                break
            if choice in {'A', 'K', 'C', 'E', 'P', 'M', 'L'}:
                section = choice
                continue
            if choice == 'S':
                model = choose_model(state)
                last = state.get('last_tests', {}).get(group_name(model)) if model else None
                continue
            if choice == 'V':
                incident = input('Incident ID' + (f' [{last}]' if last and last.startswith('M') else '') + ': ').strip().upper()
                if not incident and last and last.startswith('M'):
                    incident = last
                if not any(t['id'] == incident and incident.startswith('M') for t in bank):
                    print('Choose an M incident ID.')
                    continue
                run_task(incident, model, evidence=True)
                if fullscreen:
                    input('Press Enter to return to the test menu: ')
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
            if fullscreen:
                input('Press Enter to return to the test menu: ')
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print('Menu error: ' + str(exc), file=sys.stderr)
        return 1
    except (EOFError, KeyboardInterrupt):
        print('\nMenu closed. Existing attempts are preserved.')
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
