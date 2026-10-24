---
session_id: "ministral-14b-S03"
title: "Recoverability risk for Oct 24 backup"
source: "local"
created_at: "2026-10-24T15:30:14.548675Z"
updated_at: ""
ended_at: "2026-10-24T15:30:41.605192Z"
model: "Ministral-3-14B-Instruct-2512-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 2
tool_call_count: 0
format: "md"
exported_at: "2026-10-24T18:10:30.621702Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "1346a79ff01330d487727d92ea937cc6b8300a03eb90be1ac63f9af2570c81ad"
task_namespace: "small-model-screen"
task_attempts: [{"task": 3, "attempt": 1}]

---

# Recoverability risk for Oct 24 backup

Session ID: `ministral-14b-S03`

Source: `local`

## Messages

### User — 2026-10-24T15:30:15.176164Z

Analyze only this fictional backup record. No tools, memory,
skills, outside information, or changes.

Current time: 2026-10-24 12:00 UTC
Local database export: 2026-10-24 11:00 UTC
Latest independent off-host copy: 2026-10-21 10:00 UTC
Restore test: no result recorded
File/database consistency: not checked

Is the application proven recoverable? How old is the off-host copy?
What protection is established, and what remains unknown?

Under 100 words. Do not equate “no recorded test” with “never tested.”


### Assistant — 2026-10-24T15:30:16.929462Z

**Recovery status:**
Unproven—no recorded restore test.
**Off-host copy age:**
5 days old (2026-10-21 10:00 UTC).
**Protection:**
Exists (off-host copy), but inconsistent and untested. Unknown: integrity, accessibility, and whether the 11:00 export supersedes it.

## Original export verification — before publication review

- Session id: `ministral-14b-S03`
- Exported messages: `2`
- Source DB message count at export: `2`
- Exported at: `2026-10-24T18:10:30.621702Z`
- Source-reported SHA256 of original exported body: `c6934c9430b8a6be737757d083cd26ca88c469a3b66935e66d76de725c2b2f0c`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
