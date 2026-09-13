# AI product requirements template

Revision 1.1, 13 September 2026. Companion to AI-PRD v1.2.1.

Use this template to connect the user problem to product behavior, evidence, costs, launch decisions, and implementation. Keep §0–13 identifiers for traceability. Reuse the team's existing format where it provides the same decisions. Link detailed examples, architecture, and stories rather than repeating them.

The running example, **Athena**, is a fictional draft-only support assistant. All figures below are illustrative assumptions or proposed criteria, not measured results. Replace them with appropriate evidence before the decision that depends on them. Roles are placeholders for assignment, not named people who have approved the work.

## Contents

0. Header and decision summary
1. Opportunity
2. Boundaries
3. Users and job
4. Behavior contract
5. Solution and architecture
6. Success measurement
7. Probabilistic behavior
8. Rollout and experiment
9. Risk and incident response
10. Instrumentation
11. Economics
12. Lifecycle and launch
13. Questions and decisions

Use available discovery, strategy, readiness, architecture, evaluation, safety, observability, and cost work as inputs. Resolve conflicts and stale evidence; a missing upstream artifact is not proof that no useful work can begin. Record consequential gaps in §13.

## 0 Header and decision summary

Record feature, stage, owner and assignment status, document/configuration version, date, recommendation, supporting evidence, unresolved restrictions, and links to prototype, evals, stories, runbook, and results.

**Athena example:** Stage: Speclet. Owner: PM role, assignment pending. Recommendation: test whether reviewable reply drafts reduce routine-ticket handle time without reducing response quality. Proposed target: 15% lower handle time; proposed fully allocated cost target: $0.04 per verified resolution. No production exposure is approved by this example. The proposed stop mechanism and its response time still need testing.

## 1 Opportunity

State the problem, working hypothesis, strategy fit, reason to consider AI now, alternative approaches, expected impact, and prototype findings. Sources: discovery, `jtbd-analysis`, `strategy-canvas`, `problem-ai-fit`, and `cost-model`.

**Athena example:** Suppose support agents spend 4.2 minutes composing a routine reply across 480,000 routine tickets a year. At $0.90 per minute, a 15% reduction represents 302,400 minutes and $272,160 of annual labor capacity. It is not automatically cash savings or realized benefit. Check adoption, review time, rework, volume, and whether freed capacity can be used.

The hypothesis is that source-linked drafts reduce this time while preserving quality. Compare against templates, better retrieval, and workflow changes. A prototype session with five agents could reveal whether timing, tone control, or editing matters; it cannot establish population-level benefit. Record what was actually observed and what remains assumed.

**Seeds:** the capability story's user outcome and the impact-review comparison.

## 2 Boundaries

Define scope, non-goals, resources, accepted trade-offs, actual permissions, and conditions that limit use. Sources: `autonomy-spectrum`, `ai-use-case-readiness`, and `agent-spec` where applicable.

**Athena example:** English routine-ticket drafts in the support console; staff review and send through the existing authorized workflow. Athena can read permitted ticket/order/knowledge-base records and prepare text. It cannot send replies, issue refunds, change subscriptions, or create new customer commitments.

Voice, additional languages, knowledge-base authoring, and employee performance scoring are outside this initial experiment. Exclusion is a scope choice, not a claim that these users or channels are unimportant. State how unsupported cases receive normal service.

Use **Copilot, shared library Level 4**, if a broader label helps; the draft-only permissions above control. High acceptance or short review time does not automatically change authority or prove careless review. Audit the quality of accepted drafts before drawing that conclusion.

**Seeds:** capability boundaries and relevant guardrail requirements.

## 3 Users and job

Describe users, their task, unmet need, access constraints, and the evidence behind each segment. Sources: `jtbd-analysis`, `attitudinal-segmentation`, and `interview-synthesis`.

| User group | Need to investigate | Design hypothesis |
|---|---|---|
| Experienced support staff | Preserve judgment and quality while saving drafting time | Editable drafts and inspectable sources may help |
| New support staff | Understand policy and avoid unsupported commitments | Contextual guidance and appropriate review may help |
| Team leads | Understand quality, workload, and exceptions | A representative quality report and recovery visibility may help |

Do not assume tenure determines AI attitude. Test these needs and provide useful controls without forcing “skeptics need explanation” or “enthusiasts need friction” as universal rules.

## 4 Behavior contract

Assign stable IDs. Record input/context, authorization, expected behavior, acceptable variation, source/provenance, and the error or boundary the example tests. Label constructed cases. A set of 15–25 examples can start a substantial contract; scope and coverage matter more than count.

**G1 — Verified order status.** In a test fixture, the authorized order record states shipment on 3 March with a tracking reference. The draft accurately summarizes that record and links the available tracking source. It does not invent an arrival date when none is supplied.

**G2 — Confirmed refund already issued.** The fixture includes an authorized, completed refund record. The draft may accurately say the refund was issued and use the recorded reference and supported timing. Athena itself did not issue it.

**B1 — Duplicate-charge assumption.** Two equal charges appear on different dates. A draft declares one a duplicate and says a refund has started without evidence. Correct behavior: identify the observed charges, preserve uncertainty, and help the support agent follow the authorized investigation process.

**B2 — Unsupported reassurance.** No shipment record is available, but the draft claims the order will arrive tomorrow. Correct behavior: state the evidence gap and suggest the permitted next check; do not manufacture certainty.

**R1 — Action outside authority.** A ticket asks for a $10,000 refund. Athena does not execute it. The draft or internal guidance points staff to the applicable refund policy and authorized review route. Any approval limit or response-time promise must come from actual policy and capacity.

**R2 — Restricted legal request.** A fixture triggers the organization's defined legal-handling policy. The product routes the affected work to that process and explains the limitation to the support agent. A legal keyword alone is not a universal reason to suppress all assistance.

Wording may vary; facts, permission scope, and commitments must remain supported. Link these examples to relevant tests and stories. Maintain an independent evaluation set when measuring generalization.

## 5 Solution and architecture

Describe the approach, alternatives considered, rule/model map, data and context boundaries, dependencies, prompt/configuration versions, and recovery. Sources: `build-or-buy`, `determinism-compass`, `context-spec`, `prompt-as-product`, and `prompt-craft`.

**Athena example:** retrieve permitted ticket, order, and knowledge-base context; generate a draft; check relevant content and authorization constraints; display for staff review. Retrieval may include learned ranking, intent gating may use a classifier, and safety checks may combine rules and models. Identify each actual implementation; do not describe the entire path as having only one probabilistic stage.

Version prompts and relevant context/index/model/tool settings. Malformed-output retries are bounded and cannot expand permissions. If valid drafting is unavailable, preserve the original ticket and the support agent's normal workflow.

## 6 Success measurement

Define offline, human-review, and online evidence. For every metric, record denominator, population, baseline, sampling, window, uncertainty, owner, and the decision it supports. Sources: `eval-framework`, `confidence-tuner`, and `ai-product-metrics`.

**Offline plan:** build representative cases by intent, difficulty, relevant user/context segment, and risk. A 500-case design with adversarial and rare-intent cases is a planning example, not sufficient evidence by itself. Validate labels and automated judges; separate prompt-tuning examples from held-out tests. Use discrete checks for unsupported commitments and suitable rubrics for tone and usefulness.

**Human review:** sample accepted, edited, discarded, and fallback cases. Define how reviewers assess factual support, usefulness, permissible commitments, and task outcome. Resolve disagreement and record missing labels. Choose reviewer count and cadence from the question and risk rather than a fixed 50-per-week rule.

**Online decision examples, all provisional:**

| Measure | Proposed criterion | Action and interpretation |
|---|---|---|
| Routine-ticket handle time | Target 15% reduction; proposed graduation minimum 10% | Compare with control and review uncertainty, quality, and adoption before advancing |
| Response quality and CSAT | Pre-agreed noninferiority margins | Hold expansion if evidence crosses the limit; failure to detect a difference is not proof of equivalence |
| Unsupported factual claims | Defined claim- or draft-level limit | Investigate and contain according to severity; one severe incident can justify action |
| Calibration, if a score is used | Validated error bound by relevant group | Reassess evidence policy if calibration changes |
| Draft latency | Proposed P95 at most 2 seconds | Review degraded paths if sustained breach affects usefulness |
| Full cost per verified resolution | Target at most $0.04; review above $0.06 | Validate denominator and allocation, then consider cost or scope changes |

Acceptance and review speed are supporting signals. Include audits of accepted-but-wrong outputs; a declining exception rate can mean fewer errors or weaker detection. The same metrics do not identify which explanation is true.

## 7 Probabilistic behavior

Specify the evidence needed to display a draft, request targeted review, show source material, or pause the affected path. Sources: `confidence-tuner`, `ai-ux-patterns`, and `trust-ladder`.

**Athena candidate policy:** where a score estimates a defined quality event and has been calibrated, test bands above 0.85, 0.70–0.85 inclusive, and below 0.70. These might correspond to a normal reviewable draft, a draft with a specific uncertainty highlighted, and no generated draft with useful permitted source material instead. The thresholds remain provisional until validated. Without a useful score, use required evidence checks.

All bands remain draft-only. A safety or permission failure takes precedence. Source snippets must themselves be authorized, relevant, and safe to show. A timeout may lead to one bounded retry, an approved template, snippets, or normal manual handling; test each alternative rather than assuming every lower rung is safer. If a fallback is unavailable, explain that state honestly.

Report quality by relevant segment with estimates and uncertainty. Rare cases are not automatically safe to handle at a lower standard. Refusal volume triggers investigation, not an automatic threshold reduction.

## 8 Rollout and experiment

Define the question, proposed exposure, evaluation design, duration/evidence needs, advance/hold/stop criteria, and budget authority. Sources: `gen-ai-experimentation` and `ship-decision`.

**Athena example:** a shadow phase can test operation on real inputs without displaying drafts, subject to privacy, cost, and access requirements. It cannot directly measure user acceptance or causal effects on handle time. A subsequent controlled exposure measures those outcomes.

If staff share queues, consider team-level assignment and evaluate spillovers, number of teams, and clustering in the power calculation. An illustrative 5% → 25% → 50% → 100% exposure sequence is not a schedule commitment. Set minimum evidence, duration, guardrails, and operational capacity for each step. A proposed 8% minimum detectable change at 80% power requires actual baseline variance and cluster assumptions; percentages alone do not size the study.

Define handle-time reduction as `(control − treatment) / control`; a proposed graduation criterion is **at least 10% reduction**, alongside quality and cost requirements. Avoid the reversed rule “handle time ≥ −10%,” which could admit a slowdown. Assign budget approval according to real delegated limits, not an arbitrary ramp percentage.

## 9 Risk and incident response

Sources: `failure-modes`, `agent-risk`, `safety-by-design`, `responsible-ai-program`, and `breach-ready`.

| Failure | Detection and limitation | Containment and recovery |
|---|---|---|
| Unsupported fact or commitment | Source checks, representative review; fluent text may evade a judge | Restrict affected draft path; correct affected material and follow actual customer communication authority |
| Cross-customer disclosure | Isolation tests and authorized canary fixtures; generic PII matching is insufficient | Block affected access/output, preserve proportionate evidence, invoke privacy/incident process |
| New terminology or changed policy | Fresh samples, task-mix and source-freshness checks | Correct the relevant data/context/policy and verify before restoring affected use |
| Inadequate review | Audit accepted-output correctness plus review context | Improve workflow, evidence, training, or permissions according to findings |
| Tool injection or unauthorized action | Boundary and exfiltration tests, action logs | Enforce permissions before effects; stop and reconcile any uncertain action |

Name the incident owner, backup coverage, intervention rights, and expected response. A proposed disable-within-60-seconds target must define which effects stop and be tested. Stopping future drafts does not erase drafts already shown or reverse staff actions. Choose safe drill environments and controlled production drills only when justified and authorized.

Record applicable privacy, legal, security, and contractual requirements, with competent review where needed. A draft promise is not universally binding or universally harmless; its treatment depends on context. Reviewers need capacity and useful incentives, not an error-catching quota.

## 10 Instrumentation

Sources: `ai-product-metrics` and `production-observability`.

Define applicable events such as draft generated, eligible, shown, opened, edited, sent, discarded, fallback, and corrected. Include safe identifiers, version/configuration references, authorized source references, decision/evidence status, elapsed latency, tokens/billing basis, and relevant user action. Derive latency percentiles over a defined population; individual events do not have their own P95.

The funnel may be Eligible → Shown → Opened → Accepted → Sent → Verified outcome. Specify denominators, missing events, deduplication, and joins. CSAT, factual labels, and resolution may need survey, human-review, or ticket-system data; they cannot necessarily be computed from model logs alone.

Set access, retention, sampling, redaction, and deletion rules. Store raw text, keystrokes, or personal data only when justified and permitted. A model-generated confidence field is optional when no useful score exists.

## 11 Economics

Source: `cost-model`; connect to `token-economics` if the feature is priced externally.

**Coherent planning example:** 480,000 annual draft attempts over 250 operating days equals 1,920 attempts/day. Suppose 80% lead to a verified resolution: 1,536/day. Include the costs of all attempts, failures, review, and applicable overhead in the numerator.

| Scenario | Draft attempts/day | Verified resolutions/day | Assumed full cost/resolution | Implied full cost/day |
|---|---:|---:|---:|---:|
| Baseline | 1,920 | 1,536 | $0.031 | $47.616 |
| 10 times volume | 19,200 | 15,360 | $0.024 | $368.64 |
| 100 times volume | 192,000 | 153,600 | $0.020 | $3,072 |

These are internally consistent **assumptions**, not a bottom-up cost estimate. Validate each cost rate against the real mix of input/output tokens, tools, retries, evaluation, infrastructure, staff time, and fixed allocations. The growth rows assume economies that must be demonstrated.

At baseline, the implied annual full cost is $11,904. If a separate estimate says $95,000/year, the full cost per 384,000 annual verified resolutions is about **$0.2474**, which fails the $0.04 target. Resolve this conflict; do not label a variable-cost subtotal as the full cost. A previous $260/day estimate over 1,900 attempts also cannot yield $0.031 per resolution within that same workflow.

State the cost ceiling, review window, and response. Test price shocks and usage/review changes. Define any P90 scenario or per-outcome distribution explicitly; do not confuse it with the average above. Compare realized benefit with cost on a consistent scope and period.

## 12 Lifecycle and launch

Match requirements to the decision and risk:

- **Speclet:** problem, hypothesis, alternatives, a small behavior set, bounded next test, and open questions.
- **Kickoff:** agreed scope, resources, intended outcomes, material risks, and validation work.
- **Solution Review:** architecture, behavior contract, tests, telemetry, fallbacks, economics, and exposure design.
- **Launch Ready:** required evaluation and safety/validity checks passed for the proposed exposure; monitoring, owners, recovery, and actual approvals ready.
- **Impact Review:** results versus original hypothesis, harms, costs, surprises, and a decision to iterate, scale, hold for evidence, or retire.

Monitoring needed for safe exposure is ready before that exposure. Continuing evaluation after launch is not permission to skip a required check. Review timing follows evidence accumulation and consequence; thirty days does not guarantee significance. Prototype findings update the PRD and the next experiment. Stable criteria need no arbitrary monthly rewrite.

## 13 Questions and decisions

| Question or assumption | Evidence status | Responsible role | Needed before | Resolution and effect |
|---|---|---|---|---|
| Does reviewable drafting save meaningful time? | Provisional hypothesis | PM / research | Expansion decision | Link result and resulting choice |
| Is team assignment sufficient to control spillover? | Needs queue and workflow evidence | Experiment owner | Controlled exposure | Record design and limits |
| Is the cost target feasible on a full allocation basis? | Scenario assumption | Finance / engineering | Budget and launch decision | Reconcile estimates |
| What can drafts say about refunds and legal requests? | Actual policy needed | Authorized policy owner | Affected use | Link policy and behavior examples |

Record dates when agreed, assignment gaps where real, sources, and what new evidence would change the decision. “Verified” means a claim was checked against suitable evidence, not that every future outcome is certain.

## Appendix User story handoff

Use [AI user stories](ai-user-stories.md) for the six coverage areas and worked items. Each item links the applicable decisions, evidence, ownership, monitoring/change trigger, cost implication, and unresolved assumptions. Shared requirements can be referenced; unnecessary copies can drift apart.

Measure User Story Health over defined reviewed items and applicable requirements. Complete documentation supports readiness but does not prove a safe or successful product. Send §6/§12 evidence to `ship-decision`, §7 to UX/trust work, §10 to observability, and §1 results to the retrospective.

The [evidence notes](prd-evidence.md) distinguish source guidance from this library's examples and design choices.
