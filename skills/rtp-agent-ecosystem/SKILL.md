---
name: agent-ecosystem
version: v1.5_latest
description: 'When two or more AI agents must work together, the hard problem stops being intelligence and becomes coordination: who owns shared state, how work hands off without losing context, and what happens at the merge when agents disagree. Covers coordination topologies (supervisor, pipeline, fan-out/fan-in, peer), handoff protocols, state ownership, the multi-agent failure taxonomy (race, context drift, cascade, sub-agent divergence), and the graduation gate. Also the human twin of every handoff: the named owner of the seam, and where value concentrates beyond the agents themselves. Use when designing a system of two or more agents, choosing a topology, or diagnosing agents that collide or lose work. This skill owns the seams between agents; agent-harness owns the single-agent machine. Pairs with: agent-harness, harness-operating-model, autonomy-spectrum. Triggers: ''multi-agent'', ''agent orchestration'', ''agent handoff''.'
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
- **Trust/influence diagnostic** — a two-question check on both sides of a seam: do you trust the other side, and do you feel you have influence over the outcome? High trust paired with low influence is the dangerous pattern.
- **Value-capture layer** — the infrastructure around the agents (identity, trust, insurance, payments) where economic value is likely to concentrate, independent of which agents win.
- **Implicit organization** — the tacit knowledge, motivational alignment, and professional discretion that make a documented process actually work; invisible because humans quietly filled its gaps. An agent given only the documented spec never sees it.
- **Cross-lab model diversification** — staffing an agent team so its members come from different labs (different training data, different alignment approach), not just different prompted personas. A design axis in its own right, separate from which functional role each agent plays.

## SHOULD THIS BE MULTI-AGENT AT ALL? (the gate before anything else)

Most "multi-agent" systems should be one agent with good tools. Run the gate before designing topology:

- **Is the task decomposable into *distinct* roles** (plan / do / check), each with a bounded job? If it's one continuous job, keep it single-agent.
- **Can you write an explicit eval for each proposed sub-agent?** If you can't say what "good" means for sub-agent B alone, you can't debug it in a fleet.
- **Can the system attribute a failure to the correct agent?** If a bad outcome could come from any of five agents and you can't tell which, you've built a system you can't operate.

Only when all three hold does multi-agent pay for its coordination tax. Until then, a single agent with a narrow tool set (see `agent-harness`, the narrow-gate pattern) ships faster and fails legibly.

## BEFORE YOU PICK A TOPOLOGY: MAP THE IMPLICIT ORGANIZATION

Run this next, before the topology choice below, whenever an agent is replacing a human-occupied role rather than filling an empty one. Skip it when no human currently does the job.

Every company runs two organizations at once. One is documented: procedures, checklists, anything an agent can read. The other is implicit: tacit knowledge, motivational alignment, and the professional discretion a person applies without writing it down. The implicit half stays invisible because humans compensated for its gaps automatically, so nobody noticed it needed compensating for.

**The rule.** An agent executes the documented spec faithfully, and that is the problem, not the fix. Correctness against an incomplete spec produces confidently wrong outcomes at machine speed. In a multi-agent pipeline these errors compound silently before anyone notices. A cited multi-agent failure rate runs 40 to 80 percent (⚠ single study), cross-checked against a separate MAST taxonomy study at 41 to 86.7 percent: treat the two as the same finding family, not as independent confirmation of each other.

**The mechanism, worked.** Ramp's expense agents did this correctly (◆ company-disclosed: a 10 to 15 percent escalation rate, roughly an 85 percent reduction in manual review). The approach was neither "add an agent to the existing process" nor "reengineer around only the documented process." Ramp mapped the implicit organization first, then redesigned around both halves together: informed reengineering.

The pre-design worksheet, run before the orchestration-pattern choice:

- What do people in this role notice that never shows up in the data?
- What do they care about beyond what the job description says?
- When do they slow down, and why? Deliberate friction is often where judgment lives.

**Condition this is wrong.** The worksheet assumes tacit knowledge can be articulated on request. That assumption is often false by definition: the deepest tacit knowledge resists recall and surfaces only in the moment it is needed, not in an interview about it. Treat the worksheet as a partial elicitation tool, not a complete one. The only success case cited here, Ramp, is also low-stakes, high-volume, and transactional; the method is unproven in high-stakes, relationship-driven domains and should not be assumed to transfer there untested.

## SORT SEAM PROBLEMS INTO WHAT YOU CAN CHANGE AND WHAT YOU CAN ONLY MANAGE

Distributed teams blame collaboration failures on cultural difference. **The usual cause is organizational design, and the useful move is sorting the factors by how much control you actually have.** The same sort works on machine seams.

**Three you can manage and never really change (friction amplifiers):** time zones, language, and country culture. Manage time zones with overlap windows and asynchronous defaults. Manage language with written-first communication and an explicit glossary. Manage country culture by naming the difference out loud. **None of the three is yours to redesign.**

**Four you can change through deliberate design (trust-and-alignment multipliers):** headquarters-versus-region power dynamics, company culture, market knowledge, and process. Who has to ask permission and who is told afterward. Who is allowed to know what the customer said. Handoffs, decision rights, escalation paths.

**The rule: stop spending design effort on the amplifiers and spend it on the multipliers.** A team that keeps trying to fix time zones and never touches the power dynamic is optimizing the immovable half.

**The translation to a multi-agent system, which is why this sits here:**

| Amplifiers (manage) | Multipliers (design) |
|---|---|
| Latency between components | Ownership of shared state |
| Model-vendor behavior differences | Who can override whom |
| Format constraints of an external API | Which component sees which context |
| Rate limits and quotas | The handoff contract itself |

**The right-hand column is where your coordination failures actually come from**, and it is the column teams under-invest in because the left-hand column is more visible and easier to complain about.

**The diagnostic for either kind of seam:** list your last five coordination failures and sort them into the two columns. If most land on the left, you have a design problem you have been describing as an environment problem.

*(Source: an HBR piece on global team collaboration, Jul 2026 — ⚠ framework-tier, no measured population. **The article's own chart placing the seven elements on a control spectrum did not survive into the captured PDF**, so the two buckets and their members are recovered from the prose and are complete, while the ranking within each is unavailable. The multi-agent translation is this corpus's. Falsifier: a distributed team whose collaboration improved most from work on the three amplifiers rather than the four multipliers.)*

## THE COORDINATION TOPOLOGIES

Pick the simplest shape that fits; escalate only when it demonstrably fails.

- **Supervisor / star** — one orchestrator delegates to specialists and owns the final decision. The default for enterprise workflows with clear domain boundaries. Cost: the orchestrator is a single point of failure and a bottleneck; keep it thin.
- **Pipeline** — A→B→C, each stage transforms and passes on. Simple and legible; failures propagate downstream, so each stage needs a validated handoff.
- **Fan-out / fan-in** — one agent splits work to many parallel workers, one merges the results. Fast, but the *merge* is where sub-agent divergence bites — the merge step needs a rule for "what to do when the pieces disagree," not just concatenation.
- **Peer-to-peer** — agents negotiate directly (often across vendors via A2A). Loosely coupled at org scale, but the trust and versioning surface is widest; use only when a central orchestrator genuinely can't sit in the middle.

*(Vendor-named patterns — CodeAct, Magentic, computer-using, SLM-micro — are these topologies dressed in a product's clothes; classify a vendor's system by which topology it actually is, and by which model-under-which-harness runs each node, per `agent-harness`.)*

## MODEL DIVERSITY: A DESIGN AXIS ORTHOGONAL TO TOPOLOGY

**The rule.** Agent-team diversity that actually decorrelates errors is a stack property (which foundation model, which training data, which lab's alignment approach), not a prompted-persona property. Two audited papers back this: a DEI framework scoring a 34.3 percent versus 27.3 percent resolve rate on SWE-Bench Lite (✅ audited, arXiv:2408.07060), and a 2-vs-16-agent diversity-scaling study where full-diversity 2-agent configurations beat 16-agent homogeneous configurations (✅ audited, arXiv:2602.03794).

**The mechanism.** A costume change is not cognition. Same-model role separation, Planner, Generator, and Evaluator all running on one model, still shares that model's training data and alignment approach. The Evaluator then misses exactly what the Generator was trained to miss. Functional role separation buys organizational clarity. It does not buy error independence. Only cross-lab separation decorrelates errors, because that is the only split that changes what each agent was actually trained to get wrong.

Add cross-lab model diversification as a named harness-design axis, separate from and orthogonal to the functional role separation already covered under `agent-harness`. The canonical illustration: a reasoner, an evaluator, and a generator, each on a different lab's model. This combination is asserted here as sound design logic, not as a specific combination that has been independently tested; say so when you propose it.

**A board-ready governance device from the same source.** A model portfolio governance policy: a board-level cap on the percentage of critical agentic decisions allowed to depend on a single vendor's model, framed the way procurement already frames supplier-concentration risk.

**Condition this is wrong.** A firm with one dominant, well-understood failure mode that a homogeneous, well-evaluated pipeline already catches reliably gains nothing here. Diversification only adds handoff friction and integration failure points, with no decorrelation benefit to offset them. There is also a real ceiling here: cross-lab diversification decorrelates a firm's own pipeline, but does nothing to decorrelate that firm's aggregate behavior from the market's if every competitor is drawing agents from the same three frontier labs. Diversification within a pipeline is not diversification from the market.

## THE HUMAN SIDE OF THE SEAM: using AI as a team, not as a group of individuals

Most guidance treats an assistant as something one person types into. **In a room, that default quietly makes the typist the sole author and everyone else an audience.** Three practices change it, from a five-month field experiment with 60 managers across 12 companies in teams of three or four.

1. **Engage with the AI as a team.** Everyone introduces themselves and their role at the start, so the model addresses the group's collective context rather than one person's. Practically: a five-minute briefing round at the top of the meeting.
2. **Use role fluidity deliberately.** Assign and **rotate** the AI through several personas in one session (stakeholder, challenger, customer, competitor) rather than fixing it as note-taker for the hour. Practically: a scheduled 15-minute **challenge slot** near the end where it is explicitly cast as skeptic.
3. **Keep ownership collective.** Treat prompting as a group act. **Pause before submitting, debate the framing, judge the output together** rather than reacting to whatever appears. Practically: prompts that force the pause, such as "wait for our decision before proceeding."

**The self-audit that makes it stick**, run on the session transcript afterwards: did we introduce ourselves as a team? Did we give the AI more than one role? Did we articulate reasoning, or fall back on minimal responses? The model itself can run this audit on its own transcript.

**Why this belongs in a multi-agent skill.** Practice 3 is the human twin of the collective-ownership problem this skill already names at the machine seam. **A group that does not own its prompt has the same failure as a pipeline with no named owner of the handoff**: everyone assumes someone else is accountable for what came out.

## STABLE CORE, FLEXIBLE PERIPHERY

Two recommendations in this skill can read as competing recipes: type the agents by cognitive role, and diversify them across vendors. **They resolve into one two-tier design.**

**Keep the core stable and let the periphery vary.** Familiarity between components is itself a performance variable. In operating-room research, the same case took **20 to 40 minutes longer** depending on which team ran it, and a pilot that deliberately staffed for pairing familiarity moved on-time starts from **85% to 96%** with no new technology.

**The transferable rule: track how often a specific combination has run together**, and treat a low-familiarity combination as elevated risk. A prompt version, a model, a tool chain and a human reviewer that have never executed together are a novel configuration, whatever each component's individual track record. Route those to conservative fallbacks or closer monitoring, exactly as the hardest surgical cases were staffed most deliberately.

*(Sources: the three practices, Rosani, Farri, Trabucchi & Buganza, HBR, May 2026 — ◆ five-month field experiment, 60 managers, 12 companies, 30 hours of sessions, **no control group and no outcome metric reported**, so carry the practices and not a claimed effect. The operating-room figures are ◆ single-hospital, from HBR, May 2026; the pairing-familiarity translation to pipelines is this corpus's.)*

## ONE COMPANY RUNS SEVERAL GOVERNANCE REGIMES AT ONCE

**The assumption worth breaking early: that governance is one dial the company sets.** It is not. A single company usually runs several go-to-market motions concurrently, and **each needs a different governance architecture, not a different setting on the same one.**

| Motion | What it optimizes | Typical shape |
|---|---|---|
| **Digital-first** | efficient scale across high volume | endless-assortment e-commerce |
| **Hybrid** | synchronizing digital and human channels | distributed mid-sized accounts |
| **Relationship-led** | trusted, high-impact enterprise relationships | a named account team of seven or more roles, supported by one digital assistant |

**Why this matters for a multi-agent system.** An agent in the digital-first motion can hold broad decision rights, because volume is high and a single error is cheap and reversible. **The same agent with the same rights inside a relationship-led enterprise account is a liability**, because one wrong action reaches a named human who will remember it.

**So the seam-ownership question below has a prior question underneath it: which motion is this seam in?** Assign decision rights per motion first, then per seam. One platform-wide policy is too loose for the enterprise accounts and too tight for the volume business at the same time.

**The named barrier, worth quoting to anyone pushing a single standard.** The authors' research finds the conflict between standardized platforms and commercial-operating-need alignment is **a primary barrier to performance.** Standardization is a trade against fit, not a free win.

**When this is wrong:** a company genuinely running one motion should run one regime. Three regimes for one motion is overhead pretending to be rigor.

*(Source: HBR, "Tailor Your Digital Strategy to Reach Every Customer," Jun 2026 — ⚠ framework-tier. The three-model typology is the authors' own, with named company illustrations and no comparative outcome data. The typology is the useful part; mapping it onto agent governance is this corpus's.)*

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

**A hidden cost the same research surfaces: bridge people burn out at a higher rate.** In organizations, the person who absorbs the unglamorous work of translating context across a boundary (team, time zone, or language) churns out more than peers doing similar work without that translation load. A separate HBR piece on global team collaboration reports this from the author's own consultancy data (HBR, Jul 2026; ◆ claimed, undisclosed method, no published scale, not independently reproducible). Treat it as directional only: cite the pattern, never a number. The same role exists at an agent-to-agent or agent-to-system seam. Whoever is named, or worse, informally expected, to own the translation between two agents or two systems carries the same hidden-load risk if the responsibility is never made official. Mechanism: coordination load gets allocated by capability, so the most capable owner keeps absorbing more of it until they leave or burn out. No single allocation decision along the way looks wrong, which is why an audit that only hunts for a bad decision never catches the pattern forming. Cheap diagnostic: ask both sides of a seam, two teams, or a team and the agent-integration owner, to rate trust and influence separately. High trust paired with low influence ("respected but underpowered") is the dangerous signature. It predicts the owner will fabricate a justification rather than escalate honestly when something breaks at the seam. When wrong: a bridging role with no formal recognition whose attrition matches non-bridging peers would break the load-selects-for-departure claim. Check turnover data before assuming the risk applies.

## VALUE CAPTURE IN THE ECOSYSTEM, AND A LIMIT ON PROVIDER SUBSTITUTABILITY

**Value in an agent ecosystem often accrues to the infrastructure around the agents, not to the agents themselves.** A single researcher proposed a taxonomy for this at an MIT Sloan talk in July 2026. He runs the initiative his forecast favors, a conflict of interest he discloses himself, and the talk carries no data and no study behind it. Cite his four categories, never his forecast:

- **Identity and discovery** — proving which agent this is, and finding the right one.
- **Trust and reputation** — scoring an agent's reliability before delegating to it.
- **Insurance, repair, and legal** — who pays and who is liable when an agent's action causes harm.
- **Micropayments** — the machinery for agents to pay each other per call.

These four are where value is likely to concentrate regardless of which agents win. Mechanism: agents themselves are easy to swap and commoditize, but the infrastructure every agent needs to interoperate is not. When wrong: in a closed, single-vendor ecosystem with no external agent interoperability, none of these four exist as separate value pools. They are internal platform features, and the taxonomy does not apply.

**A related caution, on an assumption this skill otherwise takes for granted: that a provider is swappable.** Peer-to-peer topology and the fallback pattern under isolation boundaries both assume a failed or degraded provider can be replaced by another one with equivalent capability. A sovereign-AI survey (Accenture/MIT SMR, n=1,928 executives, ◆ single-vendor-commissioned) found that assumption can collapse where legal data-residency requirements apply. "N interchangeable providers" shrinks to N=1 inside a regulated jurisdiction, and failing over to a provider outside it becomes the compliance violation, not the fix. Mechanism: a model-agnostic, multi-provider architecture removes technical lock-in but not legal lock-in, and the two get conflated because both look like the same interface running on a different backend. When wrong: this caution does not apply outside regulated data-residency regimes, or where every candidate provider already runs compliant infrastructure inside the same jurisdiction. Check the regulatory map before assuming full substitutability.

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
7. For that owner: do trust and influence match? A high-trust, low-influence seam owner is a departure or fabrication risk waiting to happen.
8. Does the design assume any provider is swappable? If a regulated jurisdiction is involved, confirm failover would not itself be a compliance violation.
9. Is an agent replacing a human-occupied role? If so, has anyone run the implicit-organization worksheet before picking a topology, and named where it's still an incomplete elicitation?
10. Is the team's diversity a same-model persona split, or a real cross-lab split? If every agent shares a lab, functional roles are not buying error independence.

## QUALITY GATE

- [ ] The multi-agent gate passed: distinct roles, an eval per sub-agent, and failure-attribution to the correct agent — or it stays single-agent.
- [ ] The coordination topology is named (supervisor / pipeline / fan-out-fan-in / peer) and is the simplest that fits.
- [ ] Every mutable resource has exactly one owner; no two agents write it uncoordinated.
- [ ] Each dependency has a handoff protocol, and handoff *content* is validated, not just arrival.
- [ ] Every fan-out has an explicit merge rule for disagreement.
- [ ] Each agent has isolation boundaries; cascades are detected as a chain and broken.
- [ ] The most-likely failure mode is identified and its safeguard shipped first.
- [ ] A named human owns the seam (the Bridger).
- [ ] That owner's trust and influence have been checked separately; no high-trust, low-influence pair is going unaddressed.
- [ ] Provider substitutability has been checked against jurisdictional data-residency requirements, not assumed.
- [ ] If an agent replaces a human role, the implicit-organization worksheet ran before the topology was picked, not after.
- [ ] Team diversity has been checked at the model-and-lab level, not just at the prompted-persona level.

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
