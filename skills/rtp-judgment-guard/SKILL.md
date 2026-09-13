---
name: judgment-guard
version: v1.9.1_latest
description: 'Design where human judgment belongs in an AI workflow, how it remains effective, and how its contribution will be tested. Distinguish loss of expertise, failure to develop it, poor transfer to review, passive reliance, motivated avoidance, suppressed dissent, and framing that arrives too early. Choose proportionate checkpoints for practice, calibration, independent judgment, repair, reasoning records, and safe disclosure. Use when expert work changes, people stop questioning AI, or consequential decisions need effective human oversight. Compare human-only, AI-only, and combined performance where feasible; do not assume human involvement always improves outcomes. Pairs with determinism-compass, autonomy-spectrum, trust-ladder, agent-risk, and capability-tracking.'
imports: []
---

# Judgment Guard

Decide which human capabilities and decision rights a workflow needs, then design the work so those capabilities can be developed, exercised, and assessed. Human involvement should have a clear purpose and an effective role.

This skill addresses two connected design questions:

- **Case 1 — Capability and judgment:** is the workflow changing what people can learn, notice, evaluate, or say? If a useful capability is at risk, choose a remedy that fits the mechanism.
- **Case 2 — Human–AI complementarity:** does a particular division of labor improve the outcome, satisfy an applicable requirement, or manage a consequence that another design does not? Test the contribution rather than assume that the combination is always better.

Adoption does not inevitably remove the human, and automation does not always erode a valuable skill. The task is to make the change deliberate and inspect its consequences. A capability may be worth preserving, worth rebuilding, or intentionally retired; those are different decisions.

## Start here: role, consequence, authority, and evidence

Before prescribing a checkpoint, state:

1. **The decision and role:** what judgment is needed, who currently exercises it, and what changes with AI? Separate the expert who produces work, a trainee learning it, a reviewer, and an accountable decision-maker.
2. **The consequence:** what can go wrong, who is affected, how quickly harm can occur, and whether it can be detected, reversed, or recovered from. Include the cost of delay or unnecessary intervention.
3. **The authority:** who can approve, refuse, stop, correct, or escalate? Respect the user's constraints and verified requirements for the actual jurisdiction and use. This skill does not create a universal legal rule that every regulated decision needs the same permanent human loop.
4. **The capability objective:** which skills must remain available, to whom, and for what future task or fallback? Do not preserve manual work solely because it existed before automation.
5. **The evidence:** what would show capability loss, useful learning, effective review, or added harm? Establish a baseline and a way to compare outcomes before interpreting adoption or override rates.

Use the Universal Skill Protocol for grounding and handoffs. It is at `ai-pm-skills/UNIVERSAL-SKILL-PROTOCOL.md` in the source library and at the plugin root. A focused design can be delivered inline.

**Keep these distinctions near the decision:**

- Lower override rates may reflect better AI, changed cases, less engagement, suppressed reporting, or unnecessary deference. They do not diagnose atrophy on their own.
- Stable human performance while AI improves is a widening relative gap, not evidence that the human has lost capability.
- Assisted output quality does not establish unassisted ability, and unassisted skill does not guarantee skill at supervising AI.
- An explanation being available or opened does not prove that someone understood it or detected an error.
- Agreement between a human and AI is stronger evidence only to the extent that each supplies relevant information and their errors are not merely shared.

The original fixed loss and recovery timelines, compulsory review percentages, and numerical warning thresholds are retained as historical examples in [calibration and evidence notes](references/calibration-and-evidence.md). They are not general laws or default requirements.

## Prepare the disclosure condition first — Checkpoint 6

The checkpoint numbers are retained for compatibility with the rest of the library. **Checkpoint 6 comes first in use** because the other checks may depend on records people choose to provide.

Ask whether people can raise a concern in the decision-making group, whether they can say that a concern was dismissed, and what happens next. Give them a usable route to challenge, investigate, or escalate a consequential issue. Check that the recipient has time and authority to respond. Clear accountability without practical ability to act can produce poor decisions even when people speak candidly.

A two-question comparison can help investigate the group:

| Ability to raise a concern | Ability to discuss its dismissal | What to investigate |
|---|---|---|
| High | High | Whether the concerns receive a sound disposition and necessary action. |
| High | Low | Whether objections can be voiced but not effectively challenged after rejection. |
| Low | Low | Whether fear, incentives, access, or process suppress relevant information. |
| Low | High | Whether the items refer to different situations or are interpreted differently; do not dismiss the result as an artifact without checking. |

This is a proposed diagnostic, not a validated scale. Phrase questions about the relevant group and decision setting. High reported candor does not certify that the record is complete; private/public differences can reflect learning or different interpretations as well as suppression.

Respond to mistakes and rule departures with both investigation and proportionate accountability. The original research distinguishes self-interested, prosocial, situationally pressured, and principle-driven motives. These help explain what happened; they do not excuse harmful behavior or settle legal consequences. Do not promise immunity, assume punishment is always required, or turn a disclosure into a forced confession. Follow applicable obligations while preserving a fair route to report errors and improve the system.

Where useful, keep an optional dissent record: “I proceeded under the decision, and my unresolved concern is…” Make it accessible to an appropriate reviewer beyond the person whose decision is challenged. An empty optional field is ambiguous, not evidence that all is well. Required decision or incident records should still be completed truthfully; do not require invented disagreement to fill a form.

## Case 1 — Diagnose what is happening to judgment

The original numbering is historical, not a timeline. Use it as a shared vocabulary, not a validated taxonomy. More than one mechanism may be present.

| ID | Mechanism | Distinction and first check |
|---|---|---|
| **0 — Thinkslop** | Intent, criteria, or reasoning are outsourced before they are adequately formed. | Ask what the person needs to decide and what a good answer must satisfy. Open-ended exploration may legitimately start without a fixed view. |
| **1 — Individual atrophy** | A previously demonstrated, still-needed capability weakens through changed practice or other causes. | Compare relevant capability over time under comparable conditions; do not infer loss from AI adoption alone. |
| **2 — Non-formation and organizational capability loss** | People no longer get suitable opportunities to develop expertise, or the organization removes the people and practices that sustain it. | Map how newcomers learn and how existing experts stay calibrated. These may need different designs. |
| **3 — Handoff degradation** | Errors, omissions, or weak assumptions travel through summaries and delegated steps. | Trace important claims and decisions to the source and check end-to-end fidelity. A handoff can also correct an error. |
| **4 — Offloaded ownership** | People feel less responsible for evaluating a result because AI appears to own the work. | Examine responsibility, meaning, incentives, and observable review behavior. Anthropomorphic framing is one possible influence. |
| **5 — Motivated avoidance** | A person avoids information because engaging with it may create an unwelcome cost or conflict. | Separate unavailable, unusable, misunderstood, and deliberately avoided information before assigning a motive. |
| **6 — Suppression** | A relevant concern or judgment does not reach, or survive, the decision process. | Compare how views are formed, voiced, heard, and acted on; use the disclosure check above. Private confidence does not establish correctness. |
| **7 — Pre-emption** | An early AI or senior-person framing prevents an independent view from being exercised. | Check the order of information and judgments. A summary can be accurate yet incomplete for the decision. |

**Also test misapplication:** someone may have strong task expertise and actively intervene yet make the assisted result worse. Producing, directing, and reviewing are different operations. Compare relevant baselines and teach the new role rather than automatically prescribe more of the old task. Misapplication overlaps several drains but is not the same as atrophy or non-formation.

### Preserve formation, retention, and transfer separately

The three original “clocks” remain useful as scales of inquiry: change within a person, change in an organization's future supply of expertise, and change along a chain of handoffs. Their rates depend on the task, practice, feedback, and design. Do not forecast universal 6–18-month decay or a fixed recovery period.

Ask how a capability is acquired and maintained through production, observation, interrogation, feedback, and peer relationships. Useful options include:

- A senior and junior examining a concrete work product together, with the junior making a prediction or explaining what they think matters before feedback.
- Experts continuing selected production or difficult reviews, with outcomes that let them update their judgment.
- Protected practice on representative and boundary cases, rather than only repetitive easy work or only rare exceptions.
- Communities where people can ask colleagues, contest embedded rules, and compare interpretations.

A senior's signature is not an apprenticeship. Narration can help, but a concrete case and the learner's response make understanding easier to assess. Interrogating someone else's work may preserve some expertise; producing every artifact personally is not the only plausible route. Test the learning result for the role rather than declare one route universally necessary.

The **formative-task test** asks whether doing a task contributes to a capability the person still needs to evaluate future work. The earlier “could not evaluate it without having done it” formulation is a useful prompt, not a complete test: comparable practice, observation, or another task may supply the learning, and the old skill may be obsolete.

Keep the four named capabilities visible where relevant: **judgment under uncertainty, systems thinking, ethical escalation, and interpretive reasoning**—understanding a situation through a chosen strategy. Check three kinds of erosion: less active reasoning, important criteria buried inside systems, and weaker relationships through which people formerly learned or corrected mistakes. Use `rtp-needs-guard` when changes affect meaningful connection or agency.

### Map what a role carries before automating it

An entry-level role may produce work and provide practice, observation, and feedback. A middle-management role may carry oversight, escalation, and coordination. Removing the role can remove more than its visible output, but that is a hypothesis to inspect, not a reason to preserve every role unchanged.

Name each useful function, decide whether it is still needed, and show where it will live. Some coordination may become unnecessary; some learning or oversight may need replacement capacity. The 70–20–10 learning framework does not imply that automating an entry-level task removes 90% of development. Route the workforce plan to `rtp-capability-tracking`, including the optional question: “What oversight capacity does this role provide that our current measures miss?”

### Protect source access and the order of reasoning

For a chain of AI-assisted work, identify a **source of record**: the original document, transcript, data, or other appropriate evidence with its own reliability limits. Preserve accessible references and versions. A source can be wrong; a citation makes a claim traceable, not automatically true. Three unreviewed handoffs is a useful example to inspect, not a threshold below which fidelity is safe.

For one summary serving many readers, make ownership, version, scope, known omissions, and a usable route to source material clear. This is the practical meaning of a **controlled document** here, not a claim that every AI summary has a formal regulatory status. Per-claim links can reduce the cost of checking; their presence alone does not guarantee it happens. Route interface details to `rtp-ai-ux-patterns`.

When independent judgment is needed, collect the person's assessment or evaluation criteria before exposing them to the AI's conclusion. In a group, independent collection can prevent the highest-status view from becoming everyone's starting point. Do not require the least experienced person to make an unsupported decision; an honest question or uncertainty may be the appropriate initial contribution.

## Choose the smallest checkpoint that addresses the mechanism

A checkpoint needs a purpose, suitable evidence, an owner, and a consequence for what it finds. For consequential human review, also ensure a capable reviewer can challenge the result, the challenge can change something, and a criterion or authorized decision-maker can bring the review to a conclusion. A separate person is useful when independence matters; not every low-stakes check needs a second reviewer.

An AI critic can generate useful and unexpected objections or check observable properties. It is not an independent stakeholder, a new empirical observation, or a substitute for an authorized accountable reviewer. Test any proposed judgment substitute against the skills needed to operate it. Do not assume that a reviewer must personally suffer a loss for their evidence to be valuable.

Avoid both endless dispute and forced premature closure. Name a reasonable deadline, decision rule, and escalation path. Reward supported correction and learning; do not make silence costly in a way that manufactures objections or punishes warranted uncertainty. A protected learning venue can reduce performance pressure where that is the mechanism.

Size review for **consequence, reviewer competence and commitment, workload predictability, and case familiarity**. If a consequential case exceeds the reviewer's ability or capacity, provide support, a different reviewer, or a narrower scope. A lighter confirmation click is not an adequate substitute merely because the reviewer is unfamiliar or overloaded. The consumer-advertising study behind the original sizing analogy does not validate that substitution for high-stakes oversight.

Fatigue, interruptions, workload, and monotonous monitoring can affect attention. Protect appropriate review time, vary or rotate monitoring work where useful, and test whether lightweight engagement aids help. The three-gear model is a practitioner metaphor; it does not guarantee rubber-stamping under pressure or establish that mechanical checks are immune to fatigue.

### Checkpoint 1 — Rotation and practice

Keep appropriate opportunities to work with and without the assistance where independent capability remains needed. Select the tasks and cadence deliberately, using simulations or protected exercises when live unassisted work would expose people to avoidable risk. Include useful peer review and debriefing.

The original 80% tool-use cap and four-week rotation are example schedules, not evidence-based universal limits. An inability to rotate may indicate capacity constraints, but does not prove complete dependency. Define the desired capability and measure whether the chosen practice preserves it.

### Checkpoint 2 — Calibration

Use suitable cases with independently established answers or qualified reference judgments. Where feasible, compare **human alone, AI alone, and the combined process** on comparable tasks. Collect an independent human view first when the purpose is to measure unassisted judgment. Include uncertainty and cases without one definitive answer when the work requires them.

For longitudinal assessment, keep conditions, task difficulty, and measures comparable enough to interpret change. Use a stable reference component plus new coverage where the work changes. Ten to twenty monthly cases may support a learning conversation but need not yield a precise performance estimate.

Seeded known-good and known-bad cases can help assess detection and unnecessary rejection. Use controlled, authorized evaluation conditions; do not let deliberately wrong test material drive real consequential actions. Other methods—expert audits, outcome-linked samples, or carefully designed comparisons—may also be valid. Seeded cases are not the only way to distinguish mechanisms, and they may be unrepresentative or recognizable.

### Checkpoint 3 — Independent view, criteria, and meaningful override

When anchoring or passive assent is the concern, capture a concise initial judgment, criteria, or uncertainty **before** the AI's recommendation. Then compare the result. A “why do you follow this recommendation?” response written afterward is a different intervention; it can assess justification but does not establish an independent prior view.

Run the **three-question comparison**:

1. What did the AI add that was missing?
2. What did it get wrong?
3. What looks plausible but rests on a wrong assumption, omitted constraint, or weak evidence?

Do not require a flaw where none is supported. Plausible errors deserve attention, but severity depends on consequence rather than appearance alone. Use the comparison to support a real option to accept, revise, reject, escalate, or abstain.

Choose checkpoint frequency according to the workflow. A batch review can reduce repetitive handbacks when coverage and timely intervention remain adequate. Per-case review may be necessary where exposure cannot safely accumulate. Test review depth, delay, coverage, and outcomes rather than assume fewer checks always improve them.

Track correct acceptance and error detection as well as unnecessary rejection. A low override rate—even below 1%—does not prove disengagement. A high rate does not prove sound judgment. Compare with the underlying error rate, task mix, and outcome evidence; route instrumentation to `rtp-production-observability` and `rtp-ai-product-metrics`.

### Checkpoint 4 — Repair after a miss

First contain active harm and meet any urgent reporting or recovery obligations. Then conduct a fair review of what happened, why it happened, and what people and systems could do differently.

Where relationships or ownership were damaged, make room for social repair alongside technical correction. A reasonable decision can have a bad outcome; a favorable outcome can also conceal a poor process. Do not force admissions, postpone urgent containment for reconciliation, or promise that one process change makes recurrence impossible.

Assign the follow-up and verify whether the repair addressed the mechanism. Use `rtp-trust-ladder` for warranted trust and recovery, and `rtp-stress-test` for operational failure evidence.

### Checkpoint 5 — Decision rationale and learning records

Capture a concise, decision-relevant account:

> I chose [action] because [evidence and criteria]. I set aside [alternative or signal] because [reason]. I would reconsider if [condition].

Use this for meaningful decisions rather than every trivial act. A recorded rationale can be incomplete or post-hoc; it is not direct access to someone's internal reasoning. Automatic capture still has review, storage, privacy, and maintenance costs. Avoid collecting sensitive information without a purpose.

Review records for recurring assumptions, missed constraints, and learning. Less text or simpler language does not establish lost expertise. Compare substance and task demands, not a “reasoning complexity” score alone. A monthly or quarterly review is an option to adapt to risk and volume.

## Case 2 — Design and test human–AI complementarity

Human–AI combinations can improve outcomes, but the benefit depends on the task and design. A systematic review found that combinations did not, on average, outperform the better of the human-only or AI-only alternatives; results varied by task. This makes a relevant baseline essential. See [Vaccaro, Almaatouq, and Malone](https://arxiv.org/abs/2405.06087).

Use four moves:

1. **Split work by demonstrated strengths and required authority.** List the sub-decisions and assign them based on evidence, capabilities, constraints, and responsibility. Precision, consistency, contextual understanding, and novelty handling are not guaranteed properties of all machines or all humans. The surgeon-and-robot illustration describes complementary roles, not a universal performance specification or a rule for every clinical system.
2. **Assess severe tails alongside ordinary outcomes.** Define plausible consequential errors, detection limits, and recovery. Average accuracy cannot settle a catastrophic-risk question, but the presence of a human is not proof that the tail is controlled. Test whether that person can detect and alter the relevant outcome in time. Include the consequences of intervention and delay.
3. **Define agreement and disagreement handling.** Agreement can support a decision when inputs and errors provide genuinely additional evidence. When disagreement matters to a safety or authority boundary, stop or escalate before the exposed action. Elsewhere, use a justified adjudication, routing, or aggregation method. Do not average away a material conflict, but do not forbid all aggregation of differing estimates or require an unsafe pause during time-critical work.
4. **Keep the needed capability active.** Give the human a meaningful task, information, authority, and feedback. That may involve production, probing exceptions, contextual judgment, or evaluated oversight. Apply Case 1's checks where retention or formation matters. Merely watching can be inadequate; watching does not inevitably cause atrophy on a fixed schedule.

Preserve verified human-oversight requirements and task-specific hard boundaries when efficiency recommendations conflict with them. Resolve the actual requirement and risk with `rtp-autonomy-spectrum`, `rtp-agent-risk`, and the responsible domain owner. Do not replace those assessments with an unqualified claim that a human must remain forever because the domain is regulated. Where full automation is justified, specify residual accountability, monitoring, and fallback needs.

## Check the design with seven questions

1. When was the last meaningful acceptance, correction, or override, and what does the underlying error rate imply about that frequency?
2. If assistance were unavailable, which tasks must people still perform, to what standard, and how was that capability assessed safely?
3. What recent case shows human contribution—or an unnecessary human intervention—and what can be learned from it?
4. Has relevant human ability changed under comparable conditions, separately from changes in AI quality?
5. Does disagreement receive the response required by its consequence, with an effective route to resolution?
6. Can someone report a mistaken override or a dismissed concern and receive a fair, useful response?
7. Can the people using a consequential summary inspect appropriate source evidence, limitations, and alternative interpretations before commitment?

## Output and handoffs

```markdown
## Judgment Design: [role, task, decision]

Purpose of human involvement: [capability, contribution, authority or requirement]
Scope and consequence: [users, exposure, reversibility, intervention deadline]
Case: [capability / complementarity / mixed / deliberate automation]
Evidence: [baselines, observed gaps, hypotheses, limits]

Capability design:
- Mechanism(s): [drain IDs and/or misapplication, with evidence]
- Population: [newcomers / established experts / reviewers / other roles]
- Capability needed: [formation, retention, transfer or fallback]
- Checkpoints: [selected IDs; purpose, owner, capacity, cadence, action trigger]
- Disclosure and challenge route: [Checkpoint 6, response and escalation]

Complementarity design:
- Work and authority split: [sub-decisions and reasons]
- Tail constraints: [failure, detection, intervention and recovery]
- Agreement/disagreement handling: [decision rule and exceptions]
- Capability maintenance: [practice, feedback and evaluation]

| Measure | Baseline and scope | Review trigger | Frequency | Owner/action |
|---|---|---|---|---|
| Error detection and correct acceptance | | | | |
| Unnecessary rejection or harmful intervention | | | | |
| Relevant capability over time | | | | |
| Review time, workload and unresolved cases | | | | |
| Concern reporting and disposition | | | | |

Recommendation: [design to adopt or test, explicit limits]
Trade-off: [quality, capability, time, cost and intervention risk]
Next step: [owner, date, evaluation and condition for changing the design]
```

This skill has no formal imports; the companions below are targeted handoffs:

- `rtp-determinism-compass`: required rules, repeatability, and acceptable variation.
- `rtp-autonomy-spectrum`: decision rights at each step.
- `rtp-trust-ladder`: calibrated reliance and recovery after a miss.
- `rtp-agent-risk` and `rtp-safety-by-design`: consequential boundaries and enforceable controls.
- `rtp-stress-test`: readiness evidence and the practical ability to report a no-go.
- `rtp-agent-spec`: translate the design into workflow, permissions, tested gates, and escalation; use confidence thresholds only when calibrated for the task.
- `rtp-stakeholder-communications`: explain the evidence and trade-off behind the human role.
- `rtp-production-observability` and `rtp-ai-product-metrics`: measure review and outcome quality over time.
- `rtp-capability-tracking`: learning pathways, role changes, and oversight capacity.
- `rtp-needs-guard` and `rtp-ai-ux-patterns`: agency, relationships, resistance, and usable access to evidence.

## Final checks and limits

Before handing off, verify that the human role has a purpose; the diagnosis distinguishes capability, behavior, and authority; each selected checkpoint addresses a mechanism with an owner and capacity; metrics assess both helpful and harmful intervention; and hard constraints are reflected in the actual workflow.

Do not install heavy review in low-consequence work merely to preserve a feeling of control. Do not abandon a needed capability because it is already weak; restrict exposed work and plan supervised rebuilding where appropriate. A short project may not need long-term retention monitoring but can still have immediate anchoring, avoidance, or suppression risks.

Separate customer friction from reviewer friction, then assess each by its function. Some customer effort supports consent or accurate input; some reviewer effort adds no useful protection. “Remove friction” is not a sufficient reason either to delete a safeguard or retain a redundant one.

Evidence differs across mechanisms, roles, and timescales. A single-session study cannot establish years of atrophy. Findings on established experts do not automatically predict how newcomers learn, though research on learning with AI does exist. The live challenges and numerical examples are retained in [calibration and evidence notes](references/calibration-and-evidence.md), with the longer diagnosis and practitioner cases in [mechanisms and design notes](references/mechanisms-and-design.md).

End with the recommended design, its strongest evidence, the capability or risk it protects, the cost it introduces, and the next evaluation. A visual may compare the two cases and the chosen checkpoints; avoid drawing an unsupported universal decay timeline.
