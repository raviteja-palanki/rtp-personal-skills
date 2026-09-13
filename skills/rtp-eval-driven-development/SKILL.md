---
name: eval-driven-development
version: v1.1.1_latest
description: 'Use evaluation to define useful AI behavior, guide development priorities, and protect it as the product changes. Use when a team lacks a clear definition of done, iterates without understanding failures, or needs a repeatable path from evidence to the next change and release decision. Connect product intent to versioned Data–Task–Scores, error analysis, capability and regression suites, calibrated judges, and separate quality, safety, cost, and latency criteria. Keep successful cases as regression coverage while adding relevant new challenges; document rubric changes without moving the bar merely to improve scores. Covers quality ownership, stage reviews, source provenance, review cadence, CI/CD gates, and diagnosing when workflow, access, pricing, or distribution is the real constraint. Pairs with eval-framework, confidence-tuner, ai-prd, ship-decision, production-observability, and feedback-flywheel.'
imports: ["eval-framework", "feedback-flywheel"]
---

# Eval-Driven Development

Make the definition of useful behavior concrete enough to guide the next change, and keep evidence that the product still meets it. The evaluation suite connects product intent, quality ownership, and regression protection.

## Start with intent and the current decision

Use this skill to establish an evaluation practice, choose the next development priority, or repair a loop whose scores no longer reflect product needs. For a narrow change, inspect its intended effect, relevant failure cases, and regression risk. Reuse the request's context and format; ask only for missing information that materially changes the work.

Write a concise intent statement: who needs what outcome, why it matters, the supported scope, actual action permissions, and unacceptable failures. Pair it with an evaluation suite. The suite is an executable part of the specification; it does not replace requirements about customers, UX, rights, operations, or unresolved decisions. A one-page intent document is a useful starting point, not a page limit.

Begin evaluation early enough to inform design. A small prototype or examination of outputs may be necessary to discover the right criteria; a complete suite need not precede the first prompt. An existing product can adopt this practice now. The relevant standard is evidence appropriate to the next decision, including qualitative evidence where numerical scoring is unsuitable.

Before optimizing, inspect failures and confirm that they represent a product problem. A 40% failure rate on long documents is a priority candidate, not automatically the next sprint: weigh exposure, severity, customer value, uncertainty, and repair cost against other needs. Evals can confirm that no change is needed. They inform the backlog alongside discovery, incidents, strategy, and business constraints.

## 1. Build the first useful evaluation

Use **Data → Task → Scores** to make the specification reviewable:

| Artifact | What to record |
|---|---|
| **Data** | Versioned cases, source and sampling method, relevant context, reference evidence, labels, privacy/retention limits, and intended population |
| **Task** | User goal, starting state, available tools, permissions, allowed interaction, expected outcome, and material constraints |
| **Scores** | Rubric or tests, scorer and version, per-dimension results, pass rules, uncertainty, costs, and evidence explaining failures |

Follow five steps:

1. **Define success.** Translate “helpful” into observable task outcomes. For a summarizer, identify required main points and consequential omissions. Keep task quality, safety, honesty, latency, and cost separate. A thumbs-up rate is feedback, not a substitute for factual validity.
2. **Create a manageable initial set.** Start with enough representative cases to expose important ambiguity and plausible failures. Twenty to fifty examples can support early learning; consequential rare failures require targeted coverage and appropriate statistical precision. Include long documents, multiple main points, and conclusions away from the end when relevant. Do not imply every imagined edge case will occur.
3. **Choose a rubric and scorer.** Binary checks suit clear requirements; anchored ordinal ratings or pairwise comparisons can capture meaningful degrees of quality. Exact match suits exact outputs. ROUGE or embedding similarity may add a signal, but similarity alone does not establish correctness or usefulness. Validate automated and human scoring for its intended role.
4. **Run a fair baseline.** Use the current workflow and a simple plausible approach, including deterministic or non-AI alternatives when relevant. Record configuration and results. A baseline is a comparator, not itself a statistical null hypothesis. A candidate may validly preserve quality while reducing cost; it need not beat every baseline score.
5. **Build and iterate against a stated hypothesis.** Describe the failure category, proposed mechanism, intended improvement, possible regressions, and evidence that would change the recommendation. Keep development/tuning examples separate from held-out claims about generalization.

Use `eval-framework` for the test architecture and `confidence-tuner` for judge reliability. Not every scorer is an LLM. Deterministic checks need correct assertions and environments; human labels need clear criteria and disagreement handling. Report sample counts, repeated-trial variability where material, and uncertainty instead of treating one run as definitive.

## 2. Diagnose errors before choosing a fix

The five-step error-analysis loop is the engine of the practice:

1. **Collect failures and inspect evidence.** Read traces, input context, outcomes, and grades. Also sample passes to look for false reassurance. First distinguish product failure from an invalid test, a broken environment, missing evidence, or a judge error.
2. **Group observable failure patterns.** Useful starting categories are unsupported claims, misunderstood input, out-of-scope behavior, inconsistent performance, and excessive latency or cost. They are not proven root causes. Link failures to the state transition where they become visible, such as Generate SQL → Execute SQL, while tracing possible upstream causes.
3. **Prioritize impact.** Consider consequence, frequency, affected users, detectability, and feasible remedies. A missing edge detail may be critical; “users still get 80% of the value” cannot determine severity without evidence.
4. **Form a repair hypothesis.** Candidate changes include prompt, retrieved context, data quality, tool contract, workflow, model, fine-tuning, post-processing, or narrower scope. Avoid inventing an internal mechanism from an observed pattern; a length-related failure does not prove attention diffusion at 500 tokens.
5. **Test locally, then broaden appropriately.** A small failing slice gives fast feedback. A promising change then needs relevant regressions and release checks; rerunning the full suite can be sensible from the start when cheap or needed for an interacting change. Passing the examples used to design the fix is not evidence of broad generalization.

It is acceptable to say that the cause is not yet known and inspect logs or code. Clear uncertainty and a useful diagnostic step are better than a confident untested explanation.

## 3. Maintain cases and criteria with a clear lifecycle

Use two complementary tiers:

- **Capability/challenge cases** test relevant behavior the system is still learning or whose limits remain uncertain.
- **Regression cases** protect behavior already supported. A mastered challenge can graduate into this tier.

A high regression pass rate is desirable. A saturated challenge set prompts a coverage review; it does not prove product perfection, but neither must a scoped product always have failing cases. Add harder **relevant** tasks when they illuminate a real goal or risk. Do not manufacture failure to keep a dashboard interesting.

Preserve useful regression coverage when adding current production cases. A frozen version provides comparability; “frozen” does not mean retaining every case forever. Retire or replace a case for a documented reason such as obsolete scope, invalid labels, duplication, changed requirements, or retention obligations. Preserve the audit trail and meaningful coverage. Ease alone is not a reason to discard a regression check.

Track provenance, age, coverage, and relevance. New is not automatically representative; old is not automatically stale. Review sanitized production failures, support reports, synthetic cases, and adversarial probes at a cadence that fits traffic and changes. A fixed rule to replace 20–30% monthly can destroy useful comparability. Keep development sets, release holdouts, and fresh audits distinct enough to detect overfitting; rotating visible cases alone cannot guarantee generalization.

### Let criteria improve without hiding a change in the standard

Some criteria are known before development; others emerge while inspecting outputs. Shreya Shankar and colleagues call this interaction **criteria drift**. When evidence reveals a missing or ambiguous distinction, merge or split categories and record what prompted the change.

For each material rubric change, record old and new definitions, rationale, affected cases, responsible owner, and whether results remain comparable. Re-score a bridge set under both rubrics where needed. A lower bar may be justified by corrected requirements, but changing it merely to turn a failed release green is not improvement. A stable valid rubric does not mean the team stopped learning.

## 4. Assign quality ownership and efficient review

The **Intent Architecture ladder** describes four kinds of responsibility:

| Responsibility | Practical ownership | Evidence artifact |
|---|---|---|
| **Example** | Define criteria, label cases, resolve ambiguity | Graded examples and reasons |
| **System** | Make evaluation and monitoring repeatable | Pipeline, reports, ownership, response path |
| **Constraint** | Establish and enforce action boundaries | Permission checks, gates, intervention tests |
| **Intent** | Define goals and verify outcomes across delegated work | Goal/constraint contract and outcome evidence |

These responsibilities coexist. They are not a universal career hierarchy, nor proof that a PM alone should design infrastructure or security controls. Intent-level operation still needs oversight and does not mean the system can formally prove every outcome. Product, domain, engineering, operations, and risk owners contribute according to the decision.

Run the original five-part operating loop in a form the team can sustain:

1. **Transition Failure Matrix:** locate the failure and evidence, distinguish its visible location from its cause, and link it to a proposed test.
2. **Accountable adjudication:** name who resolves material rubric disputes and how specialist review or appeal works. The source's “benevolent dictator” emphasizes accountability; it is not a requirement to replace qualified panels or force subjective disagreement into one person's unchecked verdict.
3. **Decision plus written critique:** use pass/fail where the requirement is binary and retain the reason or evidence. Use anchored ratings where degree matters, and “unresolved” where evidence is insufficient. Critiques can improve rubrics; do not automatically treat them as ground truth or training data without review and appropriate rights.
4. **Validated scoring:** inspect relevant class-specific judge errors and reference-label quality before using the result to gate a change. Keep positive-class labels consistent; probability calibration is a separate question.
5. **Useful annotation tools:** show the artifact as reviewers need to inspect it—email, document, trace, or actual task outcome. Choose existing tools, a spreadsheet, or a custom interface by review quality, time, accessibility, privacy, and maintenance cost. A custom or quickly coded tool is not inherently superior.

Practice the full loop on one real use case. The accumulated evidence can be a durable capability if it improves repeated decisions; calling it a moat requires more than counting labeled cases.

### Set a review rhythm around decisions

An active team might use a short weekly review, a monthly failure-category investigation, and a quarterly comparison with current production. The original 15-minute/one-hour/two-hour meetings and sample sizes are examples, not standing obligations.

Review what changed, whether comparisons are fair, important failure patterns, decisions, owners, and unresolved questions. A move from 79% to 84% after adding cases mixes product and dataset effects unless the same cases are compared. New cases should have their own cohort or a reconciled comparison.

Automate relevant checks on material prompt, model, tool, or workflow changes. Choose fast checks for iteration and broader checks for release according to risk and cost. “Every commit” need not mean an expensive full suite for unrelated edits. The useful measure is timely, trusted feedback before the decision it informs—not a daily-run quota.

## 5. Keep release dimensions separate

Use distinct criteria so a task-score gain cannot conceal a violation of a required constraint:

| Dimension | Decision rule |
|---|---|
| **Safety/policy** | Enforce defined non-negotiable constraints and approved risk floors. A confirmed breach of a blocking requirement prevents release. |
| **Task success** | Meet the stated bar and justified regression tolerance on relevant cases and populations. |
| **Honesty/calibration** | Keep unsupported claims, citation failures, and confidence behavior within the defined limits. |
| **Cost/latency** | Meet the relevant budgets and service requirements, including tails, retries, and review where material. |

Helpful/Harmless/Honest (**HHH**) is a useful organizing lens: accuracy, completeness, and relevance; safety, policy, and bias; and evidence, uncertainty, and unsupported claims. Define concrete criteria beneath it. These categories can overlap and do not exhaust every product requirement.

Define gates before evaluating a candidate, with sample size, uncertainty, severity, owner, and escalation for inconclusive results. An ordinary noisy score decrease is not automatically a confirmed safety failure. Conversely, higher task performance cannot buy an exception to a mandatory legal or authorization constraint. Risk-tolerance changes require their accountable decision process, not a hidden weighted-average trade.

Align per-change criteria with `ship-decision`'s launch criteria. Evaluation provides evidence about controls; it does not by itself enforce permissions or prove that all possible future actions are safe. Emergency containment or an urgent repair may require a documented proportionate path while broader checks continue.

## 6. Reconfirm the business case and data lineage

### Stage reviews and paired adoption/performance measures

The Schneider Electric case offers four stages: **vision, ideation, incubation, deployment at scale**, with the business plan and business case reconsidered at transitions. Use such reviews when they help govern investment; do not impose four meetings on every small change.

For an internal use case, pair an adoption measure with an outcome/performance measure, co-developed with the business owner. Usage without benefit can mislead, as can strong task performance with no practical uptake. Neither measure becomes meaningless alone; interpret them together and add risk/cost measures as needed. Central AI teams can legitimately co-own metrics and decisions.

Match evaluation to the task rather than the label “analytical” or “generative.” Classification and forecasting may have delayed or noisy labels; code generation or structured extraction may have exact tests. Many systems need both objective tests and human judgment. The source's reported analytical/generative portfolio percentages have different denominators and are not a universal allocation rule; see [evidence and review notes](references/evidence-and-review-notes.md).

### Check upstream transformations

Record the **source of record** and material transformations when derived content informs a consequential decision. An interview transcript, trace, or filing is provenance evidence, not necessarily infallible ground truth. A summary can faithfully summarize an input whose earlier transformation already omitted a crucial fact.

Inspect links back to source evidence, what each transformation retained or removed, and end-to-end outcomes. Count AI-mediated passes when useful, but do not make chain length a universal quality measure. Retrieval from the original source can reduce drift yet still retrieve the wrong passage or omit context. Re-anchored passes are not automatically “clean.” Unknown lineage is an evidence gap; it does not prove the content was degraded. Apply retention and access limits rather than preserving every raw item indiscriminately.

## 7. Diagnose a stalled loop and the actual constraint

Use four diagnostic questions:

1. **Predictiveness:** Does the evaluation capture the task outcomes and failures that matter? Compare compatible case-level or cohort measures. An 85% eval score and 50% satisfaction need not be on the same scale. Correlation with retention can be informative, but sparse quarterly aggregates or a universal Pearson threshold cannot validate a suite.
2. **Error understanding:** Can the team describe important patterns, evidence, and competing explanations? Reading logs is part of good analysis; lack of an immediate root-cause story is not itself incompetence.
3. **Coverage:** Sample real production issues and ask whether the current tests would detect them. Distinguish already-known issues from new categories, and account for reporting bias and silent failures. A small support-ticket sample is not the full population.
4. **Feedback speed:** Do results arrive in time for the development or release decision? Investigate bottlenecks in execution, labeling, interpretation, or ownership rather than requiring daily full runs everywhere.

When scores improve but users do not benefit, test multiple explanations: narrow optimization, insensitive user metrics, altered cohorts, limited exposure, workflow friction, distribution, pricing, trust, or missing data. Better quality can affect willingness to pay or trust; explaining an answer does not automatically solve either. Tools/RAG may help missing context, but require access, retrieval quality, and end-to-end validation.

Ask, “If model output were much better, what important problem would remain?” Use the answer to direct effort. Continue suitable regression protection even if discovery or workflow repair becomes the immediate priority.

Recover according to the failure:

- **Eval debt:** restore ownership and the most important coverage; restrict unsupported releases as needed. A blanket freeze on all work can obstruct the repair.
- **Metric gaming:** inspect held-out behavior, leakage, rubric changes, and real outcomes. Similar examples in a prompt can be legitimate development data; they contaminate a holdout only when the evaluation claim treats them as unseen.
- **New production failures:** reproduce and classify them, add appropriate coverage, and check whether environment or monitoring also failed.
- **Evaluation bottleneck:** begin with a maintainable small loop, then strengthen it for the decision's risk. Ten binary cases can support exploration, not automatically authorize a consequential launch.
- **Plateau:** decide whether the task is sufficiently supported, the instrument has saturated, the model is limited, or another product constraint matters. A plateau alone does not identify the cause.

## Deliverable and readiness check

Deliver a concise intent statement, versioned evaluation plan, baseline and current evidence, top failure hypotheses, next priorities, release criteria, and ownership/maintenance plan. Include what remains unknown and the next decision. Use the shared Universal Skill Protocol's relevant trade-off and handoff fields; choose the user's requested format and add a diagram only when it clarifies the loop.

Before relying on the suite, verify that its tasks are valid, graders detect the intended failures, comparisons are fair, important cases have sufficient coverage, and checks can be maintained. Repeat runs when needed to characterize variability. An old model is not necessarily worse on every dimension, and two runs alone do not prove reproducibility. Record which constraints block release, which results are inconclusive, and which improvements are optional.

Route the detailed harness to `eval-framework`, judge validation to `confidence-tuner`, requirements to `ai-prd`, launch evidence to `ship-decision`, operational feedback to `production-observability` and `feedback-flywheel`, and permission/containment design to `safety-by-design`, `agent-risk`, and `tool-architecture`. `ai-product-metrics` connects these measurements to product decisions; it should retain their population, version, and evidence limits.
