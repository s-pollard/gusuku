"""Write a candidate prompt to a clipboard; never read clipboard contents.

SSH sessions use OSC 52 to request the client terminal's clipboard. Emitting
the request is not confirmation: terminal/multiplexer policy may reject it.
"""
import base64
import os
import shutil
import subprocess
import sys


def copy_prompt(text, *, environ=None, stream=None):
    env = os.environ if environ is None else environ
    out = sys.stdout if stream is None else stream
    if env.get('HOMELAB_EVAL_CLIPBOARD', '1').lower() in {'0', 'false', 'off'}:
        return {'status': 'disabled', 'method': 'none'}
    data = text.encode('utf-8')
    if len(data) > 100000:
        return {'status': 'unavailable', 'method': 'none', 'reason': 'prompt too large'}
    remote = bool(env.get('SSH_CONNECTION') or env.get('SSH_TTY'))
    if not remote:
        candidates = []
        if sys.platform == 'darwin':
            candidates.append(['pbcopy'])
        if env.get('WAYLAND_DISPLAY'):
            candidates.append(['wl-copy'])
        if env.get('DISPLAY'):
            candidates += [['xclip', '-selection', 'clipboard'], ['xsel', '--clipboard', '--input']]
        for command in candidates:
            if not shutil.which(command[0]):
                continue
            try:
                result = subprocess.run(command, input=text, text=True,
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL, timeout=2)
                if result.returncode == 0:
                    return {'status': 'copied', 'method': command[0]}
            except (OSError, subprocess.TimeoutExpired):
                continue
    if not getattr(out, 'isatty', lambda: False)() or env.get('TERM') == 'dumb':
        return {'status': 'unavailable', 'method': 'none', 'reason': 'no capable terminal output'}
    sequence = '\x1b]52;c;' + base64.b64encode(data).decode('ascii') + '\x07'
    if env.get('TMUX'):
        sequence = '\x1bPtmux;' + sequence.replace('\x1b', '\x1b\x1b') + '\x1b\\'
    try:
        out.write(sequence)
        out.flush()
    except (OSError, ValueError):
        return {'status': 'unavailable', 'method': 'osc52', 'reason': 'terminal write failed'}
    return {'status': 'requested', 'method': 'osc52',
            'target': 'SSH client terminal' if remote else 'terminal',
            'confirmation': 'unavailable; depends on terminal/multiplexer policy'}


def announce_copy(text):
    result = copy_prompt(text)
    if result['status'] == 'copied':
        print('Prompt copied to clipboard. Paste it into Hermes after it opens.', flush=True)
    elif result['status'] == 'requested':
        print('Clipboard copy requested through the terminal. Paste into Hermes;\n'
              'if your terminal blocks it, copy the displayed prompt manually.', flush=True)
    else:
        print('Automatic clipboard copy is unavailable or disabled; copy the displayed prompt.', flush=True)
    return result
