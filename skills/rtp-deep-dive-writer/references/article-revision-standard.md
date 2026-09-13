# Article revision research and editorial standard

Owner: Raviteja Palanki. Revision 1.0.1, 13 Sep 2026. Created 29 Aug 2026. Applies to AI Evals, AI PM OS, Agentic Systems, Harness Engineering, and future practitioner series.

Improve the reader's understanding, the accuracy of a claim, the central argument, a practical decision, the article's usefulness, or its connection to the series. Freshness alone is insufficient. A small factual correction or structural repair is a valid revision; it need not become a new research essay.

Read the complete article before a full revision. Preserve the useful functions of its examples, definitions, frameworks, and exercises. The main Deep Dive Writer skill governs voice and the default template; this reference governs evidence and revision quality. Use the active project's publishing requirements when its structure differs from an older template.

## 1. Establish what the revision needs

Keep a short working assessment:

| Field | Record |
|---|---|
| Article identity and reader | Actual title, file, intended audience, and requested scope |
| Decision or lesson | What the reader should understand or do |
| Current thesis | The argument in a few sentences |
| Existing strengths | Material worth preserving, including exact wording when it works |
| Weaknesses | Confusing, incomplete, repetitive, overstated, or outdated material |
| Evidence needs | Important claims, numbers, dates, and versions requiring verification |
| Teaching gaps | Missing mechanism, definition, example, action, or artifact input |
| Series relationship | Related articles and the natural home of overlapping ideas |

Understand the article before searching for news about its title. For a narrow edit, read the affected context and report that scope; do not claim a full article review.

## 2. Research according to what can change

Use recent information when it corrects a belief, affects a decision, reveals a failure mechanism, changes an applicable rule or product cost, or strengthens the evidence. A launch, funding round, ranking, forecast, or new framework needs a clear purpose in the article.

Useful search windows are the last 14 days for fast-changing incidents or prices, the last 60 days for recent research and practice, and the last 12 months for whether a signal persists. These are starting points, not mandatory searches for every edit. Keep older foundational sources when they remain the best support.

Follow discovery material to the underlying evidence: secondary account, original source, method, limitations, counterevidence, and interpretation. Prefer the paper over its summary, the benchmark repository over a screenshot, the regulator over a compliance vendor, the incident report over a dramatic retelling, and official pricing or specifications over comparison articles.

Social posts and newsletters can themselves be primary statements or firsthand accounts. Identify what they establish and verify supporting evidence; neither their format nor a prestigious publisher makes a claim reliable. A review paper may summarize original studies rather than independently replicate them. An official source can still be self-reported, incomplete, or interested in the outcome.

For important claims, actively look for corrections, retractions or withdrawals, delays, replication, criticism, contamination, methodological limits, exceptions, and updated official guidance as relevant. Check whether the date is publication, measurement, announcement, or deployment. Compare equivalent conditions and investigate whether the metric measures the value claimed. Test the claim rather than manufacture balance.

## 3. Keep an evidence ledger

For substantive research, record candidate signals before incorporating them:

| Field | What to retain |
|---|---|
| Signal and dates | What changed, when it happened, and when it was reported |
| Source and reading scope | Exact source, link or location, author, and what was actually read |
| Evidence type | Original study or documentation, case, practitioner proposal, secondary report, or author synthesis |
| Method and scope | Population, systems, sample or runs, comparison, and measurement process |
| Result and conditions | Units, denominator, period, uncertainty, and assumptions |
| Status | Measured, estimated, projected, self-reported, independently checked, disputed, or unresolved |
| Limits and challenges | Transfer limits, alternative explanations, corrections, and counterevidence |
| Article fit | Where the idea belongs and what it improves |
| Confidence and decay | Reason for confidence and how quickly the claim may become stale |

Not every field applies to every number. A price has a unit and effective date, not a research sample. Where material detail is missing, narrow the claim, attribute it as a limited report, or omit it. Calling a precise unsupported number "directional" does not repair it.

Classify evidence by what it supports:

- **Inspected primary source:** The original study, specification, report, or statement was read. Its methods and scope still determine the strength of the claim.
- **Documented case:** A dated example in a defined setting. It can illustrate a mechanism without establishing a general effect.
- **Practitioner pattern:** An operating idea worth testing, with the contributor's context and interests visible where relevant.
- **Author synthesis:** A connection or recommendation developed from evidence and reasoning. State its assumptions and distinguish it from a measured finding.
- **Secondary report:** An attributed account whose underlying evidence may not have been inspected. Preserve that limitation.

Exclude an unsupported conclusion, a claim contradicted by stronger evidence, or material that distracts from the article. A narrow or vendor-reported result can remain useful if its scope is explicit; it is not automatically unusable.

## 4. Decide what enters the article

Use eight checks:

| Check | Question |
|---|---|
| Truth | Does the inspected evidence support the precise claim? |
| Transfer | Are applicability and limits clear? |
| Relevance | Does this improve the article's argument, understanding, or decision? |
| Novelty | Does it add something useful beyond what the article already says? |
| Decision value | For guidance, what choice or action does it inform? For a correction, what misunderstanding does it remove? |
| Clarity | Can the intended reader follow it in ordinary language? |
| Durability | Is the insight lasting, or does a dated fact need an explicit update condition? |
| Placement | Is there a natural location without overwhelming the original teaching? |

A true claim may still be unnecessary. A temporary price or regulation can be essential to a current decision when clearly dated. Useful clarification does not need a novel thesis.

For new practitioner guidance, work through **evidence → mechanism → decision → action → limitation**. Explain the mechanism when known and identify interpretation when it is uncertain. A case shows what happened there; it does not establish a universal threshold. A benchmark exploit shows a vulnerability under particular conditions, not that all benchmarks are useless. An expensive evaluation does not define everyone's budget. A simulation does not alone establish real-world safety. A seat-plus-credit offer does not prove seats have disappeared, and one outcome-priced support product does not establish suitability for every workflow.

## 5. Write and place the revision

For a substantial research proposal or review, use this working block. For a direct edit, keep only the fields needed to make the change traceable; the article itself should read as finished prose.

```text
Article ID and title:
Decision or lesson:
Current weakness:
New evidence or correction:
Evidence type and strength:
Why this improves the article:
Exact insertion or replacement location:
Publication-ready wording:
Practical action, where relevant:
What this does not prove:
Related article and reason for linking:
```

Write from the reader's problem. For example, "When should we price the result?" gives an outcome-pricing article a decision. "Which model may handle this step, and what happens if it fails?" makes model orchestration concrete. "Which failures should become permanent regression tests?" gives a golden-dataset article a practical purpose. A definition-led tutorial is also appropriate when the user's need is understanding the concept.

Explain before relying on terminology. Introduce the problem, a plain explanation, an example, and the decision affected; name the technical term when it helps. For example: "Score the step that helps explain the failure, and keep that score connected to the complete task. This is often called span-level scoring."

Use concrete actors and verbs such as choose, test, record, compare, stop, approve, escalate, complete, or pay. Replace inflated words with the specific behavior they hide. "Robust" needs named failure conditions when reliability is the claim; "agentic" does not explain what the system can do.

Make recommendations testable where possible: "Shorten the required chain and test whether end-to-end completion improves" is more useful than an unspecified promise of reliability. Explanations need not all be formal hypotheses. Preserve warranted uncertainty and distinguish finding, interpretation, recommendation, and limitation without repeating four rigid labels in every paragraph.

For a practitioner article, a useful sequence is decision, common mistake, mechanism, example, decision criteria, action, limitation, and reusable artifact. Fit this sequence into the series template rather than adding a second competing article structure.

## 6. Keep the series coherent

Give each important idea a primary home. Other articles can explain enough to stand alone, apply the idea, and link for depth. Avoid duplicated full definitions and disconnected link lists. Functional navigation is useful; a substantive cross-link should also explain the relationship.

Maintain an insight-to-article map where the series needs it. Typical connections include failure classification to debugging and root cause; a golden dataset to an eval suite and production learning; a rubric to judge validation and judge design; a product job to cost, pricing, and ROI; or architecture to authority and trust boundaries.

Use shared terms consistently, with room for domain-specific qualifications:

| Term | Working meaning |
|---|---|
| Job | Work the user or business wants completed |
| Completed job | A result verified against the task's completion criteria |
| Task definition | Success, acceptable variation, prohibited actions, and escalation |
| Context | Information available to the system for its current decision |
| Test case | An input and situation used to check behavior |
| Golden dataset | A reviewed, versioned collection of important evaluation cases |
| Evaluator | A rule, program, AI judge, human, or combination used to score behavior |
| Trace | A linked record of steps leading to an outcome |
| Harness | The system around a model, including context, tools, memory, permissions, retries, and checks |
| Meter | The unit used for billing |
| Exception rate | The share of defined cases requiring additional handling; specify what counts |
| Trust boundary | The boundary between actors or resources with different permissions and trust assumptions; name independent, approved, and prohibited actions |
| Proof for a decision | Evidence sufficient for the specified decision under stated uncertainty, not universal certainty |

Check terminology, examples, arithmetic, cross-links, and the order of learning after edits. If stronger evidence corrects a canonical claim, update its primary home and connected uses instead of preserving a contradiction for consistency.

## 7. Preserve the AI Evals lessons

**Evaluate the complete system.** Results depend on model, instructions, context, retrieval, tools, permissions, environment, human interaction, evaluator, and test runner. Investigate the failure before assigning it to the model.

**Validate the evaluator for its decision.** Judges and humans can disagree or drift. Check criteria, examples, answer order, formatting, length sensitivity, missing evidence, model changes, and repeated-run variation where relevant. Approval for one task does not imply fitness for all future tasks.

**Govern the evaluation cases.** Record origins, coverage of journeys and risk, reviewed expected behavior, versions, near-duplicates, and exposure to prompts or training. Add production failures through review. No universal case count establishes quality, and tuning against the final holdout undermines what it can independently show.

**Close the production loop.** Observe behavior, review the failure, locate the first meaningful deviation, test plausible causes, add representative regression cases, make a release decision, and verify production results. A passing test does not establish that the live outcome improved.

**State the limit.** A major eval result needs the cases, system version, environment, scoring process, and uncertainty required to interpret it. Explain which capabilities, populations, or safety claims were not tested.

## 8. Preserve the AI PM OS lessons

**Own the job.** Measure useful work and acceptable user effort. Generated messages, tokens, sessions, or drafts can be diagnostic activity measures; by themselves they do not establish value. Useful outcome measures include completed and durably resolved jobs, takeovers, serious failures, effort, and cost per successful job.

**Own the context.** Before assuming a stronger model is needed, check missing, stale, irrelevant, conflicting, or mis-scoped information; lost state; and important content removed during summarization. Context can be causal without being the cause of most failures everywhere.

**Own the authority.** Specify identity, accessible data, tools, permitted changes, approval requirements, prohibited actions, and retained evidence. The implementation must enforce the permissions; a written boundary alone is insufficient.

**Own the economics.** Define the successful outcome and account for model calls, context, retrieval, tools, retries, failed attempts, evaluation, monitoring, review, exceptions, and incident costs. Match costs and outcomes to the same population and period. With no successful jobs, cost per successful job is undefined.

An illustrative per-attempt model is:

```text
Expected cost per attempt
  = automated cost
  + exception rate × incremental human cost per exception
  + expected incremental error and incident cost
```

Avoid double counting costs already included elsewhere. Convert aggregate cost to cost per successful job using the verified success count. Model human capacity and delay as well as average cost: the remaining exceptions may be unusually difficult.

**Own the proof.** Look for task evidence, user evidence, cost evidence, and control evidence. Important cases must meet their criteria; users must complete the job with acceptable effort; costs must fit the proposed economics; forbidden actions and intervention must be tested. Scale the evidence burden with harm, reversibility, and uncertainty.

## 9. Review before delivery

Check the areas relevant to the revision:

- **Research:** Complete reading within the stated scope; primary evidence and counterevidence; current dates and versions; method behind important numbers; source interests and transfer limits.
- **Editorial judgment:** A clear improvement to the article; no distracting novelty, unnecessary duplication, or unjustified generalization; corrected or replaced weaker claims.
- **Writing:** A useful opening, understandable mechanism, sufficient example, explained terms, direct sentences, and natural rhythm for the intended reader.
- **Practice:** A decision or lesson, appropriate action, usable artifact and inputs, necessary owner, and evidence limits.
- **Series:** Consistent terminology, coherent progression, accurate cross-references, and supported publishing metadata.

For a substantial revision, rate truth, usefulness, clarity, distinctiveness, and durability from 1 to 10 with a brief reason. Treat 1–4 as serious defects, 5–6 as a useful idea with major gaps, 7–8 as strong with identifiable repairs, and 9 as accurate, clear, distinctive, and practical. A 10 also integrates naturally and leaves a memorable mechanism or useful artifact. These are editorial judgments; a high average cannot cancel a factual error. Do not award a full-revision score without reading the complete original.

The ending should answer, through suitable prose or the artifact: Which decision does this inform? What evidence could change it? What remains unproven? What should the reader do next? Which assumption matters first? Do not append five repetitive questions when the article already answers them clearly.

Record material changes, completed checks, and unresolved limitations. The result should be accurate, understandable, connected to its series, and useful in the reader's work.
