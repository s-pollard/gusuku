# Interactive model/test menu

Start `python3 test-menu.py` from the extracted kit. The model screen lists saved configurations and automatically discovers main GGUF files under `~/.hermes/models` (or `$HERMES_HOME/models`) and `~/Models`. Choose a number; no model-name typing is needed. Repeated filenames are grouped into one downloaded choice with their location count; this is not a byte-identity check. The scan excludes `assets/` and projector filenames, reads no model weights and does not move or register files. R refreshes the list; N retains manual ID/alias entry. For a newly selected downloaded model, choose reasoning by number or press Enter for the configured default. The existing provider is retained. Saved choices remain available on later runs.

The task menu defaults to Core24 plus controls. Select a number or type an ID such as E01 or P02. C, E, P, M and L show their complete test sections. A shows the full bank, K returns to Core24, S changes the model, V displays operator-only incident evidence, and Q exits. Section letters filter the list; a full ID such as P02 launches a test. In an interactive terminal the test menu redraws in place: Up/Down highlight a test, Enter launches it, PgUp/PgDn scroll, and : accepts a full test ID or number. Section shortcuts remain single keys. The highlighted position is kept per section while the menu is open, including after Hermes exits. Press Enter after reviewing launcher output to return. Noninteractive/dumb terminals retain the numbered text menu with Enter suggesting the next test. The launcher displays the full prompt, prepares the appropriate environment and opens fresh Hermes after Enter. Paste the prompt; exit Hermes with /quit to return to the menu. Requested model/provider/reasoning are passed explicitly to Hermes for each run and recorded. The installed CLI is checked for the corresponding options; unsupported overrides stop instead of being silently ignored. Normal saved Hermes configuration is not changed.

Runs are grouped as `~/runs/<model-and-settings-label>/ID-attemptNN/`. Different provider/reasoning selections receive separate groups. `model-selection.json` records the selected settings; each attempt retains its own requested-inference record. These are requested settings, not independent proof of which backend served the request. Preserve native session evidence and any model switches/fallbacks. Menu settings are saved privately under `$XDG_STATE_HOME/homelab-ai-evaluation/menu.json`, defaulting to `~/.local/state/homelab-ai-evaluation/menu.json`. Prepared-attempt counts are not grades or completed coverage.

Update test-menu.py, run-test.py, run-practical.py and eval_clipboard.py together. The menu refuses launchers that predate model overrides. The downloadable `evaluation-launchers.tar.gz` contains those four files only; extract it inside the existing v4 kit. The original task bank, prompts, fixtures and previous attempts are unchanged.

## Downloaded filename IDs

Downloaded choices send the GGUF filename stem (without `.gguf`) as the requested Hermes model ID. This removes typing, but does not independently establish library registration, which model a manually managed single-model server loaded, or what backend actually served a request. Native Hermes acceptance and session/backend evidence remain required. If your setup needs a different ID or configured alias, retain it as a saved choice or use N. The menu does not silently relabel an error as a successful model switch, and it does not import external GGUF files into Hermes's library.

## Last selection and automatic clipboard

The last selected task is saved separately for each model/provider/reasoning group. It is shown in the menu header and marked `LAST SELECTED` in the list. Enter selects the next task in the displayed profile. A selected task is not proof of completion or a passing grade; select the same ID explicitly to repeat it with fresh files. Restarting the menu restores this selection after choosing that model/settings combination.

Both launchers try to copy the complete candidate prompt before opening Hermes. In SSH sessions, OSC 52 requests the client terminal's clipboard rather than changing Aso's desktop clipboard. No clipboard contents are read. The terminal may ignore or require permission for the request; a successful request is not reported as confirmed copying. Through tmux, a passthrough sequence is used, which also depends on multiplexer policy. Native local clipboard tools are used for direct desktop sessions when available. The prompt remains displayed for manual copying in every case.

Set `HOMELAB_EVAL_CLIPBOARD=0` when starting the menu to disable automatic copying. Each launched attempt records whether copying was requested, completed via a local tool, disabled or unavailable. `--evidence` never copies the private incident packet. Menu-only model data and last-task history remain in the same private state file as before. Previously saved model choices and run folders are preserved.

---

# Individual test launchers

Place run-test.py and run-practical.py beside lab.py in the extracted v4 kit.
They use the rootless Podman image `localhost/homelab-ai-eval:v4` prepared during
setup. Each task gets a new attempt directory under the kit's sibling `runs/`.
An optional `--group model-label` separates configurations. Existing attempts
are preserved. Normal saved Hermes configuration is not changed.

```sh
python3 ~/homelab-ai-evaluation-v4/run-test.py C00
python3 ~/homelab-ai-evaluation-v4/run-test.py E01
python3 ~/homelab-ai-evaluation-v4/run-test.py P02
python3 ~/homelab-ai-evaluation-v4/run-test.py M01
```

Run one command for the selected task, copy the displayed complete prompt,
press Enter, select the correct model/reasoning settings, and paste the prompt.
A new Hermes process is started without resume flags; no `/new` is needed.
After finishing, export the native chat as usual and exit with `/quit` to
return to the launcher. The script preserves the run and process exit status.

The run folder is named automatically. Chat titles are not automatically set;
the launcher displays an optional `/title ID-attemptNN` command. The selected
model and effective reasoning settings still need native session evidence.
Session wall time includes operator interaction and is not pure inference time.

## C and E

Use one fresh session per task. Tools remain visible (`terminal,file`) to test
the explicit no-tool instruction; any call violates the prompt. They are routed
to an offline rootless container with an empty /lab directory. The prompt,
evaluator guide and other kit files are not mounted into that container.
Do not assume `--toolsets none` or an empty string disables tools on Hermes
versions that fall back to the default toolsets. Record this exposure policy
when comparing with earlier sessions.

If `hermes chat --help` advertises `--ignore-rules`, the launcher uses it to
reduce context-file/memory/skill injection and records that setting. Otherwise
the record says false; ensure comparable exposure and do not claim memory was
cleared just because the session is new. The script never reads credentials.

## M simulations

Start the incident with `run-test.py M01`. Keep all incident turns in that chat.
In another Aso terminal, display only that incident's evaluator packet:

```sh
python3 ~/homelab-ai-evaluation-v4/run-test.py M01 --evidence
```

That command does not start a model or new attempt. It displays private operator
material: return only facts relevant to requested probes, never the entire
packet. Follow the incident controller and investigation limit. No real terminal
checks or configuration changes are authorized for these fictional incidents.

## P and L

P delegates to the existing practical launcher, including fresh fixtures,
the correct /lab mount and saved objective checker output. Its behavior is
unchanged. L does not launch Hermes or provision resources: it creates a record
marked INFRA_BLOCKED plus the selected live preparation brief. Start a live run
only under its separately prepared and tested infrastructure/authority contract.

## Logs

C/E/M attempts contain candidate-prompt.txt, launcher-record.json, an empty lab/
workspace and, when util-linux `script` is installed, hermes-terminal.log.
The transcript can contain ANSI/TUI control sequences; retain the native Hermes
exports for readable final review. If `script` is absent, the launcher records
terminal_transcript=false and native exports are required. No grading is done
during these runs. Keep logs private and send one tar.gz after testing.

`--prepare-only` creates a fresh prompt/run without launching Hermes or requiring
Podman. It is setup, not a model result. A prepared folder does not prove that a
model ran or that a no-tool instruction was obeyed.
