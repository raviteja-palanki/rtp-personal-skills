---
name: rtp-agent-harness
description: 'Harness architecture: Planner/Generator/Evaluator, eval separation, sprint contracts, context, communication. Use when: multi-agent pipelines, harness decision, costing. Triggers: ''agent harness'', ''planner generator evaluator'', ''orchestrate agents'''
---
# Agent Harness Engineering

## DEPTH DECISION

**Go deep if:** Designing a multi-agent system where quality must exceed single-agent capability, or when evaluating whether the complexity and cost of a harness is justified. **Skim to diagnostic questions if:** Quick check on whether your feature needs a harness vs single agent. **Skip if:** Single-turn Q&A, simple retrieval, or early exploration where you haven't validated the problem yet.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE FOUR-LAYER MODEL (Where the Harness Lives)

Anthropic's March 2026 NIST RFI and April 2026 policy research established the canonical framing: **Agent = Model + Harness + Tools + Environment**. The model supplies intelligence. The harness supplies orchestration, continuity, guardrails, and self-correction. Tools supply the actionable surface. The environment supplies the hard runtime boundaries.

These layers are distinct because failures cascade across them in ways that model-centric thinking misses. A well-trained model can still be exploited through a poorly configured harness, an overly permissive tool, or an exposed environment. The harness is the *control plane* — it doesn't replace the model's intelligence, expose raw tools, or own the sandbox. It coordinates all three.

**Why this matters for your harness decision:** When an agent fails, diagnose by layer. Most production failures are harness failures (poor session continuity, missing guardrails, no evaluation loop) — not model failures. Upgrading the model when the harness is broken is the most expensive mistake in enterprise AI.

**The nested disciplines:** Prompt engineering (single-turn) → Context engineering (multi-turn, single agent) → Harness engineering (multi-agent, multi-session) → Environment engineering (runtime boundaries, persistence). Each layer contains the previous ones. Context engineering lives *inside* the harness — the harness decides when and how context is managed. Understanding this progression prevents the common mistake of treating them as separate concerns.

## THE TRAP

You assume more agents = better output. **Mistake**: Harness systems are 10-22x more expensive, 5-10x slower, and introduce cascade failure modes that don't exist in single-agent systems. The trap is **complexity theater** — building an impressive architecture when a well-prompted single agent with good context engineering would deliver 80% of the quality at 5% of the cost.

### The Hidden Trap: Evaluator Hallucination

The most dangerous assumption in harness design is that the evaluator agent is trustworthy. When you separate generation from evaluation (GAN-inspired pattern), you've solved the "agents praise their own work" problem — but created a new one: **evaluators can hallucinate that bad work is good**. Your evaluator needs its own quality checks (deterministic graders, code-based assertions, Playwright-style functional tests), or you've just moved the problem one agent downstream.

## THE PROCESS

### 1. The Harness Decision: Single Agent vs Multi-Agent

**Use a harness when ALL THREE are true:**
- Quality requirement exceeds what a single agent can achieve with best-in-class prompting
- The task is naturally decomposable into distinct roles (planning, execution, evaluation)
- You can afford 10-22x the cost and 5-10x the latency

**Stay single-agent when ANY of these are true:**
- Task is achievable with good context engineering + single model call
- Latency budget is <10 seconds
- Cost per query must stay under $0.10
- You can't staff ongoing harness maintenance

### 2. The Initializer Pattern (Before the First Sprint)

Before ANY agent begins work, a mature harness runs an **initializer step** — an agent (or the same model wearing the "senior architect" hat) that reads the current state and creates clean starting conditions. This is the single highest-leverage harness pattern, responsible for taking Anthropic's long-running agents from ~45% to 92%+ success rates.

**What the initializer does:**
1. Reads the current state (files, git history, last progress note)
2. Creates or updates a requirements/feature list with every remaining task and success criteria
3. Writes a progress artifact (`claude-progress.txt` or equivalent) documenting exactly where work left off
4. Commits a clean git snapshot as a rollback point

**Why this matters:** Without an initializer, every new session starts from scratch — the agent has no memory of yesterday. With an initializer, the same model, same tools, same sandbox suddenly achieves 2x+ success rates because it starts with perfect context about what's been done and what's left.

**The cost is negligible:** A few hundred extra tokens at session start. The savings from eliminated rework dwarf this. For enterprise workflows spanning multiple sessions (overnight reconciliation, multi-day compliance audits), the initializer is non-negotiable.

**Spec it in every RFP:** "How does your agent handle session continuity? Show me your initializer pattern and progress artifact strategy."

### 3. Three-Agent Architecture (Anthropic Pattern)

| Agent | Role | Context | Output |
|-------|------|---------|--------|
| **Planner** | Converts brief → spec with testable criteria | Full brief, constraints, examples | Detailed spec with acceptance criteria |
| **Generator** | Implements the spec in iterative sprints | Spec + tool access + file system | Working output (code, content, artifacts) |
| **Evaluator** | Tests output against spec criteria | Spec + output + eval rubric | Pass/fail per criterion + improvement notes |

**The GAN Insight:** Separating generation from evaluation prevents the "self-praise" problem. An agent evaluating its own work is like a student grading their own exam — they'll find reasons to pass. The evaluator must be architecturally separate with its own context.

### 3. Sprint Contracts

Before the Generator begins work, the Generator and Evaluator negotiate explicit success criteria:

```
Sprint Contract:
- Criterion 1: [Specific, testable condition] → Pass/Fail
- Criterion 2: [Measurable threshold] → Pass/Fail
- Max iterations: [3-5 typical]
- Kill condition: [When to stop iterating and escalate]
```

**Why contracts matter:** Without pre-negotiated criteria, the evaluator invents criteria post-hoc, the generator never converges, and you burn 15 eval rounds at $0.80/round.

### 5. Deterministic Lifecycle Hooks

Lifecycle hooks are fixed-order checklists that always execute at specific moments — like an airplane pilot's pre-takeoff and post-landing procedures. The harness hard-codes these regardless of what the model decides to do.

**Session-start hooks (always run first):**
- Load persistent rules (CLAUDE.md, policy files)
- Read progress artifact from last session
- Run quick self-check for missing data or stale state
- Verify tool access and permissions

**Session-end hooks (always run last):**
- Write final progress summary
- Commit clean git snapshot
- Run lightweight validation (did we complete what we planned?)
- Archive logs and export to observability

**Sprint-boundary hooks (between PGE cycles):**
- Reset context (Anthropic finding: resets > compaction)
- Load only the spec + current sprint state
- Verify sprint contract criteria are still valid

**Why hooks matter for governance:** They cost almost zero extra tokens but create perfect consistency. Policy updates propagate instantly. Audit logs are always clean. The model never has to "remember" to do these things — the harness enforces them automatically. Compliance teams love hooks because they're deterministic in a probabilistic system.

### 6. Context Management for Harnesses

**The Pre-Rot Threshold:** Models degrade at 50-60% of max context, not 100%. Plan your context budget accordingly.

| Strategy | When to Use | Mechanism |
|----------|------------|-----------|
| **Context resets** | Between sprints | Clear context, load only spec + current sprint state |
| **File-based communication** | Agent-to-agent handoffs | Write state to files; next agent reads fresh |
| **Shared state file** | Coordination across agents | Single source of truth (progress.md, state.json) |
| **Compaction** | Within long sprints | Summarize context, discard verbose history |

**Critical Anthropic finding:** Context resets > compaction. A fresh context with relevant state loaded from files consistently outperforms a compacted context with accumulated noise.

### 5. Harness Cost Economics

**Single Agent (baseline):**
- 20 minutes of work, ~$9 total
- Quality: Good for straightforward tasks

**Full Harness (Planner + Generator + Evaluator):**
- 6 hours of work, ~$200 total
- Quality: Dramatically better for complex, multi-criteria tasks
- Cost breakdown: Planning ~$15, Generation ~$120, Evaluation ~$65

**The 22x Question:** Is the quality improvement worth 22x the cost for YOUR use case? Answer with this matrix:

| Task Complexity | Quality Gap (Single vs Harness) | Recommendation |
|----------------|-------------------------------|----------------|
| Simple (one clear output) | <10% improvement | Single agent |
| Medium (multi-step, some ambiguity) | 15-30% improvement | Single agent + eval pass |
| Complex (multi-criteria, high quality bar) | 40-60% improvement | Full harness |
| Critical (safety, legal, financial) | Harness or human review | Full harness + human gate |

### 6. Failure Modes Specific to Harnesses

| Failure | Cause | Detection | Mitigation |
|---------|-------|-----------|------------|
| **Infinite eval loop** | Evaluator criteria too strict or shifting | Count iterations per sprint; alert at max | Sprint contracts with max iterations + kill condition |
| **Evaluator hallucination** | Evaluator passes bad work confidently | Cross-validate with deterministic checks | Hybrid eval: LLM + code-based graders |
| **Context saturation** | Accumulated state exceeds useful context | Monitor token count; track quality vs context size | Hard resets between sprints; file-based handoffs |
| **Coordination drift** | Planner spec diverges from generator understanding | Diff spec against generator's interpretation | Shared state file; planner reviews generator plan |
| **Cost explosion** | Eval rounds multiply beyond budget | Token metering per sprint; cost alerts | Budget caps per sprint; escalate-to-human threshold |

### 7. Four Quality Dimensions (Anthropic Framework)

Evaluate harness output across all four — not just "does it work":

| Dimension | What It Measures | How to Eval |
|-----------|-----------------|------------|
| **Design Quality** | Does the output solve the right problem well? | Human review against spec |
| **Originality** | Is it creative/novel or template-derivative? | Comparative analysis |
| **Craft** | Attention to detail, polish, edge cases | Code-based checks + human spot-check |
| **Functionality** | Does it actually work end-to-end? | Automated functional tests (Playwright-style) |

### 8. Model Evolution Impact

Your harness must survive model upgrades. Design for it:

- **Pin model versions** per agent role (don't let one upgrade break the chain)
- **Eval regression suite** that runs before any model swap
- **Agent role abstraction** so you can swap models per role (cheaper model for planning, frontier for generation)
- **The harness IS the moat** — when the model improves, your harness extracts more value. Competitors with raw API calls get the same model but without the orchestration.

### The Self-Dissolving Harness (Model-Harness Training Loop)

The deepest insight from April 2026 practitioner discourse: **what the harness does today gets trained into the model tomorrow**. As models internalize capabilities that the harness currently scaffolds (better memory, longer context, self-correction), some harness components become unnecessary. A well-designed harness generates traces that feed model fine-tuning, which makes the harness simpler, which generates better traces — a compounding loop.

**What this means for design:**
- Build harnesses that can be SIMPLIFIED, not just extended. Design each component as removable.
- Treat observability as a data flywheel: every harness trace is potential training data for model improvement.
- Expect 15-30% of harness scaffolding to become unnecessary within 12 months as models improve.
- The winning strategy is not a static harness but a *meta-harness* — a decoupled design that evolves as models internalize capabilities. Anthropic's Managed Agents is exactly this: a harness that can improve underneath you without breaking your interfaces.

**The paradox for PMs:** You're investing in infrastructure designed to become unnecessary. That's not a bug — it's the feature. The harness's value is precisely that it's temporary: it solves today's reliability gap while feeding the improvement loop that closes the gap permanently. Organizations that skip the harness waiting for "smarter models" never collect the traces that make models smarter for THEIR use cases.

## DIAGNOSTIC QUESTIONS

1. **"Does this task genuinely need multiple agents, or am I adding complexity for its own sake?"** (If a single agent with better prompting could get to 80%, start there.)
2. **"What's my cost per successful outcome with vs without a harness?"** (Run the math. If harness is 22x more expensive but only 30% better, reconsider.)
3. **"How will I know if the evaluator is wrong?"** (If the answer is "I won't," you need deterministic cross-checks.)
4. **"What's my sprint contract for this task?"** (If you can't write explicit pass/fail criteria before generation begins, the evaluator will invent them — badly.)
5. **"How do I handle context across agent boundaries?"** (File-based > shared memory > context passing. Document the handoff contract.)
6. **"What happens when one agent in the chain fails?"** (Circuit breaker? Fallback? Human escalation? Document it.)
7. **"Is my harness model-agnostic?"** (Can I swap the generator model without rebuilding the pipeline? If not, you've coupled to a vendor.)
8. **"What's my context durability rate?"** (% of tasks completing successfully after 50+ tool calls without human restart. Target: >85%. This is your leading indicator of harness health — more predictive than one-shot accuracy.)
9. **"Do I have an initializer pattern?"** (If sessions start cold without reading prior progress artifacts, your multi-session success rate will be <50%. The initializer is the highest-ROI harness addition.)
10. **"Should I build, buy, or hybrid?"** (Managed harnesses like Anthropic Managed Agents handle orchestration + sandbox + recovery. Your outer layer adds domain-specific governance. Hybrid is the Fortune 100 default for 70-80% of use cases.)

## OUTPUT FORMAT

```
## Agent Harness Spec: [Feature Name]

Architecture Decision: [Single Agent / Single + Eval Pass / Full Harness]
Justification: [Why this complexity level is warranted]

Agent Roles:
| Agent | Model | Context Budget | Max Tokens | Role |
|-------|-------|---------------|------------|------|

Sprint Contract Template:
- Criterion 1: [testable condition]
- Criterion 2: [measurable threshold]
- Max iterations: [N]
- Kill condition: [when to stop]

Context Strategy:
- Agent-to-agent: [file-based / shared state / context passing]
- Reset cadence: [per sprint / per task / never]
- Pre-Rot Threshold: [X% of max context]

Cost Model:
- Per-task: $[X] (single agent) vs $[Y] (harness)
- Monthly at [N] tasks/day: $[Z]
- Break-even quality threshold: [what improvement justifies the cost]

Failure Modes:
| Mode | Detection | Mitigation | Owner |
|------|-----------|------------|-------|

Quality Dimensions:
| Dimension | Eval Method | Threshold | Weight |
|-----------|------------|-----------|--------|
```

## REALITY CHECK

- **Harness overhead is real.** Don't build a 3-agent system for a task a well-prompted single agent can handle. The best harness is the simplest one that meets quality requirements.
- **Evaluators are not oracles.** LLM-based evaluators have the same failure modes as generators. Cross-validate with deterministic checks (code runs? Tests pass? Output matches schema?).
- **Sprint contracts prevent drift.** Without explicit criteria negotiated upfront, eval loops diverge. Agents argue with themselves, burning tokens on style preferences rather than substance.
- **File-based communication scales.** In-context handoffs break at scale. File-based agent communication (Anthropic pattern) survives context resets and is auditable.
- **The 80/20 of harness ROI:** Most quality improvement comes from adding ONE evaluator pass, not from complex multi-agent orchestration. Start with single-agent + eval, only upgrade to full harness when eval reveals systematic gaps.
- **Harness maintenance is a product cost.** Budget for it. Prompt changes, model upgrades, eval dataset refreshes — someone owns this ongoing.

## QUALITY GATE

- [ ] Harness vs single-agent decision documented with cost-quality justification
- [ ] Agent roles defined with clear boundaries (no role overlap)
- [ ] Sprint contracts specify testable pass/fail criteria before generation
- [ ] Context strategy documented: handoff mechanism, reset cadence, Pre-Rot threshold
- [ ] Evaluator cross-validated with at least one deterministic check per criterion
- [ ] Cost model calculated: per-task, monthly, and break-even quality threshold
- [ ] Failure modes mapped with circuit breakers and escalation paths
- [ ] Model pinning strategy documented (per agent, upgrade protocol)

## WHEN WRONG

- Early exploration where you're validating desirability, not building production systems
- Simple tasks where single-agent + good prompting achieves sufficient quality
- Latency-critical features where harness overhead exceeds user tolerance
- When harness complexity becomes a delay tactic — "we need to design the architecture" as a way to avoid shipping
- Pre-PMF: don't build a harness until you know someone wants what it produces

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
