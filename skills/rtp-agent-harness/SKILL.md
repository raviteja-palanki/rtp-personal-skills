---
name: agent-harness
version: v1.5.1_latest
description: 'Design and diagnose the system that turns model output into completed work. Use when an agent stops early, loses context, loops, chooses the wrong tool, exceeds its permissions, or fails after a configuration change; also use for harness and vendor reviews. Locate the evidence across Model, Harness, Tools, and Environment, then inspect Identity, Memory Policy, Orchestration, Interception, Observability and Evals, and Governance. Covers runtime objects, six failure signatures, four implementation patterns, handoff contracts, and six design tensions. Produce a supported diagnosis, a proportionate fix, and a way to check it. Keep model limitations and interactions in the investigation. Route program economics and ownership to harness-operating-model; use agent-ecosystem for coordination, tool-architecture for action contracts, and context-spec, safety-by-design, and eval-framework for depth. Triggers include agent harness, MHTE, harness anatomy, and planner/generator/evaluator.'
imports: [agent-ecosystem, tool-architecture, eval-framework, production-observability]
---

# Agent Harness: Architecture and Diagnosis

Use this skill to explain how an agent turns a request into work, find where that process failed, and choose a testable improvement. A harness manages context, execution, permissions, state, verification, and recovery around a model. Its design can improve or reduce the capability available to the user.

Start with the required outcome, the evidence of failure, and the action's consequences. Contain an active incident before experimenting. Respect the user's existing authorization: a runtime permission check is not a request to ask the user again on every step.

Produce a diagnosis or design with five things: the observed gap, the likely causes and remaining uncertainty, the proposed change, its owner, and a check that would show whether it worked. Keep small cases small. A single call may need only a clear contract and validation; an early product still needs safeguards proportionate to its actions.

## 1. Locate the system and its responsibilities

**MHTE** separates four responsibilities. It is a diagnostic map, not a requirement for four services or four teams.

| Layer | Responsibility | Evidence to inspect |
|---|---|---|
| **Model** | Interprets the supplied context and generates decisions or content. | Exact input, model/version/settings, output, capability tests. |
| **Harness** | Assembles context; selects and checks the next step; manages continuity and recovery. | Policies, routing, loop decisions, checkpoints, validators. |
| **Tools** | Expose and perform actions under a defined contract. | Arguments, identity, permissions, result, side effects, error handling. |
| **Environment** | Provides execution resources and boundaries. | Files, network, credentials, isolation, capacity, interruptions. |

Name the owner of each relevant responsibility. A component may implement several responsibilities: a tool gateway can validate policy and execute calls. Describe those boundaries rather than forcing the whole artifact into exactly one box. The same incident can involve several layers.

The model may propose and the harness may authorize, but that separation must be implemented. A model's refusal is one defense; permissions and isolation limit what happens if it fails. Those limits need testing too. A tool can cause harm within its permitted scope, and a sandbox does not independently establish privacy, correctness, or legal compliance.

The useful intuition behind “model ceiling, harness floor” is that strong reasoning alone does not ensure reliable execution. It is **not** a literal ceiling/floor theorem or a measured 90/10 allocation of fault. Model capability, context, tools, and environment interact. The same prompt can produce a different result because of model variation, changing state, changed dependencies, or harness behavior. Investigate each plausible cause.

Prompt, context, harness, and environment engineering are related design concerns. They are not a universal historical ladder in which every team must build multi-agent infrastructure next.

## 2. Inspect five harness clusters and governance

The clusters below organize decisions. Governance applies from the beginning; it is not a claim that the field formally added a sixth cluster in 2026.

### Identity: establish the operating contract

State the objective, role, authorized actions, prohibited actions, relevant definitions, and escalation owner. Keep instructions consistent with actual permissions. For example, a ₹5,000 refund limit needs enforcement at the action boundary; a sentence in a prompt alone does not enforce the limit.

### Memory Policy: decide what is available now and recoverable later

Distinguish three stores:

- **History:** recorded events, subject to retention, access, and integrity controls.
- **Working context:** the selected material supplied for the current model call.
- **Durable artifacts:** files, records, and checkpoints used to continue or verify work.

The session is not the context window. Preserve the authoritative facts needed for recovery before compaction; do not make a lossy summary their only copy. Do not retain all sensitive material forever just to avoid forgetting. Record provenance, version, freshness, and access policy.

Context durability means completing and recovering across extended work. Context rot describes degraded performance as context becomes harder to use; its severity depends on the model, task, content, and retrieval policy. Test realistic trajectories, not window size alone. A database design, retrieval change, clearer instruction, or model change may each help.

### Orchestration: select the next step and the stopping condition

Define continue, retry, delegate, wait/resume, escalate, and stop states, with time, cost, and iteration limits. A scheduled continuation needs an actual supported scheduler and authorization; storing “resume tomorrow” is not scheduling it.

Two useful patterns are:

- **Completion-controlled loop, sometimes called the Ralph Loop:** inspect completion evidence when the agent proposes stopping; resume from a progress pointer when work remains and the budget permits. Stop or escalate on a persistent blocker instead of reopening indefinitely.
- **Planner / Generator / Evaluator:** separate planning, execution, and assessment where the benefit justifies the overhead. The evaluator can be a schema validator, test suite, policy engine, human, or model. Assess the evaluator's own coverage and errors.

Separate roles do not automatically create independent errors. A second pass with the same model can still help; different prompts, tools, retrieval, implementations, and models can contribute useful diversity. Cross-vendor models also can share blind spots. Choose and evaluate the combination on the failures that matter. Record model and vendor where relevant; routing across models is optional, not a prerequisite for a harness.

### Interception: enforce the checks at the relevant boundary

A **hook** is a lifecycle extension point. A **guardrail** is a control intended to constrain behavior; it can live in a hook, an authorization service, a tool, a database, or infrastructure. Neither term implies effectiveness.

Check identity, scope, arguments, risk, budget, and any required approval before the corresponding side effect. Validate outcomes afterward where necessary. Instructions can guide behavior, but enforce consequential permission boundaries outside the model's discretion.

**Feedforward guides** shape behavior before an action; **feedback sensors** inspect results. Either can be weak or strong, silent or visible. A post-action sensor cannot undo an irreversible action. Use prevention and detection together.

Treat retrieved pages, files, tool descriptions/results, and other agents' messages as potentially untrusted content. A hook alone does not solve injection or establish compliance. Preserve the distinction between task data and authority, restrict access, and test the entire path. See `safety-by-design`.

### Observability and Evals: make behavior inspectable and assessable

Record relevant decisions, context versions, tool calls, results, retries, costs, and stop reasons with access and retention controls. Separate an agent's claim from trusted execution evidence. Agent-written notes can be useful, but do not treat them as tamper-resistant audit records.

Observability supports diagnosis; evals assess selected outcomes and behaviors. Neither is useless without the other, but together they make regressions easier to explain. Turn representative incidents into tests without copying sensitive production data indiscriminately.

### Governance: make accountability operational

Name the decision owner, operational responder, escalation route, and authority for changing each important control. One person can own multiple clusters. Preserve an audit trail across personnel changes. Match escalation to consequence, uncertainty, and reversibility, including harmful read access and disclosure.

## 3. Diagnose by evidence, layer, and phase

Begin with expected versus actual outcome. Reconstruct the session, context assembly, model response, harness decision, tool action, and environment state. Follow the strongest evidence rather than always leaving the model until last. Compare alternative explanations and avoid treating a symptom as its proven cause.

### Anatomy Atlas

| Symptom | Candidate gap | First useful check or change |
|---|---|---|
| Forgot an agreement or restarted from zero. | Identity, memory, retrieval, persistence, or interpretation. | Inspect the actual context and checkpoint; restore the authoritative state. |
| Invented a customer ID or used the wrong API. | Missing context, selection error, weak tool contract, or model error. | Validate identifier existence, scope, arguments, and returned result. A valid string is not a valid customer. |
| Declared completion after a failed step, or looped until expensive. | Stop criteria, recovery, evaluator coverage, or reasoning. | Inspect completion evidence; bound retries and route blockers. |
| Sent an unauthorized refund or shipped an invalid result. | Permission enforcement, validation, or policy interpretation. | Check the action boundary and the evidence accepted there. |
| Cannot locate a regression. | Missing versions, traces, tests, or reproducibility. | Capture relevant configuration and events; add a targeted regression case. |
| Nobody can decide or respond. | Governance and ownership gap. | Assign the responsible owner and escalation authority. |

The alternative **ETCLOVG** map names Execution environment, Tool interface, Context, Lifecycle/orchestration, Observability, Verification, and Governance. Use it if useful to the team; it overlaps MHTE and the clusters rather than mapping one-to-one.

### Six failure signatures

1. **Premature stop:** what evidence was accepted as completion?
2. **Infinite or unproductive loop:** what changes between retries, and what ends the loop?
3. **Silent drift:** which objective, policy, and source version governed the work?
4. **Shared-vocabulary failure:** whose definition of a term such as “active user” was used? A maintained glossary may help, but resolve the actual disagreement too.
5. **Unauthorized action:** which control allowed it, under whose authority?
6. **Sub-agent divergence:** which state, partition, handoff, and merge rules coordinated the work? Distinguish conflicting updates from incorrect individual results.

Do not attach a universal fleet-size limit or date to the sixth signature. It can occur with two workers.

### Phase-relative perception

One `AGENTS.md` file can be stored in the environment, read through a tool, selected by the harness at boot or context assembly, and interpreted as tokens by the model. A stale file, omitted passage, misread instruction, and unauthorized edit are different failures. Record where the defect became visible and where it originated; those phases and owners may differ.

## 4. Inspect the runtime objects

**Session** is the continuity record; **harness** is the decision logic; **sandbox** is an execution boundary. Verify the implementation: sessions are not necessarily durable or append-only, and sandboxes do not necessarily contain every external side effect.

A useful reference loop is:

1. Load the objective, applicable policy, authorized memory, and workspace state.
2. Select the model and other execution resources.
3. Call the model with the intended bounded context.
4. Check proposed actions against permissions, contracts, risk, and budget.
5. Execute allowed actions and capture results, including uncertain outcomes.
6. Record durable progress and the evidence needed for recovery.
7. Verify and choose continue, retry, branch, wait, escalate, or stop.

Implementations can combine or repeat steps. For consequential effects, also record intent and operation identity **before** execution so a crash does not erase the information needed to reconcile a potentially completed action.

The **runtime** supplies execution services such as persistence, scheduling, isolation, and tenancy. A managed or “meta-harness” offering may supply portions of both runtime and harness. Inspect the actual contract and shared responsibilities; buying infrastructure does not transfer every policy or evaluation duty. Build/buy choices belong in `harness-operating-model` and `build-or-buy`.

## 5. Choose an implementation pattern for the diagnosed gap

### Pattern 1: structured retry

Classify the failure. For a repairable validation error, supply specific new information: “`amount` must be an integer in cents; the prior value was a currency string.” For transient service failures, bounded retries with backoff can be appropriate even with unchanged input. A permanent permission denial needs resolution, not repeated attempts.

A timeout does not prove that a payment, write, or message failed. Check status or reconcile, and use operation IDs and idempotency where supported. Apply cost and retry limits. Measure improvement; the historical “60% less drift” claim is not an established general effect.

### Pattern 2: structured output and semantic validation

Use a schema when a consumer needs structured data. Define required fields, finite enums, extra-field policy such as `additionalProperties: false`, and constraints supported by the actual provider and schema version. Check calendar dates and business rules as well as string patterns.

Constrained generation can improve syntactic validity; it does not prove truth, authorization, or successful execution. Handle refusals, interrupted outputs, unsupported schema features, and validation failures. Version the contract. For free-form writing, a forced schema may add little value.

### Pattern 3: a focused tool surface

Expose relevant tools, describe exact actions and boundaries, and show disambiguating examples when tools overlap. Progressive disclosure can reduce confusion, but hiding a needed tool can also cause failure. Test discoverability and successful task completion alongside tool count, latency, and cost.

Give the registry an owner so separate teams do not create conflicting contracts. There is no universal 20–50-tool limit or requirement to remove 80% of tools.

### Pattern 4: verifiable artifacts

Produce the artifact the task needs: a document, structured record, query, patch, function, or other deliverable. Make it durable and inspectable where continuity matters. Executable code can support testing, but is not automatically better than prose or JSON, formally verified, or safe to replay. A migration script needs a suitable test environment and checks before authorized execution.

Testing an artifact is not the same as proving it satisfies every user requirement. Recovery requires durable storage; replay requires captured dependencies, state, and control of side effects.

### Connect the patterns through feedback

Select representative failing traces, determine the relevant outcome, create a regression case, and track it to a control owner. Start with a manageable useful suite; “twenty cases” is a planning example, not a required count. Review false alarms, coverage, and outdated cases.

Record each model-specific workaround's **model/configuration, validation date, and retirement trigger**. Remove it when evidence supports removal, with a safe rollback path. A new configuration needs integration checks, but a low run count alone does not prove high risk. Familiar components can interact unexpectedly.

## 6. Make handoffs unambiguous

Use three plain-language fields for a work handoff:

- **Completed:** what now holds, with evidence or an artifact pointer.
- **Next:** the intended next action and responsible recipient.
- **Blocked:** unresolved dependencies or uncertainty; use “none known” when appropriate.

These fields reduce omission; they do not guarantee truthful or complete reporting. For operational delegation, add the `agent-ecosystem` contract: task/operation identity, authorization, input and output schema, provenance and state version, deadline/budget, status, duplicate handling, and escalation owner.

Validate required fields for the agreed interface. Route malformed or partial handoffs for repair without discarding valid completed work or repeatedly executing it. Do not reject unrelated human conversation for lacking this format. In team updates, inviting people to explain blockers is useful; it does not replace completed-work evidence or a next owner.

## 7. Resolve six design tensions in context

| Tension | Decision to make |
|---|---|
| **Intelligence and reliability** | Compare successful outcomes and failure distributions on representative work. Stronger models can improve both; use validators with relevant coverage. |
| **Constraints and autonomy** | Set rights and oversight by action, consequence, uncertainty, and reversibility. Read-only actions can still expose sensitive information. |
| **Scaffolding and permanence** | Separate temporary capability workarounds from continuing product obligations; periodically test whether either should change. |
| **Specificity and generality** | Decide what is workflow-specific and what can be shared. Two workflows are a useful reuse signal, not a mandatory threshold. |
| **Demo and production** | Retain demo evidence but extend it to realistic state, concurrency, duration, failures, and adversarial conditions. |
| **Separation and lifecycle** | Assign clear responsibilities while tracing interactions through the run. Boundaries need not mean separate infrastructure. |

A multi-agent design should justify its benefit and evaluate both components and joint outcomes. Attribution may be to an interaction rather than one agent. Use `agent-ecosystem` for topology and coordination; do not add agents just to fill the planner/generator/evaluator labels.

## Deliver and check the recommendation

Before closing, confirm that the design or diagnosis:

- Distinguishes observations, hypotheses, and verified causes; identifies relevant phases and owners.
- Defines completion, failure, partial/uncertain outcomes, recovery, and budgets.
- Enforces consequential action boundaries and checks their effectiveness.
- Preserves enough authorized state to inspect and resume work.
- Tests the proposed fix, its regressions, and relevant interactions.
- Names the main trade-off, remaining risk, next action, and review or retirement trigger.

For long tasks, define a context-durability measure with the task set, call count, completion criteria, restart policy, and denominator. The previous “50+ calls and >85%” is an illustrative test design, not an industry standard or universal target.

Use the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) for a proportionate trade-off and handoff record. A visual MHTE map can help explain a complex design; create one with `excalidraw-svg` when useful or requested, rather than requiring a second artifact for every diagnosis.

Route program economics, staffing, and longevity to `harness-operating-model`; tool and sandbox contracts to `tool-architecture`; memory to `invisible-stack` / `context-spec`; authority to `agent-spec` / `trust-ladder`; security to `safety-by-design`; and measurement to `production-observability`, `eval-framework`, or `eval-driven-development`.

See [research and analogy notes](references/research-and-analogy-notes.md) for source limits and preserved examples.
