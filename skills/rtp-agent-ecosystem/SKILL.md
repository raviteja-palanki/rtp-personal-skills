---
name: rtp-agent-ecosystem
description: "Orchestration, state management, handoff for multi-agent systems. Patterns: CodeAct, Magentic, SLM-micro, computer-using, A2A, harness. Use when: architecting multi-agent systems, choosing protocols. Triggers: 'multi-agent', 'agent protocol', 'orchestration'"
imports:
  - determinism-compass
---

## DEPTH DECISION

**Go deep if:** You're designing a multi-agent system (2+), evaluating orchestration architecture, planning to scale beyond one agent, or addressing coordination failure modes.

**Skim to diagnostic questions if:** You want a quick check on existing agent design or protocol choices.

**Skip if:** Single agent, synchronous execution, or no agent-to-agent communication needed.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

Agent A works. Agent B works. You deploy both. Now they compete for resources, break each other's assumptions, or act on the same object simultaneously. The trap: treating multi-agent as independent agents instead of coordinated system. Worse: picking the wrong design pattern for your problem domain.

In 2025-2026, there are 6 dominant patterns. Not picking one is a bet on luck.

## THE PROCESS

**Layer 0: Pick your design pattern**

Six patterns dominate production multi-agent systems. Choose based on your PM constraints:

1. **CodeAct (Manus):** Agent writes and executes code as primary action. When: heavy computation, scientific workflows, ETL. Cost: execution overhead, security surface.

2. **Magentic Orchestration (Microsoft Copilot):** Specialized agents (each expert in one domain) coordinated by orchestrator. When: enterprise workflows with clear domain boundaries. Cost: requires orchestrator discipline.

3. **SLM-Powered Micro Agents (Cursor):** Fast, cheap, focused agents on small language models handling subtasks. When: repetitive work, cost-sensitive. Cost: requires good decomposition.

4. **Computer-Using Agents (Claude):** Direct GUI interaction via screen understanding. When: legacy systems, UI-only integration. Cost: fragile to UI changes, slower than API.

5. **A2A Interoperability:** Agents communicating across organizational boundaries via standard protocols. When: multi-vendor ecosystems, partner integrations. Cost: protocol negotiation overhead.

6. **Harness Engineering (OpenAI Codex model):** System design > model intelligence. Ephemeral environments, local observability stacks, sandboxed execution. When: reliability critical, complex workflows. Cost: infrastructure complexity.

**Pick one or a hybrid.** Most enterprises ship Magentic + SLM-micro hybrid (orchestrator + cheap specialists).

**Layer 1: Protocol convergence — MCP + A2A**

Two protocols are consolidating agent-to-X communication:

- **MCP (Model Context Protocol):** Agent-to-tool communication. 97M+ downloads. Standard connectors for databases, APIs, cloud services. PM decision: build custom MCP connector or use existing?

- **A2A (Agent-to-Agent):** Agent-to-agent communication across boundaries. Emerging standard for agent handoffs. PM decision: when to use A2A vs request-reply, which orchestrator enforces it?

- **AG-UI:** Agent-to-frontend streaming protocol. Real-time feedback on long-running operations.

**Key PM question:** Are you betting on protocol standardization or building proprietary connectors? Standards = slower, but cheaper long-term. Proprietary = faster short-term, vendor lock-in long-term.

**Layer 2: Map agent dependency graph + failure taxonomy**

For each pair of agents, ask: can they act on the same resources? Do they depend on each other's outputs?

Draw a directed graph (critical paths where A → B → C → failure):
- **Example:** PricingAgent → OrderAgent → BillingAgent. If PricingAgent fails, cascade breaks downstream.
- **Example:** Two RecommendationAgents reading/writing same user profile. Race condition.

**Multi-agent failure taxonomy (from research):**
- 36.9% **coordination failures** (shared state, race conditions)
- **Context drift** between agents (Agent A has old data, Agent B has new)
- **Broken tool calls** (Agent calls tool with wrong arguments)
- **Misaligned reasoning** (Agents solve different problems due to ambiguous goal)
- **Cascade failures** (Agent A timeout → B waits → C fails)

**Your job:** Identify which failure mode is most likely in your system. Build safeguards for that one first.

**Layer 3: Establish state ownership**

Every mutable resource has one owner:

- **Agent-owned:** Agent X owns cache, no other agent modifies.
- **Resource-owned:** AuthService owns UserProfile, agents read only or write with permission gates.
- **Shared-with-versioning:** Multiple agents read/write with version numbers. Detect conflicts via mismatch.
- **Partitioned:** Each agent owns disjoint data (Agent-A: users 0-50k, Agent-B: 50k-100k).

**Never allow:** Two agents writing the same state without coordination.

**Layer 4: Design handoff protocols**

When Agent A completes work that Agent B needs, how does B know?

1. **Request-reply:** B asks A for work, waits. Blocking, simple, latency cost.
2. **Pub-sub:** A publishes "work complete," B subscribes. Non-blocking, eventual consistency.
3. **Queue:** A enqueues, B dequeues. Decouples timing, adds overhead.
4. **Polling:** B periodically asks "is your work done?" Inefficient but simple.

Choose based on latency tolerance: real-time → request-reply with timeout, batch → pub-sub or queue.

**Layer 5: Harness > Model**

**Critical insight:** Agent reliability comes from system design, not model intelligence. The model is a component. The system is the product.

OpenAI's Codex approach emphasizes ephemeral environments with logs, metrics, traces. Anthropic's building-effective-agents doc emphasizes simple orchestration over complex architectures.

**Model Evolution Impact:** Every harness component encodes an assumption about what the model can't do on its own. As models improve, these assumptions become obsolete and harness overhead grows unnecessary. Example: Claude 4.5 needed explicit step-by-step decomposition (Planner agent required). Opus 4.6 handles ambiguous briefs with minimal scaffolding (Planner becomes optional). Your harness must evolve with model capability.

**The moat is not the model; the moat is the harness.** When competitors have access to the same model, your harness extracts disproportionate value from it. When models improve, you either:
1. **Simplify:** Remove scaffolding components that are now redundant. Faster execution, lower cost.
2. **Redeploy:** Keep the same harness, add new capabilities the model can now handle (e.g., multi-language support on improved reasoning).
3. **Double down:** Models improved, so competition intensified. Invest in proprietary harness innovation to stay ahead.

**Watch your harness architecture; don't watch model updates.** Your harness strategy determines whether you gain or lose value from model improvements.

**Your PM checklist:**
- [ ] Ephemeral sandboxed execution (agents don't corrupt each other's state)
- [ ] Local observability (logs, metrics, traces you can inspect post-mortem)
- [ ] Graceful degradation (if Agent A fails, system doesn't cascade)
- [ ] Simple orchestration (one coordinator, not peer-to-peer)

**Layer 5.25: Managed vs. Self-Built vs. Hybrid Harnesses**

The infrastructure decision that most enterprises face in 2026: who runs the harness?

**Managed Harness** (Anthropic Managed Agents, launched April 2026): Vendor provides production-grade orchestration + sandboxed environment + observability. You define tasks, tools, and guardrails. $0.08/active session-hour + standard token costs. Pre-optimized with prompt caching — often 20-40% better effective token efficiency than average self-built. Solves the "harness goes stale" problem because vendor evolves the orchestration layer underneath stable interfaces.

**Self-Built Harness** (LangGraph, custom SDKs, enterprise VPC): Maximum control over orchestration, guardrails, and data residency. Higher upfront cost (4-20 engineer-weeks for first production version, 10-20% quarterly maintenance). Justified when: annual session fees would exceed $1M+, data sovereignty is a hard blocker, or proprietary IP in the orchestration itself is a competitive advantage.

**Hybrid** (the Fortune 100 default for 70-80% of use cases): Use vendor-managed harness as the "inner harness" for core orchestration (session continuity, sandboxing, error recovery). Build your own "outer harness" for company-specific governance (approval flows, risk classification, SIEM export, domain-specific evaluators). This is the "buy the platform, build the moat" pattern.

| Factor | Managed | Self-Built | Hybrid |
|--------|---------|------------|--------|
| Time-to-production | 2-6 weeks | 3-6 months | 3-8 weeks |
| Control | Good | Maximum | High |
| Governance | Strong built-in | You own 100% | Best of both |
| Scaling | Automatic | You manage | Automatic core |
| Risk of obsolescence | Low (vendor evolves) | High (harnesses stale) | Low |

**Decision heuristic:** Start every pilot on Managed. Layer outer harness for governance. Transition to self-built only when volume, sovereignty, or IP justify the engineering investment. Re-evaluate every 6 months using TCO modeling.

**Context Durability as Your Leading KPI**

Context durability — the % of tasks completing successfully after 50+ tool calls without human restart — is the single most predictive metric for harness health. One-shot accuracy benchmarks (SWE-Bench, etc.) don't measure this. A model might ace a benchmark in 2 tries, then fail to follow its own instructions after running for an hour.

**Target thresholds:**
- Baseline (no harness): ~45% for multi-session tasks
- Basic harness (initializer + simple loop): 75-85%
- Mature harness (PGE + lifecycle hooks + progress artifacts): 88-94%
- World-class (self-optimizing harness with trace-fed improvement): >95%

**Track weekly alongside:** Human intervention rate (<20% target), average session completion time (40% reduction target), and cost per successful task (should trend down as self-dissolving effect kicks in after 6-9 months).

**Layer 5.5: Anthropic Harness Engineering Patterns**

The three-agent Planner/Generator/Evaluator architecture is the dominant pattern in Anthropic's harness engineering approach. This pattern maps cleanly to multi-agent ecosystem design:

- **Planner Agent:** Converts brief requirements into detailed specifications. Maps user intent → actionable spec. Single LLM call, high determinism.
- **Generator Agent:** Implements the spec in focused sprints (iterative refinement). Multiple fast calls, exploration-heavy.
- **Evaluator Agent:** Uses Playwright-style browser automation to test live behavior. Observes actual outputs, not just reasoning. Acts as ground truth.

**Critical insight from GAN-inspired research:** "Agents tend to confidently praise their own mediocre work." A Generator left alone will ship mediocre solutions with high confidence. Separation of generation from evaluation is architecturally critical. The Evaluator can't be the same agent as the Generator. Conflicting incentives collapse without boundary enforcement.

**Why this matters for multi-agent design:**
- **Prevents self-deception:** Generator can't fool Evaluator because Evaluator observes live reality, not claims.
- **Enables feedback loops:** Evaluator → Planner → Generator cycles improve iteratively without human intervention.
- **Scales with complexity:** As task complexity grows, Evaluator can stay simple (test harness) while Planner and Generator specialize.

**Implementation in your ecosystem:**
- If you have 2-3 agents, this pattern may not be necessary (one agent doing all three roles).
- If you have 5+ agents, consider whether a dedicated Evaluator agent prevents false consensus among Generators.
- State ownership: Planner owns spec versions, Generator owns implementation drafts, Evaluator owns ground-truth test results.

**Layer 6: Agent capability framework**

Not all agents are created equal. Your PM litmus test: does this agent exhibit these 5 capabilities?

- **Goal interpretation:** Can it understand what the user actually wants, not just the literal request?
- **Multi-step planning:** Can it break complex work into subtasks, not just execute one command?
- **Tool selection:** Can it pick the right tool for the job, or does it use the same tool for everything?
- **Autonomous execution:** Can it recover from failures and retry, or does it fail immediately?
- **Adaptation:** Can it learn from feedback and adjust behavior, or is it static?

**Agent capability levels:**

- **Level 1 (Task Executor):** Narrow, predetermined sequences. No planning. High reliability.
- **Level 2 (Workflow Coordinator):** Multi-step with basic planning. This is where most enterprise value is.
- **Level 3 (Autonomous Strategist):** Complex, ambiguous, learns. Mostly aspirational.

Most PMs should target Level 2. Level 3 is bleeding edge.

**Layer 7: Monitor and isolate**

- **Latency:** Agent A usually 100ms. Now 5s. Alert.
- **Error rate:** Usually 99%. Now 50%. Alert.
- **Queue depth:** Work piling up? Alert.
- **State divergence:** Agent A and B disagree on shared state. Alert.
- **Cascade detection:** Agent A timeout → B timeout → C timeout. Stop the chain.

**Isolation boundaries per agent:**
- **Timeout:** 5 second limit. Proceed with fallback if exceeded.
- **Circuit breaker:** Fail 3x in a row. Stop calling this agent (until manual reset).
- **Bulkhead:** Agent crash doesn't crash peers. Separate processes/containers.
- **Fallback:** Default behavior if agent fails.

## REALITY CHECK

**Failure modes you'll hit:**

1. **Cascading timeout:** A times out → B waits → B times out → C fails. FIX: fail fast, use circuit breaker.

2. **Coordination overhead:** So many gates/locks that all agents serialize. No parallelism. FIX: minimize critical sections, use partitioning.

3. **Context drift:** Agent A has stale data, Agent B has fresh. Agents act on conflicting truth. FIX: implement versioning or CRDTs, detect divergence.

4. **Silent failure:** Agent A fails without logging. B waits forever. FIX: implement heartbeats.

5. **Protocol mismatch:** Team built custom handoff protocol. Later agent doesn't understand it. FIX: adopt MCP or A2A standard.

6. **Context Anxiety Failure Mode (March 2026 Anthropic finding):** Agents wrap up work prematurely as context window fills. Agent A is mid-analysis, realizes 15% context remaining, and ships incomplete work rather than risk hard stop. FIX: context resets > context compaction. File-based agent communication (agent writes intermediate results to file, next agent reads file) reduces context pollution and prevents premature closure. Test: increase max_tokens; agents should take longer, not ship faster.

**Cost at scale:**
- 2 agents: simple handoff, maybe a queue
- 10 agents: dependency graph gets complex, need orchestrator
- 100+ agents: formal orchestration (Kubernetes, Temporal), distributed tracing, chaos testing required

## QUALITY GATE

- [ ] Design pattern chosen (CodeAct? Magentic? SLM-micro? A2A?)
- [ ] Protocol strategy documented (MCP connectors? Custom handoff? A2A standard?)
- [ ] Dependency graph explicit (which agents interact)
- [ ] State ownership clear (every mutable resource has one owner or versioning)
- [ ] Handoff protocol per dependency (request-reply, pub-sub, queue, or polling)
- [ ] Isolation boundaries per agent (timeout, circuit breaker, bulkhead, fallback)
- [ ] Failure taxonomy identified (which failure mode is most likely? Build safeguards first.)
- [ ] Monitoring in place (latency, error rate, queue depth, state divergence)

## WHEN WRONG

This skill gives bad advice if:

1. One agent only. Use autonomy-spectrum.
2. Truly independent agents. Coordination overhead kills benefits. Keep separate.
3. Strong consistency + <100ms latency. Coordination adds latency. Partition instead.
4. Can invest in full orchestration (Kubernetes + Temporal). Do that; this skill is lighter-weight.
5. Already using Copilot, Manus, or vendor orchestrator. They handle most of this. Use their patterns.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
