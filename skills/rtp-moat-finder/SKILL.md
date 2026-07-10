---
name: moat-finder
description: "Will your AI advantage survive copycats? Scores the four defenses that get stronger with use — the data loop, workflow lock-in, behind-the-scenes engineering depth, and earned trust — plus a pre-screen on which profit line (cost vs. growth) the feature even moves, and two checks for fake moats. Use when: setting strategy, deciding whether an edge is defensible or just parity with rivals, pre-investment reviews, or ~18 months out when base models catch up. Pairs with: build-or-buy (which capability to own), safety-as-moat (the trust side), eval-framework (the hard-case audit). Triggers: 'competitive advantage', 'defensibility', 'moat'"
imports: [bias-spotter, determinism-compass]
---

# Moat Finder

## DEPTH DECISION

**Go deep if:** You're evaluating long-term defensibility (18+ months), designing features specifically to build moat, or assessing if you have a real moat vs. temporary feature advantage.

**Skim to diagnostic questions if:** You want a quick audit of your planned moat or competitive advantage.

**Skip if:** Pre-market-fit phase where feature velocity matters more than defensibility, or if you're in a single-customer/bespoke context.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will confuse impressive with defensible. The bias is **recency bias** — a clever prompt or RLHF trick feels like a moat because it's novel. Three months later every competitor uses the same approach. You're left racing on execution cost, which is not a durable strategy.

In AI, moats are invisible until they work or fail. A proprietary dataset, a fine-tuned model, deep workflow integration — all can look defensible on launch day and become commodities by month 18. Teams that win know their moat *before* they start building. Teams that don't spend 18 months optimizing something someone else will copy in weeks.

## KEY TERMS (plain language)

Read these once; the rest of the skill uses them.

- **Moat** — a durable advantage a competitor can't easily copy.
- **Data flywheel** — usage creates data that improves the product, which attracts more usage; a loop that compounds.
- **Workflow lock-in** — customers are so embedded (integrations, trained staff, stored history) that switching is expensive.
- **Context depth** — the hard-to-copy engineering behind the scenes (prompts, evals, system design) that you can't read off the outputs.
- **Trust (as a moat)** — a track record of reliability and safety that buyers pay extra for; slow to build, fast to lose in one incident.
- **7 Powers** — Hamilton Helmer's list of seven durable business advantages (scale economies, network effects, counter-positioning, switching costs, branding, cornered resource, process power).
- **Network effects** — the product gets more valuable to each user as more users join (not the same as just collecting a lot of data).
- **Compounding feedback loop** — a system that improves itself from the data its own use generates.
- **Anti-moat loop** — that same self-improving loop, but fed by public data anyone can get, so it pushes everyone toward the same average instead of ahead.
- **Long tail** — the many rare, hard cases that each occur infrequently but together are common and expensive to get wrong.
- **Agent-in-the-middle squeeze** — when an AI assistant buys for the customer, a brand can lose both the moment it would persuade a person and the moment the choice is made.
- **Model-agnostic vs. model-dependent moat** — an advantage that survives model upgrades (harness, evals, workflows) versus one that fades when the base model catches up (a fine-tune, an architecture trick).
- **P&L value-line** — which line of the profit-and-loss statement an AI feature moves (cost vs. growth); the cost line floors at zero, the growth line is multiplied by the valuation premium.
- **Growth blindspot** — believing AI can hugely raise firm value yet spending it on efficiency, where the ceiling is low.
- **Data liquidity** — how ready-to-use a company's data already is for a new purpose (clean, reusable, validated); the measurable form of a data moat.
- **Data dependence (trust tax)** — how visibly a product relies on harvesting the user's own data; the more customers feel it, the more they discount its trust claims.

## VALUE-LINE PRE-SCREEN — Is This Worth Defending?

Before the defensibility analysis, run one screen: **which line of the P&L does this AI touch, and what's that line's ceiling?** The three lines aren't equal.

- **Cost line — floored at zero.** Even the generous case (half the cost base is AI-addressable, cut it 10% = a ~5% total expense cut) moves firm value only ~10%. Real, but bounded — you can't cut a cost below zero.
- **Growth line — no ceiling, and multiplied.** Investors price the valuation *multiple* on expected future growth, so a lever that touches the growth rate touches the multiple. In the authors' valuation model (run on wealth-management firms), a firm growing organically at 5% is worth ~50% more than an identical firm at 3% — a sustained 2-point growth lift ≈ +50% firm value before earnings even grow (◆; the mechanism generalizes, the exact figure is model- and industry-specific).
- **The bias to screen for — the growth blindspot.** Executives believe AI can more than double firm value (a roundtable of senior financial-services execs put an AI-leveraged wealth firm at a ~135% premium in three years) yet almost all spend it on efficiency.

**Why it matters:** a strong, defensible moat around a *cost-line* feature still can't move firm value much; the same effort aimed at the *growth line, behind a moat*, compounds — so screen the P&L line before you invest in defending it. **When this is wrong:** in a genuinely cost-constrained business (thin margins, survival mode) the cost line is the right target; and a growth lift with *no* moat is rented, not owned — it converges away (see the anti-moat loop below). *(Source: "Companies Are Using AI for Efficiency. They Should Use It to Grow.", Benartzi, Long & Puntoni, HBR, 1 Jun 2026. The 2.35× roundtable estimate is a senior-exec judgment ◆/⚠, not audited.)*

## THE PROCESS

**Step 1: Identify the core value engine.** What irreplaceable capability makes your product work? Not features—the core that competitors would need to replicate to match you.

**Step 2: Classify the moat type.** Pick one or more:

| Type | Mechanism | Example | Decay Clock |
|------|-----------|---------|---|
| **Data Flywheel** | Usage generates training data; model improves; attracts more users | Maps routing improves with every shipment | 12-24 mo if user adoption mirrors yours |
| **Workflow Lock-in** | Retraining/migration cost. Users embedded in your interface, API, context standards | Slack's thread history; fine-tuned model formats | 18-36 mo if switching standardizes |
| **Context Depth** | Proprietary engineering: prompts, evals, constitutional principles, system design | Anthropic's Constitutional AI stack | 24+ mo but shrinking as models improve |
| **Trust** | Track record of reliability/safety/alignment. Earned, not built. | Regulatory approval trail; safety brand | 1 bad incident erases years |

**Step 3: Validate the moat.** For your chosen type(s), answer these diagnostic questions:

**For Data Flywheels:**
- How much data do you collect per user per month? (Be precise: 10 rows? 1000 rows?)
- How much better does model get per 10,000 rows of new data? (Estimate via small dataset)
- How long until data volume creates irreplaceable advantage? (Calculate: rows_needed / rows_per_month)
- Can competitors access similar data through partnerships? (If yes, less defensible)
- Do users expect their data locked in? (If no, network-switching risk)

**For Workflow Lock-in:**
- How much would a customer pay to migrate? (Function of: data loss, retraining, integration cost, downtime)
- How many integrations have you created with their systems? (1 = weak, 5+ = strong)
- Are you embedded in their critical path? (Yes = strong, supplementary = weak)
- Can they replicate your workflow with new model in <1 month? (If yes, not locked-in)

**For Context Depth:**
- How much proprietary engineering can't be reverse-engineered from API responses? (Prompts, evals, system design)
- How many months of research separates you from an equally-smart competitor? (Be honest: 3 months = weak, 12+ months = strong)
- Is your advantage in model architecture, training, or inference? (Inference = easiest to replicate)
- How quickly could open-source versions catch up? (Fast = weak)

**For Trust:**
- How many incidents would it take to destroy your brand? (1 major failure = fragile, 5+ = resilient)
- Is your trust in regulatory compliance, safety track record, or brand perception? (Compliance = transparent, easy to replicate; brand = slow to build, sticky)
- Can competitors build trust as fast as you? (Especially relevant: do they already have it?)

**Step 4: Score data flywheel defensibility (1-5 scale):**

Score each dimension, take average:
- **Data volume:** 1pt if <1k rows/user/month, 2pts if 1-10k, 3pts if 10-100k, 4pts if >100k. (5pts reserved for network effects)
- **Improvement rate:** 1pt if +1-2% per 10k rows, 3pts if +5-10%, 5pts if >15%
- **Competitors' data access:** 5pts if exclusive, 3pts if they can access similar data with effort, 1pt if identical data available
- **Time to irreplaceability:** 1pt if <6mo, 3pts if 6-12mo, 5pts if >18mo

Average score < 2 = weak flywheel (will be copied). Score 2-3 = defensible for 12-18 months. Score 3.5+ = strong 24+ month advantage.

**Step 4.5: Map moat erosion timelines.** When does each moat type degrade?

- **Data Flywheel:** Degrades fast once competitors have equal data (12-18 months). Accelerates if they use better inference (3-6 months). Strengthens if you compound (keep collecting while they static).
- **Workflow Lock-in:** Slows at switching costs (18-36 months). Collapses if standard emerges (6 months). Hold if you keep deepening integration.
- **Context Depth:** Erodes steadily (24+ months) as open-source narrows gap. Accelerates if model architecture commoditizes (12 months). Sustainable if you keep inventing.
- **Trust:** Survives 5-10 years if consistent, dies overnight with 1 major incident. This is binary, not gradual.

For each moat, estimate: "In 18 months, will competitors match or exceed us?" If yes, start planning refresh now.

**Step 5: Audit quarterly.** For each planned feature, ask: does this strengthen the moat, or just keep parity? Features that don't strengthen moat are feature requests masquerading as strategy.

Use scorecard: "This feature improves flywheel data by ___%, deepens workflow lock-in by ___%, or hardens context depth by ___%. Or it just keeps parity."

## THE 7 POWERS (Hamilton Helmer)

The four moat types above are AI-specific. Helmer's 7 Powers is the underlying business strategy framework that describes durable competitive advantage across every industry. AI products live inside it — the four moat types map to specific Powers.

Use this section when the audience is a board, a strategy committee, or anyone who already speaks the 7 Powers vocabulary. The four AI moat types tell the practitioner story. The 7 Powers tell the strategy story. Both are real; pick the right one for the audience.

The 0.1% angle: **most AI products claim "data network effects" without having them.** Section 2 below is the diagnostic. Read it before you put "network effects" in your fundraising deck.

### Power 1: Scale Economies

**Definition:** Per-unit cost falls as volume rises. The bigger you get, the cheaper your unit economics — and the harder competitors can match your pricing without bleeding.

**AI-product example (real moat):** A foundation model provider where training costs amortize over billions of API calls. Anthropic, OpenAI, Google. Each new million-user cohort drops their cost-per-token. A new entrant trying to match price has no scale to amortize.

**AI-product example (vanity):** A vertical SaaS company saying "we have scale economies because our LLM provider gets cheaper at higher volume." That's not your scale economy — that's your vendor's. Your unit cost is whatever your vendor charges. You inherit no defensibility.

**Real vs vanity test:**
- Real: Your COGS curve flattens or declines as you scale. You can prove this in your unit economics.
- Vanity: Your vendor's COGS curve declines as they scale, and you sit downstream of it.

**When it's a real moat:** You operate the inference layer (own GPUs, custom silicon, fine-tuned models with high training cost amortization). You serve enough volume that your fixed costs spread thin.

**When it's vanity:** You're a wrapper. Your "scale economies" are just better volume discounts from your model provider.

### Power 2: Network Effects

**Definition:** The product gets more valuable to each user as more users join. Not the company more valuable — the product. This is where most AI teams confuse themselves.

**AI-product example (real moat):** A dev tool where each user's debugging traces become training data that improves code suggestions for all users. New user joins → their bug patterns flow in → next month's suggestions are better for everyone. The product itself improves with each user.

**AI-product example (vanity):** "We have data network effects because we collect a lot of usage data." No, you don't. Collecting data is data accumulation, not network effects. Network effects require that USERS get value from OTHER USERS' presence — not that the company gets value from the data.

**Real vs vanity diagnostic — the four-question filter:**

| Question | Real Network Effects | Data Accumulation Only |
|---|---|---|
| Does each new user make the product better for *existing* users? | Yes — within weeks | No — data sits in storage |
| Would users switch to a smaller competitor with better features? | Costly — they lose network value | Easy — there's no network value |
| Can a competitor with the same model and 1/10th the data match your output quality? | No — your data shape is uncopyable | Yes — they catch up with synthetic data |
| Do users pay a premium because of the network? | Yes — the network is the value | No — they pay for features |

If you fail 2+ of these, you don't have data network effects. You have data, which is good but not a moat. Most "AI data network effect" claims fail at least three.

**When it's a real moat:** Multi-tenant products where one user's annotations, edits, or corrections directly improve the model that serves all users. Marketplaces where AI matches buyers/sellers and each new participant tightens the matching graph.

**When it's vanity:** Single-tenant products where each customer's data improves only their own model instance. That's data lock-in (Power 4: Switching Costs), not network effects. Different moat, different defensibility, different valuation multiple.

### Power 3: Counter-Positioning

**Definition:** You adopt a business model that the incumbent cannot copy without harming their existing business. The incumbent sees what you're doing, knows it works, and still can't follow because the cannibalization math doesn't work for them.

**AI-product example:** An AI legal tool that prices at $50/month flat for unlimited use. The incumbent (a $400/hour billable-hour law firm) cannot offer a comparable product without cratering their own pricing model. They watch you take market share and can't respond.

**The pattern in AI:** Free or commoditized AI from challengers vs. expensive expert services from incumbents. Builders selling AI agents that do what BPO firms charge $40/hour for, at $0.50/transaction. The BPO firm can't match the price without dismantling the labor arbitrage their entire business depends on.

**Real vs vanity test:**
- Real: The incumbent's response would damage their existing margin pool. There's a structural reason they can't follow.
- Vanity: "Our incumbent is slow." Slow isn't structural. Slow gets fixed when you become a real threat.

**When it's a real moat:** When the incumbent's pricing power, channel relationships, or services revenue would be cannibalized by adopting your model. The bigger their existing book, the harder it is for them to move.

**When it's vanity:** When you're just executing faster than a slow incumbent. They'll wake up. Speed isn't structural counter-positioning.

### Power 4: Switching Costs

**Definition:** Once a customer is on your product, the cost of switching to a competitor is high — financial, operational, or psychological. They stay because leaving is expensive.

**AI-product example (real moat):** An AI agent platform where the customer has built 50 custom workflows, trained the model on their internal data, integrated with their CRM/ERP/Slack, and trained their team on the interface. Switching means rebuilding all of that. Even if a competitor has a 30% better model, the switching cost is 6 months of disruption.

**AI-product example (vanity):** "We have switching costs because users would have to copy-paste their prompts to a new product." That's friction, not switching cost. A competent buyer can migrate prompts in an afternoon.

**Real vs vanity diagnostic:**

| Switching Cost Type | Real | Vanity |
|---|---|---|
| Data | Years of accumulated, model-specific corrections in your system | Generic conversation history easily exported |
| Workflow | Custom-built integrations with 5+ business systems | API key swap in their existing stack |
| Training | 200 employees trained on your interface, processes, and edge cases | Generic chat UI, similar to every other |
| Compliance | Auditor-signed-off deployment that took 9 months to certify | No compliance requirements |
| Fine-tuning | Custom model trained on their data, only useful in your platform | Off-the-shelf model with prompt customization |

The strongest AI switching costs combine 3+ of these. Single-dimension switching costs (just data, just workflows) get unstuck quickly when a competitor offers migration tooling.

**When it's a real moat:** Enterprise deployments with deep integration, custom fine-tuning, regulated compliance, and trained personnel. Switching is a multi-quarter project, not a weekend.

**When it's vanity:** Consumer or SMB tools where users can swap with a sign-up form. Your "switching cost" is brand familiarity, which isn't a moat.

### Power 5: Branding

**Definition:** Customers pay a premium for your product because of what your name signals — trust, quality, status, safety. The value attributed to the brand exceeds the functional difference.

**AI-product example (real moat):** Anthropic in regulated industries. Procurement teams at banks and hospitals will pay 30-50% more for Claude over an open-source equivalent because "Anthropic" signals safety posture, governance maturity, and enterprise-readiness. The functional model gap doesn't justify the price; the brand does.

**AI-product example (vanity):** "Our brand is strong because we have great Twitter engagement." That's awareness, not branding. Branding is willingness to pay a premium based on trust. Awareness without premium isn't a moat — it's a marketing line item.

**Real vs vanity test:**
- Real: Customers who have functionally equivalent alternatives still choose you and pay more. You can prove this in win rates and price realization.
- Vanity: Customers know your name. You're proud of it. Win rates and pricing don't reflect any premium.

**When it's a real moat in AI:** When the cost of getting it wrong is high — healthcare, finance, legal, defense. Buyers in these segments use brand as a risk-reduction shortcut. They'll pay more to buy from a name they can defend in front of their auditor or board.

**When it's vanity:** Consumer AI products where the buyer is also the user. Brand affects acquisition cost, not pricing power. Treat it as marketing efficiency, not strategic moat.

### Power 6: Cornered Resource

**Definition:** Preferential access to an asset that competitors can't get, or can only get at much higher cost. The asset itself is the moat.

**AI-product examples (real):**
- A medical AI company with exclusive access to 20 years of de-identified data from a major hospital system, locked under a multi-year contract that excludes competitors.
- A legal AI company that licensed every patent filing from a major law firm partnership for the next 10 years.
- A model provider with privileged access to a specific GPU cluster (e.g., a hyperscaler partnership with reserved capacity).
- An AI company whose founding team includes the person who literally invented the underlying technique. Their domain expertise is the cornered resource.

**AI-product example (vanity):** "We have a cornered resource: our team is amazing." Talent moves. Unless they're locked in by equity, partnership terms, or unique founder dynamics, your "cornered talent" is portable.

**Real vs vanity test:**
- Real: The resource is exclusive (contract, partnership, equity-locked talent), strategically essential to the product, and not replicable through capital alone.
- Vanity: "Best-in-class team," "great data," "deep relationships" — none of these are cornered unless they're contractually exclusive or structurally unique.

**When it's a real moat:** When you have a contract, license, or talent lock that materially advantages you for 3+ years and a competitor with $100M cannot replicate.

**When it's vanity:** When the "resource" is something a well-funded competitor can buy or hire — talent, partnerships, data, infrastructure. If money solves it, it's not cornered.

### Power 7: Process Power

**Definition:** Embedded organizational processes that produce a sustained quality, cost, or speed advantage — and that take competitors years to replicate even after they understand them.

**AI-product example (real moat):** Anthropic's RLHF + Constitutional AI training process. The recipe is partially public (papers, blog posts), but reproducing it requires the entire organizational stack: research culture, evaluation infrastructure, internal red-team capacity, alignment researchers who know which trade-offs matter. A competitor can read the papers and still fail because the process isn't in the papers — it's in the organization.

**AI-product example (vanity):** "Our process is faster product iteration." Faster iteration is execution, not process power. Process power requires that the process produces structurally better outputs in a way competitors cannot match even with more money.

**Real vs vanity test:**
- Real: A competitor with the same hires, same budget, and same playbook would still produce inferior output for 3+ years. The process is encoded in the organization, not the documentation.
- Vanity: "We move fast." Speed without process specificity isn't a moat — it's a temporary cultural advantage that decays as the company scales.

**The AI-specific version:** Eval infrastructure as process power. Teams that have invested 2+ years building proprietary eval suites, failure-mode taxonomies, and continuous improvement loops have process power. Teams that ship features and hope the model behaves don't. The eval discipline is the moat — and most competitors won't catch up because they don't believe it's the moat until they've already lost.

**When it's a real moat:** Mature AI organizations where eval, safety, model improvement, and customer learning loops are all interconnected and refined over years. New entrants can't spend their way past it.

**When it's vanity:** Early-stage products claiming "operational excellence" before they have the production scars to prove it.

### Mapping the 7 Powers to the Four AI Moat Types

The two frameworks aren't competing. They're at different altitudes.

| 7 Powers (Helmer) | AI Moat Type (this skill) | Best AI Example |
|---|---|---|
| Scale Economies | Cost moat (Phase 5 above) | Foundation model provider amortizing training |
| Network Effects | Data flywheel | Multi-tenant product where annotations improve model for all |
| Counter-positioning | (Cuts across — depends on incumbent) | AI agent priced 100x below incumbent BPO |
| Switching Costs | Workflow lock-in | Enterprise deployment with deep integration + custom fine-tuning |
| Branding | Trust | Anthropic in regulated industries |
| Cornered Resource | Context depth (when proprietary data) | Exclusive licensed dataset, locked talent |
| Process Power | Eval dataset moat + Harness moat | Mature eval discipline + proprietary improvement loop |

**The diagnostic that combines both:** Score yourself on each of the 7 Powers (Strong / Emerging / Absent). Map each Strong/Emerging Power to the AI moat type that produces it. If a Power is Strong but the underlying AI moat type is weak, your Power claim is fragile — you have the appearance of defensibility without the mechanism.

The reverse is also useful. If an AI moat type scores high but no Power maps to it, you're optimizing something that doesn't compound into long-term defensibility. Reframe.

## REALITY CHECK

- **RAG is not a moat; workflow around RAG might be.** "We have RAG" is a feature. "Our RAG is trained on exclusive customer data, embedded in their workflow, and improves with their queries" is a moat (data flywheel + lock-in).
- **Single moats are fragile.** Strongest products have 2+ moat types. Anthropic: context depth + trust + growing data flywheel. OpenAI: workflow lock-in + trust. Build with redundancy.
- **Moat decay accelerates.** Initial erosion is slow. Once it starts, collapse is fast. Budget for moat maintenance and refresh before you need it.
- **No moat, no strategy.** If you can't answer "why can't a competitor with the same model beat us?", you're competing on execution cost. That's not durable.
- **Buying a capability is not building a moat.** Acquiring the technology doesn't create the durable advantage. A large study of ~17,000 corporate transactions found that buying technology does not, on its own, produce innovation (◆). Treat "we can just acquire it" as buying parity, not building a moat — the moat is what you compound *after* the purchase, not the purchase itself. *(Source: "3 Ways to Rethink Your Build-or-Buy Strategy," Srivastava, HBR, 9 Jun 2026.)*
- **Not all data is a moat — only the rare, hard cases over costly judgment.** General models master the *common* cases fast. The part a rival can't copy is the pile of unusual, infrequent, expensive-to-get-wrong situations — the "long tail" (the many rare cases that each occur infrequently but together are common). The test you can actually check: does your data cover those rare hard cases, or only the common, easily-scraped ones? If only the common ones, the advantage is already slipping. In one field-service dataset (Bluon, HVAC repair), about a third of real issues were oddballs that fit no common topic, and 27 of 59 topics held fewer than 300 examples each — that thin, hard slice is where the advantage lives, not the common third a model already handles (◆; [VERIFY] the 135,000-call base — one Bluon page says "150,000 from 40 technicians"; author holds equity in Bluon, note the conflict wherever cited). *(Source: "AI's Impact on SaaS Will Be Uneven," Stanton, HBR, 27 May 2026.)*
- **A data moat the customer can *feel* taxes its own trust premium.** When scoring a data advantage, add a question the volume/freshness/exclusivity checks miss: *does the value visibly depend on harvesting the user's own data?* If yes, discount the moat — customers who sense high data dependence discount your trust claims, eroding the very patronage the data was meant to compound. The data moat and the trust moat can pull against each other; the strongest position is a data advantage the customer doesn't experience as "they're mining me." *When wrong:* the tax only bites where the customer perceives the dependence AND has an exit — under real lock-in, or where the data use is invisible, it doesn't fire. *(Source: "Data Privacy Is a Growth Strategy," HBR, 2026; moderator ◆ [Journal of Marketing 2025](https://journals.sagepub.com/doi/10.1177/00222429251367342).)*
- **Score data *liquidity*, not just data volume.** Readiness-to-use is a scoreable input the volume/exclusivity checks miss: an incumbent's agent ships faster than a startup's on identical model access because its data is already clean, reusable, and validated. *When wrong:* liquid data is a moat only if it covers the rare, hard cases (see the precision test above) and isn't cheaply scrape-able — high liquidity over commodity data is a fast anti-moat, not a moat. *(Source: "Data Transformation Is the CEO's Business," MIT Sloan Management Review, 21 May 2026 — Caterpillar; ◆ directional.)*
- **Sharper still — score data *vintage*, not just liquidity.** Liquidity is how ready-to-use the data is; vintage is how far back it accumulated. A second independent case (Lenovo, electronics manufacturing) makes Caterpillar's point harder: the moat is behavioral history *time-indexed to your own operation* — supplier under-commitment patterns, two decades of failure data, customer order dynamics. A competitor with a better model still can't backfill it, because time can't be bought back. The most falsifiable form of the data-moat question: "how many years would a rival need to reproduce this history, even with a better model?" *When wrong:* vintage over commodity — scrape-able data is a fake moat, and the years count only if they cover the rare, hard cases. *(Second confirming case: Handfield, HBR, 27 May 2026 — ◆ directional, independent academic. Promotes the Q2-14 data-liquidity finding to a 2-for-2 cross-industry pattern.)*

## QUALITY GATE

- [ ] Core value engine identified (not just the feature)
- [ ] Moat type classified with specific evidence for which type applies
- [ ] Validation questions answered for the claimed moat type
- [ ] Decay timeline estimated with assumptions named
- [ ] Moat-building features defined separately from feature-building features

## Harness Moat

Your agent harness (orchestration, context management, eval pipeline, tool integration) IS a moat. When competitors can access the same models, the harness — how you orchestrate, evaluate, and improve — becomes the differentiator.

### What Is a Harness Moat?

A harness moat is the system design that coordinates:
- **Orchestration:** How agents route work between tools, memory, and decision points
- **Context management:** Which information flows to each decision and in what order
- **Evaluation pipeline:** How you measure and improve each step
- **Tool integration:** Which APIs, tools, and external systems are woven in
- **Prompt architecture:** System prompts, chain-of-thought structure, reasoning patterns

### Examples

**Anthropic's Planner/Generator/Evaluator harness:**
- Three-agent architecture: first agent plans, second generates, third evaluates
- Quality comes from orchestration, not the base model alone
- Competitors see the outputs but can't reverse-engineer the harness without weeks of experimentation

**Google Maps routing harness:**
- Not the model; the real-time traffic integration + historical patterns + ML
- How they blend live signals, historical data, and current ETA is the harness

**Stripe's automation harness:**
- Not fraud detection alone; the pipeline that routes transactions, applies rules, updates in real-time

### Harness Moat Strength Factors

- **Uniqueness:** How many months of R&D would a competitor need to build an equivalent harness? <1 month = weak, 6+ months = strong
- **Measurability:** Can you prove the harness works better than simpler approaches? If yes, competitor can replicate. If no, you can't defend it.
- **Adaptability:** If base models change, does your harness still work? Adaptable = stronger (survives model upgrades)

### Decay Timeline

Harness moats decay in 24+ months as competitors experiment. But they're slow to copy — most teams are optimizing models, not orchestration. Accelerates decay if you publish the architecture.

## Eval Dataset Moat

Your curated evaluation datasets — built from thousands of production failures, edge cases, and domain-specific examples — are proprietary knowledge. A competitor with the same model but without your eval dataset ships a worse product.

### What Makes an Eval Dataset a Moat?

- **Domain specificity:** General eval datasets (MT-Bench, MMLU) are public. Your domain-specific dataset from 2 years of production failures is not.
- **Edge case coverage:** Your dataset captures corner cases competitors don't know exist yet.
- **Refresh rate:** If you update quarterly from production, competitors are always playing catch-up.
- **Size and signal quality:** 10,000 curated cases with gold labels > 100,000 noisy cases.

### Example

Two medical AI products using the same base model:
- Product A: 2,000 domain-specific eval cases covering rare diseases, drug interactions, edge cases from 5 years of deployment
- Product B: 500 public benchmark cases + synthetic data

Product A ships safer, more accurate because it's optimized for cases that actually happen. Product B is optimized for cases in public benchmarks.

### Eval Dataset Moat Strength Factors

- **Size:** <1,000 cases = weak moat. 5,000+ = strong, especially if domain-specific.
- **Domain specificity:** Generic cases = easily replicated. Domain-specific cases = hard to build without time.
- **Refresh rate:** Static dataset = moat erodes quarterly. Updated from production = moat strengthens quarterly.
- **Gold label coverage:** If 80%+ have human review, stronger. If 80% are automated labels, weaker.

### Decay Timeline

Eval moats decay in 12-18 months as competitors build their own datasets. Accelerates if you publish your eval cases (don't). Sustains if you keep growing from production.

## Context Engineering Moat

How you assemble context (retrieval strategy, prompt architecture, tool selection, Constitutional AI principles) is hard to reverse-engineer from API responses.

### What Is Context Engineering?

Context engineering is:
- **Retrieval strategy:** Which data is fetched, in what order, with what priority?
- **Prompt architecture:** System prompt, context window usage, chain-of-thought structure
- **Tool selection:** Which APIs to call, when, and in what sequence
- **Constitutional AI principles:** Which values/constraints shape the agent's reasoning
- **Filtering and ranking:** Which results are surfaced vs. hidden

### Examples

**Competitors see this (your API output):**
```
Query: "Should I refinance?"
Output: "Yes, if your interest rate drops below 3.5%..."
```

**Competitors don't see this (your context engineering):**
- Which financial data you fetched (rates, taxes, credit score impact)
- In what order you presented it (recent > historical)
- How you weighted factors (interest rate > closing costs > timeline)
- Which Constitutional principles you applied (conservative financial advice, transparency on risks)
- Which tools you called (rate API, tax calculator, credit simulator)

### Context Engineering Moat Strength Factors

- **Complexity:** Simple prompt + standard tools = weak. Complex retrieval + proprietary ranking = strong.
- **Reverse-engineering difficulty:** If a competitor seeing your outputs can guess your prompts in 1 week, weak moat. If it takes 3+ months of experimentation, strong.
- **Observability:** If you publish your prompt, it's not a moat. If you keep it secret, moat is stronger (but harder to defend if employees leave).

### Decay Timeline

Context moats decay in 24+ months as open-source LLMs improve and standard approaches solidify. Accelerates if you publish your prompts or if a competitor copies by hiring your employees. Sustains if you keep innovating on retrieval and ranking.

## Model-Agnostic Moat vs Model-Dependent Moat

A critical distinction: some moats survive model upgrades; others don't.

### Model-Dependent Moats (Fragile)

- **Fine-tuned models:** Value = base model improvement delta. When base model catches up, delta shrinks. Moat loses 50% value in 6-12 months.
- **Proprietary training data (for fine-tuning):** Value = model quality gained. As public data improves, marginal value of your proprietary data shrinks.
- **Architecture innovations:** Value = novel architecture edge. When competitors copy or base models implement it, delta erodes in 3-6 months.

**Example:** You fine-tuned GPT-3.5 on domain data and shipped 18 months ago. GPT-4 launched. Your fine-tune's relative advantage shrinks; you're now racing to fine-tune GPT-4.

### Model-Agnostic Moats (Resilient)

- **Harness:** Still valuable on GPT-4, Claude-next, or open-source models. Works with any base model.
- **Eval datasets:** Even more valuable as models improve; you're testing on harder cases.
- **Workflow integration:** Works with any model you swap in.
- **Context engineering:** Portable to new models.
- **Data flywheel:** Still compounds; data quality improves with model upgrades.

**Example:** Your eval dataset moat with GPT-3.5. When GPT-4 arrives, you evaluate both. You optimize harness and context for GPT-4. Your moat survives and strengthens.

### Strategic Implication

**Prefer model-agnostic moats.** When the next model arrives in 6 months and is 30% better, you want defensibility that doesn't depend on fine-tuning or training. Build harness, evals, context, and data flywheels. These survive model upgrades. Fine-tuning and proprietary training data are temporary advantages.

## Two 2026 Ways a "Moat" Can Be Fake

Two failure modes surfaced in mid-2026 research. Each one looks like a moat and isn't. Run these checks whenever this skill has just identified a data/feedback-loop moat or a customer-relationship moat.

### 1. The anti-moat loop — a feedback loop on public data erases your edge

A data or feedback-loop moat has a condition the moat literature usually skips: the loop's *inputs* must be yours alone. Run the same "gets better as you use it" loop (a *compounding feedback loop* — a system that improves itself from the data its own use generates) on public signals every competitor's platform also takes in — competitor prices, web traffic, weather, public inventory — and the loop pushes you toward the industry average, not ahead of it. The faster the loop, the faster you land on the same answer as everyone else. "Gets better as you use it" and "turns into a commodity" are the same machine pointed at different fuel.

**The check:** Are the inputs to this loop yours alone, or public signals every rival also takes in? If the honest answer is "mostly public," it isn't a moat — it's an *anti-moat loop* that erases what made you different.

Evidence: in German gas-station markets, margins rose ~28% only when *both* competing stations ran the same pricing algorithm on the same shared signals; when only one did, there was no rise (✅ peer-reviewed — Assad, Clark, Ershov & Xu, *Journal of Political Economy* 2024, DOI [10.1086/726906](https://www.journals.uchicago.edu/doi/10.1086/726906)). Everyone landing on the same answer needs both sides running the same loop on the same fuel — which is exactly the line between an advantage and an anti-advantage.

The first cheap fix is never a new vendor; it's feeding in one signal only you can see (behavior from your own channels, long-term relationship history, frontline operational data), plus naming one goal the off-the-shelf tool would never optimize for.

*When this over-warns:* in a thin-margin commodity market, landing on the same answer can be the profit-maximizing move, and being deliberately different a luxury that leaves money on the table. Inputs being yours alone is necessary but not sufficient — a private signal that doesn't change the decision isn't an advantage either.
*(Source: "Beware the Agentic Convergence Trap," van Esch, Cui & Black, HBR, 13 May 2026.)*

### 2. The agent-in-the-middle squeeze — a relationship moat can fail on two fronts

Once an AI assistant sits between your brand and the buyer (a person tells the assistant what they want and it does the searching and buying), a customer relationship you thought was safe has two separate ways to fail, and surviving one doesn't save you from the other:

- **The persuasion front — where your brand convinces a person.** The assistant answers in a few sentences and cites two or three sources; the human never lands on your page. Your positioning and emotional pull never fire, because no human is reading. Getting seen stops being about ranking high and becomes about being *quoted* — you have to be the source the AI trusts enough to cite.
- **The choice front — where the buying decision is made.** The assistant carries out the person's instruction ("a mattress under $800 that ships by Friday") and buys against those rules. It doesn't feel your brand. A relationship that wins the citation can still lose the sale, because what earns a citation isn't what wins an assistant's purchase.

The only lasting defenses are structural: own the assistant, own the data the assistant needs to decide, or be the option so clearly trusted the AI can't route around you. A relationship that depends on a human reading or choosing is not safe from AI.

*When this over-warns:* where no assistant sits in the purchase (the buyer is a human on your site), the classic relationship moat still holds. This front is also early — in 2026 you are defending against a buyer that barely exists yet.
*(Source: "AI Is Upending Marketing on Two Fronts," Puntoni, HBR, 23 Feb 2026.)*

## OUTPUT FORMAT

When you assess a product's moat, use this structure:

```
## Moat Assessment: [Product Name]

Core Value Engine: [what makes this irreplaceable]
- Candidate moat type(s): [data flywheel / workflow lock-in / context depth / trust]
- Why competitors can't replicate in 6 months: [specific evidence]

Moat Types:
| Type | Score (1-5) | Evidence | Decay Timeline |
|------|-------------|----------|---|
| Data Flywheel | [1-5] | [annotation velocity %, data volume, refresh rate] | [months to commoditize] |
| Workflow Lock-in | [1-5] | [integration count, switching cost, embedded integrations] | [months to standardize] |
| Context Depth | [1-5] | [complexity, reverse-engineering difficulty, training time] | [months to replicate] |
| Trust | [1-5] | [safety track record, incidents, brand perception] | [fragile/resilient] |

Harness Moat: [orchestration, eval, context engineering]
- Architecture: [how agents orchestrate]
- Uniqueness: [months for competitor to build equivalent]
- Survivability: [does it work with model upgrades?]

Eval Dataset Moat: [size, domain specificity, refresh rate]
- Size: [number of curated cases]
- Domain specificity: [generic / moderately specific / highly specific]
- Refresh rate: [static / quarterly / continuous]
- Gold label %: [% with human review]
- Competitive advantage: [if competitor had same model but no dataset, how much worse?]

Model Dependency: [high/medium/low — how much value is lost if model changes]
- High: Value is in fine-tuning or proprietary training data
- Medium: Mix of model-dependent and model-agnostic moats
- Low: Moat survives model upgrades (harness, evals, context, workflows)

18-Month Projection: [will competitors match or exceed?]
- Best case: [assumptions where you maintain lead]
- Realistic case: [most likely scenario given competitor capabilities]
- Worst case: [if competitor executes well on every moat type]
- Probability of matching: [your estimate]

Moat Refresh Plan: [quarterly actions to maintain/deepen]
- Q1-Q2: [specific actions to strengthen moat]
- Q3-Q4: [specific actions to maintain lead]
- Contingency: [if competitor narrows gap, pivot plan]
```

## WHEN WRONG

- Early prototype phase where moat is premature (focus on desirability first)
- Internal tools or single-customer products where moat defensibility is irrelevant
- When used to justify shipping inferior product ("our moat is context depth so execution doesn't matter")
- When the moat analysis is being used to avoid building features customers want

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
