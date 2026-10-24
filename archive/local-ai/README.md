# local AI administration experiments

Experiment records for local homelab-helper evaluation on Aso. These are Gusuku experiments, not production services or a declaration of current state on other homelab hosts.

## navigation

| Find | Folder / guide |
| --- | --- |
| Canonical Task 00–34 prompts | [Evaluation task catalog](evaluation/evaluation-task-catalog.md) |
| Current evaluation rules | [Evaluation protocol](evaluation/evaluation-protocol.md) |
| Per-attempt record format | [Run template](evaluation/evaluation-run-template.md) |
| Primary transcript evidence | [Native transcripts](results/native/README.md) |
| Reviewed model findings | [Reviews](results/reviews/README.md) |
| Hermes setup and lessons | [Hermes](agents/hermes.md) |
| Odysseus setup and lessons | [Odysseus](agents/odysseus.md) |
| Export / backup workflow | [Chat export](chat-export.md) |

## evaluation status

The **Task 00–34 small-model screen is the only active canonical evaluation suite**. Exact prompts are in the [task catalog](evaluation/evaluation-task-catalog.md).

The earlier 1–24 roadmap and tests are retired. Historical 1–24 results may be used to understand prior model/framework behavior, but they do **not** count as current comparison coverage. Any model previously tested only under 1–24 must be rerun with the exact 00–34 prompts before being compared as part of the current suite.

Current comparison rules:

- use a fresh chat for each task;
- preserve the first attempt and label retries separately;
- keep the prompt wording and evidence fixed across models;
- record model, quantization, runtime, reasoning setting, context/output budgets and memory/skill exposure when known;
- distinguish actual tool execution from supplied-output analysis;
- do not treat `/new` as proof that persistent memory/skills were cleared;
- do not turn missing evidence into a positive or negative conclusion;
- keep model correctness separate from framework/tool-routing failures;
- do not infer a winner from unmatched task sets or different runtime controls.

The reviewed native 2026-10-24 exports contain the primary readable evidence for Qwen 9B, Ministral 14B, Qwen 27B and Granite 4.1 8B sessions. Qwen 27B sessions that used the retired numbering remain historical source evidence and require 00–34 reruns for current comparison use. See the [native export index](results/native/2026-10-24/README.md).

## scope and boundary

All local-AI experiments, model tests, transcripts, tooling and evaluation plans in this tree belong to **Gusuku**.

Aso is the temporary execution workstation/test bed. Fujigoko is production. Fujigoko services must not depend on Aso, Hermes, Odysseus, or Gusuku experiments. If a lab experiment becomes genuinely useful for the home environment, it should be rebuilt deliberately on an appropriate Fujigoko system rather than turning Gusuku into a production dependency.

A local model is not an authority on host state. Distinguish:

- repository/documentation claims;
- direct tool results;
- user-supplied snapshots or fixtures;
- historical observations;
- assumptions or hypotheses.

Container readiness does not prove application correctness. Exporter availability does not prove disk health. A backup file or schedule does not prove recoverability. A successful login does not prove the rest of an application works.

## inference direction

Local inference is the intended deployment model for this experiment. Paid API inference is not the intended ongoing backend.

Evaluation should prioritize:

- reliable instruction following and tool calls;
- Linux, Docker, networking, monitoring and backup reasoning;
- strict production/test separation;
- evidence discipline and honest uncertainty;
- bounded output and completion;
- practical latency and context use;
- configurations that can plausibly fit future lower-power hardware without assuming VRAM fit proves model quality.

No model or GPU is selected solely by this documentation.

## observed Aso baseline

Historical shared setup observations during the first local runs:

| Component | Observed setup |
| --- | --- |
| Workstation | Aso; Arch Linux |
| CPU / RAM | Ryzen 7 7800X3D; 32 GB RAM |
| GPU | Radeon RX 7900 XTX; approximately 24 GiB VRAM |
| Initial large model | Qwen3.8-27B-UD-Q4_K_M |
| Inference | Hermes-managed llama.cpp Vulkan build b11671 during the recorded setup |
| Observed worker context | 65,536 during the recorded setup |

These are dated observations, not guarantees for later model sessions. Model picker labels, client context displays and configuration requests do not independently establish the backend or effective serving window for a particular request.

## evidence and repository workflow

Use [SECURITY.md](../../SECURITY.md). Keep credentials, key material, exact private endpoints, raw private logs, session databases and identifying operational details outside the public repository.

Native transcript exports are evidence. Do not rewrite failed answers to make them correct. Reviewer corrections belong in review files or indexes, while original prompt/answer records remain intact.

`main` is the shared accepted documentation branch. Use short-lived task branches or disposable worktrees when actual repository changes need review. Do not let two agents edit the same checkout concurrently.

## export workflow

Use Hermes native Markdown exports as the primary readable source and JSONL/private archives for fuller stored history where needed. See [chat-export.md](chat-export.md).

For a new evaluated task, use a fresh session and a title that identifies model, task and attempt, for example:

```text
/new
/title granite42-8b-task02-attempt01
```

Preserve first attempts, retries, shared-session contamination, incomplete outputs and tool evidence. Publication review may redact private information, but it must not alter the substantive model answer.

## next work

1. Run every candidate intended for comparison on the canonical Task 00–34 suite.
2. Redo Qwen 27B coverage under 00–34 rather than carrying forward old 1–24 results.
3. Keep settings and exposure as equivalent as practical across models and record the remaining differences.
4. Review each run against the same evidence rules and keep concrete errors separate from verbosity/style issues.
5. Use the resulting matched runs to decide which models deserve deeper tool-execution and homelab-helper testing.

No 1–24 result is grandfathered into the current comparison.
