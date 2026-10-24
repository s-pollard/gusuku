# local AI homelab maintenance evaluation

The active evaluation is **homelab-ai-v4.0**: local AI assistance for maintaining Fujigoko, tested through disposable Gusuku experiments and rehearsals. Aso can prepare fixtures and run text evaluations; it remains a personal administration workstation. Practical candidate execution requires a separate isolated disposable environment.

Start with the [v4 evaluation instructions](evaluation/README.md).

| Find | Location |
|---|---|
| Downloadable kit for Aso | [homelab-ai-evaluation-v4-kit.tar.gz](evaluation/homelab-ai-evaluation-v4-kit.tar.gz) |
| Complete task catalog | [v4 catalog](evaluation/v4/homelab-ai-evaluation-v4.md) |
| Individual candidate prompts | [v4 prompts](evaluation/v4/prompts/) |
| Fixture generator and checker | [v4 kit instructions](evaluation/v4/README.md) |
| Evaluator protocol, answers and incident evidence | [evaluator guide](evaluation/v4/evaluator-guide.md) — keep outside candidate access |
| Settings, evidence and scoring record | [run template](evaluation/v4/run-template.md) |
| Frozen sources and verification limits | [source snapshot](evaluation/v4/source-snapshot.md) |

V4 contains 70 scored tasks and two unscored controls. Begin matched model comparisons with **Core24**; Offline62 extends offline coverage. Live8 consists of preparation contracts for separately provisioned disposable systems, not ready-made infrastructure.

The previous local-AI setup material, tests, transcripts and reviews are in the repository-level [archive](../../archive/README.md). Their original answers remain historical evidence. They do not supply scores or coverage for v4; task numbers and semantics must be matched to their exact suite version.

Fujigoko is production. Required home services and recovery must keep working without Gusuku, Aso or the AI assistant. Useful experiments graduate by deliberate redeployment to an appropriate Fujigoko system. Follow [SECURITY.md](../../SECURITY.md); operational identifiers, credentials, raw private logs and model session databases stay private.
