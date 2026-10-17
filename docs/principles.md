# principles

## purpose

gusuku exists to support learning, experimentation, and career exploration in enterprise IT before military retirement in 2033.

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

Software development is not a career goal.

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

### 6. fujigoko remains independent

gusuku may eventually monitor, manage, automate, or interact with selected fujigoko systems for learning purposes.

fujigoko must not depend on gusuku for critical services.

### 7. document useful evidence

Documentation should capture information that would matter to a future administrator or employer:

- architecture decisions
- diagrams
- configurations worth preserving
- troubleshooting notes
- incidents
- recovery procedures
- lessons learned
- project summaries

Avoid documenting busywork merely to make the repository larger.

## career evaluation

Each major technical area should eventually be evaluated subjectively and objectively.

### subjective

- enjoyment
- troubleshooting enjoyment
- frustration
- desire to learn more
- willingness to do the work professionally
- acceptable amount of scripting or automation

### objective

- Miami-area compensation
- national compensation
- cleared opportunities
- job availability
- average worker age
- typical experience
- career progression
- promotion potential
- remote and hybrid availability
- employment outlook
- AI exposure
- AI leverage
- certification requirements
- education requirements
- on-call expectations
- travel requirements

The goal is to identify the overlap between enjoyable work and a strong civilian career.

## certifications

Certifications validate direction; they do not define it.

Likely certifications to consider:

- Security+
- CCNA
- RHCSA

Possible later certifications:

- CCNP Enterprise
- RHCE
- CISSP
- Azure certifications
- AWS certifications
- Kubernetes certifications

Certification timing should depend on career direction, employer demand, available military funding, and proximity to military retirement.

## AI

AI should be used as a tool rather than avoided.

The lab should build enough underlying knowledge to validate AI-assisted work and recognize incorrect output.

Career areas should also be evaluated for:

- likelihood of routine tasks being automated
- amount of human judgment required
- value of physical infrastructure knowledge
- value of troubleshooting ability
- ability to use AI to increase productivity
- expected durability of the field
