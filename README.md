# gusuku

gusuku is a learning and career-exploration homelab.

The goal is not to train for one specific job. The goal is to spend the years before military retirement exploring different areas of enterprise IT, figuring out what is actually enjoyable, and developing skills that can transfer into a civilian career.

`fujigoko` is the home production environment.

`gusuku` is where things can be built, broken, rebuilt, and experimented with without affecting `fujigoko`.

## environment boundary

`gusuku` is experimental and disposable by design. It should not become a production environment simply because an experiment happens to be useful.

The intended lifecycle is:

```text
idea
  ↓
gusuku
  ↓
test / break / learn / validate
  ↓
useful in the real world?
  ├── no  → remove it
  └── yes → redeploy it properly on fujigoko
```

If a service, configuration, or platform proves genuinely useful for the real home environment, it should graduate out of gusuku and be deployed on an appropriate `fujigoko` system.

`fujigoko` must not depend on gusuku for required home services.

## core principles

- learn by building and operating real systems
- prefer practical experience over theory alone
- learn how enterprise systems interact, not just individual products
- troubleshoot before rebuilding
- intentionally create failures and practice recovery
- document architecture, incidents, and lessons learned
- keep gusuku independent from critical fujigoko services
- keep gusuku workloads experimental rather than production
- graduate useful real-world services to fujigoko instead of making gusuku permanent
- add hardware only when a real lab requirement exists
- use scripting and automation as infrastructure tools, not as a software-development goal
- use AI as a productivity tool while retaining enough underlying knowledge to verify its work

Breaking gusuku is expected.

Breaking fujigoko is not.

## areas to explore

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

Cloud and higher-level platforms should come after the traditional infrastructure fundamentals they depend on.

## physical hosts

```text
gusuku
├── shuri
├── nakijin
├── zakimi
├── katsuren
└── nakagusuku
```

### shuri

First physical host.

Initial role:

- Proxmox virtualization host
- primary platform for gusuku virtual infrastructure

### reserved names

- nakijin
- zakimi
- katsuren
- nakagusuku

Additional physical hosts should only be added when the lab develops a real requirement for them.

## long-term direction

Eventually gusuku should resemble a small fictional enterprise rather than a collection of unrelated test machines.

The environment may include:

- multiple departments
- users and groups
- Windows clients
- Linux servers
- Active Directory
- internal DNS
- network segmentation
- shared storage
- internal services
- remote access
- monitoring
- centralized logging
- security controls
- backups
- disaster recovery

The environment should periodically be subjected to simulated failures so diagnosis, repair, recovery, and documentation become part of the lab rather than exceptional events.

## career goal

The technical work is only half of the project. Each major area should eventually be evaluated for both personal fit and civilian career value.

The objective is to find the overlap between work that is enjoyable and work that provides a strong post-military career.

See [`docs/principles.md`](docs/principles.md), [`docs/roadmap.md`](docs/roadmap.md), and [`hosts/shuri.md`](hosts/shuri.md) for the current source of truth.
