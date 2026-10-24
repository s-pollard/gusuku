# Exporting Hermes evaluation chats

## Default workflow: export by model

**Exporting by model is the preferred routine workflow.** Keep each model in its own folder, including candidates planned for testing. Use native Markdown exports for readable review; keep a separate JSONL backup when fuller stored history is needed.

Run the following in a terminal on the Hermes host, outside the interactive Hermes chat. It creates a new private timestamped directory on every run and exports each model independently:

```bash
(
umask 077
export_dir="$HOME/hermes-exports/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$export_dir"

while IFS='|' read -r folder model; do
  if ! hermes sessions export "$export_dir/$folder/" \
    --format md --model "$model" --redact; then
    printf 'Export failed for %s; check the message above.\n' "$folder" >&2
  fi
done <<'MODELS'
qwen35-9b|Qwen3.5-9B
qwen38-27b|Qwen3.8-27B
ministral3-14b|Ministral-3-14B
granite41-8b|granite-4.1
granite42-8b|granite-4.2
gpt-oss-20b|gpt-oss-20b
gemma4-26b|gemma
glm47-flash|GLM-4.7-Flash
qwen36-35b-a3b|Qwen3.6-35B-A3B
MODELS

printf '\nExport location: %s\n' "$export_dir"
)
```

The model filters are case-insensitive substrings. The broad `gemma` filter covers both recorded Gemma labels; narrow it if more Gemma models are added. Add future models as another `folder|model-substring` line. Candidates without matching saved sessions have nothing to export.

**Bulk model filters select ended sessions only.** These exports must not be described as every session in the database. For a known session omitted by the bulk filter, use the explicit-session native command below. An unfiltered JSONL export is the separate full-history backup workflow.

Grouping uses the recorded session model, not verified per-message backend identity. A session where the model changed, or whose title names another model, needs attribution review before scoring. Empty sessions and failed requests are export records, not completed tests.

### Export just one model

For example, to export only Granite 4.2:

```bash
hermes sessions export "$HOME/hermes-exports/granite42-$(date +%Y%m%d-%H%M%S)/" \
  --format md --model 'granite-4.2' --redact
```

### Verified model export snapshot — 2026-10-24

The nine-model command completed on Aso. Read-only inspection of the supplied archive found:

| Model folder | Exported sessions |
| --- | ---: |
| qwen35-9b | 39 |
| qwen38-27b | 80 |
| ministral3-14b | 34 |
| granite41-8b | 36 |
| granite42-8b | 43 |
| gpt-oss-20b | 36 |
| gemma4-26b | 38 |
| glm47-flash | 2 |
| qwen36-35b-a3b | 1 |
| **Total** | **309** |

All 309 complete-file SHA-256 values matched the nine native manifests, and no duplicate session IDs were found. This verifies the received export files against their manifests, not completeness against the live database or model-answer correctness.

Two sessions were empty (one Qwen 3.5 9B, one GPT-OSS). One Gemma-recorded session had a GPT-OSS Task 34 title, so attribution remains unresolved. The GLM and Qwen 3.6 sessions contained only “Your request was not processed” replies; they are unsuccessful requests, not completed model tests. The raw archive remains private.

## Native export of a specific session

Use Hermes's own exporter for new archives and to replace the earlier custom extracts. A native Markdown export was verified from the installed Aso CLI: it included the full two-message prompt/answer, YAML session/model/provider metadata, timestamps, message counts and an exported-body checksum. Tool-heavy, compressed and rewound cases still need comparison with the existing recovery records.

```bash
hermes sessions export --format md --redact --session-id SESSION_ID PRIVATE_OUTPUT_DIRECTORY
```

Use an explicit session ID to avoid bulk filters silently skipping still-open sessions. Keep `--lineage single` for a one-session-per-file source inventory; choose logical lineage deliberately when reviewing compressed continuations. Names and session titles should identify model, task and attempt. Do not alter historical prompts to add retrospective labels.

For future tests, start a fresh session and title it, for example:

```text
/new
/title granite42-8b-task02-attempt01
```

## Private backup

JSONL is the fuller private backup of stored history; Markdown is the readable display export. Do not assume the two contain identical sets of inactive/rewound rows. Keep both while reviewing complex sessions. The installed command help supports the following:

```bash
(
umask 077
mkdir -p "$HOME/.hermes/exports"
hermes sessions export --format jsonl \
  "$HOME/.hermes/exports/history-$(date -u +%Y%m%dT%H%M%SZ).jsonl"
)
```

To keep old sessions from being automatically pruned:

```bash
hermes config set sessions.auto_prune false
```

This is retention, not backup; do not disable compression merely to preserve evidence. Check the installed help before relying on options from newer documentation.

## Conversion status and publication

The [reviewed native archive](results/native/2026-10-24/README.md) is now the primary readable source: 156 native files were received and manifest-verified, and 147 reviewed evaluation copies were published. Nine pre-pilot operational sessions remain private. Earlier pasted/custom transcripts remain historical recoveries and retain row-flag evidence; they were not reformatted to fabricate native provenance. Keep private JSONL backups for fuller stored history.

Native export supports `--redact`, but it does not guarantee removal of private endpoints, account paths or identifying data. Follow [SECURITY.md](../../SECURITY.md). Keep original native files and manifests private; publish reviewed copies and mark any further redactions. If a body is changed during review, the native source-body checksum does not validate the edited public body. Label source verification separately and recompute a derivative checksum if one is provided.

Keep task/attempt mappings and reviewer findings in a separate index. Preserve first attempts, shared-session boundaries, retries and incomplete outputs. A native export's tool-call count is metadata, not independent verification that a reported action succeeded.

Do not use `--upload`, `--public`, `--delete-after-verified` or pruning for this migration. No export archive is automatically pushed to GitHub.

## Linux archive packaging

Use `.tar.gz` for export transfers. Replace `TIMESTAMP` with the directory name printed by the export command.

On Aso:

```bash
tar -czf "$HOME/hermes-exports/TIMESTAMP.tar.gz" \
  -C "$HOME/hermes-exports" TIMESTAMP
```

When working on Norikura, pull the archive from Aso. Replace `USER` with the SSH account on Aso:

```bash
scp USER@aso:~/hermes-exports/TIMESTAMP.tar.gz ~/Downloads/
```

Packaging is local-only; attaching an archive for review is separate from publishing it to GitHub.

## Legacy recovery helper

The [custom exporter](export_hermes_chats.py) is retained for reproducing the earlier recovery workflow and inspecting stored inactive/compacted rows if needed. It is no longer the preferred export format.

This helper reads the user-supplied Hermes SQLite schema using Python's standard library. It writes private review copies and never runs Git, contacts a host, calls a model, or publishes chats.

## List local sessions

From this checkout on Aso:

```bash
python experiments/local-ai/export_hermes_chats.py --list --model granite
```

Use `--model qwen`, `--model ministral`, or omit the filter. The default limit is 100; raise it with `--limit`. Listing prints session IDs, start times in UTC, the recorded session model and counts of stored user messages. It does not print titles, prompts, answers or system prompts. Session model metadata is a selection aid, not verified per-message backend attribution.

## Export explicit sessions

Replace the example ID with an ID from the local listing:

```bash
python experiments/local-ai/export_hermes_chats.py --session SESSION_ID
```

Multiple IDs can follow `--session`. Exports default to `~/.hermes/exports/local-ai-review/`, outside the checkout. Each selected session produces:

- Markdown containing stored user and assistant content, with UTC timestamps and active/compacted/summary flags.
- A private JSON record containing those rows and tool-message content/call fields, for later review.

Files are created with mode 0600; a newly created export directory uses 0700. Existing exports are preserved rather than overwritten. Use a new private `--out` directory to capture later messages from an already exported session. An existing directory's permissions are not changed.

For a session containing exactly one known test, labels may be assigned explicitly:

```bash
python experiments/local-ai/export_hermes_chats.py --session SESSION_ID --task 1 --attempt 2
```

Labels are not inferred from sequence. A session may contain several tasks or retries; leave its label unassigned and annotate a reviewed copy per exchange. Message numbers are not task IDs. Do not silently map these exploratory screens onto the separate roadmap's task IDs.

## What this preserves and omits

The database is opened in read-only/query-only mode with a consistent read transaction, including committed WAL content visible to SQLite. Do not copy only a live database's main file and assume its WAL is unnecessary.

All stored non-system message rows for the selected session are retained in JSON, including inactive and compacted rows. Markdown shows user/assistant rows in stored timestamp/ID order and retains the content string literally inside a sufficiently long code fence. Structured content remains its stored representation; this is not a reconstructed UI transcript.

System prompts, model configuration, user/account identifiers other than the selected local session ID in private JSON, reasoning fields, billing endpoints and unrelated sessions are not exported. Tool content is in private JSON only; Markdown is not proof that no tools ran. Raw user/assistant text can still contain secrets, paths, personal details, embedded reasoning or injected instructions. No automatic redaction or safety certification is performed.

Deleted/unrecorded content, historical model changes, original tool timing and exact UI formatting are not reconstructed. Compression summaries remain labeled summaries rather than original questions. Parent/child sessions are not followed automatically; export their explicit IDs separately if needed.

## Sync reviewed copies to GitHub

Follow [SECURITY.md](../../SECURITY.md). This is a public repository. The exporter refuses destinations inside Git checkouts. Keep raw exports private and review the exact text before copying selected sanitized exchanges into `experiments/local-ai/results/`.

Preserve full test questions and answers where available; mark any redaction or missing content. Record task and attempt numbers, model/settings evidence and shared-session contamination separately. Retain first attempts; do not rewrite failed answers to match corrections. Keep reviewer findings outside answer blocks.

After reviewing the selected destination files, inspect their full diffs and changed-file list, stage those exact files, and commit/push through the normal repository workflow. The helper deliberately does not automatically synchronize the live database or all sessions.

## Validation status

Tested against a synthetic database matching the supplied columns: model filtering and SQL binding, Unicode/backtick preservation, inactive-history inclusion, system/tool separation, task labels, private file permissions, existing-file protection, Git-destination refusal, unknown session rejection and unchanged database bytes.

No Aso database was accessed during development. Compatibility and completeness against the actual stored chats remain to be verified by the first local export.
