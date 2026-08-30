---
name: token-economics
version: v1.3_latest
description: "How to charge for an AI product, where your best users are your most expensive users and the work is done by the model, not the seat. Built on six first-principles axioms (cost is power-law physics; incentives must align with value not consumption; budgets are hierarchical; margin lives in the applied/harness layer; opacity kills trust; negative margins are temporary subsidies). Answers the two questions SaaS never had to: which value metric (the six 2026 models, ranked), and which budget (software vs the ~10× salary budget). Carries the agentic value-metric decision tree, the transition arc with stage gates, spend-visibility + routing as survival infrastructure, the Default-FAIL gate for outcome pricing, a mandatory margin-floor check at P90, and 2026 case law. Consumes cost-per-outcome@P90 from cost-model; produces the pricing decision + spend-control design. Pairs with: cost-model, moat-finder, adoption-launch. Triggers: 'pricing for AI', 'how to price', 'token economics', 'per-seat is dying'."
imports: [stress-test, red-team]
---

# Token Economics

## THE ONE IDEA

In normal software, one more user costs almost nothing, so you charge per seat and forget it — margins run 70-90%. In AI, every prompt, document, and agent run burns compute, so **your best users are your most expensive users**, and margins run 20-60%. That single fact breaks per-seat pricing and forces two questions SaaS never had to ask: **which value metric tracks your cost-and-value distribution**, and **which budget are you billing against**. Get the metric wrong and power users bankrupt you (Cursor's $7,225 invoice; GitHub Copilot losing money per user at launch). Get the budget wrong and you either leave 10× on the table or price yourself out of the deal.

## FIRST PRINCIPLES OF AI PRICING (reason from these, not from SaaS)

Before you pick a model, reason from the ground up. Six basics keep this skill sound when new models ship, open-weight models get cheaper, or funding tightens.

1. **Cost is real, and lopsided.** Every token is real energy, chip time, and scarce-GPU cost — never free, never uniform. A tiny fraction of users, sessions, and agents run up most of the bill. **The average user is a lie.** The only number that decides survival is cost at the **90th/99th percentile, after all the real overhead** (harness loops, regenerations, tool calls, failed attempts, support).
2. **Incentives must align with value created, not consumption.** Per-seat: seller wants seats, buyer wants usage — breaks when AI does the work. Pure per-token: seller wants tokens, buyer feels taxed for thinking. Outcome/services-as-software: both want correct, completed work. The ultimate unit is the **economic surplus created** (usually displaced expensive human labor).
3. **Budgets stack, and they're sticky.** The software/IT budget is small, closely watched, and capped. The salary/labor budget is ~10× bigger and opens up *once you can prove you replace a person or make one do 10× the work*. Stay in the software budget and your ceiling stays permanently low.
4. **The raw model is becoming a cheap commodity; the money is in the layer around it.** Open-weight models (DeepSeek-class, at 1/30–1/100th the price) set a permanent price floor on plain inference. The margin you keep comes from what you build *on top* — smart routing, checking the work, domain context. Price only the model and you have no lasting pricing power.
5. **Complexity and opacity destroy trust and sales velocity.** Hidden limits, seat cliffs, opaque credit burn, bill shock → freezes, renegotiations, churn. Simple, transparent, predictable-with-clear-overage beats clever.
6. **Negative unit economics are temporary subsidies.** Capital is currently funding deep negative margins. When conviction on payback weakens, only products with **positive contribution margin after full real cost** survive. "Grow into margins" is a dangerous delusion.

## THE TRAP

You will copy SaaS pricing and be wrong within six months. The bias is **inherited mental models** — every product you know charges per seat, so you will too. But per-seat charges your most expensive user the same as your cheapest, and in AI those differ by 10-100×. Flat-rate subsidizes power users until the margin bleeds out; pure per-token kills adoption because users feel taxed for thinking; outcome pricing only works where the outcome is unambiguous *and* you can measure it. There is no safe default — the model has to match your actual usage distribution and the budget you displace.

## KEY TERMS (plain, industry-standard)

- **Value metric** — the unit you charge for: a seat, a token, a credit, an agent-run, or an outcome. The most consequential choice.
- **The P90/P99 user** — the 90th/99th-percentile user by cost. Price against them, not the average; the average is irrelevant to survival.
- **Software budget vs salary budget** — the budget your value comes from. Software is a low single-digit % of revenue; salary is the loaded cost of the person you replace — ~10× larger.
- **Applied / harness layer** — everything above the raw model call (routing, verification, context compression, caching) — where margin is protected against the open-weights floor.
- **Default-FAIL measurement** — an outcome counts as success only if it provably passed an auditable, shared definition; the default is failure until proven (mirrors the harness `feature_list.json passes=false` pattern).
- **Contribution margin floor** — revenue minus *full* variable cost (harness multiplier, regenerations, support) at P90. If negative at expected scale, the pricing is a subsidy.
- **Spend visibility / token shock** — real-time cost instrumentation + soft/hard limits. Token prices fell ~67% in 2025 yet many bills *rose* — from missing routing and runaway agents, not model price.
- **Pricing transition arc ("SaaSpocalypse")** — per-seat → tiered → outcome → abstracted-value → services-as-software.
- **Services-as-Software** — the customer pays for the work done, like an outsourced service, not a license. Foundation Capital's default B2B-AI frame for 2026.

## WHAT THIS SKILL CONSUMES & PRODUCES

Pricing sits between the cost side and the go-to-market side. Name the handoffs before you start.

**Consumes (inputs):**
- **Cost per successful outcome at P90/P99** — from `cost-model`, *after* the harness multiplier, regenerations, tool calls, and failed trajectories. If you cannot get this number, stop and measure it first.
- **Usage distribution** — P10/P50/P90/P99 requests and cost per user, from 30+ days of instrumentation.
- **The routing strategy + spend instrumentation design** — from `cost-model` / the harness: how requests route by complexity, and whether real-time spend tracking exists.
- **Competitive pricing** — what the alternative charges and how it breaks, from `competitive-map`.
- **Which budget the buyer pays from** — software or salary (Step 0).
- **Segment + architecture** — B2B API / SaaS / B2C / platform, and Assist / Copilot / Agent / Autonomous, from `strategy-canvas`.

**Produces (outputs):**
- **The pricing decision** = value metric × pricing model × packaging, with the transition arc planned.
- **The spend-control design** → ships *with* the pricing: the spend dashboard, soft/hard limits, and approval gates (survival infrastructure, not a follow-up).
- **The launch motion** → `adoption-launch`: bundle = feature update; add-on = new SKU; standalone = full GTM.
- **The margin target + margin-floor result** → back to `cost-model`.
- **The pricing-as-strategy narrative** → `stakeholder-communications` / the board.

## STEP 0 — WHICH BUDGET ARE YOU BILLING? (THE CEILING)

Before any pricing mechanic, answer this — it sets how *high* you can charge. A tool that is just more software is paid from the **software budget** (capped by IT-procurement norms). A tool that does the work of a paid expert is paid from the **salary budget** — the loaded cost of the person plus mistakes avoided — roughly ten times larger.

This is the real reason outcome and value pricing command a premium: a judgment outcome crosses into the salary budget. It is also the agentic-era reframe of the per-seat death — an agent isn't a seat, it does a person's job, so its pricing *migrates* to the salary budget. **When wrong:** the salary ceiling only holds where you genuinely replace expert labor. A record-lookup tool dressed as "judgment software" stays on the software budget, and the higher ceiling is a mirage that prices you out. *(Stanton, HBR, 27 May 2026; Agrawal, HBR, 5 Jun 2026.)*

## THE AGENTIC SHIFT — VALUE METRIC × BUDGET DECISION TREE

The deepest structural change of 2026: agents break the old math, and **better agents make per-seat worse** (they do multi-seat work, so you sell fewer seats as the product improves). Route by what the AI actually does:

| What the AI does | Value metric | Budget | Notes |
|---|---|---|---|
| **Assist / Copilot** (suggests, human acts) | Seat + AI add-on, or hybrid | Software (+ some labor) | Seat still viable — usage variance is bounded |
| **Agent** (multi-step work, human approves) | Credit pools designed around **agent-runs**, or outcome | Crossing into labor | Per-seat is actively anti-aligned here; price the run |
| **Autonomous labor** (replaces headcount) | **Services-as-software / pay-for-work** | Salary/labor | Bill the salary budget; the outcome *is* the product |

## THE SIX PRICING MODELS (2026)

Mapped across the 50 highest-valued AI companies. **Pure-play pricing is dying — nearly half run two or three at once.** Pick per product line, not per company.

| Model | Mechanism | Fits | How it breaks | Example |
|---|---|---|---|---|
| **1. Hybrid tiered subscription** | Tiers with rising limits + model access | Consumer AI; the default | Undisclosed limits → users feel gaslit hitting a wall | Claude Free→Pro $17→Max $100/$200 |
| **2. Usage-based / per-token** | Pay per unit of compute | B2B APIs, developers | Surprise bills; thin moat (inference fell ~78% in 2025) | Anthropic/OpenAI API |
| **3. Credit / token pools** | Flat sub buys a depleting credit pool | Multi-feature / agentic products | Trust revolt when a predictable plan turns variable | Cursor (the $7,225 invoice) |
| **4. Outcome-based** | Pay per successful outcome | Clean, measurable, Default-FAIL outcomes | Revenue drops on a bad model week; needs measurement infra | Intercom Fin $0.99/resolution |
| **5. Seat-based + AI add-on** | Per-seat base, AI in a premium tier | Established SaaS adding Assist features | Heaviest users pay the same as lightest | Notion, GitHub Copilot, Harvey |
| **6. Freemium / reverse trial** | Give AI away to build habit | PLG, consumer scale | Brutal burn; <2-3% conversion = too generous | OpenAI (900M weekly), Perplexity, Duolingo (~8% of MAU paid ✅, well above the <2-3% failure line) |

**Preference order (long-term alignment, from the axioms):** Outcome / Services-as-Software **>** agent-run credits **>** hybrid with transparent overage **>** pure usage **>** pure seat (a temporary bridge only). Reverse trial beats a permanently crippled free tier.

## THE THREE INPUTS THAT PICK THE MODEL

1. **Cost structure.** Tokens as a % of *gross margin* (not revenue), at P90. >50% → usage or outcome mandatory; 20-50% → hybrid; <20% → seat survivable.
2. **Usage distribution.** P90 ÷ P10 request ratio. Under ~2× → flat-rate works; over ~5× → flat-rate fails (coding copilots run ~32× median-to-P99). Gini > 0.6 = flat-rate is risky.
3. **Competitive landscape.** No competitor → optimize margin. Competitor on per-seat → win on fairer usage-based. Competitor on per-token → match unless quality justifies a premium. Derive tiers from *your* usage data, never off a competitor's page.

## APPLIED-LAYER / ROUTING AS PRICING POWER

Pure model pass-through has no moat: open-weights set a permanent price floor, so a product that only marks up inference gets squeezed to zero. **Margin and pricing power now live in the applied/harness layer** — routing by complexity (studies show ~8× cost differences for the same output quality), verification loops, context compression, batching, and caching. This is the tight link to `harness-operating-model` and `cost-model`: the harness efficiency you build *is* the margin you protect. Under-invest here and every pricing model in this skill fails against a cheaper open-weights competitor.

## THE PRICING TRANSITION ARC — STAGE-GATED, AND WATCH THE SUBSIDY

Per-seat dies because AI costs are wildly uneven across users. The response is a stage-aware arc:

- **Pre-PMF:** reverse trial + a generous hybrid. Optimize for habit and learning the usage distribution, not margin.
- **Growth:** credits + spend visibility + soft limits. Add tiered caps *before* per-seat fails — proactively, not in crisis.
- **Leadership:** committed spend / outcome / services-as-software. Bill the salary budget.

Two rules decide whether a transition costs a quarter or a customer. **Price for the actual usage profile, not the headline** (Klarna priced for "AI replaces 853 FTEs"; reality was ~65% AI / 35% human, and both sides renegotiated). **Start before per-seat fails** (Cursor's reactive flip was public and the brand paid). **The capital warning:** many high-growth products run on subsidized unit economics — plan explicitly for the day capital reprices. "We'll grow into margins" is the trap.

**The subsidy is being withdrawn on published dates, and this is what a buyer sees from the other side of your price list.** Enterprise vendors absorbed GPU, inference and token cost as a customer-acquisition move, and the invoice language was "unmetered," "complimentary" or "included." Investors want the companies powering the transformation profitable, so that is unwinding. The dated facts, tiered:

- Oracle includes its base model in the subscription and **charges by usage for premium models** ◆ vendor-disclosed.
- SAP is expected to follow the same split, free simple queries and paid premium features ⚠ reported, forward-looking, no source and no date.
- **Workday's shift has a date: 31 January 2027** ◆ disclosed, with a stated grace period ("will not charge overages for Application APIs while customers investigate and optimize their usage") explicitly designed to avoid slowing adoption. This is the best-sourced and only dated item of the three.

**The framing sentence to carry into any pricing conversation, in either direction:** deploying AI agents at scale *"structurally shifts resources from capacity it controls (employee wages) to capacity it rents (variable token consumption)."* Rented capacity reprices on the vendor's calendar. That is why a grace period, a cap and credit rollover are worth more to a buyer than a rate concession, and why offering them is a real differentiator rather than a giveaway.

**What this changes on your side of the table.** Your customer is now being told to model their elasticity, negotiate caps and treat your tokens as a headcount substitute. Three consequences:

- **Publish a unit-of-work definition** that holds for the contract term. The buyer's sharpest question is no longer your rate. It is how much work one unit buys.
- **Expect caps and credit rollover to become table stakes** in enterprise deals through 2027.
- **Remember what a dated repricing feels like on their side.** It lands as a step change on their budget, even when your own cost curve moved gradually.

*(Source: HBR, Garr, "How to Respond to the Coming AI Cost Shock," Aug 2026. **Note the disclosure quality, which is the batch benchmark:** the author runs an analyst firm whose consortium takes fees from more than twenty HR tech vendors including Workday, discloses it in-body at first mention naming the mechanism, and argues against the disclosed party's interest by telling buyers to negotiate caps. Every dollar figure in that article derives from **the author's own illustrative one-cent-per-unit rate**, stated openly by her and not attributed to any vendor; do not carry those dollar figures without that sentence attached. Cost-side modelling lives in `rtp-cost-model` section 4B. Ledger patterns N and H.)*

## RENEWAL DEFAULTS: read the market, do not copy the competitor

**Auto-renew is not a best practice. It is a bet on what kind of market you are in**, and the two axes are both observable rather than guessed.

**Axis 1: market composition, measured by period-over-period repurchase rate.**

| Repurchase rate | Market type | What it implies |
|---|---|---|
| **above 70 to 80%** | **inertial**: subscribers who like the product retain themselves | **auto-cancel is likely optimal.** Contractual friction is unnecessary and actively suppresses acquisition and goodwill |
| **below 50%** | **variety-seeking**: subscribers rotate among options even when satisfied | **auto-renewal serves a real function**, carrying the subscriber through moments of restlessness |

**Axis 2: competitive position.** Above roughly 50% share, you are defending an installed base and auto-renewal protects it. Below that, the friction costs you more in acquisition than it returns in retention.

**The trap this closes:** copying the incumbent's renewal default when you are the challenger. **It is the one setting where the market leader's choice is actively wrong for you**, because the two axes point opposite directions at different share positions.

**For an AI product specifically**, the repurchase-rate read is complicated by usage variance. A subscriber who used the product heavily and one who barely opened it can both "renew," and only the first is real retention. Segment the rate by usage before you read it off the axis.

## DISCOUNTING IS SEGMENTATION, NOT GENEROSITY

**A discount is a hurdle that sorts customers by willingness to pay.** The discount's job is to be *inconvenient enough* that only the price-sensitive clear it, so you capture them without giving margin away to everyone.

Four sorting mechanisms, and each sorts on a different variable:

1. **Self-selected price sensitivity.** Coupons, codes, rebates, waiting, asking, identity markers like a student or local status. The friction is the filter.
2. **Purchase quantity.** Bundles and volume discounts, which work off diminishing marginal value.
3. **Acquisition moment.** Partnership discounts, cart-abandonment nudges, deadline pressure in B2B.
4. **Time and market value.** Dynamic pricing against time of day, season, weather, a competitor's move, a complementary event.

**The design test: does this discount require the customer to do something the full-price buyer would not bother doing?** If it does not, it is not a hurdle. **A discount with no friction is a price cut applied to everyone**, including every customer who would have paid full price.

**Where AI products break the pattern.** Usage-based pricing already sorts by intensity, so a volume discount can double-count the same segmentation and give margin away twice. Check which variable your meter is already sorting on before adding a hurdle that sorts on the same one.

*(Sources: the renewal matrix is Miller & Zhang, 2026, via HBR, May 2026 — ◆ the thresholds are the authors' own and are stated as bands rather than measured cut-points. The discounting structure is Rafi Mohammed in HBR, May 2026 — ⚠ the four mechanisms are reconstructed from the article's prose, which names no formal framework. The AI-specific cautions in both sections are this corpus's.)*

## THE PACKAGING DECISION — BUNDLE / ADD-ON / STANDALONE

Separate from the value metric: *do you charge for the AI separately at all?* Three signals (Broe's 44-incumbent study: 59% bundle, 23% add-on, 18% standalone).

- **Marginal cost at P90.** <5% of revenue → bundle is safe. 5-20% → bundle with fair-use, or hybrid. >20% → add-on or usage-based mandatory.
- **New value vs improvement.** Fill in "Before our AI, users could ___." "Do this manually/worse" = *improvement* → **bundle**. "Couldn't do this at all" = *new value* → **add-on**, or **standalone** only if it reaches a genuinely new buyer.
- **Separable WTP.** When sales mentions AI, does the prospect ask "what's the price for that?" (→ add-on) or "is that included?" (→ bundle). Standalone sold to the same buyer/cycle/logo is just an add-on with bad packaging.

**A worked example where all three signals point the same way.** Duolingo tried a standalone math app first, then folded it into one super app with language and music, for three stated reasons that map directly onto the tests above. Discoverability: with 2.2 million apps on the Apple App Store and 3 million on Google Play, even a known brand starts from zero in a new app. Friction: a new app means a new download, username, and login; an existing user opening a bundled feature is already signed in. Cost: gamification mechanics (leaderboards, streaks, experience points) get engineered once and reused, rather than rebuilt per subject, the practical form of the marginal-cost-at-P90 test above (◆, HBR Cold Call, "How Duolingo Aims to Diversify Beyond Language Learning," Apr 2025). The unresolved risk the case names itself: bundling means a new user's first impression of the whole product can come from its weakest line, not its strongest.

## THE QUALITY-COST-LATENCY TRIANGLE

Pick two; the third suffers. Flat-rate buys quality + latency but cost spirals. Per-token buys cost + latency but quality drops (users avoid hard questions). Outcome buys quality + cost but the user waits. Translate and instrument each vertex before pricing: **quality = acceptance rate** (% used as-is), **cost = price per outcome** (not per token), **latency = time to first useful token** (P50/P95, client-side). And watch the multiplier: **a regeneration doubles the real cost per outcome** — quality failures are cost failures.

## SPEND VISIBILITY + LIMITS — SURVIVAL INFRASTRUCTURE, NOT A FEATURE

This is the #1 operational failure destroying ROI and renewals right now. Token prices fell ~67% in 2025 yet enterprise bills *rose* — because of missing routing and runaway agents, not model price (one runaway agent loop reportedly burned ~$500M in a month; whole enterprise AI budgets gone in 3-4 months on unmetered API rates). Ship these *with* the pricing, never after:

- **Real-time spend instrumentation** — cost per user/feature/agent-run, visible to the buyer.
- **Soft limits (alert) + hard limits (block) + approval gates** for expensive agent runs.
- **No seat-threshold cliffs.** The hybrid failure mode: crossing a seat count (e.g. ~150) strips included usage and forces full API rates — a 3-3.5× overnight jump ($400K → $1.4M/yr in one real case). Design transparent staircases, not cliffs.

## DEFAULT-FAIL MEASUREMENT — THE HARD GATE FOR OUTCOME PRICING

Outcome pricing is theater without measurement. It is viable **only** when both parties share a **Default-FAIL, instrumented, auditable definition of success** — the outcome is a failure until it provably passed (mirrors the harness pattern). Intercom Fin works because "resolved" is defined (customer confirms, or no follow-up in 24h) and Intercom takes the LLM cost risk. Salesforce Agentforce charges $2 only on a full resolution with no human escalation and no negative feedback. **If you cannot measure the outcome cleanly, do not price on it** — flag `OPEN: outcome not yet measurable` and ship a different model until the instrumentation exists.

## THE MARGIN-DISCIPLINE MOVES + THE MANDATORY MARGIN FLOOR

- **The rate-limit staircase.** Want heavy usage, but throttle the top <5% toward the per-token API where cost is covered precisely (Anthropic's $17 → $100 → $200 + weekly limits). Undisclosed limits buy flexibility at the cost of trust — decide that trade knowingly.
- **The trust trap.** Never convert a predictable plan to variable without over-communicating. Cursor flipped flat-500 to credit pools and the CEO apologized twelve days later. Contrast: Snowflake/Twilio shipped metering + visibility *before* scaling usage pricing and hit 127-158% net revenue retention. **Visibility first.**
- **THE MARGIN FLOOR (do this before locking any pricing).** Compute contribution margin at P90 after the full harness multiplier, regenerations, support, and the open-weights floor. **If it's negative at expected scale, redesign the architecture or the pricing first — do not ship.** This enforces the sustainability axiom and stops the "grow into margins" delusion.

## THE COST SIDE LIVES IN `cost-model` — NOT HERE

Pricing *consumes* cost numbers; it does not compute them. The full mechanics — the harness multiplier (a Planner/Generator/Evaluator loop is 10-22× a single call), hidden costs, model routing, prompt caching (~90% off cached tokens), and batch APIs (~50% off) — live in `cost-model`. Pull one number before you price: **cost per successful outcome at P90, after regenerations and harness overhead.** If it isn't available, you have a measurement problem, not a pricing problem — fix it first.

## CASE LAW (2026) — STRESS-TEST EVERY DECISION AGAINST THESE

| Model | Got it right | Classic failure | The lesson |
|---|---|---|---|
| Hybrid tiered | Anthropic Free/Pro/Max staircase | Anthropic ~150-seat cliff ($400K→$1.4M) | Transparent staircase, no hidden cliffs |
| Usage / per-token | Snowflake / Twilio (visibility first) | Surprise bills, no routing (Uber-scale burn) | Ship spend visibility *before* scaling |
| Credit pools | Cursor (post-fix), Linear ($20 credits) | Cursor mid-2025 flip ($7,225 invoice) | Never flip predictable→variable without over-comms |
| Outcome-based | **Intercom Fin $0.99/res**, Salesforce Agentforce $2/res, Zendesk $1.50-2, Sierra | Any outcome without a Default-FAIL definition | Default-FAIL definition + take the cost risk |
| Seat + add-on | Harvey (~$1,200/seat, huge surplus) | Pure-seat Copilot (lost money per power user) | Seat is a temporary bridge for AI features |
| Agentic / hybrid | Microsoft Copilot Credits (seat + ~$0.01/credit) | Pure seat on multi-step agents | Price the agent-run; better agents kill seat math |

Test any proposal: *would it survive a Cursor-style power-user week, or an Anthropic 150-seat cliff?*

## WHERE YOU ARE — OUTPUT

```
## Pricing Decision: [Product / line]

Which budget: [software (~low single-digit % rev) | salary (~10×) — evidence you displace expert work]
What the AI does: [Assist | Copilot | Agent | Autonomous] → implied metric [seat | agent-run credit | outcome]
Value metric × model × packaging: [e.g., outcome × per-resolution × add-on]  (preference order respected?)
Chosen from: cost structure [tokens % of P90 margin] · usage spread [P90/P10] · competition
Transition arc: [stage: pre-PMF/growth/leadership] · next step = [the 1-2 quarter project]
Spend-control shipping with it: [real-time dashboard · soft/hard limits · approval gates · no seat cliff]
Outcome measurable? [Default-FAIL definition, or OPEN: not yet measurable → use model X meanwhile]
MARGIN FLOOR: gross margin at P90 after full harness+regen+support = ___%  [ship only if >0 at scale]
  at 10× usage: ___%   at 100×: ___%  (where it breaks)
Applied-layer margin move: [routing by complexity | caching | verification — vs the open-weights floor]
Trust guardrail: [comms plan if changing a predictable plan to variable]
```

Flag anything open as `OPEN: [decision] — [evidence that would settle it]`.

## WHEN WRONG

- **Pre-launch.** Pricing is premature until you know the usage distribution; ship, instrument 30 days, then price.
- **Fully custom / enterprise-negotiated** deals where standardized models don't apply.
- **Non-profit or subsidized research** contexts.
- **When pricing is already committed** — raising alienates, lowering is permanent. Price correctly the first time.

---

## GROUNDING, DELIVERABLE, TRADE-OFFS & CONCLUSION

Before starting, follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) Section 1 grounding questions (who is the customer, what problem, YES/NO scope) and confirm output format (Word / deck / inline; default Word). Close with the Trade-Off Ledger (Section 3) and the Conclusion Protocol (Section 5): state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action. If the decision hands off to `adoption-launch` or `cost-model`, generate the markdown handoff.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual — the six-model matrix (cost transparency × customer alignment, segment fit annotated) or the pricing transition arc with the trigger for each stage. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
