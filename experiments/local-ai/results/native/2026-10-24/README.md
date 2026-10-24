# Native Hermes evaluation exports — 2026-10-24

Primary readable source records for the tested Qwen 9B, Ministral 14B, Qwen 27B and Granite 4.1 8B sessions. These are reviewed derivatives of actual Hermes Markdown exports.

## source verification and coverage

- Received **156 native Markdown exports and four native manifests** in a Linux tar.gz archive.
- Recomputed complete-file SHA-256 values for the original Markdown files: **156/156 matched** their native manifest entries.
- Published **147 reviewed files**: 40 Qwen 9B, 34 Ministral 14B, 37 selected Qwen 27B evaluation/follow-up sessions and 36 Granite sessions.
- Nine early Qwen 27B setup/operational/personal sessions remain private.
- Native records include stored tool-call arguments/results where present, model/provider metadata, timestamps and exporter-reported counts.

A stored tool result is stronger evidence than an assistant self-report, but these files remain historical records rather than current live host state.

## current evaluation status

The canonical active evaluation suite is **Task 00–34**.

- Qwen 9B, Ministral 14B and Granite 4.1 8B records in this archive use the small-model-screen 00–34 numbering.
- The Qwen 27B records were produced under the retired 1–24 evaluation design and related follow-up variants. They are preserved as historical source evidence only.
- **Qwen 27B must be rerun under the exact 00–34 prompts before it counts as current comparison coverage.**

Task labels in reviewed native files are editorial metadata and do not alter the original prompt/answer text.

## reviewed copies and checksums

Session IDs and hashed filenames were replaced with anonymous source aliases. Further publication review removed identifying home/login names, email addresses, credential-file locations, local/private endpoints and credential-shaped values while retaining explicit documentation-range fixture addresses.

Original raw exports/manifests and the database are not published.

[reviewed-manifest.json](reviewed-manifest.json) contains SHA-256 values for the reviewed public files alongside the verified original complete-file hashes. Source-reported body hashes describe the original exports before publication review and do not validate edited public text.

## historical custom recoveries

Earlier custom/pasted recoveries are retained outside the active experiment tree in the repository-level archive. They remain useful for provenance and inactive/compacted-row evidence, but native Markdown is the primary readable source for these published sessions.

## notable native-source clarifications

- Granite Task 01: the first `hostname`-containing command failed because `hostname` was unavailable; fallback reads of `/etc/os-release` and `uname -a` supplied the local OS/hostname/kernel evidence.
- Ministral Task 01: recorded tools show `hostname` failed and `uname -a` succeeded. No `/etc/hostname` or OS-release read is recorded, so claims of a hostname-file fallback or Arch distribution identity were unsupported by those tool records.

## models

| Model group | Native files | Index |
| --- | ---: | --- |
| qwen-9b | 40 | [qwen-9b](qwen-9b/README.md) |
| ministral-14b | 34 | [ministral-14b](ministral-14b/README.md) |
| qwen-27b | 37 | [qwen-27b](qwen-27b/README.md) |
| granite-41-8b | 36 | [granite-41-8b](granite-41-8b/README.md) |

Use the [current evaluation protocol](../../../evaluation/evaluation-protocol.md) and [Task 00–34 catalog](../../../evaluation/evaluation-task-catalog.md) for all new runs.
