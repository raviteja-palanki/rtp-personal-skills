---
name: invisible-stack
version: v2.3.1_latest
description: 'Map the system around an AI model to find what limits production quality, safety, speed, or cost. Use the seven CONTEXT categories to inspect rules, live observations, knowledge, memory, tools, execution, and output contracts, plus shared controls and monitoring. Diagnose demo-to-production gaps, retrieval problems, architecture risks, and failures under load. Measure candidate bottlenecks and interactions before choosing a fix; do not assume the model or a single upstream layer is always responsible. Scale the audit to the actual feature and action rights. Pairs with context-spec for the build specification, eval-framework for tests, production-observability for instrumentation, failure-modes for response design, and cost-model for economics. Triggers: AI architecture review, RAG quality, demo works but production fails.'
imports: [determinism-compass, stress-test]
---

# Invisible Stack

Find which parts of the system constrain the outcome the user needs. The model, context, tools, interface, and operating environment can each cause or amplify a failure. Make those dependencies visible enough to test, then choose the change that addresses the evidence.

## Start with the task and consequence

Establish the feature, expected outcome, actual action rights, production conditions, and observed gap. Define what counts as success and which failures require containment before further diagnosis. Reuse known context and follow the Universal Skill Protocol at the source library root or packaged plugin root, scaling the work to the request.

Use a substantial audit for systems with retrieval, state, tools, or complex handoffs. A simple single-turn feature still has inputs, instructions, model behavior, output handling, and operational dependencies; inspect the relevant parts without inventing unnecessary infrastructure. If the first uncertainty is whether any model can perform the task, a bounded capability test may be the right starting point.

An autonomy label from `rtp-ai-use-case-readiness` helps frame the review, but does not determine the architecture. Inspect the actual tools, permissions, state, and control flow. A chatbot may call tools; a narrow agent may need little persistent memory. Do not infer that a numbered level guarantees the presence or absence of a CONTEXT category.

## 1. Map the actual system with CONTEXT

Use Ravi’s seven categories as a completeness check. They describe responsibilities, not seven mandatory services or a fixed sequence. A component may serve several categories; some categories may be unnecessary for this feature.

| Category | What to map | Questions that reveal a gap |
|---|---|---|
| **C — Constitution** | Instructions, policy, rules, priorities, and permission boundaries | Which rules govern the task? What enforces them? How are conflicts resolved? |
| **O — Observations** | Current request, live data, user/session context, and environmental state | Are the observations current, correctly attributed, and sufficient? |
| **N — kNowledge** | Documents, retrieval, source selection, and grounding | Can the system obtain the right evidence with the right access and provenance? |
| **T — Tracks** | Conversation history, persistent memory, state, and prior decisions | What is retained, updated, forgotten, or isolated between users and tasks? |
| **E — Equipment** | Tools, APIs, external systems, and their permissions | Are tool contracts understood, actions authorized, and failures recoverable? |
| **X — eXecution** | Routing, planning, context assembly, retries, caching, and orchestration | What runs when, what can repeat, and what happens after partial completion? |
| **T — Template** | Output schema, presentation, citations, and downstream contracts | Is the result usable, correctly structured, and faithful to its evidence? |

Place model inference explicitly on the map. Add cross-cutting validation, security, privacy, identity, observability, and human escalation where they operate. These are not substitutes for the seven categories or additional requirements to deploy as separate services.

Draw the real branches and feedback paths from input to user outcome, including data ingestion, human intervention, and external actions. Identify trust boundaries: retrieved documents, tool results, and user-provided content are data to interpret within the governing instructions, not automatic authority to alter them.

For each relevant responsibility, record its owner, inputs and outputs, version or configuration, monitoring, failure behavior, and dependencies. Mark absent responsibilities as either **not needed**, **covered elsewhere**, or **an actual gap**. An empty checklist cell is a question, not automatically a defect.

## 2. Form competing explanations

Avoid the spotlight effect of blaming the visible model by default. Also avoid its reverse: presuming infrastructure is responsible before checking model capability. The original “10% model, 90% stack” framing is an illustration, not a measured allocation or a universal ordering of importance.

Use traces and representative cases to locate where the observed behavior diverges from the intended behavior. Possible explanations include missing information, wrong information, insufficient model capability, misleading presentation, incorrect state, bad tool contracts, and failures caused by component interaction.

For a retrieval complaint, distinguish:

- the source does not contain the needed information;
- access, ingestion, indexing, or freshness prevents retrieval;
- search returns inadequate candidates;
- reranking or context assembly drops the useful evidence;
- the model misuses adequate evidence;
- the output contract or interface misrepresents the answer.

Several can be true together. Name a leading hypothesis, credible alternatives, and the next comparison that will distinguish them. If there is not enough measurement to identify a bottleneck, say so and propose the smallest useful instrumentation or replay.

### Use the weakest-layer idea precisely

A necessary unrecovered failure can limit the whole task. If success truly requires a particular fact and the system has no other permitted way to obtain it, failing to supply that fact prevents that kind of success. This is a conditional dependency, not a universal formula equating the smallest component percentage with product quality.

**Precision@5** is the fraction of five retrieved items judged relevant. It is not the percentage of requests that can be answered. Two relevant items among five may contain everything needed; five relevant items may still omit the decisive fact. Retrieval hit rate, recall, evidence sufficiency, and answer correctness measure different things. Do not call 50% precision a 50% answer-quality ceiling. See [measurement and evidence notes](references/measurement-and-evidence.md).

Upstream repair can help, but later stages sometimes recover through another retrieval, a tool, clarification, or an appropriate refusal. Test those paths. If a component fix does not improve the outcome, inspect interactions, wrong metrics, compensation, and other bottlenecks before declaring the audit successful.

## 3. Measure relevant responsibilities and the whole task

For each component, define its evaluation population and denominator. Assess coverage, quality, latency, cost, and consequence where relevant. Coverage alone does not determine importance: a rare permission check may protect the most consequential action.

| Responsibility | Useful measures and checks |
|---|---|
| Rules and permissions | Relevant policy cases covered, actual violations and incorrect restrictions, enforcement location, added work or latency |
| Observations and knowledge | Freshness, source coverage, retrieval hit/recall/precision where meaningful, evidence sufficiency, access violations, empty results, and retrieval latency |
| Tracks and context assembly | Relevant context retained, stale or contradictory state, cross-user leakage, truncation, and state-update correctness |
| Tools and execution | Valid tool selection and arguments, authorized actions, task success, safe fallback, partial failures, retries, duplicate actions, cost, and end-to-end latency |
| Validation and guardrails | Coverage by failure class, false positives and false negatives with explicit denominators, bypasses, and added delay |
| Output contract | Schema validity, factual support, citation fidelity, accessibility, downstream usability, and completion of the user’s task |
| Monitoring and response | Important failures detected, detection and response delay, alert usefulness, blind spots, and owner follow-through |

A fallback is not necessarily a defect, and a low fallback rate is not automatically desirable. Test whether it produces an acceptable result. A valid schema does not establish a true answer. “Detected before users reported it” measures one comparison; it does not count unknown failures and should not be the only monitoring measure.

Set acceptance criteria from task consequence, actual user needs, expected load, and evidence. The older thresholds—such as 70% Precision@5, 500 ms retrieval, or a 1% safety false-negative rate—are not release standards. The reference retains them as examples with their limits. Report insufficient evidence instead of treating a small test with no observed failure as proof of safety.

Allocate an end-to-end latency budget across the actual critical path. Separate time to first useful response from time to completed work, and include queues, retrieval, model calls, tools, retries, and human steps. Measure distributions under realistic concurrency. Per-component P95 values do not simply add into the overall P95. A three-to-four-second tolerance is not universal across users and tasks.

## 4. Test the diagnosis and the proposed change

Choose checks appropriate to the uncertainty and consequence:

1. **Baseline representative tasks.** Include important segments, ordinary successes, known failures, edge cases, and required adversarial cases. Record configurations and sampling limits.
2. **Compare demo and production conditions.** Identify hand-selected documents, manually supplied context, hidden human decisions, clean state, and simplified load that the demo relied on.
3. **Trace failures through components and seams.** Follow the same request across services rather than comparing unrelated dashboards.
4. **Replay or substitute a component.** For example, supply reviewed evidence to test whether retrieval is limiting the answer, or compare models while keeping inputs and evaluation stable. State what the intervention changes.
5. **Run bounded ablations when useful.** Remove or replace a component in an authorized test environment and observe effects. Avoid exposing users by disabling required controls. A near-zero measured change may reflect rare cases, redundancy, compensation, or inadequate sample coverage; it is not automatic permission to remove the component.
6. **Test the candidate repair end to end.** Check the intended improvement, relevant regressions, load behavior, cost, and recovery. Preserve independent evaluation rather than tuning every decision on the same examples.

Perform a proportionate prelaunch review and revisit after material model, data, tool, policy, or infrastructure changes. A quarterly review may be useful for a stable product; incident signals and significant changes can require earlier work. Avoid repeatedly auditing a thin prototype when a direct test can answer the question.

### Diagnose failures that appear only under load

An AI team may group errors by output quality while an infrastructure team groups them by system health. A connection pool, cache, rate limit, or queue can then escape the combined diagnosis even when neither dashboard looks obviously wrong. Bridge the taxonomies with a shared task trace, realistic load tests, and an accountable cross-functional owner.

This **classification gap** is a candidate mechanism drawn from three anonymized advisory cases, not a proven explanation for every demo-to-production failure. Failures at low load can still involve infrastructure; failures after a model change can involve interaction effects. Check both rather than using “probably infrastructure” to dismiss model regressions.

## 5. Make architecture choices against product needs

### Repair the workflow where the task requires it

Inspect data definitions, handoffs, ownership, and escalation before expanding automation. A broken process can create more errors when run faster. It creates a self-reinforcing data problem only when the system also reuses those outputs without adequate validation; automation does not necessarily learn from its own mistakes.

Fix the relevant dependency, not necessarily the entire enterprise. Data may need consistent semantics, quality, access, and curation without moving into one physical platform. A safe, bounded pilot can expose what needs redesign. A clean workflow may need little reengineering. Develop interaction and context architecture together so user requirements and system constraints inform each other.

Reuse well-tested platform capabilities when they fit. Evaluate a platform’s retrieval, state, governance, evaluation, handoffs, and observability alongside its models. Intuit’s historical GenOS case illustrates shared infrastructure and data preparation; it does not prove every company needs the same platform or years of consolidation before useful AI work. Its six-component mapping and evidence limits are in the [reference](references/measurement-and-evidence.md).

### Choose retrieval infrastructure collaboratively

Embedding, chunking, search, reranking, and database choices affect user outcomes and economics. The PM owns the product constraints and trade-offs with engineering and domain experts; the skill does not make every implementation choice a PM-only decision.

- Compare retrieval methods on representative queries and evidence needs. Small chunks may improve specificity but lose context; large chunks may preserve context but add irrelevant material. Neither is always better.
- Compare hosted, self-managed, and migration-ready options on total cost, operating capability, reliability, data controls, portability, scale, and lock-in. Hosted is not inherently more expensive, and self-hosting does not itself create a moat.
- Test reranking for its incremental effect on task quality, latency, and cost. Retrieving twenty candidates before reranking is one design example. The correct candidate set and delay budget depend on the task; research tools, chat, and autocomplete can have different constraints.
- Include indexing, storage, compute, embedding, reranking, networking, replicas, support, and operations in the cost model. Use current official pricing and workload measurements before making a purchase recommendation. Old per-query ranges are not reliable vendor comparisons.
- Check caching against freshness, permissions, user isolation, and invalidation. A cache can lower cost and latency while also creating stale or unauthorized answers.

Use `rtp-cost-model` and `rtp-token-economics` for the detailed economics.

### Separate useful data from a moat

Customer data may be valuable because of quality, rights, relevance, and the learning or workflow it supports. Exclusivity can help but does not guarantee defensibility. Identity or reputation records intended for cross-party verification may gain value from interoperability, with appropriate privacy and governance. This does not mean all such data should be public, or that an internal ranking score should be shared because it is named “trust.” Use `rtp-moat-finder` to assess the actual competitive mechanism.

## Deliver a decision-ready audit

Lead with the supported diagnosis—or the uncertainty that prevents one—and the next useful action. Include a proportional inventory:

| Responsibility | Needed and present? | Owner | Evidence and metric | Failure or gap | Next action and date |
|---|---|---|---|---|---|
| Relevant CONTEXT category or shared control | Status and reason | Accountable role | Baseline, criterion, and limits | Observation versus hypothesis | Repair or discriminating test |

Show the actual system diagram when it helps others understand dependencies. Mark measured bottlenecks, suspected causes, interactions, and recovery paths distinctly. A concise answer need not become a document, deck, spreadsheet, and visual merely to follow a template.

Before finishing, confirm that every relevant responsibility has been considered; important unknowns, owners, and controls are explicit; latency and cost use correct scopes; and proposed changes include a way to verify the user outcome. Avoid declaring a weakest layer from incomparable metrics or claiming that every failure has exactly one root layer.

Hand supported findings to `rtp-context-spec` for the build specification, `rtp-eval-framework` for evaluation design, `rtp-production-observability` for instrumentation, and `rtp-failure-modes` for response design. `rtp-determinism-compass` helps choose appropriate checks for different components; `rtp-stress-test` challenges capacity, cost, consequence, and recovery.
