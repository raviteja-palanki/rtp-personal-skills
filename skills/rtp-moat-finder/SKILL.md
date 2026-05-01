---
name: rtp-moat-finder
description: "Four moat types: data flywheel, workflow lock-in, context depth, trust. Defend at 18 months when models commoditize. Use when: strategy, moat vs parity, defensibility. Triggers: 'competitive advantage', 'defensibility', 'moat'"
imports: [bias-spotter, determinism-compass]
---

# Moat Finder

## DEPTH DECISION

**Go deep if:** You're evaluating long-term defensibility (18+ months), designing features specifically to build moat, or assessing if you have a real moat vs. temporary feature advantage.

**Skim to diagnostic questions if:** You want a quick audit of your planned moat or competitive advantage.

**Skip if:** Pre-market-fit phase where feature velocity matters more than defensibility, or if you're in a single-customer/bespoke context.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will confuse impressive with defensible. The bias is **recency bias** — a clever prompt or RLHF trick feels like a moat because it's novel. Three months later every competitor uses the same approach. You're left racing on execution cost, which is not a durable strategy.

In AI, moats are invisible until they work or fail. A proprietary dataset, a fine-tuned model, deep workflow integration — all can look defensible on launch day and become commodities by month 18. Teams that win know their moat *before* they start building. Teams that don't spend 18 months optimizing something someone else will copy in weeks.

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

**AI-product example (real moat):** Anthropic's RLHF + Constitutional AI training process. The recipe is partially public (papers, blog posts), but reproducing it requires the entire organizational stack: research culture, evaluation infrastructure, internal falsification capacity, alignment researchers who know which trade-offs matter. A competitor can read the papers and still fail because the process isn't in the papers — it's in the organization.

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
