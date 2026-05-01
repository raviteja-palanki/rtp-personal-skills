---
name: rtp-ai-use-case-readiness
description: >
  Assess whether a use case needs no AI, rules, assistive AI, or autonomous agents.
  Hypothesis-driven autonomy analysis with 12 diagnostics, dual matrices,
  phased roadmaps, and governance readiness checks.
imports:
  - first-principles
  - determinism-compass
  - autonomy-spectrum
---

# AI Use Case Readiness Assessment

Determine the right-sized autonomy for a use case — not the maximum autonomy.

> "Almost any feature has some positive return. The only question that matters is: Is this the *absolute best* use of our finite resources?" — Shreyas Doshi

## Dynamic Assessment Architecture

This skill is NOT a linear checklist. It is a **parameter-driven diagnostic** where the orchestrator (or the PM using it) selects the relevant dimensions based on what's actually known about the use case.

**The core idea:** All 12 diagnostics, 9 scoring dimensions, and 4 meta-judgments below are PARAMETERS. The orchestrator reads the context, determines which parameters matter most for this specific use case, and activates only those. A quick assessment might touch 4-5 parameters. A comprehensive one touches all of them.

### How the Orchestrator Should Invoke This Skill

1. **Read the user's context** — what do they already know? What have they already decided?
2. **Select relevant parameters** — which diagnostic questions and scoring dimensions actually matter for this use case? Not all 12 are always needed.
3. **Ask the user** which aspects they want to explore: "For this use case, the most important dimensions are [X, Y, Z]. Should I also assess [A, B]?"
4. **Produce a focused output** — not every section of this skill, but the sections that drive the actual decision.

### Parameter Categories

| Category | Parameters | When to Activate |
|----------|-----------|-----------------|
| **Customer Reality** | Grounding Q1-Q6 (Phase 1) | Always — but carry forward if already established |
| **Risk Profile** | Q3 (cost of error), Q4 (verifiability), Q8 (rollback) | Always — these set the ceiling |
| **Knowledge Character** | Q5 (explicit vs tacit), Q6 (exception rate) | When autonomy level is uncertain |
| **Operational Fit** | Q7 (environment stability), Q9 (permissions), Q11 (telemetry) | When moving beyond Level 3 |
| **Economic Justification** | Q12 (ROI), scoring dimension for economic leverage | When justifying Level 4+ investment |
| **Agency Need** | Q1 (what's delegated), Q2 (advise/decide/execute), Q10 (smallest slice) | When distinguishing between levels |
| **Matrices & Scoring** | Knowledge × Cost matrix, Agency × Control matrix, 9 dimensions | Comprehensive assessments only |
| **Roadmap & Controls** | Phase 5 operating model, phased rollout | When the decision is "yes, build it" |

**The default for a quick assessment:** Customer Reality + Risk Profile + one matrix = enough to make a recommendation.
**The default for a comprehensive assessment:** All parameters + both matrices + phased roadmap.

---

## Five Phases — Enter at Any Point

| Phase | Purpose | When to Skip |
|-------|---------|-------------|
| **1. GROUND** | Anchor in the customer's reality | Already done in problem-ai-fit |
| **2. DIAGNOSE** | Decompose the use case; answer selected diagnostic questions | Quick pattern-match only → skip to Phase 3 |
| **3. ASSESS** | Score relevant conditions; place on matrices; surface assumptions | Already have scores → skip to Phase 4 |
| **4. DECIDE** | Set autonomy level; state as hypothesis; name trade-offs | Already have a recommendation → skip to Phase 5 |
| **5. PLAN** | Phased roadmap; operating model; controls | Need roadmap only |

---

## DELIVERABLE FORMAT

Before starting the analysis, ask:

> **What format would you like this assessment in?**
> 1. **Word Document** — Formatted report with embedded visuals. Best for sharing with stakeholders.
> 2. **Presentation** — Slide deck with key findings. Best for meetings and reviews.
> 3. **Both** — Full report + summary deck.
>
> *Default if no preference: Word Document.*

Follow the [Universal Deliverable Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md) for structure, formatting, visuals, and quality standards.

---

## THE TRAP

You will optimize for maximum autonomy instead of right-sized autonomy. The bias is **agentic hype** — agents are novel, well-funded, and feel like the future. You see a use case and immediately ask "can we make this autonomous?" instead of "what's the minimum autonomy that captures the value?"

Three variants to watch:

- **Autonomy theater.** You build a level-5 agent for work that's 80% stable rules and 20% exceptions. The agent works, but costs 10x more to maintain than a level-2 system. Impressive. Wrong.

- **Novelty bias on action rights.** LLMs can write SQL or invoke APIs, so you assume they should. Execution rights are a governance question, not a capability question. The system can act; that doesn't mean it should.

- **Cost of error amnesia.** You run 12 diagnostic questions about tacitness and variability. You forget question 3: "What happens if wrong?" A high-tacit, high-error domain needs human-in-the-loop design, not autonomous agency.

---

# PHASE 1: GROUND

## Anchor in the Customer's Reality

Before assessing autonomy levels, establish the human truth underneath the use case. This prevents the most common failure: designing an elegant autonomy framework for a problem that doesn't matter enough to solve.

**If you're coming from problem-ai-fit**, carry those answers forward — don't re-interrogate. If this is your starting point, answer these before proceeding:

> **1. Who exactly is the user of this workflow?**
> Not "the business" or "operations." Name the person: "Tier-2 support agents handling billing disputes for enterprise accounts."

> **2. What is the actual job — in their words?**
> Not "leverage AI for process optimization." What would they say at lunch? "I spend 3 hours a day copying data between Salesforce and our billing system, and I still make mistakes."

> **3. How do they do it today, and what breaks?**
> Every workflow has a current solution. Maybe it's manual. Maybe it's a spreadsheet. The current solution is your baseline — the thing you have to beat.

> **4. How painful is this? Where does it rank in their top 5 problems?**
> If this workflow is their #4 or #5 pain, even a perfect agent won't drive adoption. You're solving a "nice to have" at the cost of something that matters more.

> **5. What happens when the current process fails? Who gets hurt?**
> This grounds the cost-of-error analysis in reality. "When a billing dispute is misrouted, the customer waits 72 extra hours and we lose 15% of escalated accounts" is different from "medium cost of error."

> **6. What are we saying YES to — and what are we saying NO to?**
> "By investing 3 engineers for 2 months in an autonomous ticket router, we are choosing NOT to build the self-service portal that 40% of users requested." If you can't fill in the NO, you haven't made a real decision.

**Why this comes first:** A perfectly scored autonomy matrix for a workflow nobody cares about is waste with extra steps.

---

# PHASE 2: DIAGNOSE

## Step 1: Define and Decompose the Use Case

Define the work in operational terms before assessing autonomy.

**Restate the job:**

| Element | What to capture |
|---------|----------------|
| Job to be done | User's actual need — not "use AI for X" |
| Triggering event | What makes this task occur now? |
| Inputs / Outputs | Data in → Decision or action out |
| Users and actors | Who decides, who acts, who's accountable? |
| Systems touched | Tools, data sources, integrations |
| Permissions needed | Read? Write? Delete? Spend? |
| Success metric | How you know it worked |
| Consequence magnitude if wrong | What breaks; who's affected |

**Then decompose into sub-tasks:**

| Sub-task | Explicit vs Tacit | Action Mode | Cost of Error | Verifiability | Best-fit Level |
|----------|---|---|---|---|---|
| [Task 1] | E / T / hybrid | advisory / executional | low / medium / high | easy / hard / impossible | 0-7 |

**Critical rule:** If one sub-task is much riskier than others, do not let the average hide it. Recommend a hybrid design (level 3 for stable parts, level 1 for risky parts). Many good architectures are hybrids.

---

## Step 2: Run the 12 Diagnostic Questions

Answer these before scoring. If you cannot answer all, continue with stated assumptions — but mark them. An honest "I don't know" is more useful than a confident guess.

**Q1: What exact decision or action is being delegated?**
- Sharpen it: "The system [recommends / proposes / decides / executes] [specific output]. The human [reviews / approves / overrides / learns]."
- Red flag: "The system makes the decision" but the human reviews every output. That's advisement with friction, not decision-making.

**Q2: Does the system need to advise, decide, execute, or execute-with-approval?**
- These are strictly ordered. Advising costs nothing if wrong. Execution costs a lot if wrong.
- Red flag: Governance says "human approval required" but the system defaults to yes if no one reviews in 2 hours. That's execution, not approval.

**Q3: What happens if the output is wrong, late, or fails silently?**
- Wrongness, lateness, and silence are separate failure modes. Each has different impact.
- Red flag: "Low cost because we can fix it later." Later is when? If "later" is weeks, it's not low cost.
- Sharpen it: "Worst case is [impact]. Probability is [estimate]. Consequence magnitude is [who/what affected]."

**Q4: Can correctness be checked before action, immediately after, only later, or not at all?**
- Verifiability is your control lever. If you can't verify, you can't control.
- Red flag: "We'll monitor dashboards." Monitoring is not verification if the damage is already done.

**Q5: Which parts are explicit rules versus tacit judgment?**
- Explicit = codifiable now. Tacit = expertise that's hard to capture.
- Red flag: "It's mostly rules" but examples keep requiring human override. That's tacit masquerading as explicit.

**Q6: How often do novel cases or exceptions appear?**
- Frequency of exceptions = frequency of cases needing human judgment.
- Red flag: "Exceptions are rare now." They grow with scale. At 10x volume, how many per month?

**Q7: Does the environment stay stable during execution, or can state change mid-flight?**
- Red flag: "Stable in the happy path." Errors happen when state assumptions break in the unhappy path.

**Q8: Can a bad action be rolled back quickly and cheaply?**
- Rollback is your second-order control. Without it, autonomy is reckless.
- Red flag: "Rollback is not possible." Then autonomy must be zero on that action.

**Q9: What permissions, tools, or decision rights are required?**
- Execution rights are political AND technical. Both matter.
- Red flag: "Technically possible but policy says no." The ceiling is what policy allows PLUS what's safe to delegate.

**Q10: What is the smallest bounded slice that still creates value?**
- Start small, build trust, expand later. The smallest slice is your pilot.
- Red flag: "We need to scale to all use cases immediately." You're piloting, not launching.

**Q11: What telemetry or feedback loops exist to measure outcomes?**
- If you can't measure it, you can't improve it. And you can't defend it.
- Red flag: "We'll measure quality after launch." Measure before, during, and after.

**Q12: Does the economic upside justify the control burden?**
- Higher autonomy = higher engineering + operational cost. Is the ROI there?
- Red flag: "Upside is undefined. We're building because we can."

**Need the detailed answer nudges for any question?** Each question has expanded guidance with Low/Mid/High examples and sharpening prompts. Ask for the deep version of any Q1-Q12 and it will be provided.

---

## Step 3: Surface Your Assumptions

You've answered 12 questions. Some answers were data-grounded. Others were guesses dressed as analysis. Name the difference.

| Assumption | Evidence Level | Load-Bearing? | What Breaks If Wrong |
|-----------|---------------|---------------|---------------------|
| [e.g., "Exception rate is <5%"] | See legend below | Yes / No | [e.g., "Ceiling drops from level 5 to level 3"] |
| [e.g., "Rollback possible in 5 min"] | | | |
| [e.g., "Users will review output daily"] | | | |

**Evidence Level Legend:**

| Level | Meaning | Example |
|-------|---------|---------|
| **Validated** | Data exists. Measured. Dashboards or studies available. | "We tracked exception rate for 6 months: 3.2%." |
| **Informed** | Expert judgment or directional data. Reasonable but unproven. | "Senior ops lead estimates <5% based on experience." |
| **Assumed** | No evidence. Seems reasonable. Most common failure point. | "We think rollback is fast, but haven't tested it." |
| **Unknown** | We're guessing. Honest — and more useful than being wrong. | "No idea how users will react to agent-generated output." |

**The critical assumption test:** If this assumption is wrong, does the autonomy recommendation change? If yes, it's critical — test it before committing resources.

**Name the assumption that scares you most.** This is the one to validate first — not because it's most likely wrong, but because the damage is highest if it is.

---

# PHASE 3: ASSESS

## The Autonomy Spectrum (Levels 0-7)

This is the core vocabulary. Every recommendation in this skill maps to one of these levels. Use the **lowest level** that captures the value.

**Quick read:** Think of it as a staircase. Each step up means the system does more on its own — and each step up costs more to build, control, and trust.

| Level | Plain-Language Name | One-Liner | The System... | The Human... | Example |
|-------|---|---|---|---|---|
| **0** | **No AI** | Rules and software handle it | Follows if/then logic. Deterministic. | Writes the rules once, monitors | Expense routing by policy tier |
| **1** | **Rules Engine** | Smarter rules, still no learning | Applies decision trees and business logic | Maintains and updates rules | "If amount > $10K, require manager sign-off" |
| **2** | **AI for One Task** | AI does one specific thing well | Classifies, extracts, ranks, or generates from a single prompt | Integrates output into their workflow | Sentiment scoring; document extraction |
| **3** | **Copilot** | AI drafts, human decides | Produces full drafts (emails, reports, code). Value = speed, not autonomy | Reviews, edits, approves before anything goes out | Email drafting; code suggestions; report generation |
| **4** | **Supervised Agent** | Agent acts, human reviews | Takes multiple sequential actions. Escalates ambiguity. | Reviews outcomes (async or batch) | Agent books travel + schedules meetings; human checks daily digest |
| **5** | **Bounded Agent** | Agent acts within guardrails | Has scoped permissions (read, write, delete in defined scope). Cannot override policy. | Audits exceptions; handles escalations | Support agent creates tickets, updates records, escalates edge cases |
| **6** | **Semi-Autonomous** | Agent runs a narrow domain | Acts independently in a narrow, reversible domain. Humans audit post-hoc. | Spot-checks; intervenes on anomalies | Manages staging DB; auto-routes internal tickets |
| **7** | **Fully Autonomous** | Agent runs across domains | Decides and acts with minimal oversight. Requires exceptional controls. | Monitors dashboards; handles incidents | Rare. Only after 0-6 are battle-tested. |

**Default rule:** Start at levels 0-3. Move to 4+ only if the case genuinely requires dynamic planning, multi-step tool use, or open-ended exception handling.

**Why levels matter:** Every time you see "Level [X]" in this skill's output, refer back to this table. "We recommend Level 3" means "the AI drafts; a human decides." "We recommend Level 5" means "the agent acts within guardrails; a human audits exceptions." The difference between those two sentences is months of engineering and a completely different trust model.

> **VISUAL: Invoke `excalidraw-svg` to generate an Autonomy Staircase diagram** showing levels 0-7 as ascending steps. Each step labeled with the plain-language name, a one-line description, and a color gradient from green (low risk) to amber (medium) to red (high governance burden). This visual should accompany every readiness assessment output.

---

## The Two Matrices

Always use both. Together they tell you WHERE on the autonomy spectrum you belong.

### Matrix A: Knowledge Type × Cost of Error

This matrix answers: **"How much can we safely automate?"**

|  | Low Cost of Error | High Cost of Error |
|---|---|---|
| **Explicit knowledge** (codifiable rules) | **Automation zone.** Level 0-1. Rules engine is sufficient. | **Controlled automation.** Level 1-2. Rules + verification before action. |
| **Tacit knowledge** (expert judgment) | **Assistive / sandboxed.** Level 2-3. AI recommends; human reviews. | **Human judgment zone.** Level 3 max. AI assists; human decides. Do NOT automate. |

**Key insight:** High tacitness does NOT imply high autonomy. It often implies stronger human review. Harder problems need MORE human judgment, not less.

> **VISUAL: Invoke `excalidraw-svg` to generate a 2×2 matrix** with Knowledge (Explicit → Tacit) on X-axis and Cost of Error (Low → High) on Y-axis. Each quadrant labeled with zone name, recommended level range, and a color: green (Automation), blue (Controlled), amber (Assistive), red (Human Judgment). Plot the assessed use case as a dot with label.

### Matrix B: Need for Agency × Control Burden

This matrix answers: **"How much autonomy can we responsibly give?"**

|  | Low Control Burden | High Control Burden |
|---|---|---|
| **Low agency need** (predictable steps) | **Deterministic automation.** Level 1-2. Just do it. | **Deterministic + checkpoints.** Level 1 + verification. "High burden" ≠ "need an agent." |
| **High agency need** (dynamic planning) | **Bounded / semi-autonomous.** Level 5-6. Narrow + reversible + low consequence. | **Copilot / supervised.** Level 3-4. Humans remain in the loop. |

> **VISUAL: Invoke `excalidraw-svg` to generate a 2×2 matrix** with Need for Agency (Low → High) on X-axis and Control Burden (Low → High) on Y-axis. Each quadrant labeled with pattern name and level range. Plot the assessed use case. Use the same color system as Matrix A for consistency.

---

## Score the Operating Conditions

Score 1-5 on each dimension. Numbers structure judgment — they don't imply false precision. "This is 3-4 on tacitness" is useful. "This is 3.72, therefore autonomy level 4.91" is theater.

| Dimension | 1 (Low) | 3 (Medium) | 5 (High) |
|-----------|---------|-----------|----------|
| **Knowledge tacitness** | Fully codifiable rules exist | Mix of rules + judgment calls | Requires judgment even experts disagree on |
| **Cost of error** | <$100 or minor rework | $1K-$100K or moderate disruption | >$1M or irreversible harm |
| **Verification difficulty** | Deterministic output; easy to check | Can verify but requires effort or delay | Requires human judgment; no ground truth |
| **Irreversibility** | Undo in seconds; no downstream effects | Undo in hours; some downstream impact | Permanent; data loss or published content |
| **Process variability** | 90%+ same steps, rare exceptions | 70-90% consistent; regular edge cases | 50%+ novel cases; each needs judgment |
| **Coordination complexity** | Single system; independent | 2-3 systems; manageable dependencies | Multi-system; state dependencies; async |
| **Environment dynamism** | Stable; assumptions hold for hours | Semi-stable; 5-10% drift acceptable | Volatile; assumptions break within minutes |
| **Consequence magnitude** | Single user, single session | Team or department affected | Entire customer base; regulatory exposure |
| **Decision-rights sensitivity** | No approval needed | Single approval required | Multiple sign-offs; regulatory approval |

**Optional modifiers** (include only when they directly affect the recommendation): Compliance sensitivity, Data quality gaps, Latency sensitivity, Economic leverage.

---

## Four Meta-Judgments

State all four. Do not collapse into one number.

### Need for Agency
How much dynamic planning, judgment, exception handling, or tool orchestration the work truly needs.

| Band | Meaning | Driven By |
|------|---------|-----------|
| **Low** | Task follows predictable steps. Rules handle 90%+. | Low tacitness, low variability, simple coordination |
| **Medium** | Regular exceptions. Some multi-step orchestration needed. | Moderate tacitness or variability |
| **High** | Frequent novel cases. Dynamic planning required. Multi-system coordination. | High tacitness + variability + coordination + dynamism |

### Control Burden
How hard it is to let the system act safely.

| Band | Meaning | Driven By |
|------|---------|-----------|
| **Low** | Errors are cheap, visible, reversible. Minimal governance. | Low cost, easy verification, reversible, narrow consequence |
| **Medium** | Errors are moderately costly. Some review required. | Moderate cost, delayed verification, some irreversibility |
| **High** | Errors are expensive, hard to detect, hard to reverse. Heavy governance. | High cost + hard verification + irreversible + wide consequence + regulated |

### Implementation Effort
Design, integration, eval, monitoring, and change management to deploy responsibly.

| Band | Meaning | Typical Timeline |
|------|---------|-----------------|
| **Low** | Light integration, basic eval, simple review flow | Weeks |
| **Medium** | Tool design, fallback logic, audit logging, human review design | Months |
| **High** | Governance alignment, monitoring infrastructure, incident response, regulatory | Quarters |

### Economic Leverage
Whether the upside justifies heavier engineering and control investment.

| Band | Meaning | Signal |
|------|---------|--------|
| **Low** | <$50K/year savings. Not strategic. | Low frequency × low value per case |
| **Medium** | $50K-$500K/year. Meaningful but not transformative. | Moderate frequency or moderate per-case value |
| **High** | >$500K/year OR strategic necessity. Justifies heavy investment. | High frequency × high value, or core to roadmap |

---

# PHASE 4: DECIDE

## Set the Autonomy Floor and Ceiling

**Autonomy floor** = minimum sophistication needed for the task to work.
**Autonomy ceiling** = maximum safe autonomy given current controls.

The gap between them is often the most important insight.

**If the floor is above the ceiling**, you have four options:
1. Narrow the task scope (lowers the floor)
2. Strengthen controls (raises the ceiling)
3. Delay deployment until controls exist
4. Accept human-in-the-loop as Phase 1 (level 4 now; level 6 later)

> **VISUAL: Invoke `excalidraw-svg` to generate an Autonomy Gap diagram.** Show a vertical bar from Level 0 to Level 7. Mark the floor with a green line and label ("Minimum needed: Level X"). Mark the ceiling with a red line and label ("Maximum safe: Level Y"). The gap between them is the decision space (highlight in amber). If floor > ceiling, highlight the overlap in red with a "GAP: Must resolve" callout.

---

## Analyze the Trade-Offs

### View 1: Effort vs Autonomy

| Autonomy Range | Typical Effort | Why |
|---------------|---------------|-----|
| **Level 2-3** (advisory) | 2-4 weeks | Humans absorb risk. Prompt tuning + basic eval + review workflow. |
| **Level 4-5** (bounded execution) | 2-3 months | System absorbs risk. Tool design + evals + fallback logic + audit logging. |
| **Level 6-7** (high autonomy) | 6-18 months | Scaling trust. Governance + monitoring + incident response + regulatory. Non-linear because all must mature together. |

### View 2: Effort vs Binding Constraint

Default to **verification difficulty** as the second axis. Switch to tacitness, dynamism, consequence magnitude, or latency only if that's the real bottleneck.

| Binding Constraint | Why Effort Rises |
|-------------------|-----------------|
| **Verification difficulty** | Eval design, fallback logic, human review all get harder. You can't ship what you can't verify. |
| **Knowledge tacitness** | Expertise capture, rubrics, escalation paths. High tacitness demands humans in loop. |
| **Environment dynamism** | State handling, replanning, recovery logic. System must expect assumptions to break. |
| **Consequence magnitude** | Approvals, canaries, audit trails, incident response. Managing organizational risk. |
| **Latency sensitivity** | Human review doesn't fit the operating window. Cut latency or cut autonomy. |

### View 3: The Hidden Trade-Off

After the standard analysis, name the trade-off most people miss:

```
BY CHOOSING AUTONOMY LEVEL [X]:
  We are betting on: [the core bet]
  We are giving up: [the opportunity cost — be specific]
  This is reversible within: [timeframe] / This is a one-way door because: [reason]

THE HIDDEN TRADE-OFF:
  [The non-obvious second-order consequence — e.g., "Requiring human review
   caps throughput at 200 cases/day. If volume grows past that, we'll need
   to hire reviewers or raise autonomy under pressure, not thoughtfully."]

CONFIDENCE: [High / Medium / Low]
```

**Confidence Legend:**

| Level | Meaning | Next Step |
|-------|---------|-----------|
| **High** | Strong evidence across key assumptions | Ask: What would make us wrong? |
| **Medium** | Mix of validated and assumed inputs | Ask: What evidence would move us to High? |
| **Low** | Mostly assumed or unknown inputs | Ask: Should we decide now, or gather evidence first? |

**LNO check (Shreyas Doshi):** Is this autonomy decision Leverage (get it right — shapes the product's trust model), Neutral (reasonable choice is fine), or Overhead (pick one, move on)? Most autonomy decisions for core workflows are Leverage.

---

## Watch for Agentic False Positives

These signal that a lower-autonomy design is probably better:

| Warning Sign | What It Really Means |
|-------------|---------------------|
| "Agent" but the value is extraction, routing, or templated generation | Value is in the LLM capability, not agency. Level 2 is enough. |
| The hard part is bad data or poor integration, not reasoning | Fix the upstream first. Agency isn't the constraint. |
| Low-frequency workflow; too small to justify control burden | Human labor is cheaper at low volume. |
| "Passes internal eval" but can't be verified in production | You can't scale trust without measurable feedback loops. |
| Execution rights blocked by policy | Bottleneck is governance, not capability. Solve governance first. |
| Workflow involves negotiation, relationships, or accountability | Humans must own these. Agency destroys accountability. |

---

## State Your Hypothesis

Frame the recommendation as a testable hypothesis. This is what separates a readiness assessment from a rubber stamp.

```
HYPOTHESIS: We believe autonomy level [X] is right-sized for [use case]
  because [reasoning grounded in diagnostic answers and scores].

IF TRUE:
  Leading indicator: [e.g., "acceptance rate >40% within 2 weeks"]
  Lagging indicator: [e.g., "50% reduction in processing time within 2 months"]
  Control condition: [e.g., "zero critical errors requiring rollback"]

IF FALSE:
  Counter-signal: [e.g., "escalation rate >20%" or "users bypass system within 3 weeks"]
  Damage: [specific cost, time, trust loss]
  Reversibility: [timeframe to change course]

DAMAGE IF WRONG:
  Too HIGH: [e.g., "Agent executes bad actions; customer data affected; trust recovery: 6 months"]
  Too LOW: [e.g., "Advisory system nobody uses; value requires execution, not recommendation"]

PIVOT TRIGGER:
  Raise to level [Y] if: [positive signals + mature controls]
  Lower to level [Z] if: [negative signals or control gaps]

LOAD-BEARING ASSUMPTIONS:
  1. [Most fragile] — Evidence: [level] — Test by: [method, timeframe]
  2. [Second] — Evidence: [level]
  3. [Third] — Evidence: [level]

THE ASSUMPTION THAT SCARES ME MOST:
  [Name it. Test this first.]
```

---

# PHASE 5: PLAN

## Recommend the Operating Model

State ALL of these clearly:

| Element | Your Answer |
|---------|------------|
| **Solution class now** | Level [0-7] |
| **Autonomy level now** | Level [0-7] |
| **Autonomy ceiling (future)** | Level [0-7] after controls mature |
| **Readiness band** | Ready now / Ready with controls / Assist-only now / Not a fit |
| **Why not one level lower** | [What breaks] |
| **Why not one level higher** | [What goes wrong] |
| **Human checkpoints** | [Which decisions escalate to whom] |
| **Telemetry requirements** | [What to measure to know if it's working] |

**Readiness Band Legend:**

| Band | Meaning |
|------|---------|
| **Ready now** | Controls exist. Economics justify. Ship it. |
| **Ready with controls** | Viable, but specific controls must be built first. Name them. |
| **Assist-only now** | AI can advise; cannot act. Human remains decision-maker. |
| **Not a fit** | Rules or standard software is better. AI adds cost without proportional value. |

**Recommend level 5+ ONLY when ALL five are true:**
1. Task genuinely needs dynamic planning or multi-step orchestration
2. Action rights can be scoped safely
3. Outcomes are sufficiently verifiable or reversible
4. Consequence magnitude is bounded enough for learning (error costs <$100K or affects <100 users)
5. Economics justify the control burden (>$500K/year or strategic necessity)

If any one is questionable, recommend level 3-4. Save level 5+ for when confidence is high across all five.

---

## See the Decision in Context

Step back and view the recommendation through five lenses. This takes 2 minutes and prevents the most common failure: a technically correct recommendation that ignores the world around it.

| Lens | The Question |
|------|-------------|
| **Customer** | Does this autonomy level fit their workflow? Will they trust it? Have we asked? |
| **Business** | Does the economic leverage justify the control investment? What's the unit economics at scale? |
| **Market** | Are competitors at a different autonomy level? Are we bearing pioneer risk or losing differentiation? |
| **Team** | Can we build AND operate this? Eval design, monitoring, incident response, governance — who owns each? |
| **Ethics** | Who gets harmed if errors occur at scale? A 0.1% error rate × 10K cases/month = 10 errors/month. Acceptable? |

> **VISUAL (optional): Invoke `excalidraw-svg` for a Five-Lens Radar** — pentagon chart with each lens as an axis scored Green/Amber/Red. Shows at a glance which lenses support the recommendation and which raise concerns.

---

## Phased Roadmap

Smallest valuable wedge first. Do not boil the ocean.

| Phase | Pattern | Value Hypothesis | Controls Needed | Exit Criteria |
|-------|---------|---|---|---|
| **Phase 1** | Level 2-3: assistive | "System recommends. Humans choose." ~20% time savings. | Basic eval, user feedback. | Acceptance rate >30%. Zero critical failures. |
| **Phase 2** | Level 4: bounded execution | "System acts in scope. Escalates exceptions." ~50% savings. | Tool design, fallback logic, audit logs. | <2% escalation rate. <0.5% critical errors. |
| **Phase 3** | Level 5-6: higher autonomy | "System autonomous in proven domain." ~70% savings. | Governance, monitoring, incident response. | Zero critical errors over 4 weeks. Policy approval. |

**Each phase is a hypothesis:** "We believe level [X] will deliver [Y] because [Z]. We'd know we're wrong if [signal] within [timeframe]."

**Enablers between phases:**
- Phase 1 → 2: Robust tool integrations, fallback logic, escalation design
- Phase 2 → 3: Policy alignment, incident response maturity, autonomous verification
- Phase 3 → beyond: Regulatory sign-off, organizational governance maturity

> **VISUAL: Invoke `excalidraw-svg` to generate a Phased Roadmap flow diagram.** Three horizontal swim lanes (Phase 1 → 2 → 3), each showing: the autonomy level, the value hypothesis, the key controls needed, and the exit criteria as a gate between phases. Arrows between phases labeled with enablers. Color-code: green for "ready now," amber for "ready with controls," red for "not yet."

---

## Controls and Operating Model

| Control | Specify |
|---------|---------|
| **Approvals** | Who approves what? Sync or async? |
| **Policy constraints** | What does governance require? |
| **Evaluation plan** | How to measure success and failure? |
| **Monitoring** | What dashboards or alerts? |
| **Rollback / Recovery** | How to undo a bad action? Who authorizes? |
| **Auditability** | What audit trail is needed? |
| **Kill switches** | When to stop the system? Who can pull it? |

---

# HARD RULES

These are not suggestions.

1. **Recommend the lowest-autonomy design that captures the value.**
2. **Decompose before scoring.** Good architectures are often hybrids.
3. **"Needs reasoning" ≠ "can safely act."** Intelligence and autonomy are separate questions.
4. **Current readiness ≠ future potential.** Say when it becomes ready, not just that it isn't.
5. **Don't reward novelty.** If rules or workflow design solve it better, say so.
6. **High error cost + low verifiability = human-led.** Not autonomy.
7. **High tacitness ≠ high autonomy.** Often the opposite.
8. **Action rights matter as much as reasoning quality.** Solve both.
9. **Name what must change for the recommendation to change.** Be specific — not "if policy changes" but "if we build X and measure Y past Z threshold."
10. **When evidence is thin, say so.** Name the critical assumptions — the ones where being wrong changes the recommendation. Ask what to test first.

---

# REALITY CHECK

These truths will save you from the most common mistakes:

- **Autonomy is a governance question, not a technology question.** You CAN build level 5. Policy determines whether you SHOULD operate at level 5.
- **Cost of error compounds.** 0.1% error rate × 10K tasks/month = 10 errors/month. Is that acceptable?
- **Verification IS the product.** If you can't verify output, you can't scale the system.
- **Phased rollouts are engineering, not marketing.** Start small because you need to learn what you can control.
- **"Agent" ≠ "autonomous."** An agent can be supervised (level 4) or advisory (level 2).
- **Hybrid designs are underrated.** Level 1 for 70% + level 3 for 25% + level 0 for 5% often beats pure level 4.
- **ROI must be real.** Saving 1 hour/month but spending 2 months building controls doesn't work.
- **Consequence magnitude grows with integration.** More systems = more consequence. Start with read-only.

---

# QUALITY GATE

Before delivering the assessment, verify:

- [ ] Customer reality established — who, what problem, how painful, what we're saying NO to
- [ ] Use case decomposed into sub-tasks, not treated as one blob
- [ ] All 12 diagnostic questions answered (or gaps named with evidence level)
- [ ] Load-bearing assumptions surfaced, rated, and flagged
- [ ] Both matrices completed (Knowledge × Cost; Agency × Control)
- [ ] All four meta-judgments stated with band definitions
- [ ] Autonomy floor and ceiling identified; gap explained
- [ ] Trade-off analysis includes effort/autonomy + effort/binding constraint + hidden trade-off
- [ ] Recommendation stated as hypothesis: IF TRUE / IF FALSE / PIVOT TRIGGER
- [ ] Why not one level lower + why not one level higher
- [ ] Five-lens check completed
- [ ] Phased path with exit criteria, each framed as hypothesis
- [ ] Assumptions to watch with test methods and timeframes

---

# WHEN THIS SKILL GIVES BAD ADVICE

This analysis would be wrong if:

1. **The use case hasn't been decomposed.** Use first-principles first. Applying this to a monolithic use case produces a monolithic (and wrong) recommendation.

2. **You need a technology recommendation, not an autonomy recommendation.** Use system-design for architecture. This skill is governance and readiness, not tech stack.

3. **The decision is organizational or political.** When the VP has already decided "full autonomy," no diagnostic score changes that. You need a different conversation.

4. **Evidence is too thin.** When most assumptions are "Unknown" and the critical ones are "Assumed," the framework produces false precision. Name the 3 assumptions that matter most, design experiments to test them, and defer the autonomy decision until you have data.

5. **You're using this as a recipe, not a diagnostic.** The questions surface uncertainty. If they don't help you decide, you need more information — not more framework.

6. **Customer reality has shifted.** Pain level, volume, exception rate, and regulations evolve. Reassess when the ground shifts.

---

# NATURAL FLOW

**Coming FROM** problem-ai-fit → You've established AI is the right approach. Now determine the right *level*. Carry customer grounding and assumptions forward.

**Going TO** invisible-stack → Once autonomy level is set, design the technical architecture. Autonomy constrains architecture, not the reverse.

**Going TO** determinism-compass → For deterministic portions of hybrid designs, or when governance questions dominate.

**Going TO** cost-model → When economic leverage needs deeper analysis, especially for level 4+ where control costs are significant.

**Parallel with** autonomy-spectrum → Quick autonomy-level reference without the full diagnostic. Use that for fast checks; use this for thorough assessments.

---

## DELIVERABLE FORMAT

The output of this skill should be a **polished, formatted document** — not raw markdown dumped into a chat window. Think: something a McKinsey consultant would present to a C-suite audience.

### Visual Outputs (Excalidraw SVGs)

Generate these visuals inline as part of the assessment. Each is invoked via the **excalidraw-svg** skill. Together they tell the story at a glance — a senior stakeholder should be able to understand the recommendation from the visuals alone, without reading a single paragraph.

| Visual | When to Generate | What It Shows |
|--------|-----------------|--------------|
| **Autonomy Staircase** | Always | Levels 0-7 as ascending steps with the recommended level highlighted |
| **Matrix A: Knowledge × Cost** | Always | 2×2 matrix with the use case plotted as a dot |
| **Matrix B: Agency × Control** | Always | 2×2 matrix with the use case plotted as a dot |
| **Autonomy Floor/Ceiling Gap** | When floor and ceiling differ by 2+ levels | Vertical bar showing the decision space |
| **Phased Roadmap Flow** | When recommending phased rollout | Three-phase swim lane with gates between phases |
| **Trade-Off Balance** | When the hidden trade-off is non-obvious | Two sides of a scale showing what we gain vs. give up |
| **Assumption Risk Map** | When 3+ critical assumptions are unverified | Bubble chart: X = impact if wrong, Y = evidence strength, size = how many people/systems affected |

**Rule:** If in doubt, generate the visual. A 2×2 matrix described in text is forgettable. The same matrix as a clean SVG with the use case plotted on it is instantly understood and shareable.

### Document Output

When the user requests a full deliverable (or the assessment is comprehensive), produce the assessment as a **formatted document** (`.docx` or `.pdf`) with:

1. **Executive Summary** (1 page): Recommendation, hypothesis, key trade-off, biggest risk, next action
2. **Visual Story** (1-2 pages): The SVG visuals above, captioned, telling the story without text
3. **Detailed Assessment** (3-5 pages): Full analysis following the output structure in Phase 5
4. **Assumptions & Risks** (1 page): The assumption table with test plans
5. **Phased Roadmap** (1 page): The roadmap table with exit criteria

The document should be professional enough that a PM can forward it to their VP without editing, and clear enough that an engineer can act on the phased roadmap without further translation.

### Inline Output

When the user wants a quick answer in conversation (not a document), provide:
1. The recommendation table (from Phase 5)
2. The hypothesis (from Phase 4)
3. One or two key visuals (Matrix A + Autonomy Staircase at minimum)
4. The assumptions to watch

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md` for all SVG generation.

---

## GENERATE THE DELIVERABLE

Once the analysis is complete, use this prompt to produce the final output:

```
OUTPUT GENERATION PROMPT:

You have completed the AI Use Case Readiness Assessment. Now produce the deliverable.

FORMAT: [Word Document / Presentation / Both — as chosen by user]

INSTRUCTIONS:
1. Read the full analysis above.
2. Write the Executive Summary first — the recommendation must be the first sentence.
3. Generate Excalidraw SVG visuals for:
   - Autonomy Staircase (always)
   - Matrix A: Knowledge × Cost (always)
   - Matrix B: Agency × Control (always)
   - Autonomy Floor/Ceiling Gap (if floor and ceiling differ by 2+ levels)
   - Phased Roadmap Flow (if recommending phased rollout)
   - Five-Lens Radar (if comprehensive analysis)
   - Assumption Risk Map (if 3+ critical assumptions are unverified)
4. Structure the document/deck following the Universal Deliverable Protocol.
5. Use plain language throughout — no unexplained jargon.
6. Before delivering:
   - Grammar check all text.
   - Verify the recommendation is consistent across all sections and visuals.
   - Confirm all tables and scores are filled (no placeholders).
   - Check visuals match the text.
7. Deliver the file to the user's workspace folder.

QUALITY BAR: A PM should be able to forward this to their VP without edits.
An engineer should find actionable specifics in the phased plan.
A designer should see clean, professional formatting.
```

---

## WORKFLOW HANDOFF

When this skill feeds into a downstream skill (invisible-stack, determinism-compass, cost-model), **automatically generate a markdown handoff file** that carries forward:
- The customer grounding (so the next skill doesn't re-ask)
- The recommended autonomy level and its hypothesis
- Critical assumptions with evidence ratings
- Open questions for the next skill

Follow the Markdown Handoff format in the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 9.

File naming: `ai-use-case-readiness-handoff-[use-case-slug].md`
