# shuri

## status

Packed / offline. Proxmox conversion planned after unpacking.

This physical system was previously documented as `saiko` in the fujigoko repository. It is now part of gusuku as `shuri`.

## role

First physical host in gusuku.

Initial responsibilities:

- Proxmox virtualization host
- primary platform for gusuku virtual infrastructure
- enterprise infrastructure experiments
- temporary and disposable lab workloads

shuri is not a production host. If something tested here becomes useful for the real home environment, it should be redeployed on an appropriate fujigoko system.

## hardware

- chassis: existing 4U system
- CPU: AMD Ryzen 9 3900X
- memory: 32 GB DDR4
- motherboard: MSI MPG X570 GAMING EDGE WIFI
- GPU: EVGA GeForce RTX 3060 Ti FTW3 ULTRA GAMING 8 GB
- currently documented storage: WD Blue 500 GB SSD
- network upgrade: Intel X520-DA2 dual-port 10 GbE SFP+ adapter ordered

Additional storage and hardware details should be documented only after they are confirmed.

## platform

- current platform: Bazzite
- target platform: Proxmox VE
- Proxmox version: TBD

## networking

Detailed gusuku network design: TBD.

The ordered Intel X520-DA2 provides the planned 10 GbE network upgrade.

Once established, document:

- management interface
- bridge layout
- VLANs / trunks
- physical switch connections

Exact private addressing and sensitive operational identifiers should remain outside this public repository.

Do not store secrets, passwords, private keys, recovery codes, or other credentials in this repository.

## storage

Current confirmed storage documentation is limited to the WD Blue 500 GB SSD.

The final Proxmox storage design is TBD.

Document the actual design once established, including:

- device layout
- pools / filesystems
- intended use
- redundancy assumptions
- backup relationship

## virtual systems

None yet.

Potential workloads include Linux and Windows VMs, virtual networking and firewall labs, container experiments, monitoring, identity services, storage labs, and other temporary enterprise infrastructure exercises.

As VMs become meaningful parts of the lab, document them separately rather than turning this file into a VM inventory dump.

## backup and recovery

TBD.

The eventual documentation should answer:

- what parts of shuri are backed up
- where backups live
- what is intentionally disposable
- how Proxmox configuration is recovered
- how VMs are restored
- what has actually been restore-tested

Because gusuku is experimental, complete rebuilds are acceptable and may be intentional learning exercises.

## boundary with fujigoko

shuri must remain capable of being broken, wiped, powered off, or rebuilt without affecting required fujigoko services.

Experiments may interact with selected fujigoko systems when useful for learning, but fujigoko should never require shuri to remain available.
