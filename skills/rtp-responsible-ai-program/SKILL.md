---
name: rtp-responsible-ai-program
description: 'Build or audit a responsible-AI program that connects principles to product decisions, accountable owners, effective controls, and practical resources. Use the three gaps—accountability, strategy, and resources—to locate problems, then apply SHARP: structure ownership, hardwire ethics, align ethical and business risk, reward responsible behavior, and practice judgment. Test whether people can detect, challenge, change, or stop a harmful use; distinguish written authority from evidence of effective action. Preserve meaningful participation, criteria review, proportionate oversight, and clear disclosure without treating a score or checklist as proof of maturity. Use for enterprise AI governance, program audits, launch-review design, and risk communication. Pairs with safety-as-moat, safety-by-design, dual-lens, and alignment-check. Triggers include "responsible AI", "AI governance program", "ethics program", "SHARP framework", and "accountability gap".'
imports: ["safety-as-moat", "safety-by-design", "dual-lens"]
version: v1.8.1_latest
framework_source: "MIT Sloan Management Review — Öykü Işık & Ankita Goswami, 'The Three Obstacles Slowing Responsible AI', October 2025"
---

# Responsible AI Program

Make responsible-AI commitments usable in real decisions. Establish who owns a risk, how they can act, what evidence they need, and what resources support the work. Then test whether the program changes outcomes when it should.

## Start with scope and the important decisions

Use this skill to build or review governance across a portfolio, product, or organization. Identify the affected people, AI uses, current obligations, decision rights, and material gaps. A quick review can use the three gaps and SHARP assessment. A full pass also examines authority, participation, criteria maintenance, evidence, and an implementation plan.

Scale the program to actual and planned exposure. Pre-product-market-fit, internal use, or no live model is not a reason to ignore consequential data, procurement, design, or employment decisions. A low-risk experiment may need a named owner and simple controls rather than a new department. Compliance is a legitimate objective; meeting obligations is not inherently performative.

Use known context and existing authorization. Ask only for missing information that changes the decision. A governance analysis does not itself authorize changing live permissions, stopping a deployment, contacting regulators, or revising persistent skills. Use the Universal Skill Protocol at the AI-PM library root or packaged plugin root, with a format and depth suited to the request.

For a research-dependent claim, start with relevant `3_Research` maps, indexes, source documents, and available series material. Read the sources needed for that claim; do not make every invocation depend on reading all books or series. Use current primary sources for changing facts. A post or interview can supply a lead, not invented corroboration. State population, date, method, and what the source measured. Multiple articles repeating one study are not independent evidence.

## The framework and its limits

Öykü Işık and Ankita Goswami's **“The Three Obstacles Slowing Responsible AI”**, published online 28 October 2025 in *MIT Sloan Management Review* and included in its Winter 2026 issue, draws on interviews with **over twenty** leaders, ethics officers, and executives across industries. It identifies three recurring gaps and offers five SHARP strategies. This is qualitative research informing practice, not a validated maturity score or a universal prevalence estimate.

The strategies are complementary and **not a fixed sequence**. Establish enough ownership to act, while developing procedures, resources, incentives, and learning together. The numerical assessments, extended authority tests, and twelve failure mechanisms below are this library's adaptations, not all findings of the original study. See [evidence and interpretation notes](references/governance-evidence.md).

| Concept | Meaning |
|---|---|
| Accountability gap | Responsibilities, decisions, and follow-through are unclear or ineffective. |
| Strategy gap | Ethical considerations are disconnected from product choices, business objectives, and resource allocation. |
| Resource gap | People lack the time, competence, tools, access, funding, or standing to perform the required work. |
| Alterability | The ability to influence, change, constrain, appeal, or stop an outcome through a defined mechanism and response time. It need not mean personal override of every case. |
| Prepared versus exercised authority | A role and mechanism may be designed but not yet demonstrated in a relevant case or exercise. Record the evidence level. |
| Detection competence | The ability to recognize a problem requiring action, with access to suitable evidence. |
| Ethical-business risk translation | Connecting harm and obligations to operational and financial consequences where useful, without reducing all ethics to a dollar amount. |
| Checkbox transparency | Treating an explanation's mere presence as sufficient evidence of effective understanding or appropriate use. |
| Negotiated artifact | A document supporting a real agreement about choices and responsibilities. Edits or signatures alone do not establish commitment. |
| Corporate Digital Responsibility (CDR) | Responsibilities associated with digital products and practices, including appropriate external disclosure. It is broader than communicating with regulators. |

## Diagnose the three gaps

For each question, record **evidence, gap, owner, and action**. Use yes/partial/no/unknown/not applicable where helpful. One serious failure can matter more than several completed rows. The old “zero no answers means no gap” and four-question severity bands are descriptive aids, not calibrated tests.

| Gap | Four questions to examine |
|---|---|
| Accountability | Who owns relevant system and enterprise decisions, and is the responsibility understood? Is incident escalation timely for the harm? Do teams know the required launch authority and exceptions? What evidence shows accountable follow-through, including justified approvals, changes, remediation, or lessons? |
| Strategy | Is there a usable strategy with goals, owners, and review triggers? Do risk considerations shape design and release as well as post-launch learning? Can teams connect values to actual decisions? Are prohibited or conditionally permitted uses and their trade-offs explicit? |
| Resources | Can the appropriate function require a change, delay, or stop? Is sufficient technical and domain expertise available? Are evaluation, red-teaming, fairness work, and remediation funded where needed? Does review effort and capacity match risk and volume? |

Inspect the current workflow, not only its documents. The original one-hour incident ownership, twenty-four-hour escalation, and twelve-month accountability lookback are examples; choose windows that fit the service and evidence. A board or committee can hold real accountability when its mandate and decisions are clear. Name operational owners without assigning one person responsibility for everything they cannot control.

## Apply SHARP

### S — Structure ownership at the project level

Assign a clear owner for each material AI use and connect them to the product, domain, technical, legal, risk, and executive functions needed to act. A dedicated chief AI ethics role is one option; an existing role or federated model can work. What matters is responsibility, capability, and access to decisions, not the title.

Define three levels of responsibility:

1. **Product/team:** assess the use, implement controls, maintain evidence, and surface changes or incidents.
2. **Specialist review:** challenge material risks with sufficient independence and technical/domain competence, and exercise the authority assigned to it.
3. **Enterprise leadership:** set risk posture, fund the program, resolve material cross-team decisions, and oversee applicable obligations.

Record who may approve, require redesign, restrict scope, suspend operations, accept residual risk, and authorize resumption. Make the escalation and appeal path usable. A stop requiring agreement from the person whose launch is at issue may be too slow or conflicted; design emergency authority and normal governance deliberately.

An independent reporting line can reduce conflicts but is not the only workable design. Protect challenge and escalation while retaining access to the work. Technical expertise and organizational independence can coexist. Do not present a choice between a captured reviewer and an uninformed reviewer as unavoidable.

For agents, name responsibility for updates, training/tuning, token use, deployment/embedding, bias controls, and compliance, and add explicit authority for containment and resumption. Determine the effective permissions of agent credentials or delegated sessions. A distinct machine identity can improve attribution; it neither guarantees least privilege nor is the only mechanism for enforcing it.

### H — Hardwire ethics into everyday procedures

Integrate risk work into the actual lifecycle: **discovery/procurement → design/build → trial/release → operation/change → retirement**. Define which checks are required, which can be self-served, and which need specialist review. Escalate a serious unresolved issue before the decision that creates exposure, rather than waiting until launch.

Use the original five assessment dimensions as prompts:

| Dimension | What to establish |
|---|---|
| Affected people | Internal/external users, non-users, vulnerable groups, scale, and distribution of effects. Internal use is not automatically low risk. |
| Decisions influenced | Information, access, resources, rights, safety, and external actions, including indirect influence. |
| Failure consequences | Severity, likelihood/uncertainty, detectability, reversibility, and who bears the harm. |
| Human role | Actual decision rights, review effectiveness, capacity, and recourse. A human in the loop is not automatically a risk reduction. |
| Data/model provenance | Rights, suitability, known limitations, documentation, and what is unavailable from suppliers. Full documentation alone does not establish safety. |

Create a local routing rule from these dimensions and applicable obligations. The original “any medium → ethics review; any high → chief officer sign-off before development” is a possible organizational policy, not a universal legal classification. Set thresholds and authority for the organization; do not confuse a library risk label with a statutory category.

Place the required checks in relevant PRDs, design reviews, deployment controls, and change processes. Enforce the boundary where necessary. An automated control can prevent a problem and supply evidence; a checklist can support a reliable routine. Neither should be dismissed merely because it is embedded or standardized. Check effectiveness, bypass paths, exceptions, and review capacity.

Involve affected teams and communities where their knowledge or interests matter. Ask them to test responsibilities, workload, and consequences. A team can thoughtfully accept an artifact unchanged; cosmetic edits can occur without commitment. Confirm usable agreement through an actual decision, allocation, or working practice rather than requiring every document to come back altered.

### A — Align ethical risk with business risk

Explain the harm first, then its relationship to business objectives, costs, trust, and obligations. Financial estimates can help allocate resources, but credible qualitative evidence can justify action. Avoid invented fines, churn, or reputation values, and do not let a profitable outcome excuse a prohibited or unacceptable practice.

| Risk example | Business connection to investigate | Evidence boundary |
|---|---|---|
| Bias in credit decisions | Customer harm, complaints, remediation, enforcement and litigation exposure. | Determine actual jurisdiction and decision process; a precedent fine is not this product's expected loss. |
| Misleading AI content or disclosure | Harmful reliance, contractual concerns, trust, applicable consumer protection. | Whether disclosure is required and useful depends on the use; no generic FTC fine applies to every omission. |
| Improper training/data use | Rights, contractual restrictions, privacy duties, remediation. | Consent is not the only possible legal basis, and its presence does not settle every duty. |
| Discriminatory hiring systems | Applicant harm, talent exclusion, employment-law exposure. | Assess the actual decision and affected population with relevant expertise. |
| Silent medical-system failure | Patient harm, service disruption, liability, and applicable oversight. | Device status and other obligations depend on the system and jurisdiction. |

Use ranges with assumptions, time horizons, and uncertainty. Separate statutory maxima from likely exposure and avoid double-counting churn, lost revenue, and reputation. A comparison such as $50,000 annual review cost against $500,000–$50 million enforcement exposure is an illustrative prompt, not an ROI case without probability, effectiveness, and full cost.

Apply `dual-lens`: inspect what the organization can change in design and operations, and the external conditions it must respond to. The outer world includes affected people's experience, competition, law, and public scrutiny—not only whether misconduct gets exposed.

**Transparency and review.** Determine what an explanation must accurately communicate, who needs it, and how it supports understanding, challenge, or recourse. Where the system relies on review, test its effectiveness. A click or logged acknowledgment is not proof of comprehension; forced review is not always the right intervention. Check explanation accuracy against the actual decision evidence, not merely against another generated explanation. Wording can legitimately differ while remaining faithful.

**Approval behavior.** Examine approval rate, time, case difficulty, error incidence, evidence access, and outcomes together. Above 95% approval in under sixty seconds is a historical screening heuristic, not a validated rubber-stamp threshold. A refusal that prevents execution is a real control. A low refusal rate can reflect good upstream work.

**External disclosure.** Match content to what customers, partners, regulators, and affected people need and are entitled to know. Specific evidence is better than vague assurances. Do not assume customers never value safety, that visible disclosure always harms conversion, or that early disclosure guarantees regulatory leniency. Honor obligations and explain relevant limitations even when the commercial effect is uncertain. Connect the use inventory, design-time oversight, and truthful disclosure; disclosure must describe controls that actually operate.

The original accountability-selection lens distinguishes foreseeable harms, harms attributable after the fact, and diffuse/slow harms. Use it to combine clear responsibility, appropriate incentive design, public commitments where warranted, monitoring, and redress. These are not mutually exclusive mechanisms, and no harm category eliminates the need for accountable ownership.

### R — Reward responsible behavior

Support useful challenge, early reporting, careful implementation, and remediation alongside delivery. Make the expectation concrete in performance reviews, retrospectives, recognition, and promotion criteria where appropriate.

- Recognize a substantiated risk raised in good faith, including one that leads to redesign or a justified delay.
- Review whether required assessments improved decisions, not just whether forms were submitted without prompting.
- Record near misses accurately; reporting a risk does not automatically prove a harm was prevented.
- Fund remediation and give reviewers time and access to do the work.
- Examine both what an owner gains from success and the pressures or personal costs of raising concerns or stopping work.

Do not require personal financial punishment to establish accountability. Avoid incentives that reward incident concealment, excessive blocking, or performative extra review. A separate award or bonus can be appropriate if designed well; it is not inherently incompatible with making responsibility part of the job. Good-faith reporting and actual misconduct should be handled distinctly and fairly.

### P — Practice ethical judgment as well as compliance

Use real cases, representative exercises, and relevant external incidents to strengthen judgment and reveal gaps. Compliance knowledge remains necessary; judgment helps interpret and apply it where facts, interests, and uncertainty require thought.

The original practice options are useful starting points:

- **Team case review:** for example, thirty minutes monthly. Discuss what happened, who was affected, alternatives, assumptions, and a useful change. Capture a learning when there is one; no slides or a written worksheet are format choices.
- **Cross-functional tabletop:** for example, quarterly. Product, engineering, legal, communications, risk, and leadership rehearse a material scenario and the first twenty-four hours, safely and within authorization.
- **Executive portfolio review:** for example, annually and at material change. Review exposures, incidents, near misses, obligations, and uses to retain, redesign, restrict, or retire.

Set cadence and participation from risk, volume, and learning needs. Senior leaders need meaningful involvement, not attendance at every team session. Measure the relevant capability or decision improvement; practice is not a guaranteed cure for skill loss. External cases can be valuable when adapted to the team's context.

## Test authority beyond the org chart

Ask four questions: **Who can act? Do they know? Can they exercise the authority when priorities conflict? What pressure or personal cost could inhibit that action?** Then examine the evidence.

Effective governance combines technical means, accountable decision rights, detection competence, and capacity. Missing any can matter; there is no universal ranking that makes one missing element always worse than another. Some controls act automatically, some through people. A visibility tool can support action when connected to a real process.

For material decisions, trace the recommendation, challenge, evidence, decision, enforcement, and outcome. Sample senior as well as frontline roles when relevant. An accountable person may act through escalation, delegation, appeal, or system-level constraints; personal override is not always appropriate. Refusal or delay must be distinguishable from an action that continued anyway.

Review real stops, delays, redesigns, justified approvals, and remediation over a relevant period. The original twelve-month spot check and eight-quarter review are options. Interpret the evidence against the cases that warranted intervention and the work done before submission. Zero stops can mean no problematic case, effective early design, an untested control, or a failure; a count alone cannot choose among them. One stop also does not prove general effectiveness.

Use controlled exercises when no suitable live case exists. Record intervention events as evidence without setting a target number of stops. Routine tracking can be useful if interpreted responsibly; Goodhart's law is a risk to manage, not a reason to make governance effects unobservable.

Check what the body still decides and how authority changes. A lack of disagreement is a prompt for inquiry, not proof that governance ended. A common reporting parent, an agile charter, a new platform, or a promotion can preserve or improve controls. Examine the actual transfer and enforcement of authority.

The [twelve-mechanism review](references/authority-and-participation.md) preserves the library's detailed failure patterns as hypotheses to test, including prompt changes, restructuring, encoded criteria, legitimate decision closure, exemptions, jurisdiction, and embedded controls. Review accountability when roles are deleted or reassigned as well as when reporting lines change.

For external models, the deployer may not control model weights or the provider's business decisions, but can restrict use, permissions, inputs, routes, contracts, and exposure. Provider switching is one option, not the only available control. Record actual model identity and authorized fallback paths with `tool-architecture` and `production-observability`.

## Preserve the second-order job

A decision body may both handle cases and develop the criteria used to judge them. Automation can reduce incidental opportunities to question those criteria, but that loss is not inevitable.

| Body | Case-level work | Possible second-order work |
|---|---|---|
| Credit committee | Approve or decline lending. | Reconsider standards, assumptions, and distribution of access. |
| Promotion committee | Evaluate candidates. | Discuss merit, context, and fairness. |
| Compliance function | Apply requirements. | Resolve ambiguity and update interpretation. |
| Design review | Assess a proposal. | Refine quality standards and user needs. |

Before automating case work, name any valuable second-order function, assign an owner and review trigger, and feed it relevant edge cases, overrides, incidents, and stakeholder feedback. Record the decision and rationale, including a justified decision to keep criteria unchanged. A standing review can help; it does not need to occur on an arbitrary cadence or manufacture changes. Stable criteria may remain appropriate.

This connection matters for eval rubrics, definitions of done, autonomy limits, and tracking plans as well as formal governance. Criteria embedded in software remain inspectable and revisable if the process makes that possible.

## Assess and prioritize without hiding critical gaps in a score

An optional SHARP profile can use **0 = absent, 1 = partial, 2 = implemented with evidence**, with unknown/not applicable recorded separately. Describe the evidence for ownership, routine controls, risk alignment, incentives, and practice. A total out of ten is descriptive, not proof of maturity, compliance, or readiness. The original 0–2/3–4/5–7/8–10 maturity bands were not validated and should not govern a release.

Prioritize urgent harm and obligations, then dependencies, expected improvement, feasibility, and capacity. The lowest score is not automatically the first task. Establishing an accountable owner may unlock work, while urgent containment or a legal requirement may need immediate action alongside it.

Use a ninety-day plan if helpful: first establish scope and urgent controls, then implement and exercise the relevant procedures, then review operating evidence and remaining gaps. Tailor timing rather than promising a mature program in one quarter. A weak sponsorship commitment is a finding to address through concrete decisions and resources, not a reason to produce a fictitious complete program.

```markdown
# Responsible AI Program: [Organization / product]
Decision and scope: [uses, affected parties, objective, applicable obligations]

## Three gaps
Accountability: [evidence, material gap, owner]
Strategy: [evidence, material gap, owner]
Resources: [evidence, material gap, owner]

## SHARP profile
S — Ownership and decision rights: [evidence, action]
H — Lifecycle controls: [evidence, action]
A — Harm/business connection and disclosure: [evidence, action]
R — Incentives and reporting: [evidence, action]
P — Practice and criteria maintenance: [evidence, action]
Optional scores: [definitions, unknowns; no readiness inference from total]

## Authority and participation
Detection → decision → enforcement → recovery: [roles and tested mechanisms]
Cases/exercises: [interventions, justified approvals, limits]
Agreement and capacity: [receiving teams, commitments, unresolved concerns]
Authority changes and criteria review: [owner, triggers, evidence]

## Priority plan
Action | Why now | Owner/resources | Evidence of completion | Review date

Material risks and trade-offs: [harm, ranges where justified, assumptions]
Not yet demonstrated: [gaps and limits]
Next decision: [owner, evidence needed, scope]
```

`safety-by-design` implements technical controls; `agent-risk` examines authority and containment; `judgment-guard` examines human contribution; `alignment-check` supports operating agreement; `safety-as-moat` tests commercial value. These layers develop together. External claims should follow the evidence rather than precede functioning controls.

Close with the recommendation, material trade-off, main uncertainty, and next action. Use a visual only when it clarifies decision rights, lifecycle gates, or the connection between governance and implementation. If this review reveals a reusable skill defect, record it for an authorized revision rather than automatically editing persistent instructions during every invocation.
