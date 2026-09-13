---
name: rtp-trust-ladder
description: 'Design appropriate reliance on AI so users understand its limits, accept useful help, and catch consequential errors. Use for permissions, progressive autonomy, over-reliance, avoidable distrust, and recovery after failure. Match authority to the task, stakes, evidence, user needs, and real recovery options. Assess trust separately from the ability to challenge an outcome. Measure correct acceptance and error detection without targeting a fixed rejection rate. Produce a permission and visibility plan, calibration measures, failure examples, and a recovery path. Pairs with autonomy-spectrum for capability labels, confidence-tuner for uncertainty signals, judgment-guard for effective review, and trust-under-fog for disclosure. Triggers: calibrated trust, over-reliance, trust repair, progressive autonomy. Trust scores or acceptance rates alone do not authorize consequential action.'
imports: ["determinism-compass"]
version: v1.4.1_latest
---

# Trust Ladder

Help people rely on AI appropriately for the task. **The goal is neither maximum acceptance nor a quota of rejections.** A user can reasonably accept nearly every suggestion from a reliable system in a narrow task. A user can also reject many suggestions without noticing the errors that matter.

Assess three things separately: what the system can reliably do, what the user believes it can do, and what authority the system actually holds. Trust is relevant to design; it does not grant permission or establish safety.

## Start with the task and the decision

Use this skill for a new permission model, a change in autonomy, a production reliance problem, or recovery after a visible failure. Established trust is still worth checking after a material change. For a quick audit, use the diagnostic questions near the end; use the full process when designing progression.

Identify the user and affected people, task, available evidence, action boundaries, and decision to make. Reuse known context and clarify only material gaps. Follow the shared Universal Skill Protocol at the appropriate depth. Use `determinism-compass` for invariants and `autonomy-spectrum` for the library’s shared capability labels.

This skill’s five **trust states** describe a relationship in a particular task. They are not autonomy levels, personality diagnoses, or a validated maturity scale. Do not translate tenure, confidence, or a high acceptance rate directly into permission.

## Terms that guide the assessment

- **Calibrated trust:** confidence in the system that matches evidence about its reliability and limits in the relevant setting.
- **Appropriate reliance:** using, checking, correcting, or declining the system in a way that improves the decision, given its consequences and alternatives.
- **Automation complacency or over-reliance:** insufficient scrutiny where scrutiny is needed, allowing material errors to pass.
- **Under-reliance:** avoiding useful assistance without sufficient reason. Nonuse can also be rational because of poor fit, privacy, effort, or preferences.
- **Calibrated suspicion:** treating an uncertain adverse signal as a reason for proportionate investigation, not as proof against a person.
- **Trust repair:** acknowledging a failure, addressing harm, restoring usable control, and demonstrating relevant improvement.
- **Independent detection competence:** the ability to assess an output using relevant knowledge, evidence, tools, or other checks beyond simply accepting the AI’s explanation.
- **Influence:** the practical ability to contest, correct, restrict, or change an outcome. A person can be trusted and still lack this authority.
- **Visibility tax:** the perceived reputational, workload, or job-security cost of revealing useful AI methods at work. Treat it as a design lens, not a diagnosed motive.

## Step 1 — Establish severity, reversibility, and authorization

Describe what can go wrong, who is affected, and when intervention remains possible. Separate the severity of harm from the ease of correction.

| Situation | Design implication |
|---|---|
| Low consequence, easily corrected | Reduce unnecessary interruption within the user’s authorization; provide useful visibility and correction. |
| Recoverable with cost, delay, or cooperation | Verify the actual recovery path, its limits, and who bears the cost. Consider bounded delegation and targeted review. |
| Irreversible or difficult to remedy | Prioritize prevention and appropriate authorization before the effect; restrict scope where assurance is inadequate. |

A transfer, deletion, calendar cancellation, or sent message is not inherently reversible. An apology or a compensating transaction does not erase the original effect. “Undo for 24 hours” is valid only if the system really provides it—for example, by delaying execution or retaining a recoverable version—and its limits are clear.

Record current authority: actor, action, resource, scope, limits, duration, and applicable policy. A narrow, already authorized workflow need not ask again at every routine step. A friendly interface or a high confidence score cannot expand that authority. Apply relevant legal and organizational requirements to the specific activity; HIPAA does not impose blanket approval for every medical decision.

## Step 2 — Test the user’s mental model

Ask the user to explain what will happen before a consequential interaction: what the system will access, decide, change, and ask them to review. Compare that explanation with actual behavior. Include failure and recovery, not just the happy path.

Correct material misunderstandings before exposing the user to the misunderstood action. Use concrete previews, evidence, limitations, and examples. Explain whether a result is a recommendation, a queued action, or a completed action. System-level deterministic checks can coexist with a probabilistic model; avoid suggesting that every part of an AI product must vary.

Use explanations that help the person assess the result. A generated account is not a faithful trace of all internal reasoning. Showing evidence, source quality, assumptions, or verified action receipts can be more useful than a long rationale. Evaluate comprehension; do not equate opening an explanation with reading or understanding it.

## Step 3 — Assess trust and influence separately

Use these five states as prompts for inquiry:

| Trust state | What to investigate | Useful response |
|---|---|---|
| Distrustful | Prior failure, poor fit, or a reasonable unmet requirement. | Show task-relevant evidence and a usable alternative; do not pressure adoption. |
| Skeptical | Uncertainty about capability, data use, or consequences. | Demonstrate the bounded task and its controls. |
| Conditional | Trust varies by action, domain, or circumstance. | Preserve separate permissions and evidence by task. |
| Confident | Experience supports delegation in a defined scope. | Verify that reliability and permissions still match the scope. |
| Potentially over-reliant | Evidence suggests material errors are being accepted or necessary review is ineffective. | Investigate the failure, reduce relevant exposure if needed, and repair the review design. |

Ask about trust directly and compare responses with task performance. Do not assign a state solely from click speed, tenure, low rejection, or lack of reported errors. These signals have multiple explanations.

For reviewers, ask two distinct questions: “How much do you trust the recommendation in this task?” and “Can you challenge or change what happens when it is wrong?” Investigate the reasons and actual decision rights. High trust with low influence can expose an authority gap; it is not a validated detector of fabricated justification. A score difference needs a defined instrument and comparable meanings before interpretation. Use `judgment-guard` for review competence and `responsible-ai-program` for authority and escalation.

## Step 4 — Assign a permission mode for each action

Choose from explicit modes such as **suggest**, **prepare for approval**, **execute within delegated bounds**, or **pause and refer**. Use the shared autonomy labels only as a separate description of the system. These modes replace the earlier conflicting Level 0–4 numbering.

Decide from stakes, actual permissions, tested performance, available controls, user preferences, and recovery. Trust alone is insufficient. More autonomy is not the required endpoint of every ladder.

- For a new or uncertain workflow, previews and approval can establish a shared understanding without asking about every trivial substep.
- For a validated, bounded workflow, execution may be delegated with visible scope, limits, and effective intervention or recovery.
- For significant unresolved risk, narrow the scope, require qualified review where useful, or pause the action. Adding a confirmation modal is inadequate if nobody can assess or stop the outcome.
- When evidence shows harmful reliance, target the affected action and failure path. Do not withdraw all autonomy merely to raise a rejection metric.

Make permission changes specific and reviewable. A “trust this type” control should name the action class, data, recipients, limits, and duration; it is not an open-ended waiver. Allow people to change a preference or revoke delegation through a usable route. Recheck policy and resource authorization at execution.

See the [calibration design tables](references/calibration-design-tables.md) for the eleven relationship scenarios and domain-specific considerations retained from the original framework.

## Step 5 — Present uncertainty and explanations that support judgment

Use `confidence-tuner` to determine whether a confidence signal is valid and understandable. Show what the person needs for this decision, not a number on every recommendation by default.

| Pattern | When useful | Limit |
|---|---|---|
| Clear recommendation | The action and decision rule are understandable without a probability. | “Hold for review” is a recommendation, not a claim of certainty. |
| Graded confidence | Validated bands communicate meaningful differences. | Define what high, medium, and low refer to. |
| Numeric estimate | A calibrated probability for a named event helps the decision. | Avoid invented precision and explain applicability or uncertainty. |
| Evidence and explanation | Sources, assumptions, alternatives, or checks help the recipient evaluate. | Source counts and polished language do not establish correctness. |

Offer progressive detail according to task and user needs. Expertise alone does not dictate a format. Novices can benefit from well-explained probabilities; experts can prefer a concise recommendation. Do not convert an 82% fraud probability into an “18% false-positive rate.” The complement concerns this predicted event; false-positive rate is measured across cases that are actually negative.

A confidence estimate of 85% is calibrated when the named event occurs about 85% of the time across comparable predictions. It does **not** mean users should accept 85% of those recommendations. Stakes, action costs, alternatives, and personal preferences affect the decision.

Explanation can improve understanding, error detection, or uptake; it can also increase unwarranted reliance. Measure the effects separately. A reviewer may develop competence through useful explanations and feedback, so pre-existing independent skill is not the only path. Do not treat explanation as inherently protective or inherently harmful. The sepsis and other research examples are qualified in the [evidence notes](references/trust-evidence.md).

### Five techniques to test

1. **State specific limitations.** Match them to the task and current configuration. Verify provider features before claiming every product supplies only generic disclaimers.
2. **Demonstrate competence.** Be clear, respectful, and willing to disagree. Competence and warmth can coexist; avoid hostility and sycophancy.
3. **Connect recommendations to stated goals.** Show the actual connection without inventing intentions or pretending to understand emotions. The cited acceptance effect was conditional on long-term or virtue-oriented choices, not a universal task gain.
4. **Describe actual authority honestly.** “Assists” is misleading if the system independently decides or executes consequential actions. Fix the permissions or the description rather than concealing power to reduce concern.
5. **Preserve effective control.** Show where people can approve, edit, pause, stop, appeal, or recover. Select the scope from the task; “moderate autonomy” is not a universal optimum.

These interventions need evaluation in the intended use. Reported adoption figures do not establish that distrust is the sole cause of limited autonomous deployment. Successful bounded assistance can be valuable without becoming fully autonomous.

## Step 6 — Measure appropriate reliance

Pair behavior with independent evaluation of the relevant outcomes. Use representative, consented or otherwise appropriate samples and safely isolated known-error exercises when useful. Never insert dangerous live errors or fabricated “45% confidence” messages every tenth turn to provoke rejection.

| Measure | Definition or question |
|---|---|
| Correct acceptance | How often are sound, applicable recommendations used when use is appropriate? |
| Harmful acceptance | How often are materially wrong or unsafe recommendations accepted or acted on? |
| Error detection and correction | Of the relevant errors present, which were caught and corrected before harm? |
| Erroneous override | When does a user change a sound recommendation into a worse result? |
| Review burden | What time and effort does the review consume, and what does it detect? |
| System outcome | Does the combination of user and AI improve the actual task relative to a suitable alternative? |

For each rate, state numerator, denominator, labels, exclusions, sample, time window, and severity. Rejection, editing, regeneration, ignoring, and undo are useful diagnostic events; none inherently indicates error, vigilance, or distrust. A correct output may be edited for style. Silence may mean abandonment, delayed review, or successful background operation.

The old 15–30% rejection target, <5% over-reliance trigger, fixed industry ranges, two-second reading rule, and <5% undo target are not validated universal benchmarks. Do not optimize toward them. A low harmful-error rate and effective controls may justify high acceptance; a high rejection rate can hide serious misses.

Use privacy-conscious event capture with output or action IDs, configuration and policy version, the confidence measure if valid, available user action, and actual execution state. Distinguish multiple events on one item from final outcomes. Select an observation window and alert threshold suited to volume and risk; seven-day averages, thirty-day cohorts, and a five-percentage-point alert are optional starting choices, not fixed rules. Inspect severity and actual cases before drawing conclusions.

### Teach limitations with representative failure cards

Use a small, relevant set of safely presented failures to support learning. Five cards can cover: a common failure, a consequential failure, a subtle failure, an obvious failure, and a user-specific case. Categories may overlap; do not pad the set to reach a count. Include successes and boundaries so examples do not falsely imply pervasive failure.

For each card show the scenario, what the system did, the specific error, how to detect it, and what to do. Test whether the user can explain the relevant limitation and recovery action. The previous “three of five identified” and “four of five recoveries” were exercise scores, not validated authorization gates. Tailor competence checks to the actual responsibility and stakes; do not make users bear a risk the product could prevent.

## Step 7 — Support enterprise trust and review rights

Use the original enterprise trust equation as a discussion aid: reliability, transparency, and compliance can support trust, while exposure to blame or reputational harm can discourage delegation. It is **not** a calculable equation with validated weights, and embarrassment is not always the dominant factor. Include the customer’s mission, economics, rights, and operational consequences.

Preserve appropriate evidence of consequential actions: actor, authority, action and resource, time, configuration, source or rationale where available, approval if required, actual result, and recovery limits. An audit trail cannot reproduce unknowable internal reasoning or reverse every effect. Define scope and retention from the use and obligations; enterprise status alone does not require every raw interaction to be recorded.

Treat knowledge hiding as a separate organizational question. The 604-person survey links trust, psychological safety, and disclosure, with sanctioned tooling moderating the association. It does not prove that installing approved tools causes concealment. Clarify what is logged and why, credit contributions, limit the burden of sharing, and make fair use of efficiency gains credible. Address actual security issues without treating all private experimentation as misconduct. The identified source and limits are in the evidence notes.

## When an interaction is mandatory

A review, consent step, or interruption can sometimes offer useful choice over timing or content. Ensure the choice is real and compatible with the obligation. Do not offer “later” when authorization is needed before acting, or imply optional consent where no meaningful choice exists.

Consider three factors: commitment to complete, available and predictable attention, and familiarity with the options. The advertising research suggests timing choice can work when people are committed and can anticipate their session; low commitment increases the risk of deferral and abandonment. Content choice requires meaningful options and enough attention. Unfamiliar options or limited inventory can favor a timing choice when deferral is feasible.

This is a hypothesis for AI workflows, not a proven transfer from ads to approvals. Similar average effects in separate studies do not establish universal equivalence. A standard choice can be appropriate when needs are shared; personalization is not mandatory. Track whether deferred obligations are completed, and evaluate comprehension and outcomes alongside attention and annoyance.

## Repair trust after a failure

Use five phases, scaled to the consequence:

1. **Acknowledge promptly.** State what is known to have failed and who or what is affected. Do not invent a diagnosis or accept unsupported blame merely to sound accountable.
2. **Explain accurately.** Separate observed facts, likely causes, and unresolved questions. Include relevant external dependencies without using them to evade responsibility. Never fabricate a past confidence score or internal rationale.
3. **Restore usable control.** Contain exposure and offer a genuine manual, assisted, or safe fallback path. Report whether the action occurred, remains queued, or is still uncertain.
4. **Provide remedy or support.** Correct or compensate where feasible and authorized. Additional review can be temporary protection; it is not automatically compensation. Support teams can be part of effective recovery.
5. **Demonstrate relevant improvement.** Name the change, owner, evidence, and remaining limits. Claim a “94% catch rate” only with a defined supporting evaluation. Show when the fix takes effect and how it will be checked.

There is no established rule that trust falls two to three times faster than it grows, every user must drop two stages, or recovery must reach full autonomy. Restrict the affected scope according to the incident, then reassess with evidence and user preferences. Repeat approval requests without correcting the failure can worsen the experience.

## Deliver a trust and permission plan

```markdown
## Trust-Ladder Review: [task and user group]
Decision and evidence:
Actual permissions and recovery limits:
User mental model and material gaps:
Trust assessment and separate influence/recourse assessment:

| Action | Consequence | Permission mode | User visibility | Check or recovery | Owner |
|---|---|---|---|---|---|

Calibration measures: [correct/harmful acceptance, detection, overrides,
                      review burden, denominators, outcome comparison]
Learning and failure examples:
Change, escalation, and trust-repair path:
Next action: [owner, test, date, evidence that changes the decision]
Main trade-off and residual risk:
```

Use the shared conclusion and trade-off guidance without duplicating content. Add a visual map through the available drawing skill if it makes the permissions clearer.

## Seven checks and practical questions

Check credible severity mapping; tested mental models; useful and valid uncertainty information; effective permission and recovery paths; outcome-based reliance measures; an honest repair process; and appropriate action evidence. “All failures identified” or “every recommendation has a confidence number” is not a realistic completion standard.

Ask: Are material errors reaching action? Do users understand the boundary and have the means to intervene? Does review improve outcomes at an acceptable cost? Are product and marketing claims accurate? What happens after a visible failure? Can the organization explain who authorized a consequential action and what actually happened?

Reassess when stakes, permissions, users, or system behavior change. Ask about trust rather than guessing it. Preserve separate plans by domain. Increasing trust is useful only when it makes reliance more appropriate; lowering warranted trust is not a safety achievement. See [CONCEPT.md](CONCEPT.md) for worked examples.
