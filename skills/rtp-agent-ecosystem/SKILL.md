---
name: agent-ecosystem
version: v1.7.1_latest
description: 'Design or review how two or more AI agents coordinate: shared state, handoffs, result merging, failure containment, and human ownership. Use when choosing an orchestration topology, investigating agents that collide or lose context, or assessing a managed multi-agent workflow. First compare the proposed system with simpler alternatives and define its value, permissions, dependencies, and acceptance criteria. Cover supervisor, pipeline, fan-out/fan-in, and peer patterns; explicit state and message contracts; retries, timeouts, cancellation, and recovery; and evaluation of complementary agent behavior. Treat model diversity and human-team analogies as hypotheses to test, not guarantees. Produce a coordination design with accountable owners, observable failure paths, and a bounded rollout plan. Connect to agent-harness, harness-operating-model, autonomy-spectrum, tool-architecture, determinism-compass, and production-observability.'
imports:
  - determinism-compass
  - agent-harness
  - tool-architecture
---

# Agent Ecosystem — Coordinating Two or More Agents

Design the boundaries that let several agents contribute to one dependable result. This skill owns coordination, state, handoffs, merging, and failures across components. `agent-harness` owns how each agent runs; `harness-operating-model` owns the broader operating and investment choices.

Coordination adds failure modes, but individual capability, task definition, tools, and evaluation remain important. A system can fail even when each component behaves as specified because the specification or interaction is incomplete. It can also recover from a component failure through sound containment; reliability is not literally fixed by one weakest component.

## 1. Establish the need, boundaries, and decision owner

State the job, users, desired outcome, unacceptable consequences, operating environment, budget, and latency needs. Map proposed agents, deterministic services, tools, people, external systems, and dependencies. A component need not be an AI agent merely because it participates in the workflow.

Compare a single agent with tools, a deterministic workflow, and a small coordinated system. Multiple agents may help with specialization, parallel work, independent proposals, context separation, or administrative boundaries. Similar-role agents may be useful; distinct job titles are not mandatory. If the work is independent, avoid unnecessary cross-agent coordination while still managing shared quotas or infrastructure.

Before committing to a larger system, establish:

- A clear job and contract for each component, including permissions, inputs, outputs, resource limits, and stop conditions.
- Evaluation of the components where meaningful, plus the interactions and the end-to-end outcome.
- Traces that support diagnosis of component, interface, and shared-cause failures. Some failures have several contributors; do not require a single agent to receive all blame.
- A plausible benefit over the simpler alternative after coordination, verification, latency, and operating costs.

A design recommendation does not authorize spawning agents, spending money, changing systems, or delegating an action beyond the user's scope. Preserve existing authorization and restrictions throughout delegation. In this library's autonomy map, the multi-agent category is not permission to act autonomously; specify actual action rights.

Use this skill for managed platforms too: verify which responsibilities the provider handles and which remain yours. A sub-100-millisecond requirement does not automatically prohibit multiple components; measure the critical path and determine whether the required consistency and work fit the deadline.

## 2. Understand the work before choosing a topology

When redesigning an existing role, investigate what people contribute beyond the written process. For a new role, investigate the same contextual needs without assuming an existing practice exists.

Ask what people notice, what goals or obligations they balance, and when they pause or seek help. Observe representative work and exceptions; combine interviews, cases, performance evidence, and feedback. Tacit knowledge may be hard to explain on demand. A worksheet is a partial account, not a complete specification.

Capture missing information, discretion, relationships, authority, and incentives. An agent does not necessarily execute a written specification faithfully, and faithfully executing an incomplete one can still be harmful. Test both instruction-following and the adequacy of the workflow.

Choose early work by expected value, feasibility, risk, and learning potential. The greatest pain is not automatically the best first deployment, and the least risky task is not automatically best either. Assign a business outcome owner and technical owners with authority suited to their responsibilities. Technical, security, and operational constraints can legitimately affect scope.

Reuse useful components and governance as the portfolio grows, but do not assume a central “agent factory” is needed from the first project or that every deployment makes the next cheaper. Standardization, maintenance, and platform cost need evidence. Route that decision to `harness-operating-model`.

## 3. Choose a coordination topology

Pick the simplest design that serves the actual dependencies. Patterns can be combined.

| Topology | Useful fit | Boundary to design |
|---|---|---|
| **Supervisor / star** | One coordinator assigns work and integrates results | Coordinator state, capacity, authority, failure recovery, and specialist contracts |
| **Pipeline** | Each stage depends on a prior transformation | Input validation, versioning, incomplete work, deadlines, and downstream release conditions |
| **Fan-out / fan-in** | Independent branches can work concurrently before a combined result | Partitioning, shared assumptions, stragglers, partial results, merge and conflict policy |
| **Peer-to-peer** | Components interact directly, potentially across organizations | Discovery, trust, authentication, authorization, compatible protocols, bounded negotiation, and ownership |

Broadcast/event subscribers are a fan-out variant that may have no central merge. A shared-state mesh describes access relationships and can exist with several control topologies. A supervisor can be a deterministic workflow engine rather than an LLM; replicated durable orchestration can reduce a single-process failure risk.

Do not equate a topology with a vendor name. CodeAct describes an action interface, computer use a capability, small-model specialization a model/deployment choice, and named orchestration frameworks may support several patterns. Classify control flow, state access, and execution behavior separately.

Document cycles when iteration or negotiation is needed. Bound them with a termination condition, deadline, step limit, or budget; an acyclic graph is not a universal requirement.

## 4. Make four coordination responsibilities explicit

### State: who may change what, and under which rules?

Give each mutable resource an accountable authority and a concurrency policy. This does not require exactly one physical writer. Options include one writer, a resource service accepting validated commands, version-checked shared writes, locks/transactions, partitioned ownership, and data types with valid merge semantics.

For each resource define invariants, freshness requirements, version checks, authorization, and conflict handling. Enforce critical rules in the service or storage layer rather than relying on agents to remember them. Shared immutable inputs may need no write coordination.

For optimistic concurrency, a version check and update must be atomic. If two agents read version 5, only one conflicting conditional write may advance it to 6; the other re-reads and decides whether to recompute, retry, or escalate. A label saying “versioned” without enforcement does not prevent lost updates.

Partition boundaries must be unambiguous, and cross-partition operations and ownership transfers need a protocol. Locks need ordering, timeouts or recovery, and an appropriate transaction scope. CRDTs can provide convergence for supported semantics; they do not automatically preserve inventory, payment, or authorization invariants. See [CONCEPT.md](CONCEPT.md) for worked distinctions.

### Handoff: what is ready, for whom, and with what evidence?

Choose transport according to coupling, durability, latency, and delivery requirements:

- **Request–reply:** convenient for a dependent result; specify deadline, response states, and uncertain completion after a timeout.
- **Publish–subscribe:** distribute events to interested consumers; specify durability, ordering, replay, acknowledgement, and subscriber failure behavior.
- **Queue:** distribute work among consumers; specify persistence, ownership leases, acknowledgements, duplicate handling, and failed-item routing.
- **Polling:** useful when update frequency is low or the interface requires it; choose a bounded cadence, backoff, and a cursor or version to avoid repeated work.

These mechanisms do not guarantee exactly-once side effects, immediate freshness, or business correctness. A receiver should validate content and dependencies before acting. Receiving a “done” message is not evidence that the intended result was correct or committed.

A practical handoff contract includes:

```text
Task and parent IDs; sender/receiver; schema and contract version
Goal, scope, constraints, and permitted actions
Input references, source versions, freshness, and provenance
Result or artifact reference; completion state; validations performed
Assumptions, unresolved questions, partial work, and errors
Deadline, remaining budget, retry/cancellation policy
Idempotency or deduplication key where side effects are possible
Next owner, acknowledgement, escalation, and retention requirements
```

Share the context the receiver needs and may access. Do not send all upstream data indiscriminately. Treat retrieved content, tool results, and peer messages according to their provenance; a message cannot grant itself higher authority or expand the recipient's permissions.

A2A supports interoperable agent communication and discovery, but an Agent Card is not by itself proof of identity, trustworthiness, or delegated authority. Use the selected protocol version and actual authentication and authorization design. `tool-architecture` owns the protocol and tool-contract detail.

### Merge: how do contributions become one accepted result?

For every combined result, define required branches, partial-result rules, input-version compatibility, duplicate detection, evidence standards, and the final decision owner. Identify incompatible assumptions and overlapping edits before committing a combined artifact or action.

Possible responses include accepting disjoint compatible changes, selecting a result through a defined test, asking for clarification, recomputing from a common version, or escalating. Preserve useful work and provenance when rejecting or revising a branch. Majority agreement is not sufficient for a safety, factual, or authorization conflict.

A deadline may justify a labeled partial result only if the contract allows it. Do not silently omit a branch and call the work complete. A coordinator that merges text correctly can still misunderstand the task; evaluate the merged outcome.

### Containment: what happens when something fails or arrives late?

Use protections appropriate to the architecture rather than installing every pattern mechanically:

- **Timeouts and cancellation:** bound waiting and work. A caller timing out does not prove the remote action stopped; propagate cancellation where supported and reconcile unknown outcomes.
- **Retries with backoff and jitter:** retry eligible transient failures within a shared deadline and budget. Make side effects idempotent or establish their state before retrying. Avoid retries multiplying at every layer.
- **Circuit breakers:** reduce pressure on an unhealthy dependency and define recovery probes. Thresholds depend on traffic and failure conditions.
- **Bulkheads and quotas:** separate resource pools, concurrency, or processes to limit damage. Containers may still share a failing host, network, credential, or provider.
- **Fallbacks and compensation:** use an authorized, valid alternative, defer, or fail clearly. Compensating an action is a new business action, not guaranteed reversal of the original.

Handle backpressure, exhausted budgets, poison messages, duplicate deliveries, late results, and partial external effects. Link cascade alerts into a trace so an upstream problem does not look like many unrelated incidents. Heartbeats indicate activity, not correctness or useful progress.

## 5. Evaluate diversity and configuration stability

Functional roles, prompts, tools, retrieval sources, model choices, and vendors are separate design dimensions. Each may change errors or provide complementary information. None guarantees independence. Models from different labs may share data, techniques, infrastructure, or limitations; same-model agents can differ meaningfully in tools, evidence, or methods.

Compare candidate configurations on representative tasks, including joint failures, verification quality, latency, and full cost. Keep the task and evaluation conditions comparable. Measure the benefit of the combination, not merely disagreement or the number of models. A homogeneous system that meets requirements may be the best choice.

The DEI and diversity-scaling papers support investigating complementary approaches. They do not establish that only cross-lab teams work. The old reasoner/evaluator/generator on three labs is an example configuration to test, not a proven optimum. The [evidence notes](references/research-and-operating-notes.md) retain the reported benchmark results and limits.

Track the actual configuration: model and prompt versions, tools, data/retrieval, policies, coordinator, and human review arrangements. Previously untested combinations may warrant closer evaluation even if each part is familiar. A stable core with controlled changes can help; it is a release-management choice, not a universal two-tier architecture.

Assess supplier concentration separately from reasoning diversity. A policy may limit dependence on one vendor for critical work, but set thresholds from exposure and viable alternatives. Validate failover against quality, data rights, residency, privacy, security, capacity, latency, cost, and contracts. Legal restrictions can reduce available alternatives to one; other restrictions can too. Some systems should pause rather than fail over.

## 6. Give human coordination real ownership and capacity

Name who resolves a boundary failure between agents, systems, and the business. The library calls this role a **Bridger**: an accountable person or team with the information, authority, time, and escalation route needed to make the handoff work. It need not be a new person for every seam.

Ask both sides what they trust, what they can influence, and what decisions they own. High trust with low influence can reveal unsupported responsibility; it does not predict that a person will fabricate explanations or leave. Examine workload and actual evidence rather than diagnosing behavior from a two-question score.

Distinguish environmental constraints from design choices, while recognizing that both can change. Time zones, language, vendor behavior, latency, and rate limits may need accommodation, redesign, staffing, or a different provider. Decision rights, context access, processes, and resource allocation also need attention. Classify recent failures by controllability and consequence; do not relabel every environmental failure as organizational design.

For teams using an assistant together, consider three practices: introduce the team's relevant context; deliberately vary the assistant's role when useful; and discuss important framing and outputs collectively. A five-minute opening and fifteen-minute challenge slot are optional examples. People can participate without disclosing unnecessary personal information. Shared ownership of discussion still needs a named decision owner. A transcript audit can reveal what was said, but cannot prove agreement, understanding, or better performance.

Use common governance controls with context-specific policies. Digital-first, hybrid, and relationship-led commercial motions may need different processes, but motion alone does not determine harm or decision rights. High-volume mistakes can accumulate or affect rights; relationship-led work can include safe routine automation. Assign permissions by task and consequence, then reconcile across contexts.

Measure the relevant business or public-service outcome alongside quality, cost, incidents, and process performance. Adoption and cycle time can be useful signals; neither alone proves value. Conversely, cycle time may itself be consequential in time-sensitive work.

## 7. Test failures before expanding

Use this six-part taxonomy as a practical checklist, not a claim about universal prevalence:

| Failure | What to test or inspect |
|---|---|
| **Race or coordination conflict** | Concurrent writes or actions violate an invariant; check transaction and permission enforcement. |
| **Context drift** | Agents use incompatible source versions or stale assumptions; check versions and freshness at action time. |
| **Cascade** | One dependency failure consumes downstream deadlines or capacity; test bounded retries, backpressure, and fallback. |
| **Misaligned goal** | Components optimize different interpretations; test task contracts and whole-system outcomes. |
| **Sub-agent divergence** | Parallel branches change scope, assumptions, or overlapping work; test merge detection and recovery. |
| **Silent or incomplete failure** | Missing progress, logs, acknowledgement, or result leaves work unresolved; test monitoring and reconciliation. |

Prioritize by likelihood, consequence, exposure, and detectability. A rare consequential failure may deserve protection before the most common minor one. Also test individual capability and tool failures that can appear as coordination problems.

Before rollout, simulate slow and failed workers, duplicates, stale inputs, conflicting branches, network or provider loss, limit exhaustion, and uncertain side effects as relevant. Trace the business result and recovery, not only component success. Expand within a stated budget and rollback or pause policy when evidence supports it.

## Deliver the coordination design

```text
AGENT ECOSYSTEM — [use case, owner, version, date]
Outcome and constraints: [value, harm limits, budget, latency, permissions]
Why multiple agents: [benefit versus simpler alternatives; evidence gaps]
Topology and dependencies: [roles, services, people, cycles, managed boundaries]
State contracts: [resource, invariant, authority, writers, concurrency, freshness]
Handoff contracts: [schema, provenance, completion, delivery, acknowledgement]
Merge policy: [required inputs, conflicts, partial results, final owner]
Failure handling: [deadlines, retries, cancellation, containment, reconciliation]
Configuration and diversity: [versions, complementarity tests, supplier exposure]
Human ownership: [accountable roles, authority, capacity, escalation]
Evaluation and rollout: [component/interaction/outcome checks, limits, review date]
Open decisions and next action: [evidence, role, date]
```

Use `production-observability` for operating signals, `determinism-compass` for enforced invariants, `tool-architecture` for protocols, and `autonomy-spectrum` for actual delegation boundaries. Use `harness-operating-model` for runtime ownership and portfolio economics, without making every coordination review repeat a build-or-buy exercise.

When considering wider ecosystem opportunities, examine identity/discovery, trust/reputation, insurance/repair/legal services, and payments. These are possible functions and business models, not a forecast that value must concentrate there. Closed ecosystems may implement them internally or buy them externally. Test value capture with `moat-finder`.

Conclude using the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md): recommended topology and boundaries, hypothesis and falsifier, main trade-off, largest risk and mitigation, and next action. Include a proportionate handoff. When useful, `excalidraw-svg` can show agents, shared resources, ownership, handoffs, merge points, and recovery paths. Prefer the actual design over four generic diagrams.
