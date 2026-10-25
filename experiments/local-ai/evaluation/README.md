# homelab AI evaluation

**Current suite: homelab-ai-v4.0.** This is the active maintenance evaluation; earlier suites and results are historical material in the repository-level [archive](../../../archive/README.md).

| File | Use |
|---|---|
| [Download the tar.gz kit](homelab-ai-evaluation-v4-kit.tar.gz) | Transfer the complete kit to Aso without needing an existing checkout |
| [Archive checksum](homelab-ai-evaluation-v4-kit.tar.gz.sha256) | Verify the downloaded archive |
| [Catalog](v4/homelab-ai-evaluation-v4.md) | Full prompts, profiles, scope and evaluation sequence |
| [Kit instructions](v4/README.md) | Fixture setup, checks and candidate/evaluator separation |
| [Evaluator guide](v4/evaluator-guide.md) | Scoring protocol, task acceptance, fixed incident responses and live prerequisites |
| [Run template](v4/run-template.md) | Record model/runtime settings, first attempts, actions, results and interventions |
| [Individual prompts](v4/prompts/) | Give the candidate only one selected prompt at a time |

## Download on Aso

Run in a directory where you want the evaluation files:

```sh
curl -fL https://raw.githubusercontent.com/s-pollard/gusuku/main/experiments/local-ai/evaluation/homelab-ai-evaluation-v4-kit.tar.gz -o homelab-ai-evaluation-v4-kit.tar.gz
curl -fL https://raw.githubusercontent.com/s-pollard/gusuku/main/experiments/local-ai/evaluation/homelab-ai-evaluation-v4-kit.tar.gz.sha256 -o homelab-ai-evaluation-v4-kit.tar.gz.sha256
sha256sum -c homelab-ai-evaluation-v4-kit.tar.gz.sha256
tar -xzf homelab-ai-evaluation-v4-kit.tar.gz
cd homelab-ai-evaluation-v4
sha256sum -c SHA256SUMS
python3 -B selftest.py
```

If you already have a Gusuku checkout, update it with your normal Git workflow and use `experiments/local-ai/evaluation/v4/` directly. Do not discard local changes to update it.

## Interactive menu

Download the launcher scripts together into your existing v4 kit:

```sh
cd ~/homelab-ai-evaluation-v4
curl -fLO https://raw.githubusercontent.com/s-pollard/gusuku/main/experiments/local-ai/evaluation/evaluation-launchers.tar.gz
tar -xzf evaluation-launchers.tar.gz
python3 test-menu.py
```

Choose a numbered downloaded model or saved configuration; the menu scans the local GGUF directories automatically. Select reasoning by number or keep the configured default. Use R to refresh or N for a manual model ID/alias. Then select a task from the menu. The script displays the prompt, prepares the matching environment and starts fresh Hermes. Paste the prompt; after /quit you return to the menu and can select the next test. Use C/E/P/M/L for complete test sections, A for the full bank, K for Core24, S to change models, V for incident evidence, and Q to quit. The interactive test menu redraws in place. Use Up/Down and Enter, PgUp/PgDn to scroll, or : to type a task ID/number. It keeps your position when Hermes exits; press Enter after reviewing launcher output to return. Section shortcuts remain available. Noninteractive/dumb terminals retain the numbered text menu. Downloaded choices use filename-stem IDs with the existing provider; Hermes/backend acceptance must still be verified. Settings combinations are remembered privately; run folders and metadata are grouped by model/provider/reasoning. The chosen model is passed with --model, not merely used as a folder label. Unsupported CLI settings stop with an error. Native session evidence is still required to verify the serving backend.

The menu remembers and highlights the last selected test per model/settings group; Arrow-key mode keeps the highlighted selection; the fallback text menu suggests the next task. Candidate prompts are automatically sent to an available local clipboard tool or requested through OSC 52 over SSH. Terminal/multiplexer policy may block SSH copying; the prompt is always displayed for manual copying. Clipboard contents are never read. [Menu and launcher details](v4/launchers.md). The launcher tar.gz contains test-menu.py, run-test.py, run-practical.py, eval_clipboard.py, eval_save.py and export-runs.py; extract it in the existing kit. Earlier run folders are preserved. Optional chat titles remain manual; no /new is needed when starting from this menu. Live tasks still record INFRA_BLOCKED until their required infrastructure exists.

## One-command launchers

Install the complete six-file launcher update using the tar.gz commands above;
individual launcher downloads alone omit the required saving helper. The original
kit tar.gz remains unchanged.

Then use one command for a task:

```sh
python3 ~/homelab-ai-evaluation-v4/run-test.py C00
python3 ~/homelab-ai-evaluation-v4/run-test.py E01
python3 ~/homelab-ai-evaluation-v4/run-test.py P02
python3 ~/homelab-ai-evaluation-v4/run-test.py M01
```

Each opens a fresh session after displaying the candidate prompt; select the same model/settings and paste it. P uses the existing practical workflow. For C/E/M, terminal/file tools remain visible but their use is prohibited by the prompt; execution is routed to an offline empty sandbox. The run record captures this exposure policy and whether context-rule suppression was available. See [launcher instructions](v4/launchers.md) for setup, log locations, optional titles, and comparison limits.

For an M incident, view evaluator evidence in another Aso terminal:

```sh
python3 ~/homelab-ai-evaluation-v4/run-test.py M01 --evidence
```

Return only facts relevant to the model's requested probes. Do not paste the whole evaluator packet. L tasks only save an INFRA_BLOCKED preparation brief; the launcher does not provision live infrastructure.

## Start testing

1. Record the exact model, quantization, client/agent, serving build, context/output limits, reasoning effort, tool policy and memory/skill exposure in the run template.
2. Start a fresh candidate session and paste `prompts/C00.txt`; preserve the first response. Repeat with C01 in a separate session.
3. Run the same complete Core24 profile for every compared configuration. Start with the evidence prompts if no disposable execution environment is ready, and report that partial coverage accurately.
4. For each E task, paste its complete individual prompt and save the answer. No tools are authorized. For each M incident, keep one continuous session and return only relevant fixed evidence from the evaluator guide for requested probes.
5. For each P task, generate a new run with `lab.py init`, expose only its candidate `lab/` directory as `/lab` in an isolated disposable environment, and supply `candidate-prompt.txt`. Keep the kit, baseline state and evaluator materials outside candidate access. Return the resulting lab files and review the trace plus `lab.py check` output.
6. Score with the evaluator guide and retain failed first attempts, separately labeled retries and operator intervention. Existing historical suites do not count as v4 coverage.

Core24 IDs:

```text
E01 E02 E03 E04 E07 E16 E19 E20
P01 P02 P05 P07 P09 P11 P22 P24 P25 P26
M01 M03 M05 M06 M07 M08
```

Controls C00/C01 are additional and unscored. All 70 tasks and the two controls have individual prompt files. An `objective_pass` checker result is supporting evidence, not a complete grade.

## Readiness

The supplied self-test passed 26 reference outcomes, rejected 26 untouched baselines and rejected 16 selected broken outcomes. This validates selected fixture/checker behavior; no AI model was evaluated. Candidate script behavior checks execute code and require caller-provided disposable isolation. Live modules L01–L08 require the separately prepared infrastructure in the evaluator guide; missing infrastructure is INFRA_BLOCKED. Aso and Fujigoko are not disposable test targets.


## Save and export v4 runs

Each attempt saves its prompt, model settings, UUID, timestamps, kit/prompt hashes,
lifecycle events and terminal transcript. Practical attempts also retain checker
results. util-linux `script` is required for recording. Menu statuses distinguish
prepared, started/unclosed, normally closed, interrupted, runtime/launcher errors
and infrastructure-blocked runs. Normally closed is not a verified pass. Native
Hermes session IDs and serving backend remain unverified; global history is not
copied into attempts.

After exiting active launchers, press U in the menu or run
`python3 -B export-runs.py`. A new tar.gz under ~/evaluation-exports/ includes all
evaluation attempts, an index and file checksums, with a separate archive checksum.
Symlinks/special files are excluded and listed. Started/unclosed attempts block
export pending inspection. Existing attempts and exports are never overwritten.


Local model selection now prefers section names from
~/.hermes/runtimes/llamacpp/presets.ini (under HERMES_HOME when set), showing
only presets whose model file exists. A configured preset file suppresses raw
filename choices; the model ID can differ from its filename. This reads names
and paths only and does not reload routers, edit presets or verify successful
model loading. Without a preset file, GGUF filename discovery remains a fallback.
Press D in model selection and enter a saved entry number to remove that menu
choice without deleting weights, links, runs or test history. Old saved IDs are
not silently rewritten: remove stale choices and select the registered ID.
