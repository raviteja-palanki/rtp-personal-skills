---
name: alignment-check
version: v1.8.1_latest
description: 'Diagnose whether an AI initiative has a coherent purpose, strategy, capability, architecture, and operating system. Compare stakeholders’ concrete expectations before group discussion, then locate the consequential gaps in ownership, authority, capacity, incentives, design, or execution. Use before a major investment, when a pilot stalls, when inheriting an initiative, or after an operating failure. Produce an evidence-based repair plan with owners and decision points. This is a proportionate diagnostic, not a maturity score or a demand for unanimous agreement. Pairs with problem-type, responsible-ai-program, adoption-launch, stress-test, and judgment-guard.'
imports: []
---

# Alignment Check

Find the gap that prevents an AI initiative from delivering its intended outcome, and identify the smallest credible repair. Examine the organization and technology together rather than assume either is the cause.

The organizing lens is:

**Purpose → Strategy → Capability → Architecture → Systems**

These five links connect the problem, the approach, the ability to execute, the design, and the way the service is run. They are a diagnostic framework, not a proven law that every weakness causes failure. A small experiment needs different readiness from a consequential deployment.

## Begin with the decision and the people who can make it

State the problem, affected users, proposed scope, and decision this assessment will inform. Name the cross-functional owner and what failure or delay would cost. Identify who supplies expertise, who decides, and who can block, stop, or override the decision. Check the actual route of influence as well as the org chart.

Use a deep pass for a major investment, a stalled transformation, or repeated production problems. Use a focused check for an incremental change with relevant evidence from prior execution. An urgent incident calls for immediate containment and a short assessment of authority and dependencies; deeper diagnosis can follow. A committed date is not a reason to ignore a consequential gap.

Use the Universal Skill Protocol for grounding and handoffs, at `ai-pm-skills/UNIVERSAL-SKILL-PROTOCOL.md` in the source library and at the plugin root. Choose inline, document, or presentation according to the user's need; do not interrupt a clear request solely to ask for a format.

## 1. Compare expectations before discussing them

For a consequential cross-functional initiative, ask each relevant stakeholder to give an independent, concrete account of:

- The problem and intended outcome.
- What will change in the workflow, and what will remain unchanged.
- The strategic benefit, costs, constraints, and trade-offs.
- Their own responsibility, required capacity, and understanding of who decides.

Compare the answers before the group conversation. Use the meaningful differences to set the agenda. Writing first is useful because broad verbal assent can conceal different expectations. It does not prove that every verbal agreement is false, or that written statements are complete, candid, and binding. If writing is impractical, use another suitable independent elicitation method and record its limits.

The original source's energy-distributor case reports 10 of 13 executives feeling clear and 8 of 13 perceiving alignment, followed by divergent written descriptions of the future company. That is a single reported case, not a prevalence estimate. See [research notes](references/research-and-limits.md).

### Distinguish three kinds of misunderstanding from a substantive dispute

When IT, AI, or business functions disagree, check their definitions of:

1. **Data:** what counts as data, its boundaries, and how it may be used.
2. **Competence:** which category the issue belongs to and whose expertise applies.
3. **Foundation:** which dependency layer supports the use case and what changes if that layer changes.

Use concrete examples to see whether shared definitions resolve the dispute. Agreement on classification may help, but it does not remove real differences in risk, priorities, incentives, rights, or resources. Reclassification is not a shortcut around a required access or approval process. If disagreement remains under shared terms, address its substance.

**Make the resulting decision visible to affected parties.** A shared manager may settle a dispute in separate private conversations, leaving each function with a different account. Record the decision, rationale, owner, unresolved points, and review conditions in an appropriate shared place. Respect confidentiality; the aim is a common authoritative record for those who need it, not unrestricted disclosure.

## 2. Examine the five links

Assess each as **aligned, partially aligned, broken, or unknown** for the proposed scope. “Aligned” means there is sufficient evidence to act, not that everyone thinks identically. Distinguish observed gaps from hypotheses. Use the [15-question diagnostic](references/diagnostic-questions.md) for a fuller pass, with at least one relevant question for each link.

### Link 1 — Purpose: the problem and outcome

**Question:** do the affected parties understand the problem and the intended change in terms relevant to their work?

Look for a clear problem statement, a meaningful customer need, an outcome thesis, and an explanation of why AI is suitable compared with a simpler approach. The executive sponsor, operating teams, and finance should be able to connect their responsibilities to that outcome. Their wording need not be identical.

Investigate statements such as “competitors are using AI,” an implementation disconnected from the stated problem, or a purpose broadcast without checking understanding. These are prompts to examine the rationale, not automatic evidence that the initiative is wrong. A leader can set a legitimate direction; the assessment asks whether the implications are understood and executable.

### Link 2 — Strategy: the route to value

**Question:** does the approach connect customer value, competitive position, workflow changes, and economics?

Check where AI is expected to differentiate the product and where it supplies ordinary capability. Identify intended segments, the adoption plan, the operations impact, and how sales or other relevant functions will explain the offer. Model costs, volume, benefits, and possible cannibalization or displacement concerns. For an internal service, use the relevant organizational objective rather than force a market-positioning exercise.

Investigate an AI roadmap disconnected from the product plan, an undefined “strategic priority,” uninvolved operating teams, or an assumption of frictionless voluntary adoption. A technical improvement and organizational change may both be needed; use `rtp-problem-type` to separate their dependencies.

**Check the urgency trap.** Is a strategic initiative being reduced to the easiest visible metric—output count, dashboard activity, or one cost line—without an explicit trade-off? Track whether the local measure advances the intended outcome, including rework, workload, customer effects, and who captures the benefit. A narrow security patch or compliance deadline can be the right priority; do not require a broad transformation thesis for every urgent fix. Survey figures behind the original urgency example are retained with their limits in the research notes.

### Link 3 — Capability: skills, authority, and capacity

**Question:** can the people and organization do the work, evaluate it, and change course?

Technical capability may include domain-informed model selection, data engineering, infrastructure, evaluation, product judgment, and operation. It need not mean hiring a separate person for every specialty or training a model from scratch. Match available skills and support to the actual architecture.

Organizational capability includes an identifiable outcome owner, effective decision rights, change support, and the ability to reject or stop an unsuitable use. Examine overloaded roles, ambiguous ownership, unexamined changes to incentives, and gaps in experience. Lack of previous large-scale change is a planning concern, not proof that the team cannot learn.

#### Readiness triad

Assess three complementary conditions:

- **Appetite:** enough commitment and ownership to carry out the agreed scope.
- **Capacity:** time, focus, resources, and resilience to sustain the work.
- **Skillset:** the ability to perform and judge the tasks involved.

Do not average away a critical missing condition. A material skill or capacity gap requires a repair, a narrower scope, or a pause. Partial readiness may still support a bounded learning exercise. This practitioner triad is a useful lens, not a validated score with universal stop thresholds.

Create capacity deliberately: postpone competing work, clarify decisions, reallocate resources, protect focused time, or add capable people where that addresses the constraint. Hiring can help; it does not automatically solve onboarding, coordination, or prioritization. Record who will do the work, how much time is available, and what will be displaced.

#### Accountability versus ability to act

Apply this matrix to a specific decision or outcome, not a person's general seniority:

| | Able to alter, stop, or escalate the outcome effectively | Not able to do so |
|---|---|---|
| **Accountable** | Check whether the authority, information, and response path actually work. | Address the mismatch through authority, an effective escalation route, or a change in the accountability assignment. |
| **Not accountable** | Check whether consequential power lacks clear ownership or controls. | May be an appropriate observer role; check whether the decision as a whole still has an owner. |

The accountable-but-unable cell is important, but it is not the only possible risk. Someone able to change a routing rule without corresponding accountability can also cause harm. A named owner does not need personal permission to reverse every decision: legitimate delegation and pre-agreed closure can limit intervention. Make the boundary, escalation route, and conditions for reopening explicit.

#### Trust and learning

Ask how people expect AI-use records, errors, and shared workflows to be treated. Logging may feel supportive or punitive depending on its purpose, access, incentives, and organizational behavior. A policy and sanctioned tools alone do not establish trust.

The original trust study is a cross-sectional survey of 604 daily AI-using US employees. Its associations cannot prove that adding approved tools causes hiding. Use it to investigate local incentives and behavior, not to predict a universal rate or remove necessary controls. Clarify the purpose of records, who can see them, and how useful contributions and disclosed mistakes will be handled.

People may need different forms of participation. Some need training or a visible benefit; others need a real role in shaping the standard their work will use. Co-design can help, but it does not guarantee adoption or require every participant to agree.

### Link 4 — Architecture: design that fits the task

**Question:** do the technical choices support the actual problem, constraints, and failure consequences?

Examine data availability, access, quality, dependencies, evaluation, monitoring, fallback behavior, and relevant privacy or compliance requirements early. Include operating and domain knowledge in design decisions. Define what happens when an incorrect answer is detected and how unrecognized errors are assessed. A confidence score alone does not contain a failure.

Plan for changing models and task distributions, but do not assume every system must continuously retrain or that degradation is inevitable on a fixed schedule. Improvement might involve retrieval, prompts, tools, routing, interface changes, or a model update. Each needs suitable evaluation before release.

#### Shared-component ownership and re-attachment

A reusable data or context component is a building block consumed by several products or agents. Identify the owner of its business meaning and quality, its technical steward, consumers, change process, and escalation path. Small teams may combine these roles.

**Re-attachment** means transferring ownership and decision rights before a platform migration removes the old system-specific arrangement. Test the transfer: who approves a changed definition, handles a bad shared input, and informs affected consumers? Name the person or accountable role clearly enough that a current person can be found.

The Caterpillar account describes 14 data domains, roughly a dozen VP owners, and monthly quality reports. It illustrates visible domain ownership; it does not establish that every component needs a VP or a monthly report. Choose an appropriate cadence and verify actual ability to act. A consequential ownership gap may need resolution before release, while a documentation refinement need not block a safe experiment.

### Link 5 — Systems: the continuing operating practice

**Question:** can the organization keep the service useful, investigate failures, and improve it responsibly?

Check:

- **Monitoring:** suitable quality, performance, segment, and outcome measures, with a justified cadence and alert policy. Some labels arrive late; “real time” is not always feasible or necessary.
- **Incident response:** an available responder, effective authority, tested rollback or containment, and clear escalation.
- **Improvement:** a way to evaluate proposed changes and release or reject them based on evidence.
- **Feedback:** a process to assess user corrections, identify patterns, and turn valid findings into fixes. Do not automatically train on every correction.
- **Documentation:** purpose, architecture, known limitations, decision history, operating instructions, and recovery guidance that a new team member can use.

Calendar checks, event-triggered reviews, and continuous signals can complement each other. A quarterly retraining schedule is not intrinsically wrong; it is insufficient if it misses the system's real risks. Likewise, more frequent retraining is not an improvement unless data, evaluation, and operating evidence support it.

## 3. Identify the constraint and sequence a repair

1. **Map the links and their evidence.** Record agreements, material differences, operating facts, and unknowns.
2. **Locate the consequential gap.** Do not assume it is organizational or force exactly one weakest link. Several linked constraints may matter.
3. **Trace the mechanism.** Explain how the gap could prevent the outcome: unclear purpose can lead to the wrong feature; a weak strategy can undermine value; missing capability can prevent execution or judgment; unsuitable architecture can expose failures; weak operating systems can leave problems unresolved. These are hypotheses to test against the actual case.
4. **Prioritize by consequence and dependency.** Choose the repair that unlocks the next justified step. A technical fix may build trust; a change in incentives may make existing capability useful. Avoid the claim that work elsewhere can never help.
5. **Sequence and assign.** Purpose-to-systems is a useful reading order, not a mandatory waterfall. Some work can proceed together while a launch boundary remains closed. Name an owner, capacity, date, completion evidence, and review or stop condition for each material action.

## 4. Check durability for larger transformations

### Capability before and during disruption

Ask which capabilities already operate, which have been exercised under stress, and which remain plans. Rehearse important decision rights and recovery paths rather than rely only on a policy or past funding.

Prior preparation can increase resilience, but new capability can also be built during a crisis. A capability does not become real only after a budget cut, and surviving one shock does not prove future resilience. Prioritize preparation against plausible risks and opportunity cost. The UNHCR narrative behind this lens is a single account without a counterfactual; its timing and numerical context are in the research notes.

For a transformation that asks employees to change how they use their expertise, check whether goals, evaluation, data access, rewards, and support enable the new work. Radical targets and fully unified data are not prerequisites for every useful deployment. Match the supporting infrastructure to the actual change before asking people to accept its consequences.

### Leadership and board context

Assess the decision-maker's relevant knowledge and information needs directly. The original five-stage board model—peripheral AI, personal productivity use, AI in governance processes, agents contributing to deliberation, and full delegation—is a conceptual conversation aid, not a maturity ladder to climb.

A board using little AI may still understand its risks through appropriate expertise. Bring a clear business decision, its material technical implications, and the right advisors; do not bypass responsibilities or assume AI literacy from tool use. An AI-generated alternative is not an independent accountable director. The source's full-delegation endpoint is a warning, not an instruction or forecast.

For senior hiring and promotion, ask whether criteria match the role's current requirements: domain competence, judgment, learning, coordination, and execution. Job-description trends do not prove that technical expertise has become irrelevant. Check the counterpart's actual objectives before assuming that an old scorecard no longer applies.

### Continuity when sponsors change

Identify where the initiative depends on a particular executive, and what would need reconfirmation after a transition. Keep rationale, funding, ownership, decision rights, and review conditions in maintained records. Documents and charters can also change; they are not immune to a new leader's decisions.

Use tenure and hiring studies as context, not a countdown for an individual sponsor. Ask internal and external appointees what evidence they need instead of stereotyping their preferences. Bring out relevant differences in a review, but do not require someone to change position to prove that debate occurred. A sound discussion can confirm the original view.

## Output and handoffs

```markdown
## Alignment Check: [initiative and decision]

Purpose and scope: [problem, users, intended outcome, commitment]
Decision rights: [owner, contributors, stop/override/escalation route]
Independent expectations: [material agreements, differences, unresolved terms]

| Link | Status | Evidence and limits | Consequence of the gap | Repair |
|---|---|---|---|---|
| Purpose | | | | |
| Strategy | | | | |
| Capability | | | | |
| Architecture | | | | |
| Systems | | | | |

Priority: [constraint or connected constraints, with reason]
Next action: [owner, capacity, date, completion evidence]
Decision: [proceed, proceed within limits, investigate, or pause exposed scope]
Review condition: [what evidence or change reopens the decision]
Shared record: [where affected parties can find the agreed decision]
```

Use `rtp-problem-type` for technical/adaptive dependencies; `rtp-responsible-ai-program` for program governance; `rtp-adoption-launch` for adoption and shared expectations; `rtp-stress-test` for production evidence; and `rtp-judgment-guard` for effective review and intervention. `rtp-bias-spotter` and `rtp-moat-finder` help when apparent agreement reflects shared inputs rather than independent evidence. Do not invoke every related skill for a narrow assessment.

## Quality and limits

Before handing off, check that all five links have a supported status, at least one relevant diagnostic question has been answered per link, the leading constraint has evidence, the failure mechanism is explicit, and actions have owners and practical capacity. Explain partial alignment using concrete anchors, not only red/green labels.

This assessment need not establish perfect agreement. Its value is a better action, including a small experiment or a justified continuation. One or two weeks of diagnosis is an illustrative budget, not a requirement or a guaranteed three-month saving. Avoid repeating broad planning when a specific test or fix would resolve the uncertainty.

Revisit after a material change to purpose, scope, incentives, leadership, architecture, or operating performance. A quarterly review may fit a larger initiative; choose cadence by need. Finish with the priority repair, the trade-off in time and capacity, the largest unresolved risk, and the next decision point. Add a five-link diagram only if it helps people use the result.
