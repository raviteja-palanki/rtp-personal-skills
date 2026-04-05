# Cost Model — Concept Guide

## FIRST PRINCIPLES

Traditional software scales linearly. A database query that costs 10ms at 1,000 QPS costs 10ms at 10,000 QPS (horizontal scaling is transparent). The economics are predictable: add compute, add cost proportionally.

AI products scale differently. They degrade. Context windows grow as the corpus expands. Token usage per query increases as users learn to ask more sophisticated questions. Retry rates increase under load because inference latency goes up. Caching hit rates drop because the query distribution becomes more uniform. The marginal cost of serving the 10,000th user is 3-5x the marginal cost of serving the 1,000th.

The atomic insight: **AI unit economics are non-linear. The cost model you build at pilot stage is obsolete by the time you've shipped.**

## DUAL DEFINITION

**Business definition:** A cost model for an AI feature is a detailed unit economics calculation that predicts the cost to serve one user action (or session, or day) across the full range of anticipated scale, from launch to 10x growth. It's used to determine feature sustainability, pricing, and resource allocation. An AI feature without a unit cost model is a liability masquerading as a feature.

**Technical definition:** A structured calculation of token volume per user action (including overhead, retries, context, and evaluation infrastructure), multiplied by token prices (adjusted for scale discounts and inflation), stress-tested against user behavior models at 10x scale, with sensitivity analysis on key variables and identification of cost levers for optimization.

## THE TRAP (Expanded)

**The Pilot Mirage.** You ship to 500 pilot users. Token cost is $2,000/month. You extrapolate: at 15,000 users, cost will be $60,000/month. But the 15,000-user reality hits you at $150,000/month — 2.5x your estimate — because:

1. Users learn to ask more sophisticated questions as they become comfortable. Average tokens per query increase 30%.
2. The corpus grows to support more use cases. Context windows expand 2x.
3. Caching becomes less effective as queries diversify. Hit rate drops from 40% to 20%.
4. Retry rates increase under load. What was 5% becomes 15%.
5. Your eval infrastructure, which was negligible at pilot, is now substantial.

You've committed engineering resources, made pricing commitments to customers, promised board members unit economics that don't exist. Too late to redesign.

**The Overhead Blindness.** Engineers estimate token cost as: (tokens per call) × (cost per token). This is the direct cost, roughly 30% of total cost. They miss:

- Vector DB queries and re-ranking (adds 20-40% to inference cost)
- Error handling and retries (adds 5-15%)
- Context padding and safety margins (adds 10-20%)
- Logging, monitoring, evaluation infrastructure (adds 15-25%)
- Provider price increases and volume unpredictability (adds 20-30%)

Direct cost: $0.01. Total cost: $0.03-0.05. Build a product that assumes $0.01 and you're underfunded by 3-5x.

**The Leverage Blindness.** Teams accept negative unit economics under the assumption "we'll optimize later." This is mathematically wrong. If your feature costs $5 per user per month and you sell it for $10/month, adding 10x users adds $50M/month in losses. You don't optimize your way out of that. You change the model or kill the feature.

The only exception: strategic loss leaders where the cost is known, bounded, and subsidized by the business (e.g., free tier with CAC payback in a freemium model). Even then, the unit economics must be explicit.

## INTELLECTUAL LINEAGE

- **Will Larson (Sequoia)** — "Sizing AI Features" and unit economics in AI product decisions.
- **Eugene Yan** — Production ML systems and the cost of infrastructure debt.
- **OpenAI's Pricing Evolution** — How model prices actually decrease, slowly, but never as fast as consumption increases.
- **SaaS Unit Economics** — The paradigm that no SaaS product survives if CAC payback > LTV. Apply this to AI: if token cost per user per year > revenue per user per year, the feature is DoA.
- **Amazon's 10x Cost Structure** — The insight that scaling reveals second-order effects. Build for 1x volume. Deploy at 10x and discover your assumptions were wrong.

## REAL-WORLD EXAMPLES

**Example 1: The Startup That Didn't Model.** An AI note-taking company launched with free transcription (speech-to-text + summarization). Unit cost estimated: $0.08/minute. Average user: 10 minutes/day = $0.80/month. They charged $10/month subscription.

At pilot (100 users): profitable. They scaled to 10,000 users and discovered:
- Users shared heavy files; top 10% uploaded 1-2 hours/day (10x average).
- Model provider raised prices 15%.
- Actual retry rate: 12% (modeled as 5%).
- Unaccounted infrastructure overhead: $0.03/minute.

Effective cost at scale: $0.15/minute. Top 10% of users alone cost $12+/month in tokens. **Result:** Feature was profitable for 70% of users, loss-making for 30%. They couldn't segment (free tier). They raised prices; half the user base left. **Lesson:** The cost model at 100 users was fiction. Stress testing at 10x would have shown the 10% of power users driving 50% of cost.

**Example 2: The Enterprise That Over-Engineered.** A financial services firm built an AI risk analyst feature. The core token cost was $0.12 per analysis. But they added:
- Human review layer (lawyer review on all outputs): +$5 labor cost
- Regulatory logging and audit trail: +$0.08
- Evaluation infrastructure to track model drift: +$0.15
- Compliance test suite (run nightly): +$0.10

Total cost per analysis: $5.45. They charged enterprise customers $10/analysis, assuming high volume. But regulators required manual review, so the human was the bottleneck. They could scale AI cost-free; the feature was gated by human capacity (200 reviews/month per lawyer, 5 lawyers = 1,000/month max throughput).

They built AI infrastructure for 10,000 analyses/month but could only serve 1,000. They over-allocated engineering budget to the AI side, under-allocated to building the human-in-the-loop workflow. A cost model that separated AI cost from operational cost would have surfaced this.

**Example 3: The Cache Assumption.** An AI search startup modeled cache savings: at 500 users, cache hit rate was 60%, reducing cost from $0.003/query to $0.001/query.

At 50,000 users (100x), cache hit rate collapsed to 8% because:
- **Long-tail queries:** Each user asks unique questions; limited repetition across 50K users.
- **Diverse use cases:** Different industries, different query patterns, zero overlap.
- **Variation in phrasing:** "How do I fix a bug?" vs. "How to debug?" vs. "What's causing this error?" — all miss cache despite semantic similarity.

Cost per query jumped: $0.001 × (1 - 0.60 cache benefit) = $0.0004 at pilot → $0.003 × (1 - 0.08 cache benefit) = $0.00276 at scale. **Effective cost 7x higher.**

They'd sized infrastructure for the cached scenario. By the time they discovered the problem, they were over-provisioned and losing millions. **Lesson:** Cache hit rate is not a scaling assumption. It's a scaling risk. Stress-test it with diversified user distributions.

## FURTHER READING

- Will Larson, "Sizing AI Features" — Sequoia playbook for unit economics
- Eugene Yan, "Real-World ML: Lessons from Anthropic" — Production cost structure reality
- Byrne Hobart, "The Economic Structure of AI" — Long-form analysis of model pricing evolution
- Stripe's "Pricing as a Moat" — Tiering strategies to manage cost-sensitive features
