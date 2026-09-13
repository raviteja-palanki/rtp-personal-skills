---
name: rtp-trust-under-fog
version: v1.2.1_latest
description: 'Communicate clearly when outcomes remain uncertain. Use for AI capability claims, stakeholder expectations, planning ranges, disclosure decisions, and recovery after over-promising. Separate observed results, forecasts, enforceable commitments, and unknowns. Explain the evidence, conditions, consequences, and response plan at the depth the audience needs. Decide what to disclose using materiality, obligations, actionability, and timing; account for the costs of silence as well as disclosure. Produce a claim-and-evidence map, audience-specific wording, monitoring and reset conditions, and a recovery plan where needed. Pairs with determinism-compass for system boundaries, dual-lens for technical and stakeholder perspectives, trust-ladder for appropriate reliance, and confidence-tuner for calibrated estimates. Do not invent probabilities, stakeholder tolerance percentages, or guarantees merely to sound confident.'
imports: [determinism-compass, dual-lens]
---

# Trust Under Fog

Help stakeholders make a sound decision with the uncertainty that actually exists. **Say what is known, what is expected, what is uncertain, and what you will do next.** Confidence should come from a credible plan and evidence, not from disguising a forecast as a guarantee.

## Start with the decision and the audience

Identify the stakeholder, decision, consequence of being wrong, relevant evidence, and commitments already made. Use `dual-lens` to connect technical uncertainty to the stakeholder’s practical concern. Reuse known context and ask only for information that changes the claim or decision.

- **Full review:** capability claims to customers, boards, or regulators; a consequential forecast; disclosure policy; or recovery from over-promising.
- **Focused review:** audit a sentence, proposal, update, or presentation for unsupported certainty and missing conditions.
- **Simple communication:** if the relevant facts are established and uncertainty is immaterial, state them directly. A deterministic implementation can still have uncertain inputs, operational reliability, adoption, or business effects.

Use the shared Universal Skill Protocol at a proportionate depth. Choose a document, presentation, or inline response to fit the request. Sophisticated stakeholders may need more precise ranges and assumptions, not fewer.

## The trap: a useful claim becomes a stronger claim

Pressure to win budget or close a deal can strip away a qualification: “95% correct on this test” becomes “95% accurate,” or “we will test whether this workflow can be automated” becomes “the workflow will be automated.” Repetition can turn the stronger claim into an internal target before anyone checks it.

The remedy is not adding vague caveats to everything. Preserve the conditions that would change a reasonable person’s decision. Do not replace an unsupported guarantee with an equally unsupported range such as “70–80% automation.”

Wells Fargo’s sales-practices case illustrates how incentives, leadership, oversight, and the treatment of contrary evidence can interact. It does not prove that a different growth forecast alone would have prevented misconduct or that trust takes exactly five years to recover. Use the qualified [case and evidence notes](references/communication-evidence.md).

## 1. Audit certainty claim by claim

Ask: **What exactly are we claiming, and what supports that claim?**

| Claim type | What to state |
|---|---|
| Enforced behavior or commitment | Scope, conditions, owner, enforcement or delivery mechanism, and what happens if it fails. |
| Observed result | Metric, denominator, population, configuration, period, and uncertainty or limitations. |
| Forecast | Expected outcome, horizon, assumptions, method, and what could invalidate it. |
| Target | Desired outcome and the plan to pursue it; distinguish it from a forecast. |
| Unknown | What is unresolved, why it matters, and a feasible way to reduce or manage it. |

A service commitment can be meaningful even when delivery is not physically certain. Explain the agreed obligation and remedy; do not imply that a contract makes failures impossible. Verify authority before promising staffing, compensation, timing, or policy changes.

### Example: support-ticket triage

The following is a structure for an assessment, not a set of measured probabilities:

| Component | What can be established | What remains uncertain | Evidence or next step |
|---|---|---|---|
| Output uses ten permitted categories | Schema validation can reject invalid labels. | Whether the chosen category is correct. | Test validation and classification separately. |
| Classification of familiar tickets | Performance on a specified test population. | Transfer to current traffic and uncommon cases. | Compare live samples and evaluate relevant segments. |
| New or unsupported categories | Whether an unknown-category route exists. | Recognition of unseen cases and routing quality. | Test abstention and escalation, not forced guesses alone. |
| Usefulness to the support team | User feedback and task observations. | Fit, adoption, review burden, and sustained use. | Evaluate the workflow with representative users. |
| Faster service or lower cost | A baseline and a proposed improvement. | Causal contribution, staffing, demand, overhead, and quality effects. | Define the comparison and full cost horizon. |

Ten thousand successful examples do not create a universal guarantee. Do not assign “20%, 60%, 40%, or 30% confidence” unless a defined method supports those estimates. Carry important unknowns into the recommendation rather than filling blank cells with plausible numbers.

## 2. Locate the uncertainty in the system

Use `determinism-compass` to separate rule enforcement, probabilistic inference, and the surrounding workflow.

- **Repeatability:** under identical relevant inputs and configuration, does the system produce the same result?
- **Correctness:** is that result right for the task and current circumstances?
- **Operational delivery:** do dependencies, permissions, and execution work as intended?
- **Human and business effects:** does the result lead to adoption, better decisions, or economic value?

A keyword router can be perfectly repeatable while consistently routing ambiguous tickets incorrectly. A model can return a repeatable answer without that answer being reliable. A deterministic component can fail because of bad input or unavailable infrastructure. There is no 99% repeatability boundary that classifies an outcome as probabilistic.

State where uncertainty enters, what it affects, and which controls reduce it. Do not let confidence in one component silently stand in for confidence in the entire outcome.

## 3. Choose one or combine three communication styles

Select by the decision and information need rather than job title. Use ordinary words unless a technical distinction matters.

### Confident uncertainty

**Pattern:** “Here is the evidence we have, the limit that matters, and the action we take when that limit is reached.”

Example: “In the reviewed pilot, the system correctly routed 850 of 1,000 eligible tickets. We have not yet validated the new complaint category. Those tickets will remain in manual review while we test it.”

The numbers are illustrative. They describe observed performance, not a confidence score for each future ticket. If uncertainty estimates guide routing, verify their calibration and the escalation path. The “other 15%” is not necessarily identifiable in advance, and low-confidence routing does not catch every error.

### Bounded promises

**Pattern:** “We commit to this controllable deliverable or service level under these stated conditions. We forecast this additional outcome, and we will review it if these assumptions change.”

Example: “We will complete the defined pilot review by Friday and report results, gaps, and a rollout recommendation. We forecast lower support cost if ticket mix and review effort stay within the tested range; we will revise that forecast if either changes materially.”

Name who owns the commitment and whether it is feasible. A forecast reset does not erase an earlier miss or unilaterally change a contract. Document how a formal commitment can be changed through the applicable agreement.

### Transparent ranges

**Pattern:** “We estimate a range of outcomes over this period, based on these assumptions. Here is how we will plan for the downside and learn more.”

Example: “Our planning scenarios assume 60–85% of eligible tickets can be handled automatically while meeting the quality standard. That leaves 15–40% for manual handling, before adding review, escalation, and rework. We will check those assumptions after two weeks and report whether the evidence is sufficient.”

State whether a range is an empirical interval, a forecast interval, or a set of scenarios. A scenario range is not a confidence interval or a guaranteed bound. In this example, **60% automation leaves the larger manual workload: 40%**. The earlier version reversed best and worst cases. A result of 50% is below the stated 60–85% range, not inside it.

## 4. Define the stakeholder’s uncertainty budget

Use “uncertainty budget” to mean the practical amount and type of variation the decision can absorb. Establish it from the decision, capacity, consequences, and requirements—not a percentage assigned to a stakeholder category.

| Stakeholder | What to clarify |
|---|---|
| Board or investor | Planning horizon, downside exposure, liquidity or capacity needs, and what evidence changes funding or scope. |
| Customer | Which outcomes matter, acceptable failure and recovery, service commitments, and meaningful choices. |
| Frontline team | Workload, exception volume, review capability, training, and whether the fallback is usable. |
| Regulator or assurance function | Applicable standard, required evidence, permitted operation, and material uncertainties. Do not invent an acceptable error budget. |

The former 10–20%, 30–40%, 50%+, and 5–10% tolerances were unsupported. The same person may accept wide uncertainty in an experiment and very little in a consequential service.

For an insurance workflow, distinguish forecast processing speed and cost, the fraction eligible for automation, the evidence of correct decisions, and audit coverage. A 98% aggregate accuracy threshold or ninety days of review is not a universal authorization standard. A claim to audit 100% of decisions must identify the actual review, staffing, detection capability, and timing; it does not imply every error will be caught.

### Decide what to disclose using materiality, actionability, and timing

Start with required disclosures and information material to rights, safety, consent, contractual expectations, or a reasonable decision. Do not withhold such information because it might reduce trust or because the recipient cannot reverse the event.

For other details, ask:

1. What decision or expectation could this information change?
2. Can the recipient act, prepare, seek help, or choose an alternative?
3. Will the information arrive while those options remain useful?
4. What context, uncertainty, or response plan prevents a misleading impression?

Porsche’s “Track Your Dream” case contrasts reassuring progress information with distressing delivery news. It suggests that the *kind* of information matters as well as its volume. It does not establish that a customer whose car was lost at sea has zero recourse: they may need to replan, ask about replacement, or exercise contractual options. A truthful production photograph can reassure, but no fact has the same emotional effect on every recipient.

Where the customer cannot influence the event, explain its implications, what the organization is doing, what options remain, and when the next update will arrive. Do not recast your own action as customer control when it is not.

### Account for silence as well as disclosure

The Novel Insights CBA/Porsche comparison proposes an important measurement risk: disclosure’s immediate costs may be more visible than delayed benefits such as better fit, fewer surprises, or more informed decisions. A team could then reduce disclosure because its measurement captures only one side.

Treat that as a hypothesis to investigate. An incomplete feedback loop is not literally a controlled experiment, and under-disclosure is not inevitable. Compare disclosure and silence on relevant outcomes over an appropriate horizon. Use ethical experiments where suitable, interviews, comprehension checks, complaint patterns, and retention or decision outcomes. Do not experiment by withholding required or material information.

The CBA podcast withholds the focal experiment’s outcome; it does not prove that disclosing drawbacks increased sales. A team that measures modest commercial benefits may still have a duty to disclose. Better measurement supports judgment but does not replace obligations or affected people’s interests.

## 5. Define signals and a response before making the claim

For each consequential forecast or commitment, specify the signal, metric and denominator, observation window, threshold or condition, response, owner, and update time. Include data freshness and measurement quality so a broken dashboard is not mistaken for good performance.

| Signal type | Example question | Response to design |
|---|---|---|
| Leading | Are error severity, exception volume, review effort, or dependency failures diverging from assumptions? | Investigate, narrow scope, add effective protection, or pause exposed actions. |
| Lagging | Are cost, adoption, service quality, or business outcomes meeting the forecast? | Reassess causes, economics, product fit, and the forecast; do not assume the model is the only cause. |
| Evidence gap | Is the sample sufficient and representative to judge the claim? | State what remains unknown, preserve appropriate limits, and set the next evidence plan. |

The former 95% accuracy, five-percent satisfaction drop, ten-percent cost gain at three months, and sixty-percent adoption at six months were example triggers. They are not default gates. Distinguish relative change from percentage points and routine variance from a material shift. A single credible severe event can warrant action before a rate crosses a threshold.

Commit to feasible updates and actions, not certainty that an investigation will finish in one week. Some warning signals emerge too late or not at all. Use preventive constraints, downside reserves, or narrower scope where monitoring cannot protect against the harm.

## Six diagnostic questions

1. **How could this claim be wrong?** Cover material failure paths; being unable to invent five does not itself prove overconfidence.
2. **What is the worst credible consequence?** Include severe possibilities supported by a causal path; “catastrophic” and “realistic” are not opposites.
3. **What outcome does the stakeholder need?** Accuracy may matter directly or through workflow performance. Clarify rather than dismissing their metric.
4. **What do they understand about the range and downside?** Use a brief teach-back or scenario discussion where useful.
5. **What evidence would make us change course?** Name the signal and response, including how uncertainty will be reported.
6. **Can the claim withstand scrutiny?** Check evidence and wording. Feeling nervous is not proof that a claim is false or overstated.

## Recover from an over-promise

Use four phases at a pace matched to the harm. The old week-one, week-two, and months-two-to-six schedule was illustrative; do not delay a necessary correction to fit it.

1. **Admit and contain.** Identify the original claim, the current evidence, who is affected, and any immediate protective action. Separate known causes from unresolved questions.
2. **Reset expectations.** State a supported estimate or unknown, explain the gap, and offer feasible choices such as continuing within a narrower scope, pausing, or exiting. Respect existing commitments and rights.
3. **Deliver and report.** Make realistic commitments and show actual results against them. Do not deliberately understate a forecast to manufacture “over-delivery.” If a range is repeatedly exceeded, improve the estimate rather than treating poor calibration as a win.
4. **Rebuild through evidence.** Demonstrate relevant changes, keep update commitments, and invite review of outcomes. Trust may recover at different rates or remain limited; full restoration is not guaranteed.

Any of the three communication styles can be appropriate during repair if it is accurate. A support conversation, a product change, and a leadership update may all be needed. Record what was learned and what will change in future claims.

## Support understanding without manufacturing anxiety

The Storoni interview offers a practitioner explanation of arousal and learning. It does not establish an ideal emotional state for every stakeholder or show that calm people cannot learn.

Use three possible states as observation prompts, not diagnoses:

| Possible state | What to check | Helpful response |
|---|---|---|
| Quiet or apparently disengaged | Are people clear, reflecting, reluctant to speak, or uninterested? | Ask for understanding and offer ways to respond privately or later. |
| Engaged with manageable concern | Can people reason, ask questions, and act on what matters? | State genuine uncertainty, clarify boundaries, and give a useful next step. |
| Overwhelmed | Are cognitive load, stakes, or lack of control obstructing understanding? | Slow down, prioritize essential information, offer support, and avoid unnecessary pressure. |

Three useful moves remain: state the uncertainty and real commitments; give people a meaningful action or question; and check understanding when the room is quiet as well as distressed. Reassurance can be truthful and helpful. Do not infer chemical states from behavior, provoke discomfort as a learning technique, or promise employment stability unless authorized and able to support that commitment.

## Produce a communication the stakeholder can use

Lead with the decision or update, then the necessary evidence and limits. A complete working record can use this structure:

```markdown
## Communication Under Uncertainty: [decision and audience]
Main message:
What is observed, forecast, targeted, committed, and unknown:
Evidence and scope: [metric, denominator, population, configuration, period]
Range or scenarios and planning consequence:
Important conditions, downside, and available choices:
Required/material disclosures and timing:
Monitoring or learning plan: [signal, owner, action, next update]
What changed from any earlier claim:
Main trade-off and next decision:
```

For a short request, deliver the revised wording and the few assumptions needed to use it. For a broader decision, retain the claim map and evidence. Create a handoff only when another workflow needs it. Add a visual with the available drawing skill if the map, scenarios, or response path are easier to understand that way; do not draw invented stakeholder tolerance percentages.

## Final review and decision

Check seven things: claim types distinguished; uncertainty located; communication style fitted to the decision; actual tolerance and obligations understood; meaningful signals defined; a feasible reset or recovery path; and wording tested through an appropriate skeptical review or comprehension check.

Use 3E as a decision aid: **Explore** unsupported assumptions with a bounded test; **Exploit** evidence and capabilities that support a useful commitment; **Exit** an infeasible claim, scope, or proposal when a sound alternative cannot be found. Exit does not require abandoning the stakeholder, and an unmet guarantee request can sometimes be solved through narrower scope, a service commitment, or a reliable non-AI component.

State the recommendation, key trade-off, residual risk, and next action. Honesty need not reduce enthusiasm or slow every deal, and a stakeholder who declines may be making a reasonable decision. Do not guarantee a commercial reward for transparency. The practical standard is a claim people can understand and a plan the team can stand behind.
