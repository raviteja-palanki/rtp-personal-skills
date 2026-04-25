---
name: strategy-review
description: Quarterly strategic check for AI products. Chains strategy-canvas + moat-finder + competitive-map + cost-model + signal-scanner. Outputs a 25-point scorecard, strategic gaps, and 3 recommended moves for the next quarter. Triggers on "strategy review," "quarterly review," "where are we strategically."
version: 1.0.0
author: RTP (Ravi Teja Palanki)
chains:
  - strategy-canvas
  - moat-finder
  - competitive-map
  - cost-model
  - signal-scanner
---

# /strategy-review
**Quarterly strategic pressure test. Five dimensions. One scorecard. Three moves.**

> "A strategy review that ends with 'we're doing great' wasn't a review. It was a vibes check." — RTP

---

## WHEN THIS RUNS

Trigger phrases: "strategy review," "quarterly review," "where are we strategically," "is our AI strategy working."

Cadence: quarterly. Run before the next planning cycle, not after — the output should change what you fund next quarter.

Do NOT use this for:
- Single-feature strategy decisions (use `/design-ai-feature`)
- Pricing-only reviews (use `pm-product-strategy:pricing-strategy`)
- Competitive intel for a sales deal (use `pm-go-to-market:competitive-battlecard`)

---

## INPUT

The user invokes this with optional focus area. If empty, run the full review.

If a focus area is named (e.g., "our AI agents positioning"), keep the structure but bias every step toward that area.

If context is thin, ask:

1. "What's your primary AI bet right now — the one thing eating most of the team's time?"
2. "Who are your top 2-3 competitors or alternatives in this space?"
3. "What changed in the last 90 days that prompted this review?"

---

## STEP 1 — STRATEGY-CANVAS

**Skill: `strategy-canvas`**

Map the current AI strategy across the canvas dimensions:

- **Vision** — Where are we trying to land in 3 years?
- **Customer outcome** — What user problem are we solving (the JTBD)?
- **Where we play** — Which segment, which use cases, which moments?
- **How we win** — What's the differentiator (capability, data, distribution, trust)?
- **Capabilities** — Which AI capabilities are we betting on (and what's the half-life)?
- **Trade-offs** — What did we say NO to in service of YES?
- **Metrics** — How will we know this is working?

For each dimension, score: **Strong** (clearly articulated, team aligned) / **Weak** (loosely articulated) / **Missing** (not yet defined).

Flag any **Missing** dimension as a critical gap. Strategy with a missing dimension isn't a strategy — it's a list of features.

---

## STEP 2 — MOAT-FINDER

**Skill: `moat-finder`**

Where does AI defensibility live? Run the four-source check:

| Source | Question | Status |
|---|---|---|
| Data flywheel | Does usage create proprietary data the AI uses to improve? | Strong / Emerging / Absent |
| Workflow lock-in | Is the AI deeply integrated into the user's daily work? | Strong / Emerging / Absent |
| Context depth | Does the AI know things about the user that took time to learn? | Strong / Emerging / Absent |
| Earned trust | Has the AI proven safe and accurate enough that users hand over more autonomy? | Strong / Emerging / Absent |

The blunt question: **If a competitor with the same model and 10x the engineering team copied this feature today, what stops them from winning?** If the answer is "nothing," your moat is the model itself — and the model is not your moat.

For each Absent or Emerging source: what would move it to Strong over the next quarter?

---

## STEP 3 — COMPETITIVE-MAP

**Skill: `competitive-map`**

Map the AI competitive landscape. Direct competitors, alternative approaches, and the platform players (OpenAI, Anthropic, Google) that could absorb your category.

For each competitor:

- **What they do well** — be honest, not defensive
- **Where they're weak** — the gap you can attack
- **What changed in 90 days** — new feature, new capability, new pricing
- **Threat level** — Existential / Material / Watch

The platform-player check: if OpenAI or Anthropic shipped a feature next quarter that does 80% of what you do, would you survive? If the answer is "we'd be in trouble," you're building on someone else's roadmap. Plan accordingly.

---

## STEP 4 — COST-MODEL (Strategic Pass)

**Skill: `cost-model`**

A strategic cost model is different from a feature-level cost model. Here you check:

- **Per-call cost trajectory** — has it gone up, down, or sideways in 90 days? Why?
- **Volume trajectory** — are calls growing faster than revenue? That's a margin compression you'll feel in two quarters.
- **Margin at GA volume** — extrapolate to your 12-month volume target. Is the unit economics still positive?
- **Optimization runway** — what's the next 50% cost reduction lever, and is it scoped?

The strategic question: **Are we ahead of the cost curve or behind it?** Companies that win on AI are the ones who know their cost curve cold and have a credible plan for the next two halvings.

---

## STEP 5 — SIGNAL-SCANNER

**Skill: `signal-scanner`**

What's changing in the AI landscape that we haven't responded to yet? The last 90 days only. Five categories:

| Category | What to scan | So what |
|---|---|---|
| New model capabilities | What can models do now they couldn't 90 days ago? | Does this open a feature we can build, or commoditize one we have? |
| New tools / infra | What's available now (eval tools, agent frameworks, RAG infra)? | Should we adopt? Build? Ignore? |
| Competitor moves | What did competitors ship or announce? | Existential / Material / Watch |
| Customer signals | What are users asking for that we're not building? | Demand pattern or noise? |
| Regulatory shifts | What changed in policy, compliance, or risk landscape? | Cost increase, restriction, opportunity? |

For each signal: **what action does this trigger?** A signal without an action is observation, not strategy.

---

## STEP 6 — THE SCORECARD

After all five steps run, score each dimension on a 1-5 scale. Honest scoring or skip the exercise.

| Dimension | Score (1-5) | Rationale |
|---|---|---|
| Strategy clarity | | Is the strategy articulated, with all canvas dimensions filled? |
| Moat strength | | How many sources are Strong vs. Emerging vs. Absent? |
| Competitive position | | Are we leading, parity, or behind in our segment? |
| Cost trajectory | | Are we ahead of or behind the cost curve? |
| Signal responsiveness | | Have we acted on the last 90 days of changes? |
| **Total** | **/25** | |

**Interpretation:**

- **20-25:** Strong strategic position. Focus is on execution and compounding.
- **15-19:** Workable strategy with known gaps. Identify the one weakest dimension and invest there.
- **10-14:** Strategy is fragile. At least two dimensions are Weak or Missing. Pause new bets, fix the foundation.
- **<10:** Not a strategy. Stop and rebuild before next quarter starts.

---

## STEP 7 — THREE MOVES FOR NEXT QUARTER

Distill the review into three (and only three) recommended moves. Not five. Not "and also." Three.

For each move:

- **What to do** — specific, scoped, owned by a named person
- **Why this move** — which dimension of the scorecard does it lift?
- **What success looks like at end of quarter** — measurable
- **What we're NOT doing** because of this — the trade-off

The discipline of three moves is the discipline of strategy. A list of ten moves is a wish list. Three moves is a portfolio.

---

## OUTPUT FORMAT

```
Strategy Review — [Quarter, Year]
Date: [DDMMMYYYY]
Owner: [PM name]
Focus area: [If specified]

SCORECARD
- Strategy clarity: [N/5]
- Moat strength: [N/5]
- Competitive position: [N/5]
- Cost trajectory: [N/5]
- Signal responsiveness: [N/5]
- TOTAL: [N/25]

INTERPRETATION
[One paragraph — what the score means for the next quarter]

TOP STRATEGIC GAPS (max 3)
1. [Gap, with evidence]
2. [Gap, with evidence]
3. [Gap, with evidence]

THREE MOVES FOR NEXT QUARTER
1. [Move name]
   - What: [specific action]
   - Why: [scorecard dimension lifted]
   - Success: [measurable end-of-quarter signal]
   - Trade-off: [what we're not doing]

2. [Move name] — same structure

3. [Move name] — same structure

THINGS TO STOP DOING
[Bets that are low-conviction and consuming resources]

THINGS TO WATCH
[Signals from Step 5 that don't yet warrant action but could escalate]
```

---

## QUALITY BAR

A real `/strategy-review` produces:

- A scorecard with honest numbers, not "we're a 4 in everything"
- Three moves, not ten
- Clear trade-offs (what we're saying NO to in order to say YES to the three)
- Identification of the platform-player risk (could OpenAI absorb our category)
- A cost trajectory check, not just current cost
- A signal scan that's tied to action, not just observation

**The test:** Read it to a board member. They should be able to ask "why this and not that?" and get an answer that doesn't dissolve under pressure. If everything is "important," nothing is.

---

## CROSS-REFERENCES

- **Run before:** annual planning, OKR-setting (`pm-execution:plan-okrs`)
- **Run after:** any major competitor launch, model capability shift, or cost-curve change
- **Related workflows:** `/design-ai-feature` for individual feature strategy, `/retro` for post-ship learning
- **Skill files used:** `strategy-canvas`, `moat-finder`, `competitive-map`, `cost-model`, `signal-scanner`
