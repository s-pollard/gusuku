# local AI homelab maintenance evaluation — archived

> **Archived 2026-10-25.** This evaluation is no longer active. The model-selection phase closed with **Qwen3.8-27B-UD-Q4-K-M** selected for the homelab-helper role. This directory is retained as historical evaluation material and should not be treated as the current operating plan.

**homelab-ai-v4.0** evaluated local AI assistance for maintaining Fujigoko through disposable Gusuku experiments and rehearsals. Aso could prepare fixtures and run text evaluations; it remained a personal administration workstation. Practical candidate execution required a separate isolated disposable environment.

The original v4 material is preserved below.

| Find | Location |
|---|---|
| Downloadable kit for Aso | [homelab-ai-evaluation-v4-kit.tar.gz](evaluation/homelab-ai-evaluation-v4-kit.tar.gz) |
| Complete task catalog | [v4 catalog](evaluation/v4/homelab-ai-evaluation-v4.md) |
| Individual candidate prompts | [v4 prompts](evaluation/v4/prompts/) |
| Fixture generator and checker | [v4 kit instructions](evaluation/v4/README.md) |
| Evaluator protocol, answers and incident evidence | [evaluator guide](evaluation/v4/evaluator-guide.md) — keep outside candidate access |
| Settings, evidence and scoring record | [run template](evaluation/v4/run-template.md) |
| Frozen sources and verification limits | [source snapshot](evaluation/v4/source-snapshot.md) |

V4 contains 70 scored tasks and two unscored controls. Its original comparison design began with **Core24**; Offline62 extended offline coverage. Live8 consisted of preparation contracts for separately provisioned disposable systems, not ready-made infrastructure.

Earlier local-AI setup material, tests, transcripts, and reviews are elsewhere under [`archive/local-ai/`](../). Their original answers remain historical evidence. Task numbers, scores, and semantics are meaningful only in the exact suite and model configuration that produced them.

Fujigoko is production. Required home services and recovery must keep working without Gusuku, Aso, or the AI assistant. Follow the repository [SECURITY.md](../../../SECURITY.md); operational identifiers, credentials, raw private logs, and model session databases stay private.
