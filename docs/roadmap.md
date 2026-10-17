# roadmap

This roadmap describes direction, not a fixed schedule.

The purpose of gusuku is exploration. Later phases may change based on what proves interesting.

## phase 0 — foundation

- define the purpose and design principles of gusuku
- acquire and document shuri
- install Proxmox
- establish basic management access
- document physical networking and storage
- establish a repeatable VM creation process

## phase 1 — core systems

Build a small environment that exposes fundamental enterprise concepts.

Suggested components:

- one or more RHEL-compatible Linux VMs
- Windows Server
- Active Directory
- internal DNS
- Windows client
- basic Linux / AD integration
- shared storage
- segmented virtual networks

Focus areas:

- accounts and permissions
- DNS
- DHCP where useful
- services
- patching
- firewalling
- storage
- troubleshooting

## phase 2 — operations

Add the systems needed to operate the environment rather than merely run it.

Explore:

- monitoring
- centralized logging
- alerting
- backup
- restore testing
- configuration recovery
- documentation and runbooks

Begin intentional failure exercises.

## phase 3 — networking and security depth

Expand into more realistic infrastructure behavior.

Explore:

- VLANs and trunks
- routing
- ACLs
- VPNs
- packet capture
- network troubleshooting
- network segmentation
- least privilege
- vulnerability scanning
- patch management
- Linux and Windows hardening
- STIG concepts
- centralized security logging
- incident investigation

## phase 4 — automation

Automate tasks already understood manually.

Possible tools:

- Ansible
- PowerShell
- Bash
- infrastructure as code

The objective is to evaluate both the usefulness and personal appeal of automation-heavy infrastructure work.

## phase 5 — containers

Start with basic container infrastructure.

Possible progression:

1. Docker or Podman
2. container networking and storage
3. image lifecycle and registries
4. orchestration only if it remains interesting
5. Kubernetes if there is a real learning reason

## phase 6 — cloud and hybrid infrastructure

After traditional infrastructure fundamentals are established, explore Azure and/or AWS.

Focus on infrastructure concepts rather than product collecting:

- compute
- networking
- storage
- identity
- security
- monitoring
- hybrid connectivity

## ongoing — failure and recovery

Periodically introduce failures into the fictional organization.

Examples:

- failed server
- broken DNS
- bad firewall rule
- authentication failure
- inaccessible share
- full filesystem
- expired certificate
- routing failure
- deleted data
- failed storage device
- misconfigured system

For each meaningful exercise:

1. record symptoms
2. diagnose the fault
3. repair the system
4. verify service restoration
5. document root cause
6. record what would make future diagnosis faster

## ongoing — career evaluation

As enough experience accumulates in an area, create a career evaluation based on actual hands-on experience rather than assumptions.

No specialization needs to be chosen early.
