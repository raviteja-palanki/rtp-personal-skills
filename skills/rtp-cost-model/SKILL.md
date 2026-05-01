---
name: rtp-cost-model
description: "AI product unit economics: cost stack (inference, retrieval, storage, compute, human review), stress-test at 10x, identify cost levers and margin cliffs. Maps cost per successful outcome, 80/20 levers, margin cliff scale. Triggers: 'unit economics', 'AI cost model'"
imports: [stress-test, token-economics, product-pricing]
---

# Cost Model

## DEPTH DECISION

**Go deep** if: you're pricing an AI feature, doing go/no-go on a launch, or your margin is unclear at 10x scale. Read sections 1-6.

**Skim to KEY DIAGNOSTIC QUESTIONS** if: you have an existing cost model and want to pressure-test assumptions. The 8 questions will surface blind spots fast.

**Skip** if: the feature is a loss-leader by design, or you're in early prototype where unit economics are irrelevant.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will model inference cost in isolation. Reality: **inference is 20-30% of total cost.** The other 70% hides in retrieval (embedding + vector DB + re-ranking), storage, compute overhead, human review pipelines, and eval infrastructure.

You'll also assume costs scale linearly. They don't. Retrieval cost grows with corpus size. Eval cost grows with volume. Error correction compounds under load. Cache hit rates collapse as query diversity increases. By 10x scale, your $0.02-per-call assumption becomes $0.06-0.10. You'll have committed infrastructure before realizing margin is negative.

## THE PROCESS

### 1. Map Your Real Cost Stack

Don't start with tokens. Start with every system that touches your feature:

**Inference layer:** Model API calls (input + output tokens)
**Retrieval layer:** Vector embeddings (queries + documents), vector DB hosting, re-ranking models, hybrid search
**Storage layer:** Document storage, vector embeddings at scale, cache storage, logs
**Compute layer:** Orchestration, retries, timeouts, fallback routing, load balancing
**Human layer:** QA review, safety review, user feedback loops, annotation for improving retrieval
**Eval layer:** Daily evaluation runs, quality monitoring, drift detection, cost auditing

For each layer, ask: **At what scale does this become expensive?** Embedding costs are negligible at 1M documents but substantial at 100M.

### 2. Build the Cost Calculation: Real Numbers

Start with actual pricing. For a document search feature:

| Component | Volume | Unit Price | Monthly Cost | % of Total |
|-----------|--------|------------|--------------|------------|
| Query inference | 100K queries | $0.0218/call | $2,180 | 8% |
| Embedding (queries) | 100K queries | $0.00001/token × 100 avg tokens | $100 | <1% |
| Retrieval re-rank | 100K queries | $0.001/call | $100 | <1% |
| **Retrieval subtotal** | | | $2,380 | 9% |
| Storage (1M docs) | 1M × 500 tokens | $0.30/1M vector-months | $300 | 1% |
| Vector DB hosting | | | $800 | 3% |
| **Storage subtotal** | | | $1,100 | 4% |
| Eval infrastructure | Daily eval runs | $150/day | $4,500 | 17% |
| Human QA review | 500 samples/month | $15/sample | $7,500 | 28% |
| Infrastructure overhead | Orchestration, logging, monitoring | | $6,000 | 22% |
| **Total realistic cost** | | | **$26,880** | |

**Key insight:** Human review alone is 28% of cost. Inference is only 8%. This changes how you optimize.

### 3. Calculate Cost Per Successful Outcome (Not Per Call)

Inference cost per call is misleading. What matters is cost per user getting a useful answer.

- Query inference: $0.0218/call
- Retrieval quality issues force re-query: 15% fail rate
- Failed queries require human escalation: $5 per escalation
- **True cost per successful outcome:** $0.0218 × 1.15 + ($0.0218 × 0.15 × 5) = $0.041

If your feature has 20% failure rate (common for RAG), the math changes dramatically:
- Successful outcomes cost 1.25x more than the naive calculation
- You're paying full inference cost for failed attempts too
- This is invisible in simple per-call models

### 4. Model at 10x: The Real Degradation

When you go from 1,000 to 10,000 users, these change:

| Factor | Current | At 10x | Why |
|--------|---------|--------|-----|
| Tokens per query | 2,000 | 3,500 | Larger retrieved context, longer user query complexity |
| Retrieval latency | 300ms | 800ms | Slower vector DB as corpus grows 10x |
| Cache hit rate | 45% | 18% | Query diversity explodes; fewer repeats |
| Model routing: cheap model % | 60% | 40% | Hard queries increase; can't use cheap model for everything |
| Eval pipeline cost | $4.5K/mo | $45K/mo | 10x volume requires continuous monitoring |
| Human review volume | 500/mo | 2,000/mo | More failures at scale + safety requirements increase |
| Infrastructure cost | 1.5x baseline | 3-4x baseline | Multi-region, failover, caching layers |

**Effective cost per outcome at 10x:**
- Baseline: $0.041
- × 1.75 (larger context, slower retrieval)
- × 1.22 (worse cache hit)
- + Model routing premium: $0.008 (more expensive models needed)
- + Eval scaling: +$0.012
- × 1.15 (higher human review rate under quality pressure)
- **= $0.094 per successful outcome (2.3x baseline)**

### 5. Harness Cost Economics: Agent Architectures & ROI (Critical Decision Framework)

The complexity of your AI system has a 22x cost multiplier. Know when to pay it.

**Solo agent (single LLM call):**
- Cost: ~$0.01 per task (20 minute wall time)
- Example: "Summarize this document" = 1 API call
- Failure mode: Garbage in, garbage out. No recovery.
- When to use: Low-risk, simple classification, no stakes

**Single agent + eval pass (generation + validation):**
- Cost: ~$0.05 per task (30 minutes wall time)
- Example: Generate + check quality (hallucination filter, fact-check)
- Architecture: Generate → Safety model check → Deliver or escalate
- Failure mode: Caught and escalated. Quality gate works.
- When to use: Medium-risk, user-visible output, content generation

**Full harness (Planner → Generator → Evaluator → Loop):**
- Cost: ~$200 per task (6 hours wall time)
- Example: Complex analysis, code generation, multi-step reasoning
- Architecture: Planner → Generator (v1) → Evaluator → [Loop until pass] → Deliver
- Failure mode: Can retry, iterate, self-improve
- When to use: High-stakes, irreversible decisions, complex reasoning

**Full harness + human gate (Planner → Generator → Evaluator → Human → Deliver):**
- Cost: ~$500 per task (8+ hours wall time + human time)
- Example: Legal analysis, medical recommendations, financial decisions
- Architecture: Harness → Human review + approval
- Failure mode: Escalated and human-verified before delivery
- When to use: Critical decisions, regulatory requirements, reputation risk

**The 22x question: When is it justified?**

Matrix:
| Task Risk | Use Solo | Use Solo+Eval | Use Harness | Use Harness+Human |
|-----------|----------|--------------|------------|------------------|
| **Simple** (low stakes, reversible) | X | | | |
| **Medium** (user impact, recoverable) | | X | | |
| **Complex** (analysis, reasoning) | | | X | |
| **Critical** (legal, medical, financial) | | | | X |

**Real-world examples:**
- "Find all support tickets from yesterday" → Solo ($0.01)
- "Summarize 50 support tickets and flag urgent ones" → Solo+Eval ($0.05)
- "Design a system architecture for our product" → Harness ($200)
- "Review contract for legal compliance" → Harness+Human ($500+)

**Cost-benefit analysis:**
- If failure cost > 100x task cost, upgrade architecture.
- If failure cost < 10x task cost, stick with solo.
- In between: Solo+Eval is the sweet spot.

### 5A. Model Routing ROI (40-60% Cost Reduction)

Most of your queries are easy. Use that.

**The distribution (empirically validated across products):**
- 70-80% of queries are "easy" (can use Haiku, cached results, rules engine)
- 15-25% are "medium" (need full context, Sonnet-level reasoning)
- 5-10% are "hard" (new problem, Opus-level reasoning, research needed)

**Cost per model (2025 pricing):**
- Claude Haiku: $0.80 / 1M input, $4.00 / 1M output
- Claude 3.5 Sonnet: $3.00 / 1M input, $15.00 / 1M output
- Claude 3 Opus: $15.00 / 1M input, $75.00 / 1M output

**Naive approach (use Opus for everything):**
- Cost per 1000-token request: ~$0.05

**Smart routing (classifier + tiered models):**
- Easy queries (70%): Haiku. Cost: ~$0.004 per request
- Medium queries (20%): Sonnet. Cost: ~$0.015 per request
- Hard queries (10%): Opus. Cost: ~$0.05 per request
- Average cost: (0.70 × 0.004) + (0.20 × 0.015) + (0.10 × 0.05) = **$0.0138 per request**

**Savings: 72% reduction vs. Opus-only (0.0138 / 0.05)**

**But routing has overhead:**
- Classifier model (lightweight, ~50ms latency): ~$0.0005 per request
- Misrouting risk (5% of "medium" sent to Haiku): Quality loss measurable
- Break-even: Routing pays off if you have >10K requests / day

**Implementation strategy:**
1. Start with simple heuristics (token count, keyword patterns): low cost, 70% accuracy
2. Build lightweight classifier (Haiku-size) if heuristics fail: +$0.0005 cost, +5% accuracy
3. Don't over-invest in routing precision; 75% routing accuracy is often sufficient

**Hidden cost of bad routing:**
- 5% of medium queries go to Haiku → 15-20% accuracy drop
- Users get bad answers → escalation / retry → full cost again (Opus)
- Effective cost: Haiku + Opus + support overhead

### 5B. Identify Your Cost Levers (Ranked by Reality)

Most powerful in production:

| Lever | Mechanism | Cost Reduction | Implementation | Quality Risk |
|-------|-----------|-----------------|----------------|-------------|
| **Smart model routing** | 70% queries → cheap model (Claude Haiku), 30% → Sonnet | -35% | Medium (routing logic) | Low (users don't see cheap model) |
| **Hybrid retrieval pruning** | Cut retrieval from 20 docs to 8, validate with re-ranking | -40% retrieval | Low (algorithm) | High (hallucination if too aggressive) |
| **Cache query patterns** | Identify 20% of queries repeat; cache results for 24h | -18% effective cost | Low (caching layer) | Low (deterministic queries only) |
| **Embedding optimization** | Switch to smaller embedding model, re-rank for quality | -25% embedding cost | Medium (re-test quality) | Medium (retrieval quality dips slightly) |
| **Batch human review** | Async batching of reviews instead of real-time | -40% human cost | Medium (UX: slower feedback) | Low (review quality same) |
| **Cheaper inference model** | Use Claude Haiku for everything | -60% | Low (API swap) | **CRITICAL** (hallucination, accuracy) |

**The reality:** Combine smart routing (70% cheap model) + hybrid retrieval pruning (8 vs 20 docs) + embedding optimization = 50% total cost reduction with acceptable quality tradeoff.

Never use "cheaper model for everything" alone. It fails.

### 6. Eval Cost at Scale (Hidden Product Line Item)

Eval is not infrastructure overhead. It's a feature. It costs money. Budget for it.

**Cost structure:**
- Running eval suite once: $100-500 (depends on model, sample size, complexity)
  - Example: Eval on 1,000 examples with Opus = ~$3 inference + overhead = $150-200
  - Example: Eval on 10,000 examples with Haiku = ~$0.40 inference + overhead = $50-100

**Monthly eval budget (mature product):**
- Baseline: 5-10 eval runs / month = $500-5,000 / month
- Growth phase: 20-30 eval runs / month (daily evals) = $2,000-15,000 / month
- Critical product: 50-100 eval runs / month (daily evals + regression suite + segment analysis) = $5,000-50,000 / month

**Common surprise: Eval cost exceeds inference cost at scale**
- Inference: 100K queries/day × $0.015/query = $1,500/day ($45K/month)
- Eval: Daily eval on 1% sample (1K examples) × $0.20 = $200/day ($6K/month)
- Monthly eval monitoring: $6-8K
- At 1M queries/day: Inference $450K, Eval $60-80K (13-18% of inference cost)

**Budget as product P&L line item:**
- "Eval & monitoring infrastructure" = separate line item
- Allocate 5-15% of inference budget to eval
- If eval costs exceed 20% of inference, feature is over-monitored (or under-utilized)

**Cost-benefit of eval intensity:**
- Low eval (monthly): Save $10K/month, risk undetected drift (2-4 week lag)
- Medium eval (weekly): $30-40K/month, detect drift in 7 days
- High eval (daily): $60-100K/month, detect drift in 1 day
- Critical (continuous): $150K+/month, minute-by-minute monitoring

**Optimization strategies:**
- Use cheaper model for eval (Haiku instead of Opus): -60% cost, +5% eval time
- Stratified sampling (eval rare cases more, common cases less): -40% samples, same coverage
- Cached evals (compare to baseline, not absolute): -50% compute for regression detection
- Batch eval runs (nightly, not continuous): -30% infrastructure overhead

**Never skip eval to save money. If you can't afford to eval, you can't afford the feature.**

### 6A. Cached Prompt Discounts (40-70% Cost Reduction)

Anthropic offers 90% discount on cached tokens. Design context to exploit it.

**Prompt caching economics:**
- Standard tokens: $3 / 1M input (Sonnet)
- Cached tokens: $0.30 / 1M input (90% discount)
- Non-cached tokens: $3 / 1M input (normal price)

**Caching strategy:**
- Static system prompt (same for all users): ~2,000 tokens, cached
- Static context (documentation, knowledge base): ~8,000-15,000 tokens, cached
- Dynamic user input: ~500-2,000 tokens, non-cached

**Cost impact:**
- Naive approach (no caching): (2000 + 12000 + 1000) tokens × $3/1M = $0.045 per request
- Cached approach: (14000 cached × $0.30) + (1000 non-cached × $3) = $0.0042 + $0.003 = **$0.0072 per request**

**Savings: 84% reduction (0.0072 / 0.045)**

**But caching has requirements:**
- Prompts must be identical for cache hit (whitespace, punctuation, everything)
- Cache window: 5 minutes (token expires after 5 min of inactivity)
- Minimum cache size: ~1,000 tokens (smaller prompts not cached)
- One cache per model + API key combination

**Implementation (standard pattern):**
```
System Prompt (static, cached):
"You are a support bot. Knowledge base: [100KB of docs]"
↓ (cached across all users for 5 minutes)

User Query (dynamic):
"How do I reset my password?"
↓ (fresh tokens, normal price)

Output: Same model, reuses cached system + docs, only charges for query
```

**Cost comparison:**
- 1,000 queries/day without cache: $45 (all tokens non-cached)
- 1,000 queries/day with cache: $7.20 (84% savings)
- 1,000,000 queries/day without cache: $45,000/day
- 1,000,000 queries/day with cache: $7,200/day

**When caching doesn't work:**
- Personalized system prompts (per-user → no cache hit)
- Highly dynamic context (retrieval results change per query → no cache hit)
- Batch processing (cache expires between requests)

**Design for cache hits:**
1. Separate **static** (system prompt, docs, rules) from **dynamic** (user input)
2. Version your static context. When you update docs, new prompt = new cache entry (old one still exists, harmless)
3. Use context streaming: static prompt → cached → dynamic user query → sent in single request
4. Measure cache hit rate: (cached tokens used) / (total tokens sent). Target: >70%

**Cache hit monitoring:**
- Low hit rate (<30%): Your static context is not reusable. Redesign.
- Medium hit rate (30-70%): Acceptable. Dynamic context is the constraint.
- High hit rate (>70%): Optimal. You're using cache effectively.

### 6B. Calculate Margin at Scale

| Metric | Value | Notes |
|--------|-------|-------|
| **Cost per successful outcome** | $0.094 | At 10x scale, with stress test |
| **Cost per user/month** (10 queries/user) | $0.94 | 10 × $0.094 |
| **Monthly users (10x scenario)** | 10,000 | |
| **Monthly cost** | $94,000 | |
| **Revenue per user/month** | $20 | Assumed: freemium +upsell |
| **Monthly revenue** | $200,000 | |
| **Gross margin** | +53% | **Sustainable.** Negative? You have a feature problem. |

If margin is negative at 10x, the feature doesn't work. Period. Either the costs are wrong, the revenue model is wrong, or the feature shouldn't ship.

## KEY DIAGNOSTIC QUESTIONS

Ask yourself:

- **What's my cost per successful outcome, not per call?** (Include failure rate, human review, escalation)
- **Where's the 80/20 in my cost stack?** (If eval is 28% of cost, that's where to optimize, not inference)
- **At what scale does my margin turn negative?** (2x? 5x? Never?)
- **What's my retrieval cost vs. inference cost?** (If retrieval > 40% of inference, your vector DB is the constraint, not the model)
- **How many failed queries does my feature generate?** (Each failure is full cost with zero value)
- **Can I tier my model routing by query complexity?** (70% cheap model for easy queries is 35% cost reduction)
- **What happens to cache hit rate at 10x query volume?** (It collapses. Plan for 15-25%, not 40%+)
- **What's my eval infrastructure cost, and does it scale?** (At 100K queries/day, eval costs can exceed inference)

## REALITY CHECK

- **The overhead multiplier is real.** Naive token cost × 3-5 is the actual cost when you include retrieval, human review, eval, and infrastructure. Plan for 5x if you're honest.
- **Retrieval cost is often bigger than inference cost.** Especially for RAG: embedding every document, storing vectors, re-ranking, and searching is expensive. Don't ignore it.
- **Human review costs scale with volume, not linearly.** At 1,000 queries/day you review 10. At 100,000 queries/day you need systematic ML-assisted review. Cost multiplies 20x.
- **Model routing is your best lever.** If 70% of queries are simple, use a cheap model. This is safe and reduces cost by 35-50%.
- **Cache hit rates collapse at scale.** You can't predict them. Plan for 25% at 10x volume, not 45%.

## QUALITY GATE

Before committing resources:

- [ ] **Cost stack mapped:** Every system identified (inference, retrieval, storage, compute, human, eval) with estimated cost per component
- [ ] **Cost per successful outcome calculated:** Not per call; accounts for failure rate, escalations, human review
- [ ] **10x scale stress test done:** Retrieve volume, token size, cache hit, eval cost, human review volume all re-estimated
- [ ] **Model routing strategy defined:** % queries per model (cheap vs. expensive) at current and 10x scale
- [ ] **Margin calculated at scale:** If negative, feature doesn't ship without cost reduction
- [ ] **Cost levers chosen and modeled:** Primary lever picked (smart routing, retrieval pruning, or both) with realistic impact
- [ ] **Failure rate measured or estimated:** Not assumed zero
- [ ] **Board or stakeholder sign-off:** On the cost model and margin acceptance (profitable or approved loss)

## WHEN WRONG

- **When your feature is cost-insensitive.** If it's loss-leader or core product moat, unit economics don't matter for go/no-go. (Still build the model to know the loss.)
- **When user behavior is entirely unknown.** Build the model with wide ranges; re-run weekly with actual data.
- **When inference dominates all other costs.** Rare. Usually means you've under-estimated retrieval or human cost.
- **When you're comparing models without stress-testing scale.** Claude 3.5 Sonnet vs. Haiku looks like 3x cost difference until you add model routing; then it's 35%.
- **When you assume you can control failure rates.** You can't, at scale. Plan for degradation.

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
