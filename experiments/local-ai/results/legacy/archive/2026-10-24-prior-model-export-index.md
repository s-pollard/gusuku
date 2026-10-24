# Recovered prior-model chats — 2026-10-24

**Superseded for primary reading by the [reviewed native Hermes archive](../native/2026-10-24/README.md).** This catalogue remains the historical custom-recovery inventory and task mapping. Native exports now include tool evidence absent from that earlier Markdown. Source and reviewed-public checksum scopes are documented in the native index.

These records were recovered from the user's Hermes database export and published in **Gusuku**, the home for local AI experiments. The raw archive/database/private JSON remain private. This is a source-recovery update, not a new benchmark or claim that all candidate sessions are independent tests.

## what was recovered

| Recorded model group | Candidate sessions | Public evaluation records |
| --- | --- | --- |
| Qwen3.5 9B Q4_K_M | 42 | [Full screen transcript](2026-10-24-qwen-9b-full-transcript.md): 35 topics (tasks 0–34), 38 test-related prompt occurrences; all 85 stored user/assistant rows from this group retained, including non-test material |
| Ministral 3 14B Instruct Q4_K_M | 34 | [Full screen transcript](2026-10-24-ministral-14b-full-transcript.md): tasks 1–34, 34 prompts; all 69 stored user/assistant rows retained |
| Qwen3.8 27B UD-Q4_K_M | 46 | 37 selected evaluation/follow-up sessions in three files; nine earlier setup/operational/personal sessions excluded from public publication |

The supplied archive contains 122 sessions. Session counts are not attempt counts. The Qwen 9B group includes two empty sessions, a greeting and an accidentally incomplete input. One readiness request received a generic unprocessed-request response; it is not scored as a model reasoning failure. Hostname task 1 and network-log task 17 each have two distinct sessions. The network rerun was not present in the earlier pasted-answer record.

The 34 main Qwen 9B and Ministral prompt texts match after whitespace normalization. Original stored whitespace/markup remains intact in both transcripts. This establishes prompt similarity, not matched settings, memory, actual tools, runtime or equivalent exposure. Granite's later prompts were revised and must not be silently described as the identical test set.

## Qwen 27B source records

- [Pilot source records](2026-10-23-qwen-27b-pilot-full-transcript.md): 24 sessions, 174 published user/assistant rows; 10 generated context/wrapper rows omitted.
- [Execution, runtime and retrieval follow-ups](2026-10-23-qwen-27b-follow-up-full-transcript.md): seven sessions, 227 published rows; 14 generated context/wrapper rows omitted.
- [Skill reuse and timestamp review](2026-10-23-24-qwen-27b-skill-full-transcript.md): six sessions, 314 published rows; 22 generated context/wrapper rows omitted.

These retain original questions, intermediate commentary, final answers, corrections, empty rows and inactive/compacted history where available. A repeated inactive prompt/answer may be a stored replay or rewind; it is not automatically another model attempt. There are 83 published user-role prompt occurrences across these 37 sessions, not 83 independently scored tasks. Explicit framework summaries and wrapper messages are indexed as omissions rather than passed off as original user questions.

Nine pre-pilot sessions from October 21–22 contain initial setup, general conversation, operational inspection or repository work. Their raw bodies are not published. Existing reviewed historical summaries were migrated intact. No deleted/missing conversation or unavailable tool output is reconstructed.

## numbering

The **small-model exploratory screen** uses task 0 (ready) and tasks 1–34. Task titles/attempt labels were added retrospectively without modifying original prompts.

The **27B pilot** uses the earlier roadmap's tasks 1–24, with execution variants and additional follow-ups. Those numbers describe different tasks; do not equate, for example, small-model task 12 with 27B task 12.

Original 27B task association by anonymous source session:

| Original task | Topic | Source sessions |
| --- | --- | --- |
| 1 | Git branch/status | P10 |
| 2 | Security summary | P11 |
| 3 | Production/lab boundary | P12 |
| 4 | Backup gaps | P13 |
| 5 | Database-engine evidence | P14 shared; P29 rerun |
| 6 | Current/planned AdGuard placement | P14 shared; P30 rerun |
| 7 | Documentation contradiction | P14 shared and correction; P31 rerun |
| 8 | SSH failure fixture | P14 shared; P32 rerun |
| 9 | Monitoring authentication fixture | P14 shared; P33 rerun |
| 10 | Container snapshot | P15, including initially missing fixture and supplied completion |
| 11 | Intentional stopped stack | P16 |
| 12 | Persistent storage | P17 |
| 13 | Host-health snapshot | P19; P18 is an extra local-command request |
| 14 | Exporter diagnostic | P20; P38 execution variant |
| 15 | Loki query | P21; P39 execution variant |
| 16 | DNS upstream error | P22 |
| 17 | Backup freshness | P23 |
| 18 | Partial restore | P24 |
| 19 | Backup procedure | P25 |
| 20 | Upgrade/rollback | P26 |
| 21 | Edit-verification planning | P27 |
| 22 | Isolated heading edit | P28 |
| 23 | Execution-host preflight | P34; P35 variant |
| 24 | Conflicting-evidence fixture | P37, after runtime investigation |

P36–P37 also include runtime/reasoning investigation. P39 includes retrieval and skill questions after the Loki execution exercise. P40–P46 cover skill origin/reuse, proposed/reported edits, and source verification. These are follow-ups, not newly invented roadmap task numbers. The public transcript preserves source-session and message boundaries so shared history remains visible.

## review and redaction limits

For the small-model groups, all supplied message bodies are unchanged and all source rows are active, not compacted, and not summaries. The earlier [Qwen](2026-10-24-qwen-9b-answer-transcript.md) and [Ministral](2026-10-24-ministral-14b-answer-transcript.md) pasted-answer recoveries remain as historical records; use the new full exports to resolve their missing-prompt gaps and terminal formatting differences.

The 27B public extracts use marked placeholders for home usernames (35 replacements), SSH key locations (one), loopback URLs (eight), loopback host/port strings (five) and other non-documentation IPv4 literals (two). Fictional documentation-range addresses remain. Redaction occurrence counts describe textual substitutions, not unique devices or secrets. Source session identifiers and hashed filenames are replaced with chronological aliases; sensitive operational sessions are excluded altogether.

No credentials, raw private archive or system/configuration dumps were published. Identifying-path redaction changes some literal commands, so the public extract is not a ready-to-run recreation of private execution tests. False historical claims and malformed probes remain quoted evidence, not guidance. Source message flags and timestamps remain; timing differences do not prove inference latency.

Tool outputs/arguments, system prompts and reasoning fields were not included in the Markdown-only archive. We cannot recover them from this upload or verify model-executed actions by reading assistant claims. Session model metadata is not a captured request-level backend identity. Runtime/sampling, persistent memory/skills and comparison controls remain incomplete.

The earlier review reports remain qualitative and historical. This source update does not create an aggregate leaderboard, deployment approval or live production-health finding. Preserve future exports with explicit task/attempt labels and equivalent settings; use [the evaluation protocol](../../evaluation/evaluation-protocol.md).
