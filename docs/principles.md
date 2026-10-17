# principles

## purpose

gusuku exists to support learning and experimentation in enterprise IT.

It is not optimized for production uptime. It is optimized for learning from building, operating, breaking, troubleshooting, and recovering systems.

## scope

Areas of interest include:

- virtualization
- Linux / RHEL
- networking
- Windows enterprise
- storage
- monitoring and observability
- security
- automation
- containers
- cloud
- backup and disaster recovery

Software development is not a goal.

Scripting and automation are in scope when they are normal tools for infrastructure work.

Radar and RF are not areas of interest.

## design rules

### 1. fundamentals before abstraction

Prefer learning the underlying system before adding abstraction layers.

Examples:

- Linux administration before large-scale configuration management
- switching and routing before software-defined networking
- virtual machines before Kubernetes
- traditional infrastructure before cloud-heavy designs

### 2. troubleshoot before rebuild

Reinstallation is sometimes the correct answer, but it should not become the default escape from a problem.

When practical:

1. identify symptoms
2. collect evidence
3. form a hypothesis
4. test the hypothesis
5. repair the fault
6. verify recovery
7. document what happened

### 3. failure is part of the curriculum

The environment should periodically experience intentional failures such as:

- failed server
- broken DNS
- incorrect firewall rule
- failed authentication
- inaccessible file share
- full filesystem
- expired certificate
- routing failure
- deleted data
- failed storage device
- compromised or misconfigured system

The goal is not just restoration. The goal is to understand why the system failed and how to recognize the failure again.

### 4. build an organization, not a VM collection

Over time, gusuku should become a fictional organization with coherent infrastructure, users, departments, policies, services, and dependencies.

New systems should have a reason to exist within that organization.

### 5. hardware follows requirements

Do not add physical hosts simply to fill reserved names.

A new host should solve a real learning or infrastructure requirement that cannot reasonably be met with the existing environment.

### 6. gusuku is not production

gusuku is an experimental environment. Services, configurations, and platforms running in gusuku should be considered disposable and should not become required parts of the real home environment.

If an experiment proves genuinely useful in day-to-day life, the result should be redeployed on an appropriate fujigoko system rather than promoted in place inside gusuku.

The normal path is:

```text
experiment in gusuku → validate → redeploy on fujigoko if useful
```

### 7. fujigoko remains independent

gusuku may eventually monitor, manage, automate, or interact with selected fujigoko systems for learning purposes.

fujigoko must not depend on gusuku for critical or required services.

A gusuku outage, rebuild, or complete loss should not materially affect normal home operations.

### 8. document useful evidence

Documentation should capture information that would matter when revisiting or rebuilding the environment:

- architecture decisions
- diagrams
- configurations worth preserving
- troubleshooting notes
- incidents
- recovery procedures
- lessons learned
- project summaries

Avoid documenting busywork merely to make the repository larger.

## evaluation

Each major technical area can eventually be evaluated based on actual hands-on experience.

Useful questions include:

- was it enjoyable?
- was troubleshooting it enjoyable?
- what was frustrating?
- is there a desire to learn more?
- how much scripting or automation did it require?
- did the technology make underlying systems easier or harder to understand?
- is it worth revisiting later?

No specialization needs to be chosen.

## certifications

Certifications may be useful as structured learning goals or validation after an area becomes interesting, but they are not the purpose of gusuku.

Possible certifications to consider:

- Security+
- CCNA
- RHCSA
- CCNP Enterprise
- RHCE
- CISSP
- Azure certifications
- AWS certifications
- Kubernetes certifications

They should only be pursued when they add useful structure or validation to something already being explored.

## AI

AI should be used as a tool rather than avoided.

The lab should build enough underlying knowledge to validate AI-assisted work and recognize incorrect output.

Areas can also be evaluated for:

- likelihood of routine tasks being automated
- amount of human judgment required
- value of physical infrastructure knowledge
- value of troubleshooting ability
- ability to use AI to increase productivity
