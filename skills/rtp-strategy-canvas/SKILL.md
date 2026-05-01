---
name: rtp-strategy-canvas
description: "AI product strategy that survives quarterly capability changes: 6-month horizons, conditional bets (IF model X → Path A), model-agnostic moats, reset triggers. Use for: strategic direction, roadmap review. Triggers: 'AI strategy', 'product strategy for AI', 'strategic direction', 'roadmap for AI'"
imports: [first-principles, falsification]
---

# Strategy Canvas

## DEPTH DECISION

**Go deep if:** You're setting a 6-month strategic horizon for an AI product, evaluating a roadmap against model capability changes, or designing for moat defensibility in a fast-moving space.

**Skim to diagnostic questions if:** You want a quick strategy audit or quarterly reset check.

**Skip if:** Pre-product-market fit where experimentation matters more than strategy. If you need agent harness *architecture* (orchestration framework, context caching, eval metrics), use the **agent-harness** skill — this skill covers strategic direction. If you need a competitive analysis of moats, use **moat-finder**.

## DELIVERABLE FORMAT

Before starting, ask: Word Document, Presentation, or Both?
Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

The mistake you're about to make: **writing a static 12-month strategy and calling it "adaptive."**

Here's how it plays out. You design a roadmap against today's model capability. Three months later a new model ships that invalidates two of your four bets. You don't revise — the roadmap is already in the deck, stakeholders are aligned, quarterly milestones are set. You ship features the base model absorbed three months ago.

This is **planning fallacy meets AI frontier**. The bias compounds because static strategies *look* professional (printed roadmaps, quarterly milestones) while adaptive strategies look messy (conditional bets, regular re-evaluation). You optimize for the appearance of strategy rather than the substance.

**The fix:** Set a **6-month strategic horizon with quarterly trigger checks** — not a 12-month plan with annual reviews. Every bet has explicit conditions ("IF capability X reaches level Y by date Z") and explicit fallbacks. When a trigger condition changes, the strategy updates. This isn't indecisiveness — it's how competent AI strategy actually works.

**The contradiction to avoid:** If your strategy document has no expiration date — if there's nothing that would force a re-check — you have a planning document, not a strategy.

---

## THE PROCESS

**Step 1: Separate stable from volatile.** Create a table:
- **Stable (12+ months):** User problems, market structure, regulatory constraints, organizational capabilities
- **Volatile (3-6 months):** Model capability, token cost, competitor feature parity, tool availability, context window size

Strategy anchors on stable. Strategy adapts on volatile.

> **Diagnostic check:** For each initiative on your roadmap, ask: "Is this anchored to something stable or volatile?" If it's anchored to a volatile assumption (e.g., "GPT-4o is currently the best at X"), it needs a conditional trigger, not a fixed milestone. If your strategy has more volatile anchors than stable ones, the first major model release will require a full rewrite.

---

**Step 2: Define capability-conditional bets.** For each major product bet, write:

*"IF [capability threshold] by [date], THEN build [path A]. IF NOT, THEN build [path B]."*

Example: "IF multi-step reasoning reaches >90% accuracy by Q2, THEN invest in autonomous agents. IF NOT, THEN invest in AI-assisted human agents."

Each bet needs three parts:
- **Trigger:** A measurable capability threshold (pass@k accuracy %, cost per call, P95 latency)
- **Condition:** An external checkpoint date (quarterly, not annual)
- **Fallback:** A Path B that's ready to execute — not "we'll figure it out"

> **Q: "How specific should the trigger be?"**
>
> **Think through:** Can someone on your team check this number quarterly without ambiguity? If not, it's too vague.
>
> **Vague (unusable):** "IF AI gets better at reasoning" — better by how much? Measured how?
>
> **Specific (usable):** "IF pass@10 accuracy on [our internal eval suite] reaches 85% by end of Q2" — checkable, unambiguous.
>
> **Red flag:** If your trigger is "when the team feels confident in the model," you don't have a conditional strategy — you have a decision you're deferring. Name the number.
>
> **Sharpen it:** For each bet, ask: "What number do we track, and how often?" If you can't answer in 10 seconds, spend 15 minutes defining the metric before building the strategy.

> **Q: "How strong does Path B need to be?"**
>
> **Red flag:** If your Path B is "delay the feature" or "we'll reassess," you haven't designed a real conditional strategy — you've written Plan A with a panic option. Path B should be something you'd ship and be proud of. If it isn't, the bet is premature.

---

**Step 3: Identify unique context advantage.** What can't a competitor replicate by switching models?
- Proprietary data (domain-specific, hard to recreate)
- Workflow depth in a specific domain (deep integrations, habit formation)
- Enterprise trust/compliance credentials (SOC 2, HIPAA, existing relationships)
- Customer integration lock-in (APIs, data pipes, embedded in daily workflow)

Pick 1-2 that are model-agnostic. A moat without multiple vectors is fragile. A moat that depends on the current model is not a moat.

> **Q: "Is this actually a moat or a temporary feature lead?"**
>
> **The test:** "If our competitor switches from GPT-4 to Claude tomorrow, does this advantage disappear?"
> - If **yes** — it's a feature parity race, not a moat.
> - If **no** — you have something worth protecting.
>
> **Low (feature lead, not moat):** "We use model X and it produces better outputs." Competitor matches this in one model release.
>
> **Mid (emerging moat):** "We have 6 months of customer workflow integrations that would take a competitor 6 months to replicate." Durable for a strategic window.
>
> **High (durable moat):** "We have proprietary domain data + workflow lock-in + user behavior that trains the system. A competitor with a better model still can't replicate what we've learned." Survives multiple model generations.
>
> **Red flag in your inputs:** If your moat section says "we use [model X] and it's better than [model Y]" — you have a temporary lead. Six months from now, all providers will have equivalent capability on standard tasks. Build the advantage that survives that equalization.

---

**Step 4: Build one-page strategy canvas:**

```
STRATEGIC HORIZON | 6 months from [date]. Reset: [quarterly date].
PROBLEM           | What user problems are we solving? (stable anchors)
CAPABILITY-BETS   | Path A (IF X by date), Path B (IF NOT X)
MOAT              | Which defensible advantage(s)? Model-agnostic?
RESET TRIGGERS    | What fires a strategy reset before the quarterly date?
NEXT REVIEW       | Specific date — max 90 days out.
```

---

**Step 5: Account for capability shift problem.** Features you build, foundation models absorb.

Example: You ship "context window optimization" as a feature (compress docs into summaries). In 6 months, base models include 200k context windows. Your feature is obsolete. This isn't failure — it's the frontier moving.

**Defense strategies:**
- **Deepening:** Instead of "optimization," shift to "judgment" (which docs matter). Requires proprietary training data.
- **Lock-in:** Embed your feature in workflow so deep that switching costs exceed the value of model improvements (integration moat).
- **Velocity:** Ship faster than models improve. Not sustainable long-term, but buys time.

For each planned feature, ask: "If the model absorbs this capability in 6 months, what's our fallback?" If no fallback exists, that feature is a risk to your roadmap — not a moat.

---

**Step 5.5: Estimate strategy half-life.** How long before model improvements invalidate your strategy?

| Time horizon | Stability | Strategy guidance |
|---|---|---|
| 0-3 months | Frontier features (long-context, tool use, reasoning) | Use as triggers — not as bets. Strategy built here is dead on arrival. |
| 3-6 months | Competitive features (speed, cost, quality) | Conditional bets here. Expect to adjust 2× per year. |
| 6-12 months | Market structure | Slower to shift. Good anchors. |
| 12+ months | User problems, organizational capabilities | Most stable. Strategy anchors here. |

Build strategy primarily on 6-12 month anchors. Use 3-6 month contingencies with triggers. Avoid 0-3 month frontier features as strategic foundations.

---

**Step 5.75: Agentic PMF lens.** If your product is agent-first (autonomous, multi-step), adjust your strategy.

| Product type | What users want | PMF definition |
|---|---|---|
| Traditional AI | "Answer my question" | Accuracy + latency + price |
| Agentic AI | "Complete my goal" | Reliability + error recovery + autonomy calibration |

**Capability bets shift:**
- NOT: "If LLM reaches 95% accuracy, build X"
- BUT: "If multi-step agentic reasoning reaches 85% success rate with <2 hallucinations per 10 steps, build autonomous mode. Otherwise, co-pilot mode."

**Failure mode planning shifts too:**
- Traditional: "If accuracy drops 5%, users notice immediately"
- Agentic: "If multi-step reliability drops 10%, users notice eventually — invest in monitoring and transparent failure so failures are surfaced, not hidden"

---

## RESET TRIGGERS

A strategy document that can't be invalidated is not a strategy — it's a plan.

These are the five conditions that should immediately trigger a strategy reset, not wait for the next quarterly review:

**Trigger 1 — Major model capability jump (>15% improvement on your evaluation benchmark)**
When a model releases with meaningful improvement on the benchmark most relevant to your product (reasoning accuracy, code correctness, multimodal fidelity), re-evaluate your capability bets. Features you planned to build may already exist in the base model.

**Trigger 2 — Competitor ships a feature you had in your 6-month plan**
Your moat calculation changes. The question is no longer "should we build X?" but "does our differentiation hold if they have X?" Answer that before continuing.

**Trigger 3 — Inference cost drops >40%**
Costs drop roughly 10x every 12-18 months. When they drop significantly, use cases that were economically impossible become viable — and your cost model assumptions about which features to build change.

**Trigger 4 — Core user assumption disproven by your own data**
If your strategy assumed "users want X" and you have 4+ weeks of evidence that users don't want X (low acceptance rate, high correction rate, low return usage), the strategy needs to revisit that bet — not just the feature design.

**Trigger 5 — Regulatory signal in your domain**
For healthcare, finance, legal, or any regulated vertical: a regulatory guidance, enforcement action, or announced framework in your space changes the risk calculus on autonomy and safety bets. Don't wait for the quarterly review.

> **How to operationalize:** Document these 5 triggers alongside your strategy canvas in a shared doc. Anyone on the team should be able to say "Trigger 2 just fired — here's what they shipped" and know that means a strategy reset conversation, not just a roadmap note.
>
> **Calibration signal:** If your triggers never fire across 6 months, they're too vague to be meaningful. Sharpen the thresholds.

---

**Step 6: Set quarterly cadence.** Schedule the review. At each quarterly check, test:
- Did model capability hit a trigger or conditional bet threshold?
- Did cost structure change significantly?
- Did a competitor move into our territory?
- Do we still have the moat we claimed?
- Did capability shift absorb any features we planned to build?
- Do we need to deepen, lock-in, or accelerate?

---

## Harness Strategy *(Strategic case only — for architecture decisions, use: agent-harness skill)*

Your harness (agent orchestration, context management, eval pipeline, tool integration, error recovery) is a **strategic asset** — it survives model upgrades. This section explains why it belongs on your strategy canvas. For how to design it, use the **agent-harness** skill.

**The strategic case:** When the next model releases, you swap the model and keep the harness. Teams that invest in harness architecture:
- Can upgrade models with one-line config changes
- Run multi-model strategies (cheap model for routine tasks, expensive for complex reasoning)
- Are not locked into a single provider's pricing or deprecation decisions

**Teams that skip harness investment:**
- Rewrite their product when moving models
- Are vulnerable to single-provider pricing changes
- Have no competitive defense when models commoditize

**The moat this creates:** Your orchestration, context management, and tool integrations are harder for competitors to replicate than any model-specific feature. They can copy your features. They can't quickly replicate 12 months of tool integrations and eval infrastructure embedded in customer workflows.

**On your strategy canvas:** Treat harness maturity as a strategic investment line item with quarterly goals — not a technical decision. "Harness maturity" should appear on the canvas. For the architecture (orchestration framework, context caching strategy, eval metrics), defer to the **agent-harness** skill.

---

## The Model-Agnostic Moat

The moat is not the model. The moat is what you can do with any model that competitors can't replicate by switching models.

| Moat type | Example | Durability |
|---|---|---|
| **Model-dependent (fragile)** | "We built X using GPT-4's capability." Competitor builds X better with Claude. | Evaporates on next model release. |
| **Model-agnostic (durable)** | "We have 10 domain-specific tools integrated into hospital workflows, with 18 months of usage data training the system." | Survives model generations. |

**How to build model-agnostic moat:**
1. Create an abstraction layer between product and model
2. Document model swap cost (how many lines of code must change? Config only? Full rewrite?)
3. Plan model rotation: quarterly evaluate if cheaper/faster/better models exist
4. Lock-in through workflow depth — even if competitors replicate the abstraction, your customers are integrated into workflows they don't want to leave

---

## Strategy for Agentic Products

Agentic products have fundamentally different strategic dynamics: the product *is* the harness.

**Traditional AI product strategy:** Features, speed, cost, model capability.

**Agentic product strategy:** Harness maturity matters most.
- **Eval infrastructure:** Can you measure agent success systematically across thousands of scenarios?
- **Tool integration depth:** How tightly integrated are agents in customer workflows?
- **Error recovery:** How well do agents fail gracefully without human intervention?
- **Multi-step reasoning reliability:** How consistently does your orchestration work?

**Strategic investment split for agentic products:**
- 40% in eval infrastructure
- 30% in tool integration
- 20% in error recovery and monitoring
- 10% in model updates

Your competitive moat is eval infrastructure + orchestration quality — not model quality.

**Capability bets for agentic:**
- NOT: "If LLM reaches 95% accuracy, ship autonomous agents"
- BUT: "If we can measure agent success across 1,000+ scenarios, and error recovery works 95% of the time, ship autonomous agents. We accept 80% accuracy on individual steps — but we measure and surface every failure."

---

## OUTPUT FORMAT

```
## Strategy Canvas: [Product Name]

**STRATEGIC HORIZON:** 6 months from [date]. Reset: [quarterly review date].

**STABLE ANCHORS** (valid 12+ months):
- [User problem 1]
- [Market structure constraint]
- [Regulatory constraint]
- [Org capability]

**VOLATILE ASSUMPTIONS** (valid 3-6 months):
- [Model capability threshold]
- [Token cost assumption]
- [Competitor feature parity assumption]

**CAPABILITY-CONDITIONAL BETS:**
1. IF [measurable trigger] by [date] THEN [Path A]. ELSE [Path B — specific, shippable].
2. IF [measurable trigger] by [date] THEN [Path A]. ELSE [Path B — specific, shippable].
3. IF [measurable trigger] by [date] THEN [Path A]. ELSE [Path B — specific, shippable].

**MOAT:**
- Type: [proprietary data | workflow depth | tool integration | enterprise trust]
- Evidence: [specific advantage vs. competitor]
- Model-agnostic? [Yes: survives any model change | No: explain why it's still defensible]

**HARNESS STRATEGY:**
- Strategic goal: [what capability the harness must support by Q_]
- Model swap readiness: [config-only | partial rewrite | full rewrite — and why]
- For architecture decisions, run: agent-harness skill

**RESET TRIGGERS LIVE:**
- [ ] Model capability jump >15% on [specific benchmark]
- [ ] Competitor ships [specific feature]
- [ ] Inference cost drops >40%
- [ ] Core assumption disproven: [which assumption, which signal]
- [ ] Regulatory signal in [domain]

**STRATEGY HALF-LIFE:** [3 months | 6 months | 12 months] — because [reason]

**NEXT REVIEW:** [specific date, max 90 days out]
```

---

## REALITY CHECK

- **Prediction fails.** You will be wrong about model capability timelines. Design for scenario planning, not point estimates.
- **"Use the best model" is not strategy.** It's a dependency. Real strategy answers: what do we do when the best model is the competitor's?
- **Strategy without moat is a feature list.** It will be copied in weeks. Real strategy answers: why can *only* we solve this?
- **Quarterly reviews must actually happen.** Scheduled, not optional. If you skip them, this becomes static theater.
- **Harness survives models.** The strategic asset is orchestration, context management, and tool integration — not which model you're using today.
- **A strategy without an expiration date is a plan.** Set the horizon. Set the triggers. Schedule the reset.

---

## QUALITY GATE

- [ ] Stable vs volatile assumptions explicitly separated
- [ ] Strategic bets are capability-conditional with measurable triggers and real Path B fallbacks
- [ ] Unique context advantage identified and passes the model-agnostic test
- [ ] Strategy canvas produced as a one-page artifact
- [ ] Strategic horizon is **6 months**, not 12 months
- [ ] **Five reset triggers** documented alongside the canvas
- [ ] Quarterly review date set (maximum 90 days out)
- [ ] Harness strategy appears as a strategic line item (not just a technical footnote)
- [ ] If agentic product: eval infrastructure and error recovery included with specific targets
- [ ] All triggers are **measurable** — a number, not a feeling

## WHEN WRONG

- Very early-stage companies where finding product-market fit matters more than strategy
- When the team needs to execute, not strategize (analysis paralysis risk)
- When the market is so new that strategic analysis has insufficient data to anchor on
- **When you need harness architecture:** Use **agent-harness** skill instead
- **When you need moat depth:** Use **moat-finder** for competitive analysis and moat scoring

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. **The recommendation** — clear strategic direction, not "it depends"
2. **The hypothesis** — "We believe [X] will [Y] because [Z]. We'd know we're wrong if [signal] within [timeframe]."
3. **The key trade-off** — what we're prioritizing and what we're giving up
4. **The biggest risk** — and the specific mitigation
5. **The next action** — [step] by [role] by [date]

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (moat-finder, agent-harness, capability-tracking), also generate the markdown handoff file per Section 9.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. The diagram should show:
- The capability-conditional bets as a branching tree (IF → Path A vs IF NOT → Path B)
- Stable anchors vs volatile assumptions as two columns with a dividing line
- The moat type plotted on a model-agnostic (durable) ↔ model-dependent (fragile) spectrum

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
