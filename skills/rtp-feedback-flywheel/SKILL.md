---
name: feedback-flywheel
version: v1.4.1_latest
description: 'Turn user feedback into verified product improvements through a clear path from capture to review, evaluation, experiment, and release. Use when designing a feedback loop, finding why collected feedback changes nothing, or preparing a loop before launch. Include corrections, exceptional successes, and unexpected uses. Distinguish behavior from a reliable label, speed from improvement, and useful learning from a defensible moat. Scale the process to volume, consequence, and available data rights; a manual loop can be appropriate. Pairs with eval-framework and eval-driven-development for testing, ai-product-metrics for measurement, moat-finder for defensibility, and gossip-mode for informal signals. Triggers: feedback loop, data flywheel, user corrections, annotation bottleneck.'
imports: [first-principles, stress-test]
---

# Feedback Flywheel

Turn a useful signal into a product change whose effect you can assess. The loop closes when someone can trace what was learned, what changed, and whether the change helped. A growing feedback database alone does not establish progress.

## Start with the decision and the boundaries

Establish the output, the user’s task, the decisions this feedback will inform, existing telemetry, and who can act on the findings. Reuse available context; ask only for missing information that changes the design. Follow the Universal Skill Protocol at the source library root or the packaged plugin root, scaling its depth and format to the request.

Before designing collection or automatic updates, settle four things:

1. **Useful outcome.** Name the user or business result to improve and the harms or regressions to avoid. Acceptance, engagement, and fewer escalations are signals, not automatic proof of quality.
2. **Permitted use.** Check collection, access, retention, reuse, and vendor-sharing rights for this data and purpose. Permission to process a request does not necessarily permit training on it. Minimize sensitive content; de-identification and a notice alone do not establish adequate protection or authorization. Carry applicable consent and opt-out choices through the pipeline.
3. **Update authority.** Separate permission to log, label, propose, test, and release. A captured correction must not silently change a production model, shared memory, policy, or retrieval corpus.
4. **Human usefulness.** If feedback reaches people, provide enough task context and a way to investigate or respond. A score may summarize a problem; pair it with the evidence and an actionable next step when needed. Increasing frequency without increasing usefulness can add burden.

Use this skill for low-volume, batch, and prelaunch products too when there is a meaningful learning opportunity. They may need periodic review rather than continuous telemetry. If reuse is prohibited or no credible improvement path exists, explain that limit and choose an allowed alternative, such as aggregate measurement or a workflow change.

## 1. Capture three kinds of learning

Design capture around a question you can act on, with an owner and proportionate retention. Avoid collecting everything merely because it is possible.

| Channel | What to examine | What it does not prove |
|---|---|---|
| **Corrections and failures** | Edits, rejections, regenerations, abandoned tasks, complaints, and human escalations | Every edit is a factual correction; every abandonment is a product failure; every escalation was unnecessary |
| **Exceptional success** | Specific moments, workflows, and conditions that devoted users find unusually valuable | High engagement means satisfaction, or a power-user preference should become everyone’s default |
| **Repurposing** | Users succeeding at an intent or workflow the product did not anticipate | Every outlier is a new market, or intuition should override contrary evidence |

Capture implicit signals where they are informative and permitted: edit direction and extent, regeneration sequences, time before reuse, and escalation context. Offer lightweight explicit feedback—such as a rating with optional tone, accuracy, completeness, or relevance categories—when it helps interpretation. There is no universal requirement that 80% of signals be implicit.

An expert-validated correction often conveys more than a bare rating. Its value still depends on competence, task, and context. A full rewrite may change style rather than fix errors; no edit may mean satisfaction, uncritical acceptance, or abandonment elsewhere. A human resolution becomes a reference only after checking its quality. Do not assign fixed reliability percentages to these behaviors.

Preserve enough provenance to reconstruct the task and system version, understand the signal, and honor data restrictions. Collect identifying information only when the purpose requires it. Keep the original observation distinct from an inferred explanation and from an approved reference answer.

### Find unexpected uses

Deliberately sample permitted outlier sessions for intent, alongside routine cases. Ask what the person was trying to accomplish, what helped, and whether the pattern recurs. Do not discard an unfamiliar success as noise just because it falls outside the intended workflow.

Distinguish evidence against a proposal from an instrument that never tested it. Existing telemetry may say little about an unavailable experience; prototypes, interviews, and experiments can generate evidence about it. A weak instrument is a reason to improve the test, not to ignore an inconvenient result. Historical success stories suggest possibilities, not the base rate of successful pivots. See [research boundaries](references/evidence-and-examples.md) for the corrected Walkman example.

### Learn why something is loved

Interview a purposive sample of exceptionally satisfied or engaged users and identify the mechanism behind their experience. Keep satisfaction and engagement as separate selection criteria. Compare with ordinary, dissatisfied, and absent users where the decision requires it. The output is a design hypothesis, not just a testimonial.

Preserve the rating distribution so unusually positive responses remain visible. Inspect top-box and adjacent ratings separately when testing whether their outcomes differ. Do not assume a universal cliff between 4 and 5, ban all aggregation, or substitute a five-point satisfaction scale for NPS.

Buckingham’s five conditions provide optional interview prompts:

| Condition | Question to investigate | Possible design response |
|---|---|---|
| **Control** | Do people understand what this is and how to engage? | Orientation and meaningful choices |
| **Harmony** | Does the experience fit their emotional situation? | Appropriate pacing, tone, and demands |
| **Significance** | Does the experience recognize their particular context? | Relevant personalization without intrusive assumptions |
| **Warmth** | Is useful support visible and reachable? | A credible route to help |
| **Growth** | Does the experience leave them more capable? | Learning, practice, or greater ability to act |

Treat these as a framework to test, not a validated prerequisite sequence. Growth does not universally require all four other conditions. A quarterly interview cycle is one option; choose timing around the decision. Feed promising findings into the same review and testing process as corrections.

## 2. Make signals usable

**Annotation** means adding the interpretation needed for a particular decision. It need not produce training data. Label an issue’s type, severity, context, and supporting evidence; preserve disagreement and uncertainty when a single answer would conceal them.

Use tiers to describe how a label was produced:

- **Gold:** checked by qualified reviewers against a stated standard. Audit disagreement and reference quality; the name does not guarantee correctness.
- **Silver:** an automated or model-based judgment validated against suitable human references. Check performance by relevant category and after material changes.
- **Bronze:** a behavioral or rule-based proxy. Use it for triage or sampling until its relationship to the intended outcome is established.

A model’s stated confidence, a high edit distance, or “deleted everything” is not sufficient approval for unattended learning. Decide which labels require review from their demonstrated reliability and the consequence of misuse.

Find the actual bottleneck: access, deduplication, interpretation, expert availability, evaluation, engineering, release, or outcome measurement. Track eligible demand, useful throughput, unresolved high-priority items, and age at each stage. A growing queue does not by itself prove annotation is the problem. Nor should every collected event be labeled: duplicates, irrelevant events, and intentionally sampled traffic can make a low processing percentage sensible.

### Before real users exist

Start with representative tasks, domain examples, and reviewed synthetic cases. Have qualified people assess or correct outputs using explicit criteria. Keep synthetic provenance visible and test later against actual usage. Simulated accept/reject events can exercise instrumentation; they cannot establish what users value or supply ground truth merely because the simulation labels them “pass” and “fail.”

Choose sample sizes for the decisions and uncertainty involved. A small product can learn from a few consequential failures; a precise rate estimate or experiment may require many more observations. There is no 500-user eligibility threshold for this skill.

## 3. Close the loop with owners

Document a path for each priority finding:

```text
Permitted observation → interpretation and validation → prioritized finding
→ reproducible evaluation case → candidate change → regression and impact checks
→ authorized release or rejection → outcome review → next learning
```

Changes may improve prompts, retrieval, tools, rules, interface, documentation, or the model itself. Do not count only model training as closure. Record a reasoned decision not to change the product separately from a verified improvement.

| Stage | Responsibility | Completion evidence |
|---|---|---|
| Review | Feedback owner | Validated pattern, severity, affected users, and uncertainty |
| Evaluate | Evaluation owner | Reproducible case, intended outcome, and suitable comparison |
| Experiment | Product and engineering owners | Candidate change and a credible measurement plan |
| Release | Authorized release owner | Required checks pass; monitoring and recovery are ready |
| Follow through | Outcome owner | Effect assessed, limits recorded, and next action chosen |

One person can own several stages. Assign actual people or roles; avoid a nominal owner without time or authority. Weekly pattern review, monthly evaluation maintenance, quarterly experiments, and continuous automated triage form one possible cadence. An urgent safety failure should not wait for the next quarter; a slow-moving, sparse domain need not manufacture weekly changes.

Protect each transition:

- **Deduplicate and validate.** Separate repeated symptoms from independent corroboration. Check malicious or mistaken corrections, conflicting preferences, and changed context before promoting an example into shared knowledge.
- **Learn from the boundary.** An expert’s explanation of an unusual case can reveal a useful rule. Record its scope and provenance, then test it on other cases. One explanation may be incomplete or a post-hoc rationalization. Sample ordinary and apparently successful cases too; an escalation queue misses failures the system never detected.
- **Prevent evaluation leakage.** Use reviewed production failures for development and regression tests while preserving independent, representative evaluation. A case used to design or tune a change is no longer an untouched test of generalization. Add appropriate adversarial and shifted-distribution cases.
- **Test before claiming gain.** Reproduce the failure before the fix, apply the change, then retain a regression test. Verify the main outcome and relevant quality, safety, cost, and latency effects.
- **Measure impact credibly.** Use a randomized experiment when feasible and suitable. Otherwise state the comparison design, confounders, sample limits, and what causal claim it supports. An offline score increase is not automatically a user benefit.

## 4. Measure closure and choose useful automation

Keep a small set of measures tied to the decision:

- Time from an actionable signal to triage, a tested change, and observed outcome; report the distribution and severe cases, not only an average.
- Validated findings used in evaluation or experiments, with denominators defined. Distinguish raw events, unique issues, eligible examples, and released changes.
- Backlog age and throughput at the limiting stage, including reviewer effort and cost.
- The change in the intended outcome, relevant regressions, affected segments, and uncertainty.
- Coverage gaps: non-users, silent failures, positive experiences, unusual uses, and effects that appear later.

Visible short-term events can dominate the loop. For example, a caveat may reduce immediate completion while preventing a later misunderstanding that is never logged. Treat this asymmetry as a hypothesis to investigate; measure both relevant costs and benefits instead of treating an unobserved benefit as zero.

Use the five maturity labels descriptively:

| Level | What exists | Useful next improvement |
|---|---|---|
| **L1 — Collection** | Signals are retained but rarely lead to a decision | Give a valuable class of signals an owner and review path |
| **L2 — Manual learning** | People review, test, and act periodically | Make the process repeatable and track outcomes |
| **L3 — Assisted learning** | Automated triage or judging supports reviewed changes | Validate assistance and remove the actual bottleneck |
| **L4 — Integrated learning** | Evaluation, experiments, and releases connect reliably | Improve coverage, speed, and recovery where worthwhile |
| **L5 — Bounded automatic adaptation** | Some updates run within explicit authority and verified controls | Monitor degradation, containment, and whether automation still earns its cost |

L2 or L3 can be the right end state. L5 does not require unrestricted online learning, and a level does not establish safety or defensibility. Reference-set sizes, staffing, processing percentages, and cycle times depend on the workload. See [examples and calculations](references/evidence-and-examples.md) for the original illustrative values and their limits.

## 5. Test the advantage separately

A useful learning loop may improve the product without creating a moat. Ask what rivals could reproduce and what remains distinctive: data access and reuse rights, hard-won domain knowledge, coverage, validated execution, workflow integration, or the speed and economics of learning.

Exclusive inputs can help but are neither sufficient nor the only possible source of advantage. Public signals can produce useful gains; common-case fixes can matter greatly. Rare cases deserve attention when their consequence or information value warrants it. Test whether a new model, substitute workflow, or competitor can erase the advantage rather than assuming it will—or cannot.

Balance loop investment against buying better baseline capability. Include collection, labeling, evaluation, infrastructure, user burden, and ongoing maintenance. Infrastructure may be reversible; retained data, learned dependencies, and released changes can carry lasting costs. Use `rtp-moat-finder` for the fuller defensibility decision.

## Deliver and check the result

Lead with the current state, the limiting link, and the next useful action. Include the owner, permitted signal sources, interpretation standard, testing path, cadence, success measure, and main trade-off. A diagram is helpful when several teams need to see the path; use the available visual skill and highlight the actual bottleneck. A short diagnostic answer need not produce a separate artifact.

Before finishing, check that the proposal:

- separates observations, labels, experiments, and demonstrated improvements;
- includes failure, success, and unexpected-use channels where relevant;
- respects data rights and update authority at every stage;
- has realistic capacity and human feedback people can use;
- preserves independent evaluation and checks relevant regressions;
- avoids treating fixed percentages, rapid cycles, rising trust, or exclusive data as proof of success.

Connect to `rtp-eval-framework` and `rtp-eval-driven-development` for testing; `rtp-ai-product-metrics` for measures; `rtp-attitudinal-segmentation` for cohort interpretation; and `rtp-fit-signal` for downstream product-fit evidence. A rising or flat trust curve has several possible causes: trace the loop rather than diagnosing it from that curve alone. `rtp-gossip-mode` handles informal signals; `rtp-first-principles` clarifies what improvement means; `rtp-stress-test` checks capacity, cost, failure, and recovery.
