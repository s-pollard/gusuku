# gusuku

gusuku is a learning and experimentation homelab for exploring enterprise IT.

The goal is to build practical experience across different infrastructure domains, understand how enterprise systems work together, and figure out which areas are actually interesting through hands-on use.

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

## evaluation

As different areas are explored, they can be evaluated based on hands-on experience:

- enjoyment
- troubleshooting enjoyment
- frustration
- desire to go deeper
- useful concepts learned
- acceptable amount of scripting or automation
- whether the technology is worth revisiting later

There is no requirement to choose a specialization.

See [`docs/principles.md`](docs/principles.md), [`docs/roadmap.md`](docs/roadmap.md), and [`hosts/shuri.md`](hosts/shuri.md) for the current source of truth.
