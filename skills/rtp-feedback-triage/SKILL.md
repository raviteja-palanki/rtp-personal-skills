---
name: feedback-triage
version: v1.0.1_latest
description: 'Turn tickets, comments, and complaints into a prioritized report with evidence, accountable owners, and next actions. Classify themes across six categories, assess frequency, severity, and strategic fit, and identify possible AI failures without confusing a report with a confirmed cause. Surface rare serious harm before scoring routine work. Use for support feedback, NPS comments, in-product responses, or sprint triage; simplify for a small batch or a single issue. Keep feedback share separate from production failure rate. Pairs with failure-modes for diagnosis, eval-framework for regression coverage, ai-product-metrics for denominators, interview-synthesis for depth, and opportunity-solution-tree for unmet needs. Triggers: triage feedback, rank these tickets, what should we fix first.'
imports:
  - failure-modes
  - ai-product-metrics
  - eval-framework
---

# Feedback Triage

Produce a ranked, routed account of what users experienced and what should happen next. Keep serious failures visible even when most feedback is positive. Average sentiment can hide a harmful minority; AI feedback need not be bimodal for this to matter.

## Establish scope and handle urgent issues first

Identify the product and version, feedback period, channels, affected populations, and decision the report supports. Reuse known context. Follow the Universal Skill Protocol at the source library root or packaged plugin root, with depth and format appropriate to the request.

Before routine ranking, surface credible reports of consequential harm: unsafe action, material financial or factual error, privacy or security exposure, discrimination, or loss of a critical workflow. One report may justify immediate investigation or containment. Record what is known, who owns the response, and which decision remains open. A low frequency score or poor roadmap fit must not bury a serious issue.

Use the full method when clustering and routing will change priorities. For a clear single bug, document the evidence and route it directly. A small batch can reveal an important problem; it does not need an elaborate score. For non-AI feedback, omit the AI-specific dimension. An internal report can still describe a real user failure: distinguish first-hand observation from stakeholder preference instead of excluding it by job title.

## 1. Make the evidence traceable

Give each item an ID and retain its source, date, relevant context, and observed consequence. Use the minimum personal data needed for the task. Distinguish:

- **Observation:** what the person reported or what a trace shows.
- **Interpretation:** what that might mean.
- **Verification:** what has been reproduced or independently checked.

Quote exactly when presenting a quote; otherwise label the text as a paraphrase. Redact sensitive details transparently. Do not invent quotations, user intent, recurrence, or a root cause to make a theme complete.

Deduplicate repeated tickets about the same event while preserving evidence of reach. Count distinct items, incidents, users, and organizations separately when relevant. Repeated forwarding of one complaint is not independent corroboration. Explain missing channels and selection effects: people who complain are not a random sample of all users.

Cluster by the underlying task and reported problem, not just matching words. Keep contradictory or unmatched items visible. Use provisional themes where evidence is thin, and inspect examples before accepting automated clusters.

## 2. Classify for investigation

Assign a primary category for summary counts and optional secondary tags for overlap. Categories guide initial investigation; they do not prove which team caused or can solve the problem.

| Category | What it captures | Starting owner or collaboration |
|---|---|---|
| **UX issue** | Difficulty understanding, finding, controlling, or completing an interaction | Product/design with relevant engineering |
| **Performance** | Slow, failed, frozen, or unreliable operation | Engineering, then the component owner identified by diagnosis |
| **AI failure** | A reported or verified problem in an AI-supported output, decision, refusal, or action | Evaluation or AI-system owner with domain, product, and other specialists as needed |
| **Edge case** | A failure associated with a particular input, language, environment, or user group | Relevant component owner; assess reach and consequence before calling it minor |
| **Out-of-scope request** | A requested capability outside the current commitment | Product for an explicit scope decision |
| **Future-capability signal** | Evidence of an unmet job, repeated workaround, or alternative tool | Discovery or strategy for investigation |

An item may contain both a defect and an unmet need. Record both. “I dislike the new workflow” may reveal lost control or a broken user outcome; it is not automatically an out-of-scope request. Nor does mentioning AI make a complaint an AI failure.

Keep an **AI-failure indicator** separate from the primary category:

- **Yes:** evidence supports an AI-system failure; name the observed failure and verification state.
- **Possible:** the report suggests one, but expected behavior or cause is unresolved.
- **No:** current evidence points elsewhere, or the behavior is valid for the stated task.

Design, data, prompts, retrieval, model behavior, tools, and infrastructure can jointly contribute to a failure. A safer interaction can reduce harm while a model or grounding fix is developed. Conversely, changing a confidence label does not make an incorrect output correct. Assign one accountable investigation owner with named collaborators rather than forcing a false choice between design and AI teams.

## 3. Rank themes without hiding consequences

First apply the urgent-issue judgment above. For the remaining work, a transparent score can help compare themes. The following is an **illustrative additive rubric**, not a validated universal model:

| Dimension | Example scale |
|---|---|
| **Frequency, 0–5** | In a defined corpus: 0 = none observed; 1 = below 2%; 2 = 2% to below 5%; 3 = 5% to below 10%; 4 = 10% through 20%; 5 = above 20% |
| **Severity, 0–3** | 0 = cosmetic; 1 = minor disruption; 2 = material friction or rework; 3 = blocked critical task or potentially serious harm |
| **Strategic fit, 0–2** | 0 = outside current priorities; 1 = adjacent; 2 = directly supports the current commitment |
| **Confirmed AI-failure flag, 0–1** | 1 when the indicator is Yes; otherwise 0, with Possible explicitly retained |

Total = frequency + severity + fit + confirmed AI-failure flag, from 0 to 11. The AI flag’s main job is routing; one extra point does not make an AI issue inherently more important than an equally harmful non-AI issue. If the flag adds no useful prioritization value, show it separately and use the first three dimensions for ranking.

For small corpora, report counts instead of unstable percentages. One possible frequency scale is 0 for none, 1 for one, 2 for two, 3 for three or four, 4 for five through nine, and 5 for ten or more. Choose and record a scale before comparing themes. Do not mix counts and percentage bands in one ranking or imply scores are comparable across differently sized corpora.

Example action bands are 8–11 for near-term investigation or action, 5–7 for planned work or an experiment, 3–4 for a monitored backlog, and 0–2 for deferral. These do not override serious consequences, commitments, dependencies, effort, or available capacity. Set the actual urgency and due date explicitly rather than promising every high score a fix this sprint.

Rank within an owner’s queue to support execution and across categories to resolve shared resource choices. Show why a lower-scoring theme was elevated or a high-scoring one deferred. A score is a decision aid, not a substitute for judgment. Record customer reach or commercial commitments separately from how loudly someone complains.

## 4. Subtype possible AI failures and choose the next check

Use the following initial routes. They are not exhaustive, mutually exclusive, or promises about repair time. `rtp-failure-modes` owns the deeper diagnosis and response design.

| Subtype | Observed concern | Initial investigation |
|---|---|---|
| **Hallucination or unsupported output** | An invented fact, citation, or claim without adequate support | Check the expected answer, source, retrieval, prompt, and model output with the evaluation and grounding owners |
| **Over-confidence** | Certainty or a confidence display exceeds demonstrated reliability | Evaluation and product/UX examine calibration, presentation, and the underlying error |
| **Under-confidence** | Excessive hedging or avoidance despite adequate support | Check actual evidence and task policy before changing prompts or confidence behavior |
| **Wrong refusal** | An apparently legitimate request was declined | Safety/policy and system owners determine whether refusal, a careful answer, or escalation was appropriate |
| **Wrong tool or routing** | The wrong source, tool, agent, or action path was selected | Orchestration owner inspects the trajectory, permissions, tool descriptions, and ambiguous inputs |
| **Latency failure** | A response arrived too late for the task | Trace collection, queueing, retrieval, inference, tools, and delivery before choosing an infrastructure or model change |

Keep additional tags for missed detection, stale state, integration failure, or other causes instead of forcing every complaint into the six examples. “The alert arrived four hours late” does not establish slow inference. “Insufficient data” can be a correct refusal. A recommendation inconsistent with maintenance history may reflect missing or stale context rather than an invented fact.

Specify a next check, expected behavior, and completion evidence. A model change, streaming interface, smaller model, retrieval update, or threshold adjustment is a candidate remedy to test, not the automatic result of assigning a subtype.

## 5. Report the right denominator

Separate three quantities:

1. **Feedback share:** AI-failure reports divided by feedback items in the defined corpus.
2. **Incident or exposure rate:** verified failures divided by relevant tasks, outputs, users, or action opportunities, with the unit stated.
3. **Harm and burden:** consequence, affected groups, correction effort, and necessary versus missed escalation.

If production exposure is unavailable, report that limitation. A complaint share cannot establish the product’s failure rate. Show Yes and Possible separately, keep unknowns visible, and avoid double-counting overlapping categories. Compare periods only after checking product mix, channels, sampling, definitions, and exposure.

There is no general rule that more than 25% AI-related complaints makes a feature structurally unsafe, or that a lower share makes it acceptable. Escalate to `rtp-ship-decision` when severity, recurrence, failed controls, or uncertainty warrants reopening availability or autonomy. Triage supplies evidence; the accountable decision owner chooses continuation, containment, restricted use, or withdrawal.

## Worked example: predictive maintenance

Suppose 200 feedback items collected over six weeks have these primary categories: UX 64 (32%), performance 18 (9%), AI failure 71 (35.5%), edge case 22 (11%), out-of-scope 14 (7%), and future capability 11 (5.5%). This is a hypothetical complaint mix, not a measured 35.5% production failure rate.

| Theme | What to verify before assigning a remedy |
|---|---|
| Alert ranking conflicts with operator judgment | Whether the ranking, operator assumption, available context, or presentation is wrong |
| Alert arrives four hours after the operator noticed a problem | Event timestamps, sensor availability, detection logic, scheduling, and delivery |
| A healthy asset receives “high confidence: failure imminent” | Actual condition, prediction horizon, calibration, action taken, and harm |
| A Tier-2 asset is declined for insufficient data | Whether required data exists and whether the refusal policy is appropriate |
| A recently replaced part is recommended for replacement | Maintenance-history freshness, asset identity, retrieval, and legitimate repeat-failure possibilities |

If a validated serious false alert has example scores F=4, S=3, Fit=2, AI=1, its total is 10. A rare hazardous recommendation still receives urgent attention even with F=1 and Fit=0. Do not lower alert thresholds automatically: the direction and trade-off depend on which error the threshold controls.

UX themes such as plant filtering, mobile truncation, and snoozing enter the same consequence-based resource discussion. The 11 future-capability items might include seven requests to share alerts with reliability engineers and four requests for an action recommendation. These suggest collaboration and decision-support opportunities; “audit defensibility” remains a hypothesis to investigate with users.

The report should recommend the next verified actions and state whether evidence warrants a feature-availability review. It should not declare inevitable adoption collapse or assume a reassuring “draft” label contains the relevant risk.

## Deliver a report that can trigger work

Lead with the important findings and decisions. Include:

- scope, counts, denominators, and source limitations;
- prioritized themes with traceable examples, severity, uncertainty, and affected segments;
- one accountable owner, collaborators, next check or action, due date, and completion evidence for each priority;
- discovery opportunities, explicit deferrals with reasons and review triggers, and any availability decision to escalate.

Use attitudinal and task segments to investigate different experiences without presuming Skeptics always experience more harm or Embracers need fewer protections. An anonymous report can be useful; qualify what can be verified and protect the reporter as appropriate.

Before finishing, check that every item is accounted for, unresolved classifications remain visible, scores reproduce their stated formula, and quotes or paraphrases are labeled correctly. Confirm who can accept the work. If no owner has capacity or authority, surface that gap and propose a concrete resolution instead of merely producing another backlog.

Feed relevant failures into `rtp-eval-framework` and `rtp-eval-driven-development`: reproduce the failure before changing the system and retain regression coverage. Use `rtp-ai-product-metrics` for outcome and exposure measures, `rtp-interview-synthesis` for deeper understanding, and `rtp-opportunity-solution-tree` for unmet needs. `rtp-gossip-mode` covers informal single signals; `rtp-feedback-flywheel` follows the broader path from feedback to assessed improvement.

A compact routing diagram may help a complex report. Show observed categories, uncertainty, and shared ownership; draw a bimodal distribution only if the actual data supports it. Choose the output format for the user’s decision, not to satisfy an unnecessary artifact checklist.
