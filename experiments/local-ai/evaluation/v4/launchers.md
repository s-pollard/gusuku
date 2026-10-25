# Test launchers

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
