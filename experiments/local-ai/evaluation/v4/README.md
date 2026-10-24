# Homelab AI evaluation v4

This kit tests whether a local AI configuration can help maintain **Fujigoko**, the deployed homelab. **Gusuku** is the experimental/learning environment and place for disposable trials before deliberate production redeployment. The catalog is grounded in the repository snapshots listed in source-snapshot.md and the operator explanation in this chat, with synthetic task data.

Start with the **Core24** profile and two controls. Full offline coverage is 62 tasks; eight additional live modules require separate infrastructure. No model has been graded by this kit.

| File | Purpose | Candidate exposure |
|---|---|---|
| homelab-ai-evaluation-v4.md | Complete catalog, scope and workflow | Give only the selected task and instructions |
| candidate-instructions.md | Shared context and mode contracts | Selected context/mode only |
| prompts/ID.txt | Ready-to-copy candidate prompts, including the controls | One selected prompt only |
| lab.py / fixtures.py / tasks.json | Evaluator fixture/prompt generation and limited checks | Keep hidden |
| evaluator-guide.md | Task acceptance, incident branches and live setup contracts | Keep hidden |
| selftest.py | Trusted reference results and selected checker regressions | Keep hidden |
| run-template.md | Settings, evidence, scoring and repeat comparison | Evaluator record |
| source-snapshot.md | Frozen repository provenance and technical references | Evaluator reference |
| validation-report.json | Kit QA result, not a model evaluation | Evaluator reference |
| SHA256SUMS | Packaged file identities | Evaluator reference |

## Offline preparation

For manual testing, use one ready-to-copy text from `prompts/`. Start with C00/C01, then the exact Core24 list in the catalog. Practical P prompts also require their generated candidate lab; text alone does not test execution.

Use Python 3 standard library, POSIX sh and Git. Do not install model packages or run services just to prepare these fixtures.

```sh
python3 -B selftest.py
python3 -B lab.py init P02 --run ../runs/v4-p02-attempt01
```

Init refuses to overwrite an existing run. Inside that run:

- `lab/` contains candidate inputs and permitted output locations.
- `candidate-prompt.txt` contains the exact shared context, mode and task.
- `evaluator-state.json` contains private baseline state; keep outside the candidate environment.

Expose only lab/ at `/lab` in a **prepared isolated disposable guest**, then give the generated prompt separately. No production mounts, credentials, Docker sockets or management-network access. Kit contents and evaluator state must stay outside candidate-visible storage/retrieval/memory. A working directory and a fresh conversation are not a sandbox. Aso is a personal workstation, not disposable infrastructure.

For evidence or simulated tasks, generate one prompt at a fresh path:

```sh
python3 -B lab.py prompt E19 --output ../runs/e19-candidate.txt
```

The parent output directory must exist. Return incident evidence using the evaluator guide's matching hidden packet; never dump the entire packet to the candidate.

## Verification

Run final-state checks after receiving the candidate directory back:

```sh
python3 -B lab.py check --run ../runs/v4-p02-attempt01
```

For P07/P08/P15 only, additional script behavior checks are available:

```sh
python3 -B lab.py check --run ../runs/v4-p07-attempt01 --behavioral
```

**Behavioral checks execute candidate-written code.** Run them only within the separately isolated disposable evaluation guest. The checker itself does not enforce filesystem/network/privilege isolation. It reports objective evidence; every task also needs trace review and human scoring. `objective_pass` is not a full task PASS. Missing reports or checker errors need diagnosis before blaming the evaluator or the model.

Live modules L01–L08 are task definitions and setup contracts, not provisioned infrastructure. Mark INFRA_BLOCKED until their exact prerequisites and independent acceptance probes are ready. Never substitute real production hosts or backups.

## Results

Use run-template.md. Record model+agent+runtime, exact artifact and fixture versions, scope, memory/skills exposure, real actions/results, failures, repeats, latency, resource usage and operator intervention. Retain failed first attempts. Keep technical accuracy, execution competence, framework failure and operational usefulness distinguishable.

The source repositories are read-only inputs to this deliverable. Adoption into Gusuku requires a deliberate index/protocol update; this kit does not change which suite its current main branch names canonical.
