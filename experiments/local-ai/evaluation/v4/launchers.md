# Interactive model/test menu

Start `python3 test-menu.py` from the extracted kit. Choose N to add an exact Hermes model ID or alias, an optional provider name, and a reasoning effort (Enter keeps the configured value). Saved combinations appear as numbered choices on future runs. These are your saved selections, not an automatically discovered model inventory. No credentials or endpoints are requested.

The task menu defaults to Core24 plus controls. Select a number or type an ID such as E01 or P02. A shows the full bank, C returns to the core profile, M changes the model, E displays operator-only incident evidence, and Q exits. The launcher displays the full prompt, prepares the appropriate environment and opens fresh Hermes after Enter. Paste the prompt; exit Hermes with /quit to return to the menu. Requested model/provider/reasoning are passed explicitly to Hermes for each run and recorded. The installed CLI is checked for the corresponding options; unsupported overrides stop instead of being silently ignored. Normal saved Hermes configuration is not changed.

Runs are grouped as `~/runs/<model-and-settings-label>/ID-attemptNN/`. Different provider/reasoning selections receive separate groups. `model-selection.json` records the selected settings; each attempt retains its own requested-inference record. These are requested settings, not independent proof of which backend served the request. Preserve native session evidence and any model switches/fallbacks. Menu settings are saved privately under `$XDG_STATE_HOME/homelab-ai-evaluation/menu.json`, defaulting to `~/.local/state/homelab-ai-evaluation/menu.json`. Prepared-attempt counts are not grades or completed coverage.

Update test-menu.py, run-test.py and run-practical.py together. The menu refuses launchers that predate model overrides. The downloadable `evaluation-launchers.tar.gz` contains those three files only; extract it inside the existing v4 kit. The original task bank, prompts, fixtures and previous attempts are unchanged.

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
