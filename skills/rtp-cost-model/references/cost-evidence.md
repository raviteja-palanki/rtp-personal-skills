# Cost Model — Evidence, Assumptions, and Corrections

Reviewed 13 September 2026. Full original SKILL.md and CONCEPT.md read. This revision preserves the full-workflow cost method, growth analysis, routing/caching/harness mechanics, human effort, energy, vendor terms, and pricing handoff. It removes unsupported universal thresholds and corrects examples that could change a decision.

## Current primary checks

**Prompt caching.** [Anthropic documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) checked for pricing, minimum lengths, isolation, lifetimes, and batch compatibility. It distinguishes cache writes, reads, ordinary input, and output. Write prices differ by lifetime; read multipliers and minimum lengths vary by model. Isolation is defined at organization/workspace or platform boundaries, not universally per API key. Asynchronous batches can use caching, with best-effort hits. The skill’s numerical example uses explicit hypothetical rates rather than a permanent vendor price table.

**Harness cost.** [Anthropic’s 24 March 2026 report](https://www.anthropic.com/engineering/harness-design-long-running-apps) reports $9 and 20 minutes for one solo application build, versus $200 and six hours for its harness comparison. It does not establish universal $0.01/$0.05/$200/$500 architecture tiers, guaranteed human verification, or a risk-to-cost threshold for adding agents. The solo run was not a single twenty-minute API call.

**Routing.** [Huot, Kaisers, and Lapata, 10 July 2026](https://arxiv.org/abs/2607.09197), abstract and publication record checked. The paper examines behavioral differentiation and robustness to query perturbations on particular routing benchmarks. It does not establish a universal 75% deployment threshold, 70–80% easy-query share, 10,000-requests/day break-even, or guaranteed savings range. This revision recommends outcome, cost, latency, and stability checks without claiming the full paper was reviewed here. Similar-quality models can still differ usefully in price or availability.

**Energy.** [IEA, 2026 Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) projects about 950 TWh of data-centre electricity demand in 2030 from 485 TWh in 2025. The earlier 2025 report used 415 TWh in 2024 and about 945 TWh in 2030. Do not blend report vintages or call a projection audited. Multiple reports quoting the IEA are not independent forecasts. Global data-centre demand is not a direct estimate of an application’s energy use.

**Early labor-market evidence.** The previously unnamed survey-to-payroll study is Humlum and Vestergaard’s work, originally titled *Large Language Models, Small Labor Market Effects*. Its [University of Chicago research record](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/) describes linked Danish surveys and administrative records, with precise null estimates for earnings and recorded hours over the studied early period. This does not establish zero task benefits everywhere, nor prove that botsitting alone caused the null. The NBER listing now uses *Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI*, working paper 33777. Full econometric results were not re-audited in this revision.

**Review design.** [Gu, Li, and Zhu, Should Humans Be in the Loop? Human-AI Collaboration Paradox and Automation Cliffs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6417798), SSRN record and abstract checked. The record dates the manuscript March 2026 and its revision June 2026, rather than a demonstrated July field study. It describes a game-theoretic model of adaptive oversight. The full model was not verified here; do not attribute to it a proven claim that independent-then-compare is the only safe review design or that assisted review must cost more than manual review.

## User-supplied research read for this revision

**Hinds and Leonardi, “How Much Time Do Your Employees Spend Botsitting?”, HBR, 5 August 2026.** Full article text read from the research PDF. It describes a Glean Work AI Index survey of 6,000 digital workers in the US, UK, and Australia, and reports 11 weekly hours automated and 6.4 hours managing AI. Those are self-reports with different constructs; the article does not establish that their quotient measures the share of net time savings lost.

The arithmetic `6.4 / 11 ≈ 58.2%` is valid, but the interpretation requires compatible definitions and overlap checks. Shared survey respondents do not make biases cancel or make 58% an upper bound. The stated component times, 2.3 + 2.2 + 1.7 hours, sum to 6.2 rather than 6.4; the text does not reconcile that difference. Do not silently adjust the source or use the breakdown as an exact ledger. The 75% individual-productivity and 13% significant-organizational-performance answers are also different questions, not a sixfold productivity attenuation.

**Garr, “How to Respond to the Coming AI Cost Shock,” HBR, 17 August 2026.** Full article text read. Preserve attention to usage definitions, price changes, hidden work, migration, internal expertise, and contractual safeguards. The one-cent unit price is the author’s illustration; the Workday date is reported through an email to the author, not independently verified here as every customer’s contract. The large spending anecdotes are insufficiently traceable for a forecast and are not reused as typical costs. A finite budget remains useful even when prices are uncertain.

**Tang and Zhao, “Your Company Needs an Energy Strategy for AI’s Next Phase,” HBR, 4 June 2026.** Full article text read. The Great Value Loop is the authors’ strategic framing, not a law requiring profits to migrate through four layers. The article itself includes efficiency and placement options for firms that do not control energy infrastructure. Carbon reporting is not automatically direct per-workflow energy measurement. Specific power deals and named-company workload claims were not independently reverified; the revised skill uses the general planning questions and the primary IEA outlook.

**Carlsson-Szlezak and Swartz, “AI and the Looming Competition for Margin,” HBR, 30 July 2026.** Full article text read. The three productivity pathways are retained. The article also discusses uneven effects, market structure, demand, and competition inhibitors; it does not warrant treating every saving from a rented model as certain to disappear on the same schedule. Proprietary data can support advantage without guaranteeing margin. Do not turn the article’s strategic argument into a universal investment mandate.

**“Bring Back Managing for Value,” HBR, August 2026.** Read the four-capabilities section: alternatives, business-unit capital reporting, capital costs, and scenario forecasts. The cited market-average equity rate and survey statistic were not independently audited. Retain the finance disciplines; use the organization’s applicable current rates and match them to the cash-flow definition. The article’s broader governance and company cases were not fully re-reviewed in this pass.

**Other inherited examples.** Vanguard’s coding-versus-development-life-cycle figures, a vendor/customer productivity comparison, and Perplexity’s modeled manual baseline informed the original skill. Their lesson is to examine scope, baseline construction, and independence. They do not supply calibrated half-or-third coefficients. A modeled baseline can be useful if labeled and tested; it is not inherently worse than having no baseline. Salary-versus-software budget and growth-versus-efficiency discussions remain decision prompts; their 10× salary and industry-specific valuation figures are not transferable pricing or investment rules.

## Arithmetic repairs

| Earlier example | Correct interpretation or calculation |
|---|---|
| Monthly cost table totaled $26,880 | Listed cost rows total **$21,480**; the $5,400 difference was not explained |
| Storage of one million vectors at $0.30/million vector-months yielded $300 | That stated rate yields **$0.30**. The revised illustration explicitly assumes **$300/million vector-months**, yielding $300 |
| Inference share 8%, review share 28% | On the corrected $21,480 example, approximately **10.1%** and **34.9%** |
| Escalation cost multiplied by inference dollars | Incompatible units. A 15% probability of a $5 escalation adds **$0.75 per initial task** |
| 20% failure always means 1.25× cost | `1 / 0.8 = 1.25` only under matching cost/success assumptions; retries and escalation require their own branches |
| Growth-factor example yielded $0.094 | Its written operations yield **$0.12366525**, and the overlapping factors lack an adequately defined cost base. Rebuild components rather than preserve the invented precision |
| Routing weighted mean $0.0138 | `.70×.004 + .20×.015 + .10×.05 = .0108`; adding .0005 routing gives **.0113** |
| 72% routing saving | The corrected .0113 is **77.4%** below .05, before additional rework and fixed costs |
| Cache hit saving applied to every request | Include initial/renewed cache writes, misses, output, and other charges. The 84% example describes a successful hit’s input cost only |
| 10 successes × .094 × 10,000 users = $94,000 | **$9,400**, with scope and success definition held constant |
| $20 revenue and .94 cost implied 53% margin | **95.3%** on that cost scope; does not establish operating profit |
| Example said eval exceeded inference | $6,000 eval versus $45,000 inference is **13.3%**, not an excess |
| $5 cost and $10 price produce growing unit losses | They produce **$5 contribution per unit** before other costs |
| .08/minute × 10 minutes/day = .80/month | **$24 over 30 days** |
| .01+.10+.01-style costs or cost ratios used without scope | Reconcile units, period, and denominator before comparing; do not borrow one example’s cost for another |
| Response-cache deterioration implied 7× cost | At .003 per miss and negligible hit compute, 60% to 8% hits changes .0012 to .00276: **2.3×** |

## Thresholds now treated as hypotheses

The earlier fixed values—3–5× overhead, 10–20 calls/task, 70% cache hits, 70–80% easy requests, 75% routing accuracy, automatic 10× deterioration, 20% eval-spend ceiling, and fixed architecture prices—were not established as general requirements. They are replaced with observable drivers, appropriate quality constraints, and measured or explicitly assumed scenario values.

The 30% price-erosion case remains available as a sensitivity. It is not a forecast. A required review design can be expensive; a bounded loss leader can be an intentional decision; a cheaper single model can be adequate. None should be accepted or rejected by a generic ratio alone.

Novel Insights sections H, the botsitting comparison, vendor dependence, and the devaluable meter were re-read for this skill. Their useful questions are carried forward. Stronger claims about automatic bias cancellation, fixed productivity haircuts, inevitable supplier capture, or capability-versus-price clocks are recorded as interpretations to narrow in the ledger’s final editorial pass.
