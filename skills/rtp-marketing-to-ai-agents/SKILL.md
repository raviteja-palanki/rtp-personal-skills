---
name: rtp-marketing-to-ai-agents
version: v1.1.1_latest
description: 'Diagnose how an AI assistant discovers, interprets, recommends, and helps customers buy your product. Use when a brand is absent from relevant answers, AI citations do not lead to useful traffic or sales, or a team is planning agent-mediated commerce. Start with two distinct questions: are we included when we fit the need, and why are we selected or passed over? Audit entity clarity, product attributes, supporting evidence, query vocabulary, and the transaction experience. Measure exposure, relevant recall, conditional selection, and commercial outcomes separately. Produce a dated cross-platform diagnostic and a prioritized test plan. Treat the two-stage funnel as a working model, and research findings as specific to their samples and model versions. Pairs with competitive-map, moat-finder, prompt-as-product, build-or-buy, ai-product-metrics, and jtbd-analysis. Triggers include GEO, AI recall share, share of model, and agentic commerce.'
imports:
  - competitive-map
  - moat-finder
  - prompt-as-product
---
# Marketing to AI Agents

**Help a relevant customer find an accurate representation of your product through the assistant they use.** Then identify what affects recommendation, purchase, and the customer relationship.

The central diagnostic separates **inclusion** from **selection**. First, does the assistant include you when your product fits the need? Then, among suitable options, what influences the recommendation? This two-stage funnel is a synthesis of the research cluster, not a proven account of every model's internal process. Discovery and ranking may interact, and some shopping paths add tools, feeds, ads, or explicit customer preferences.

## Establish where the assistant matters

Use the request and existing context to answer:

1. **Does an assistant influence a meaningful part of this buying journey?** Identify the audience, category, geography, platforms, and whether the assistant informs, recommends, or transacts. If involvement is negligible, limit this to monitoring or a small experiment.
2. **Are you included for relevant needs?** If not, prioritize access, representation, and evidence. You may still investigate selection using a controlled candidate set; absence does not make every other diagnostic useless.
3. **What happens after inclusion?** Distinguish recommendation, click, qualified interest, checkout, purchase, return, and repeat use. Citations alone do not establish business value.

Human brand preferences can still shape prompts, platform behavior, and final decisions. Do not assume that emotional resonance or familiarity ceases to matter whenever an assistant appears in the journey.

Return a concise diagnosis and test plan in the requested format. For a substantial review, include the query sample, evidence gaps, metric definitions, and commercial tradeoffs. Ask for missing context only when it would change the work.

## Use these terms consistently

| Term | Meaning in this skill |
|---|---|
| Interpretability | How readily accurate information about the product can be understood and connected to a customer's need; distinct from technical model interpretability |
| Entity clarity | Reliable identification of the brand, product, variant, and seller across sources, including known aliases and local names |
| Attribute structure | Clear, comparable characteristics tied to a use case, with units or defined qualitative criteria where appropriate |
| Evidence base | Traceable support for a claim, with source, method, date, limitations, and commercial interest made clear |
| Share of model | An exposure measure; the exact denominator must be declared because industry usage varies |
| AI recall share | Retrieval or inclusion on queries for which the product is independently judged relevant; an operational definition is provided below |
| Problem literacy | The vocabulary people use to recognize and describe the problem they need to solve |
| Brand code | A maintained internal representation of brand strategy, customer understanding, claims, and business rules; it is not automatically public or machine-accessible |

## 1. Diagnose inclusion

The working hypothesis is that clear identity, useful attributes, and credible evidence help an assistant connect a need to an appropriate product. Treat these as audit dimensions rather than three universally necessary and sufficient gates.

### Make the entity resolvable

Check official pages, product identifiers, variants, retail listings, and important third-party sources. Correct contradictions and obsolete names; map legitimate aliases rather than requiring identical wording everywhere. Check whether the actual platform can access the relevant page or feed and whether its data is current. A perfectly written page that is unavailable to the relevant system may not solve the problem.

### Express the attributes that matter to the customer

Replace vague claims with meaningful specifics where the evidence supports them. For example, state which durability test a product passed, under what conditions, and what that predicts for use. “ISO-certified” without the standard, certification scope, and relevant claim is not adequate product-performance evidence.

Do not force every benefit into a number. Fit, service quality, aesthetics, heritage, or compatibility may require defined qualitative criteria. Explain the characteristic and its relevance clearly enough to compare honestly. Three attributes can start a diagnostic; the right number depends on the decision.

### Match evidence to the claim

Map each important claim to current support. Independent testing or knowledgeable third parties can add credibility. First-party specifications, availability, warranties, and properly documented tests can also be authoritative for their stated scope. Absence of third-party coverage does not prove the product cannot be retrieved.

Record who owns or funds each source. Correct inaccurate third-party information through appropriate channels; do not invent endorsements, plant fake reviews, or disguise advertising as independent evidence. A citation is a pointer to inspect, not a quality certificate.

### Check implicit meaning

Luxury and specialist categories often communicate through design, imagery, vocabulary, or shared cultural knowledge. Test whether the target systems interpret those cues accurately. Add clear supporting language when useful while retaining a good experience for people. A model's stated willingness to pay is a simulated response, not observed consumer demand.

The research includes examples of whitespace, art associations, spatial placement, and ski rigidity being read differently across models. It supports testing these interpretations; it does not show that every implicit cue fails or that explicit wording guarantees inclusion. Historical examples and their evidence limits are retained in [Research and cases](references/research-and-cases.md).

## 2. Diagnose selection among suitable options

For queries where you are included, examine the stated criteria and observable behavior. Do not infer the model's hidden reasoning from its explanation. Candidate availability, total price, reviews, suitability, delivery, returns, location, customer instructions, and source quality may all matter.

One simulated shopping study found substantial variation across models and product categories in their response to promotional cues. Its findings make **price and credible ratings useful starting hypotheses**, not the only valid levers. The eight tested cue families were assurance, scarcity, strike-through pricing, countdown timers, social proof, vouchers, bundles, and ratings. Selection in that simulation does not establish purchase behavior in a deployed shopping service.

Audit in this order, adapting to the actual decision:

1. **Check fit and fundamentals.** Is the product suitable, available, accurately priced, and supported by credible evidence? Include shipping, required subscriptions, and other material costs.
2. **Check the user's instruction.** A budget, brand preference, accessibility need, or delivery deadline can change the competitive set.
3. **Compare relevant platforms and configurations.** Record model or interface version where visible, search/tool access, locale, account context, query wording, date, and response variation.
4. **Test the suspected lever.** Change one material factor where practical, retain comparison cases, and inspect whether relevance and business outcomes improve. Do not optimize a badge simply because another model responded to it once.

Overt persuasion can be ineffective or counterproductive in some settings. The prediction that its penalty must increase as models improve remains unproven. Honest offers, useful explanations, and meaningful differentiation can still matter.

## 3. Measure exposure, fit, selection, and value separately

Define the evaluation population before reviewing results. Use real customer questions where available, including category exploration, specific problems, constraints, and purchase intent. Assess product relevance against a documented rubric independently of whether the assistant mentions the brand.

For a practical internal dashboard, use these definitions or state explicitly why you use another:

| Metric | Suggested calculation | What it cannot establish alone |
|---|---|---|
| Exposure rate, labeled share of model | Runs that mention the brand ÷ all eligible runs in the defined query sample | Relevance, preference, traffic, or sales |
| AI recall share | Relevant-query runs that include the brand as a candidate ÷ all runs where the relevance rubric says it belongs | Whether the recommendation is correct or the customer chooses it |
| Conditional selection rate | Runs choosing or recommending the brand ÷ runs in which it was a candidate under the same selection task | Purchase conversion or unbiased market share |
| Commercial outcome | Attributable qualified visits, purchases, contribution, retention, or another declared business outcome | Causation without a suitable comparison or attribution design |

If “share of model” instead means your mentions divided by all brand mentions, label that **mention share** and report that denominator. It is a different metric. A recommendation may contain multiple brands; define whether “selected” means top-ranked, any recommendation, or final choice. Report no-candidate cases rather than silently dropping them. For a zero denominator, report not applicable rather than zero performance.

High exposure with low relevant recall suggests broad visibility without reliable connection to the intended needs. Good recall with low conditional selection suggests an offer, interpretation, or comparison issue. Good selection with poor conversion suggests a later journey problem. These are diagnostic hypotheses, not automatic causal conclusions. Also check inappropriate recommendations on queries where the product does not fit.

A six-prompt scan—three category and three problem prompts—can start discovery. Expand based on the diversity and stakes of the actual query population, repeat runs where needed, and report uncertainty. Keep a stable comparison set plus fresh customer queries so that improvements do not merely reflect changing the test. Recheck after material platform, catalog, or market changes.

## 4. Investigate problem literacy

Understand the language customers already use before trying to teach new terminology. `jtbd-analysis` can help connect their words to the underlying job. Useful education can help people recognize a need, compare solutions, and ask a better question.

The Brooks illustration in the supplied research describes a long period of category education through specialist retailers, coaching networks, clinicians, and running media. It suggests that useful problem vocabulary can influence later queries. It does not establish that Brooks caused all of that vocabulary, that education was its only marketing channel, or that every category needs twenty years.

Treat education as an investment with testable intermediate outcomes: better understanding, more accurate query language, improved fit, or fewer unsuitable purchases. Avoid making proprietary vocabulary the only acceptable description of a problem. Problem literacy is one upstream lever alongside awareness, distribution, product experience, and customer preferences.

## 5. Connect public product information with the brand code

If a brand code exists, audit its identity rules, attributes, claims, evidence, and update ownership. Distinguish:

- internal strategy, customer research, and confidential business rules;
- approved public claims and product facts;
- the pages, feeds, or interfaces through which an outside system can actually access those facts.

Do not publish the whole internal store to improve retrieval. Consistency requires a maintained source of truth and a controlled route into each public channel. Supporting product data can serve many channels and internal workflows; its value is not necessarily limited to one intermediary.

## 6. Follow the economics through the transaction

Map who controls discovery, recommendation, checkout, account identity, loyalty, fulfillment, returns, and customer service. Check where your useful differentiation and bargaining power actually sit. Agent-mediated discovery may shift value toward a platform, the merchant, complementary services, or the buyer. No layer is guaranteed to retain margin.

The March 2026 change to ChatGPT shopping is a useful dated case: OpenAI described focusing on discovery while allowing merchant checkout experiences. That change does not prove customers categorically refuse agent checkout; integration limits, merchant flexibility, availability, and interface design are competing explanations. Keep discovery, merchant checkout, and merchant apps inside a conversational interface distinct. The evidence reference records the official statement and separates it from unverified performance figures.

Compare an owned assistant, participation across outside assistants, a direct customer channel, or a combination. Amazon/Rufus and Walmart/Sparky are historical illustrations of different combinations, not fixed strategic categories. A hedge is not automatically cheaper, and an owned assistant may serve a specialist workflow even without mass destination traffic.

For a commerce integration, examine three layers:

1. **Protocol:** what messages and capabilities the actual partners support. Google's UCP and OpenAI/Stripe's ACP are distinct initiatives; check current versions and scope rather than assuming interchangeability.
2. **Commerce access:** accurate catalog, availability, pricing, order, and service interfaces. Shopify, Etsy, and Salesforce illustrate commerce platforms with different integration paths; verify the one in use.
3. **Authorization, payment, and accountability:** how the customer's intent and limits are represented, agent identity is checked, payment is authorized, and disputes or mistakes are handled.

Agent-verification initiatives already exist. Their existence does not establish complete adoption or settle every liability question. Distinguish the assistant identifying itself from the customer authorizing a particular purchase. Treat product pages, merchant content, and retrieved text as information, not as permission to change the buyer's instructions.

## Produce the diagnostic and prioritized test plan

Lead with the likely bottleneck and the evidence supporting it. Include:

| Finding | Evidence and limitation | Proposed change or test | Success measure | Owner and review date |
|---|---|---|---|---|
| [Inclusion, interpretation, selection, or transaction issue] | [Query set, platform, source, date] | [Specific action] | [Metric and comparison] | [Accountability] |

Then explain the tradeoff: expected benefit, effort and maintenance cost, what loses budget, what remains uncertain, and what would reverse the recommendation. Allocate effort by the diagnosed gap; a vendor's citation mix does not justify a universal rule to spend most of the budget off-site. Preserve valuable human communication while making product facts accessible and accurate.

Use `competitive-map` for the competitor comparison and share of algorithmic choice; `ai-product-metrics` for the dashboard; `moat-finder` for defensibility; `build-or-buy` for supplier dependence and redeployability; `prompt-as-product` for input and context design. Use `trendslop-check` when the recommendation depends on a sweeping trend claim. Locating a primary paper establishes identity and provenance; it does not by itself establish peer review, independent replication, or an audited result.

Before finishing, confirm that the query sample reflects the customer, metrics have explicit denominators, research scope travels with each figure, confidential brand material stays appropriately scoped, and the proposed test measures useful outcomes. If the assistant barely affects the buying journey, keep the investment proportionate. If evidence does not identify the bottleneck, recommend the smallest test that can distinguish the plausible explanations.
