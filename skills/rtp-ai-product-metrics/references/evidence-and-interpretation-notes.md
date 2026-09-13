# Evidence and Interpretation Notes

Reviewed 13 September 2026. The source skill contains valuable measurement lenses alongside historical numerical cases. Keep findings, reported estimates, and proposed applications distinct. These notes preserve those cases without converting them into universal thresholds.

## Repeated trials and measurement arithmetic

Anthropic's primary [agent-evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), January 9, 2026, distinguishes pass@k from pass^k and recommends choosing them for the task. The concepts have earlier benchmark lineage; they are not exclusively an Anthropic invention. It also distinguishes capability evaluation from regression protection: a solved case can remain valuable as a regression check.

For independent identical trials, `p^k` describes all-trial success. Across tasks with different probabilities, averaging task-specific `p_i^k` is not generally the same as raising average success to the kth power. Multi-step workflows have their own dependencies, recovery, and critical paths. More attempts also cost money and time, and a user needs a way to select a successful candidate.

The original pass@k/pass^k threshold table (0.80/0.33, 0.50/0.20, and 0.90/0.85) is not a validated diagnosis or production gate. The sample dashboard called pass^5 = 0.82 “above target” while its overall target was 0.85; the revised template leaves status contingent on an actual target.

False-positive rate, false-discovery proportion, hallucination rate, and calibration are different measures. Similarly, revenue minus selected variable costs is a contribution measure, not automatically net revenue or full gross profit. Review cost requires time per case, not just cases times an hourly rate.

## Microsoft: preserve scope and restore the quality checks

The primary [November 2023 Work Trend Index report](https://www.microsoft.com/en-us/worklab/work-trend-index/copilots-earliest-users-teach-us-about-generative-ai-at-work) describes a **147-person** study of searching, meeting summarization, and blog drafting. Reported completion time was 29m42s with Copilot versus 42m6s without—about 29.5% less time. The report calls this 29% faster; do not translate it into 30% of an entire workweek saved.

The source skill blended this study with a workplace license-allocation description. Keep those designs separate. The original report **did assess accuracy and writing quality**: it reports no statistically significant accuracy difference across the tasks and no statistically significant blog-quality difference under an LLM-panel assessment. That is not proof of exact equivalence or a guarantee across all work, but “quality was not assessed or could not be established” is too strong after checking the primary report.

## MIT task acceptance and professional contribution

The library's preceding capability-tracking revision checked [MIT FutureTech arXiv:2604.01363v3](https://arxiv.org/abs/2604.01363v3), dated July 23, 2026. It covers more than 6,000 supplied-input text tasks and more than 60,000 evaluations. Use the version-specific findings: approximately 60% of tasks in Q2 2024 rising above 70% in Q3 2025 at the stated acceptance standard. The source skill's broader 50–75% range and 2.2–2.8-year failure-halving claim should not be mixed with another paper version or treated as a measured future law. The 2030 projections are conditional.

Minimally sufficient, typical-human-equivalent, and better-than-typical judgments are different bars. Rater judgments about a typical human are not a measured head-to-head workforce substitution experiment. The supplied-input setting also excludes some real input assembly and integration work. “Better than average” is neither the only possible economic substitution case nor sufficient evidence for replacing a role.

The KPMG/UT Austin case involves **523 US early-career professionals with under 18 months' tenure**, not 523 organizations or the workforce generally. Its human-contribution lens should remain tied to its tasks and method, not a universal declaration that final-output metrics can no longer distinguish people.

The earlier n=78 working-paper case reports spread changing from 0.80 to 0.13 on conceptualization and 0.58 on assisted writing. Preserve these as source-reported measures whose exact definition and uncertainty need the paper; do not call them population variances or universal ceiling dates. Scores around 4.05–4.18 on a five-point scale may reflect instrument limitations, but are not at the literal maximum. The adjacent rebalancing-versus-human-inertia comparison and “AI gravity” argument likewise motivate task-specific assessment, not a rule that invariant tasks always ceiling first or that state-dependent ones never do.

## Estimated counterfactuals and expanded work

The user-provided primary PDF of “Research: How AI Agents Broaden the Scope of Knowledge Work” (HBR, July 2026) was inspected for the numerical comparison and limitations. It compares matched, near-identical opening requests within one product ecosystem, with early adopters overrepresented.

It reports mean machine time of about **26 minutes versus 33 seconds**, approximately 48×, and medians of **nine minutes versus 14 seconds**, approximately 40×. These are duration comparisons, not direct counts of useful work. Agent pauses were about 38% of sessions versus under 1%, and user stops 3.7% versus 3.4%; that pattern alone does not establish whether the pauses were necessary or review effective.

The **269→36-minute** comparison is modeled, approximately 86.6% less time or 7.47× speedup; the reported cost reduction is 94%. The article also reports a second LLM-based estimate of 84% time and 93% cost savings, plus user-reported speedups from 5× to over 300× with a median near 25×. The original skill omitted the second method. These estimates differ in method and summary statistic; dividing 25 by 7.5 does not show a clean contradictory estimate for the same population and statistic.

A modeled baseline can be informative if assumptions, validation, sensitivity, and scope are clear. It is not automatically invalid or based on “nothing.” Do not present modeled savings as a directly timed human comparison. New task scope indicates changing demand; pair it with quality and realized benefit rather than claiming it must be the least verifiable work.

## Ratios, forecasts, and company examples

The primary [MIT CISR digital-colleagues briefing](https://cisr.mit.edu/publication/2026_0401_DigitalColleagues_WeillWoerner) reports a September 2025 survey of **132 organizations**, published April 2026. Its summary says **75% of respondents predicted** an average 25% revenue-per-employee increase over three years, with a median of 15%. Preserve that subgroup and forecast framing; it is not a realized 25% gain across all 132 firms.

Revenue-per-employee already contains revenue's price and quantity effects. It can rise, fall, or stay flat when prices or staffing change. Tokens-per-task is a different ratio. Both deserve component analysis, not the original claim that they all necessarily rise when gains are passed to customers.

The Bolt.new/StackBlitz and Bench ARR-per-FTE comparison is a historical warning about business model, inherited assets, contractor treatment, and timing. The source reports $1.3m versus $23k and approximately $105.5m of prior StackBlitz funding; do not use these as verified current ratios or proof that AI caused one company's efficiency or another's failure. ARR is an annualized revenue run rate, not accumulated engineering stock, and FTE is a workforce quantity, not a financial flow. Inherited assets still matter to the comparison. Bench's later brand/asset continuity does not settle the original entity's insolvency history; see `trendslop-check`.

Caterpillar's enablement/creation/realization case is reported in MIT SMR, “Data Transformation Is the CEO's Business,” May 21, 2026. The source cites services revenue of $14bn in 2016 and $24bn in 2024. Treat those as company-reported service measures requiring the relevant dated disclosure; the annual-report URL now changes over time. Neither that growth nor accurate asset-record counts identify how much value AI caused. The reporting triad can still be useful without a causal revenue attribution.

The Klarna “700 agents” and subsequent human-service story requires scope: workload-equivalence, job counts, customer outcomes, and hiring decisions are not interchangeable. The original CNBC link/date and simplified replacement/rehiring narrative were not independently resolved here. Do not repeat them as a settled causal proof. Splunk's user-versus-economic-buyer account (Wise and May, HBR, August 2026) is an insider narrative; the reported SEC revenue figures do not independently verify the authors' causal story about value communication.

## Satisfaction, review, incentives, and adoption cases

**Top-box satisfaction:** the source's June 2026 HBR discussion, Gallup work, and Anderson/Mittal lineage motivate testing nonlinear relationships, not an exclusive rule that only 5s predict retention. Use distributions and actual predictive evidence. The primary [Net Promoter definition](https://www.netpromoter.com/know/) is percentage promoters (9–10) minus percentage detractors (0–6), with all respondents in the percentage denominator. NPS does aggregate categories, but it is not an average of averages.

**Persona and invisible work:** the HBR personality and hidden-work cases suggest that satisfaction and behavior may detect different things. A null satisfaction result in one study does not prove satisfaction cannot detect harm. Turn length, arguments, after-hours messages, fragmented calendars, and open surfaces are imperfect proxies, not automatically superior or independent of how someone feels. Avoid intrusive individual monitoring under a product-metrics rationale.

**Accounts payable:** the reported 17.4→3.1-day approval median and 22%→9% exception rate in the middle-office account lack a specified survey method in the source. Either faster handling or fewer exceptions can have favorable and unfavorable causes. Sample both escalated and non-escalated outcomes, not only the cases the system already flagged. Handoff counts and escalation rates remain distinct.

**Review incentives:** Gu, Li, and Zhu's automation-cliff theory uses assumptions about performance and constrained human attention. A predicted review-effort response is not a measured universal law. Known-error tests, independent audits, and other assessment designs can address ambiguity; none is uniquely sufficient. The Hinds/Leonardi botsitting anecdotes—hidden use, hidden cleanup, manufactured usage, and a no-blame review rewarding evidence against unsuitable automation—are useful candidate mechanisms, not measured prevalence. A vendor estimate that roughly one-third conceal use needs its population and method before reuse.

**Adoption:** the upside/downside × lead/lag matrix from “The Human Side of AI Adoption” is a planning lens. Metrics need not already appear in compensation to matter. Demystifying, embedding, and proving benefit may each help without a mandatory sequence or a guarantee of pull. The MGB scribe-license anecdote supplies no unused-license rate. Historical licensing data can remain measurable after revocation; capture the event and censoring rather than assuming the population was deleted. Benefit destination is one possible cause alongside practical access and workflow issues.

| Adoption lens | Earlier signals to investigate | Later outcomes to assess |
|---|---|---|
| Upside | Useful utilization, task-level wins, and evidence of better work | Repeat use, realized revenue or capacity benefit, and durable customer outcomes |
| Downside | Complaints, emerging errors, and signs of excess review burden | Confirmed leakage, workflow disruption, and sustained harm |

These are candidate placements, not fixed classifications: a win rate or complaint can lead one decision and lag another. Define the outcome and time horizon before calling a measure leading or lagging.

**Decision-service analytics:** the HBR framework distinguishes efficient answers, reliable answers, and better decisions. Do not claim most organizations occupy a particular tier without a measured population, or that analytics teams cannot co-own decisions. Instrumentation can serve discovery and future diagnosis even before one immediate decision is known.

## Outcome pricing snapshots

As checked during this pass, official pages list HubSpot Customer Agent at **$0.50 per resolved conversation** and Help Scout AI Answers at **$0.75 per resolution** under the applicable plan/trial terms. See [HubSpot's announcement](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete) and [Help Scout's help page](https://docs.helpscout.com/article/1750-help-website-visitors-with-ai). HubSpot's [resolution guidance](https://knowledge.hubspot.com/customer-agent/understand-the-customer-agent) applies a 72-hour rule for relevant reply-based resolution status and distinguishes qualifying handoff from mere manual assignment. Check current account terms before modeling a bill.

The prior `token-economics` revision checked Intercom's $0.99 resolution pricing and distinct procedure/handoff and qualification charges. Use that contract's scope; do not simplify all billed outcomes into verified problem resolution. The original 27%→41% hybrid/outcome vendor-share claim, attributed through Bessemer/Flexprice, is not a verified market census here. No price snapshot proves that seats have been replaced across the market.

## Historical dashboard defaults

The source's acceptance ≥70%, regeneration <10%, abandonment <5%, hallucination <2%, false negatives <3%, pass^5 targets 0.75/0.85/0.90, first value in 60 seconds, four-week trust period, 3–5× acquisition/churn multipliers, 15% cluster threshold, monthly 20–30% dataset replacement, and fixed month-1/month-4 instrumentation stages are not universal requirements. Keep the underlying measurement questions, then set justified local criteria.

## Novel Insights carried into the revision

The reread of ledger lines 1958–1993 adds a fourth assessment option: examine how the tool/retrieval configuration changes what the metric can distinguish. It also warns that a new rubric cannot validate its own claim about valuable expertise. Retain those useful questions without claiming that all prior null studies are uninterpretable or that an escalation rate is a handoff count. The framework is strongest when it helps specify what remains unknown.
