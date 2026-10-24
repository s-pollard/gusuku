---
session_id: "qwen-27b-P17"
title: "Map Paperless persistent storage snapshot"
source: "local"
created_at: "2026-10-23T16:16:18.793476Z"
updated_at: ""
ended_at: "2026-10-23T16:18:07.070191Z"
model: "Qwen3.8-27B-UD-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 2
tool_call_count: 0
format: "md"
exported_at: "2026-10-24T18:10:55.755562Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "1baf05a46fad7025458dfb18e508d02a56228fc208d656a2c54e979df825e1b7"
task_namespace: "27b-roadmap"
task_attempts: [{"task": 12, "attempt": null}]

---

# Map Paperless persistent storage snapshot

Session ID: `qwen-27b-P17`

Source: `local`

## Messages

### User — 2026-10-23T16:16:20.496348Z

Task 12: map Paperless persistent storage using only this supplied
snapshot. Do not run tools, access hosts, or change anything.

Report the host/container path mappings, mount types, and read/write
status. Distinguish bind mounts from Docker-managed named volumes.

Explain what the database settings establish and what remains unknown.
Unset environment variables alone do not prove the effective database
engine or database-file location. Propose the minimum additional
read-only evidence needed to establish those, without executing it.

Keep the answer under 250 words.

Snapshot timestamp: 2026-10-23T12:15:35-04:00
Container: paperless-ngx

Mounts:
Type=bind Source=/srv/docker/paperless/consume Destination=/usr/src/paperless/consume RW=true
Type=bind Source=/srv/docker/paperless/data Destination=/usr/src/paperless/data RW=true
Type=bind Source=/srv/docker/paperless/export Destination=/usr/src/paperless/export RW=true
Type=bind Source=/srv/docker/paperless/media Destination=/usr/src/paperless/media RW=true

Selected container environment variables:
PAPERLESS_DBENGINE=<not explicitly set>
PAPERLESS_DBHOST=<not explicitly set>
PAPERLESS_DBPORT=<not explicitly set>
PAPERLESS_DBNAME=<not explicitly set>


### Assistant — 2026-10-23T16:17:08.813875Z

Storage — four host-path bind mounts, all RW; no Docker-managed named volumes appear in the snapshot:

- /srv/docker/paperless/consume → /usr/src/paperless/consume (bind, RW)
- /srv/docker/paperless/data → /usr/src/paperless/data (bind, RW)
- /srv/docker/paperless/export → /usr/src/paperless/export (bind, RW)
- /srv/docker/paperless/media → /usr/src/paperless/media (bind, RW)

Every mount is a bind mount, not a named volume.

What the DB settings establish: PAPERLESS_DBENGINE, DBHOST, DBPORT, DBNAME are all unset, so no external-DB override is declared in the listed environment. Unset values alone do not prove the engine: the app could still default to SQLite, or a value could come from compose-level defaults. PAPERLESS_DATA_DIR is not in the selected subset, so the data-directory base (and hence the SQLite file path, if SQLite) is also unestablished. Effective engine and DB-file location both remain unknown.

Minimum additional read-only evidence (proposed, not executed):
1. Full environment: `docker inspect paperless-ngx` — read the complete Environment list, especially PAPERLESS_DATA_DIR and any PAPERLESS_DB*.
2. Compose source: `docker compose config` (or the .yml) — shows declared volumes (named vs bind) and env defaults.
3. Host listing: `ls -la /srv/docker/paperless/data` — locate a SQLite database file.
4. `docker inspect` Mounts — confirm no volume-type mounts exist.

These four, read-only, resolve both unknowns.

## Original export verification — before publication review

- Session id: `qwen-27b-P17`
- Exported messages: `2`
- Source DB message count at export: `2`
- Exported at: `2026-10-24T18:10:55.755562Z`
- Source-reported SHA256 of original exported body: `36dac4fa4bce74c63af6daeaf048adb56457cca97ce3bc805e2811b122012cd5`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
