---
session_id: "qwen-27b-P12"
title: "Explain Fujigoko and Gusuku differences"
source: "local"
created_at: "2026-10-23T13:57:02.490588Z"
updated_at: ""
ended_at: "2026-10-23T13:58:36.943670Z"
model: "Qwen3.8-27B-UD-Q4_K_M"
provider: "custom"
cwd: null
archived: false
message_count: 14
tool_call_count: 8
format: "md"
exported_at: "2026-10-24T18:10:53.062860Z"
exporter: "hermes sessions export (md/qmd) v1"
publication_reviewed: true
source_file_sha256: "0c7cdeb8ae241e2c4c1ff3c193b87c2318d491ba94134c11c90213f26c884265"
task_namespace: "27b-roadmap"
task_attempts: [{"task": 3, "attempt": null}]

---

# Explain Fujigoko and Gusuku differences

Session ID: `qwen-27b-P12`

Source: `local`

## Messages

### User — 2026-10-23T13:57:09.182549Z

In /home/[USER]/Projects/fujigoko, read the relevant documentation
and explain the difference between Fujigoko and Gusuku.

Cover their purposes, whether real home services may depend on
Gusuku, and what should happen when an experiment becomes useful
for the home environment. Cite the file paths supporting your answer.

Use repository evidence and mark anything undocumented as unknown.
Read-only: no edits, configuration changes, or access to other hosts.
Keep the answer concise.


### Assistant — 2026-10-23T13:57:10.992785Z



## Tool calls

```json
[
  {
    "id": "GKo8J1kRbwZnrrK807gznZqQhE8NkPAD",
    "call_id": "GKo8J1kRbwZnrrK807gznZqQhE8NkPAD",
    "response_item_id": "fc_GKo8J1kRbwZnrrK807gznZqQhE8NkPAD",
    "type": "function",
    "function": {
      "name": "skill_view",
      "arguments": "{\"name\":\"homelab-repos\"}"
    }
  }
]
```


### Tool — skill_view — 2026-10-23T13:57:11.020863Z

{"success": true, "name": "homelab-repos", "description": "Use when working with homelab repos fujigoko or gusuku.", "tags": ["homelab", "fujigoko", "gusuku", "documentation-audit", "git", "runbooks"], "related_skills": ["github"], "content": "---\nname: homelab-repos\ndescription: Use when working with homelab repos fujigoko or gusuku.\nversion: 1.2.0\nauthor: Hermes Agent\nlicense: MIT\nplatforms: [linux]\nmetadata:\n  hermes:\n    tags: [homelab, fujigoko, gusuku, documentation-audit, git, runbooks]\n    related_skills: [github]\n---\n\n# Homelab repositories (fujigoko + gusuku)\n\n## When to Use\n\n- Navigating either repo: inventories, architecture, service placement, backups, migration progress, recovery runbooks.\n- Auditing or updating homelab docs (status wording, contradictions).\n- Git work in either repo (first commit, identity, branches, push).\n- Any task whose answer depends on a changing fact (hardware, placement, IPs, purchases).\n- Read-only baseline inspection of a live host and comparing its state against the repo docs.\n\nStable context only. Changing facts (hardware, service placement, IP addresses, purchase status, migration progress) live in the repos — always read the current files before answering about them. Never copy changing facts into memory or this skill.\n\n## Environments\n\n- **fujigoko** — `~/Projects/fujigoko` — production home homelab, public GitHub repo. Lake-named hosts: kawaguchi (Unraid, media/manga), motosu (TrueNAS SCALE, Immich/photos/backup target/B2 off-site), yamanaka (Debian 13, non-media apps + monitoring/logging + DNS), shoji (reserved).\n- **gusuku** — `~/Projects/gusuku` — disposable learning lab for enterprise IT exploration, public GitHub repo. Castle names; only physical host is shuri (Proxmox target, formerly fujigoko's \"saiko\").\n- **One-way dependency**: fujigoko must never depend on gusuku for anything. A gusuku outage or total loss must not affect home operations. Useful experiments graduate by being *rebuilt* on fujigoko — never promoted in place.\n- **Workstations are not lab hosts**: aso (primary desktop, Arch), ontake (gaming laptop, Bazzite), norikura (Arch), azuma (macOS) are personal clients used to administer both environments (fujigoko `hosts/workstations.md`, gusuku `docs/administration.md`).\n- Naming conventions: lakes=hosts, mountains=PCs, rivers=physical network, shinkansen=logical/transit, stations=hubs (fujigoko `architecture/naming.md`). Note saiko (reserved fujigoko lake name) ≠ shuri (gusuku host).\n\n## Live host access (connection methods only — never store host facts or secrets here)\n\n- yamanaka, from aso: `ssh -i [REDACTED_SSH_PATH] -o BatchMode=yes [USER]@yamanaka 'COMMAND'` (user sam, key-based, BatchMode). Never read or copy the private key file itself.\n- Other fujigoko hosts (kawaguchi, motosu) and workstations: no connection method provided yet — ask the user.\n- Paperless-ngx restore-test procedure (isolated container, LocMemCache, pre-created index dir, verification recipe): `references/paperless-restore-test.md`.\n- Baseline inspection playbook, DNS verification rules, and passive identification of unknown LAN IPs (pre-connection): `references/live-inspection.md`; raw DNS probe (no `dig` dependency): `scripts/dns-probe.py`.\n- DNS interpretation rules (both cost a user correction): a device's system resolver (e.g. Tailscale MagicDNS) may forward to the homelab resolver — resolver config never proves the device is a non-user; a resolver's upstream failure lines (e.g. DoH connection resets) never prove client query failures, because retry/fallback may succeed. Verify both directions with a direct end-to-end probe to the resolver's actual serving IP.\n- Connecting to live hosts is still only when the user asks; the repos remain documentation, not live state.\n\n## File map (stable shape; the tree evolves — verify with `find <repo> -type f`)\n\nfujigoko (entry point: `README.md`):\n- `architecture/README.md` — role split per host; `architecture/naming.md` — naming\n- `hosts/README.md` — host hardware inventory; `hosts/workstations.md` — personal workstations\n- `network/README.md` — current vs target network; `network/topology.md` — topology diagrams\n- `services/README.md` — service-to-host placement + deployment state; `services/classification.md` — table + priorities\n- `storage/README.md` — storage layout; `backups/README.md` — backup policy + known gaps\n- `migration/yamanaka.md` — migration record (what happened, what remains) — the most recently dated doc\n- `runbooks/<host>-recovery.md` + `runbooks/README.md` — recovery procedures, general incident order\n- `SECURITY.md` — what must never appear in the public repo (no secrets, IPs, MACs, serials, management URLs, keys)\n\ngusuku (entry point: `README.md`):\n- `docs/principles.md` — purpose, scope, 8 design rules (incl. the fujigoko-independence rule)\n- `docs/administration.md` — administration workstations and how the lab is administered\n- `docs/roadmap.md` — phases 0–6 plus ongoing failure/evaluation work\n- `hosts/shuri.md` — the one physical lab host\n\n## Orientation (first, every time)\n\n1. `git -C <repo> status -sb && git log --oneline -5` — which branch, is it pushed? (the working tree may sit on an unpushed fix branch; treat main and its upstream as the published state — don't assume, read it)\n2. Read the repo `README.md`.\n3. Read only the domain files the task needs.\n4. For any changing fact, re-read the relevant current file even when this skill mentions it.\n\n## Documentation audit workflow (lessons from the 2026-10-21 audit)\n\n- Find every file stating the same fact. Status words (deployed / current / temporary / target / planned / ordered / complete) go stale as work completes.\n- The most recently dated doc (usually `migration/`) records what actually happened, but do not silently adopt it as the truth for every other doc — flag the divergence.\n- Runbooks intentionally lag inventory docs (conservative during transitions; may say \"partly provisional\"). Note the lag; do not \"fix\" runbook wording without asking.\n- Keep completed work and remaining work strictly separate; never merge two distinct cleanup scopes into one status line.\n- Before editing, show the user the exact conflicting excerpts with file paths.\n- After editing one file, `grep -rn` the whole repo for the same fact — a single-file edit leaves contradictions behind.\n- **Contradiction = unresolved.** Present both sides and let the user decide or verify against the live host. Never silently choose a version, never turn an assumption into a saved fact.\n\n**Contradictions are never saved here.** The list of known-unresolved contradictions is temporary: when a task touches a potentially conflicting fact, re-derive it from current files (grep the fact across all docs, compare status wording, check the migration record) and present what is *currently* unresolved — both sides, with paths. Never cite or extend a saved list, and never record one in this skill or memory.\n\n## Git workflow (lesson from the git identity mistake)\n\n- Fresh clones have no git identity; the first commit fails.\n- Before the first commit in a repo, check `git config user.name && git config user.email`. If unset, set the **repo-local** identity to the user's established one: `s-pollard` / `[REDACTED_EMAIL]`. Never the global config.\n- Be careful with shell lines: in the incident, a readback line accidentally wrote junk into user.name/user.email. Run config commands as explicit, single-purpose commands.\n- Verify the author with `git log -1` after committing; amending changes the hash — record old → new.\n- User work style: no committing or pushing without explicit permission. Do documentation fixes on a dedicated branch named for the change, and leave merge/push to the user.\n- Pre-commit gate (standing requirement): stage only the named files, then verify the staged diff (`git diff --cached`) and author identity (`git config user.name/email`) and run `git diff --cached --check` BEFORE committing; show the commit summary (`git log -1 --stat`) afterward. Push only when explicitly told to; set upstream with `git push -u origin <branch>` on that explicit instruction.\n- Both repos are public: follow `SECURITY.md` — never commit secrets, private IPs, MACs, serials, management URLs, or credentials.\n\n## Hard rules\n\n- fujigoko never depends on gusuku (one-way).\n- Workstations are personal machines, not disposable lab hosts.\n- Do not connect to hosts unless the user asks; the repos are documentation, not live state.\n- Do not modify the repos unless asked; audits are read-only by default.\n", "path": "homelab-repos/SKILL.md", "skill_dir": "/home/[USER]/.hermes/skills/homelab-repos", "linked_files": {"references": ["references/live-inspection.md", "references/paperless-restore-test.md"], "scripts": ["scripts/dns-probe.py"]}, "usage_hint": "To view linked files, call skill_view(name, file_path) where file_path is e.g. 'references/api.md' or 'assets/config.yaml'", "required_environment_variables": [], "required_commands": [], "missing_required_environment_variables": [], "missing_credential_files": [], "missing_required_commands": [], "setup_needed": false, "setup_skipped": false, "readiness_status": "available", "metadata": {"hermes": {"tags": ["homelab", "fujigoko", "gusuku", "documentation-audit", "git", "runbooks"], "related_skills": ["github"]}}}


### Assistant — 2026-10-23T13:57:20.463708Z



## Tool calls

```json
[
  {
    "id": "TVzzTcfN6LOd05jubPihMb8YvpRoZvbD",
    "call_id": "TVzzTcfN6LOd05jubPihMb8YvpRoZvbD",
    "response_item_id": "fc_TVzzTcfN6LOd05jubPihMb8YvpRoZvbD",
    "type": "function",
    "function": {
      "name": "search_files",
      "arguments": "{\"pattern\":\"gusuku\",\"path\":\"/home/[USER]/Projects/fujigoko\",\"output_mode\":\"content\",\"limit\":100}"
    }
  },
  {
    "id": "ApgaSPakULTMDjmYKdqgLOTNwVcgDoac",
    "call_id": "ApgaSPakULTMDjmYKdqgLOTNwVcgDoac",
    "response_item_id": "fc_ApgaSPakULTMDjmYKdqgLOTNwVcgDoac",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"/home/[USER]/Projects/fujigoko/README.md\"}"
    }
  }
]
```


### Tool — search_files — 2026-10-23T13:57:20.567117Z

{"total_count": 17, "matches_format": "path-grouped: each file path on its own line, followed by indented '<line>: <content>' rows for matches in that file", "matches_text": "/home/[USER]/Projects/fujigoko/network/topology.md\n  57: - experimental/lab infrastructure belongs in gusuku and is not part of the Fujigoko production topology.\n/home/[USER]/Projects/fujigoko/network/README.md\n  108: Experimental gusuku networking is separate from this production design and must not become a required dependency for Fujigoko.\n  146: Lab/gusuku UPS decisions are intentionally outside this production-network document.\n/home/[USER]/Projects/fujigoko/migration/yamanaka.md\n  16: Experimental/lab workloads belong in gusuku, not Yamanaka.\n/home/[USER]/Projects/fujigoko/README.md\n  7: Experimental and career-learning infrastructure belongs in the separate [`gusuku`](https://github.com/s-pollard/gusuku) lab. Fujigoko must not depend on gusuku for required home services.\n  16: The physical system formerly documented as **saiko** is no longer part of Fujigoko. It moved to gusuku and is now **shuri**.\n/home/[USER]/Projects/fujigoko/architecture/README.md\n  5: Fujigoko is the production homelab. Host roles should remain obvious, production services should not depend on the experimental gusuku lab, and storage/recovery design should follow the value of the data rather than the size of the system.\n  14: The physical machine formerly documented here as `saiko` moved to the separate gusuku lab and is now `shuri`.\n  120: experimentation                  -> gusuku, not fujigoko\n/home/[USER]/Projects/fujigoko/storage/README.md\n  101: Experimental/lab storage belongs in gusuku and is intentionally not part of the Fujigoko production-storage model.\n/home/[USER]/Projects/fujigoko/architecture/naming.md\n  21: The physical machine that was briefly documented as `saiko` moved out of Fujigoko into the separate gusuku lab and was renamed `shuri`. Do not use `saiko` and `shuri` interchangeably: `shuri` belongs to gusuku; `saiko` is again only a reserved Fujigoko lake name.\n/home/[USER]/Projects/fujigoko/runbooks/yamanaka-recovery.md\n  45: Game servers and disposable lab workloads belong in gusuku.\n/home/[USER]/Projects/fujigoko/hosts/README.md\n  78: ## gusuku boundary\n  80: The physical system formerly documented in Fujigoko as `saiko` has moved to the separate [`gusuku`](https://github.com/s-pollard/gusuku) learning/experimentation lab and is now `shuri`.\n  82: Do not duplicate Shuri hardware or lab-state documentation here. Fujigoko should only document the boundary: production services must not depend on gusuku.\n/home/[USER]/Projects/fujigoko/services/README.md\n  152: Disposable services, VMs, Kubernetes experiments, game servers, and other learning workloads belong in the separate gusuku lab. Fujigoko production services must not depend on them.\n/home/[USER]/Projects/fujigoko/services/classification.md\n  12: Experimental infrastructure belongs in gusuku, not Fujigoko."}


### Tool — read_file — 2026-10-23T13:57:20.569586Z

{"content": "1|# fujigoko\n2|\n3|Fujigoko is my production homelab.\n4|\n5|The design is intentionally simple: keep host roles clear, document deployed state, preserve recoverability, and add complexity only when it solves a real production problem.\n6|\n7|Experimental and career-learning infrastructure belongs in the separate [`gusuku`](https://github.com/s-pollard/gusuku) lab. Fujigoko must not depend on gusuku for required home services.\n8|\n9|## Core hosts\n10|\n11|- **kawaguchi** — Unraid media server, manga, bulk media storage, and host-specific monitoring agent\n12|- **motosu** — TrueNAS SCALE photo/Immich host and backup target\n13|- **yamanaka** — Debian general-application server hosting retained non-media services, monitoring/logging, Uptime Kuma, and one AdGuard Home instance\n14|- **shoji** — reserved; no assigned role\n15|\n16|The physical system formerly documented as **saiko** is no longer part of Fujigoko. It moved to gusuku and is now **shuri**.\n17|\n18|## Administration workstations\n19|\n20|**Aso** is the primary personal desktop and administration workstation. **Ontake**, **Norikura**, and **Azuma** provide alternative laptop access. See [workstation inventory](hosts/workstations.md) for hardware, roles, and backup scope.\n21|\n22|## Network direction\n23|\n24|- current gateway: UDM-Pro\n25|- target gateway/firewall: dedicated OPNsense appliance\n26|- current aggregation: USW-Aggregation\n27|- future core-switch main candidate: TP-Link Omada SX3016F\n28|- target wireless AP: TP-Link Omada EAP775-Wall\n29|- target DNS: redundant AdGuard Home on Yamanaka and Motosu\n30|\n31|The UDM-Pro can be sold after replacement routing and any required UniFi management are stable.\n32|\n33|## Public repository policy\n34|\n35|This repository is intended to be safe to publish. Do not commit credentials, secrets, public/WAN addressing, exact private addressing, MAC addresses, serial numbers, account identifiers, cloud resource identifiers, management URLs, or personal location details.\n36|\n37|See [`SECURITY.md`](SECURITY.md) for the full policy.\n38|\n39|## Documentation\n40|\n41|- [architecture](architecture/README.md) — production roles and placement rules\n42|- [naming](architecture/naming.md) — naming conventions\n43|- [hosts](hosts/README.md) — hardware and platform inventory\n44|- [local AI administration experiments](administration/local-ai/README.md) — dated Hermes and Odysseus testing on Aso, findings, and remaining work\n45|- [network](network/README.md) — current and target network design\n46|- [topology](network/topology.md) — physical/logical topology\n47|- [services](services/README.md) — service inventory and dependencies\n48|- [service classification](services/classification.md) — placement and lifecycle decisions\n49|- [storage](storage/README.md) — storage ownership and data criticality\n50|- [backups](backups/README.md) — backup policy, verified state, and gaps\n51|- [Yamanaka migration](migration/yamanaka.md) — completed service cutover and remaining cleanup/backup work\n52|- [runbooks](runbooks/README.md) — recovery procedures\n53|\n54|## Current priorities\n55|\n56|1. Establish and verify Yamanaka-to-Motosu backups.\n57|2. Deploy the second AdGuard Home instance on Motosu to complete redundant DNS.\n58|3. Rebuild the post-move network around OPNsense; keep the SX3016F as the main core-switch candidate until purchased and verified.\n59|4. Finalize the UPS/power plan after verifying real outlet/receptacle compatibility.\n60|5. Preserve independent recovery for irreplaceable data before optimizing convenience services.\n61|6. Remove the legacy Kawaguchi shares (uppercase `Media` and `roms`) after dependency checks confirm nothing still uses them.\n62|\n63|Immich restoration and Kawaguchi container/appdata cleanup are complete. See [migration](migration/yamanaka.md) and [services](services/README.md) for details.", "total_lines": 63, "file_size": 3688, "truncated": false, "is_binary": false, "is_image": false, "not_found": false}


### Assistant — 2026-10-23T13:57:28.339786Z



## Tool calls

```json
[
  {
    "id": "dDdVLBaCibuRmrXiPZJWEAJXmygC7OQ3",
    "call_id": "dDdVLBaCibuRmrXiPZJWEAJXmygC7OQ3",
    "response_item_id": "fc_dDdVLBaCibuRmrXiPZJWEAJXmygC7OQ3",
    "type": "function",
    "function": {
      "name": "search_files",
      "arguments": "{\"pattern\":\"rebuild|promot|graduat|useful\",\"path\":\"/home/[USER]/Projects/fujigoko\",\"output_mode\":\"content\",\"limit\":40}"
    }
  },
  {
    "id": "W5zUNxlN1m9Vrjr4fmCb0gToCYf271ue",
    "call_id": "W5zUNxlN1m9Vrjr4fmCb0gToCYf271ue",
    "response_item_id": "fc_W5zUNxlN1m9Vrjr4fmCb0gToCYf271ue",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"/home/[USER]/Projects/fujigoko/architecture/README.md\"}"
    }
  }
]
```


### Tool — search_files — 2026-10-23T13:57:28.389603Z

{"total_count": 24, "matches_format": "path-grouped: each file path on its own line, followed by indented '<line>: <content>' rows for matches in that file", "matches_text": "/home/[USER]/Projects/fujigoko/administration/local-ai/odysseus.md\n  17: Repository orientation was useful but needed corrections: a mirror was initially described with doubled usable capacity; existing snapshot retention was reused as a proposed backup policy; live DB/file backup consistency was overstated; documented state was sometimes presented too confidently. Those proposals were not implemented.\n  127: The durable fact tested was: Fujigoko is production; Gusuku is disposable learning infrastructure; Fujigoko must never depend on Gusuku for required home services; useful experiments graduate by being rebuilt on Fujigoko.\n/home/[USER]/Projects/fujigoko/administration/local-ai/README.md\n  11: Aso remains a personal administration workstation. Fujigoko services must continue without it or either agent. Gusuku remains disposable; useful experiments are rebuilt on Fujigoko rather than making production depend on the lab.\n/home/[USER]/Projects/fujigoko/administration/local-ai/hermes.md\n  40: The reported writes were checked during the session. A controlled new-session test of all learned behavior remains useful; saving a skill does not prove reliable future application.\n/home/[USER]/Projects/fujigoko/network/topology.md\n  3: This document shows useful production infrastructure relationships without publishing exact addressing or other sensitive operational identifiers.\n  28: - Motosu reaches the network through the access-switch path (USW-Lite-8-PoE). Its storage/Immich rebuild is complete and validated.\n/home/[USER]/Projects/fujigoko/storage/README.md\n  36: One mirror member failed after the rebuild and was replaced temporarily with the best available older spare. The resilver completed successfully and redundancy was restored. Replacing that temporary member with a better drive remains planned maintenance.\n/home/[USER]/Projects/fujigoko/network/README.md\n  22: The U7 Pro is the currently active AP. Other owned UniFi APs may remain offline during the move/rebuild period.\n/home/[USER]/Projects/fujigoko/services/classification.md\n  94: Planned does not mean required. Remove ideas that are no longer useful rather than carrying them indefinitely.\n/home/[USER]/Projects/fujigoko/services/README.md\n  74: Critical persistence is the Immich library, database recovery data, photo/archive data, and Yamanaka backup datasets. Redis/Valkey state and machine-learning caches are rebuildable.\n  117: These remain optional until actually deployed and found useful.\n/home/[USER]/Projects/fujigoko/runbooks/kawaguchi-recovery.md\n  7: Kawaguchi is intentionally treated as more rebuildable than Motosu or Yamanaka. The priority is restoring configuration and service function, not immediately restoring every media file.\n/home/[USER]/Projects/fujigoko/runbooks/yamanaka-recovery.md\n  130: Redis is rebuildable unless future deployment documentation establishes otherwise.\n/home/[USER]/Projects/fujigoko/runbooks/README.md\n  46: The goal is to restore useful service, not to reproduce every byte or historical metric immediately.\n/home/[USER]/Projects/fujigoko/backups/README.md\n  3: Backup effort follows data value and rebuild cost rather than raw storage size.\n  6: kawaguchi = mostly rebuildable media infrastructure\n  15: Application-generated backups stored only on the source host are useful restore points but are not sufficient host-failure protection.\n  62: Kawaguchi is comparatively rebuildable. The backup priority is configuration and metadata, not the full media payload.\n  71: - useful manga application metadata\n/home/[USER]/Projects/fujigoko/architecture/naming.md\n  31: Japanese river names are reserved for physical network infrastructure where useful, such as core, aggregation, or access switching.\n  33: Do not rename working production hardware solely to satisfy the convention. Apply the convention when it improves clarity during a rebuild or replacement.\n  37: Shinkansen-related names are reserved for logical or transit-oriented networking concepts where useful, such as VPN/transit networks, inter-site links, or routing projects.\n/home/[USER]/Projects/fujigoko/architecture/README.md\n  33: Kawaguchi is intentionally relatively rebuildable. Configuration and metadata are more important to protect than reacquirable movie/TV payloads.\n  144: - transient metrics/history where rebuilding is acceptable"}


### Tool — read_file — 2026-10-23T13:57:28.392415Z

{"content": "1|# architecture\n2|\n3|## design intent\n4|\n5|Fujigoko is the production homelab. Host roles should remain obvious, production services should not depend on the experimental gusuku lab, and storage/recovery design should follow the value of the data rather than the size of the system.\n6|\n7|```text\n8|kawaguchi = media + manga + host-specific monitoring agent\n9|motosu    = photos + Immich + backup storage\n10|yamanaka  = general applications + centralized monitoring/logging + DNS\n11|shoji     = reserved / unassigned\n12|```\n13|\n14|The physical machine formerly documented here as `saiko` moved to the separate gusuku lab and is now `shuri`.\n15|\n16|## kawaguchi — media\n17|\n18|Primary role: media server and media-adjacent storage/services.\n19|\n20|- UGREEN iDX6011 64GB AI NAS\n21|- Intel Core Ultra 5 125H\n22|- 64 GB memory\n23|- Unraid 7.3.2\n24|- 10 GbE uplink\n25|\n26|Permanent workload classes:\n27|\n28|- Plex and media automation\n29|- manga services\n30|- bulk media/download storage\n31|- cAdvisor and smartctl-exporter / host-specific monitoring agents\n32|\n33|Kawaguchi is intentionally relatively rebuildable. Configuration and metadata are more important to protect than reacquirable movie/TV payloads.\n34|\n35|## motosu — photos and backup storage\n36|\n37|Primary role: photo storage, Immich, and local backup target.\n38|\n39|- UGREEN NASync DXP2800\n40|- Intel N100\n41|- 8 GB memory\n42|- TrueNAS SCALE\n43|- 2 × 6 TB Seagate ST6000NM0024 HDDs\n44|- mirrored ZFS storage\n45|- 2.5 GbE onboard networking\n46|\n47|Current migration state:\n48|\n49|- TrueNAS SCALE is installed\n50|- the photo/Immich dataset exists under the Motosu pool\n51|- the Immich library was copied to the rebuilt system and verified during migration\n52|- Immich application/database restoration is complete and validated\n53|\n54|Target permanent workloads:\n55|\n56|- Immich\n57|- photo/archive storage\n58|- Yamanaka backup datasets\n59|- ZFS snapshots\n60|- Backblaze B2 off-site protection for selected high-value data\n61|- one AdGuard Home instance as the second DNS node\n62|\n63|Motosu remains storage/photo focused rather than becoming a general application host.\n64|\n65|## yamanaka — general applications\n66|\n67|Primary role: simple, always-on production application server.\n68|\n69|- Dell OptiPlex 3070 SFF\n70|- Intel Core i5-9500\n71|- Debian GNU/Linux 13\n72|- 16 GB DDR4 installed; upgrade only if measured usage justifies it\n73|- Patriot P300 512 GB NVMe\n74|- Intel X520-DA2 10 GbE upgrade planned/ordered\n75|\n76|Current workload classes:\n77|\n78|- retained non-media personal applications\n79|- Prometheus / Grafana / Loki / Alloy\n80|- Uptime Kuma and Signal notification bridge\n81|- one AdGuard Home instance\n82|- application-local PostgreSQL/Redis dependencies\n83|\n84|The migrated workload has substantial CPU and memory headroom on the current hardware. Yamanaka does not host game servers or disposable lab workloads.\n85|\n86|## shoji — reserved\n87|\n88|Shoji has no assigned role. Keep the name reserved until another production host is justified.\n89|\n90|## network architecture\n91|\n92|```text\n93|current\n94|internet -> UDM-Pro -> USW-Aggregation -> hosts\n95|\n96|target\n97|fiber handoff -> OPNsense -> switching -> hosts\n98|```\n99|\n100|Decisions:\n101|\n102|- OPNsense is the target production router/firewall\n103|- UDM-Pro leaves the routing role only after replacement routing is proven\n104|- USW-Aggregation can remain during transition\n105|- TP-Link Omada SX3016F is the main future core/aggregation-switch candidate\n106|- TP-Link Omada EAP775-Wall is the planned target AP\n107|- exact addressing, VLAN IDs, reservations, and management URLs stay out of this public repository\n108|\n109|## service placement\n110|\n111|```text\n112|media / manga                    -> kawaguchi\n113|host-specific monitoring agent   -> monitored host\n114|Immich / photos / backup storage -> motosu\n115|general personal applications   -> yamanaka\n116|central monitoring/logging       -> yamanaka\n117|uptime monitoring                -> yamanaka\n118|DNS                              -> yamanaka + motosu target pair\n119|routing / firewall               -> OPNsense appliance\n120|experimentation                  -> gusuku, not fujigoko\n121|```\n122|\n123|Uptime Kuma currently runs on Yamanaka, so a total Yamanaka host failure also removes that monitoring path. This is accepted current state rather than an independent-watchdog design.\n124|\n125|## backup priorities\n126|\n127|High priority:\n128|\n129|- Immich library and database recovery data\n130|- photo archive data\n131|- Yamanaka application data/databases\n132|- irreplaceable documents and records\n133|\n134|Medium priority:\n135|\n136|- Kawaguchi Unraid configuration\n137|- retained application configuration and metadata\n138|- DNS/monitoring configuration\n139|\n140|Low priority / replaceable:\n141|\n142|- movie/TV payloads\n143|- downloads and caches\n144|- transient metrics/history where rebuilding is acceptable\n145|\n146|## principles\n147|\n148|1. Keep production and experimentation separate.\n149|2. Keep host roles obvious.\n150|3. Prefer understandable systems over unnecessary clustering.\n151|4. Keep application databases local to the host that runs them; back them up independently.\n152|5. Document storage, dependencies, and recovery before adding automation.\n153|6. Remove retired experiments instead of preserving them by inertia.\n154|7. Keep secrets, exact addressing, personal information, and unique external identifiers out of the public repository.\n155|8. Treat deployed state—not old migration assumptions—as the source of truth.", "total_lines": 155, "file_size": 5042, "truncated": false, "is_binary": false, "is_image": false, "not_found": false}


### Assistant — 2026-10-23T13:57:38.344449Z



## Tool calls

```json
[
  {
    "id": "XziAgLzMPCNVNFuVaGdNNTyovTI3Ao5s",
    "call_id": "XziAgLzMPCNVNFuVaGdNNTyovTI3Ao5s",
    "response_item_id": "fc_XziAgLzMPCNVNFuVaGdNNTyovTI3Ao5s",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"/home/[USER]/Projects/fujigoko/administration/local-ai/README.md\"}"
    }
  },
  {
    "id": "6yznuicRBux4y9Msc8bOPY5ZVR9yVLrR",
    "call_id": "6yznuicRBux4y9Msc8bOPY5ZVR9yVLrR",
    "response_item_id": "fc_6yznuicRBux4y9Msc8bOPY5ZVR9yVLrR",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"/home/[USER]/Projects/fujigoko/services/README.md\",\"offset\":130,\"limit\":40}"
    }
  },
  {
    "id": "FCMNZCkN1F0pwbHaeTMq6oQ8r6EzCmwo",
    "call_id": "FCMNZCkN1F0pwbHaeTMq6oQ8r6EzCmwo",
    "response_item_id": "fc_FCMNZCkN1F0pwbHaeTMq6oQ8r6EzCmwo",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"/home/[USER]/Projects/fujigoko/services/classification.md\",\"offset\":1,\"limit\":30}"
    }
  }
]
```


### Tool — read_file — 2026-10-23T13:57:38.357213Z

{"content": "1|# local AI administration experiments\n2|\n3|Experiment records: 2026-10-21 through 2026-10-22 (America/Chicago). This records observations from interactive testing on Aso, not a declaration that the agents are production services. UTC logs can show 2026-10-22 for the same evening.\n4|\n5|- [Hermes Agent](hermes.md) — setup, homelab work, memory/skills, inference failures, and lessons\n6|- [Odysseus](odysseus.md) — setup, tool execution, routing diagnosis, local patches, and remaining work\n7|- [Workstation inventory](../../hosts/workstations.md) — hardware source of truth\n8|\n9|## scope and boundary\n10|\n11|Aso remains a personal administration workstation. Fujigoko services must continue without it or either agent. Gusuku remains disposable; useful experiments are rebuilt on Fujigoko rather than making production depend on the lab.\n12|\n13|The agents can help inspect documentation, propose plans, execute authorized diagnostics, and prepare reviewed changes. A local model is not an authority on host state. Distinguish repository claims, direct tool results, user-supplied evidence, and assumptions. Container readiness does not prove application correctness, backup recoverability, or disk health.\n14|\n15|These dated records preserve failures and corrections. They do not replace the live inventories, service records, or recovery runbooks. Re-read those files and verify live state when needed. Do not copy changing findings into permanent memory as timeless facts.\n16|\n17|## shared inference setup observed during testing\n18|\n19|| Component | Observed setup |\n20|| --- | --- |\n21|| Workstation | Aso; Arch Linux, KDE Plasma/Wayland |\n22|| CPU / RAM | Ryzen 7 7800X3D; 32 GB RAM |\n23|| GPU | Radeon RX 7900 XTX; approximately 24 GiB VRAM |\n24|| Model | Qwen3.8-27B-UD-Q4_K_M GGUF; approximately 17.3 GB download |\n25|| Inference | Hermes-managed llama.cpp Vulkan build b11671 |\n26|| Serving window | Worker command line showed `--ctx-size 65536` |\n27|| Cache / acceleration | Q8 K/V cache, flash attention, draft-MTP observed in the worker arguments |\n28|\n29|Odysseus was pointed at the existing local OpenAI-compatible inference service. This is Odysseus running its own agent against llama.cpp, not a verified Odysseus-to-Hermes-agent integration. Stopping the inference server interrupts either client. Two llama-server processes were the model router and its worker, not evidence of duplicate model loads.\n30|\n31|Generation logs and UI counters showed roughly 50–70 tokens/second in different tasks. Discrete VRAM usage was observed around 21.4 GiB during a model run. These are informal observations, not comparable benchmarks: prompt length, caching, reasoning, speculation, tool rounds, and concurrent work differ. UI cumulative input totals can count repeated history across calls and should not be interpreted as one request's context size.\n32|\n33|## operating lessons\n34|\n35|- Require actual tool-call records before accepting claims that commands ran or files were read. Model self-identification is not reliable endpoint identification.\n36|- Local inference still has input, output, and context token limits. Reasoning consumes output capacity and compute even without per-token API billing.\n37|- GPU activity after a visible answer can be an auxiliary task, background review, compression, or continued generation. Inspect agent and inference logs rather than infer a cause from utilization alone.\n38|- Use scoped tasks and bounded output. Reading every document repeatedly produced large cumulative input and slow orientation turns.\n39|- Shell access is not a read-only sandbox. A prompt restriction does not technically remove the account's ability to change hosts or use Docker.\n40|- Review diffs and changed-file lists and run `git diff --check`. A clean whitespace check does not establish factual correctness.\n41|- Follow [SECURITY.md](../../SECURITY.md). Keep credentials, key locations/material, exact addressing, management endpoints, raw private logs, and identifying device metadata outside this public repo.\n42|\n43|## repository workflow\n44|\n45|`main` is the shared accepted documentation for both agents. Hermes and Odysseus have separate documents, not permanent agent-specific branches. Use a short-lived task branch for work that needs review, merge it after verification, then remove the completed branch. Keep the local checkout synchronized with `main` before another task. Do not let both agents edit the same checkout concurrently; use separate worktrees when parallel work is intentional.\n46|\n47|Changes to an agent's own upstream source belong in that project's checkout; this repository records their purpose, tested behavior, and remaining limitations.\n48|\n49|## latest follow-up — 2026-10-22\n50|\n51|Aso's Fujigoko checkout was fast-forwarded to the consolidated `main`. Odysseus then demonstrated direct workspace file reads, creation and editing, cross-chat memory retrieval, and answering from a pinned homelab boundary without tools. A further local source patch added memory to the workspace toolset. A read-only Markdown target-file check executed and reported no missing targets. Private Tailscale Serve access was configured; external-client connectivity is not yet verified. See the [dated Odysseus follow-up](odysseus.md#follow-up--2026-10-22) for evidence and remaining limitations.\n52|\n53|## next work\n54|\n55|1. Verify the server's serving window and both clients' effective budgets with authenticated discovery or an explicit supported override.\n56|2. Harden Odysseus tool selection across turns and wording. Explicit workspace read/create/edit access now passes; broad intent filtering remains an issue.\n57|3. Improve automatic memory relevance and duplicate handling. Cross-chat memory-tool retrieval and pinned-rule recall now pass; skill persistence remains untested.\n58|4. Verify unattended startup, cancellation, and off-LAN access end to end. Tailscale Serve is configured, but an actual remote-client test has not been reported.\n59|5. Continue with scoped administration tasks. A local Markdown target-file check ran successfully; backup implementation remains separate work requiring app-consistent methods and restore verification.", "total_lines": 59, "file_size": 6046, "truncated": false, "is_binary": false, "is_image": false, "not_found": false}


### Tool — read_file — 2026-10-23T13:57:38.359725Z

{"content": "130|yamanaka -> adguard-home\n131|motosu   -> adguard-home\n132|```\n133|\n134|Both instances should provide equivalent filtering policy on separate physical hosts. Exact resolver addresses and synchronization details stay in private operational configuration.\n135|\n136|## completed cleanup\n137|\n138|Kawaguchi cleanup completed on 2026-10-20:\n139|\n140|- migrated non-media containers removed\n141|- RomM and MariaDB removed\n142|- obsolete stopped containers removed\n143|- dangling Docker volumes removed\n144|- unused Docker images pruned\n145|- retired appdata removed\n146|- TitleCardMaker, Kometa, Lidarr, and Listenarr appdata removed\n147|\n148|The resulting Docker state was 14 active containers, 14 active images, no local Docker volumes, and no reclaimable Docker image/container space.\n149|\n150|## lab boundary\n151|\n152|Disposable services, VMs, Kubernetes experiments, game servers, and other learning workloads belong in the separate gusuku lab. Fujigoko production services must not depend on them.", "total_lines": 152, "file_size": 4841, "truncated": false, "is_binary": false, "is_image": false, "not_found": false}


### Tool — read_file — 2026-10-23T13:57:38.361676Z

{"content": "1|# service classification\n2|\n3|Services are classified by function, intended production placement, and persistence value.\n4|\n5|```text\n6|kawaguchi = media + manga + host-specific monitoring agent\n7|motosu    = photos + Immich + backup storage + redundant DNS target\n8|yamanaka  = non-media applications + centralized monitoring/logging + DNS\n9|shoji     = reserved / unassigned\n10|```\n11|\n12|Experimental infrastructure belongs in gusuku, not Fujigoko.\n13|\n14|## media — kawaguchi\n15|\n16|Permanent:\n17|\n18|- Plex\n19|- Sonarr\n20|- Radarr\n21|- SABnzbd\n22|- Bazarr\n23|- Seerr\n24|- Tautulli\n25|- Recyclarr\n26|- Unpackerr\n27|- Komga\n28|- Komf\n29|- Tachidesk\n30|- cAdvisor", "total_lines": 127, "file_size": 4054, "truncated": true, "hint": "Use offset=31 to continue reading (showing 1-30 of 127 lines)", "is_binary": false, "is_image": false, "not_found": false}


### Assistant — 2026-10-23T13:58:04.035650Z

All evidence comes from the fujigoko repo only (read-only, no changes).

Purpose
- Fujigoko is the production homelab: "Fujigoko is my production homelab" — README.md:3. Design intent keeps host roles clear and recoverable — architecture/README.md:5. Hosts: kawaguchi (media/manga), motosu (photos/Immich/backup), yamanaka (apps + monitoring), shoji (reserved) — README.md:9-14, architecture/README.md:7-12.
- Gusuku is the separate experimental/career-learning lab: "Experimental and career-learning infrastructure belongs in the separate gusuku lab" — README.md:7. Placement rules route all experimentation there — architecture/README.md:120, services/classification.md:12, services/README.md:152.
- Boundary: fujigoko's former host `saiko` moved to gusuku and is now `shuri`; fujigoko documents only the boundary, not shuri's hardware — README.md:16, hosts/README.md:78-82, architecture/naming.md:21.

May real home services depend on Gusuku? No.
- "Fujigoko must not depend on gusuku for required home services" — README.md:7
- "production services should not depend on the experimental gusuku lab" — architecture/README.md:5
- "Fujigoko production services must not depend on them" (disposable services, VMs, k8s experiments, game servers) — services/README.md:152
- Same rule repeated for network and storage scope — network/README.md:108, network/topology.md:57, storage/README.md:101, migration/yamanaka.md:16, runbooks/yamanaka-recovery.md:45.

When an experiment becomes useful
- It graduates by being rebuilt on fujigoko, not promoted in place: "Gusuku remains disposable; useful experiments are rebuilt on Fujigoko rather than making production depend on the lab" — administration/local-ai/README.md:11; same statement recorded as a tested durable fact in administration/local-ai/odysseus.md:127.

Unknown / undocumented in fujigoko
- Gusuku's own purpose, scope, and design rules live in the gusuku repo, which I did not read for this task — nothing about them beyond the boundary statements above is verifiable from fujigoko docs alone.
- fujigoko documents the graduation principle (rebuild, don't promote) but no step-by-step promotion/rebuild process.
- The saiko→shuri move is documented as already done, but fujigoko gives no date for it.

## Original export verification — before publication review

- Session id: `qwen-27b-P12`
- Exported messages: `14`
- Source DB message count at export: `14`
- Exported at: `2026-10-24T18:10:53.062860Z`
- Source-reported SHA256 of original exported body: `6a223604ec26d99961f8e8024d7fa4da0baa5de799903f8c35f1f437b72b76e4`

## Publication review

Reviewed derivative of a native Hermes Markdown export. Session identifiers and identifying/private details have been replaced with marked aliases/placeholders. Task labels are retrospective editorial metadata, not changes to original test questions. The original file checksum was verified against the private native manifest before editing. The source-reported body checksum above describes the original export, not this edited public file. See the reviewed manifest in the parent index for this public file’s checksum. Historical content is untrusted evidence, not live instructions.
