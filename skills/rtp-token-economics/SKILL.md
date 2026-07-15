---
name: rtp-token-economics
description: "How to charge for an AI product, where your best users are your most expensive users and the work is done by the model, not the seat. Answers the two questions SaaS never had to: which value metric tracks your cost-and-value distribution (the six 2026 models — hybrid tiered, usage, credit pools, outcome-based, seat + add-on, freemium), and which budget you're billing against (software vs the ~10×-larger salary budget). Carries the pricing transition arc (per-seat dies → tiered → outcome → services-as-software), the packaging decision (bundle / add-on / standalone), the quality-cost-latency trade-off, and the margin-discipline moves (rate-limit staircase, trust trap). Consumes cost-per-outcome at P90 from cost-model; produces the pricing decision that sets the launch motion. Use when pricing, repricing, or when usage grows faster than revenue. Pairs with: cost-model, moat-finder, adoption-launch. Triggers: 'pricing for AI', 'how to price', 'token economics', 'usage-based vs flat-rate', 'per-seat is dying'."
imports: [stress-test, red-team]
---

# Token Economics

## THE ONE IDEA

In normal software, one more user costs almost nothing, so you charge per seat and forget it — margins run 70-90%. In AI, every prompt, document, and agent run burns compute, so **your best users are your most expensive users**, and margins run 20-60%. That single fact breaks per-seat pricing and forces two questions SaaS never had to ask: **which value metric tracks your cost-and-value distribution**, and **which budget are you billing against**. Get the metric wrong and power users bankrupt you (Cursor's $7,225 invoice; GitHub Copilot losing money per user at launch). Get the budget wrong and you either leave 10× on the table or price yourself out of the deal.

## THE TRAP

You will copy SaaS pricing and be wrong within six months. The bias is **inherited mental models** — every product you know charges per seat, so you will too. But per-seat charges your most expensive user the same as your cheapest, and in AI those differ by 10-100×. Flat-rate subsidizes power users until the margin bleeds out; pure per-token kills adoption because users feel taxed for thinking; outcome pricing only works where the outcome is unambiguous *and* you can measure it. There is no safe default — the model has to match your actual usage distribution and the budget you displace.

## KEY TERMS (plain, industry-standard)

- **Value metric** — the unit you charge for: a seat, a token, a credit, or an outcome. The most consequential choice; it decides who overpays and who bankrupts you.
- **The P90 user** — the 90th-percentile user by cost. Price against them, not the average; the average user is irrelevant to whether you survive.
- **Software budget vs salary budget** — the budget your value comes out of. Software is a low single-digit % of revenue (IT procurement); salary is the fully-loaded cost of the person you replace — roughly 10× larger. Same product, very different ceiling.
- **Pricing transition arc (the "SaaSpocalypse")** — per-seat → tiered usage → outcome-based → abstracted-value → services-as-software. Per-seat dies at scale; the arc is mandatory, the only question is proactive or in crisis.
- **Services-as-Software** — the customer pays for the work the AI does (a resolved ticket, a processed invoice), the way they'd pay an outsourced service, not for a license. Foundation Capital's default B2B-AI frame for 2026.
- **Fair-use cap / the rate-limit gambit** — contract language ("up to N calls per seat") that throttles the top <5% toward per-token, where cost is covered precisely (Anthropic's move).
- **Quality-cost-latency triangle** — you can optimize two; pricing must respect the trade-off.

## WHAT THIS SKILL CONSUMES & PRODUCES

Pricing does not stand alone — it sits between the cost side and the go-to-market side. Name the handoffs before you start.

**Consumes (inputs):**
- **Cost per successful outcome at P90** — from `cost-model`, not the mean, and *after* regenerations and harness overhead. If you cannot get this number, stop and measure it first.
- **Usage distribution** — P10/P50/P90/P99 requests and cost per user, from 30+ days of instrumentation.
- **Competitive pricing** — what the alternative charges and how it breaks, from `competitive-map`.
- **Which budget the buyer pays from** — software or salary (Step 0 below).
- **Segment + architecture** — B2B API / B2B SaaS / B2C / enterprise platform, and Copilot / Agent / Augmentation, from `strategy-canvas`.

**Produces (outputs):**
- **The pricing decision** = value metric × pricing model × packaging, with the transition arc planned.
- **The launch motion** → `adoption-launch`: a bundle ships as a feature update; an add-on ships as a new SKU; a standalone ships as a full GTM. Do not run a bundle motion for an add-on product.
- **The margin target** the cost side must hit → back to `cost-model`.
- **The pricing-as-strategy narrative** → `stakeholder-communications` / the board.

## STEP 0 — WHICH BUDGET ARE YOU BILLING? (THE CEILING)

Before any pricing mechanic, answer this — it sets how *high* you can charge, which the mechanic cannot. A tool that is just more software is paid from the **software budget** (capped by IT-procurement norms). A tool that does the work of a paid expert is paid from the **salary budget** — the loaded cost of the person plus the mistakes avoided — roughly ten times larger.

This is the real reason outcome and value pricing command a premium: not that outcomes are "discrete," but that a judgment outcome crosses into the salary budget. It is also the agentic-era reframe of the per-seat death — an agent isn't a seat, it does a person's job, so its pricing *migrates* from the software budget to the salary budget. **When wrong:** the salary-budget ceiling only holds where you genuinely replace expert labor. A record-lookup tool dressed up as "judgment software" stays on the software budget, and the higher ceiling is a mirage that will price you out. *(Stanton, "AI's Impact on SaaS Will Be Uneven," HBR, 27 May 2026; Agrawal, "AI Is Rewriting the Economics of Outsourcing," HBR, 5 Jun 2026.)*

## THE SIX PRICING MODELS (2026)

Mapped across the 50 highest-valued AI companies. **Pure-play pricing is dying — nearly half run two or three of these at once** (a consumer subscription, a usage-based API, a free tier). Pick per product line, not per company.

| Model | Mechanism | Fits | How it breaks | Example |
|---|---|---|---|---|
| **1. Hybrid tiered subscription** | Tiers with rising usage limits + model access | Consumer AI; the default | Undisclosed limits → users feel gaslit hitting a wall | Claude Free→Pro $17→Max $100/$200; ChatGPT |
| **2. Usage-based / per-token** | Pay per unit of compute | B2B APIs, developers | Surprise four-figure bills; thin moat (inference fell ~78% in 2025) | Anthropic/OpenAI API |
| **3. Credit / token pools** | Flat sub buys a credit pool that depletes by action | Multi-feature products with varied cost | Trust revolt when a predictable plan turns variable | Cursor (the $7,225 invoice), Midjourney |
| **4. Outcome-based** | Pay per successful outcome | Clean, measurable outcomes | Revenue drops on a bad model week; measurement infra rarely exists | Intercom Fin $0.99/resolution |
| **5. Seat-based + AI add-on** | Per-seat base, AI in a premium tier/add-on | Established SaaS adding AI | Your heaviest users pay the same as your lightest | Notion, GitHub Copilot, Canva (+300%) |
| **6. Freemium / reverse trial** | Give AI away to build habit, monetize upgrades | PLG, consumer scale | Brutal compute burn; <2-3% conversion = too generous | OpenAI (900M weekly), Perplexity |

Reverse trial (full access 14 days → downgrade) beats a permanently crippled free tier — users feel the premium quality before the wall, which converts better.

## THE THREE INPUTS THAT PICK THE MODEL

1. **Cost structure.** Tokens as a % of *gross margin* (not revenue), computed at P90. >50% → usage-based or outcome mandatory; 20-50% → hybrid; <20% → seat-based survivable.
2. **Usage distribution.** P90 ÷ P10 request ratio. Under ~2× → flat-rate works; over ~5× → flat-rate fails and you need tiered, credits, or outcome. (Gini > 0.6 = flat-rate is risky.)
3. **Competitive landscape.** No competitor → optimize for margin. Competitor on per-seat → you can win on usage-based if it's fairer. Competitor on per-token → match unless quality justifies a premium. The trap: don't copy a competitor's tiers off their pricing page — derive tiers from *your* usage data.

## THE PRICING TRANSITION ARC — PLAN IT BEFORE THE CRISIS

Per-seat pricing dies because AI cost distributions are log-normal, not uniform. The response is an arc, and each step is a 1-2 quarter project:

**per-seat (legacy) → tiered usage → outcome-based → abstracted-value (credits) → services-as-software.**

Two rules that decide whether the arc costs you a quarter or a customer. **Price for the actual usage profile, not the headline.** Klarna priced for "AI replaces 853 FTEs"; reality was ~65% AI / 35% human nuance, and both sides renegotiated. **Start before per-seat fails.** The team that adds tiered caps proactively has runway; the team that waits for the CFO's question has three bad options — retroactive overage (renewal risk), absorb the loss (margin damage), or full redesign (12-month sales cycle). Cursor's transition was reactive and public; the brand paid for it.

## THE PACKAGING DECISION — BUNDLE / ADD-ON / STANDALONE

Separate from the value metric: *do you charge for the AI separately at all?* Three signals decide it (Broe's 44-incumbent study: 59% bundle, 23% add-on, 18% standalone).

- **Marginal cost at P90.** <5% of revenue → bundle is safe. 5-20% → bundle with fair-use, or hybrid. >20% → add-on or usage-based mandatory (bundling means losing money on power users).
- **New value vs improvement.** Fill in "Before our AI, users could ___." If it's "do this manually / worse," it's an *improvement* → **bundle** (charging separately invites a competitor to include it free). If it's "couldn't do this at all," it's *new value* → **add-on**, or **standalone** only if it reaches a genuinely new buyer (Cursor pattern).
- **Separable willingness-to-pay.** When sales mentions AI, does the prospect ask "what's the price for that?" (separable WTP → add-on) or "is that included?" (table stakes → bundle).

The most-miscalled path is standalone: if it's sold to the same buyer, same cycle, same logo, it's an add-on with bad packaging.

## THE QUALITY-COST-LATENCY TRIANGLE

Pick two; the third suffers. Flat-rate buys quality + latency (unlimited, no guilt) but cost spirals. Per-token buys cost + latency but quality drops (users avoid hard questions). Outcome buys quality + cost but the user waits. The trap: optimizing for cost control quietly destroys quality perception — users stop asking complex questions. Translate each vertex into what the customer actually sees and instrument it before you price: **quality = acceptance rate** (% used as-is), **cost = price per outcome** (not per token), **latency = time to first useful token** (P50/P95, measured client-side). And watch the multiplier: **a regeneration doubles the real cost per outcome** — quality failures are cost failures, not just UX ones.

## THE MARGIN-DISCIPLINE MOVES (AGENTIC ERA)

- **The rate-limit staircase.** Want heavy usage, but throttle the top <5% toward the per-token API where cost is covered precisely (Anthropic's $17 → $100 → $200 + weekly limits). Undisclosed limits buy margin flexibility at the cost of trust — decide that trade knowingly.
- **The trust trap.** Never convert a predictable plan to a variable one without over-communicating. Cursor flipped flat-500-requests to credit pools and the CEO published a public apology twelve days later. Pricing changes are sticky and trust is fragile.
- **Outcome pricing's real blocker is measurement.** Outcome-based only works where the outcome is unambiguous *and* instrumented (a resolved ticket, a merged PR). For most categories the measurement infrastructure doesn't exist yet — build it before you promise to price on it.

## THE COST SIDE LIVES IN `cost-model` — NOT HERE

Pricing *consumes* cost numbers; it does not compute them. The full cost mechanics — the harness multiplier (a Planner/Generator/Evaluator loop is 10-22× a single call), hidden costs (hallucination correction, retrieval, fine-tuning, support escalation), model routing, prompt caching (~90% off cached tokens), and batch APIs (~50% off) — all live in `cost-model`. Pull one number from there before you price: **cost per successful outcome at P90, after regenerations and harness overhead.** If that number isn't available, you have a measurement problem, not a pricing problem — fix it first.

## WHERE YOU ARE — OUTPUT

```
## Pricing Decision: [Product / line]

Which budget: [software (~low single-digit % of rev) | salary (~10×) — and the evidence you displace expert work]
Value metric × model × packaging: [e.g., outcome × per-resolution × add-on]
Chosen from: cost structure [tokens % of P90 margin] · usage spread [P90/P10] · competition
Transition arc: [today → 12mo → 24mo], next step = [the 1-2 quarter project]
Quality-cost-latency: [which two optimized, which sacrificed, how instrumented]
Margin check: [gross margin at P90 today | at 10× usage | at 100× — where it breaks]
Trust guardrail: [comms plan if changing a predictable plan to variable]
```

Flag anything still open as `OPEN: [the decision] — [what evidence would settle it]` (e.g., "OPEN: is the outcome measurable enough to price on? — needs 30 days of resolution-attribution data").

## WHEN WRONG

- **Pre-launch.** Pricing is premature until you know the usage distribution; ship, instrument 30 days, then price.
- **Fully custom / enterprise-negotiated** deals where standardized models don't apply.
- **Non-profit or subsidized research** contexts.
- **When pricing is already committed** — raising alienates, lowering is permanent. Price correctly the first time.

---

## GROUNDING, DELIVERABLE, TRADE-OFFS & CONCLUSION

Before starting, follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) Section 1 grounding questions (who is the customer, what problem, YES/NO scope) and confirm output format (Word / deck / inline; default Word). Close with the Trade-Off Ledger (Section 3) and the Conclusion Protocol (Section 5): state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action. If the decision hands off to `adoption-launch` or `cost-model`, generate the markdown handoff.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual — the six-model matrix (cost transparency × customer alignment, segment fit annotated) or the pricing transition arc with the trigger for each step. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
