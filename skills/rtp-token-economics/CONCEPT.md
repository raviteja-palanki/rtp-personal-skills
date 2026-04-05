# Token Economics — Concept Guide

## FIRST PRINCIPLES

Traditional SaaS pricing is built on an assumption: marginal cost of one more user is zero (or near-zero). Whether Salesforce has 100,000 users or 1,000,000 users, the per-user cost of cloud infrastructure doesn't change proportionally. Their marginal cost is mostly fixed, with a small variable component.

AI products break this assumption. The cost of Claude serving 100,000 tokens is 100x the cost of serving 1,000 tokens. The cost is proportional to work done, not users. This single fact — that marginal cost is per-token, not per-user — shatters every pricing model SaaS invented.

The atomic insight: **Pricing an AI product is not about fairness to users; it's about preventing marginal cost from exceeding margin.** Get this wrong and you'll be profitable at 1,000 users and bankrupt at 10,000.

## DUAL DEFINITION

**Business definition:** The selection of a pricing model that aligns user willingness-to-pay with the AI service's cost structure (per-token or per-outcome), ensuring both user adoption and positive unit economics at scale.

**Technical definition:** A revenue model that maps the primary cost variable (tokens consumed or outcomes delivered) to a payment structure that captures value while remaining competitive, optimizing across adoption friction, margin sustainability, and quality perception.

## THE TRAP (Expanded)

**"We'll use a flat-rate subscription."** Heard from every first-time AI PM. They've built on SaaS pricing precedent, not AI cost structure. Day one: great for you (clear pricing, easy to forecast). Day 90: a power user (researcher, analyst, automation) uses 100x the tokens you predicted. Day 180: that one user is burning more margin than 100 normal users generate. You're forced to choose: cap the user (destroy UX) or redesign pricing (break customer contracts).

**"We'll use per-token pricing."** The opposite extreme. Transparent, fair, defensible. But every new user asks, "How much will this cost?" That friction kills adoption. Users avoid asking hard questions because each token has a visible cost. You end up competing on cost, not quality.

**"We'll use per-outcome pricing."** Only works if outcomes are discrete and valuable enough to justify the friction. Medical diagnosis, legal opinion, strategy consulting — great. Customer support classification, spell-check, content moderation — terrible. The cost can't be per-outcome; there are thousands per user per day.

**The meta-trap:** You'll optimize for the wrong dimension. You'll maximize revenue (charge more) and minimize adoption. You'll maximize adoption (charge less) and minimize margin. You'll try to balance both and end up with hybrid pricing so complex that users can't predict cost.

## COST STRUCTURE FUNDAMENTALS

### The Marginal Cost Curve

Traditional SaaS:
```
Marginal cost per user
        |
        |     _______________  (flat line)
        |    /
        |___/
        +----+----+----+----+ Users
         0   10k  20k  30k
```

AI products:
```
Marginal cost per token
        |
        |\
        | \
        |  \
        |   \____  (slight curve downward as model cost amortizes)
        |_________
        +----+----+----+----+ Tokens
         0   1M   10M  100M
```

The curve is different. For SaaS, cost is mostly fixed overhead. For AI, cost is proportional to usage.

### Break-Even Analysis

**Traditional SaaS:**
- Fixed cost: $100k/month (infrastructure, team)
- Marginal cost per user: $5/month (support, bandwidth)
- Price: $50/month per user
- Break-even: 100k/50-5 = 2500 users
- At 10x: 25,000 users, margin is the same %

**AI Product:**
- Fixed cost: $50k/month (team, infrastructure)
- Marginal cost per token: $0.000001 (token price from provider)
- But: average request = 2000 tokens (input + output) = $0.002/request
- At 1M requests/month: marginal cost = $2000/month
- If you charge $X per month flat-rate, you need to generate >$2000 from those users
- At 10x (10M requests/month): marginal cost = $20,000/month + fixed = $70k. If you're still charging the same $X per month, you're underwater

This is where AI pricing breaks SaaS thinking.

## PRICING MODELS IN THE QUALITY-COST-LATENCY SPACE

Every model makes implicit trade-offs:

### Flat-Rate Pricing
- **User experience:** "I have a budget of $X. I can use it however I want."
- **Quality outcome:** Users feel empowered to ask hard questions (no token guilt).
- **Business outcome:** Margin is strong at 10x users only if usage distribution is even.
- **Failure mode:** Power users game the system. One researcher using 100x average explodes your margin.

### Per-Token Pricing
- **User experience:** "This is going to cost me $0.02. Is it worth it?"
- **Quality outcome:** Users think twice before asking complex questions. Quality perception drops because users avoid hard problems.
- **Business outcome:** Margin is predictable. You know exactly what 1M tokens costs.
- **Failure mode:** Adoption is slow because cost is transparent and scary. Users compare to competitors token-by-token. Price war ensues.

### Per-Outcome Pricing
- **User experience:** "This diagnosis costs $50. Is it right?" (Can't predict cost in advance.)
- **Quality outcome:** Users are willing to invest in better outcomes. Quality perception is high.
- **Business outcome:** Margin is strong because you capture value. But total addressable market is small (high price = fewer buyers).
- **Failure mode:** Doesn't work for commodity tasks. You can't charge $50 per customer support classification.

### Seat-Based Pricing
- **User experience:** "My team of 5 costs $250/month." (Simple, predictable.)
- **Quality outcome:** Usage is hidden from users; they might over-use or under-use without realizing cost.
- **Business outcome:** Revenue is predictable. But margin depends on usage distribution. One power user per seat breaks economics.
- **Failure mode:** Doesn't scale to high usage. One user can consume as much as a team.

### Hybrid Pricing
- **User experience:** "Base plan is $X/month for 100k tokens, then $Y per 1M tokens above that."
- **Quality outcome:** Balanced. Most users stay in base plan (flat-rate benefit). Power users are captured by overage.
- **Business outcome:** Revenue is predictable (base) + variable (overage). Margin improves as power users adopt.
- **Failure mode:** Complexity. Users game the threshold. "Should I ask this question now or save it for next month?"

## THE REAL VARIABLE: USAGE DISTRIBUTION

The true variable that makes pricing work or fail is **how usage is distributed across your customer base.**

**Tight distribution (90% of users within 2x of mean):**
- Flat-rate pricing works. Everyone uses roughly the same amount.
- Example: Customer support routing. Average support agent handles 100-200 tickets/day. Range is 50-300. Tight distribution. Flat-rate works.

**Loose distribution (users vary 100x from min to max):**
- Per-token or hybrid pricing required. Flat-rate will be gamed by power users.
- Example: Research analysis. One user does daily analysis (500 tokens/day). Another does quarterly deep-dives (50k tokens/quarter). Hundred-fold variation. Per-token required.

**How do you know your distribution?**

1. **Model it.** Ask: what's the 10th percentile user, median, 90th percentile?
2. **Test it.** Launch with hypothetical pricing; see which customers self-select.
3. **Measure it.** Track actual usage for six months. Calculate Gini coefficient (measure of inequality).

If Gini > 0.4, your distribution is too loose for flat-rate pricing.

## INTELLECTUAL LINEAGE

- **Marc Andreessen, "Why Software is Eating the World"** — The foundational insight that software marginal cost is near-zero. AI breaks this.
- **Dan Ariely, "Predictably Irrational"** — Pricing psychology. Transparent pricing (per-token) feels scarier than hidden pricing (flat-rate) even if total cost is the same.
- **OpenAI's Pricing Model** — The canonical example of per-token pricing in AI. They chose transparency over adoption friction because marginal cost is unavoidable.
- **Anthropic's Approach** — Hybrid (custom contracts for large customers, per-token for small). Captures value from power users while remaining accessible to new users.

## REAL-WORLD EXAMPLE: Three Products, Three Models

### Customer Support Routing (Tight Distribution)
- Average support agent: 200 tickets/day
- Range: 100-400 tickets/day
- Token per ticket: ~500 tokens
- Distribution: Tight (3.5x max/min)
- **Pricing model: Flat-rate** ($X per agent per month)
- **Why:** Most agents are within 2x of each other. One agent doing 400 tickets/day isn't subsidizing the product; margin stays strong.
- **Cost check:** At 1M tokens/day, cost is $2/day. If 100 agents, at 200 tokens each = 200 agents × $2/day = $400/day = $12k/month. If you charge $X per agent, 100 agents × $X need to beat $12k/month. At $150/agent, you break even and scale profitably.

### Medical Diagnosis (High-Value, Discrete)
- One diagnosis call worth: $500 (if correct)
- Token cost: $2
- Margin available: $498 per call
- Distribution: Not applicable (each call is independent)
- **Pricing model: Per-outcome** ($50-200 per diagnosis, or subscription for hospitals)
- **Why:** The value of a single diagnosis is high. Users don't care if it costs $2 or $50 in tokens; they care if the diagnosis is right.
- **Cost check:** Even at $50 per call, you're capturing 10% of value created. Margin is 96%.

### Research Analysis (Loose Distribution, Variable)
- Light user: 50 requests/month, 500 tokens each = 25k tokens/month
- Power user: 1000 requests/month, 2000 tokens each = 2M tokens/month
- Ratio: 80x difference
- Distribution: Extremely loose
- **Pricing model: Per-token or hybrid**
- **Why:** Flat-rate doesn't work. If you charge $X/month for "unlimited analysis," the power user is subsidized 80x over. Hybrid captures value from both: base plan for light users ($100/month), then overage.
- **Cost check:** At $0.005 per 1k tokens, light user costs $0.125, power user costs $10. If you charge $100 base, light user margin is $99.875, power user margin is $90 + overages. Both are profitable, both feel fair.

## FURTHER READING

- OpenAI, "Pricing and models" documentation
- Anthropic, "Pricing and models" documentation
- Marc Andreessen, "Why Software is Eating the World"
- Your own spreadsheet modeling the 10x and 100x scenarios (most important)
