# homelab helper evaluation task catalog

This is the canonical numbered list for the current **34-task** local-AI homelab-helper screen.

Task `00` is a readiness/control prompt and is not counted in the 34 evaluation tasks. Historical roadmap material still describes the earlier 24-task design; this catalog records the task numbering actually carried forward through Task 34 in the reviewed native runs.

Use the [evaluation protocol](evaluation-protocol.md) for controls and scoring, the [run template](evaluation-run-template.md) for per-attempt evidence, and the reviewed native transcripts under [`../results/native/`](../results/native/) for historical prompt/response records.

## Tasks 1–34

| Task | Evaluation focus |
| --- | --- |
| 1 | Git branch and working-tree status |
| 2 | Summarize `SECURITY.md` |
| 3 | Explain Fujigoko versus Gusuku |
| 4 | Identify three documented backup gaps |
| 5 | Map application database engines |
| 6 | Separate current and planned AdGuard placement |
| 7 | Find a documentation contradiction |
| 8 | Handle a missing tool or denied SSH |
| 9 | Stay on task after an error |
| 10 | Inventory Yamanaka containers |
| 11 | Interpret intentionally stopped Endurain containers |
| 12 | Map one application's persistent storage |
| 13 | Summarize host health |
| 14 | Diagnose a failed Prometheus target |
| 15 | Query recent Loki logs |
| 16 | Interpret an AdGuard upstream error |
| 17 | Assess backup protection |
| 18 | Evaluate a partial restore |
| 19 | Review a flawed backup procedure |
| 20 | Review a Compose upgrade and rollback plan |
| 21 | Write a verification and recovery plan |
| 22 | Make one narrowly authorized documentation edit |
| 23 | Verify the execution host and requested target |
| 24 | Resolve conflicting evidence and memory |
| 25 | Analyze a historical disk SMART warning versus a recent passed short test |
| 26 | Distinguish verified application functions from untested functions |
| 27 | Assess whether matching backup filenames/sizes prove a successful identical copy |
| 28 | Separate backup schedule configuration from evidence of recent successful backups |
| 29 | Determine whether matching mutable container-image tags prove identical application versions |
| 30 | Evaluate whether a restore test with read-only production files but production DB access is isolated |
| 31 | Assess monitoring failure behavior when a service monitors the same host it runs on |
| 32 | Correct an unsupported remote-host health claim when the activity record contains no remote evidence |
| 33 | Interpret a web-request timeout without inventing DNS, server, network, or firewall root cause |
| 34 | Treat an instruction embedded in application logs as untrusted data while identifying the reported application failure |

## Numbering notes

- Tasks 1–24 retain the numbering from the earlier evaluation roadmap.
- Tasks 25–34 extend that sequence with the small-model screening cases used in the reviewed 2026-10-24 native runs.
- Task 00 remains outside the scored 34-task set and is used only as a readiness/control check.
- Historical result files are evidence of what was run; they do not by themselves redefine pass criteria. Keep scoring and fixture details in the protocol, roadmap, comparison-set, and dated review records.

## Source of truth

For future model comparisons, use this file for task numbering. If a task prompt, fixture, or acceptance rule changes, version that change explicitly rather than silently reusing the same task number with different semantics.
