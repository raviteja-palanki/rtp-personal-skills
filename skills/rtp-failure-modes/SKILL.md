---
name: failure-modes
version: v2.1.1_latest
description: "Identify how an AI feature can fail, assess the consequences and detection gaps, and design the response before release. Covers six hallucination subtypes, retrieval failures, prompt injection, inappropriate refusals, latency and cost overruns, cascades, and silent degradation. Build a failure register with evidence, owners, prevention and detection controls, user recovery, fallback triggers, and testable acceptance criteria. Use for feature specifications, production monitoring, pre-launch audits, and analysis of live failures, including deterministic components within the AI workflow. Pairs with stress-test, feedback-triage, ai-ux-patterns, confidence-tuner, trust-ladder, and agent-risk. Use problem-ai-fit when the main question is whether AI belongs in the solution. Triggers: 'what could go wrong', 'failure audit', 'how should it fail'."
imports: [stress-test]
---

# Failure Modes — Diagnostic and Response Design

Map how the product can fail its users, then specify what prevents the failure, detects it, contains its effects, and helps people recover. The deliverable is an **owned failure register and testable response criteria**. This skill includes the confidence UX, correction paths, refusal boundaries, and degradation content formerly separated into Failure Design.

A successful model response can still be false, incomplete, stale, unauthorized, or unsuitable for its next use. Valid syntax and a successful tool call do not establish a correct outcome. Design the full path from input to user consequence, including deterministic components and human handoffs.

## Start with consequence and exposure

Establish the user and task, the output's next use, permitted actions, and the time before a mistake causes harm. Read existing telemetry and incidents when available. Distinguish observed failures from suspected ones and unknown coverage; do not invent a rate to complete the table.

Prioritize severe or unacceptable consequences before using an expected-cost estimate. **Confident wrong** is an important risk when certainty encourages action on false information, but it is not always the most harmful failure. An omitted warning, denied legitimate request, privacy breach, or late result can be worse in a particular task. A disclaimer does not guarantee that the user verifies or avoids harm.

Use `rtp-jtbd-analysis` to understand the job and relevant failure costs, without assuming a hidden job from a label. If the main question is whether AI is appropriate, use `rtp-problem-ai-fit`. Reuse the shared `UNIVERSAL-SKILL-PROTOCOL.md` at the AI-PM collection or plugin root.

A quick audit can focus on the most consequential few modes and the next decision. A full review covers the workflow, dependencies, monitoring, controls, and response tests. Five modes, twenty minutes, or two to four hours are planning examples—not proof of sufficient coverage. A sandbox or beta label can reduce exposure but does not remove data, tool, or downstream risks.

## Phase 1 — Identify specific failures

Write each mode as a concrete event: **under [condition], the system does [wrong behavior], causing [effect] for [person or system].** Keep cause, manifestation, consequence, and detection separate. Taxonomy categories can overlap; tag them for routing without counting one incident several times in a loss estimate.

| Type | What can go wrong | Check to consider |
|---|---|---|
| Hallucination — fabrication | Invents a fact, event, citation, or result | Verify against an authoritative source or independent evidence. |
| Hallucination — conflation | Combines real facts from different entities or contexts | Check entity, scope, and relationships against the underlying records. |
| Hallucination — extrapolation | Extends a pattern beyond the supporting data without adequate qualification | Inspect the inference, assumptions, and limits of the evidence. |
| Hallucination — temporal confusion | Presents historical or future information as current | Check dates, version, and the task's freshness requirement. |
| Hallucination — over-generalization | Treats a finding about a specific setting as broadly established | Compare the claimed population and scope with what was measured. |
| Hallucination — misattribution | Assigns a real quote, fact, or work to the wrong source | Check the citation and its actual support for the claim. |
| Confident wrong | Presents an incorrect result with unjustified certainty | Compare correctness with the signal users receive and the actions they take. |
| Prompt injection | Untrusted content redirects behavior or seeks unauthorized access or disclosure | Test instruction boundaries, permissions, data handling, and tool controls. |
| Retrieval or synthesis failure | Misses relevant material, retrieves unsuitable material, or misuses a correct source | Inspect coverage, access, ranking, source support, and synthesis separately. |
| Inappropriate refusal | Declines a legitimate supported request or fails to offer available help | Review refusal reasons, task scope, and outcome costs. An appropriate refusal is a control, not an error. |
| Latency or cost overrun | Misses a time requirement, repeats work, or exceeds the budget | Measure end-to-end latency, tails, retries, tool costs, and human work. |
| Cascade or coordination failure | A bad assumption, stale state, or failed action propagates through later steps | Test handoff contracts, state transitions, partial failure, and final outcomes. |
| Silent degradation | Quality or coverage changes without a useful alert | Use representative outcome checks, change records, segment analysis, and detection tests. |

Include other task-relevant failures: omissions, unequal performance, unauthorized actions, privacy leakage, data corruption, and poor recovery. The list is a starting taxonomy, not an exhaustive proof that every failure is known. Detectability and severity depend on the actual product; conflation is not inherently undetectable and refusal is not inherently low-cost.

## Phase 2 — Quantify exposure and detection gaps

For each material mode, record:

- **Frequency or probability:** observed rate, estimate range, or unknown; include denominator, period, and source.
- **Consequence:** direct and downstream effects, affected population, severity, recoverability, and who bears the cost.
- **Detection:** method, coverage, likely delay, owner, and time remaining to intervene.
- **Response and residual risk:** proposed control, expected effectiveness, cost, new failure modes, and what remains after it.

Use **immediate**, **delayed**, or **unobserved without additional checks** as useful detection descriptions, with task-specific time ranges. **External discovery** describes who notices, not a distinct delay: a customer can discover an error immediately or months later. Assign effective detection to material silent failures; where detection remains weak, reduce exposure, add prevention, or defer the unsupported use.

An expected annual loss can help compare ordinary recurring risks:

```text
annual expected loss = annual exposure × failure probability per exposure × expected loss per incident
```

State assumptions about dependence, event definitions, and overlapping losses. This estimate does not replace severe-scenario analysis or applicable requirements. Detection delay can increase exposure and loss, but **cost × time invisible** and **cost × 1/detectability** are not universal quantitative formulas. Use them as qualitative prompts unless the variables and model are justified.

An illustrative comparison at **10,000 exposures per year**:

| Mode | Assumed probability | Loss per incident | Expected annual loss |
|---|---:|---:|---:|
| Confident wrong | 0.5% | $5,000 | $250,000 |
| Fabrication | 3% | $500 | $150,000 |
| Injection incident | 0.01% | $50,000 | $50,000 |

The rows illustrate arithmetic, not measured attack rates or a universal priority order. Categories can overlap and must not be blindly summed. A rare injection with a much larger plausible consequence may still dominate the decision.

Compare **expected risk reduction**, control effectiveness, and complete control cost—not only prevention cost versus gross annual risk. The former “invest below 10%, reassess above 50%” bands were illustrative and ignore important context. Some controls are required even when financial estimates are uncertain; some cheap controls are ineffective.

## Phase 3 — Design the response and user experience

For each failure, distinguish four situations:

| Situation | Required design question |
|---|---|
| Wrong and noticed before use | How can the result be corrected, rejected, or independently checked? |
| Wrong and noticed after use | Which actions and people are affected, and what repair or notification is possible? |
| Wrong but unlikely to be noticed | What check can detect it, or what boundary prevents unsupported reliance? |
| Wrong and already propagated | How do we stop further use, identify descendants, correct records, and address external consequences? |

Choose among **bounded partial service**, **explicit abstention or failure**, and **an explicitly accepted residual risk**. The last is not a license to hide failure. In a low-consequence experiment, users may knowingly receive unverified drafts; describe what is unverified and prevent unsupported use. When residual risk is unacceptable, constrain or withhold the affected capability.

Useful UX patterns include task-specific uncertainty, editable drafts, evidence views, a meaningful feedback route, clear degraded-mode labels, and supported undo or escalation. State known causes accurately: “The available policy was last updated in January” is appropriate only when verified. A request for one missing detail can be helpful; asking someone to rephrase everything may merely shift the burden.

An edit or report does not automatically train the model. Route proposed corrections through validation, privacy handling, evaluation, and change approval as appropriate. Feedback collection and deployed learning are separate processes.

**Refusal boundaries depend on support and consequence.** Define when the system can answer, should ask a focused question, may provide a limited result, must escalate, or must refuse. Where a calibrated probability usefully informs this decision, specify the measure and justified threshold. Do not invent one from the model's wording or use confidence as the sole control. Over-refusal can cause real harm too.

An undo control must state its true window and effects. Thirty seconds is not a universal minimum, and deleting a record does not retract information already disclosed. Use `rtp-ai-ux-patterns` and `rtp-confidence-tuner` for the interface; this register owns the failure-response requirement.

## Watch for a documented error becoming an accepted rule

The library's **laundering-path hypothesis** describes a risk in four steps:

1. The system fails to recognize that a case exceeds its competence.
2. It resolves the case rather than escalating, without a visible error.
3. A traceable record is saved and may be reused as precedent.
4. Later people or systems treat the recorded answer as validated rather than as an unresolved result.

Provenance helps audit and correction; it does not itself cause error or establish truth. The dangerous step is **promotion from recorded output to accepted guidance without validation**. Silent errors can also leave records, and a documented wrong answer is not necessarily permanent if correction and invalidation are designed.

Falling escalation and rising automation may reflect improved capability—or a weakened boundary check. Investigate the change rather than celebrating or condemning it from the graph alone.

Sample cases near the operating boundary and cases that previously would have escalated, alongside representative general cases and appropriate automated checks. Human grading must be competent and sufficiently independent. Review model, prompt, threshold, data, and policy changes. Preserve status, version, source, and links from a rule to the evidence and decisions that produced it; provide a way to retract a wrong rule and find affected outputs.

This mechanism was assembled in the Novel Insights ledger from the middle-office article; it is a hypothesis, not a documented universal incident class. `rtp-context-spec` owns the boundary context and handoff requirements. Scale checks to consequence; a cheap reversible draft may need much less than a reused decision precedent.

## Phase 4 — Choose a valid fallback path

Consider cache → simpler model → rules → human escalation → explicit error as **options**, not an automatically safer fixed hierarchy. Choose the order by failure cause and task requirements; a later option may be less suitable than stopping.

| Option | Useful when | Check before using it |
|---|---|---|
| Cached result | A prior result remains valid for the current request | Freshness, context, user/tenant permissions, policy version, and whether the original result was verified |
| Simpler model | The task remains within that model's evaluated capability | It does not repeat the same failure, lower required quality, or bypass restrictions. |
| Deterministic rules | The relevant case is covered by current, tested logic | Rule correctness, completeness, inputs, and appropriate exceptions; deterministic does not mean error-free. |
| Human escalation | A suitable person can resolve the issue in time | Competence, access, capacity, authority, response time, and what happens while waiting |
| Explicit failure or limited result | No supported path can complete the request | Clear status, preserved work, useful next step, and no false claim of completion |

For each path, specify the trigger, allowed data and actions, user-visible status, owner, timeout, cost limit, and exit behavior. A support flow might use a current authorized knowledge-base answer, then a bounded response, then a staffed handoff. “Creating a support ticket” is a completed-action claim only when the tool has actually created it and the action is authorized.

The old 50-plus cached matches, 50 ms/200 ms targets, and 60% threshold were examples. Test the actual service; exact textual similarity does not establish factual applicability. Do not silently return stale or less reliable information as an ordinary successful answer.

## Phase 5 — Control cascades across the full workflow

Cascades can occur in a single agent with several tools, multiple agents, deterministic services, or a human handoff. They are not exclusive to multi-agent systems. Map dependencies and specify checks at consequential boundaries, with final outcome checks for failures no individual step can see.

| Propagation path | Controls to evaluate |
|---|---|
| Unsupported upstream claim reused as fact | Evidence and validity checks, explicit uncertainty/status, and a handoff contract |
| Coordination or shared-state drift | Ownership, state-version checks, concurrency control, and reconciliation |
| Repeated failing or duplicate tool actions | Retry limits, idempotency where supported, timeouts, isolation, and circuit breakers |
| Context loss or saturation | Context-budget monitoring, grounded summaries, preserved constraints, and checks after handoff; compaction can itself lose information |
| Evaluator error | Appropriate deterministic checks, calibrated model-based assessment, expert review where needed, and disagreement analysis |

A **circuit breaker** temporarily blocks a failing operation and routes to a defined response. Set its conditions from failure severity, volume, and behavior. The former “three failures in ten minutes” was illustrative; a single severe event may require immediate stopping. Test reset and recovery so the breaker does not silently resume an unsafe action.

Log enough to trace agent or component → operation → input/source version → latency → failure → response, while limiting sensitive data. A checkpoint supports recovery only if the state and external effects can actually be restored. Do not prescribe rollback before every handoff as if it reverses every consequence.

**Use conditional reliability arithmetic.** If two stages each succeed with probability 0.95 under the necessary independence or conditional-success assumptions, both succeed with probability 0.9025. That describes a defined two-stage requirement, not an automatic law of final-answer accuracy.

In the earlier example, A passes bad input 5% of the time and B succeeds on bad input 20% of the time. Then **1% of all paths are bad-input cases B rescues**, and **4% retain an error on that branch**, assuming success means correction. Neither number establishes confident-wrong frequency. Overall outcome quality also needs B's performance on good input and the workflow's recovery behavior.

Classify recovery by actual effect: some suggestions can be dismissed in seconds; sent content or code may need correction and communication; bulk-record errors may require a broader audit. Information disclosure or injury may be irreversible, but containment, notification, remediation, and support can still be necessary. “No full reversal” does not mean “no useful response.”

## Example: stale data through a reporting pipeline

An illustrative three-stage pipeline uses an Analyst to retrieve warehouse data, a Summarizer to synthesize it, and a Reporter to format an executive brief. A partition stops refreshing but continues returning structurally valid rows. No component reports an error, and the polished final brief conceals the stale input.

The original anonymized story gave 19 days undetected, 34 customers receiving briefs, and three acting on them, without a verifiable source. Treat those as scenario values, not a documented 2024 incident. The lesson is testable: data freshness and end-to-end usefulness need checks beyond tool success or output format.

Define freshness requirements from the business use, carry source timestamps, test the freshness check itself, and examine final output quality. A six-hour freshness limit, 20% deviation flag, and daily check are example settings. Genuine business shifts can exceed a deviation threshold; stale data can remain within it. Use independent signals rather than treating either check as proof of correctness.

## Deliver the register and acceptance criteria

Use a table containing:

```text
Failure ID and version | subtask | condition and wrong behavior | affected user/action
Evidence, exposure, rate/uncertainty | severity and recoverability | detection coverage/delay
Prevention | detection | containment/recovery | fallback and user-visible response
Owner and operating capacity | response deadline | residual risk and decision
Acceptance case and expected result | validation evidence | next review trigger
```

For each relevant user story, add a specific failure criterion. For example: **Given** data older than the allowed freshness window, **when** a brief is generated, **then** the affected conclusion is withheld or clearly limited, the source date is visible, and the defined recovery path is offered. Test the real control, including partial failure, rather than only its wording.

Before concluding, check coverage of the six hallucination subtypes and other relevant modes; plausible severe scenarios; assumptions behind risk estimates; detection ownership; refusal and fallback triggers; cascade boundaries; recovery limits; and evidence that the planned response works. Mark a category inapplicable with a reason rather than inventing an example. The need for monitoring follows consequence and detectability, not a universal one-hour cutoff.

`rtp-stress-test` supplies load, cost, latency, adversarial, and operating evidence. `rtp-feedback-triage` routes observed failures using this taxonomy. `rtp-ai-ux-patterns` renders the response; `rtp-confidence-tuner` validates signals; `rtp-trust-ladder` addresses reliance and repair; `rtp-agent-risk` handles proportionality, authority, and stopping.

Name the top unresolved risk, the recommended control or accepted residual risk, its evidence and cost, the largest uncertainty, and the next action with an owner. Consider over-mitigation too: checks can add latency and workload, refusals can block useful work, and repeated generic warnings may be ignored. Choose proportionate controls instead of maximizing every safeguard.

Use a cost/consequence-versus-detection-delay visual when it clarifies priorities, with uncertainty shown and hard constraints kept visible. Consult [examples and calculation notes](references/examples-and-calculations.md) and the [concept guide](CONCEPT.md) for supporting detail.
