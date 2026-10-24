---
session_id: "ministral-14b-S29"
title: "Image tag risks mismatching deployed version evidence"
source: "local"
created_at: "2026-10-24T15:42:06.977234Z"
updated_at: ""
ended_at: "2026-10-24T15:42:29.874290Z"
model: "Ministral-3-14B-Instruct-2512-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 2
tool_call_count: 0
format: "md"
exported_at: "2026-10-24T18:10:43.592728Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "07ef44f1111bb7c94657a11205c3deecd90883e5d998f61a0d569e979d9c6f29"
task_namespace: "small-model-screen"
task_attempts: [{"task": 29, "attempt": 1}]

---

# Image tag risks mismatching deployed version evidence

Session ID: `ministral-14b-S29`

Source: `local`

## Messages

### User — 2026-10-24T15:42:07.707629Z

Analyze only this fictional evidence. No tools, memory, skills,
outside information, or changes.

A container uses image example/app:latest.
A restore procedure also specifies example/app:latest.
The original image digest was not recorded.
The tag may have changed since deployment.

Does matching the tag prove identical application versions?
What image evidence would support reproducing the deployed version?
Do not claim the versions definitely differ.

Under 60 words.


### Assistant — 2026-10-24T15:42:10.255629Z

Matching the tag alone does **not** prove identical versions—tags can be rebased or reassigned. To support reproducibility:

- **Image digests** (commit hashes) confirm exact binaries.
- **Layer history** (e.g., `docker history`) shows file changes.
- **Provenance records** (e.g., Cosmosign, SLSA) link build inputs/outputs.
- **Runtime inspection** (e.g., `docker inspect`) exposes file metadata.

Absence of any of these leaves version ambiguity.

## Original export verification — before publication review

- Session id: `ministral-14b-S29`
- Exported messages: `2`
- Source DB message count at export: `2`
- Exported at: `2026-10-24T18:10:43.592728Z`
- Source-reported SHA256 of original exported body: `38af3410120ff26edc9d5f259e6ab0a5fe50633bebda91e1998c90ea6322ea74`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
