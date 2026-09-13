# Agent Ecosystem — Research and Operating Notes

Editorial review: 13 September 2026. Distinguish primary benchmark results, practitioner accounts, and this library's transfers from human organizations to agent systems. A useful analogy does not establish identical mechanisms or effects.

## Model and agent diversity

[Diversity Empowers Intelligence](https://arxiv.org/abs/2408.07060), August 2024, studies a committee and selection approach over software-engineering agents. It reports 34.3% resolved on SWE-Bench Lite for an open-agent committee versus 27.3% for the best individual member: seven percentage points, approximately 25.6% relative improvement. The paper studies different agent frameworks and candidate solutions, not a controlled finding that cross-lab models are the only source of complementary errors. Its tables include shared model families and repeated runs, and its selection method matters. Do not label the result an independent audit of every underlying company system or a general production reliability result.

[Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity](https://arxiv.org/abs/2602.03794), February 2026, explicitly includes different models, prompts, and tools in its concept of heterogeneity. It reports that two diverse agents can match or exceed sixteen homogeneous agents on its evaluated tasks. It does not establish that any two diverse agents beat any sixteen others, or that different laboratories are necessary and sufficient. Its effective-channel framework and measurements are research tools with assumptions, not a universal procurement test.

A role prompt alone does not guarantee complementary information. It can nevertheless change behavior; so can retrieval, tools, sampling, architecture, or external verification. Test the actual combination's joint errors and outcomes. Different vendors may share common errors or dependencies. A single-vendor system can be useful, and a cross-vendor system can add integration, cost, privacy, and availability problems.

The human-musician analogy in the prior skill comes from Deshmane and Martinez-de-Albeniz's August 2026 HBR discussion of more than 4,200 musicians over fifteen years. The reported national-background versus craft-specialization contrast is observational; attention is not the same outcome as error independence or work quality. Selection and prior opportunities may matter. Do not infer that national origin determines a person's perspective, that role differences cannot add value, or that the finding proves how to choose model vendors.

## Multi-agent failure evidence

[Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657) reports task failure rates of 41–86.7% for seven evaluated open-source systems and describes 1,642 annotated execution traces. It organizes fourteen failure modes into three broad categories. That is a studied benchmark setting, not the failure rate of all deployed agent systems. The main skill's six-part operational checklist is its own practical taxonomy, not a verbatim copy of MAST.

The earlier 40–80% practitioner claim may be a retelling of related evidence. Do not count it and MAST as independent confirmation without tracing the sources. Nor does the quoted range establish that races are the largest failure category, that coordination always dominates capability, or that a narrow per-agent evaluation alone makes a system ready.

## Protocol and distributed-systems references

The [A2A v0.3.0 specification](https://a2a-protocol.org/v0.3.0/specification/) illustrates the distinction between agent discovery and the authentication/authorization mechanisms needed for interaction. Use the actual version implemented; do not mix fields or requirements from development and released specifications. An agent's declared identity or capability is not self-validating evidence of permission or trust.

[AWS guidance on idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) explains why retries need to account for repeated side effects and unknown completion. [Backoff and jitter guidance](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) describes spreading retries rather than synchronizing repeated load. Apply the ideas to the actual service semantics, deadlines, and budgets; copying a retry interval does not ensure recovery.

[PostgreSQL's explicit-locking documentation](https://www.postgresql.org/docs/17/explicit-locking.html) describes lock behavior and deadlock risks, including consistent ordering of multiple locks. This is an implementation example; use the guarantees of the chosen storage system. [The CRDT overview](https://arxiv.org/abs/1806.10254) provides the broader research context for replicated data types and their semantics. A convergent structure still needs application invariants.

## Implicit work and reusable platforms

The prior Ramp expense-agent example reports 10–15% escalation and roughly 85% less manual review. Treat it as a company account with a specific workflow, denominator, and period to verify. Escalation rate and reduction in review effort are different measures, and neither proves complete capture of tacit work. Expense approval can have fraud, financial, employment, or policy consequences; it is not universally low-stakes.

Himmelreich, Oshri, Scala, and Zaidani's August 2026 HBR procurement discussion motivates repeatable components, business ownership, and attention to valuable bottlenecks. It is practitioner interview evidence without a comparative estimate that every subsequent agent costs less or that late entrants cannot catch up. The organization's eighth agent can inherit assets and also accumulate maintenance and coordination costs.

Reuse may justify a common platform; a small project may benefit from a lighter approach. Business functions need ownership of outcomes, while technical and governance owners retain their legitimate decision responsibilities. Moving people into ecosystem curation is one staffing possibility, not a universal prediction or a complete redeployment plan.

## Human collaboration and governance analogies

**Global-team design.** The July 2026 HBR global-collaboration discussion distinguishes time zones, language, and country culture from headquarters/region dynamics, company culture, market knowledge, and process. The captured chart was unavailable, so the old two-bucket ranking came through prose. These factors have different degrees of control; they are not permanently unchangeable versus completely redesignable. Staffing, translation, overlap hours, architecture, and contracts can change exposure. Examine recent failures instead of declaring one column the true cause by definition.

**Group use of an assistant.** Rosani, Farri, Trabucchi, and Buganza's May 2026 HBR account describes five months, sixty managers, twelve companies, teams of three or four, and thirty hours of sessions. The local record reports no control group or measured outcome effect. Introducing team context, varying the assistant's role, and reviewing prompts together are practices to test. A five-minute introduction or fifteen-minute challenge period is the library's example, not a validated intervention dose.

**Familiar configurations.** A May 2026 single-hospital HBR account reports operating-time differences of twenty to forty minutes and a familiarity-focused pilot moving on-time starts from 85% to 96%. That is eleven percentage points, about 12.9% relative improvement in the on-time-start rate. It does not isolate familiarity as the cause or measure agent configurations. The engineering transfer is to track combinations and evaluate changes, not to assume unfamiliar components must always be unsafe.

**Several commercial motions.** The June 2026 HBR digital-strategy typology describes digital-first, hybrid, and relationship-led approaches; an example relationship account team has seven or more roles and one digital assistant. These are not required staffing counts or distinct agent-rights regimes. A shared policy framework can support differentiated workflows. Error consequence, data, reversibility, affected people, and actual authority determine permissions more directly than commercial motion.

**Bridging ownership.** Linda Hill's research discussion is described in the earlier skill as spanning twenty-four industries and twenty-three countries. It motivates attention to translation across organizational boundaries; the machine-handoff comparison is the library's analogy. Separate consultancy claims about greater attrition among bridge roles have no disclosed scale or reproducible method in the skill. Check workload and authority; do not present higher burnout, departure, or fabricated explanations as a proven consequence for a specific person.

## Ecosystem value and provider alternatives

The four categories—identity/discovery, trust/reputation, insurance/repair/legal, and micropayments—come from a July 2026 MIT Sloan talk by a researcher whose initiative could benefit from the forecast. The talk offered a taxonomy without comparative economic data. Keep the categories as opportunities to assess, not a prediction that value must move away from agents into these layers. Even a closed ecosystem can purchase external identity, payment, or insurance services.

The Accenture/MIT SMR sovereign-AI survey cited 1,928 executives. It is a commissioned survey, not legal authority and not proof that every regulated jurisdiction has only one eligible provider. Verify the specific deployment and contract with the responsible experts. Technical interface compatibility does not establish legal, security, commercial, or functional substitutability. The same check matters outside formal residency regimes.

## Novel Insights applied

The ledger's shared-workspace/shared-retrieval distinction suggests comparing information sources separately from collaboration channels. Shared retrieval can correlate results, but it does not force identical thinking; different retrieval does not guarantee better evidence. The associated human studies do not prove a cross-lab-only agent rule.

The dissent entries distinguish generated objections from independent evidence that a concern occurred. Retain that distinction while allowing an AI argument to reveal a testable issue. The handoff-value entries motivate measuring downstream realization, but escalation rate is not literally handoff count: one escalation can involve several handoffs, and ordinary handoffs may not be escalations. Avoid a universal productivity haircut based on the number of seams.
