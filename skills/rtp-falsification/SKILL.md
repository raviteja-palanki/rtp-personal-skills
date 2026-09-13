---
name: falsification
version: v1.1.1_latest
description: 'Turn a product recommendation into a claim that evidence could challenge, with a clear test and an agreed response to failure. Use before a significant investment, launch, strategy commitment, or continued rollout when success is being asserted without a credible stopping rule. Specify the population, measures, timeframe, counter-evidence, and decision owner; distinguish success criteria from pause, pivot, and stop conditions. Use a lightweight learning check for cheap, reversible experiments. Pairs with bias-spotter, problem-type, stress-test, eval-driven-development, and ship-decision.'
imports: []
---

# Make the claim testable before committing

State what you believe will happen, what evidence would challenge it, and what decision follows if the evidence is unfavorable. Agree on those terms before launch momentum makes them harder to use. The result should help the team act with a clearer basis for continuing, changing direction, pausing, or stopping.

**Keep three things distinct:** the success you are aiming for, the evidence that would undermine the claim, and the condition that requires a particular action. Missing an ambitious target does not always justify stopping; crossing a serious harm threshold may require action before the full value experiment ends.

Use a full brief for a consequential investment or launch. For a small, readily reversible experiment, a claim, learning question, and review point may be enough. Use existing context and the requested format. Ask only for missing information that changes the test or decision. Do not prolong analysis once the available evidence supports the next bounded action.

## The method

1. **Write the hypothesis.** Specify the population, intervention, comparison or baseline, intended outcome, timeframe, and important guardrail. Include the current approach or doing nothing as a real alternative, with its cost and risk. Use numbers where they meaningfully measure the claim; a precisely observable qualitative failure can also matter.
2. **Choose the consequential failure conditions.** Usually a few are sufficient. Cover the assumptions most likely to invalidate the decision or create serious harm. Three to five is a useful starting range, not a quota.
3. **Design a counter-test for each.** Define the measure, data source, sample or coverage, observation window, threshold, uncertainty, and competing explanations. Choose the least costly test that can answer the question credibly.
4. **Record the decision rule before inspecting confirmatory results.** State: "If [condition] is observed with [required evidence] by [decision point], [owner] will [action]." Explain which triggers act immediately, which require persistence, and how combined triggers work.
5. **Seek the strongest counterargument.** Imagine the claim failing and identify evidence or conditions that could cause it. Examine plausible failure cases, including those already present in real use. An AI-generated skeptic can suggest counter-tests; its objections are not independent findings or stakeholder dissent.
6. **Confirm ownership and review the result.** For a shared commitment, establish who has agreed, who can change or stop the outcome, and what capacity is reserved for that response. A signature or job title alone does not establish those conditions. Report actual agreement separately from a proposed sign-off. Evaluate the original claim honestly, including an inconclusive result, and record any change to the hypothesis or decision rule.

For example, replace "AI search improves the experience" with: "Over the agreed pilot window, at least 80% of eligible queries receive a verified answer within 90 seconds, compared with the current four-minute average baseline, without increasing support escalations beyond the agreed allowance." The new proportion-based target and old average are different measures; collect comparable baseline measures before claiming the size of the improvement.

## Protect against misleading evidence

A model demonstration can show that a result is possible without showing how often it succeeds or where it fails. Five selected successes from hundreds of attempts cannot establish reliability. The same concern applies to selected user praise or a convenient subset of production traffic.

| Pattern | What can mislead the team | What to examine |
|---|---|---|
| Demo bias | Only the best outputs are shown | The selection process, all relevant attempts, and representative cases |
| Average masking | A 90% aggregate hides a consequential segment near 40% | Segment performance, prevalence, uncertainty, and error severity |
| Metric gaming | Tickets fall 20% because failures are recategorized or users give up | Completed work, displaced effort, unresolved issues, and the measure's denominator |
| Distribution mismatch | An illustrative 85% evaluation score becomes 65% in production | Differences in inputs, labels, users, exposure, and environment |
| Silent failure | Plausible answers pass unnoticed | Direct correctness checks, user consequences, and feedback contamination |

For a measure tied to rewards or rollout targets, pair it with a measure of the underlying outcome or hidden cost. Sample apparently successful, unflagged, or rejected cases when that is where missed harm would remain invisible. Repeated accounts of one study are one underlying source; record whether evidence confirms, extends, limits, or contradicts the claim rather than pooling these as a support count.

These numerical contrasts are illustrations, not reported prevalence. A probabilistic system does not necessarily produce a success for every task, and neither an anecdote nor an aggregate tells the whole story.

**Pre-registration** records the question, measurement, and analysis before the confirmatory result. **Pre-commitment** records the action and authority before pressure to preserve the project grows. Both help; neither makes an inadequate test reliable or guarantees that a decision will be honored.

## Build the evaluation around the actual claim

Map each material claim to a measure that could challenge it. A search relevance score alone does not test whether people finish research faster. Deflection alone does not test whether support problems were solved.

Use binary criteria for genuinely binary requirements, such as whether the correct document was retrieved or a required condition was met. Use continuous measures, calibrated rubrics, or qualitative evidence where they fit better. A binary label does not remove ambiguity unless the underlying criterion is clear.

Define the difference between a stable regression set and held-out confirmatory data. A frozen set helps comparison; a held-out set has not been used to tune the relevant system or decision. Repeatedly optimizing against a frozen set can compromise its independence. Do not claim that a foundation model never encountered the data unless that is known.

Choose sample size and observation windows to match the decision. An experiment on 200 documents with an 80% completion target is one possible design, not a universal standard. Report uncertainty and important segments. Plan how interim looks, missing data, changing traffic, and insufficient evidence will be handled instead of declaring failure or success from a noisy early result.

### Let criteria improve without rewriting history

Shankar and colleagues use **criteria drift** for the way inspecting outputs can help people develop their evaluation criteria. That can be legitimate learning, not necessarily dishonest goalpost-moving. See [Who Validates the Validators?](https://arxiv.org/abs/2404.12272).

Explore and refine criteria openly, then version the criteria used for a confirmatory decision. If new learning changes the test, preserve the old result and explain the revision; use fresh or appropriately held-out evidence for the new claim where needed. Do not relabel the original failed claim as a success because another metric improved. Whenever the claim gains a mechanism, condition, or scope, update its disconfirming test in the same revision. Check that the test challenges the current claim rather than an obsolete version or the successful operation of its own remedy.

A test moving from fail to pass is evidence of improvement under that test, not proof that the product works generally. Likewise, a decline calls for investigation; the cause is not established by the score alone.

| Illustrative evaluation | Threshold | Launch | Month 1 | Month 3 | Month 6 | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| Sarcasm detection | 85% | 87% | 84% | 82% | 78% | Investigate a sustained decline; do not infer data drift without examining it |
| Task completion | 70% | 72% | 71% | 68% | 65% | Examine task mix, system changes, and measurement before choosing a response |

## Run a pre-mortem on the hypothesis

Imagine the feature failed after an appropriate period, such as six months. Consider these five failure families and select the ones relevant to the decision. `stress-test` examines technical and operational failure in more depth; reuse its evidence instead of repeating the same exercise.

| Failure family | Plausible story | Evidence to collect | Type of response to pre-agree |
|---|---|---|---|
| Model degradation | Performance falls after launch | Stable regression tests and fresh production samples | Investigate, restrict exposure, repair, roll back, or stop according to severity and persistence |
| Cost explosion | Query volume, retries, or review make the product uneconomic | Cost per successful task and total spend at the relevant scale | Bound spend, test alternatives, narrow scope, or reconsider viability |
| Trust damage | People correct, avoid, or work around the feature | Observed work, appropriate overrides, escalations, and research | Fix the failure, change the interaction, or pause the affected use |
| Data or environment mismatch | Production differs from the development setting | Stratified comparisons and trace inspection | Repair the gap or constrain the supported population |
| Competitive change | An alternative changes the value proposition | Current capabilities, customer choice, and switching evidence | Reassess differentiation and opportunity cost; a rival's launch alone need not imply exit |

For each selected risk, record estimated likelihood only when there is a basis, time to detect, time to recover, and who can act. [Counter-test examples](references/counter-tests.md) retain the numerical teaching cases with their interpretation limits.

## Measure AI-specific failure directly

| Claim | Counter-test | Interpretation to preserve |
|---|---|---|
| "AI reduces support tickets" | Measure solved issues, deflection, AI-caused tickets, and displaced effort separately | A ticket-count reduction can coexist with worse customer outcomes |
| "Users prefer summaries" | Compare completed work with the original available; examine reverts, edits, and their reasons | Editing can improve an otherwise valuable summary; edit distance alone is not rejection |
| "The model is accurate enough" | Evaluate relevant segments, complexity, and languages with error severity | A worst-segment failure can matter even when the aggregate passes |
| "Unsupported answers occur in fewer than 2% of responses" | Use a defined, blinded grading process on representative responses, with uncertainty | A 5% emergency stop threshold does not validate the separate under-2% claim |
| "Users trust the feature appropriately" | Observe when people rely, verify, override, and recover relative to actual reliability | Acting without checking can signal overreliance; willingness to use a low-stakes tool for high-stakes decisions is not a universal goal |

## Worked example: AI document search

This is an illustrative pilot design, not a validated research protocol or company result. All targets, costs, and sample sizes need justification for the actual case.

**Hypothesis:** "Within a 30-day pilot on a 10,000-document repository, at least 80% of eligible research tasks finish correctly in under 15 minutes, with task error at or below 3%. The current average is 45 minutes; collect the comparable baseline distribution and include verification work."

Use five explicit conditions rather than referring to conditions that are absent from the brief:

| Condition | Detection and decision point | Proposed response |
|---|---|---|
| Insufficient value | At day 30, average completed-task time remains above 25 minutes, alongside the primary target and uncertainty | Reassess the value hypothesis and test a hybrid search approach |
| Citation failure | A defined review finds unsupported citations in more than 5% of assessed results | Pause the affected output path or constrain exposure; verify citations and reassess before expansion |
| Unsustainable cost | Cost exceeds $0.08 per query at the assumed 10,000 daily queries | Investigate actual cost drivers and test appropriate caching, retrieval, or model changes under a quality constraint |
| Excess task error | Reliable evidence indicates task error above the proposed 3% guardrail | Contain affected use and investigate before continuing exposure |
| Insufficient retrieval quality | The correct document appears in the top three for fewer than the proposed 80% of eligible test queries | Investigate coverage and ranking; do not claim that retrieval alone explains task-time outcomes |

A day-14 review can act on early guardrail or spend breaches. It cannot declare that a day-30 value condition has elapsed. If the team proposes "two triggers mean stop," specify which triggers qualify, what evidence is required, and whether one severe trigger is sufficient. Do not automatically sunset on two incomplete or incomparable observations.

The earlier pilot design suggested 50 AI-assisted and 50 manual participants, a 20% time-improvement target, and citation reviews of at least 100 queries. Those are candidate design choices. Check sample adequacy and clarify whether 20% is an interim learning target or a separate success criterion; it does not equal the under-15-minute claim. Link outcome, citation, retrieval, and cost results to their respective hypotheses.

**Proposed commitment:** the accountable product, engineering, data, and business owners review the conditions before exposure and record who can pause, repair, pivot, or stop. Mark sign-off as pending until it actually occurs. For each action, make the operational commitment visible: the responsible person, time or capacity reserved, and the decision point. Creating this brief does not itself authorize an external launch or shutdown.

## Compare conflicting evidence fairly

External rejection can be mistaken, but "they do not understand it" can also protect a weak idea. Compare the actual evidence: population, task, artifact maturity, measurement quality, incentives, and alternative explanations. Private conviction is not a better instrument; external status is not automatically better evidence either.

The library's Tim Ferriss case describes self-reported persistence after 29 publisher rejections, supported by workshops with roughly a thousand students and written feedback. Treat it as an autobiographical illustration, not validation of a general rule. A proposal review and a workshop can measure different things; stronger audience response does not necessarily resolve a publisher's commercial concern.

Similarly, an evaluation on 2,000 production-like cases may be more relevant to reliability than a selected demo, while the demo discussion may expose a separate business or safety issue. Explain which claim each instrument addresses. If the comparison remains unclear, retain uncertainty and seek discriminating evidence rather than defaulting to either party.

## Connect to the rest of the library

- `bias-spotter` identifies reasoning habits that may protect an assumption; this skill turns the concern into a test.
- `problem-type` distinguishes technical and adaptive work; this skill gives a learning period a review point and a reason to change course.
- `judgment-guard` uses independent judgment before seeing an AI suggestion; both skills reduce the chance that later influence rewrites an earlier assessment.
- `stress-test` investigates load, cost, latency, failure propagation, and other operational threats.
- `eval-driven-development` operates and versions the evaluations; this skill defines what decision the evidence supports.
- `ship-decision` uses the agreed conditions in the rollout decision and escalation process.

The shared `UNIVERSAL-SKILL-PROTOCOL.md` is at the AI-PM source root or plugin root. Use its handoff guidance when another skill needs the result. Read [CONCEPT.md](CONCEPT.md) for conceptual influences and further illustrations.

## A reusable falsification brief

```text
Feature or decision:
Hypothesis: [population, intervention, comparison, outcome, timeframe, guardrail]
Evidence status: [known, assumed, untested]
Success criteria: [what supports the intended claim]
Failure conditions: [measure, threshold or observable event, evidence window]
Action for each condition: [investigate, contain, pause, repair, pivot, stop]
Evaluation mapping: [claim → test → decision rule → uncertainty]
Pre-mortem: [relevant risks, detection, recovery]
Counterargument: [strongest competing explanation and discriminating test]
Decision ownership: [who can act; actual agreement or pending review]
Criteria version and changes:
Next action and decision point:
```

## Check that the plan can be used

The claim should be capable of being challenged, the tests relevant, and the conditions measurable or clearly observable. Check denominators, units, windows, uncertainty, and consistency between the hypothesis and the decision rules. Confirm that owners know what they are being asked to do and that any reported agreement is real. Record the strongest counterargument and the response to inconclusive evidence.

The goal is to reduce consequential uncertainty, not to make every idea fail or avoid committing. A two-to-four-hour review is an illustrative time budget. Scale effort to the decision, name the remaining risk, and act on the best available evidence. If new information makes a rule inappropriate, document the reason and accountable decision rather than silently moving the goalposts.

A visual can connect the hypothesis to its test and action, showing how pre-registration addresses selective interpretation and pre-commitment addresses organizational reluctance. Use it when it clarifies the brief. Conclude with the proposed decision, its material trade-off, and the next test or review.

**Version 1.1.1, 13 SEP 2026.** Puts testability, decision rules, and evidence windows first; retains the pre-mortem, counter-tests, cases, brief, and library connections. Clarifies criteria learning, statistical uncertainty, actual sign-off, and the difference between a failed target and a stop condition.
