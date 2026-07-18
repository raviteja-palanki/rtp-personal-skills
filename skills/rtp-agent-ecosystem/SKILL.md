---
name: agent-ecosystem
version: v1.0_latest
description: "When two or more AI agents must work together, the hard problem stops being intelligence and becomes coordination: who owns the shared state, how work hands off without losing context, and what happens at the merge when the agents disagree. Covers the coordination topologies (supervisor, pipeline, fan-out/fan-in, peer), handoff protocols, state ownership, the multi-agent failure taxonomy (race, context drift, cascade, sub-agent divergence), isolation boundaries, the multi-agent graduation gate, and the human twin of every handoff — the named owner of the seam. Use when designing a 2+ agent system, choosing a topology, or diagnosing agents that collide or lose work. This skill owns the seams between agents; agent-harness owns the single-agent machine. Pairs with: agent-harness, harness-operating-model (build/buy + fleet cost), autonomy-spectrum (Level 7), tool-architecture (A2A), determinism-compass. Triggers: 'multi-agent', 'agent orchestration', 'agent handoff', 'sub-agent divergence'."
imports:
  - determinism-compass
  - agent-harness
  - tool-architecture
---

# Agent Ecosystem — Coordinating Two or More Agents

**The objective:** make a set of agents behave like one reliable system instead of a pile of independent workers that collide. This skill owns the **seams between agents** — coordination, handoff, shared state, merge. It does *not* re-teach the harness that runs each agent (that's `agent-harness`) or the cost/org of running it (`harness-operating-model`); it routes there. What's left here is the problem that only exists once there are two.

## THE ONE IDEA

**The moment you have two agents, your problem is no longer how smart each one is — it's who owns the seam between them.** Every agent can be individually correct and the system still fails, because no one owns the shared state, the handoff, or the merge. Three consequences:

1. **Coordination is the failure surface, not capability.** The dominant multi-agent failure is *coordination* — race conditions on shared state, agents acting on stale copies, cascades where one timeout stalls the chain, and the newest one: **sub-agent divergence** (an orchestrator fans work out to parallel workers whose copies of the situation quietly stop matching, and the merge drops correct work or hits a conflict with no rule to resolve it). A smarter model does not fix a missing merge rule.
2. **Don't go multi-agent until you've earned it.** The 2026 practitioner consensus: stay narrow until you know the surface. Graduate to multi-agent only when **each sub-agent has a narrow job, each has an explicit eval, and the system can attribute a failure to the correct agent.** Premature multi-agent multiplies failure modes before you understand any one of them — it's the most expensive way to look sophisticated.
3. **Every machine handoff has a human twin.** The "context lost at the handoff" problem is the same failure the org has always had at the tech↔business seam: no one owns the translation step, so it never gets built. Name the owner of the seam — the *Bridger* — for both the agents and the humans around them.

The spine: **an agent ecosystem is only as reliable as its weakest seam — so own the state, own the handoff, own the merge, and don't add an agent you can't attribute a failure to.**

## KEY TERMS (plain language)

- **Multi-agent system** — two or more AIs on the same job, each with a role, that must coordinate instead of collide.
- **Coordination topology** — the shape of who talks to whom: one supervisor delegating (star), a pipeline (A→B→C), fan-out/fan-in (one splits, many work, one merges), or peer-to-peer.
- **Handoff** — one agent passing work to the next; the point where context (what's been learned) is most easily lost.
- **State ownership** — the rule that every mutable resource has exactly one owner, so two agents never write it uncoordinated.
- **Sub-agent divergence** — parallel workers drift from a shared plan; the merge step is where it surfaces.
- **A2A** — the open standard for one agent to prove its identity to and hand work to another (the protocol depth lives in `tool-architecture`).
- **Bridger** — the named human owner of a seam (agent↔agent, or agent-team↔business-team); the human counterpart of a handoff protocol.

## SHOULD THIS BE MULTI-AGENT AT ALL? (the gate before anything else)

Most "multi-agent" systems should be one agent with good tools. Run the gate before designing topology:

- **Is the task decomposable into *distinct* roles** (plan / do / check), each with a bounded job? If it's one continuous job, keep it single-agent.
- **Can you write an explicit eval for each proposed sub-agent?** If you can't say what "good" means for sub-agent B alone, you can't debug it in a fleet.
- **Can the system attribute a failure to the correct agent?** If a bad outcome could come from any of five agents and you can't tell which, you've built a system you can't operate.

Only when all three hold does multi-agent pay for its coordination tax. Until then, a single agent with a narrow tool set (see `agent-harness`, the narrow-gate pattern) ships faster and fails legibly.

## THE COORDINATION TOPOLOGIES

Pick the simplest shape that fits; escalate only when it demonstrably fails.

- **Supervisor / star** — one orchestrator delegates to specialists and owns the final decision. The default for enterprise workflows with clear domain boundaries. Cost: the orchestrator is a single point of failure and a bottleneck; keep it thin.
- **Pipeline** — A→B→C, each stage transforms and passes on. Simple and legible; failures propagate downstream, so each stage needs a validated handoff.
- **Fan-out / fan-in** — one agent splits work to many parallel workers, one merges the results. Fast, but the *merge* is where sub-agent divergence bites — the merge step needs a rule for "what to do when the pieces disagree," not just concatenation.
- **Peer-to-peer** — agents negotiate directly (often across vendors via A2A). Loosely coupled at org scale, but the trust and versioning surface is widest; use only when a central orchestrator genuinely can't sit in the middle.

*(Vendor-named patterns — CodeAct, Magentic, computer-using, SLM-micro — are these topologies dressed in a product's clothes; classify a vendor's system by which topology it actually is, and by which model-under-which-harness runs each node, per `agent-harness`.)*

## THE FOUR THINGS TO OWN

**1. State ownership — every mutable resource has exactly one owner.** *Agent-owned* (one agent writes, others read), *resource-owned* (a service owns it; agents write only through permission gates), *shared-with-versioning* (multiple writers with version numbers; conflicts detected on mismatch), or *partitioned* (each agent owns a disjoint slice). **Never allow two agents to write the same state without coordination** — that's the race condition that produces the field's most common multi-agent failure.

**2. Handoff protocol — how B learns A's work is ready.** *Request-reply* (B asks, waits — simple, blocking, for real-time with a timeout); *pub-sub* (A publishes "done," B subscribes — non-blocking, eventual consistency); *queue* (A enqueues, B dequeues — decouples timing); *polling* (B asks periodically — inefficient, simple). Choose by latency tolerance. And validate the *content* of the handoff, not just its arrival — a handoff that carries stale or malformed state is silent drift with extra steps.

**3. The merge rule — what happens when parallel work disagrees.** The step teams skip. For any fan-out, define: how the merge checks the pieces still agree, and what it does when they don't (pick one, escalate, re-run). No merge rule = sub-agent divergence with no recovery.

**4. Isolation boundaries — so one agent's failure doesn't become the system's.** *Timeout* (fail with a fallback past a limit), *circuit breaker* (stop calling an agent after N consecutive failures), *bulkhead* (separate processes/containers so a crash doesn't take peers down), *fallback* (a default behavior when an agent fails). Add *cascade detection*: A timeout → B waits → C fails is a chain to break, not a set of independent alerts.

## THE MULTI-AGENT FAILURE TAXONOMY

Identify which is *most likely* in your system and build the safeguard for that one first:

- **Coordination / race** — two agents act on the same resource at once *(→ state ownership)*. This is the largest single share of multi-agent failures in the field (⚠ practitioner-reported).
- **Context drift** — Agent A holds old data, Agent B new; they act on conflicting truth *(→ versioning + divergence detection)*.
- **Cascade** — one agent's timeout stalls everything downstream *(→ circuit breaker, fail-fast)*.
- **Misaligned goal** — agents solve subtly different problems from an ambiguous brief *(→ a shared, explicit spec; the orchestrator owns it)*.
- **Sub-agent divergence** — parallel workers drift and the merge breaks *(→ the merge rule)*.
- **Silent failure** — an agent dies without logging and a peer waits forever *(→ heartbeats + observability, see `production-observability`)*.

## THE HUMAN TWIN — name the owner of the seam

The machine "context lost per handoff" problem has a clean non-technical twin: Linda Hill's innovation research finds the *human* tech↔business handoff inside companies fails for structurally the same reason — no one owns the translation step, and translating work ("bridging") is unrewarded, so it never gets built. The fix is the org-design version of the protocols above: **name a specific bridging owner and reward the bridging itself**, rather than hoping coordination emerges from proximity. Use this when explaining agent-handoff design to non-technical stakeholders — a *Bridger* is the human fix to the same failure a handoff protocol is the machine fix to. *(When wrong: it's an analogy, not an identity — the machine loss is measured context; the human loss is accountability and information. Source: Linda Hill, HBR, Jun 2026 — ◆ research base, 24 industries / 23 countries.)*

## WHERE THIS SKILL MEETS YOUR STACK

This skill owns the *seams*; the depth on either side lives elsewhere:

- **The machine each agent runs on → `agent-harness`.** Orchestration is one of its five clusters; the Planner/Generator/Evaluator pattern, the Ralph Loop, the narrow-gate, and context durability are taught there. This skill assumes each node is a competent single agent and worries only about how they combine.
- **Build vs buy the orchestration runtime, and the cost of running a fleet → `harness-operating-model`** (managed vs self-built vs hybrid, the moat, the maturity ladder). Do not re-decide build/buy here.
- **Level 7 (multi-agent) on the autonomy map, and why the frontier is fragile → `autonomy-spectrum`**; **the A2A protocol + per-tool contract that carries a handoff → `tool-architecture`.**
- **Detecting silent failures and cascades in production → `production-observability`**; **what must stay deterministic across the handoff → `determinism-compass`.**

The spine: **this skill makes a set of agents into one system by owning the seams; the harness makes each agent reliable, and the operating model pays for the fleet.**

## DIAGNOSTIC QUESTIONS

1. Should this even be multi-agent? Can you write an explicit eval for each sub-agent and attribute a failure to the right one? If not, keep it single-agent.
2. For every mutable resource: who is the single owner, and can two agents ever write it uncoordinated?
3. For every fan-out: what is the merge rule when the parallel pieces disagree — pick one, escalate, or re-run?
4. Which failure mode is most likely in *your* topology (race / drift / cascade / divergence)? What's the safeguard for that one, shipped?
5. Does each agent have an isolation boundary (timeout, circuit breaker, bulkhead, fallback), and do you detect cascades as a chain?
6. Who is the named human owner of the seam between the agent team and the business it serves?

## QUALITY GATE

- [ ] The multi-agent gate passed: distinct roles, an eval per sub-agent, and failure-attribution to the correct agent — or it stays single-agent.
- [ ] The coordination topology is named (supervisor / pipeline / fan-out-fan-in / peer) and is the simplest that fits.
- [ ] Every mutable resource has exactly one owner; no two agents write it uncoordinated.
- [ ] Each dependency has a handoff protocol, and handoff *content* is validated, not just arrival.
- [ ] Every fan-out has an explicit merge rule for disagreement.
- [ ] Each agent has isolation boundaries; cascades are detected as a chain and broken.
- [ ] The most-likely failure mode is identified and its safeguard shipped first.
- [ ] A named human owns the seam (the Bridger).

## WHEN WRONG

Don't reach for this skill when: it's one agent (use `autonomy-spectrum` for the level, `agent-harness` for the machine); the agents are *truly* independent (coordination overhead kills the benefit — keep them separate); you need strong consistency at <100ms (coordination adds latency — partition the data instead); or a vendor orchestrator (Copilot, Manus, a managed platform) already handles coordination (use their patterns; this skill is for when you own the seams). And be honest about the evidence tier — the failure-share percentages, context-durability thresholds, and cost figures that used to live here are practitioner-reported field patterns (⚠), and the harness/managed-vs-self-built economics now belong to `harness-operating-model`; don't quote them here as settled.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally the four coordination topologies with the *seam* (shared state / handoff / merge) highlighted as the failure surface on each. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
