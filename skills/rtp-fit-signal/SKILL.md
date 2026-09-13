---
name: fit-signal
version: v1.3.1_latest
description: 'Assess whether an AI product delivers repeatable value for a defined user segment and use case, then recommend scale, iteration, diagnosis, or a pivot. Combine longitudinal trust and use, verified output quality, correction patterns, retention, buying behavior, and alternatives. Distinguish useful reliance from curiosity, overconfidence, resignation, or lock-in. Treat the fidelity-weighted reuse score as a behavioral proxy, not a validated measure of trust or proof of product-market fit. Identify candidate activation moments and test whether they predict later value. Deliver a four-verdict scorecard with evidence, uncertainty, and conditions that would change the recommendation. Use with pilot or production evidence; adapt depth to sample size and task frequency rather than requiring 100 weekly users or eight weeks. Pre-launch work can define the measurement plan. Pairs with falsification, feedback-flywheel, stress-test, and ai-product-metrics.'
imports:
  - falsification
  - feedback-flywheel
  - stress-test
---

# Fit Signal

Determine whether a specific group repeatedly gets enough value from the product to choose it for a real job. Separate that evidence from curiosity, repeated troubleshooting, habit, subsidies, and inability to switch. State what the evidence supports now and what would change the decision.

**No single metric proves fit.** Retention, NPS, usage, and surveys remain useful for AI products; they do not require perfectly deterministic experiences. Add the distinctions AI makes especially important: output quality, review effort, appropriate reliance, and the consequences of errors. A rising trust curve is also vulnerable to selection, overconfidence, and measurement error.

The aim is **warranted reliance**, not maximum dependence or unconditional trust. A user who values a tool and checks consequential outputs may be using it exactly as intended.

## Set the scope before interpreting signals

Reuse the brief under the Universal Skill Protocol. Record the user segment, job, alternative, product/model version, task frequency, commercial context, and decision being made. Use `jtbd-analysis` and `ai-product-taste` to define the intended value and meaningful first success. Ask only for missing information that changes the analysis.

Use available pilot or production evidence. Eight weeks can be a useful observation period for a weekly product; it is neither necessary nor sufficient for every product. Sample adequacy depends on independent users/accounts, task volume, variability, effect size, and decision consequence. A small enterprise cohort can yield meaningful qualitative and behavioral evidence. Batch and offline products can be assessed through repeated jobs, downstream outcomes, and renewals.

Before launch, define the plan and use discovery or prototype evidence for an early judgment. Do not claim observed retention or sustained fit without actual use. For a deterministic feature, omit AI-specific measures that do not add value.

Answer four questions:

1. Are trust, actual use, and verified outcomes becoming better aligned over time?
2. Which early experience predicts later value, and is it a cause or just a marker?
3. Are fewer corrections evidence of better results, changed work, or less checking?
4. What decision is justified for this segment, with what uncertainty and review condition?

## 1. State what would challenge the fit hypothesis

Use `falsification` to define the hypothesis, expected observations, competing explanations, and decision criteria before a prospective test. When analyzing existing data, label the work exploratory and validate important findings on fresh evidence. Do not pretend a rule was pre-registered after seeing the results.

Four counterfactual questions are useful, but none is an automatic kill condition:

| Question | What the answer can help distinguish |
|---|---|
| Would the workflow remain valuable without its AI component? | Overall workflow fit versus the AI component’s incremental value |
| Would a different model produce an equivalent experience? | Dependence on a particular model versus value elsewhere in the product |
| How would users respond to a different price or package? | Willingness to pay, alternatives, affordability, and segment economics |
| What would users do if the product were unavailable? | Urgency, frequency, fallback options, and consequences of disruption |

A price-sensitive user may still prefer the product. A user finding an alternative during downtime may demonstrate a real need. A product can have fit without a model moat. Ask or study these counterfactuals proportionately; the skill does not authorize a live outage, price change, or competitor enrollment.

## 2. Track trust, reuse, and quality separately

Maintain three related views:

- **Perceived trust:** direct, consistently worded questions about confidence in using the product for the defined task and the checking users believe it needs.
- **Observed reliance:** whether outputs are used, edited, rejected, or acted on, and how much review effort precedes use.
- **Verified quality and value:** independent checks appropriate to the task, downstream outcomes, and the user’s actual benefit.

Use the same event log to connect these views without assuming one proves another. Track product version, task type, user/account, date, exposure, and outcome where collection is permitted and useful. Missing downstream visibility is an uncertainty, not automatic evidence of use.

### Optional fidelity-weighted reuse index

The original skill’s “trust score” is better named a **reuse index**. Its weights are illustrative and unvalidated; retain them only when they help summarize a stable rubric.

| Observed disposition | Illustrative weight | Record separately |
|---|---:|---|
| Used as provided | 1.0 | Whether reviewed and whether the result was correct |
| Used after minor change | 0.6 | Cosmetic/preference edit versus correction |
| Used after major change | 0.2 | Material error, changed scope, or collaborative drafting |
| Rejected or regenerated | 0.0 | Failure versus deliberate exploration or variation |
| Unknown or pending use disposition | Not scored | Coverage gap and reason |

Define minor and major by their effect on the task, with examples. Avoid gaps such as “under 30%” and “over 50%” text changed. One altered digit can be consequential; a large stylistic rewrite can be harmless. An unedited output is not necessarily an accepted or verified output.

For ten outputs with known dispositions—six used as-is, two minor edits, one major edit, and one rejection:

```text
Reuse index = (6×1.0 + 2×0.6 + 1×0.2 + 1×0.0) / 10 = 0.74
Major-edit/rejection share = (1 + 1) / 10 = 20%
```

The second number is a disposition rate, not automatically an error rate. To measure corrective intervention, use reason-coded interventions with a stated denominator. Report unknown dispositions and observation coverage. Do not quietly map old “trust” series to the new name without noting the definition and rubric version.

### Read trajectories with their denominators

An illustrative eight-period series—0.42, 0.45, 0.48, 0.51, 0.58, 0.62, 0.65, 0.67—suggests improving reuse under that rubric. It does not establish trust calibration or fit at a 0.60 cutoff.

- A stable high level can be healthy; an upward inflection is not required.
- A rise can reflect quality improvement, easier tasks, learning, weaker review, or departure of dissatisfied users.
- A fall can reflect a regression, harder tasks, or better recognition of limitations.
- Volatility can reflect genuine variation or sparse measurement. Investigate rather than assume a fixed “normal” weekly swing.

Show sample sizes, coverage, task mix, product changes, and uncertainty. Repeated outputs from one user are not independent users. Keep acquisition cohorts and follow-up windows consistent; include churn and missing responses. Distinguish an output-weighted average from an average across users so a few heavy users do not silently define the result.

Segment by use case and relevant customer differences. Use attitudinal segments from `attitudinal-segmentation` when evidence supports them; do not label low-frequency users “skeptics” merely from frequency. A 0.72 index in one segment and 0.38 in another is a prompt to investigate, not proof that one has fit and the other should be killed.

## 3. Identify a candidate activation moment

Find an early interaction that plausibly helps users realize the product’s value: completing a useful task, successfully revising and using a draft, sharing an output that helps a colleague, or returning when the need recurs. Call it a **candidate magic moment** until it is validated. Not every product has one discrete moment.

Compare users who reach it with comparable users who had the opportunity but did not. Specify the exposure window before the retention/outcome window. Avoid selecting only surviving power users or defining the event using behavior from the very period you are trying to predict. A user who must remain active for weeks to “hit the moment” has already been selected for retention.

An illustrative cohort table might show:

| Usage cohort | Reached candidate event | Later retention if reached | Later retention if not |
|---|---:|---:|---:|
| Frequent | 70% | 78% | 32% |
| Regular | 45% | 65% | 28% |
| Occasional | 20% | 55% | 18% |

These are hypothetical associations, not causal effects or target values. Check need frequency, onboarding opportunity, customer type, task difficulty, and acquisition source. An occasional user may get excellent value without weekly use. A low event rate could mean poor onboarding, the wrong event, or a different job.

Test a plausible improvement with `gen-ai-experimentation` when warranted and authorized, or validate prediction in a fresh cohort. Do not force users through arbitrary repetitions to raise the event count. Retain quality, time-to-value, and later value as checks against optimizing a proxy.

## 4. Explain correction patterns and test for silent failure

Track major edits, rejections, regenerations, verified errors, review effort, and downstream use by reason and task. Where useful, calculate relative change from a stated baseline: a decline from 60% to 15% is a **45-percentage-point** or **75% relative** reduction. If the baseline is zero, relative reduction is undefined.

Falling corrections can mean better output, better task selection, less ambitious use, changed expectations, or resignation. Flat or rising corrections can result from harder tasks, better detection, or an interface that makes feedback easier. Neither direction diagnoses quality by itself.

Use complaints and downstream behavior as clues, then check an appropriate sample independently:

| Pattern | Hypotheses to investigate |
|---|---|
| Corrections fall; verified quality and useful outcomes improve | Product or workflow improvement |
| Corrections fall; complaints rise or useful use drops | Unresolved errors, avoidance, resignation, or reporting changes |
| Corrections fall; use continues but checking disappears | Appropriate reduced effort or unsafe over-reliance; verify which |
| Corrections rise; quality looks stable | New task mix, higher standards, easier feedback, or a measurement change |

Low complaints do not rule out silent mistakes. Continued action is not proof that the action was sound. Match error detection and follow-up to consequence, and report what remains unobservable. Do not prescribe fixed code-versus-creative acceptance rates or a universal eight-week correction reduction.

### Check whether feedback is used

With `feedback-flywheel`, inspect a manageable sample of consequential and common correction patterns. Trace capture, interpretation, ownership, and the resulting decision: prompt/retrieval/model/interface change, training, clarification, or a justified decision not to change. Verify effects where a change was made.

No recent product edit does not prove resignation; users may learn, tasks may change, or the existing behavior may be right. A funded loop can still fail, and an unfunded one has an identifiable capacity gap. Do not count raw feedback collection as improvement.

## 5. Distinguish preference, buying intent, and switching friction

Retention can reflect value, habit, contractual constraints, migration cost, or lack of alternatives. Payment and renewal are important commercial evidence, but neither proves trust alone. A valuable product with easy export can have strong fit and low switching friction.

Inspect early abandonment, competitor comparisons, voluntary return, paid conversion, renewal, repeated valuable use, and users’ explanations. Define each denominator; “came back after trying a competitor” is measured among relevant trials, not all users. Fifty interactions can be productive work or repeated attempts to fix a problem.

When a direct comparison is needed, design a consensual, appropriately scoped study with equivalent tasks and onboarding. A 20–30-person exploratory trial may reveal reasons, not establish a universal 70% return benchmark. Price research should distinguish stated intent from actual behavior and account for demand and revenue effects. Do not infer a sustainable premium solely because fewer than 5% say they would leave after a 20% increase.

### Interest and founder-led sales

AI may make some outreach and demonstrations cheaper. That can weaken a particular signal without making all interest worthless. Look for a concrete problem, decision owner, credible budget or resource commitment, implementation work, and timing. A trigger event can emerge through a good question; it need not be volunteered unprompted.

Use the SPRINT lens where founder-led selling is relevant:

| Element | Evidence to look for |
|---|---|
| **Speed** | The buyer recognizes that the seller understands their situation |
| **Problem** | A specific need and reason to act within a meaningful period |
| **Results** | An observable outcome the buyer can explain to other decision makers |
| **Implementation** | Open risks, integration needs, and a credible way to address them |
| **Niche** | A repeatable customer/problem combination, without forced over-narrowing |
| **Trust** | Credibility supported by evidence and relationships beyond the founder |

Buyer silence can reflect risk, budget, priorities, fit, or timing. Investigate instead of assuming an unseen objection. Founder credibility can transfer through references, a capable team, and demonstrated delivery; it is not destined to become a liability. SPRINT is an interview-derived diagnostic lens, not a validated fit score. [Source details](references/fit-evidence.md)

### Read satisfaction distributions

Keep the full distribution and relevant top-category shares when averages hide differences. Research supports investigating nonlinear satisfaction–retention relationships; it does not establish that every “4” is commercially weak and only “5s” predict retention. Test the relationship in the relevant product and segment. NPS has its own recommendation question and categories; it is not an average of a five-point satisfaction scale. [Research context](https://business.rice.edu/wisdom/peer-reviewed-research/product-marketing-customer-satisfaction)

## 6. Revisit the underlying need before a pivot

Separate the **instinct**—a belief about a better way to serve a need—from the **idea**—the specific product that attempts it. For example: “booking a contractor requires too much coordination” versus “a marketplace app is the answer.”

A failed implementation can challenge the packaging, the need, or both. Write the belief without the product and ask which evidence bears on it. Consider several credible alternatives—four or five can be a useful exercise—and learn from other approaches. Do not protect the belief from falsification by declaring every failure merely a packaging problem. Balance another test against the cost of continuing and the strength of contrary evidence.

## 7. Issue a scoped verdict

Use a qualitative scorecard with actual evidence, pre-agreed criteria where available, limitations, and the next decision. Do not collapse these different dimensions into an unvalidated points total.

```text
Segment / job / version / cohort / observation period:
Decision under consideration:

Signal                         Evidence, coverage, uncertainty        Read
Repeated useful outcomes       ...                                    ...
Trust and verified reliability  ...                                    ...
Reuse and correction patterns  ...                                    ...
Candidate activation event     ...                                    ...
Feedback response              ...                                    ...
Retention and demand           ...                                    ...
Preference and buying behavior ...                                    ...
Economics and readiness        ...                                    ...

Verdict / confidence / strongest competing explanation:
What would change it / next action / owner / review date or event:
```

| Verdict | Meaning and next action | Revisit when |
|---|---|---|
| **CONFIRMED for this scope** | Converging evidence supports repeatable value, meaningful demand, and appropriate reliance for the stated segment. Consider measured expansion after economics and operational checks. | Quality, demand, retention, alternatives, or the scope changes enough to undermine the case |
| **EMERGING** | Promising repeated value exists, but durability, breadth, or a competing explanation remains unresolved. Invest in the most informative bounded improvement or test. | New evidence supports durability or reveals that the promising pattern does not hold |
| **UNCERTAIN** | Evidence is sparse, conflicting, or poorly measured. Diagnose the decisive gap before selecting a fix or pivot. | A defined measurement or test resolves the uncertainty |
| **ABSENT for this scope** | Adequate relevant evidence contradicts the fit hypothesis. Stop, narrow, or pivot according to consequences and remaining options. | Materially new evidence or a meaningfully changed proposition warrants reconsideration |

“Confirmed” is a current decision judgment, not permanent proof or authority to ship adjacent features. Every verdict, including absent, has a stated scope and reconsideration condition. Stable performance does not automatically downgrade emerging evidence; a plateau may be the expected healthy outcome.

## Review and connect the decision

- [ ] Segment, job, version, frequency, and decision scope are clear.
- [ ] Evidence sufficiency and uncertainty are assessed without a universal user-count or time gate.
- [ ] Prospective criteria and exploratory findings are distinguished.
- [ ] Perceived trust, reuse, and verified quality are separate; denominators and missing data are visible.
- [ ] Cohort composition, attrition, task mix, and product changes are checked.
- [ ] The activation candidate is tested without treating association as causation.
- [ ] Correction patterns are checked against independent quality and downstream use where possible.
- [ ] Feedback decisions and preference/constraint explanations are examined.
- [ ] The verdict, competing explanation, change condition, owner, and next action are stated.

`ai-product-metrics` supplies events and outcome definitions; `uncertainty-research` helps with longitudinal inference. `failure-modes` diagnoses quality failures and `problem-ai-fit` revisits the problem/approach. An absent inflection alone does not identify the hidden job as wrong.

Use `stress-test` and `cost-model` early enough to shape a scaling decision, not only after declaring fit. `ship-decision` combines fit evidence with actual release constraints. Send resource choices to `ai-portfolio-management`, unresolved causal questions to `gen-ai-experimentation`, and the scoped verdict to `stakeholder-communications`.

Deliver the recommendation, strongest evidence, main uncertainty, trade-off, and next action. A longitudinal chart with sample sizes and product changes may help; add cohort bars or a verdict table only when useful. Use `excalidraw-svg` if an explanatory diagram is appropriate. The [concept guide](CONCEPT.md) and [evidence notes](references/fit-evidence.md) provide examples and source boundaries.
