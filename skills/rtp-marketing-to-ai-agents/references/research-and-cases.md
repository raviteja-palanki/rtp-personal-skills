# Research and cases

Use this note when a recommendation depends on a study or historical example. The main skill's two-stage funnel combines related ideas; it was not tested as a complete causal model in one study. Multiple articles with overlapping authors, datasets, or vendor interests are not automatically independent replications.

## Inclusion and interpretation

**Source in the supplied skill:** Gale, Cian, and Wathieu, “How to Get AI to Surface Your Brand,” HBR, 29 June 2026. The [publisher's listing](https://store.hbr.org/product/how-to-get-ai-to-surface-your-brand/H09828) identifies those authors and the article. The supplied skill reports 716 brands, more than 1,000 mentions, 15 retail categories, and comparisons across GPT-4o, Claude, and Gemini. The detailed figures below remain article-reported; this revision did not independently reproduce that study.

| Reported observation | Figure retained from the supplied skill | Interpretation limit |
|---|---:|---|
| Brands appearing across all three platforms | 8.4% | Sample-specific overlap, not proof that one platform says nothing about another |
| Multi-platform brands described differently across systems | 55% | Depends on the framing rubric and denominator |
| Additional mentions for exploratory versus goal-directed queries | 95% more | Relative difference in that query sample, not a universal traffic multiplier |
| Brands appearing in both query types | About 11% | Does not establish what every customer asks |
| Positive sentiment among mentions | 78.7% | Conditional on inclusion; does not establish fairness, indifference to tone, or the absence of harmful misrepresentation |

The supplied examples name Disney, Starbucks, McDonald's, Netflix, IBM, and Intel as absent from that query set; Toyota, Coca-Cola, and Pepsi as represented through products or variants; and Brooks as more visible than Nike in the comparison. Preserve **“in that query set.”** These examples do not show that narrative brands become universally invisible or that representation alone caused the differences.

**Corrected source match.** The earlier skill said arXiv 2606.23057 corroborated this study's design and scale. It does not. [That paper](https://arxiv.org/abs/2606.23057), submitted 22 June 2026, is by Dmitrij Żatuchin and reports 3,750 responses, 50 brands, five industries, 250 queries, and a different model set. It is a separate investigation. Its presence cannot upgrade the provenance of the 716-brand figures.

## Implicit luxury cues

**Source in the supplied skill:** Dubois, Hess, Dawson, and Jaiswal, HBR, 22 June 2026. [INSEAD's institutional summary](https://www.insead.edu/faculty-research/publications/journal-articles/llms-misunderstand-luxury-brands-heres-how-optimize) confirms the investigation of explicit and implicit luxury cues and recommends testing model-specific interpretations.

The supplied skill reports 150 samples per stimulus across three models in one experiment and 5,400 simulated willingness-to-pay evaluations in another. These are retained as article-reported design details, not a newly reproduced experiment. Its examples include physical placement, association with art, minimalist whitespace, and slender proportions being interpreted unexpectedly; Ferrari versus BMW prestige; Ferrari paired with Van Gogh producing different responses across models; Porsche losing and Mercedes gaining stated value in a luxury context; and a model treating Atomic ski rigidity negatively.

These examples motivate an interpretation audit. Reusing stimuli from human studies helps comparison, but replacing human participants with model responses changes more than an isolated “reasoning” variable. Prompt, modality, model version, sampling, and evaluation context can matter. Simulated willingness to pay is not actual spending. Do not generalize from a model's response to what every system or buyer values.

The same article relayed a Jellyfish proprietary U.S. beauty analysis: brand sites 20% of citations, commerce sites 24%, news 21%, specialist blogs 15%, and other sources 20%. The original skill already marked the split **[VERIFY]**. It remains unreplicated here. Even if correct for that sample, a citation share is not a budget-allocation rule, a measure of causal influence, or proof that 80% of useful work lies outside owned channels. Investigate the sources your customers' assistants actually use.

## Promotional cues and simulated selection

**Sources in the supplied skill:** Sabbah and Acar, HBR, May 2026, and [“Marketing to Machines: How AI Models Respond to Promotional Cues,” SSRN 6406639](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6406639), written 13 March 2026. The primary abstract identifies the authors and describes a controlled simulation using four models and four categories, with heterogeneous responses to promotional cues. The full text was unavailable during this revision; locating its record is not confirmation of peer review or an independent audit.

The supplied skill reports 16,000 choice situations from four models × four categories × 1,000 rounds. It identifies ratings as the most consistent cue and discusses price effects, unstable other cues, and penalties for overt persuasion in some reasoning-model settings. Retain the category and model limits. A mechanism count in the earlier prose was ambiguous: price is not identical to one of the eight badge families, so “only two worked and the other six failed” is not a clean classification. Report the actual intervention and outcome when using the paper.

Its eight cue families are assurance, countdowns, strike-through prices, scarcity, social proof, vouchers, bundles, and ratings. The related 50-executive survey is exploratory context; no numeric result was supplied. A future increase in penalties for persuasion is a hypothesis, not an observed trend established by this experiment.

## Commerce: separate the official change from explanations for it

OpenAI's [24 March 2026 announcement](https://openai.com/index/powering-product-discovery-in-chatgpt/) says the initial Instant Checkout did not provide the desired flexibility. It describes focusing on discovery, allowing merchants' own checkout experiences, and supporting deeper merchant integrations through ChatGPT apps. Walmart's described app includes account linking, loyalty, and payments. This is a change in integration approach, not proof that every transaction must leave the conversational interface or that agent checkout has been permanently abandoned.

The supplied skill also relayed completion at roughly one-third of merchant-site rates, about 8% of U.S. adult ChatGPT users trying the feature in its first month, and roughly a dozen integrated Shopify merchants. **Those performance figures are not established by the official announcement inspected here.** Preserve them only as historical reported claims requiring their original source, population, dates, and denominators before reuse. Do not infer that buyers accepted discovery but rejected checkout from those figures alone. Coverage, availability, integration work, user mix, and experience design are alternative explanations.

Historical examples named Instacart, Target, Expedia, Booking.com, Amazon/Rufus, and Walmart/Sparky. Confirm each partnership's date and actual function before making a current strategy claim. The earlier Walmart citations named October 2025 for OpenAI and 11 January 2026 for Google; absolute dates are preferable to unreconciled phrases such as “last month.”

**Protocols:** Google's [11 January 2026 UCP technical introduction](https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/) identifies an open commerce protocol spanning consumer surfaces, businesses, and payments, with flexible integration methods. UCP and ACP are different projects, even when partners overlap. A protocol's published specification does not establish which capabilities a given merchant or platform has deployed.

**Agent verification:** Visa [announced Trusted Agent Protocol on 14 October 2025](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html), developed with Cloudflare and made available through its developer center and GitHub. This contradicts the earlier blanket claim that no such system exists. It does not prove universal production maturity, complete ecosystem adoption, or resolution of every fraud, payment, authorization, and liability issue.

## Problem literacy, brand code, and the Novel Insights connections

The Brooks illustration connects useful category education to the language customers bring to assistants. Its long history is a case context rather than a minimum implementation period or a proven causal estimate. Creating understandable product information, supporting independent evidence, and teaching useful problem language can complement each other.

Taite, Winsor, and Fernandez's May 2026 practitioner article supplies the brand-code concept; pairing it with the inclusion triad is this library's synthesis. An internal brand code is not necessarily an external model's input. Separate public product facts from confidential strategy and customer information.

The Novel Insights ledger's W entry initially described corpus presence as non-purchasable distribution; later entries challenged that. Keep **presence, recommendation, traffic, and conversion** distinct. Paid work can improve information availability without guaranteeing a recommendation. Maintenance costs do not by themselves mean the resulting information has no durable asset value.

The N/F/G and hold-up connections ask who controls ranking, who can contest errors, and whether an alternative route exists. These are useful questions. Do not assume every brand has no appeal mechanism, a direct channel is its only option, structured data has only one consumer, or better representation can never improve margin. Check the actual contract, portability, other channels, and unit economics before recommending investment.

The Porsche brand-extension connection suggests checking whether a new offer preserves the quality that earned trust. A successful historical extension does not prove a universal necessary condition. This skill's job is to make the promise legible and test its interpretation; `moat-finder` carries the broader trust-and-defensibility analysis.

Specific primary pages above were checked on 13 September 2026. Detailed inherited article claims are labeled when their underlying data or full text was not inspected. Recheck material platform facts and study versions when using this skill; there is no date until which every number remains valid.
