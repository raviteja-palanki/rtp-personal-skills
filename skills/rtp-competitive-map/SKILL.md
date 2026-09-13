---
name: competitive-map
version: v1.2.1_latest
description: 'Compare an AI product with the alternatives its customers actually consider, including manual work, existing tools, in-house systems, and doing nothing new. Look beyond feature parity to task quality, safety, privacy, full unit economics, switching costs, trust, distribution, and the durability of each advantage. Use observed evidence and labeled estimates; model choice, certifications, low cost, and an AI-native label do not establish a moat by themselves. Add agent-mediated discovery and purchase measures where relevant. Produce a competitive map, positioning choices, and an evidence-backed battlecard when needed. Useful before or after product-market fit, with depth matched to the decision. Pairs with moat-finder, strategy-canvas, cost-model, signal-scanner, and marketing-to-ai-agents. Triggers: competitive analysis, competitive positioning, competitor map, battlecard.'
imports:
  - moat-finder
  - first-principles
---

# Competitive map for AI products

Identify which alternatives customers would choose, where your product creates better value, and what could sustain or erase that advantage. The deliverable should support a concrete decision: a segment to pursue, a threat to respond to, a capability to invest in, or a claim the sales team can substantiate.

Similar interfaces can hide different quality, costs, data rights, controls, and operating capabilities. Those differences matter alongside features, usability, distribution, and customer fit. A model lead may be temporary or durable; neither a fixed expiry date nor a product's “AI-native” label answers that question.

## Start with the customer and the decision

Define the task, buyer/user, segment, geography, deployment constraints, and time horizon. Use known context and identify consequential gaps. Replace vague arenas such as “AI for knowledge workers” with the particular work and requirements customers pay to satisfy. Avoid invented measures such as “98% privacy compliance.”

Include the alternatives that affect this decision: direct products, adjacent tools, manual services, internal builds, rules-based workflows, and the status quo. Five to eight rivals can be manageable for a substantial review, but do not invent competitors to fill a quota. Pre-PMF products still have alternatives; use a lightweight map to test assumptions about them.

For a feature comparison, keep the relevant feature evidence and use `first-principles` to test whether the difference matters. Use a deeper map when economics, dependencies, trust, or durability determine the strategy. Stop expanding the analysis when the next decision has enough evidence; an exhaustive map is rarely necessary.

## Keep evidence visible

For every material claim record source, date, product tier/configuration, observed fact, inference, and uncertainty. Distinguish vendor claims, your own tests, customer reports, estimates, and rumors. “Not publicly documented” is different from “absent.”

Benchmark comparable workflows with the same task constraints and appropriate data permissions. Include representative and consequential edge cases, relevant repetition, version/settings, and outcome scoring. Twenty to thirty queries can reveal issues in an exploratory screen; they do not establish broad superiority or rare-failure reliability. Report coverage and uncertainty.

Unknown internals remain unknown. Public price is not production cost; a model named in marketing may be only one part of a routed system. Respect lawful access and confidentiality when gathering evidence. A customer report can prompt investigation without becoming a public accusation or a verified claim.

## Compare operating capability without a maturity shortcut

Review the following dimensions using anchored descriptions. An optional 1–4 scale can summarize absent/limited/deployed/validated capability **when the evidence supports that classification**; keep unknown separate and define the anchors for each dimension.

Model quality, failure mitigation, latency, cost structure, evaluation/monitoring, safety, data learning, trust design, applicable regulatory/procurement readiness, model flexibility, infrastructure/deployment fit, and moat clarity are useful prompts. They are related dimensions, not independent scientific measures.

Do not average them into an “AI-native >3.0” verdict. A proprietary fine-tune, multiple models, or on-premises deployment may help one task and add cost or risk to another. Hosted APIs and a well-integrated AI feature can be strong product choices. Show the specific capability, evidence, and customer value instead of treating complexity as maturity.

## Examine the dimensions that could change the decision

### Task capability and architecture

Compare quality, completeness, latency, reliability, supported actions, and integration under the buyer's real workload. Identify the model, data, retrieval, orchestration, or UX contribution only when supported. Separate measured outcomes from explanations for them.

Test the durability of a lead against plausible model upgrades, replication, substitutes, and changing customer requirements. A shared foundation-model upgrade does not improve every product equally: integration, routing, costs, data access, and release choices differ. Use dated scenarios rather than assuming all advantages expire in three to six months.

### Safety and trustworthiness

Compare relevant failure prevention, appropriate refusal, uncertainty communication, recovery, incident handling, and evidence of consistent operation. More refusals do not automatically mean more safety. Safety can be essential even where customers do not pay a visible premium; any commercial premium needs buyer evidence.

Separate the harm controls a product needs from the features buyers notice and the advantages rivals cannot easily copy. Use `safety-as-moat` and `moat-finder` when those distinctions are central.

### Data rights and privacy

Compare collection, permitted use, training policy, retention/deletion, access isolation, deployment options, subprocessors, and contractual commitments. Verify the applicable plan and settings.

Treat a SOC 2 report, a legal obligation, and a government authorization as different forms of evidence with different scopes. SOC 2 is not an AI-safety certification or a universal license to sell to regulated customers; “HIPAA-ready” and “FedRAMP in progress” do not establish compliance or authorization. Identify actual buyer requirements before estimating which part of the market is accessible.

### Full unit economics

Estimate cost on a consistent unit, period, workload, quality target, and service scope. Include input/output billing, context, cache behavior, retries, tools, serving infrastructure, review, support, and relevant fixed allocations. Use `cost-model` and `token-economics` for the calculation.

Build a range where competitor internals are unavailable. Pricing divided by assumed users is a revenue or price estimate, not a cost estimate. Separate funding/runway from unit costs and profitability.

Lower costs can support lower prices, higher margins, or reinvestment; they do not force a rival to remain in a low-price market. A costlier product can win where its additional value justifies its price. Market access also depends on capability, trust, distribution, contracts, willingness to pay, and service costs. See the [worked scenarios](CONCEPT.md).

### Switching costs and portability

Assess the actual effort, disruption, risk, and lost value from moving: data history, integrations, learned configuration, workflow change, contracts, training, and export/import quality. Distinguish genuine ongoing value from avoidable lock-in.

Estimate migration cost and recovery time with an explicit basis. Do not assume a universal 30–50% price premium, indefinite retention, or a data flywheel from repeated usage. Useful learning requires rights, valid feedback, effective improvement, and benefits that rivals cannot cheaply reproduce.

### Trust, brand, and relationships

Compare buyer recognition, relevant references, sentiment, demonstrated performance, relationship depth, incident history, and verified procurement evidence. These signals can overlap, so avoid counting the same evidence as several independent advantages.

Identify events that could undermine a claim and the competitor's capacity to respond. Trust can erode quickly or recover; there is no general “three years lost in three months” rule. A familiar brand or a safety-oriented founding story does not prove superior operation.

### Agent-mediated discovery and choice

Add this dimension when software agents influence the relevant buyer's discovery, shortlist, recommendation, or purchase. Measure these stages separately.

Define **share of algorithmic choice** for a bounded observation set: selections of your product divided by eligible observed agent-mediated choices, with the agent/platform, task, category, period, sampling method, and purchase-versus-recommendation distinction stated. A synthetic shopping test is a test-set result, not market share. Mark real-market coverage unknown when platform data is unavailable.

Track inputs—attribute completeness, verified claims, inventory/price freshness, accessibility, and interface performance—separately from the selection outcome. Human awareness and algorithmic choice can differ, but agents may also use brand preferences, reviews, reputation, and unstructured web content. Structured data is valuable without being the only possible input.

Assess platform concentration, discovery/payment rules, portability, direct-channel strength, alternatives, fees, and available contractual or regulatory recourse. Direct access to customers can reduce dependence; it is not the only possible influence or remedy, and future tolls are a scenario rather than a certainty. Product data can create operating value beyond preventing exclusion.

Use `marketing-to-ai-agents` for channel mechanics and `build-or-buy` for dependency choices. The [evidence note](references/competitive-evidence.md) qualifies the HBR algorithmic-shopping examples and the Novel Insights interpretation.

## Synthesize the position

Use these three views when they help the decision:

| View | Question to answer | How to keep it interpretable |
|---|---|---|
| Capability and cost | Who delivers the required outcome at a viable cost? | Define the task-quality and full-cost units; show ranges where estimates are weak |
| Trust and price | Which buyers value the assurance offered at this price? | Define trust evidence and a comparable price/service scope; do not equate high price with regulated-market fit |
| Moat and runway | What could preserve or erode each advantage, and when? | Use a categorical moat-by-scenario table; if drawing a 2×2, use defensibility strength versus estimated durability, not a numerical axis called “moat type” |

Choose meaningful boundaries for a 2×2 rather than putting arbitrary scores at the center. These views support a judgment; their visual intersection does not mathematically prove a defensible market. State the strongest candidate position, credible alternatives, evidence gaps, and the event that would change the choice.

## Develop positioning from buyer alternatives

April Dunford's [five-component method](https://www.aprildunford.com/post/a-quickstart-guide-to-positioning) connects:

1. **Alternatives:** what buyers would actually use without this offering.
2. **Differentiated capabilities:** the relevant differences against those alternatives.
3. **Value:** the outcome those differences enable, supported by evidence.
4. **Best-fit customers:** who most values that outcome and can adopt the product.
5. **Category:** the context that makes this value understandable without misleading expectations.

Work through the relationships before writing a statement. A fill-in-the-blanks sentence is a summary, not the discovery method. A currently unique feature can still be easy to copy; current uniqueness and long-term defensibility are separate. A half-point difference on an internal score does not settle either question.

Test candidate positioning with the relevant buyer and against actual alternatives. Do not automatically narrow a category until you can claim to lead it, dismiss a general-purpose assistant, or assume the smallest segment is best. Consider value, adoption constraints, commercial opportunity, and evidence.

An optional summary is: “For [customer] facing [problem], [product] provides [value] through [relevant difference], compared with [actual alternative].” Use natural language suitable for the audience, with no unsupported exclusivity or outcome promise.

## Build a useful battlecard when sales needs one

Keep one dated, source-linked card per relevant competitor. Product marketing or the assigned owner maintains it. Use six sections:

1. **Positioning snapshot:** the buyer, value, and reason to consider us.
2. **Supported strengths:** a few customer-relevant advantages with evidence and comparison scope.
3. **Honest limitations:** where the rival is stronger, the practical implication, and a valid mitigation or fit boundary. Do not force a positive spin when none exists.
4. **Objection handling:** real buyer questions and substantiated answers. Avoid invented claims about what the rival's salespeople say.
5. **Proof points:** artifacts the team can share lawfully, such as documented results, comparable evaluations, references, or scoped cost analyses.
6. **Talk track:** two or three natural sentences a representative can say accurately, plus qualification when needed.

Do not answer “they have more experience” with an unsupported claim that they are obsolete. Evidence may show the buyer is better served by the rival; the card should help qualify the opportunity honestly.

Refresh after material changes in product, price, evidence, incidents, buyer priorities, or channel rules. A quarterly review can be a useful backstop. Check actual use and feedback; an unused section may reflect relevance, training, access, or workflow rather than incorrect content.

## Review and handoff

- The arena and alternatives reflect the buyer's decision, including the status quo where relevant.
- Material claims have dates, sources, scope, and uncertainty; unknowns have not been scored as failures.
- Capability, economics, safety/privacy, switching, trust, and relevant distribution evidence are compared on a fair basis.
- Model choice and procurement claims are verified or clearly labeled as unknown/inferred.
- The three synthesis views support the conclusion without pretending to prove it.
- Positioning and any battlecard use defensible claims and preserve real limitations.
- The next action, owner, review trigger, and largest unresolved risk are clear.

Hand the chosen position and conditional bets to `strategy-canvas`, your own durability questions to `moat-finder`, and monitoring triggers to `signal-scanner`. `gossip-mode` can supply informal leads between reviews; preserve provenance and verify before changing consequential claims. Use `trust-under-fog` to communicate uncertainty appropriately.

Explain the trade-off between present customer value and investment in a potentially durable advantage. Price competition may be a valid strategy when economics and value support it; do not use this map to rationalize an unsupported price war or to avoid a needed product decision. Include a visual only where it improves comparison.
