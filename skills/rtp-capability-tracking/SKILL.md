---
name: rtp-capability-tracking
description: Decide whether to build an AI feature now or wait for model capability uplift to deliver it for free. Frames build-vs-wait decisions when frontier models are improving every 6-9 months and custom engineering risks being commoditized. Use when scoping 12-18 month roadmaps, evaluating which features will commoditize on next model release, deciding between custom fine-tuning and waiting for foundation-model improvements, or building a capability watchlist for portfolio bets. Triggers on "should we build this", "wait for the next model", "18-month roadmap", "commoditization risk", "capability planning", "build vs. wait", "model capability tracking".
---
# Capability Tracking: Know What the Model Will Do Next

## DEPTH DECISION

You are evaluating whether a feature should be built by your team or acquired through model capability improvements. The question: Is this something we invest in custom engineering for, or do we wait for Claude/GPT-5/Gemini to do it for free in 9 months?

The trap: Treating model capabilities as fixed. They are not. A feature that needs 3 engineers today might be a prompt rewrite next quarter. But the opposite is also true: betting your product on an unreleased capability is how you get stranded.

**Who uses this:** Product managers deciding between build/buy/wait. Founders planning 18-month roadmaps. Tech leads scoping feature work.

## DELIVERABLE FORMAT

Before starting, ask:
> **What format would you like this in?**
> 1. **Word Document** (.docx) — Formatted report with embedded visuals. Best for sharing.
> 2. **Presentation** (.pptx) — Slide deck with key findings. Best for meetings.
> 3. **Both** — Full report + summary deck.
>
> *Default: Word Document.*

If the user specifies format in their request, skip the question.

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

**Trap 1: Assuming capabilities stay flat.** You evaluate the current model, build a feature, ship it. Six months later, the model does it natively. You spent 8 weeks on what is now a prompt.

**Trap 2: Betting on futures that never materialize.** "We'll wait for multimodal." Three years later, you're still waiting and competitors shipped.

**Trap 3: Mistaking capability for product feature.** GPT-4 can do reasoning. That doesn't mean users want a 20-second latency reasoning feature. Capability ≠ Product.

**Trap 4: Building moats that evaporate.** Your 2023 differentiation was a fine-tuned model. By 2024, prompt engineering + RAG obsoleted it. You need capabilities models won't commoditize fast.

## THE PROCESS

### 1. Capability Radar
For each critical capability your product depends on:
- Current state: Does the latest model do this? What's the quality/latency?
- Trajectory: Is this improving? By how much per release cycle?
- Deprecation risk: When does this go from "custom engineering" to "included"?

Create a 3x3 grid:
- X-axis: Time to commoditization (0–3 months, 3–12 months, 12+ months)
- Y-axis: How much your product depends on this (core, differentiating, nice-to-have)

**Quick diagnostic:** Plot your top 5 features. Anything in the "core capability + commoditizing in 3 months" cell is a threat.

### 2. Strategy Half-Life
For each piece of tech/capability your product relies on, ask:
- When was this capability created/integrated?
- How much value has degraded since then?
- What will commoditize it?

**Example:** Your ranking algorithm was state-of-the-art 18 months ago. Models now rank nearly as well with a prompt. Your half-life on this advantage is ~9 months. Decision: Do you hold it or migrate to a model-native approach?

### 3. Build vs. Wait Decision Tree

START: Do you have a critical need for this capability right now?
- NO → Ask: Is it core to your differentiation in 2027?
  - NO → Don't build. Wait.
  - YES → Go to BUILD.
- YES → Ask: Will a future model provide 80% of the value?
  - NO → BUILD now.
  - YES → Ask: When will that model release?
    - 0–3 months → WAIT.
    - 3–6 months → BUILD minimum viable + plan migration.
    - 6+ months → BUILD, own it, plan obsolescence.

### 4. Deprecation Planning
Once you build something, assume it will be commoditized.

Set a "model capability check" quarterly. For each custom capability:
- Has the model improved against this? By how much?
- Would a migration to model-native be faster than maintaining custom code?
- What's the sunk cost of switching?

Document the switchover path before you forget it.

### 5. Harness Capability Tracking

Every component in a multi-agent harness encodes an assumption about what the model can't do on its own. Track which harness components become obsolete with each model upgrade.

**Maintain a "harness assumption register"** — a list of every workaround, scaffold, and orchestration piece with the model limitation it addresses:

Example harness assumptions:
- Planner agent exists because: "Claude can't decompose 50-step tasks without losing coherence"
- Memory shard system exists because: "Claude can't access full session history without context explosion"
- Fact-checker node exists because: "Claude hallucinates dates in long documents"
- Router agent exists because: "Claude can't dynamically decide between expert models"

When a new model ships, test each assumption:
- **If assumption still holds:** Keep the component, maybe optimize it
- **If assumption is violated:** Simplify the harness and redeploy savings elsewhere

**Example decision path:**
- Opus 4.5 needed scaffolded planning. Opus 4.6 can plan 50-step sequences natively
- Remove the planner node; test the agent on the same tasks
- Result: latency drops 30%, complexity cuts in half, you redeploy that engineering capacity to improve retrieval quality instead

This is not "simplification for simplicity's sake." It's: every harness component is debt that accrues interest. As models improve, pay down the debt.

### 6. Strategy Half-Life Quantification

Quantify how fast your AI strategy assumptions decay. This is not a fixed decay (straight-line depreciation). It's exponential, driven by:
- How many competitors are building the same thing
- How close the capability is to commoditization
- How defensible your data/moat is

**Strategy Half-Life Benchmarks:**

| Advantage Type | Half-Life | Example | Why It Decays |
|---|---|---|---|
| Prompt-level advantage | 3-6 months | "We have a 30-turn conversation template that beats baseline" | Competitors copy your prompts; models improve; techniques commoditize fast |
| RAG/retrieval advantage | 6-12 months | "We indexed the full Knowledge Graph; retrieval is 2x faster" | Embedding models improve every 3-4 months; retrieval becomes table-stakes |
| Fine-tuning advantage | 12-18 months | "We fine-tuned on domain data; domain accuracy is 95%" | New base models often exceed fine-tunes; your dataset becomes dated; competitors collect better data |
| Data flywheel advantage | 24-36 months | "We've collected 5 years of user interactions; our signal is unmatched" | Hardest to replicate; stickiest moat; but eventually competitors gather enough data |
| Harness/orchestration advantage | 12-24 months | "Our 4-agent workflow is faster than single-agent baselines" | Orchestration patterns become known; simpler models do it natively; architecture spreads |

**How to track half-life decay:**
1. **At creation:** Log the date, capability, and estimated half-life category
2. **At 50% half-life:** Test the assumption. Has the capability commoditized? Yes/No
3. **At 100% half-life:** If assumption is NOT violated, extend the half-life (you were conservative). If violated, start renewal/replacement planning

**Example tracking:**
- Prompt-level advantage created Jan 2025. Half-life = 3-6 months. Review date = April/May 2025.
- April 2025: "We tested Opus 4.6 on the same prompt template. It matches our performance now."
- Decision: Refresh the prompt to maintain advantage, or accept that advantage is decaying and plan migration to a deeper moat (fine-tuning, data).
- If you don't refresh, the advantage is dead by July 2025.

**Track your top 5 capabilities against these benchmarks:**
- Which are past half-life and stale?
- Which are 50% through half-life and need renewal plans?
- Which haven't decayed yet (why? is your estimate conservative)?

This prevents the trap of "we built something smart 3 years ago and we're still coasting on it."

## THE QUARTERLY CAPABILITY TEST

Model benchmarks tell you what changed. This tells you what it means for *your* product.

**The protocol (run every quarter, or whenever a major model update ships):**

1. **Pull your golden set.** Take the 100 queries your product handles most frequently. These should already be in your eval dataset. If they're not, sample 100 from production logs today.

2. **Run on old model + new model, same prompts.** No prompt changes — you're isolating the model variable.

3. **Measure three things:**
   - **Accuracy delta:** What % of queries improved? What % regressed? Net movement.
   - **Latency delta:** P50 and P95 latency. Did the new model get faster or slower at your task?
   - **Cost delta:** Input + output tokens per query. Did the new model use more or fewer tokens to reach the same answer?

4. **Categorize results:**
   - **Clear win:** Accuracy up, latency down or same, cost down or same. Switch immediately.
   - **Quality-cost tradeoff:** Better accuracy but higher cost. Run unit economics to see if it's worth it.
   - **Regressed cases:** Any accuracy decrease on previously-working queries. These are your blockers — fix before switching.
   - **Wash:** No meaningful delta. Wait for the next release.

5. **Decide in 48 hours.** Don't let model evaluation drag into a 2-week analysis. The test gives you a decision, not a research paper.

**What good looks like:** You're running this test before model updates ship to users, not after. Proactive testing beats reactive debugging.

## KEY DIAGNOSTIC QUESTIONS

**Q1: Capability Velocity**
What's the quarter-over-quarter improvement rate for your core model capability?
- If > 15% improvement per quarter: This is commoditizing. Stop investing.
- If 5–15% improvement: Build defensible product layers, not capability layers.
- If < 5% improvement: Safe to own this capability long-term.

*Think through:* How are you measuring improvement? Is it on your specific task, or general benchmarks?
*Low end:* <5% QoQ. Capability is stable or improving slowly. Safe to invest in custom engineering.
*Mid range:* 5–15% QoQ. Noticeable improvement every quarter. Your custom work has 12–18 months before commoditization pressure.
*High end:* >15% QoQ. Rapid acceleration. Commodity threat is immediate.
*Red flag:* You haven't actually measured this. You're guessing based on model release notes.
*Sharpen it:* Run the Quarterly Capability Test. Get numbers. Then you can answer Q1 with data.

**Q2: Dependency Strength**
If this capability disappeared tomorrow, how quickly could your product operate without it?
- < 1 week: You're custodian, not dependent. Okay to own.
- 1–4 weeks: You're exposed. Plan a migration path.
- > 1 month: This is critical infrastructure. Owns you. Build flexibility.

*Think through:* What's the manual workaround? How many customers does it affect?
*Low end:* <1 week recovery. You have a fallback path. Low risk.
*Mid range:* 1–4 weeks recovery. You can migrate but it requires coordination. Moderate risk.
*High end:* >1 month recovery. Loss of this capability creates customer outage. Critical risk.
*Red flag:* You haven't identified a fallback. Your entire product depends on one thing the model can do.
*Sharpen it:* Document the recovery plan. Run it as a fire drill quarterly.

**Q3: Copycatting Cost**
A competitor with access to the same model, how long would it take them to match your capability advantage?
- < 1 week: You built prompt engineering. Not defensible.
- 1–4 weeks: You built a system. Defensible but fragile.
- > 1 month: You built proprietary data, training, or novel architecture. Worth protecting.

*Think through:* What would they need to copy? Just your prompts, or your data/training/infrastructure too?
*Low end:* <1 week. Your advantage is prompt-level. Anyone with the same model can match you quickly.
*Mid range:* 1–4 weeks. You've built scaffolding or integration work that's non-obvious. Some defensibility.
*High end:* >1 month. You've invested in data collection, fine-tuning, or custom infrastructure. Harder to replicate.
*Red flag:* You haven't thought about this. Assume your competitor is copying you next week.
*Sharpen it:* What would it cost them in time and money? That's your moat strength.

**Q4: Moat Durability**
Is your advantage from the model, from what you built on top, or from data you collected?
- From model (GPT-4 solves it) → 6-month lifespan.
- From your system (your workflow is better) → 18-month lifespan.
- From data (you trained on real usage) → 3+ year lifespan.

*Think through:* If we switched to the newest, most capable model tomorrow, would we still have an advantage?
*Low end:* Model-driven advantage. Next model release erodes it. 6-month lifespan.
*Mid range:* System-driven advantage. You've built better integration, orchestration, or UX. 18-month lifespan.
*High end:* Data-driven advantage. You've collected proprietary signals. 3+ year lifespan.
*Red flag:* Your advantage is all from the model. You're riding on Claude 3.5 Sonnet's shoulders. When 4.0 ships, what's left?
*Sharpen it:* Which of these three sources should you be investing in? Pick one and build it.

## REALITY CHECK

Check yourself:
- Have you actually tested the latest model on this capability? Or are you extrapolating from knowledge cutoff?
- Are you underweighting the "hidden work" of integrating a new model version? (Costs exist even if the capability is free.)
- Are you overweighting sunk cost? (Yes, you spent 3 months. That cost is gone. What matters is forward cost.)
- Have you asked your users whether they'd wait 3 months for a cheaper solution, or do they want it now?

## HALF-LIFE MODIFIERS: YOUR VERTICAL CHANGES EVERYTHING

The standard half-life benchmarks (prompt advantage: 3–6 months, RAG: 6–12 months, fine-tune: 12–18 months) assume a competitive, commoditizing space. Adjust based on where your vertical sits:

**Modifier table:**

| Your situation | Adjustment | Why |
|---|---|---|
| You're in a niche vertical (healthcare compliance, legal contract review, industrial maintenance) | Extend half-life 1.5–2× | Foundation models train on general data. Your domain stays differentiated longer. |
| You're in a commoditized space (email writing, code completion, customer support) | Shorten half-life 0.5× | Every frontier model release directly attacks your core capability. |
| Your advantage is data (you have proprietary labels, rare documents, specialized corpora) | Fine-tune half-life extends to 24–36 months | Data moats are the most durable. |
| Your advantage is workflow integration (deep CRM/ERP hooks, proprietary context) | Integration advantage: 18–24 months | Switching cost is the moat, not the model. |
| Your advantage is prompt engineering alone | Reduce to 1–3 months | Anyone can copy a prompt. |

**The honest question:** "Is what makes us good about *our capability* or about *the model's capability*?" If the answer is mostly the model, your half-life is whatever the model's release cycle is.

## BUILD OR WAIT: READING COMPETITIVE SIGNALS

Don't wait 6 months because a benchmark said capability half-life is 6 months. Watch the signals that tell you *specifically* when to move.

**Build now signals:**
- A direct competitor just launched a feature in this capability area. Waiting = falling behind.
- A foundation model just crossed your accuracy threshold in your evaluation suite.
- Your current provider announced deprecation or pricing changes.
- Customer feedback explicitly names the missing capability as a blocker to renewal.

**Wait signals:**
- The current leader model is actively degrading (common with rapidly-updated models). Wait for stability.
- You're in an active model race — two frontier labs are leapfrogging on your task every 4–6 weeks. Building now means rebuilding in 2 months.
- Your capability gap is <10% accuracy. The cost of engineering time to close it exceeds the user value.
- Your market doesn't yet reward the capability. No customer has asked for it unprompted.

**The competitive signal check (monthly, 15 minutes):**
1. Check benchmarks for your specific task type (not general leaderboards — find task-specific ones).
2. Check what your top 3 competitors announced in the last 30 days.
3. Check your own support tickets and lost-deal notes for any capability mentions.
4. Decide: build, wait, or monitor.

## OUTPUT FORMAT

Use this template to document and track capabilities, strategy decay, and harness assumptions:

```
## Capability Tracking Register: [Product Name]

**Product:** [Product, version, date]
**Maintained by:** [Team, review cadence]
**Last updated:** [Date]

---

### Capability Radar

| Capability | Current Quality vs SOTA | Trajectory (QoQ) | Commoditization Timeline | Renewal Plan | Owner |
|-----------|------------------------|-----------------|-------------------------|------------|-------|
| [Capability A] | [vs GPT-4.5, Opus 4.6, etc.] | [up, flat, down ±%] | [0-3mo, 3-12mo, 12+mo] | [maintain/refresh/replace] | [owner] |
| [Capability B] | [comparison] | [trend] | [timeline] | [action] | [owner] |

---

### Strategy Half-Life Tracker

| Advantage | Category | Created | Half-Life | Expires | Current Status | Renewal Plan |
|-----------|----------|---------|-----------|---------|---|---|
| Prompt template for complex reasoning | prompt-level | Jan 2025 | 3-6mo | Apr-Jul 2025 | Still ahead (Apr) | Upgrade Q2 if Opus 4.7 matches |
| RAG on domain-specific documents | RAG/retrieval | Jun 2024 | 6-12mo | Dec 2024-Jun 2025 | DECAYED (past 50% mark) | Migrate to embedding v4 + hybrid search |
| Fine-tuned model on customer support | fine-tuning | Mar 2024 | 12-18mo | Mar-Sep 2025 | PAST HALF-LIFE | Test base model equivalence Q2; plan deprecation |
| Data flywheel: 3yr of interaction logs | data-flywheel | Jan 2022 | 24-36mo | Jan-Sep 2025 | STILL AHEAD (20mo in) | Continue collection; no threat in next 12mo |
| 4-agent orchestration for workflow | harness/orch | Oct 2024 | 12-24mo | Oct 2025-Oct 2026 | Stable (6mo in) | Monitor Claude agent roadmap for native equivalents |

---

### Harness Assumption Register

| Harness Component | Model Limitation Assumed | Assumption Test Date | Still Valid? | If Invalid, Simplify To |
|--|--|--|--|--|
| Planner Agent | "Claude can't decompose 50-step tasks without losing coherence" | Apr 2026 | No | Remove planner; test direct planning in task agent |
| Memory Shard Manager | "Claude can't handle 200k token session history efficiently" | Apr 2026 | Yes, but Opus 4.7 pushes to 500k | Raise shard threshold from 100k to 250k tokens |
| Fact-Checker Node | "Claude hallucinates dates in long documents >20k tokens" | Apr 2026 | Partially (dates still 15% error at 20k+) | Keep for >15k docs; remove for <15k; test new embedding-based fact grounding |
| Router Agent | "Claude can't dynamically select the right tool for novel tasks" | Apr 2026 | No | Implement simple confidence-based routing; test single-agent with tools |
| Fallback Cache | "Claude's output is inconsistent for repeated queries" | Apr 2026 | No (deterministic outputs in 4.6+) | Remove fallback cache; simplify to single inference |

---

### Decision Log

**Quarterly Reviews:**
- [Date]: Capability A still ahead; prompt template refresh scheduled
- [Date]: Harness assumption X violated; simplified orchestration
- [Date]: Half-life on advantage Y approaching; renewal plan triggered

---
```

**Usage notes:**
- **Capability Radar:** Update quarterly after testing latest model releases. Flag any commoditization acceleration.
- **Strategy Half-Life:** Review at 50% mark and 100% mark. If past 100% and advantage still holds, extend the estimate (you were conservative). If violated, trigger renewal or retirement.
- **Harness Register:** Update after each major model release. Test each assumption against the new capabilities. If violated, simplify and redeploy engineering.
- **Decision Log:** Brief entries of strategic choices. Useful for post-mortems ("We kept this too long") and future planning ("We nailed the timeline on this one").

This format prevents strategic debt from accruing silently.

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., build-or-buy, ai-use-case-readiness), generate the markdown handoff file as well.

## QUALITY GATE

Before you commit to building a custom capability:
- [ ] You've tested the latest model release on this exact task. Documented results.
- [ ] You've predicted the trajectory. (Rough estimate: when does this become commodity?)
- [ ] You've costed both paths: build it vs. wait + migrate.
- [ ] You've identified your switchover trigger. (What change in the model would force a pivot?)
- [ ] You have a user waiting to pay for this *now*, not in 6 months.

## WHEN WRONG

**You see this capability commoditizing faster than expected.**
- Your 8-week feature is obsolete in 3 months.
- Trigger: Model release jump in capability. Competitor ships a model-native version.
- Recovery: You have 2 weeks to pivot to a model-native approach or your feature becomes technical debt.

**You waited, but the capability didn't arrive.**
- You expected GPT-5 to do X. It doesn't. Now you're 12 months behind.
- Trigger: Model release doesn't deliver promised capability.
- Recovery: Build it now (late) or acquire a company that did.

**You built defensible, but the moat collapsed anyway.**
- Your fine-tuned model matched GPT-4 in 2023. GPT-4.5 renders it obsolete in 2024.
- Trigger: Capabilities jump unexpectedly.
- Recovery: You own the data + customer relationships. Migrate your value layer, not your capability layer.

**You prioritized capability over product.**
- You built something technically sophisticated that users don't want.
- Trigger: Your capability is solid, but adoption is 10% of forecast.
- Recovery: Reframe. What product problem does this capability actually solve? Start there.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
