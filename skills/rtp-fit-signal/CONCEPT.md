# Fit Signal — Concept Guide

Fit means repeatable value for a particular group and job under relevant market conditions. Users may reveal it through continued use, successful outcomes, preference, advocacy, payment, or renewal. AI adds questions about variable quality, verification effort, and whether reliance is appropriate. It does not make established product metrics meaningless.

## Why one attractive number can mislead

High engagement can mean useful work, curiosity, or repeated repair. A longer session can mean deeper value or more friction. An NPS response concerns recommendation, not every dimension of quality or trust. A reuse index measures observed treatment of outputs under its rubric; it cannot distinguish a correct unedited answer from an unchecked wrong one by itself.

Trust, satisfaction, and use can be related without being interchangeable. They are not inherently statistically independent. The right comparison asks whether people repeatedly achieve the intended outcome at acceptable effort, cost, and consequence.

A stable product can still lose fit when needs or alternatives change. An AI product can have fit despite variable outputs when the complete workflow delivers value and handles its limitations well. Creative collaboration may deliberately involve substantial editing; that does not make the product a failure.

## Five traps and the checks that address them

| Trap | Better check |
|---|---|
| Engagement is mistaken for dependence | Observe the work accomplished, repeated need, and avoidable effort |
| A cohort average hides difficult experiences | Inspect individual/account trajectories, task segments, uncertainty, and attrition |
| Fewer corrections are treated as better quality | Check reasons, review coverage, verified errors, and downstream outcomes |
| An aggregate benchmark is treated as a market verdict | Weight performance by relevant tasks, consequences, alternatives, and user value |
| Recommendation is treated as complete trust | Ask about intended use and checking; compare perceived trust with observed reliability |

The reverse mistakes matter too: more corrections can follow better reporting, a lower trust rating can reflect better calibration, and a flat high trajectory can be healthy. Fit analysis should explain these patterns rather than attach a verdict to their direction alone.

## Example 1: Two coding assistants

This is a fictional comparison using numbers from the earlier teaching example, not a historical claim about two vendors.

| Measure | Assistant A | Assistant B |
|---|---:|---:|
| Aggregate task success | 81% | 73% |
| Sessions per week | 4 | 2.5 |
| NPS | 44 | 51 |
| Eight-week retention | 62% | 71% |
| Illustrative reuse index at week eight | 0.52 | 0.65 |

A has better aggregate task success, while B already has stronger recommendation and retention in this table. It would be incorrect to say all traditional metrics favor A or that only a trust curve detects B’s appeal.

Possible explanations include B performing better on common valuable tasks, giving clearer warnings, requiring less review, or serving a different cohort. Compare matched tasks and users, inspect consequential failures, and measure effort. The earlier undefined “±25% versus ±8% variance” is not a usable statistic without a variable, estimator, and sample. Consistency matters, but consistently wrong output does not beat accurate output as a general rule.

## Example 2: Fast support answers without reliable resolution

A fictional support product reports 35% initial deflection, 4.2/5 satisfaction among surveyed initially deflected cases, NPS 42, and 58% retention. Those numbers do not establish that issues were resolved, but they are still evidence to interpret.

Define deflection’s time window and identify later contacts about the same issue. A case can avoid escalation in the initial session and still require help later; without the window, “deflected but escalated” sounds contradictory. Match satisfaction responses to eligibility and follow-up, including users who abandoned the process or did not answer the survey.

Check resolution, repeat contacts, corrections, review effort, and the job users value. Fast acknowledgement may itself have value, but it is different from reliable resolution. A reuse index of 0.48 would not, by itself, prove either job lacks fit or explain subsequent customer churn.

## Example 3: Privacy expectations and a research assistant

Suppose a fictional study observes these reuse-index trajectories in two cohorts:

| Period | Earlier cohort | Later cohort |
|---|---:|---:|
| 1 | 0.42 | 0.48 |
| 2 | 0.45 | 0.56 |
| 3 | 0.44 | 0.62 |
| 4 | 0.43 | 0.68 |

Between cohorts, the product changed its data-retention design and explanation. NPS rose from 38 to 41 and retention from 45% to 52%. The latter is a seven-percentage-point increase, about 15.6% relative; whether it is meaningful depends on sample, uncertainty, and context.

These observations make privacy a plausible explanation, not an established cause. Check other product changes, acquisition, task mix, and user accounts of the barrier. Test a clearer explanation or different approved design where appropriate. Any privacy promise must accurately describe actual storage, logs, backups, and exceptions; do not use “we never retain your data” as an unsupported conversion tactic.

## Example 4: Finding an activation candidate in legal research

A fictional platform observes the following associations:

| Use case | Reached candidate event | Later retention among those who reached it |
|---|---:|---:|
| Case-law search: five useful searches | 15% | 75% |
| Contract analysis: one useful analysis | 40% | 82% |
| Regulatory checking: one completed check | 8% | 70% |

Contract analysis is worth investigating. It is not automatically the winning market: the events demand different effort, users may have different needs, and retention among non-attainers is missing. A person who completes five searches has more opportunity to be selected for continued use than someone whose event requires one task.

Use a fixed early observation window, compare opportunity and task mix, and measure later outcomes in a separate window. Test whether improving the path to useful analysis helps comparable users, or whether the event simply identifies those who already need the product most. Choose investment from the total opportunity and evidence, not an automatic 80% allocation.

## Keep scope and uncertainty attached to the verdict

“Emerging among frequent contract reviewers in this pilot” is useful. “PMF confirmed because trust exceeded 0.60” hides the assumptions. A scorecard should preserve alternative explanations, evidence gaps, and what would justify expansion or reconsideration.

Small samples may support case-level learning without precise population estimates. Infrequent and offline products need observation periods suited to the task. Subjective products can use judged usefulness, preferences, and repeated outcomes rather than pretend editing is a binary defect. Technical correctness alone also leaves usability, reliability, and commercial questions unanswered.

Switching friction is a separate economic property. It can reflect integration value or a captive customer. It does not need to exceed the seller’s acquisition cost to establish fit; those quantities describe different parties and decisions. Use `cost-model` and `token-economics` for the economics alongside the fit evidence.

## Lineage and further reading

Sean Ellis’s disappointment question and Rahul Vohra’s segmentation method are useful inputs, not universal proofs of fit. Vohra’s [first-hand account](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) describes a survey-driven process for Superhuman; it does not establish that AI products cannot use surveys or retention measures.

The established paper *Trust in Automation: Designing for Appropriate Reliance* is by **John D. Lee and Katrina A. See (2004)**, not Elaine May. The [evidence notes](references/fit-evidence.md) distinguish the verified citation from this revision’s access limits and explain the other research checks. Use the [main skill](SKILL.md) for the working process.
