# Native Hermes evaluation exports — 2026-10-24

**Primary readable source records** for the tested Qwen 9B, Ministral 14B, Qwen 27B and Granite 4.1 8B sessions. These are reviewed derivatives of actual Hermes Markdown exports, not the earlier custom exporter reformatted to look native.

## source verification and coverage

- Received **156 native Markdown exports and four native manifests**, bundled as a Linux tar.gz archive. Source archive SHA-256: `6b49c83d51f48af7e89ccd1b38c98a7bbaafd0c02ebb328d4e32d474da7ade05`.
- Recomputed the complete-file SHA-256 for every original Markdown file: **156/156 matched its native manifest entry**. Session ID/path matching and message-count agreement between front matter and manifest also passed.
- Publish **147 reviewed files**: 40 Qwen 9B, 34 Ministral, 37 selected Qwen 27B evaluation/follow-up sessions and 36 Granite sessions. The nine early 27B setup/operational/personal sessions remain private, as in the prior recovery catalogue.
- Every native session maps to a previously supplied custom-export session. The two empty Qwen 9B sessions were intentionally excluded by the export command's nonempty-session selection. No test was rerun for this conversion.
- Native files include actual stored tool-call arguments/results where present, plus model/provider metadata, timestamps and exporter-reported counts. They can resolve evidence gaps left by the custom Markdown. A stored tool result is stronger than an assistant's self-report, but this remains historical evidence, not current live state.

## reviewed copies and checksums

Session IDs and hashed filenames are replaced with anonymous source aliases. Further redactions cover identifying home/login names, email addresses, SSH/credential-file locations, local/private endpoints and credential-shaped values. Explicit documentation-range fixture addresses remain. Original raw exports/manifests and the database are not published.

The native header/rendering is retained with added `publication_reviewed`, source-file checksum and editorial task metadata. The native verification footer is explicitly labeled **before publication review**. Its original body hash is retained as an exporter-reported source value; we did not independently reproduce that body-hash algorithm. It does **not** validate edited public text.

[reviewed-manifest.json](reviewed-manifest.json) supplies SHA-256 for each final reviewed public file, alongside the original complete-file hash verified before review. It is a review manifest, not an untouched native manifest. Body redactions can change literal commands, so these copies are not private execution fixtures ready to run.

## task and attempt indexing

Small-model screen tasks are 0–34; the earlier 27B roadmap uses a different task numbering scheme. Metadata labels are editorial and do not change prompt text. Shared sessions retain multiple task labels. Non-test greetings, incomplete inputs and failed readiness requests are retained with qualifications, not silently scored as successful model attempts. For 27B, an unassigned attempt remains null: inactive/replayed records are not automatically distinct attempts.

See [the earlier recovery catalogue](../../legacy/2026-10-24-prior-model-export-index.md) for 27B source-session mapping and [the Granite review](../../reviews/2026-10-24-granite-41-8b-screen.md) for shared-session/rerun details. Use separate [review findings](../../reviews/2026-10-24-model-inventory-and-ministral-screen.md) rather than treating any quoted claim as verified.

## new evidence resolved by native export

- Granite task 1: first call was `hostname && uname -a`; missing hostname stopped that command. The fallback was `cat /etc/os-release && uname -a`, returning Arch Linux and the hostname/kernel string. These support the local-only answer.
- Ministral task 1: tools ran `hostname` (failed) and `uname -a` (succeeded). The latter supports hostname/kernel. No `/etc/hostname` or OS-release read is recorded, so the answer's claimed hostname-file fallback is unsupported and Arch distribution identity was not established by those tools.
- This is still one preview of native format behavior plus a reviewed batch, not proof that Markdown retains every inactive/rewound row. Keep private native JSONL backups and the legacy recovery records for those distinctions. Timings derived from message timestamps are not model stopwatches.

## models

| Model group | Native files | Index |
| --- | --- | --- |
| qwen-9b | 40 | [qwen-9b](qwen-9b/README.md) |
| ministral-14b | 34 | [ministral-14b](ministral-14b/README.md) |
| qwen-27b | 37 | [qwen-27b](qwen-27b/README.md) |
| granite-41-8b | 36 | [granite-41-8b](granite-41-8b/README.md) |
