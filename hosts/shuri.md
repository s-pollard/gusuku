# shuri

## status

planned

## role

First physical host in gusuku.

Initial responsibilities:

- Proxmox virtualization host
- primary platform for gusuku virtual infrastructure

## hardware

TBD

Document confirmed hardware here once selected or installed.

Suggested fields:

- manufacturer / model
- CPU
- memory
- boot storage
- VM storage
- network interfaces
- expansion cards
- firmware / BIOS notes

## platform

Planned hypervisor: Proxmox VE

Version: TBD

## networking

TBD

Document only the actual design once established, including:

- management interface
- bridge layout
- VLANs / trunks
- IP addressing
- physical switch connections

Do not store secrets, passwords, private keys, recovery codes, or other credentials in this repository.

## storage

TBD

Document:

- device layout
- pools / filesystems
- intended use
- redundancy assumptions
- backup relationship

## virtual systems

None yet.

As VMs become persistent parts of the lab, document them separately rather than turning this file into a VM inventory dump.

## backup and recovery

TBD

The eventual documentation should answer:

- what parts of shuri are backed up
- where backups live
- what is intentionally disposable
- how Proxmox configuration is recovered
- how VMs are restored
- what has actually been restore-tested

## notes

shuri should remain capable of being broken and rebuilt without affecting critical fujigoko services.
