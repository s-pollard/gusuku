---
session_id: "qwen-27b-P25"
title: "Review flawed paperless-ngx backup procedure"
source: "local"
created_at: "2026-10-23T16:31:11.661125Z"
updated_at: ""
ended_at: "2026-10-23T16:34:59.809094Z"
model: "Qwen3.8-27B-UD-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 2
tool_call_count: 0
format: "md"
exported_at: "2026-10-24T18:10:59.773793Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "a8ee180f83442558ea72728531ddd488930463dc782ba943ec80d1ff93e4ea06"
task_namespace: "27b-roadmap"
task_attempts: [{"task": 19, "attempt": null}]

---

# Review flawed paperless-ngx backup procedure

Session ID: `qwen-27b-P25`

Source: `local`

## Messages

### User — 2026-10-23T16:31:16.103697Z

Controlled fixture: review this flawed backup procedure.
Analyze only; do not execute commands or change anything.

Requirements:
- Export only after the production app has successfully stopped.
- Use the same image version as the deployed app.
- Isolate the exporter from production data and networks.
- Confirm the exporter has exited before restarting production.

Proposed script:

#!/bin/sh
docker stop paperless-ngx
docker run -d --name paperless-export \
  --network host \
  -v /srv/docker/paperless/data:/usr/src/paperless/data \
  -v /srv/docker/paperless/media:/usr/src/paperless/media \
  -v /srv/docker/paperless/export:/usr/src/paperless/export \
  ghcr.io/paperless-ngx/paperless-ngx:latest \
  document_exporter /usr/src/paperless/export
docker start paperless-ngx

Identify stop-failure handling, image selection, mount isolation,
and restart-ordering problems. Flag any requirement that needs
clarification before a safe replacement can be designed.
Do not write a replacement script. Under 220 words.


### Assistant — 2026-10-23T16:32:27.216790Z

Four problems:

1) Stop-failure: `docker stop` exit code is unchecked, no `set -e`. A missing container, a still-running app, or one that hangs past the 10s SIGTERM window (then force-killed, risking unflushed writes) all proceed to export and restart. No state check, no `--timeout`, no abort.

2) Image: pinned to `:latest`, a moving tag, never read from the deployed container — the exporter can run a different version than production. Must use the same tag/digest.

3) Isolation: `--network host` exposes the exporter to prod networks. `data` and `media` are read-write by default, so the exporter can mutate production data; these need `:ro`.

4) Restart ordering: `docker run -d` detaches; nothing waits for the export. `docker start` fires while the exporter is still running. Need `docker wait` + exit-code check first. `--name` also collides with a stale container from a prior failed run (no cleanup).

Clarify before designing:
- Is the deployed app pinned by digest or tag? Define "same version."
- Does "isolate from production data" mean read-only only, or also network/filesystem separation? Can the exporter use `--network none`?
- Is the host bind dir `/srv/.../export` an acceptable isolated target, or must it live on separate storage?

## Original export verification — before publication review

- Session id: `qwen-27b-P25`
- Exported messages: `2`
- Source DB message count at export: `2`
- Exported at: `2026-10-24T18:10:59.773793Z`
- Source-reported SHA256 of original exported body: `64cfe1f084a81d8e5de1125944509afb58199f37007cf79ee65d20c56d2c06d9`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
