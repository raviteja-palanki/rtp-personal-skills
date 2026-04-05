---
name: rtp-token-economics
version: "2.0"
description: "Pricing for per-token cost structure (flat-rate, per-token, outcome, seat, hybrid). Tradeoff: optimize 2 of 3 (quality, cost, latency). Use when: new products, pricing changes, scaling, unit economics at 10x. Triggers: 'pricing for AI', 'token economics', 'how to price', 'usage-based vs flat-rate'"
imports: [stress-test, falsification]
---

# Token Economics

## DEPTH DECISION

**Go deep if:** You're designing pricing for a new AI product, scaling to 10x+ usage, or modeling unit economics at scale.

**Skim to diagnostic questions if:** You want to audit current pricing sustainability.

**Skip if:** Pre-launch or pricing is externally mandated (e.g., enterprise contracts, regulated pricing).

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

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will copy SaaS pricing and be wrong within six months. The bias is **inherited mental models** — every product you know charges per seat, so you will too.

But AI's cost structure is fundamentally different. Marginal cost is per-token, not per-user. A user writing a 10,000-token prompt costs you 10x more than one writing 1,000 tokens. SaaS ignores this because marginal cost of adding one more user is near-zero. AI can't.

Flat-rate pricing subsidizes power users exponentially. Per-token pricing kills adoption through transparency. Outcome pricing only works for high-value discrete results. You pick wrong and either burn margin or alienate customers. The trick: pick a model that matches your usage distribution and competitive landscape.

## THE PROCESS

Three dimensions. Find the intersection.

**Dimension 1: Cost Structure**

Calculate: (tokens/request) × (requests/user/month) × (token price).

Then assess:
- **Tokens % of total cost:** >50% = usage-based mandatory; 20-50% = hybrid; <20% = seat-based possible
- **Behavior of costs at scale:** Fixed (infra) vs. linear (tokens) vs. super-linear (hallucination correction, retrieval)
- **Margin at 10x usage:** Model it. If margin stays positive, pricing is sustainable.

*Think through:* What portion of your per-customer cost comes from model inference tokens vs. infrastructure?

*Low end:* Tokens are 5-10% of cost. Mostly server/infrastructure. (Vertical SaaS with light AI features.)

*Mid range:* Tokens are 30-50% of cost. Significant but not dominant. (Hybrid product with AI as a major feature.)

*High end:* Tokens are >70% of cost. Tokens are the business. (Pure AI service, per-request pricing.)

*Red flag:* You don't know this number. If you can't calculate (avg tokens per request) × (requests per customer) × (token rate), stop and measure it first.

*Sharpen it:* For your top 3 customer segments, what's the token cost as a % of gross margin? (Not revenue — margin.)

**Dimension 2: Usage Distribution**

Ask: How much variation is there in customer usage?

- **Tight (90% within 2x of median):** Flat-rate works (e.g., customer support, 100-300 tickets/agent/day)
- **Loose (users vary 10x-100x):** Per-token or hybrid required (e.g., research analysis, light to power users)

Find this by: 10th percentile usage vs. 90th percentile. If ratio >5x, flat-rate fails.

*Think through:* What's the actual spread of usage across your customer base?

*Low end:* 90th percentile is 2-3x the 10th percentile. Usage is tight. Most customers behave similarly.

*Mid range:* 90th percentile is 5-10x the 10th percentile. Wide variation. Heavy users exist but are minority.

*High end:* 90th percentile is 20x+ the 10th percentile. Extreme outliers. Power users are fundamentally different product.

*Red flag:* You haven't measured this yet. Assumption-based pricing fails. Collect 2-4 weeks of actual usage data.

*Sharpen it:* What's your Gini coefficient for usage? (0 = everyone uses equally, 1 = one user consumes everything.) If >0.6, flat-rate is risky.

**Dimension 3: Competitive Landscape**

- No competitors → You set standard (optimize for margin)
- Competitors use per-seat → You can use usage-based if better
- Competitors use per-token → Match unless quality justifies premium
- Mixed → Copy what customers expect (usually hybrid)

*Think through:* What are customers already paying for equivalent solutions?

*Low end:* No direct competitors. Pricing is greenfield — optimize for margin and adoption curve.

*Mid range:* 1-2 established competitors with known pricing. You need to match or justify a premium.

*High end:* >3 competitors with transparent pricing. Margins are compressed. Differentiate on quality or bundle.

*Red flag:* You don't know what competitors charge. Competitive pricing research is non-negotiable.

*Sharpen it:* For each competitor, what % of revenue comes from power users (top 20%)? Does their pricing model capture that?

**The Quality-Cost-Latency Triangle:**

```
        QUALITY
        /      \
       /        \
      /          \
   COST -------- LATENCY
```

Pick any two; the third suffers:
- Flat-rate: Quality + Latency (unlimited, no guilt) but Cost spirals
- Per-token: Cost + Latency (no request limits) but Quality drops (token guilt)
- Outcome: Quality + Cost (value capture) but Latency (user waits for perfect)
- Seat: Cost + Latency (predictable) but Quality (hoard seats, don't think deeply)
- Hybrid: Balanced, but Complexity (confusion about thresholds)

**The trap:** Optimizing for cost control destroys quality perception. Users stop asking complex questions.

### The Triangle in Customer Terms

The Quality-Cost-Latency triangle is only actionable if you translate each dimension into what customers actually observe — and instrument each vertex so you can actually measure it.

| Abstract Dimension | What Customers See | What You Measure | How You Instrument It |
|---|---|---|---|
| Quality | Acceptance rate — did they use the output as-is? | % of outputs accepted without edit | Track "accept" vs "edit" vs "regenerate" events per output. Minimum sample: 500 interactions before drawing conclusions. |
| Quality (failure) | Regenerations — they asked again | Regenerate clicks per session | Log every regeneration event with session ID, prompt hash, and output hash. Compute regeneration rate = regenerations ÷ total outputs. |
| Cost | Price per outcome — not per token | (Tokens × rate) ÷ tasks completed | Instrument cost per API call at the gateway. Aggregate by user, feature, and outcome (not just raw tokens). Daily cost dashboard: total spend ÷ completed tasks. |
| Latency | Time to first useful token | P50/P95 time-to-first-token | Measure client-side (not server-side). Use real user monitoring, not synthetic tests. Track TTFT separately from total completion time. |

**Instrumentation checklist before you set pricing:**
1. Are you logging cost per outcome (not just per API call)?
2. Can you segment cost by feature, user tier, and time period?
3. Do you have regeneration rate instrumented? (This is your quality-cost multiplier.)
4. Is latency measured client-side at P50/P95? (Server-side latency hides network overhead.)

**The hidden cost of quality failures:**

If a user rejects an output and regenerates, the actual cost per outcome doubles. If they regenerate twice, it triples. Quality failures are cost multipliers — not just UX problems.

**The real formula:**

`Cost per outcome = (avg tokens × rate × avg regenerations per outcome) + (operator overhead per task)`

A 90%-quality model that requires 1.1 regenerations per outcome costs the same as an 85%-quality model that requires 1.3 regenerations — but has very different unit economics at scale.

**Triangle instrumentation dashboard (minimum viable):**
```
┌──────────────────────────────────────────────────────────┐
│  QUALITY         │  COST              │  LATENCY          │
│  Acceptance: 87% │  $/outcome: $0.04  │  TTFT P50: 1.2s   │
│  Regen rate: 1.15│  $/user/mo: $3.20  │  TTFT P95: 3.8s   │
│  Trend: ↑2%/wk   │  Trend: ↓5%/wk     │  Trend: stable    │
└──────────────────────────────────────────────────────────┘
```

## Five Pricing Models

**1. Flat-Rate** ($X/month, unlimited)
- Works: Tight usage distribution (<2x variation)
- Fails: Power users subsidize light users exponentially
- Example: Support routing, 100-300 tickets/agent/day

**2. Per-Token** ($X per 1M tokens)
- Works: Transparent, variable usage, developers expect it
- Fails: Adoption friction, quality guilt (users avoid hard questions), price wars
- Example: OpenAI API, developer tools

**3. Per-Outcome** ($X per request, regardless of tokens)
- Works: High-value discrete results (medical diagnosis, legal advice)
- Fails: Low-value commodity tasks, hidden usage (logging, testing)
- Example: Medical diagnosis, legal research

**4. Seat-Based** ($X per user/month)
- Works: Predictable headcount, team collaboration, sales simplicity
- Fails: Uneven per-user usage, automation scales beyond "users"
- Example: Slack, predictable team tools

**5. Hybrid** (Seat + token overage, or base + outcome overage)
- Works: Predictable base + unpredictable spikes
- Fails: Complexity, threshold confusion, customer manipulation
- Example: Anthropic, Datadog (base + metered)

## Advanced: Batch vs. Real-Time Pricing

Anthropic, OpenAI, and others are introducing batch APIs with 50% discount. Think about when to use each:

**Real-time (standard API):** Immediate response. Full price. Use when: user waiting for result, <2s latency required, interactive workflows.

**Batch (async API):** 6-24 hour turnaround, 50% discount. Use when: analysis jobs, report generation, bulk processing, model evals, anything non-urgent.

**Strategy: Hybrid pricing.** Offer both. Force users to choose:
- Real-time query = full price
- Batch request = half price, 12-hour SLA

Many users will choose batch and your margin improves. But be careful: if 90% of usage shifts to batch, you've halved revenue.

**Token budget design:** For each feature, calculate "token budget per user per month." If a user hits their budget, what happens?
- Throttle (slow down responses)
- Block (no more requests)
- Upsell (offer higher tier)
- Warn (notify user they're approaching limit)

Most consumer products should throttle (preserve experience). Enterprise should warn (preserve relationship). Make it explicit.

## Cached Prompt Economics

Newer models support prompt caching (cache the system prompt, retrieve context, etc.). Cached tokens cost 10-25% of normal tokens.

**Architecture change:**
- Traditional: "System prompt + new user query" each time. Cost: 100% × tokens.
- Cached: Cache system prompt, retrieve once. Cost: 100% × first_call + 10% × subsequent_calls.

**ROI calculation:** If user makes 10+ requests, caching saves ~45% on prompt tokens. But you need 2-4 weeks to implement caching infrastructure.

**When to invest:** If average user makes 20+ requests/month. If <5 requests/month, skip caching.

**90% Discount on Cached Tokens:** Anthropic offers 90% discount on cached prompt tokens. Design context architecture to maximize cache hits: separate static system prompt (cacheable) from dynamic user context (not cacheable). This can cut inference costs 40-70% at scale. Track cache hit rate as a product metric.

## Harness Cost: The Multiplier Nobody Budgets For

Single model call: 1 unit of cost.
Multi-agent harness (Planner + Generator + Evaluator): 10–22× that unit.

**Why the multiplier is so high:**

- **Planner call:** Reads the full context, decides which tools to invoke, produces a structured plan. Cost: 1–3× the base call.
- **Generator call(s):** One or more calls executing the plan steps. If 3 parallel steps: 3× the base call each.
- **Evaluator call:** Scores the output for correctness/safety. Another full-context call. Cost: 1–2× base.
- **Retry loop:** If evaluator rejects, the generator re-runs. Each retry adds another full cycle.

**What this means in practice:**

If your base model call costs $0.01:
- Single call: $0.01
- Planner + Generator + Evaluator (1 retry allowed): $0.05–$0.10
- 3-parallel-agent harness with evaluator: $0.15–$0.22

**The budget test:** Before architecting a harness, multiply your expected call volume by 15× and ask: "Is the product worth that cost per outcome?"

*Think through:* What's your orchestration overhead as a multiple of a single model call?

*Low end:* Single-agent or simple routing. 1–2× base cost. (Direct API call, maybe one fallback.)

*Mid range:* Multi-step with evaluation. 5–10× base cost. (Planner → Generator → Light evaluator, 1 retry.)

*High end:* Complex multi-agent with retries and fallbacks. 15–25× base cost. (3+ agents, heavy evaluation, multiple retry loops.)

*Red flag:* You're designing a harness without knowing the cost multiplier. Measure it on your test set first.

*Sharpen it:* What's your actual cost per successful outcome (not per token)? At your expected monthly volume, what's the total cost per customer?

## Hidden Costs

When modeling unit economics, budget for:

| Cost | Mitigation |
|------|-----------|
| **Hallucination correction** (user reports bad answers, you fix) | Cap inference cost per request; add guardrails |
| **Retrieval cost** (RAG = embeddings + vector DB) | Amortize across requests; separate RAG pricing |
| **Fine-tuning** (if offered; 100k-examples = 50k API calls) | Price separately; margin only on large customers |
| **Support escalation** (harder problems need help) | Outcome-based pricing captures this |
| **Cache invalidation** (queries re-run; cached cheaper) | Adjust pricing for cache hits vs. misses |
| **Model routing** (query small model, fallback to large) | Track cost of fallbacks; may invalidate ROI |

## Model Routing Economics

When you have access to multiple models (GPT-4, Claude, Llama), which should you call for each request?

**Intelligent routing:** Route simple questions to cheap models (Llama-3 = $0.0001/call), complex questions to expensive models (Claude = $0.001/call).

**Challenge:** Deciding "simple vs. complex" costs tokens (run classifier = overhead).

**Math:** If 70% of queries are simple (10-token overhead to classify, savings of 10x on model cost), routing ROI is positive. If only 10% are simple, routing overhead kills savings.

**Strategy:** Only implement intelligent routing if:
1. You have >10M requests/month (small scale, overhead kills ROI)
2. Your cost distribution is wide (cheap + expensive models available)
3. You can classify requests without extra inference (use heuristics, user metadata)

Most startups shouldn't route. Just pick the best model and keep it simple.

**Token budget per feature:** Assign budget:
- Search = 500 tokens/request max
- Write assist = 2000 tokens max
- Analysis = unlimited (batch API)

Enforce via API gateway. Track overage. If feature consistently exceeds budget, either raise budget or reduce scope.

## Tiered Pricing: The Power User Subsidy Problem

Flat-rate pricing ($20/month unlimited) assumes usage is roughly equal. For AI products, it rarely is.

**The usage distribution reality:**

- Bottom 60% of users: 10–50 requests/month. Revenue: $20. Cost: $0.50–$2.
- Middle 30% of users: 50–200 requests/month. Revenue: $20. Cost: $2–$8.
- Top 10% of users: 500–2,000+ requests/month. Revenue: $20. Cost: $20–$80.

**The math:** If 10% of users generate 50× the average cost, flat-rate pricing means your profitable users subsidize your unprofitable ones — but you don't know which is which until you've run the product for 90 days.

### Step 1: Instrument Before Pricing

Run at least 30 days of usage data before setting tiers. You need:
- Per-user request count distribution (P10, P50, P90, P95, P99)
- Per-user cost distribution (same percentiles)
- Feature-level cost breakdown (which features drive the power-user spike?)
- Session patterns (are power users doing more requests or more expensive requests?)

### Step 2: Define Tiers From Customer Behavior, Not Round Numbers

Don't pick tiers from a competitor's pricing page. Derive them from your usage data:

| Tier | Usage Percentile | Behavior Pattern | Revenue Goal | Churn Risk |
|---|---|---|---|---|
| **Light** (Tier 1) | P0–P60 | 10–50 requests/mo. Casual, exploratory. Low habit formation. | Cover direct cost (cost-neutral or slight margin) | High — 40–60% monthly churn if no habit loop |
| **Standard** (Tier 2) | P60–P90 | 50–200 requests/mo. Daily users, moderate complexity. Core workflow integration. | Cost + 40–60% gross margin | Medium — 15–25% monthly churn. Stickier due to workflow integration |
| **Power** (Tier 3) | P90+ | 500–2,000+ requests/mo. Heavy automation, complex queries, multi-step workflows. | Primary margin driver — 60–80% gross margin | Low — 5–10% monthly churn. Deeply embedded in workflows. But concentrated risk if they leave. |

### Step 3: Price Each Tier to Its Economics

**The tiered design heuristic:** Tier 1 covers your direct cost. Tier 2 covers cost + margin. Tier 3 is where you make your gross margin.

**Pricing sanity check per tier:**
```
Tier 1: Price ≥ (avg cost per user in P0-P60 segment) × 1.2
Tier 2: Price ≥ (avg cost per user in P60-P90 segment) × 1.6
Tier 3: Price ≥ (avg cost per user in P90+ segment) × 1.3
        BUT must also deliver >60% gross margin
```

If your pricing doesn't have a tier where you make real margin, you have a cost model problem, not a pricing problem.

### Step 4: Account for Harness Cost in Tier Economics

If your product uses multi-agent orchestration (see Harness Cost section above), the harness multiplier changes tier economics:

| Tier | Without Harness | With 10× Harness | Implication |
|---|---|---|---|
| Light | Cost: $1.50/mo, Price: $10 → 85% margin | Cost: $15/mo, Price: $10 → **−50% margin** | Harness kills light-tier profitability. Gate harness features behind Tier 2+. |
| Standard | Cost: $5/mo, Price: $25 → 80% margin | Cost: $50/mo, Price: $25 → **−100% margin** | Must increase price or restrict harness usage. |
| Power | Cost: $40/mo, Price: $99 → 60% margin | Cost: $400/mo, Price: $99 → **−300% margin** | Power users destroy economics. Usage caps or outcome-based pricing required. |

**The rule:** If you use orchestration, flat-rate pricing is almost certainly wrong. Move to hybrid (seat + usage overage) or outcome-based pricing for any feature that triggers multi-agent flows.

### Step 5: Build Credit Systems With Decay

Monthly credits that don't roll over create consistent revenue. They also surface power users (who hit limits and upgrade).

**Revenue attribution by tier (track monthly):**
```
Tier 1 revenue: $_______ (target: 20-30% of total)
Tier 2 revenue: $_______ (target: 30-40% of total)
Tier 3 revenue: $_______ (target: 30-40% of total)
Overage revenue: $_______ (target: 5-10% of total)
```

If >50% of revenue comes from Tier 1, scaling is painful — you need 10 tier-1 customers to offset one tier-3 customer. If >50% comes from Tier 3, healthy unit economics but concentrated churn risk.

*Think through:* What's the revenue distribution across your customer tiers?

*Low end:* 60%+ of revenue from Tier 1 (light users). Scaling is painful — you need 10 tier-1 customers to offset one tier-3 customer.

*Mid range:* Revenue roughly balanced across tiers. 30-40% from tier 1, 30-40% from tier 2, 20-30% from tier 3.

*High end:* >50% of revenue from Tier 3 (power users). Concentrated risk but healthy unit economics.

*Red flag:* You don't know which tier your revenue comes from. Install usage instrumentation before launch.

*Sharpen it:* For each tier, what's the actual cost per customer after 6 months? Is margin positive for all tiers, including harness overhead?

## REALITY CHECK

- **Failure mode:** Prices viable at 10x but not 100x. Model 10x scenarios.
- **Pricing changes are sticky.** Price correctly the first time — raising alienates, lowering is permanent.
- **Transparency builds trust** despite sticker shock.

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., build-or-buy, cost-model), generate the markdown handoff file as well.

## QUALITY GATE

- [ ] Cost structure calculated and classified (tokens %, fixed %, variable %)
- [ ] Usage distribution analyzed (10th/50th/90th percentile; Gini if possible)
- [ ] Competitive landscape mapped (what are alternatives charging?)
- [ ] Pricing model selected with explicit tradeoff: which of (quality, cost, latency) sacrificed?
- [ ] 10x scenario modeled (does margin stay positive at 10x usage?)
- [ ] 100x scenario tested (at what scale does the model break?)
- [ ] Hidden costs enumerated and budgeted
- [ ] Customer segment pricing audit (does the model fair-price light users AND capture power users?)

## WHEN WRONG

- Pre-launch exploration where pricing is premature
- Fully custom/enterprise where standardized models don't apply
- Non-profit or subsidized research models
- When pricing is committed and change breaks trust

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
