---
name: rtp-ai-prd
version: v1.2.1_latest
description: 'Specify an AI feature so product, design, engineering, and operations can build and evaluate the same intended behavior. Connect the user problem and scope to behavior examples, evidence and confidence requirements, failure recovery, ownership, cost per successful outcome, rollout decisions, and monitoring. Translate relevant requirements into acceptance criteria across six backlog areas: capability, evaluation, fallback, guardrails, instrumentation, and rollout. Use for new AI capabilities, production requirements, architecture reviews, or adding AI criteria to an existing backlog; use a provisional Speclet for early exploration. Includes the section 0–13 PRD template and worked user stories. Pairs with eval-framework, confidence-tuner, cost-model, gen-ai-experimentation, ship-decision, and user-stories. Triggers: AI PRD, probabilistic spec, AI product requirements, AI user story.'
imports:
  - determinism-compass
  - bias-spotter
  - stress-test
  - prompt-as-product
---

# AI product requirements

Specify what the user should achieve, what the system may do, and how the product behaves when evidence or performance is insufficient. AI quality depends on both successful performance and effective handling of limitations. A good PRD connects these decisions to implementation, evaluation, and operations.

Traditional software also needs failure handling, costs, and uncertainty. AI often adds learned behavior, open-ended outputs, calibration questions, and changing data or context. These need explicit requirements even when a particular model returns the same output on repeated runs.

Start with the customer problem and authorized scope. Reuse available evidence and previous decisions. Ask for missing information when it changes a consequential choice; do not require every upstream skill to run before drafting.

## Choose the appropriate depth

- **New production capability:** follow the five phases and use the [PRD template](references/ai-prd-template.md). Keep supporting examples and backlog items in linked annexes when that improves readability.
- **Existing PRD:** inspect its problem and boundaries first, then fill gaps in evaluation, failure behavior, costs, and story acceptance criteria. Phase 3 is the main entry point for this work.
- **Cold start or early exploration:** create a Speclet. State the hypothesis and boundaries, sketch a few good/bad/refer examples, identify the most consequential failures, propose metrics and next tests, and write provisional stories or spikes if useful. Five examples—two good, two bad, one refer—can start discussion; they do not establish coverage.
- **Small or deterministic feature:** use only the relevant requirements in the team's existing format. A small AI component can still create a consequential effect, so percentage of the workflow is not a sufficient reason to omit risk analysis.

Use **⚠ provisional** for a material assumption without adequate evidence. In §13 record its basis, owner or assignment gap, validation method, and the decision it must be resolved before. Do not invent numbers or people to complete the form. Some assumptions can remain bounded after Kickoff; assumptions required for safe or meaningful exposure must be resolved before that exposure. Synthetic examples remain useful later, provided they are labeled and complemented by representative evidence.

## The decisions this PRD connects

| Input | Primary source or related skill | PRD section |
|---|---|---|
| Problem, job, segments, chosen opportunity | `jtbd-analysis`, `interview-synthesis`, `opportunity-solution-tree` | §1–3 |
| Strategy and reason to use AI | `strategy-canvas`, `problem-ai-fit` | §1 |
| Actual permissions and readiness | `autonomy-spectrum`, `ai-use-case-readiness` | §2 |
| Approach, rule/model boundaries, context | `build-or-buy`, `determinism-compass`, `context-spec` | §5 |
| Behavioral evidence and definition of good | Research/traces, `eval-framework`, `confidence-tuner` | §4, §6–7 |
| Experiment and exposure design | `gen-ai-experimentation` | §8 |
| Failures, containment, privacy, safety obligations | `failure-modes`, `agent-risk`, `safety-by-design`, `responsible-ai-program` | §9 |
| Measurement and telemetry | `ai-product-metrics`, `production-observability` | §6, §10 |
| Cost and viable economics | `cost-model`, `token-economics` where relevant | §11 |

Reuse current, applicable inputs; reconcile stale or conflicting ones. The PRD records the shared decision and its evidence rather than simply pasting incompatible outputs together.

The document feeds `ai-ux-patterns` and `trust-ladder` for product states, `user-stories` for backlog craft, `ship-decision` and `plan-launch` for readiness, observability and metrics for operation, and `retro` for the impact review. Produce the requested artifact; include linked stories when the work is ready for backlog handoff. A PRD can also support an early decision before a full backlog exists.

## Terms that need precise definitions

- **Evidence or confidence threshold:** a condition for showing, checking, or withholding a result. A score must estimate a defined event and be validated for the intended population. It never grants permission to take an action.
- **Dual metrics:** user outcomes alongside model/system behavior. Cost and safety guardrails complete the decision picture; “dual” does not mean exactly two numbers.
- **Hallucination or factual-error rate:** a specifically defined error measure. State whether the denominator is claims, outputs, conversations, or tasks, and distinguish unsupported claims from demonstrated falsehoods.
- **Calibration:** whether predicted probabilities match observed frequencies for a defined outcome. Good calibration allows some high-confidence errors; it does not mean none can occur.
- **Drift:** a change in inputs, context, task mix, behavior, or performance. It may be sudden or gradual and need not be deterioration. Retraining is one possible response.
- **Story inheritance:** an implementation item references the applicable PRD decisions and turns them into verifiable acceptance criteria. It need not copy irrelevant fields or duplicate a changing source of truth.

## Phase 1 — Map the behavior and the permissions

List operations such as validation, retrieval, ranking, generation, safety checks, and delivery. For each, identify input domain, output and acceptable variation, dependencies, state changes, authority, evidence requirements, latency, cost, and failure possibilities. Classify the actual implementation as rules, learned, generative, human, or hybrid. A rule written in a prompt is not automatically deterministic enforcement.

Define scope and non-goals before tool use or commitments. Separate drafting from sending, recommending from approving, and simulated actions from real effects. For agent workflows, use `agent-spec` to define handoffs, loops, termination, recovery, and permissions at each step. Multi-day execution does not remove product ownership or imply that someone is watching continuously.

Record a provisional user-outcome and system-metric pair here; define it once in Phase 3. Version prompts, model/configuration, context/retrieval changes, and relevant tools so later results can be traced to the configuration that produced them.

## Phase 2 — Specify failure, containment, and ownership

For relevant operations, examine false positives, false negatives, ambiguity, out-of-domain inputs, unsupported claims, unavailable dependencies, changing data, misuse, and adverse segment effects. When content is retrieved or tools are connected, include prompt injection, unauthorized writes, exfiltration, cross-user leakage, and uncertain external-action status.

For each material failure, record:

1. **Evidence or estimated frequency:** source, population, uncertainty, or “unknown.” Similar products and expert judgment are assumptions, not measured local rates.
2. **Consequence and exposure:** affected people, resources, downstream effects, reversibility, and aggregate scale.
3. **Detection:** signal, coverage, latency, and known blind spots. User feedback is often delayed and selectively observed.
4. **Containment:** affected work to stop or restrict, safe fallback, or authorized escalation. Prevent harmful tool effects before commitment where feasible.
5. **Recovery and communication:** distinguish rollback, compensation, reconciliation, and correction. Define what the user sees and who acts.
6. **Learning:** whether investigation should change data, context, prompts, tools, permissions, thresholds, tests, or training.

Name the responsible person or organizational role, intervention authority, capacity, coverage, and escalation route. The mindset/meaning/mechanisms lens helps check whether the owner understands their contribution, values the outcome, and has practical support. Reward sound review, justified approvals, error detection, and learning rather than an error-catching quota. Autonomous execution may have no per-action human reviewer; it still has a product or process owner.

For consequential production artifacts, establish appropriate review and sign-off, including lifecycle concerns that a narrow test suite misses. Existing delegated approval processes can be valid. Do not add an individual sign-off to every low-impact action or use a signature as proof of quality. The [evidence notes](references/prd-evidence.md) qualify the accountability-framing research.

Define monitoring and response to drift by risk and change rate. Investigate task mix, measurement changes, and data freshness before deciding to retrain. A new model can improve capability, create new failure modes, or leave the product decision unchanged.

## Phase 3 — Turn intended behavior into acceptance criteria

### Define examples and evaluation together

Use three categories:

- **Good:** input, relevant context and permission, acceptable output or action, and why it meets the requirement.
- **Bad:** observed or anticipated failure, why it is wrong, and the expected alternative.
- **Reject or refer:** the boundary that prevents the proposed action and the useful response, escalation, or safe continuation that remains possible.

Give examples stable IDs and provenance. Mark invented names, records, amounts, and thresholds as illustrative. Never teach a draft-only assistant to claim that it issued a refund. Do not require fabricated tracking numbers, response times, or manager names to make an example sound concrete.

Fifteen to twenty-five examples can be a useful initial behavior contract, not a universal minimum or a statistically sufficient evaluation set. Coverage depends on the task, segments, important errors, and interactions. Questions from engineers can reveal a missing requirement, conflicting evidence, or a design choice; they do not mean the only remedy is more examples.

Behavior examples seed both regression tests and story criteria. Keep a held-out evaluation set where needed; examples used to tune prompts are not independent evidence of generalization. Triage production corrections for validity, duplication, sensitivity, and generalizability. Add the meaningful failure pattern to tests and update affected examples/stories. Do not automatically retain every raw correction or alter three artifacts for every typo.

### Specify three evaluation layers

1. **Offline:** representative and challenging cases, defined labels/rubrics, relevant segments, uncertainty, and regression checks. Validate automated judges against appropriate human or objective references.
2. **Human review:** a rubric for qualities and consequences that automated checks miss, reviewer guidance, disagreement handling, and sufficient capacity. Binary checks suit discrete conditions; graded scales can preserve meaningful quality differences.
3. **Online:** user outcomes, system quality, operational metrics, and guardrails with an explicit action when evidence crosses the decision threshold.

For every important measure, define denominator, population, baseline, window, source, target or limit, uncertainty, and triggered decision. Distinguish a target, observed estimate, statistical interval, and operating limit. An estimated range is not inherently more honest than a well-qualified point estimate.

Use actual serving conditions. `pass@5` measures whether at least one of five candidates succeeds; it does not establish reliability when the product serves one unverified candidate. “Zero high-confidence errors in this sample” is a result or gate on that sample, not proof of perfect calibration or zero future risk.

### Connect evidence to product behavior

For each operation, specify when to show the result, request useful review, obtain more evidence, use a fallback, or decline the affected action. Bands such as above 0.85, 0.70–0.85, and below 0.70 are **illustrative only**. Simulate candidate policies on appropriate data, measure retained quality and coverage, and consider error consequences and review capacity. High rejection can be justified; low rejection can hide missed errors.

If scores are not calibrated or useful, use validated observable conditions. User confirmation is not ground truth, and willingness to accept does not authorize an otherwise prohibited action.

A fallback must fit the task and preserve its own permissions and freshness. Cached information can be wrong; rules are not automatically faster or safer; a safety classifier is not a truth oracle. Route to a cheaper or stronger model only when evidence supports the quality/cost trade-off for that case, not because “medium confidence” mechanically means cheaper.

### Link metrics to decisions without assuming a cause

User outcomes can include task completion, time saved, satisfaction, retention, and cost to the user. System measures can include class-level precision/recall, factual errors, calibration, latency percentiles, and cost per successful outcome. Acceptance, edit distance, and review time are behavioral signals, not direct correctness measures.

High average accuracy with poor outcomes can reflect UX, a poorly chosen metric, failure concentration, workflow friction, or insufficient capability. High acceptance with modest accuracy can reflect useful human correction **or** undetected harm. Investigate before concluding “redesign, never retrain” or “users filter well, ship.” Pair speed and approval rates with audits of accepted outputs and missed errors.

### Govern prompt and configuration changes

Keep versions, intent, relevant evaluation results, and an accountable change owner. Log configuration references with appropriate traces; do not indiscriminately log raw content. Test relevant regressions before exposure. Choose offline comparisons, canaries, A/B tests, or other validation according to consequence and the question being answered. An offline prompt comparison is not a live randomized experiment.

Define rollout and rollback criteria, emergency handling, and authorized reviewers. No fixed 200-case suite, 5% canary, two-week ramp, monthly review, or PM approval is appropriate for every change. Required safety or validity checks must pass before the corresponding exposure. Record legitimate changes to requirements explicitly; do not call a failed required check “post-launch work.”

### Carry applicable decisions into the backlog

Review all six areas, using existing shared work where it already covers the need:

| Story area | Inherits | Acceptance must demonstrate |
|---|---|---|
| Capability | §1–2, §4–5, §7 | User behavior, permission scope, relevant evidence policy, and examples |
| Eval / quality | §6 | Dataset coverage, judge/rubric validity, regression behavior, and review workflow |
| Fallback / degraded UX | §7, §9 | Exact trigger, allowed alternative, unavailable-alternative behavior, and recovery |
| Guardrail / safety | §2, §9 | Relevant failure, detection/prevention mechanism, containment, and actual obligation |
| Instrumentation | §6, §10 | Correct events and joins that make intended metrics computable, including missing-data behavior |
| Rollout / operations | §8, §12 | Exposure controls, evaluation/guardrail decisions, applicable assignment unit, and stop/recovery procedure |

These are coverage areas, not mandatory separate tickets or fixed counts. Instrumentation and evaluation needed for shadow or live decisions must be ready before those decisions. Use the [story template and six worked examples](references/ai-user-stories.md); use `user-stories` for INVEST, scenario thinking, spikes, and estimation.

Each relevant item should identify the user or operational need, inherited requirement/version, evidence/examples, owner, change or monitoring trigger, cost implication, and unresolved assumptions. Link shared feature requirements instead of inventing a confidence score or standalone cost-per-outcome for an event-logging task. An assumptions review may correctly find no material unresolved assumptions.

**User Story Health** is the proportion of reviewed in-scope items with all *applicable* inherited requirements traceable and verifiable. Define that denominator and review applicability. Aim for complete coverage of required work before exposure; a 100% documentation score does not prove product quality.

## Phase 4 — Check economics and segment consequences

Model total cost over a defined period, including input/output tokens at their respective rates, tools, retrieval, retries, caching, evaluation, infrastructure, monitoring, review, and relevant fixed allocations. Use consistent units and the actual billing basis.

```text
Token cost = (input tokens × input price per million
            + output tokens × output price per million) / 1,000,000
Cost per successful outcome = total cost attributable to the workflow
                              / verified successful outcomes
```

State whether cost is variable, fully allocated, or marginal. Include failed attempts in the numerator. Define what “P90 cost” measures; a percentile of request costs is not automatically the percentile of a cost-per-outcome ratio.

Compare a baseline, plausible growth, and stress cases. Tenfold and hundredfold volume and two-, three-, or fivefold price changes can be useful sensitivities when relevant, not forecasts. Model retries from the actual policy; `error rate × one-call cost` covers only a particular one-retry assumption.

Set a ceiling and the decision it triggers: investigate, optimize, change scope/pricing, limit exposure, or retire. Cheap routing or deprecation is not automatically the correct response. Carry feature economics into capability/fallback stories and an explicit overhead/allocation basis into enabling work.

Evaluate relevant language, geography, demographic, accessibility, and task segments where lawful and appropriate. Choose fairness measures based on the decision and harms; equal aggregate accuracy alone does not establish fairness. Report sample limits and investigate disparities. Threshold changes, data changes, UX changes, or restricted use may help; disclosure alone may be inadequate. Follow applicable obligations and pre-agreed containment rules rather than a universal quarterly schedule or arbitrary percentage-gap cutoff.

## Phase 5 — Assemble, test, and maintain the PRD

The canonical format contains **a §0 header plus thirteen substantive sections, §1–13**. Preserve section identifiers so stories and related skills can reference them.

| Section | Decision |
|---|---|
| §0 Header and decision summary | Stage, owner, current recommendation, material evidence and blockers |
| §1 Opportunity | Problem, hypothesis, strategy fit, AI rationale, impact, prototype learning |
| §2 Boundaries | Scope, non-goals, accepted trade-offs, permissions |
| §3 Users and job | Relevant segments, needs, evidence, access constraints |
| §4 Behavior contract | Good/bad/refer examples and acceptable variation |
| §5 Solution and architecture | Approach, components, context, prompts, dependencies |
| §6 Success measurement | Offline, human, and online evaluation with decision criteria |
| §7 Probabilistic behavior | Evidence policy, quality limits, fallback and refusal experience |
| §8 Rollout and experiment | Exposure, assignment where relevant, evidence duration, advance/hold/stop decisions |
| §9 Risk and incident response | Material failures, controls, recovery, obligations, owners |
| §10 Instrumentation | Events, labels, joins, sampling, privacy, observability limits |
| §11 Economics | Cost, outcome denominator, growth/stress cases, ceiling and response |
| §12 Lifecycle and launch | Stage criteria, readiness evidence, review decisions |
| §13 Questions and decisions | Assumptions, sources, owners, due decisions, resolutions |

Use the team's existing format when appropriate and retain an equivalent mapping. Length follows complexity and consequence; a particular page count does not establish rigor.

### Match evidence to the lifecycle stage

| Stage | Purpose and transition evidence |
|---|---|
| Speclet | Test the problem and proposed approach; proceed when evidence supports the next bounded investment, with gaps explicit |
| Kickoff | Agree scope, intended outcomes, resources, key risks, and validation plan; draft relevant stories and spikes |
| Solution Review | Review architecture, behavior contract, eval design, economics, and controls sufficiently to implement and test |
| Launch Ready | Verify checks required for the proposed exposure, monitoring, recovery, ownership, and applicable approvals; route the decision to `ship-decision` |
| Impact Review | Compare outcomes and harms with the original hypothesis; decide to iterate, scale, hold for more evidence, or retire |

Do not use the retired 8/16 AI-fit score or a fixed thirty-day significance claim to advance stages. Required launch checks and continuing post-launch evaluation are separate: “70% eval complete” says nothing about which necessary checks remain.

Use prototypes to test a stated question, then update the PRD with findings and constraints for the next round. A prototype's visible completion is not proof that the problem is valuable. AI may help draft when supplied with real context; accountable people still validate strategy, scope, accepted consequences, and evidence. Do not impose a blanket ban on AI first drafts.

Set review cadence by risk, change rate, volume, and feedback delay. Routine dashboards, representative review, segment audits, cost checks, prompt reviews, and model changes should lead to specific decisions. Refresh affected examples and backlog criteria after meaningful corrections; stable requirements do not need cosmetic weekly or monthly edits.

## Readiness review and handoff

Check that the PRD has:

- A clear problem, scope, user need, and appropriate AI rationale.
- User outcomes and system metrics with denominators, evidence, and triggered decisions.
- Material failure paths with detection limits, tested controls, recovery, and equipped owners.
- Relevant pre-exposure evaluation and regression results, including segment and adversarial coverage.
- Explicit evidence requirements, permitted actions, fallback behavior, and configuration versions.
- Coherent economics, stress cases, and a response to the cost ceiling.
- Instrumentation, external labels/joins where needed, privacy rules, and monitoring ownership.
- An exposure plan with meaningful advance, hold, and stop criteria and a usable recovery route.
- Traceable backlog coverage across the six applicable areas, without artificial duplicate requirements.
- Stage-appropriate open questions and a reviewer able to challenge missing assumptions.

Close with the actual recommendation, key trade-off, largest unresolved risk, and next decision/action. State what is provisional, reviewed, tested, or still blocked. Deliver the PRD, relevant example set and stories, and readiness evidence appropriate to the request. A diagram from intent through requirements to stories and production feedback can clarify the handoff; use it only when helpful.
