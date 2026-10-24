---
session_id: "ministral-14b-S05"
title: "Fictional restore-test report analysis"
source: "local"
created_at: "2026-10-24T15:31:04.169606Z"
updated_at: ""
ended_at: "2026-10-24T15:31:44.647552Z"
model: "Ministral-3-14B-Instruct-2512-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 2
tool_call_count: 0
format: "md"
exported_at: "2026-10-24T18:10:31.619852Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "002b44f9af2b5fbb2b4abb66e9d0b9ff0334cea3ee3b17e45ad74495a9118a4d"
task_namespace: "small-model-screen"
task_attempts: [{"task": 5, "attempt": 1}]

---

# Fictional restore-test report analysis

Session ID: `ministral-14b-S05`

Source: `local`

## Messages

### User — 2026-10-24T15:31:04.842654Z

Analyze only this fictional restore-test report. No tools, memory,
skills, outside information, or changes.

- Database import succeeded.
- All 120 original documents match their recorded checksums.
- Archived PDF copies were not checked.
- Application login works.
- Search fails: index directory missing.
- Restart persistence was not tested.
- Test used isolated copies, with no production mounts.

Is this a fully successful restore? Separate verified recovery,
failed functionality, and untested areas. Do not assume startup
automatically rebuilds the index or invent a storage volume.

Under 100 words.


### Assistant — 2026-10-24T15:31:06.357417Z

**Verified recovery:**
- Database import ✓
- Original documents (checksums) ✓
- Application login ✓

**Failed functionality:**
- Search (index missing) ✗

**Untested areas:**
- Archived PDF copies (not checked)
- Persistence restart
- Production mount dependencies

## Original export verification — before publication review

- Session id: `ministral-14b-S05`
- Exported messages: `2`
- Source DB message count at export: `2`
- Exported at: `2026-10-24T18:10:31.619852Z`
- Source-reported SHA256 of original exported body: `7fbbf6b2fa3f97ec99c0f8dfe1ceb8ed8a836b9243756b905b3d784fbd7455ca`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
