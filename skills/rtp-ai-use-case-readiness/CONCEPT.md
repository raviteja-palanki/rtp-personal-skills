# AI Use Case Readiness — Concept Guide

## FIRST PRINCIPLES

The default move in a hype cycle is to ask "where can we deploy an agent?" The better question is "what is the lowest-autonomy design that captures the value?"

In AI, maximum autonomy is not the goal. Right-sized autonomy is. Most organizations default to building agents when the answer is often rules, workflow automation, or a copilot. This happens because teams conflate "interesting to build" with "necessary to build." The atomic insight: **the highest-value use of AI is often the lowest autonomy level that captures the value.**

This matters because autonomy has a cost. Agents require strong controls, heavy monitoring, rollback design, governance frameworks, and teams to maintain them. Build too much autonomy too early and you've increased engineering burden by 10x while solving a problem that rules or a workflow could have handled. Decompose first. Then let the problem dictate the autonomy level, not the technology.

## DUAL DEFINITION

**Business definition:** AI use case readiness is the discipline of matching business problems to the minimum viable autonomy level—determining whether a workflow needs no AI, deterministic automation, assistive AI, human-in-the-loop execution, or autonomous agents. It prevents the most expensive AI product mistake: building sophisticated autonomy for problems that don't need it.

**Technical definition:** A structured assessment of a workflow's knowledge tacitness, error cost, verifiability, environment stability, and execution rights, producing a defensible recommendation for the safest autonomy level now and the conditions required for higher autonomy later.

## THE TRAP (Expanded)

Three incentive misalignments push teams toward over-automation:

**The novelty bias.** Agents are newer, more interesting to build, and more impressive in demos. A team that could solve a problem with rules + extraction feels like they're "leaving value on the table" if they don't attempt an agent. But leaving value on the table is often cheaper than deploying the wrong automation at the wrong autonomy level.

**The autonomy mirage.** A problem looks harder than it is because the team hasn't decomposed it. They see "customer support workflow" as one blob. Decompose it: routing (rules), extraction (AI component), sentiment detection (classifier), response drafting (LLM), escalation (hybrid). Suddenly the blob becomes seven distinct problems, and only two might need agents.

**The control cost invisibility.** Deterministic automation and assistive AI are cheap to pilot. Agents that require approvals, rollback, monitoring, policy, and audit trails are not. A team that pilots an agent at a hackathon later discovers production requires 6 months of control design. By then, stakeholder expectations are set and the conversation becomes "how do we make it work?" instead of "should we make it work this way?"

The common pattern: a team proposes "an AI agent that does X." Nobody asks whether X needs agency, whether the operating environment is stable enough for autonomous execution, or whether a human-in-the-loop design with stronger oversight would be safer and less expensive.

## INTELLECTUAL LINEAGE

- **Anthropic's "Building Effective Agents"** — Start simple. Add complexity only when justified. The clarity on when to use simple chains vs. multi-step agents directly informs autonomy decisions.
- **OpenAI's Agents SDK** — Handoffs and guardrails as first-class primitives. The insight: autonomy without guardrails is recklessness. Build controls first.
- **Google DeepMind Frontier Safety Framework** — Scaled safeguards with capability. More capable systems require proportionally stronger safety controls, not weaker ones.
- **Shreyas Doshi** — Product sense as the #1 AI PM skill. The distinction between the problem (what users need) and the solution (which technology). Respect that distinction ruthlessly.
- **Clayton Christensen** — Frames of reference for learners. Different problems demand different knowledge levels. Don't apply high-autonomy designs to low-frame-of-reference problems.
- **Kapil Gupta** — Diagnosis before prescription. Diagnose what the work actually needs before prescribing a technology level. Most teams skip this.
- **Charlie Munger** — Inversion thinking. Instead of asking "where should we add autonomy?", ask "where would high autonomy make this worse?"
- **BCG ASPIRE framework** — Organizational readiness dimensions. Autonomy requires not just technology but governance, skills, data, and processes.
- **Factory AI's 5 levels of agent readiness** — A rigorous taxonomy of what each autonomy level demands operationally.
- **Knight First Amendment Institute** — Levels of autonomy for AI agents in high-stakes domains. The baseline: autonomy in high-stakes work requires iron-clad reverification and rollback paths.

## REAL-WORLD EXAMPLES

**Example 1: Invoice matching.** A team proposed an agent that would match incoming invoices to purchase orders, approve them, and route them for payment. Deep dive revealed the work was 85% extraction (structured data from unstructured invoice PDFs) and 15% matching logic (lookups on PO number, amount, vendor, date). The extraction needed AI. The matching did not. Solution: AI component for extraction + simple rules for matching + human review on exceptions. Autonomy level: copilot with human-in-the-loop approval, not an agent. Cost: 40% of the original estimate.

**Example 2: Customer support triage.** A support team asked for an agent to route incoming tickets. Decomposition revealed: intake (extraction), routing (rules + classifier), escalation paths (rule-based), and human handoff. The team built a copilot instead. It shows the customer what category the ticket belongs in, suggests a routing destination, and flags urgency signals. The agent would have meant building action rights (touching production ticket systems), monitoring, and rollback. The copilot gave 80% of the value with 20% of the control burden.

**Example 3: Security incident triage.** A security team needed to ingest alerts from multiple sources, correlate events, prioritize, and recommend response actions. This case genuinely needed some agency: environment was dynamic (new threat types), knowledge was tacit (expert judgment on priority and response), and multi-step planning mattered. Recommendation: bounded agent with tool limits (can read alerts and suggest, cannot execute remediation), checkpoints (human approves response), strong telemetry, and kill switch. Autonomy level: 5/7 (bounded agent). Why not 7? Because error cost and consequence magnitude were both high.

**Example 4: Cross-system scheduling.** A company needed to schedule meetings across four calendar systems with different APIs, timezone handling, and delegate rules. The knowledge was explicit (API specs, business rules), error cost was moderate (wrong room, wrong time), environment was stable (people don't change as the agent runs). This was a solid agent candidate. Autonomy level: 6/7 (semi-autonomous with strong monitoring).

**Example 5: Commercial negotiation.** A vendor asked for an agent to conduct price negotiations on their behalf. Deep analysis showed the work was tacit (reading counterparty signals, building trust, managing ego), high-error-cost (bad deals compound), and involved relationship management (accountability matters). Recommendation: human-led with AI-assistive copilot. The AI suggests talking points, flags market-rate comparisons, drafts language. Humans execute and approve. Why no autonomy? Because negotiation hides relationship and accountability that should remain visible.

## THE ANSWER NUDGES INNOVATION

This repository teaches something unprecedented: not just how to ask diagnostic questions about autonomy, but how to think through the answers. Other AI PM frameworks ask "Is this a good agent candidate?" This one teaches you to diagnose the answer yourself using matrices, dimension scoring, and clear tradeoff reasoning.

That matters because it flips the dependency. Instead of relying on a consultant, a framework, or a senior person's gut call, a product manager can now walk through a structured diagnosis and defend their recommendation. The framework doesn't make the decision for you. It makes your thinking transparent—which means it can be challenged, refined, and taught to others.

Most existing agent frameworks assume the answer is "build an agent." This one assumes the answer is "find the minimum viable autonomy level." That's a different philosophy, and it shows up in every step.

## PRODUCTION DISCIPLINE

In high-stakes AI product decisions, use case readiness assessment becomes the governance gate that prevents expensive mistakes:

**The decomposition discipline.** Before estimating effort or assigning resources, decompose the workflow into sub-tasks. Most good solutions are hybrids: rules for the stable parts, AI for ambiguous reasoning, humans for high-risk approvals. If you skip decomposition, you'll spend 8 weeks building a monolithic agent when you could have spent 4 weeks building a hybrid system that works better.

**The autonomy floor vs. ceiling distinction.** State both explicitly. If the floor is above the ceiling, you have three options: human-in-the-loop design, narrower task boundaries, or stronger controls. This gap is often the most important insight a readiness assessment produces.

**The economic filter.** More autonomy is more work. Heavyweight control (approvals, audit, recovery) is more work. If the use case is low-frequency, small-scale, or low-leverage, higher autonomy will never make economic sense. Do the math before designing controls.

**Red flags that readiness assessment is being skipped:**
- "The demo works, so let's ship it" (demos are best-case scenarios)
- "We have an agent framework, so let's use it" (frameworks are tools, not goals)
- "Competitors are using agents for this" (different problem, different readiness, different controls)
- "More autonomy is always better" (it's not; right-sized autonomy is better)

## FURTHER READING

- Anthropic, "Building Effective Agents" — On simplicity as a virtue in agent design
- Shreyas Doshi, "Product Sense" essays — On problem obsession vs. solution obsession
- Clayton Christensen, "Competing Against Luck" — On understanding what jobs customers need done
- Kapil Gupta, *A Master's Secret Whispers* — On diagnosis before prescription
- Charlie Munger, *Poor Charlie's Almanack* — On inversion thinking and avoiding mistakes
- Knight First Amendment Institute, "AI Autonomy Levels" — On governance frameworks for high-stakes AI
- BCG, ASPIRE framework — On organizational readiness for AI transformation
