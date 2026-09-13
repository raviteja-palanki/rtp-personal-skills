# Communication formats and examples

Choose a format that fits the reader's task. The five types are reusable patterns, not a mandatory wrapper. Lengths are starting targets; urgency, complexity, and the user's request take precedence.

## 1. Executive summary

Use when leadership needs a decision, a material update, or both. State the recommendation or status, then situation, complication, response, evidence, and the specific ask if there is one. An initial target around 150 words can help focus; scrolling is not a test of quality.

For an AI claim, state the boundary and decision-relevant evidence in plain language, with a link to methods when available. Do not replace substance with “significant progress,” list every risk equally, or hide a measurement limitation in an appendix when it changes the recommendation.

## 2. Engineering brief

Use when the team needs to build, instrument, review, or decide. Include the user problem, current state, owners and credible dates, relevant eval matrix, effective configuration or prompt diff, regressions, interface implications, and open questions. Name stable contracts only when that prevents a real misunderstanding.

An initial 400–700 words may work for a substantial brief. Engineers also benefit from clear prose, customer context, and business priorities. Link detail rather than assuming dense or unpolished writing is desirable. Separate verified decisions from open architecture questions and targets from commitments.

## 3. Launch announcement

Begin with the relevant user situation, explain what is available, and state the limits and controls needed to use it well. Give a real feedback or assistance path. Verify the launch status, supported scope, claims, and permission to announce it.

Prepare internal enablement when sales, support, or customer success need different detail: evidence, permitted claims, likely questions, and escalation paths. External and internal copy can share language while differing in purpose. Neither audience should receive invented certainty, an unimplemented human fallback, or an automatic-learning promise.

## 4. Risk escalation

Lead with what happened, who or what is affected, and any containment or decision needed now. Separate known facts from hypotheses. Give options that are genuinely available, their costs and limits, a recommendation, and the decision or next-update time.

An initial 300–500 words is useful for a substantive escalation. Do not wait for a three-option table or a precise probability before surfacing urgent harm. When the responsible immediate step is clear, say so. If no remedy is yet supported, request investigation or decision authority rather than inventing one.

## 5. Weekly digest

Use a consistent structure so someone can re-enter after missing a few updates: material change and ask; shipped outcomes; work in progress; relevant quality state; priority risks with age, owner, and action; next focus. An initial target of about 400 words encourages editing.

Show risks that persist or change rather than quietly recycling them. Three risks is a useful focus limit only if it does not hide another material issue. Three weeks without movement is a prompt to review, not an automatic escalation deadline. Include participation and missing evidence where they change the picture. “No reported incidents” is different from “no incidents occurred.”

## Four illustrative cases

The cases below are fictional and their numbers are illustrative. They demonstrate faithful communication, not verified launches or completed tests. Replace assumptions and placeholders with actual evidence before use.

### Case 1: A predictive-maintenance rollout with a skeptical CFO

Assume the pilot has verified 284 true alerts out of 312 predicted alerts on held-out data, about 91% precision. This says nothing by itself about recall, unseen-pattern detection, or all plants. Assume the scoped fallback and cost scenarios below were tested.

> We recommend expanding the predictive-maintenance pilot to the next three plants, with a review before wider rollout. We need approval for that scope and its operating budget.
>
> In held-out pilot data, 284 of 312 predicted alerts matched verified faults. Recall and results by plant are in the evaluation record; these determine which workflows are eligible. Operators retain the existing inspection process, and the tested fallback remains available when an alert cannot support a decision.
>
> Cost was $0.12 per assisted decision in the pilot. The tenfold-volume scenario remains below $0.20 under its stated assumptions. Separately, operators used 78% of recommendations without edits; that is a reuse measure, not a trust or correctness score.
>
> New plants may differ from the pilot. The operations owner will monitor verified outcomes and review the agreed quality and capacity limits before each expansion.

This answers the CFO's prior experience through scope, evidence, and accountability. It does not claim a model can automatically recognize every unfamiliar failure or that acceptance below 60% must always trigger a fallback.

### Case 2: Recommendation acceptance falls before a board update

Assume acceptance fell from 78% to 64% over two weeks. Denominators, comparable cohorts, and the meaning of acceptance still need to be included in the actual evidence record. The $420,000 below is affected pipeline, not forecast lost revenue.

> Enterprise recommendation acceptance fell 14 percentage points over the last two weeks. Two customer champions have reported problems. We have paused expansion while we test the affected workflows; the board update is in nine days.
>
> The timing overlaps a catalog refresh that added sparse-data products. Retrieval is our leading hypothesis, with ranking and other interactions still under review. The prompt version is unchanged and P95 latency is stable, but those facts do not rule out all prompt or infrastructure causes. Verified quality and calibration results are still being checked.
>
> The feature touches $420,000 of Q2 renewal pipeline. We have not established how much revenue is at risk because of this change.
>
> | Option | Expected work | Potential benefit | Main limitation |
> |---|---|---|---|
> | Restore the prior compatible catalog configuration | About one engineering day plus customer coordination | May recover prior behavior | Removes recent coverage; restoration effect needs verification |
> | Test a retrieval patch before scoped release | About two engineering days | May preserve new coverage while improving results | Could underrepresent new products or fail to address the cause |
> | Keep affected scope restricted while investigating | Investigation and ongoing support | Avoids an unsupported production change | Delays benefit and leaves a degraded or limited experience |
>
> We recommend testing the patch first, with results reviewed before a release decision. If it fails the agreed quality checks, retain the restriction and assess restoration. The engineering owner will provide the next result by Tuesday afternoon; a Wednesday release is conditional on that evidence.

An unchanged prompt does not establish a ruled-out cause. “Recover 80% of the 14-point decline” would mean an 11.2-point gain to 75.2%, not necessarily 80% acceptance. If a catalog grew from 100 to 123 items, removing the added 23 removes about 18.7% of the new total. Avoid ambiguous percentage promises.

### Case 3: The weekly digest contains bad news

> Enterprise recommendation acceptance remains at 64%, down from 78% two weeks ago. A candidate retrieval patch is in testing; release timing depends on the results. The maintenance pilot has reached plant 4, and we need the next rollout decision by Friday.
>
> **Delivered:** Plant 4 onboarding and the vendor-risk alert integration are complete. Confirmed operating status and evidence links are in the release records.
>
> **In progress:** The recommendation patch has an engineering owner and a Tuesday review. Plant 5 expansion remains pending the operations decision.
>
> **Quality state:** Recommendation acceptance is below its agreed bar; root cause and verified quality impact remain under investigation. Plant 4's first-week reuse is 78%, with independent quality review reported separately. The vendor classifier's latest precision result is in its evaluation record; a dashboard coverage gap remains open.
>
> **Risks and asks:** Engineering owns the recommendation investigation. Operations must confirm expansion conditions. Sales and support need agreed wording for affected customers. The vendor monitoring gap has been open for 21 days and needs a named remediation date or a justified scope restriction.
>
> **Next focus:** Resolve the recommendation release decision and complete the plant-expansion review.

The digest separates shipped work, conditional plans, and missing evidence. It does not call a dashboard green while acknowledging that it cannot detect the relevant drift.

### Case 4: A summarizer is below its launch target

Suppose reviewers accepted 272 of 312 summaries, about 87%, against an 88% target. This is reviewer acceptance under a rubric, not necessarily factual accuracy. A one-point shortfall does not automatically mean ship or hold: assess uncertainty, severity, the role of the target, and the authority for any exception with `ship-decision`. Event timing does not resolve the gate.

If an appropriately limited beta is authorized and the described controls exist, customer copy could say:

> Review a draft summary alongside the source contract.
>
> The new beta helps you locate parties, dates, obligations, and issues that deserve a closer read in supported English-language contracts. It is a reading aid; use the source document to verify terms before relying on them.
>
> The current scope covers the contract types and length limits listed in the workspace. Complex multi-party agreements and unsupported documents need a separate review. Source links help you inspect each summary point, and the report option sends a problem to the review team.
>
> Beta access is available to the eligible group shown in the workspace. We will explain material scope or quality changes as the evaluation progresses.

The internal record carries the 272/312 result, target, exception rationale, and evidence limits. Add a public quantitative claim only when it helps the user and is accurately defined. Do not change “acceptance” to “accuracy,” promise every override trains the model, or invent a 92% graduation target.

## Optional preparation record

Keep these fields with the draft when they help review: audience; primary purpose; evidence date and effective configuration; material claim/source; boundary and response; actual availability; sensitivity or confidentiality; ask/owner/date; cross-audience reconciliation. The published message need not display this record or a “Communication Notes” footer.
