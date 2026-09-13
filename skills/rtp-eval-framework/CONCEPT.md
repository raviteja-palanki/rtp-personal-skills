# Evaluation Framework — Concept Guide

An evaluation framework connects a product's intended outcome to cases, evidence, scoring, and decisions. It helps detect failure, compare changes, and state what is still unknown.

What you measure influences development priorities, but measurement does not determine all behavior. Unmeasured qualities can improve, measured ones can remain unchanged, and optimization can help as well as exploit a weak metric. The practical discipline is to check whether the evidence supports the intended use.

## Two useful definitions

**Business:** a repeatable way to assess whether the product meets the quality and consequence requirements of its use case and to decide what to change.

**Technical:** a suitable combination of component tests, integration/end-to-end trials, human review, automated semantic scoring, and production monitoring. Not every system needs every layer. Each layer has a defined scope and failure response.

## Common measurement traps

- **Unstructured impression mistaken for broad assurance.** Reading ten outputs can reveal useful issues. It does not establish that rare failures or important user groups are covered. Record what was sampled and what the review can support.
- **Optimizing a proxy while losing the purpose.** Similarity can reward a wrong reference; a judge can reward style over substance; clicks can increase without useful decisions. Check the mechanism and outcome instead of assuming every metric is inherently gamed.
- **A narrow evaluation population.** A set of formal, patient users can miss multilingual, novice, constrained, or adversarial use. Sampling and reporting determine what generalizes.
- **Misreading annotation disagreement.** Seventy-three percent agreement is not proof that 27% of labels are noise. Differences can arise from ambiguity, valid perspectives, rater mistakes, prevalence, or mismatched evidence. Investigate before treating labels as ground truth.
- **Selection hidden by the source of examples.** Developer-produced examples are not necessarily cherry-picked, and production logs are not automatically representative. Document selection, coverage, and exclusions for both.

## Four illustrative cases

These examples preserve the original teaching mechanisms; their numbers are hypothetical, not audited deployments.

1. **Support classification:** 92% accuracy on 100 mostly English mid-market tickets coexists with 60% accuracy for an enterprise segment using non-English product names. Investigate relevant slices and sampling before claiming population reliability; the same test can be implemented correctly and still cover the wrong population.
2. **Content generation:** a judge marks 87% of outputs correct while users find them evasive. A separate human rubric yields 73%; the two percentages are not automatically comparable. Inspect whether the judge rewarded hedging rather than clarity, then test outcomes under a common, versioned standard.
3. **Recommendations:** click-through rate changes from 15% to 11% while revenue improves. CTR is not conversion rate. Examine relevance, diversity, purchase decisions, abandonment, and time to purchase; fewer clicks need not mean worse recommendations. A thirty-second conversion target is only appropriate if justified by the task.
4. **Fact checking:** 68% agreement prompts review of “mostly true” versus “misleading without context.” Separate factual errors from interpretation and evidence gaps. Reasons and adjudication can make the result actionable without pretending all disputes must disappear.

## Compose the dataset deliberately

Use a coverage matrix across relevant dimensions:

| Dimension | Candidate coverage |
|---|---|
| User/context | Experience, role, language, accessibility needs, legitimate permissions |
| Complexity | Direct lookup, multi-step work, ambiguity, conflicting evidence, recovery |
| Domain | Common tasks, consequential rare tasks, unsupported requests, plausible attacks |
| Time/state | Relevant recent and historical cases, product versions, state transitions, changing conditions |

Adversarial behavior is a scenario, not a fixed kind of person. The source's 20/50/20/10 user mix, 30/40/20/10 complexity mix, 60/20/15/5 domain mix, and equal month-1/3/6/12 samples are illustrative marginal allocations. They do not ensure the combinations of dimensions are covered. Separate population-representative estimates from deliberately enriched stress sets; use sampling weights when making a population claim that requires them.

## Validate the judge without reusing the answer key

Select qualified reviewers and reference evidence. Label cases under clear criteria, inspect disagreements, and assess reliability in a way suited to the scale. Fleiss' kappa treats categories nominally; use an appropriate ordered-score measure when distance between ratings matters.

Use development cases to improve the rubric and judge prompt, then assess on held-out cases and relevant slices. Check both wrongly accepted bad outputs and wrongly rejected good ones. A 50-case/five-reviewer exercise can teach the team; a two-to-four-hour estimate or 80% agreement does not establish production readiness. Repeatability, sample uncertainty, severe failures, and the decision's consequences matter. See `confidence-tuner` for the detailed method.

## Connect evaluation to value and regression response

Compare meaningful user outcomes across appropriately defined exposures or cohorts. People who receive easy tasks may obtain high eval scores and also retain more, without the score causing retention. Confounding, ceiling effects, and sparse outcomes can limit correlation analysis. Experiments, case review, outcome audits, and other designs can complement it; quarterly correlation is not the only valid instrument.

A regression detector balances missed deterioration against unnecessary alerts. A twenty-percent drop threshold may miss meaningful changes; a two-percent threshold may react to noise. Define whether “percent” means relative change or percentage points. Choose thresholds using severity, sample size, paired comparisons, baseline variability, repeated monitoring, and the response the alert triggers.

Running a fixed set ten times can reveal some trial variability, but not every production shift. Three times the observed standard deviation is a possible heuristic under suitable assumptions, not a universal optimum or a guarantee against false alarms. Separate measurement uncertainty from minimum meaningful change.

## Intellectual influences and further reading

The original guide draws broadly on Eugene Yan's practical ML evaluation work, Aman Khan's AI evaluation practice, Katherine Lee's work on models/data, human-feedback research associated with John Schulman, and Pearl/Mackenzie's causal-inference explanations. These are intellectual influences; the original exact title/author pairings were not all verified and should not be used as precise citations without checking.

For verified primary links and corrected numerical research cases, use [evidence and validity notes](references/evidence-and-validity-notes.md). The main [skill](SKILL.md) supplies the workflow and handoffs.
