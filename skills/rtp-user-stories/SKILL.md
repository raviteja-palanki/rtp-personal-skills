---
name: rtp-user-stories
version: v1.0.1_latest
description: 'Turn product intent into verifiable backlog items for AI and non-AI work. Use when refining a backlog, breaking a PRD into stories, resolving repeated acceptance disagreements, or deciding whether unknowns need a spike. Choose a useful work type: user story, technical enabler, investigation, or ordinary task. Apply INVEST with judgment, examine five scenario classes, define observable acceptance and verification, size using the team’s conventions, and slice into useful increments. AI items trace applicable behavior, permissions, evidence policy, examples, failure ownership, monitoring, and cost implications to the current AI-PRD; resolve conflicts rather than copying outdated thresholds. Includes invoice-routing, webhook, OCR, and draft-assistant examples. Prefer lightweight cards and conversation to unnecessary ceremony, and distinguish implementation complete from approved user exposure. Pairs with ai-prd, determinism-compass, and eval-framework.'
imports:
  - ai-prd
  - determinism-compass
---

# User Stories

Make the intended outcome and the evidence of completion clear enough for the people building, reviewing, and owning the work to proceed. A story is a **shared understanding supported by conversation and confirmation**. It is not an immutable miniature contract that prevents learning during implementation.

Use this skill for backlog refinement, PRD breakdown, unclear acceptance criteria, and repeated review disagreements. For a small task, incident, or solo prototype, keep the useful outcome, constraints, and verification without forcing a story template. For unresolved discovery, define the question and a proportionate investigation.

## What to bring and what to produce

Use the current product intent, relevant requirements, user or operational outcome, team Definition of Done, dependencies, and planning conventions. A complete PRD is helpful but not required to write a draft item; mark missing decisions honestly.

For AI work, use `ai-prd` and `determinism-compass` to identify the approved behavior and which parts rely on models. The AI-PRD's current structure places behavior in §4, evaluation in §6, confidence/fallback policy in §7, rollout in §8, risk in §9, metrics/events in §10, economics in §11, and operations in §12. Follow the actual version and section headings if they change.

Produce the useful backlog items, their applicable scenarios, requirement links, dependencies, sizing or uncertainty, and a verdict: **ready for the next planning step, needs clarification, retype, split, or investigate**. Readiness to plan is different from implementation complete or authorization to expose users.

## Seven steps

### 1. Type the work honestly

| Type | Purpose | Evidence of completion |
|---|---|---|
| User story | Deliver a meaningful behavior or outcome for a user or other beneficiary | The defined behavior and its applicable acceptance criteria are demonstrated |
| Technical enabler | Establish a capability, reduce a material risk, or support an operational requirement | A verifiable technical/operational outcome and a clear value or dependency link |
| Spike / investigation | Resolve or reduce a consequential uncertainty within a bounded effort | Findings, limits, and a decision or explicit unresolved question with a next step |

Keep ordinary implementation tasks, maintenance, and incidents in their appropriate form. A refactor does not become user value merely by adding “As a user.” An enabler need not unblock exactly one next story: security maintenance, resilience, compliance, and shared infrastructure can have portfolio or operational value. Name that value rather than inventing a dependent story.

Scope a spike around a question, such as whether a vendor API can support a specified workload. Agree on a timebox, evidence plan, decision owner, and what happens if the answer remains uncertain. One to three days can suit a small investigation; it is not a universal duration. Experimental code may be disposable or reusable after review. The deliverable is learning and a decision, not a promise to produce production code or reach a predetermined answer.

### 2. Write the outcome plainly

Use a story spine when it helps:

```text
As a [relevant role or beneficiary], I want [capability],
so that [meaningful outcome].
```

Read the outcome clause on its own. Does it explain why the work matters? A quantified target can help when supported, but accessibility, reduced confusion, necessary maintenance, or a learning objective need not have an invented percentage. “User” can be adequate when no narrower role matters; name a specific role when it changes behavior or permissions.

For an enabler, a direct statement is often clearer: “Make payment-webhook processing idempotent under vendor retries so reconciliation does not post the same event twice.” Link the relevant capability, risk, or dependent work.

### 3. Apply INVEST as a conversation aid

| Check | Question and useful response |
|---|---|
| **Independent** | Can this be prioritized and demonstrated without hidden dependencies? Declare and sequence real dependencies rather than pretending they do not exist |
| **Negotiable** | Which details can the team refine, and which constraints are binding? Mark fixed requirements with their real authority and source; an entire implementation is not necessarily fixed because one obligation is |
| **Valuable** | Who benefits, through what outcome, risk reduction, or enabling capability? Make indirect value traceable |
| **Estimable** | Is there enough understanding for the planning decision? Use a range, smaller scope, investigation, or empirical flow history when more useful than points |
| **Small** | Can the team complete and verify a useful increment within its working cadence? Split where that preserves coherence; record an irreducible dependency or migration explicitly |
| **Testable** | Can builder and reviewer agree on how evidence will establish completion? Clarify ambiguous behavior and use an appropriate rubric or measurement method |

Do not assign a large item the sprint's first slot merely because it is difficult to split. Prioritize using value, risk, dependencies, and capacity. If an acceptance disagreement appears during implementation, update the shared understanding and requirement source through the agreed process.

### 4. Examine five scenario classes

Consider each class and write the cases relevant to the story. The grid is a coverage aid, not a requirement to manufacture a negative case for every small edit.

| Class | What to consider |
|---|---|
| Positive | Intended behavior for the primary role and supported variations |
| Negative | Invalid input, unavailable dependencies, denied or revoked permission, malformed responses, interrupted work |
| Boundary | Empty and maximum values, concurrent edits, duplicate submissions, expired sessions, first/last item, threshold equality |
| Non-functional | User-relevant latency, accessibility, auditability, localization, resource limits, privacy, retention, and operational behavior |
| State and data variation | Legacy records, migrated accounts, feature flags, rollout cohorts, partial updates, and version changes |

Given/When/Then is one useful form:

```text
Given [relevant state, input, and authority],
when [event or action],
then [observable behavior and important limits].
Verification: [fixture, check, rubric, measurement, or review].
```

Use concise checklists, examples, or tables when they are clearer. For discrete requirements, write a definite pass/fail check. For probabilistic quality, usability, or subjective work, define the rubric, sample, measurement, and acceptance decision while retaining graded evidence. A clear decision does not require pretending every output has only one correct wording.

“Handles errors gracefully” needs observable behavior. “Returns a retryable 503” may be useful for a particular API contract, but it is not the right response to every error. For an uncertain write, a retry can create duplicate effects; define reconciliation and idempotency before retrying. Showing an idempotency key in a log is not enough to prove exactly one business effect.

Link the team-wide **Definition of Done** for shared requirements such as review and instrumentation. State story-specific additions and exceptions explicitly. Avoid repeating the whole DoD on every card, but do not omit a critical requirement just because a generic DoD mentions testing.

### 5. Trace applicable AI requirements

Use the current AI-PRD and its `references/ai-user-stories.md` to preserve six areas of coverage: **capability, evaluation, fallback, guardrails, instrumentation, and rollout/operations**. These are areas to cover, not six mandatory new tickets. Shared infrastructure can satisfy part of the work.

For the item, trace the relevant:

- Behavior, permission boundary, evidence policy, and fallback.
- Examples and evaluation cases, including meaningful good, bad, and boundary behavior.
- Ownership, escalation, and operational coverage.
- Monitoring or change trigger, where applicable.
- Cost implication and its connection to the feature budget or outcome target.

A numerical confidence band is needed only when the product uses a validated signal and policy. An event-logging or evaluation story does not need a fictional user-facing confidence threshold. Three examples can start a review; relevance and coverage determine whether fewer or more are needed. Link shared owners, budgets, and monitoring instead of inventing a standalone success denominator for every infrastructure ticket.

Add model-specific cases where they apply: timeout, malformed output, insufficient evidence, unsafe output, unsupported intent, context limits, and configuration changes. Check equality at any actual threshold and distinguish a missing score from a low score. Use population-based latency or quality measures; a single request does not have its own P95.

When a required product decision is missing or contradicts the story, surface the gap and resolve it with the responsible people. Do not silently improvise a threshold, preserve a known-wrong PRD, or send all discovery back to the PM by default. Update the authoritative requirement and dependent items together. A draft story can exist before resolution; dependent exposure cannot be called ready while a material required decision remains open.

### 6. Size using the team's actual conventions

Use enough estimation to support a decision. H/M/L is an option when coarse sizing helps:

| Label | Typical meaning | Illustrative local point mapping |
|---|---|---|
| Low | Familiar work with limited scope and understood dependencies | 1–3 |
| Medium | Several surfaces or a meaningful new pattern/dependency | 5–8 |
| High | Substantial scope, difficult dependencies, or important uncertainty | 13+ |

These mappings are not universal or comparable across teams. Effort, elapsed time, complexity, and uncertainty are related but different. Historical examples can calibrate labels; stable velocity does not make a point estimate objectively precise.

A long sizing discussion may reveal a missing fact, disagreement on scope, or simply unfamiliarity. Pause to identify which one rather than creating an automatic spike after two minutes. High means inspect the work: split it, investigate a specific unknown, or plan an explicitly understood larger item if the team's cadence and capacity support it. Do not batch all small work or seek a PO exception for every large item solely because this table says so.

### 7. Slice into useful, safe increments

Prefer a coherent behavior or operational outcome over a collection of unfinished layers. A vertical slice crosses the layers **needed for that outcome**, not necessarily a UI, API, and database in every story. Technical tasks and enabling layers can still be planned honestly with integration and completion criteria.

Possible slices include a supported scenario, one segment or region, one data variation, one workflow step, or one mode of service. Choose the sequence from value, dependency, and risk rather than a universal order.

**Build order and release readiness are different.** You may implement the happy path first, but complete its necessary authorization, failure handling, validation, and recovery before exposing it. Do not ship a high-confidence AI path while postponing the fallback or refusal behavior it requires. A later story may expand supported scenarios; it must not conceal a safeguard needed by the earlier slice. Narrow or disable unsupported behavior where appropriate.

## Worked examples

These are illustrative requirements to discuss with the team, not verified systems or universal standards.

### User story: invoice approval routing

As a regional finance approver, I want invoices above my delegation limit to reach an authorized approval tier so that month-end work is not delayed by manual reassignment. A proposed 80% reduction in reassignment tickets is an outcome hypothesis, measured separately from implementing the routing correctly.

- Given an invoice one cent above the applicable limit, submission routes it to the next authorized tier within the agreed target, such as 60 seconds, and shows its status and approver.
- If that approver's delegation has expired, apply the controlled escalation policy. Skip to another tier only if the policy authorizes it; otherwise hold for resolution. Record the reason.
- If the hierarchy service is unavailable, retain a visible pending state. Retry only within the agreed policy and budget, rechecking authority as required; at an illustrative four-hour limit, alert finance operations and preserve a recoverable state.
- Duplicate submission or redelivery creates one approval workflow for the same logical invoice operation. Test concurrent requests and recovery after interruption.
- Record the actor, event, time, decision, and rule version with appropriate access controls. A five-minute retrieval target is a proposed internal control requirement, not a universal SOX rule.
- Delegation limits come from the controlled authority table; changes follow the approved process.

**Illustrative size:** Medium in a team familiar with the workflow engine and the hierarchy dependency. Verify the policy and unknowns before assigning the estimate.

### Technical enabler: idempotent payment webhooks

Make ingestion idempotent so auto-reconciliation, including story #214 in this example, does not post the same payment event twice.

Use a fixture of **500 unique vendor event IDs plus duplicate deliveries**. After replay and interruption/recovery, demonstrate 500 intended ledger postings with no duplicated or missing logical events under the specified test conditions. Test concurrency, deduplication retention, transaction boundaries, and uncertain acknowledgments. A test fixture passing is evidence for those cases, not a guarantee of exactly-once delivery everywhere.

**Illustrative size:** Medium if the storage and vendor semantics are understood; otherwise name the unknown before estimating.

### Spike: vendor OCR fitness

**Question:** can the vendor OCR service sustain the intended 50-request/second workload on representative invoice PDFs while meeting a proposed 95% field-quality criterion and the relevant latency, cost, privacy, and error-severity requirements?

**Example timebox:** two days. Use an authorized test environment and workload. Define fields, scoring, document/language mix, critical-field failures, sampling limits, and steady-state/load conditions. Report whether the evidence supports vendor use, further investigation, or evaluating a self-hosted alternative. Do not assume the alternative works merely because the vendor fails.

**Output:** concise findings, limitations, recommendation, and updated scope or estimates for dependent items. Decide explicitly whether experimental code is discarded or reviewed for reuse.

### AI story: Athena's reviewable draft replies

Use Story A1 in the revised AI-PRD's `references/ai-user-stories.md`. Athena produces drafts and never gains permission to send messages or issue refunds from a confidence score.

Apply the grid: source unavailable or stale; permission revoked; no score; a score exactly at a validated policy boundary; a legal-threat case under the actual escalation rule; and the first request after a configuration change. The 0.85/0.70 bands remain candidate policies until validated, not numbers this skill can approve by copying them.

Verify the linked G1/G2/B1/B2/R1/R2 behavior examples and broader coverage, actual operational owners, configuration traceability, monitoring, and proposed P95 two-second workload target. Inherit the feature cost definition from §11; $0.031 is a fictional modeled target, not a guarantee for this story or an independently measured outcome cost.

If the work is too large, slice by a safe supported scope or an enabling capability. Preserve required fallback and authority behavior before exposure; do not split simply into “high score now, safety later.”

## Review and deliver

- [ ] Each item has an honest type and a traceable user, operational, or enabling outcome; investigations have a question, timebox, and decision path.
- [ ] The purpose explains why the work matters without invented metrics or decorative story clauses.
- [ ] The five scenario classes were considered; applicable criteria have observable verification and a clear acceptance decision.
- [ ] INVEST surfaced real dependencies, uncertainty, and fixed requirements rather than hiding them.
- [ ] AI requirements trace to the current source, with applicability and unresolved conflicts explicit.
- [ ] Size or uncertainty uses the team's planning method; larger items have a credible completion plan.
- [ ] Slices deliver coherent value, with release dependencies and necessary safeguards intact.

Use a compact card: **title/type, outcome, requirement source, acceptance and verification, dependencies/constraints, size or uncertainty, and readiness verdict**. Include owner and next decision where needed. Separate story completion from the later evidence that a business outcome improved.

The trade-off is time spent clarifying now against rework and late surprises. No universal 20% refinement overhead or 100-fold later cost is established. For a backlog audit, reviewing the top ten items and applying the grid deeply to three can be a useful starting exercise; choose a smaller or broader sample when it better serves the task.

A diagram is optional if it helps explain work typing, coverage, or dependencies. See [Story evidence and review notes](references/story-evidence.md), and use the shared Universal Skill Protocol for proportionate handoffs.
