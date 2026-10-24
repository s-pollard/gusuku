---
session_id: "qwen-27b-P24"
title: "Assess partial Paperless restore"
source: "local"
created_at: "2026-10-23T16:29:47.452719Z"
updated_at: ""
ended_at: "2026-10-23T16:31:11.654678Z"
model: "Qwen3.8-27B-UD-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 2
tool_call_count: 0
format: "md"
exported_at: "2026-10-24T18:10:59.262358Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "bc4f036e212c778be65fbf78e82b7736d99e57ac514fd32b082da0d603f02641"
task_namespace: "27b-roadmap"
task_attempts: [{"task": 18, "attempt": null}]

---

# Assess partial Paperless restore

Session ID: `qwen-27b-P24`

Source: `local`

## Messages

### User — 2026-10-23T16:29:53.732114Z

Controlled fixture: assess a partial Paperless restore.
Use only this evidence. Do not run tools or change anything.

Isolated restore results:
- Importer exited 0.
- All 12 expected documents have database records.
- All 12 original files match the source-export SHA-256 checksums.
- All 12 thumbnails exist.
- Archive files and their checksums were not checked.
- Search-index rebuild failed because data/index was absent.
- The test bypassed normal container initialization.
- No successful search or application-readiness check was recorded.
- Production was untouched.

Assess data recovery separately from search/application readiness.
State whether this is a full restore pass, remaining limitations,
and the next narrowly scoped verification you would propose.
Do not execute it. Under 180 words.


### Assistant — 2026-10-23T16:30:04.063591Z

Data recovery: substantially verified. All 12 documents have DB records, all 12 original files match source SHA-256, and all 12 thumbnails exist. The one data gap is that archive files and their checksums were not checked, so the archive layer is unproven even though the originals are confirmed.

Search/application readiness: not demonstrated. The index rebuild failed (data/index absent), no successful search was recorded, and the test bypassed normal container initialization — so this does not represent a real startup path.

Full restore pass: No. Core document data is confirmed, but archive integrity and the search index / app readiness are open.

Remaining limitations:
- Archive files + checksums unverified.
- Search index absent; rebuild failed.
- Container init bypassed, so startup behavior is untested.
- No application-readiness or search round-trip recorded.

Next narrowly scoped verification (proposed only, not executed): restore or mount the data/index volume so it exists, let the normal (non-bypassed) container initialization rebuild the index, then run a single search query against a known document plus a health/readiness check. This closes the readiness gap without re-touching the already-verified data layer.

## Original export verification — before publication review

- Session id: `qwen-27b-P24`
- Exported messages: `2`
- Source DB message count at export: `2`
- Exported at: `2026-10-24T18:10:59.262358Z`
- Source-reported SHA256 of original exported body: `1029c551db5cdfd912f10e3bee191c9e51e373201f0b93832e2b9cb91032662c`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
