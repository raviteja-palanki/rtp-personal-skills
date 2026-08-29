---
name: cost-model
version: v1.3_latest
description: 'What does your AI feature really cost, and does the math still work at 10× the usage? Maps the full cost stack (model calls, retrieval, storage, human review, eval) and prices the cost of a *successful* outcome, including failures, escalations, and the agentic call multiplier (one task now fires 10-20 calls). Owns the cost mechanics the money system needs (harness multiplier, model routing, prompt caching, batch) and hands the P90 cost-per-outcome to token-economics for pricing. Covers the Jevons trap (cheaper tokens, bigger bills), the 10× degradation table, routing ROI and its maturity ladder, eval-cost-at-scale, and the margin gate with a price-erosion stress test. Use when: pricing decisions, scaling plans, ''can we afford this'' reviews. Pairs with: token-economics (how to charge), moat-finder (cost vs growth line), ship-decision (the margin gate). Triggers: ''unit economics'', ''AI cost model'', ''cost per outcome'
imports: [stress-test, token-economics]
---

# Cost Model

## THE ONE IDEA

**The cost that matters is never the token — it's the cost of a *successful outcome*.** One outcome hides what the token count doesn't show: in an agentic flow it takes 10-20 model calls, inference is only ~20-30% of the real bill, and you pay for every failed attempt whether or not the user got a good answer. Model that real number — at P90, at 10× usage, at your true call multiplier — or you'll ship a margin you can't defend in a scaling review. This skill owns the cost math; `token-economics` turns the answer into a price.

## DEPTH DECISION

**Go deep** if: you're pricing an AI feature, doing go/no-go on a launch, or your margin is unclear at 10x scale. Read sections 1-6.

**Skim to KEY DIAGNOSTIC QUESTIONS** if: you have an existing cost model and want to pressure-test assumptions. The diagnostic questions will surface blind spots fast.

**Skip** if: the feature is a loss-leader by design, or you're in early prototype where unit economics are irrelevant.

## THE TRAP

**The Jevons trap — cheaper tokens, bigger bills.** The price of a token fell roughly 75× since 2023, and enterprise AI spend went *up*, not down. The reason: as each call got cheaper, teams used far more of them. One user task no longer means one model call — an agent plans, acts, checks, and retries, so a single task now fires **10-20 calls**; retrieval (RAG) inflates the context 3-5×; and always-on monitors run 24/7. The teams that win built routing, caching, and harness discipline in from day one; everyone else gets Cursor-style bill shock (reported multi-million annual run-rates with no matching productivity, ⚠ production signal). So "just measure tokens" is not enough — the number that survives a P&L review is **cost per successful outcome**, and the biggest driver of it in 2026 is how many calls one task quietly triggers.

You will model inference cost in isolation. Reality: **inference is usually only 20-30% of total cost.** The other 70% hides in retrieval (embedding + vector DB + re-ranking), storage, compute overhead, human review pipelines, and eval infrastructure.

You'll also assume costs scale linearly. They don't. Retrieval cost grows with corpus size. Eval cost grows with volume. Error correction compounds under load. Cache hit rates collapse as query diversity increases. By 10× scale, your $0.02-per-call assumption becomes $0.06-0.10 — before the agentic multiplier above. You'll have committed infrastructure before realizing margin is negative.

## WHAT THIS SKILL CONSUMES & PRODUCES

Cost-model is the **cost engine** of the money system: it owns the full cost mechanics, and the pricing skill consumes its answer. Naming the edges also closes a live boundary — the harness multiplier, model routing, caching, and batch economics live *here*, not in `token-economics`.

**Consumes (inputs):**
- **Usage telemetry** — calls and cost per user at P50/P90/P99, plus the agentic call multiplier, from your instrumentation.
- **The harness architecture** — how many agents, evals, retries, and human gates a task runs through, from `agent-harness` (the machine) and `harness-operating-model` (the program).
- **Current model prices** — the live per-token rates and cache/batch discounts.
- **The failure taxonomy** — how and how often outcomes fail, from `production-observability` / `eval-framework`.

**Produces (outputs):**
- **Cost per successful outcome at P90** — the single number `token-economics` needs to price (this is the hand-off that closes the routing debt).
- **The cost-moat read** → `moat-finder` (is our routing/harness efficiency a real cost advantage, or parity?).
- **The margin gate** → `ship-decision` (positive at 10× or don't ship).
- **The cost dashboard** — the live KPIs below, for ongoing telemetry.

## THE PROCESS

### KEY TERMS (plain language)

- **Cost stack** — all the real costs behind an AI feature: inference, retrieval, storage, eval runs, human review, infrastructure.
- **Cost per successful outcome** — the cost of a user actually getting a useful answer, including failed attempts and escalations — not the cost of a single call. This is the north-star number; report it to the board, not "cost per call."
- **Agentic call multiplier** — how many model calls one user task actually triggers (plan → act → observe → verify → retry). Was ~1 in a chatbot; is 10-20 in a real agent. Track it over time — it is the fastest-moving driver of your cost.
- **Model routing** — sending easy queries to a cheap model and hard ones to an expensive model to cut cost.
- **Cache hit rate** — the share of your prompt tokens served from cache (much cheaper). A first-class dashboard metric; target **>70%**.
- **Cached prompt discount** — paying much less for repeated prompt prefixes the provider can cache.
- **Margin at scale** — whether the feature is still profitable once volume, failures, and eval costs grow.
- **Salary budget vs. software budget** — the price ceiling is set by which P&L line the outcome displaces: expert-judgment labor (uncapped, risk-adjusted) versus another software seat (capped). Same product, 5-10× different ceiling when it genuinely does judgment work. The mirage to avoid: a pure record-lookup tool dressed as "AI judgment" stays on the software budget.

### 1. Map Your Real Cost Stack

Don't start with tokens. Start with every system that touches your feature:

**Inference layer:** Model API calls (input + output tokens)
**Retrieval layer:** Vector embeddings (queries + documents), vector DB hosting, re-ranking models, hybrid search
**Storage layer:** Document storage, vector embeddings at scale, cache storage, logs
**Compute layer:** Orchestration, retries, timeouts, fallback routing, load balancing
**Orchestration & retry overhead:** state management, tool-calling glue, multi-model handoffs, retry/fallback loops — no longer negligible in agentic or RAG-heavy flows, where one task fans out into many calls
**Human layer:** QA review, safety review, user feedback loops, annotation for improving retrieval
**Eval layer:** Daily evaluation runs, quality monitoring, drift detection, cost auditing

For each layer, ask: **At what scale does this become expensive?** Embedding costs are negligible at 1M documents but substantial at 100M. The sharper version of the scale question: *at what corpus size or query diversity does retrieval cost exceed what caching saves?*

### 1A. Which Pathway Does This Saving Assume? (ask before you model anything)

Before you build a cost stack for any AI-driven saving, name which of three pathways it assumes. BCG's economists sort every AI productivity claim into one of these: the same output with less input, more output with the same input, or a new business model that replaces the old one.

Mechanism: all three pathways converge on the same endpoint once the AI capability behind the saving is rented and available to every competitor, because price competition erodes the saving back out of the business that captured it first. A saving built on an owned or exclusive capability, one competitors cannot rent from the same vendor, does not face that same pressure on the same timeline.

So ask two questions before the cost math starts: which of the three pathways is this, and is the underlying capability rented/universal (a frontier model API any competitor can buy today) or owned/exclusive (proprietary data, a fine-tuned model, a workflow competitors cannot replicate)? A saving built on a rented, universal capability is a temporary advantage. Model it with an explicit erosion timeline. Don't book it as permanent margin.

When this is wrong: a saving from a genuinely owned capability, or from a market position that blocks competitors from renting the same tool, does not erode on the same clock. Test that assumption instead of assuming rented capability always erodes and owned capability never does.

*(Source: BCG economists on AI and margin, Jul 2026 — framework, not a measured statistic, no population to tier.)*

### 1B. Map the Physical Energy Layer

Every cost in section 1 is still, underneath, a line on a cloud invoice you can renegotiate every year. Electricity is not, and this skill has treated compute as an abstract, purchasable software cost with no physical or geographic dimension until now.

Global data-center electricity use is projected to roughly double this decade: about 485 terawatt-hours in 2025, rising to 945-950 terawatt-hours by 2030 (tier: ✅ audited, IEA, cross-confirmed by trade press covering the same estimate).

The pattern behind that number has a name: the Great Value Loop. AI competition's scarce layer has moved through four eras: connectivity, then attention, then intelligence and compute, and now energy and physics. Each era's scarce layer commoditizes as capital floods in to build more of it, but demand does not pause once that happens. It accelerates and presses on the next constraint underneath. This is a Jevons-paradox effect: cheaper intelligence expands the number of viable use cases faster than it cuts the energy draw per use, so the aggregate bill keeps climbing even as the unit cost falls.

Mechanism, and the reason this is a genuinely different cost category than anything else in this stack: electricity is local, physically permitted, slow to add new capacity for, and politically contested, in a way cloud compute spend simply is not. You can renegotiate or switch a cloud contract inside a fiscal year. You cannot relocate a data center to a cheaper power market on the same clock, and a new substation or transmission line can take years to permit and build no matter how much capital shows up.

Two metrics belong on the cost dashboard once you are tracking this layer: energy cost per workflow, and tokens or inferences produced per kilowatt-hour. Both give a unit that survives a change in which model or vendor you use, the way cost per successful outcome already does for compute.

When this doesn't apply: this sub-step earns its place only for a company with real negotiating leverage and volume, large enough to consider a power-purchase agreement or a data-center site decision. A mid-size company running entirely on one cloud vendor's managed API has no practical lever over region selection or energy sourcing today, and gets little value from this analysis. That may change once vendors start exposing per-workflow energy reporting, but until they do, treat this section as a watch item rather than a modeling requirement.

*(Source: Tang and Zhao, "Your Company Needs an Energy Strategy for AI's Next Phase," HBR, 4 Jun 2026 — the electricity projection is tier: ✅ audited (IEA), cross-confirmed by trade press covering the same estimate; the Great Value Loop and the Jevons-paradox mechanism are the article's own framing.)*

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

*The numbers above are an illustrative 2025/early-2026 production example, not a template to copy.* Two rules: (1) **replace this table with your own telemetry within 30 days of launch** — real cost lives in your traces, not in an example; (2) add a **P90 cost-per-outcome** column next to the average — the average hides the outlier users and tasks that actually blow the margin.

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

**Instrument this from day one, not after.** Track a **failure taxonomy** — retrieval miss, hallucination, policy violation, timeout — and the **human escalation rate**, from launch. You cannot price or fix what you cannot name. Report **cost per completed/accepted outcome** as the north-star metric to the board; "cost per call" is the vanity number that hides the problem.

**The cost line everyone omits sits inside the user's own week, before any of this.** Call it botsitting: prompt attempts before a usable output, review passes, and time spent patching context the model should have had. One survey put both quantities on the same people in the same instrument: **11 hours a week automated against 6.4 hours a week botsitting.** That is **58% of the reported individual time saving consumed by the labour of making the tool produce it**, an arithmetic the article itself does not perform.

Why the ratio is more defensible than either level: both figures are self-reported by the same respondents in the same survey, so the ratio cancels most of the shared optimism bias that makes each level suspect alone. The vendor's interest runs toward a larger botsitting number, so **treat 58% as a ceiling**. Even at half of it, a third of the saving is eaten before it leaves the individual's week.

**What to do with it.** Botsitting hours are countable and the three components are named, so add them to the cost stack as an explicit line rather than assuming a productivity claim nets out. A feature that saves ten hours and costs six in prompt-wrangling is a different business case from one that saves ten and costs one, and nothing in a per-call model distinguishes them.

**Two haircut coefficients, not one, and the coefficient depends on who produced the number.**

- **Halve for a scope change inside one measuring party.** Vanguard measured about 25% for coding alone and 10 to 15% across the development life cycle. Same organisation, same underlying work, two scopes.
- **Third for a vendor claim met by a customer's own measurement.** Vendors putting forward 15 to 20%, a firm measuring 5 to 7% on its own service lines. Tier ⚠ on the numerator, since the vendor figure is the authors' characterisation of unnamed claims, so the ratio inherits it.

The general form is the useful part: **a number's inflation tracks the distance between whoever produced it and whoever pays when it is wrong.** Treat both coefficients as priors rather than findings, each resting on one case.

**A modelled counterfactual is a worse denominator than a missing one.** One widely-cited speed claim rests on a manual baseline that was never observed, produced by two model-based estimates from one team on one telemetry set, which is one estimate rather than two, and the study's own users put the multiple more than three times higher than its model, one paragraph apart and unreconciled. A missing denominator invites the question. A modelled one answers it, wrongly, and stops anyone asking. **When you meet a productivity multiple, ask whether the baseline was measured or reconstructed, before you ask how big it is.**

**And the caution that keeps this honest.** In the same survey, 75% of workers reported being more productive with AI while 13% reported their organisation performing significantly better. Those are **not one quantity measured twice**. Different questions, different bars, and the second asks a worker to assess something they mostly cannot see. That 6-to-1 gap is not a scope-adjusted productivity figure and must never ship as one.

*(Sources: HBR, Hinds & Leonardi, "How Much Time Do Your Employees Spend Botsitting?", Aug 2026; HBR, Blangeois & Roulet, Aug 2026, for the vendor-versus-customer ratio; the Vanguard figures already carried in this library. Ledger pattern H.)*

**Check what a cheap "AI-assisted review" number is quietly assuming.** An unrefereed SSRN theory paper on the "collaboration paradox" argues that assisted review looks cheaper than manual review only because its model assumes away the one review design that would actually catch AI errors. That design is independent-then-compare: a human reviews before seeing the AI's answer, then compares the two. It costs more than simple approve/reject review, so the paper's cost math leaves it out.

Mechanism: approve/reject review is cheap because the human anchors on the AI's answer instead of forming an independent judgment first. That same anchoring is why approve/reject review is worse at catching AI errors. The paper's cost advantage and its blind spot come from the same assumption.

So if a cost model prices "AI-assisted review" at or below the cost of pure manual review, check whether it silently assumes away the safer, costlier review design. Collaboration priced below manual cost is a warning sign, not a win.

When this is wrong: for low-stakes review where an uncaught AI error costs little, approve/reject review is a legitimate design choice, and the lower price is real rather than hidden.

*(Source: unrefereed SSRN theory paper on the "collaboration paradox," Jul 2026 — tier: theoretical, no data, no population; a model rather than a study.)*

### 3A. Which Budget Pays For It — The Price Ceiling

Cost-per-outcome (above) is the *cost* side. The *price* side is set by which budget the value comes out of — and that's often the bigger lever.

**Salary budget vs. software budget.** A tool that replaces a paid expert comes out of the *salary* budget (the cost of the person, plus the mistakes avoided). A tool that's just another piece of software comes out of the *software* budget. The salary budget is roughly ten times larger. Same product, very different price ceiling, depending on which budget line it displaces. "Charging per outcome instead of per seat" isn't a fashion — it's software crossing into that bigger, salary-sized budget by doing judgment work a paid expert used to do. **Why it matters:** a feature with a thin margin at a per-seat price can have a healthy one once you re-price it against the labor it replaces; cost-per-outcome tells you whether you're *profitable*, not how high you can price. **When this is wrong:** only holds where the tool genuinely displaces expert labor — a record-lookup tool dressed up as "judgment software" stays on the software budget, and the bigger ceiling is a mirage. *(Source: "AI's Impact on SaaS Will Be Uneven," Stanton, HBR, 27 May 2026.)*

**The edge case that keeps you on the software budget.** When the AI only *speeds up* an existing workflow without changing who owns the judgment or the risk, the ceiling stays software-budget — no matter how impressive the demo. The 10× labor-displacement ceiling only opens when your prompts + proprietary context + ownership of the outcome become a compounding asset the buyer can't easily rebuild. Speed alone doesn't cross budgets; owned judgment does.

**Reprice work by value, not by the hourly rate (vendor renewals and insource decisions).** The outsourcing era priced work by where labor was cheapest. On any vendor renewal or in-source decision, ask what the work is actually worth across five things — cost, quality, speed, risk, and control — not what an hour of offshore labor costs. Make the vendor show how AI changes each of the five, and put ownership of the prompts, code, and knowledge bases into the contract. **Why it matters:** the hourly rate hides where AI actually shifts value (usually quality, speed, and control), and whoever owns the prompts-and-data loop keeps the compounding asset. **When this is wrong:** for genuinely commodity work with no data or control value, the hourly rate is still the right basis. *(Source: "AI Is Rewriting the Economics of Outsourcing," Agrawal, HBR, 5 Jun 2026.)*

**One-line placement check (before you optimize cost at all):** the cost line you're modeling here is *floored at zero* — even a generous AI cut moves firm value only ~10%. Before investing to shave it, check whether a *growth* line (uncapped, and multiplied by the valuation premium) is sitting unexamined; a sustained 2-point organic-growth lift ≈ +50% firm value (◆ the authors' wealth-management valuation model — the mechanism generalizes, the figure is theirs). Don't optimize the capped line while the multiplied one goes unaimed. *(Full math in `rtp-moat-finder`, the value-line pre-screen. Source: "Companies Are Using AI for Efficiency. They Should Use It to Grow.", HBR, 1 Jun 2026.)*

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

### 4A. Agentic Multi-Call Inflation & the Jevons Reality (read this before you trust any per-call number)

The degradation table above assumes *one call per task*. Agents break that assumption, and it is the fastest way naive math turns into negative margin.

**What inflates the cost:**
- **One task → 10-20 calls.** A real agent plans, acts, observes, verifies, and retries. Each loop is another call. Your "call multiplier" is the number to watch — and to track over time (it was ~1 six months ago and climbs as you add autonomy).
- **RAG context bloat.** Retrieval stuffs 3-5× more tokens into every call, and you pay for all of them.
- **Always-on monitors.** Background agents and watchers run 24/7 whether or not a user is active.

**The counter — cost control is system design, not a cheaper model.** The levers that keep the multiplier manageable are architectural: **route** by complexity (cheap model for easy calls), **cache** aggressively (>70% hit rate), and **prune the harness** (early exit, fewer retries, tighter context). Production teams running billions of tokens report the same lesson: the win comes from routing + context discipline + guardrails measured against *cost per accepted outcome*, not from chasing the cheapest model (⚠ production signal).

**The decision:** before you ship an agentic flow, compute cost at your *real* call multiplier, not one call. If the multiplier × per-call cost breaks the margin, the fix is fewer/cheaper calls by design — cap retries, route, cache, prune — not a model swap.

### 4B. Who Sets the Terms of the Meter (read before you model any vendor-supplied AI)

Everything above prices what you consume. This prices **who decides what a unit is**, which turns out to matter more, because the vendor subsidy era is ending on published dates rather than gradually.

**The bill has four terms and you hold one of them.**

| Term | Who sets it | Notes |
|---|---|---|
| Interactions per agent | the vendor's design | an agent that "thinks" more bills more |
| Units per request | **the vendor's definition** | the dangerous one, see below |
| Price per unit | the vendor | the only term anyone negotiates |
| Seats and usage frequency | **you** | and only partly, once the tool is in a workflow |

Setting an overall AI budget in the abstract is close to useless while three of four terms belong to someone else. **Model your elasticity instead: work out what per-unit price your actual usage could justify, then negotiate against that number.**

**Units per request is the devaluation lever, and almost no contract closes it.** A vendor can raise your effective price without touching the headline rate, by changing how much work one unit buys. The honest version of the problem, from a practitioner: *"It's also unclear just how much actual work is included in each unit."* A rate card tells you the price of a unit and not the size of one. **The missing contract term: a written definition of the unit of work, fixed for the contract term, with a right to re-measure.** Ask for it explicitly. Also negotiate caps, grace periods and credit rollover, which are the terms that survive a mid-contract repricing.

**The worked example, and its finding runs against the alarm around it.** Take a published structure: five AI units per basic request, 20,000 units included free per month, at an illustrative one cent per unit. Run a 10,000-employee company through it. Ten percent of staff at ten interactions a month is about **$3,600 a year**. Half the staff at the same rate is about **$27,600 a year**. Even at six figures, that is **ten to thirty dollars per employee per year**. **Per-unit token pricing at plausible enterprise usage is a rounding error against payroll.** The costs that are not a rounding error are the ones nobody meters: the human time spent running the tools, the change management, and the capability you lose when you stop doing the work yourself. Price those before you argue about the rate card.

**The structural point worth carrying into any board conversation.** Deploying AI agents at scale *"structurally shifts resources from capacity it controls (employee wages) to capacity it rents (variable token consumption)."* Rented capacity reprices on someone else's calendar. Owned capacity does not. That is a balance-sheet argument rather than a budget one, and it is the reason to keep people **capable** of executing core functions even when they are not doing them daily.

**One cross-source finding that changes how you size the adaptation window.** Two credible 2026 sources, twelve days apart, describe the same technology on two different clocks:

- **Capability is a rising tide.** Broad, steady improvement, with the failure rate halving roughly every 2.2 to 2.8 years. Many labs improving independently smooths into a curve at the benchmark level.
- **Price is a step function.** Subsidy withdrawal arrives as discrete vendor decisions with effective dates, made on a board's calendar under quarterly investor pressure. Nothing smooths it.

**Organizations compute their adaptation window on the capability curve and get hit by the price curve.** One gives you years. The other gives you a date. Only the second one shows up on a budget, so size your runway on the repricing calendar of the vendors you actually depend on, and use the capability curve for capability decisions only.

**Four finance prerequisites underneath any AI investment case.** These are ordinary corporate-finance discipline, and AI business cases routinely skip all four:

1. **Alternatives-based decision-making.** What else could this capital do? In one survey of executives at 760 large organizations, only about **one in five** reported explicitly considering alternatives in strategy development.
2. **Unit-level balance-sheet reporting.** Can you see the assets and returns at the level of the business unit making the bet?
3. **Cost-of-equity discipline.** Have a real discount rate. A usable anchor: the average cost of equity across large public companies sits **slightly above 9%**, implying a market risk premium of roughly 4% to 4.5% over long-term government bond yields, and most large public companies fall within **plus or minus 1.5 percentage points** of that.
4. **Scenario-based forecasting.** One number is not a forecast, and per-unit pricing with three vendor-controlled terms is exactly the case that needs a band.

**The standing warning on the benefit side.** Economists linking large-scale adoption surveys to administrative payroll records found the effect on earnings and hours two years on **statistically indistinguishable from zero**, and the proposed cause is that the time saved was consumed by the work of running the tools. **So a measured task-level productivity gain does not entitle you to a line in a business case.** Between the accelerated task and the business outcome sit human steps: responding to the model's output, wiring it into existing systems, and re-entering it into the decision. Count those steps before you book the saving.

*(Sources: the four-term bill, the units-per-request problem, the worked example and the rented-capacity sentence, HBR, Garr, "How to Respond to the Coming AI Cost Shock," Aug 2026 — the vendor structure is ◆ company-disclosed, the per-unit rate is the author's own illustration, and the alarming figures elsewhere in that article have the weakest provenance in it. The two-curve finding is this corpus's synthesis of Garr against MIT Sloan's FutureTech coverage, Aug 2026 ◆; neither source makes it. The finance prerequisites and the cost-of-equity band, HBR, "Bring Back Managing for Value," Aug 2026 — ◆ Bain's own analysis and methodology, not an audited figure; the 760-executive survey is ⚠ and is cited in the article without a retrievable link **[VERIFY]**. The payroll null, HBR, "4 Steps to Transform the 'Middle Office' with AI," Aug 2026 — ⚠ and worse, the underlying study is described but never named **[VERIFY: linked survey-to-payroll design, findable literature]**; carry the mechanism, not the null as a settled result. Ledger patterns H and N.)*

---

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

**Two 2026 notes.** (1) Budget the **orchestration overhead** as its own line — state machines, tool-calling glue, retry logic, and parallel-agent fan-out (Cursor-Composer-style) add real cost on top of the model calls. (2) A harness loop that *measurably lowers the human-escalation rate over time* stops being a cost center and becomes a **reliability moat** — a compounding asset once models commoditize. Design the loop for that, and track the escalation-rate trend. The *how-to-build-it* side lives in `agent-harness` (the machine) and `harness-operating-model` (the program); this skill only prices it.

### 5A. Model Routing ROI

Most of your queries are easy. Use that.

**The distribution (empirically validated across products):**
- 70-80% of queries are "easy" (can use Haiku, cached results, rules engine)
- 15-25% are "medium" (need full context, Sonnet-level reasoning)
- 5-10% are "hard" (new problem, Opus-level reasoning, research needed)

**Cost per model** *(illustrative tiers — always re-check live prices for the current generation, e.g. Haiku 4.5 / Sonnet 5 / Opus 4.8 / GPT-5.x; the shape holds, the numbers move):*
- Cheap tier (Haiku-class): ~$0.80 / 1M input, ~$4.00 / 1M output
- Mid tier (Sonnet-class): ~$3.00 / 1M input, ~$15.00 / 1M output
- Frontier tier (Opus-class): ~$15.00 / 1M input, ~$75.00 / 1M output

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

**Implementation maturity ladder (don't skip steps, don't over-build):**
1. **Heuristics** — token count, keyword patterns. Low cost, ~70% accuracy. Start here.
2. **Lightweight classifier** (cheap-tier model) if heuristics stall: +~$0.0005/request, +~5% accuracy.
3. **Learned router with stability checks** — only if volume justifies it. A router is only worth it when the models behave *differently enough* on your traffic and the routing is *stable when a query is paraphrased* — otherwise you're adding cost and flakiness for little gain (⚠ DeepMind routing research, Jul 2026). Require **>75% routing accuracy** as the minimum-viable bar, and **measure the misroute → escalation rate** — publish it.

**Hidden cost of bad routing (it compounds):**
- 5% of medium queries go to the cheap model → 15-20% accuracy drop
- Users get bad answers → escalation / retry → full frontier cost *again* + support
- Effective cost: cheap model + frontier model + support overhead — worse than never routing. This is why routing accuracy is a tracked metric, not a set-and-forget.

Validated at scale in 2026: production routing reports **46-76% cost reduction** (balanced/eco modes) and up to **~80% lower cost at the same quality** via orchestration; one ops team ran 2M+ requests across 14 models for a fraction of single-frontier cost (⚠ vendor/production claims — treat as directional, verify on your traffic).

### 5B. Identify Your Cost Levers (Ranked by Reality)

Most powerful in production:

| Lever | Mechanism | Cost Reduction | Implementation | Quality Risk |
|-------|-----------|-----------------|----------------|-------------|
| **Smart model routing** | 70% queries → cheap model (Claude Haiku), 30% → Sonnet | -35% | Medium (routing logic) | Low (users don't see cheap model) |
| **Hybrid retrieval pruning** | Cut retrieval from 20 docs to 8, validate with re-ranking | -40% retrieval | Low (algorithm) | High (hallucination if too aggressive) |
| **Cache query patterns** | Identify 20% of queries repeat; cache results for 24h | -18% effective cost | Low (caching layer) | Low (deterministic queries only) |
| **Embedding optimization** | Switch to smaller embedding model, re-rank for quality | -25% embedding cost | Medium (re-test quality) | Medium (retrieval quality dips slightly) |
| **Batch human review** | Async batching of reviews instead of real-time | -40% human cost | Medium (UX: slower feedback) | Low (review quality same) |
| **Orchestration pruning / early exit** | Cap retries, stop the agent loop once the answer is good enough, tighten context | -20-40% on agentic flows | Medium (harness logic) | Medium (stop too early → worse answer; gate with evals) |
| **Cheaper inference model** | Use the cheap-tier model for everything | -60% | Low (API swap) | **CRITICAL** (hallucination, accuracy) |

**The reality:** Combine smart routing (70% cheap model) + hybrid retrieval pruning (8 vs 20 docs) + embedding optimization = ~50% total cost reduction with acceptable quality tradeoff. On agentic flows, add orchestration pruning — it's often the biggest single lever once the call multiplier is high.

**Rank levers by impact on cost per *successful outcome*, not per call** — a lever that cuts per-call cost but raises the failure rate can make the real number worse. Every aggressive lever needs a named countermeasure (evals, a reranker, or a human gate). Never use "cheaper model for everything" alone — it fails.

### 5C. Fixed Setup Cost vs. Marginal Execution Cost (the averaging trap)

An agent's cost has two very different components, and averaging them together overstates cost per unit until volume is high enough.

Specifying and reviewing what an agent should do for a given task type is a high fixed cost: someone writes the spec, tests it, and signs off on it once per task type. Running the agent step by step after that is a low marginal cost: each additional run pays only for the calls that run makes, not for the setup work again.

Mechanism: an agent's true cost advantage over a human doing the same task shows up only past a certain repetition volume, the point where the fixed setup cost has been spread across enough runs that the marginal cost dominates the average. Below that volume, the fixed cost dominates instead, and the agent can look more expensive than the process it replaced even though its marginal cost is lower.

So before you compute cost per unit for an agentic workflow, separate the fixed setup line from the marginal execution line and state the volume at which you expect to cross breakeven. A cost model that blends fixed and marginal cost across a small number of runs will overstate cost per unit and can kill a project that would pay off at real scale.

When this is wrong: for a one-off or rarely repeated task, there is no breakeven to reach, and the fixed setup cost is simply the real cost. Don't force an amortization argument onto a task that will only run a handful of times.

*(Source: vendor study of its own agent products, Jul 2026 — tier ◆ company-disclosed/vendor-modeled; no human timed on the counterfactual, treat the cost estimates as directional, not audited.)*

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

### 6A. Cached Prompt Discounts

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

**Stress-test the revenue side too, not just cost.** Re-run the margin with **30% price erosion** — open-weight and self-hosted competitors are already pushing prices down on easy and medium work. And run it at your **P90 cost per outcome**, not the average — that's the scenario the power users put you in. A margin that only survives at average cost and today's price is not a margin you can defend in a scaling review.

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
- **What's my agentic call multiplier today vs. 6 months ago?** (If it's climbing, your cost is climbing even as token prices fall — the Jevons trap.)
- **What share of my cost comes from the top 5% of power users?** (Usage is power-law; a handful of users can drive most of the bill. Price and cap for them, not the average.)

## REALITY CHECK

- **The overhead multiplier is real.** Naive token cost × 3-5 is the actual cost when you include retrieval, human review, eval, and infrastructure. Plan for 5x if you're honest.
- **Retrieval cost is often bigger than inference cost.** Especially for RAG: embedding every document, storing vectors, re-ranking, and searching is expensive. Don't ignore it.
- **Human review costs scale with volume, not linearly.** At 1,000 queries/day you review 10. At 100,000 queries/day you need systematic ML-assisted review. Cost multiplies 20x.
- **Model routing is your best lever.** If 70% of queries are simple, use a cheap model. This is safe and reduces cost by 35-50%.
- **Cache hit rates collapse at scale.** You can't predict them. Plan for 25% at 10x volume, not 45%.
- **Open-weights + routing pressure is already here.** Frontier labs are losing share on easy and medium queries to cheaper open models. Raw model access is not a cost moat — your durable cost advantage is **harness efficiency + proprietary context + measured reliability**, not which API you call.

## QUALITY GATE

Before committing resources:

- [ ] **Cost stack mapped:** Every system identified (inference, retrieval, storage, compute, human, eval) with estimated cost per component
- [ ] **Cost per successful outcome calculated:** Not per call; accounts for failure rate, escalations, human review
- [ ] **10x scale stress test done:** Retrieve volume, token size, cache hit, eval cost, human review volume all re-estimated
- [ ] **Model routing strategy defined:** % queries per model (cheap vs. expensive) at current and 10x scale
- [ ] **Margin calculated at scale:** If negative, feature doesn't ship without cost reduction
- [ ] **Cost levers chosen and modeled:** Primary lever picked (smart routing, retrieval pruning, or both) with realistic impact
- [ ] **Failure rate measured or estimated:** Not assumed zero
- [ ] **Live KPIs instrumented and baselined:** cost per successful outcome, routing accuracy, cache hit rate (>70%), human escalation rate, agentic call multiplier
- [ ] **Revenue stress-tested:** margin still positive at P90 cost and 30% price erosion
- [ ] **Hand-off to `token-economics` complete:** the P90 cost-per-outcome number is delivered, and *what outcome we charge for* is decided
- [ ] **Board or stakeholder sign-off:** On the cost model and margin acceptance (profitable or approved loss)

## WHEN WRONG

- **When your feature is cost-insensitive.** If it's loss-leader or core product moat, unit economics don't matter for go/no-go. (Still build the model to know the loss.)
- **When user behavior is entirely unknown.** Build the model with wide ranges; re-run weekly with actual data.
- **When inference dominates all other costs.** Rare. Usually means you've under-estimated retrieval or human cost.
- **When you're comparing models without stress-testing scale.** Claude 3.5 Sonnet vs. Haiku looks like 3x cost difference until you add model routing; then it's 35%.
- **When you assume you can control failure rates.** You can't, at scale. Plan for degradation.
- **When speed-to-market or compliance outranks cost.** For a pure distribution play or a regulatory must-have, cost is secondary — build the model to know the number, but don't let it block the decision.
- **When self-hosting changes the whole stack.** Open-weight, self-hosted economics are predictable opex (fixed GPUs) rather than variable API spend — a different model entirely. Re-run the math on that basis before comparing.

## THE COST DASHBOARD (the one-pager to run monthly)

Ship the feature with a live dashboard, not a one-time spreadsheet. Five KPIs make the whole operating system glanceable for a PM or board:

```
COST MODEL — [Feature]                         [month]
Cost per successful outcome   $____   (P50 __ / P90 __)   trend __
Agentic call multiplier       __ calls/task     vs 6mo ago __
Routing accuracy              __%   (min viable >75%)  misroute→escalation __%
Cache hit rate                __%   (target >70%)
Human escalation rate         __%   trend __
Eval spend as % of inference  __%   (flag if >20%)
Gross margin at P90           __%   (at 30% price erosion __%)
```

If any line is blank, the cost model isn't instrumented yet — that's the first task, not the analysis.

---

## GROUNDING, TRADE-OFFS & CONCLUSION

Before starting, follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) Section 1 grounding questions (who is the customer, what problem, what are we saying YES and NO to) and confirm output format (document / deck / spreadsheet / inline). Close with the Trade-Off Ledger (Section 3) and the Conclusion Protocol (Section 5):
1. State the recommendation
2. Name the key trade-off — usually **harness complexity vs. the reliability moat it buys vs. near-term cost**
3. Acknowledge the biggest risk — you ship on "acceptable" per-call economics, hit 10× usage or an agentic flow, and discover the real cost per successful outcome is 2-3× higher as escalation and eval lines explode (the Cursor-style compression already visible in 2026)
4. Define the single next action — **instrument cost-per-successful-outcome + routing accuracy + the call multiplier this sprint**, then re-run the margin

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
