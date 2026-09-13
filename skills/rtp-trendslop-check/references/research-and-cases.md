# Trendslop Check — Research and Cases

Editorial review: 13 September 2026. The complete saved primary HBR article text was read during this revision. Its charts were not recoverable as readable data from the saved PDF; precise values previously taken from secondary summaries remain distinguished below.

## What the trendslop article actually reports

Angelo Romasanta, Llewellyn D.W. Thomas, and Natalia Levina published [Researchers Asked LLMs for Strategic Advice. They Got “Trendslop” in Return](https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return) on March 16, 2026. The saved article describes several analyses, not one approximately 15,000-run experiment across six models.

**Baseline comparison.** The article names seven tested systems: ChatGPT, Claude, DeepSeek, GPT-5 through the API, Gemini, Grok, and Mistral. These are not necessarily seven independent model families. It says the chart plots each system's average preference over fifty runs for the binary tensions. It reports common preferences, particularly for differentiation, augmentation, and long-term performance. Exploration versus exploitation varies across systems; the text explicitly says ChatGPT still favors exploration. It is not a bias-free control condition, and a neutral 50/50 rate is not itself proof of correct advice.

**Prompt manipulations.** The deeper analysis focuses on the system the article calls ChatGPT-5. It reports over 15,000 trials varying option order, framing, pros-and-cons analysis, and incentives. For differentiation and augmentation, biased-answer shares dropped by less than 2% across manipulations. For the other tensions, responses generally moved about 22% from baseline in either direction; option order was a major factor, with a reported 19% reduction in biased-answer likelihood.

**Context manipulations.** A separate description says over 15,000 trials varied industry and detail of context. The reported average movement is 11% from baseline, sometimes increasing and sometimes decreasing the preference. The article does not fully resolve every trial-count overlap in the prose. Do not sum or collapse counts without the underlying design.

The earlier skill incorrectly converted the less-than-2% result for two tensions into a universal “deeper reasoning changes bias by 2%” row. Its 19/2 and 11/2 comparisons consequently did not compare equivalent interventions. Do not present them as fourfold or tenfold evidence against reasoning. Preserve the source's percentage wording unless the underlying measures establish relative change versus percentage points.

**Mechanism and limits.** The authors attribute the pattern to positive and negative associations in training material. This is their explanation; the described behavior does not isolate training-data valence from other model, interface, prompting, or alignment effects. It also does not show that every new model is equally biased, that AI never reasons about context, or that these strategic choices generally cause poor business outcomes.

**Recommendations retained.** Use AI to expand options; examine known and potential biases; remain alert to model changes; investigate incoherent hybrid advice; and supply context without treating it as a cure. The article's main argument supports careful human judgment. The benefit of this particular skill's audit on realized strategy outcomes remains a hypothesis, not a result demonstrated by the study.

### Historical numeric claims and seven tensions

| Tension | Reported tendency in the earlier skill | Evidence status for this revision |
|---|---|---|
| Differentiation / commoditization | 96% toward differentiation | Direction supported by primary prose; exact percentage retained from the prior secondary summaries, not independently recovered from chart data |
| Automation / augmentation | 93% toward augmentation | Same distinction |
| Short / long term | Long term | Primary prose supports the direction for the studied settings |
| Competition / collaboration | Collaboration | Direction reported in the earlier chart summary and consistent with the primary discussion; no newly verified exact rate |
| Radical / incremental innovation | Radical | Earlier chart summary, no newly verified exact rate; do not reverse it into a claimed incremental study finding |
| Centralization / decentralization | Decentralization | Direction reported in the earlier chart summary and discussed in the primary text; no newly verified exact rate |
| Exploration / exploitation | Varied across systems | Primary prose; variation is not absence of within-system bias |

Growth versus profitability was not one of the seven tested tensions. It is a practical extension, with no prevalence estimate established here.

The old hybrid figures—63% trendy-only, 24% both, and 12% less-fashionable—came through secondary accounts. They sum to 99%, potentially from rounding; do not silently repair the missing point or present them as newly independently verified. The primary text describes the hybrid exercise on ChatGPT. A hybrid can obscure trade-offs, but it can also be coherent when activities, segments, timing, and resources support it.

The prior secondary links were [Zenn's review](https://zenn.dev/sigma7641/articles/fcf90de4822321) and [Polything's commentary](https://polything.co.uk/blog/ai-strategy-trendslop-why-llms-give-bad-advice). Agreement between retellings of one study is not independent replication. Use the primary study or chart data for consequential numerical claims.

The unattributed “real quote from a PM” in the earlier skill had no traceable speaker or record. It has been removed as a quotation. Its useful scenario—polished advice that fits a different company—is retained as an explicit illustration in the main skill.

## Teaching case: composite value at Vanguard

The source is *MIT Sloan Management Review*, not HBR: [Investing in AI Payoffs at Vanguard](https://sloanreview.mit.edu/article/investing-in-ai-payoffs-at-vanguard/), by Thomas H. Davenport and Randy Bean, October 2025. The local source note records a roughly $500 million company-reported value figure across data, analytics, and AI. Do not relabel it AI-only value or a measured return on investment without the investment denominator.

The four buckets are cost avoidance, shareholder value creation, risk reduction, and operational efficiency. Ask for the period, per-bucket amounts, methods, baseline, costs, overlaps, and uncertainty. Vanguard's client-owned structure affects the meaning of shareholder value; it does not render all economic claims inherently unverifiable.

The older table incorrectly said three buckets cannot be checked and only efficiency can be. Counterfactual cost avoidance and risk reduction can use auditable assumptions, comparison groups, actuarial models, experiments, or other suitable designs. Before-and-after efficiency also needs a credible comparison if it is claimed as an AI effect. A model is an estimate with assumptions, not automatically a false number.

No disclosed component split in the cited account means the reader cannot reconstruct the total from that account. It does not prove no internal audit is possible, that three categories are unfalsifiable, or that operational efficiency must dominate for the total to be sound. The nearby report of a few dozen applications being piloted prompts a scope question: which periods, deployed uses, and non-generative analytics contribute to the value figure? It is not itself a contradiction.

## Teaching case: comparable numbers and company chronology

A July 2026 MIT Sloan entrepreneurship discussion compared Netflix reaching one million users with ChatGPT reaching that count in five days. The library's earlier source review distinguishes paying DVD-service subscribers from free signups. Even if both figures are individually correct, they do not measure the same commercial milestone. A comparison can be informative when differences are explicit; it cannot support a clean ratio of adoption efficiency without adjustment. Do not infer that provisioning, repeat use, and payment are interchangeable.

The same discussion used roughly $23,000 ARR per FTE and a January 2025 bankruptcy reference to explain Bench's difficulty. The ratio's underlying method remains unverified. The prior research record places closure on December 27, 2024 and an acquisition announcement on December 30. [Employer.com's announcement](https://www.einpresswire.com/article/772843833/employer-com-announces-acquisition-of-bench-accounting), published December 31, and [Bench's transition information](https://www.bench.co/transition-faqs) support distinguishing acquired assets from the prior entity and its obligations. The [current FAQ](https://www.bench.co/faq) describes resumed service in January 2025.

Continuation of a brand or acquired service does not establish that the original company avoided insolvency or liquidation. Verify legal entity, transaction status, and filing records before making that claim. Neither the old ratio nor the acquisition alone establishes why the business failed or survived.

These cases show that checking a number, its units, chronology, and causal story are separate tasks. A narrow fact lookup can miss either mismatch; the earlier skill's claim about which check catches which case was internally reversed.

## Five further evidence patterns

### 1. A statistic points in the opposite direction from its sentence

The earlier review records an August 3, 2026 MIT Sloan article, *6 Questions to Guide Your AI Strategy*, describing 70–95% of AI pilots reaching scale while calling the result dismal. Taken literally, that is a high success rate. A missing negation is a possible explanation, not a correction the reviewer may silently make.

The underlying studies, populations, and meaning of scale were not established in the skill. Do not republish either the original or an assumed corrected failure rate as fact. Locate the source or remove the unsupported numeric inference. A wide range may reflect different populations, definitions, methods, or real variation; its width alone does not prove which explanation applies. The number can remain in a clearly identified audit example.

### 2. A cited outcome is absent from a related primary disclosure

The prior research note for *How Leaders Can Use AI to Solve Real Business Problems* records a 41% sepsis mortality claim about Cleveland Clinic and a related institutional disclosure that did not report that mortality figure. The note says an 18% number belongs to a different study at other hospitals and that multiple initiatives and a financial interest in the vendor require attention.

The source URL was unresolved in the older skill. This revision does not independently verify either clinical percentage. Keep them as claims under review, not medical outcome evidence. Do not substitute 18% as a “corrected” version of 41%. Match study, hospital, intervention, outcome, period, and adjustment method.

Silence in a press release does not refute a result that may appear in a paper or another disclosure. It establishes that this document does not verify it. If the exact figure is disclosed, still examine methods and attribution; a matching quote does not by itself establish causality. A disclosed financial interest is relevant context, not proof that a result is false.

### 3. An uncited statistic can be traced and repaired

The earlier skill treated “6,000+ executives, 90% no productivity improvement, NBER” as lacking an identifiable study. The study is now located: *Firm Data on AI*, NBER Working Paper 34836, by Ivan Yotzov and coauthors. [NBER's own May 2026 summary](https://www.nber.org/digest/202605/global-evidence-business-use-ai) reports nearly 6,000 executives across the US, UK, Germany, and Australia, surveyed November 2025–January 2026. It distinguishes more than 90% reporting no employment effect from 89% reporting no labor-productivity effect over the previous three years.

This is executive survey evidence, not an independently measured null effect in every firm or proof that AI cannot improve productivity. “Nearly 6,000” is not “6,000+.” The older blanket “no source exists” conclusion should be replaced with the citation and correct scope. The current HBR urgency article also contains an NBER link; an earlier copy's missing link is not a permanent property of the source.

### 4. A claim that evidence exists still needs support

The mentoring example asserted that return on investment was well documented without identifying a study. Search the surrounding document and linked material first. If no support is supplied, label the claim unsupported in that source and look for the evidence relevant to the actual decision.

The absence is a reporting weakness, not proof that mentoring lacks evidence or that the claim is necessarily more false than an incorrect number. A source trail, a measurable claim, and methodological strength are distinct qualities. Do not rank rhetorical defects as substitutes for verifying substance.

### 5. Tacit capability needs a valid observable measure

The earlier podcast example attributed company decline to lost process knowledge. Difficulty writing down a skill does not make the skill unmeasurable or the causal claim unfalsifiable by definition. Test specified predictions about performance, adaptation, failures, training, or knowledge transfer.

Attrition among knowledgeable staff, time to proficiency, documented handoffs, and mentoring hours are candidate indicators. They need construct validity and competing explanations: hours can increase without learning, and attrition can follow decline rather than cause it. A capability already paired with a measurable proxy still needs this scrutiny. Process knowledge can transfer through practice, demonstration, hiring, collaboration, and written support; no single channel is exclusive.

## How to use Novel Insights here

Reread the ledger's cautions about modeled baselines, reporting granularity, tacit knowledge, shared sources, and instrument quality. Treat its broad claims as hypotheses to examine. This revision specifically qualifies H's blanket distrust of counterfactual models and K/P's inference that unrecordable means unmeasurable. Retain the practical request for observable evidence while allowing valid causal estimation and performance assessment.
