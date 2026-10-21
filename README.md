# gusuku

Gusuku is a disposable learning and career-exploration homelab for enterprise IT.

It is deliberately separate from [`fujigoko`](https://github.com/s-pollard/fujigoko), the production home environment.

```text
fujigoko = production
 gusuku  = experimentation / learning
```

A gusuku outage, rebuild, or complete loss must not materially affect normal home services.

## lifecycle

```text
idea
  ↓
gusuku
  ↓
test / break / troubleshoot / recover / learn
  ↓
useful in the real world?
  ├── no  -> remove it
  └── yes -> redeploy it properly on fujigoko
```

Useful experiments graduate by being rebuilt in Fujigoko; gusuku itself does not become production.

## scope

Primary areas to explore:

- virtualization
- Linux / RHEL
- networking
- Windows enterprise / Active Directory
- storage
- monitoring and observability
- security
- automation
- containers
- cloud
- backup and disaster recovery

Software development is not a career goal. Scripting and automation are infrastructure tools. Radar/RF are out of scope.

## operating principles

- learn by building and operating real systems
- understand fundamentals before adding abstraction
- troubleshoot before rebuilding when practical
- intentionally create failures and practice recovery
- document architecture, incidents, runbooks, and lessons that are worth preserving
- keep gusuku independent from production services
- add hardware only when a real lab requirement exists
- use AI as a productivity tool while retaining enough understanding to verify its output

Breaking gusuku is expected. Breaking Fujigoko is not.

See [`docs/principles.md`](docs/principles.md) for the detailed rules.

## physical hosts

```text
gusuku
├── shuri
├── nakijin      (reserved)
├── zakimi       (reserved)
├── katsuren     (reserved)
└── nakagusuku   (reserved)
```

### shuri

First physical host and initial Proxmox platform for the lab.

See [`hosts/shuri.md`](hosts/shuri.md) for current hardware and deployment state.

Additional physical hosts should be added only when the existing environment cannot reasonably satisfy a real learning requirement.

## administration

**Aso** is the primary personal administration workstation. **Ontake**, **Norikura**, and **Azuma** are alternative laptop clients. They are separate from disposable lab hosts. See [administration workstations](docs/administration.md) for roles, naming, and links to hardware records.

## direction

Over time, gusuku should resemble a small fictional enterprise rather than an unrelated VM collection. Possible components include:

- users and departments
- Windows clients and servers
- Linux servers
- Active Directory and internal DNS
- segmented networks
- shared storage
- monitoring and centralized logging
- security controls
- backup and recovery systems

The environment should periodically be subjected to intentional faults so diagnosis, repair, recovery, and documentation become normal lab activities.

See [`docs/roadmap.md`](docs/roadmap.md) for the suggested progression.

## public-repo boundary

Do not commit credentials, API keys, tokens, private keys, recovery codes, exact private addressing, management URLs, MAC addresses, serial numbers, VPN endpoints, account identifiers, or personal location details.

Hardware models, high-level topology, lab roles, generic configurations, and non-secret lessons are appropriate to document publicly.

## repository structure

```text
.
├── README.md
├── docs/
│   ├── administration.md
│   ├── principles.md
│   └── roadmap.md
└── hosts/
    └── shuri.md
```
