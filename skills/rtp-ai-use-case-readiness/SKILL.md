---
name: ai-use-case-readiness
version: v2.6.1_latest
description: 'Choose the least autonomous operating model that delivers the required value with acceptable risk, cost, and human workload. Use when assessing an agent proposal, deciding what AI may recommend or execute, or resolving a gap between desired autonomy and current controls. Follow five phases: ground the job, diagnose its subtasks with 12 questions, assess knowledge and control burden, set a practical autonomy floor and ceiling, and plan evidence-based rollout. Separate capability, permission, supervision, and economics; use the shared autonomy-spectrum labels with explicit action rights. The output is a testable recommendation, including prerequisites, critical assumptions, and conditions for changing it. Pairs with problem-ai-fit, determinism-compass, agent-risk, agent-spec, invisible-stack, and cost-model.'
imports:
  - first-principles
  - determinism-compass
  - autonomy-spectrum
---

# AI Use Case Readiness

Determine how much a system should do on its own for a particular use case. Recommend the simplest operating model that meets the user's needs with acceptable consequences, cost, and human workload. Compare manual work, deterministic automation, AI assistance, and bounded agents; more autonomy is not the objective.

The deliverable is a **readiness recommendation**: what the system may do now, who remains responsible, what evidence supports that boundary, and what would justify changing it. A score or an autonomy label does not authorize deployment.

## Separate the decisions before scoring

Four questions must agree:

1. **Capability:** can the proposed system perform this work reliably in the intended environment?
2. **Authority:** which decisions and actions may it take under the user's authorization and applicable policy or requirements?
3. **Control:** can failures be prevented, detected, contained, or recovered within the consequence window?
4. **Value:** does the benefit justify implementation, controls, operating cost, and the work retained by people?

A model's ability to call an API answers only part of the first question. Advice can also cause harm when people act on it. Human approval is a control only when the reviewer has relevant competence, evidence, time, and authority to intervene.

Identify hard boundaries before applying weighted criteria. An applicable prohibition or explicit values constraint cannot be averaged away by a high business-impact score. If the boundary is contested or changing, name the decision owner, current rule, and evidence needed to revisit it. A diagnostic does not resolve that dispute by itself.

Decompose a broad use case with `rtp-first-principles`; do not assign one level to a mixture of unrelated actions. If the question is whether AI is useful at all, use `rtp-problem-ai-fit`. If only a technical stack is needed, route to system design. Reuse existing customer grounding and the shared `UNIVERSAL-SKILL-PROTOCOL.md` at the AI-PM collection or plugin root.

## Five phases, scaled to the decision

Run **Ground → Diagnose → Assess → Decide → Plan**. Reuse evidence already available. A quick assessment may examine the relevant risks and one matrix, with its limitations stated. A full recommendation uses both matrices and addresses all 12 questions, recording unknowns rather than forcing answers. Use the output format the user needs; a comprehensive assessment does not automatically require a Word document.

### Phase 1 — Ground the job and opportunity cost

Establish:

- The specific user and job in their language.
- The current method, its outcomes, and what breaks.
- The problem's importance, frequency, and urgency relative to other work.
- Who bears the consequences of an incorrect, late, or missing result.
- The outcome worth improving, the alternatives considered, and what this investment would displace.

Pain rankings can guide prioritization, but a user's fourth-ranked problem is not automatically unworthy or unadoptable. A low-frequency task can still matter when consequences or strategic value are large.

For an early company still testing demand, the [lightweight qualification frame](references/opportunity-and-research.md) helps establish the opportunity first. It does not replace an autonomy assessment for consequential actions.

### Phase 2 — Diagnose the subtasks

Describe the trigger, inputs, outputs, actors, systems, permissions, success measure, and consequence of failure. Break the workflow into actions small enough to assign meaningful controls. A useful hybrid may combine extraction, rules, generated drafts, and human decisions.

**Map foundation dependencies early.** For each subtask, record the needed data, tools, schemas, models, integrations, and owners. Use these working categories without pretending they are mutually exclusive:

- **Low-foundation:** few specialized upstream dependencies; still dependent on ordinary runtime, access, and inputs.
- **Data-dependent:** relies on a particular source or pipeline whose absence, staleness, or failure affects the result.
- **Foundation-critical:** a shared platform, schema, model, or integration change can materially disrupt operation and therefore needs change coordination and validation.

A task may carry more than one tag. Define the actual dependency and change test; the label alone is not a readiness result. Classify per subtask after enough decomposition to see the dependencies.

**Answer the 12 diagnostic questions.**

| # | Question | What the answer must make clear |
|---:|---|---|
| 1 | What exact decision or action is delegated? | State what the system proposes, decides, or executes and what the person does. Separate producing a recommendation from authority to use it. |
| 2 | Is the mode advise, decide, execute, or execute with approval? | Name each approval point and its default. A timeout that proceeds is automatic execution after a delay, not affirmative approval. These modes are not a universal ranking of harm. |
| 3 | What happens if the result is wrong, late, or silently absent? | Assess each failure separately, including affected people, severity, frequency, and time before consequences occur. |
| 4 | When and how can correctness or safe operation be checked? | Distinguish pre-action verification, immediate detection, delayed outcome measurement, and uncertainty that cannot be resolved. Monitoring after harm is different from prevention. |
| 5 | Which parts use explicit rules and which need tacit judgment? | Examine real exceptions. Frequent overrides may indicate incomplete rules, changing conditions, poor inputs, or judgment that is difficult to codify. |
| 6 | How often do novel cases occur? | Estimate absolute volume at expected scale and identify their handling. An exception may be automatable; it does not necessarily need a person. |
| 7 | Can the environment change during execution? | Consider concurrent edits, stale reads, expiring permissions, changed business state, and partial completion. |
| 8 | Can a bad action be undone or its effects contained? | Name the recovery window and residual harm. Irreversibility strengthens the case for pre-action controls; it does not mechanically assign level zero. |
| 9 | What permissions and decision rights are required? | Specify scope, accountable owner, enforcement, and conflicts with current authorization or policy. Technical access is not sufficient authority. |
| 10 | What is the smallest bounded slice that still creates value or resolves a critical uncertainty? | Define the test population, action limits, duration, and what the pilot can establish. |
| 11 | What evidence can show outcomes and control performance? | Identify telemetry, sampling, independent checks, incident signals, and limits. Logging alone does not prove correctness. |
| 12 | Does the upside justify the complete control burden? | Include implementation, runtime, human review, maintenance, rework, incidents, and opportunity cost. Compare a credible lower-autonomy alternative. |

For consequential human checkpoints, test whether the intended reviewer can identify errors and choose the right response on representative examples. Stating an acceptance standard, sharing vocabulary, or editing frequently is not enough by itself. Direct production experience may help, but competent evaluation and production are different capabilities. `rtp-judgment-guard` develops this distinction.

Label assumptions **Validated** (measured in a stated setting), **Informed** (supported by relevant expert judgment), **Assumed** (plausible but untested), or **Unknown**. Validation has a scope and date; it is not permanent certainty. Prioritize the assumptions that would change the recommendation and expose the greatest consequence. Name the most concerning one and a concrete way to test it.

### Phase 3 — Assess the operating model

**Use the shared spectrum consistently.** `rtp-autonomy-spectrum` owns the library's seven labels. Use **0 — no AI/deterministic baseline** as an additional comparator, not as an AI maturity stage.

| Label | Useful shorthand | What still needs to be specified |
|---|---|---|
| 0 — Baseline | Manual work or deterministic rules without AI | Rules, permitted actions, monitoring, and responsibility |
| 1 — AI Feature | A bounded prediction or generation within a product | How code and users consume the output |
| 2 — Chatbot | A constrained conversational workflow | Whether routing is scripted and what it can actually do |
| 3 — AI Assistant | User-directed assistance | Task boundaries, tool access, and permitted actions |
| 4 — Copilot | Assistance embedded in a person's work | What the person reviews or approves before consequential use |
| 5 — Agent | Model-directed steps within defined boundaries | Scope, action permissions, checkpoints, stopping, and escalation |
| 6 — Autonomous Agent | Independent execution of a bounded job with outcome supervision | Verification, exposure limits, intervention time, and accountable ownership |
| 7 — Multi-Agent System | Several agents coordinate | Each agent's authority plus coordination and shared-state controls |

These are descriptive categories, not a validated numeric scale. Several agents can have less authority than one agent, and a chatbot can expose a consequential action. **Always state the operational contract alongside the number.** This version resolves the older readiness skill's conflicting 0–7 numbering; see the [migration crosswalk](references/level-crosswalk.md) when reading earlier assessments. Never silently reinterpret a saved number.

Start by comparing the baseline and assistive designs. Add model-directed planning only where it improves the job enough to justify its costs and controls. Deterministic software can already execute multiple steps; multi-step work alone does not establish the need for an agent. Anthropic's workflow/agent distinction is useful here. [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents).

**Matrix A — Knowledge × Cost of error**

| | Lower consequence | Higher consequence |
|---|---|---|
| Mostly explicit knowledge | Consider rules or a bounded AI component; verify the actual fit. | Consider controlled automation with strong input checks, pre-action verification, and appropriate review. |
| Substantial tacit judgment | Consider assistance or a bounded experiment with meaningful feedback. | Prefer a human-led or tightly constrained design until competent review and sufficient controls are demonstrated. A person in the loop is not automatically sufficient. |

**Matrix B — Need for agency × Control burden**

| | Lower control burden | Higher control burden |
|---|---|---|
| Low need for dynamic planning | Compare deterministic workflows and AI components. | Improve deterministic checks and checkpoint design; high risk does not create a need for an agent. |
| High need for dynamic planning | Consider bounded agent execution with tested limits. | Consider supervised planning, restricted actions, stronger verification, or narrower scope; defer unsupported execution. |

The matrices reveal tensions; they do not calculate a permitted level. If they suggest different designs, explain which consequence or control is binding. For the chosen dimensions, low/medium/high or anchored 1–5 ratings can structure discussion: tacitness, error cost, verification difficulty, irreversibility, variability, coordination, environmental change, consequence breadth, and decision-rights sensitivity. Do not average a severe subtask away or convert a decimal score into an autonomy level.

State four separate judgments: **need for agency**, **control burden**, **implementation effort**, and **economic leverage**. Give units, ranges, scope, and evidence. Monetary bands in earlier versions were illustrative; strategic or nonfinancial benefits need explicit outcomes too.

### Phase 4 — Decide the floor, ceiling, and hypothesis

The **floor** is the least independent operation needed to meet the stated value, timeliness, and workload requirements. It is not the intelligence required to understand the task. The **ceiling** is the greatest action scope supported by current capability, authorization, controls, and operating capacity.

State both as permissions and human responsibilities, then add the spectrum label if useful. Numeric comparisons are meaningful only within comparable operating modes. If the needed action scope exceeds what can be supported, choose among four responses:

1. Narrow the job, population, consequence, or service promise.
2. Build and test the missing controls or capability.
3. Retain a competent human step with realistic capacity and latency.
4. Defer or reject the unsupported use.

An assistive first phase is a valid destination, not a promise to become autonomous later. “Ready with controls” means the named controls must exist and pass their checks before the associated actions are enabled.

Look for **unnecessary agent design**: extraction or templated generation presented as planning; weak data blamed on reasoning; tool access mistaken for permission; internal eval success without an operational check; or costs that overwhelm benefits. Negotiation and relationship work require explicit ownership and limits, but using an agent does not inherently erase human accountability. The owner and actual decision rights determine that.

```text
HYPOTHESIS: [operating model / label] fits [job and bounded scope] because [evidence].
CURRENT RIGHTS: system may [actions]; person must [decisions]; prohibited [actions].
IF SUPPORTED: outcome, leading signal, and control measure over [sample / period].
IF CHALLENGED: contrary evidence, unacceptable consequence, and response.
DAMAGE IF WRONG: over-autonomy [harm]; under-autonomy [lost value / workload].
FLOOR / CEILING: required independence versus supportable action scope; gap and remedy.
PIVOT: expand only if [capability, value, authorization, controls]; restrict if [signals].
CRITICAL ASSUMPTIONS: evidence level, scope, owner, test, and decision date.
MOST CONCERNING ASSUMPTION: [what could overturn the recommendation].
```

Set thresholds for this use. A fixed acceptance rate, six-month trust-recovery claim, or generic “zero critical errors for four weeks” does not establish readiness.

### Phase 5 — Plan operation and evidence-based rollout

Choose a readiness band: **Ready now**, **Ready after named controls**, **Assist-only now**, **Not an AI fit**, or **Insufficient evidence**. State why a simpler design falls short, why greater autonomy is unsupported or unnecessary, and what remains uncertain.

For independent agent execution, establish five conditions: a demonstrated reason for dynamic planning; safely scoped action rights; verification or other effective prevention, containment, and recovery; acceptable consequence exposure; and sufficient value after operating costs. Reversibility alone is not permission, and a dollar amount or user count cannot serve as a universal harm limit.

Phase by evidence, not by the calendar or an obligation to climb the spectrum:

| Phase | Learn or deliver | Specify before starting |
|---|---|---|
| Assistive or shadow test | Task quality, reviewer performance, usefulness, and likely workload | Representative cases, allowed data, safe exposure, evaluation, and limits of shadow evidence |
| Bounded execution | Whether scoped actions deliver value under real controls | Permissions, approvals, fallback, audit trail, monitoring, exposure limits, and response owner |
| Sustained operation or expansion | Whether value and control performance hold across the intended conditions | Capacity, change tests, incident response, maintenance, and explicit expansion criteria |

Not every use needs every phase. For each chosen phase, define its hypothesis, baseline, sample, duration, owner, allocated time, control checks, stop conditions, and decision at exit. Confirm that people assigned to review or run the pilot can actually do so. A sponsor or signature without time and authority is insufficient; formal performance-review inclusion is one possible support, not a universal prerequisite.

Keep approval, policy enforcement, evaluation, monitoring, recovery, auditability, and a tested stop mechanism proportionate to the actions. Plan review throughput before volume creates pressure to remove it. Test interruptions, stale state, partial completion, and escalation—not only successful runs. Do not treat an intentionally appropriate escalation as a defect to minimize unconditionally.

At a stable 0.1% per-task error rate and 10,000 tasks, the expected count is 10 errors. This is a volume calculation, not evidence that errors compound or that the rate is acceptable. Severity, correlation, detection, and clustered incidents still matter. A period with zero observed failures does not prove zero risk.

## Keep adjacent questions in their proper place

- **Opportunity and adoption:** the Speed–Problem–Results–Implementation–Niche–Trust frame helps qualify demand. A helpful product is not necessarily ready for independent action.
- **Workforce capability:** test the intended users' actual judgment, correction, and outcomes. Neither a job title nor paste-through alone proves expertise or its absence.
- **Competitive advantage:** readiness may reveal reusable organizational capability. Call it a moat only after testing value, differentiation, imitation, and durability; vendors can supply parts of many capabilities.
- **Portfolio sequence:** economic visibility, repeatable processes, and unresolved judgment needs help screen candidates. They do not prove procurement or any other function should always go first. Consequence and readiness can outweigh breadth or demand.
- **New work:** compare before/after tasks at a meaningful level of detail. Helping an existing task is distinct from creating a new one. Wage, employment, and expertise effects require additional evidence.

The [research and opportunity reference](references/opportunity-and-research.md) preserves these lenses, cases, and their evidentiary limits. The [concept guide](CONCEPT.md) provides worked examples without presenting hypothetical savings as measured results.

## Handoff and final check

Upstream, `rtp-opportunity-solution-tree` identifies the opportunity and `rtp-problem-ai-fit` tests the role of AI. Reuse their findings. `rtp-determinism-compass` identifies stable rules and verification needs. Data ownership, recency, reuse, and availability may also require `rtp-build-or-buy` and `rtp-moat-finder`; this assessment must record its own dependencies rather than assume the foundation exists.

Downstream, pass the action contract, level vocabulary, customer grounding, floor/ceiling, critical assumptions, and operating evidence to `rtp-invisible-stack` and `rtp-agent-spec`. They turn the recommendation into architecture, permissions, checks, escalation, and recovery. `rtp-cost-model` prices the full operating design. `rtp-agent-risk` tests proportionality and consequence boundaries; `rtp-ship-decision` uses that evidence for release. Unverified confidence thresholds must not become permissions during handoff.

Before concluding, confirm that consequential subtasks were assessed separately, foundation and reviewer dependencies are named, both matrices were used for a full assessment, unknowns remain visible, and the proposed pilot has an owner with capacity. If a stakeholder has already chosen full autonomy, present the evidence and unresolved decision rights; do not claim a diagnostic is powerless or disguise disagreement as a score.

Lead with the recommended operating model and readiness band, the main tradeoff, the assumption most likely to change the call, and the next action with its owner. Use a per-action table, matrix, or floor/ceiling diagram when it helps the audience; do not add every possible visual by default.
