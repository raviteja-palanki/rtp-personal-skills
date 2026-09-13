# Research and Interpretation Notes

Reviewed 13 September 2026. Examples inform hypotheses; they do not establish the expected return from a different deployment.

## The J-curve predates the 2026 HBR application

[Brynjolfsson, Rock, and Syverson, 2021](https://www.aeaweb.org/articles?id=10.1257/mac.20180386), *American Economic Journal: Macroeconomics* 13(1), 333–372, develops the Productivity J-curve around complementary intangible investment and measured productivity. The original skill attributed development of the concept to the 2026 HBR authors; that is incorrect. Paul David's historical work on electricity provides related background, not the sole attribution for this named model.

The HBR application can motivate planning for learning and integration costs. It does not prove that nearly every organization must dip, that a dip cannot indicate failure, or that a recovery will occur by month 9–18.

McKinsey's [2025 agentic-AI article](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage) reports more than 80% of companies seeing no material earnings contribution from gen AI. Preserve the date and self-report nature. That cross-sectional finding does not identify a J-curve phase or promise later returns.

## Historical experiment results with their populations

| Case | What the evidence supports | Limit to carry |
|---|---|---|
| **Customer service** | [NBER WP31161, November 2023 revision](https://www.nber.org/papers/w31161): 5,179 support agents; issues resolved per hour +14% overall and +34% for novice/low-skilled workers under its staggered introduction design | Version-specific figures. A later QJE 2025 publication exists; do not mix versions or generalize to all roles. Sentiment/retention findings concern this setting. |
| **P&G innovation** | [NBER WP33641](https://www.nber.org/papers/w33641): preregistered experiment with 776 professionals, randomized across individual/team and AI/no-AI conditions; AI-assisted individuals matched non-AI teams on the studied innovation performance | The NBER record lists publication in *Organization Science*, June 2026, DOI 10.1287/orsc.2025.20702. This is task-specific collaboration evidence, not workforce equivalence. The source's blending technical/commercial perspectives belongs to that case. |
| **Copilot across firms** | Current [AER: Insights forthcoming abstract](https://www.aeaweb.org/articles?id=10.1257/aeri.20250275): 66 firms, 7,137 knowledge workers, six-month experiment; in its second half, the 80% of treated workers who used the tool spent about two fewer hours weekly on email and less time outside normal hours | No detected quantity/composition shift in tasks from individual-level provision. The source's 1.3–3.6-hour range and faster-document claim reflect earlier reporting; do not turn different versions/estimands into one universal effect range. These were workers across firms, not all Microsoft employees. |
| **Coding assistants** | The user-provided HBR article reports GitHub and Google controlled-task results spanning 21–55% faster completion with some completion/well-being gains | Separate studies and tasks, not a pooled causal range for every engineering role. Primary coding papers were not rechecked here; use the claim only as dated source-reported background. |
| **Siemens shop floor** | The same HBR article reports a 2024 Erlangen trial with faster information finding, greater independence, and improved perceived job security | Authors participated in the test; it was exploratory and a larger randomized trial was still being developed. Concurrent team downsizing is described as unrelated to AI. Do not call these results an already completed randomized causal estimate. |

The main HBR source is Berndt, Englmaier, Sadun, Tamayo, and von Hesler, “A Systematic Approach to Experimenting with Gen AI,” January–February 2026. The user-provided PDF was checked for the passages above, its authorship, and the ecosystem claims; it was not reread in full for this revision.

## Ecosystem, learning, and support cases

The HBR article says Grab was **currently collaborating** with HBS and INSEAD academics on an assistant study concerning more than one million entrepreneurs in six countries. It supplies the scale of the reported initiative, not a published effect estimate or proof that every person completed an experiment. Distinguish target population, recruited sample, exposed users, and analyzed units.

The Warner Bros. Discovery information-versus-permission distinction comes from a single-company HBR account. The source skill's prose also reverses its own safe-bet comparison. Use the two purposes to clarify the pilot's job; uncertainty and stakes are separate dimensions, and one design can yield both learning and adoption readiness.

The three-practice-arms-plus-forecast template is attributed to an unpublished 2026 study without an identified sample in the skill. It remains a design lead. A one-week test may measure recall, skill, or transfer depending on its tasks; its effect is not automatically a lower bound on a longer-term effect. Forecast surprise is separate from causal validity.

The HBR “AI Experiments Need Domain Experts. Here's How to Support Them,” August 2026, describes two pseudonymized sites over two years, with 141 versus three reported solutions and over-80% expert withdrawal at one site. The settings differ and the withdrawal denominator is unspecified in the source skill. Calling the shared sandbox a control condition does not make this a controlled experiment. Industry, goals, organization, and implementation can also explain differences. The four support categories and three work modes are useful design questions; compensation is not established as the sole causal bottleneck.

The eBay incrementality example is a counterfactual-design lead. The original ledger recognized a likely Blake/Nosko/Tadelis field experiment but had not opened it; this revision does not upgrade that unverified link into a newly checked result. The scaling questions are an adaptation of John A. List's *The Voltage Effect*, not a guarantee that passing five questions makes a rollout work.

## Product testing and agent arithmetic

Google's primary [SRE canarying chapter](https://sre.google/workbook/canarying-releases/) discusses partial deployments, comparison populations, shared-state contamination, and traffic teeing. Shadow outputs being hidden does not remove possible side effects, shared-load interference, or data exposure. Canary detection and a powered causal A/B study can share infrastructure while answering different questions.

The original April/March 2026 rollout blog links are implementation leads, not authority for “online always proves it,” “shadow has zero risk,” or “never release directly.” Choose the design from the actual exposure and evidence requirements.

`0.95^10 = 0.5987` and `0.90^10 = 0.3487` are correct arithmetic for ten independent indispensable equal-reliability steps. The source incorrectly labels this **pass^k** and uses it as a general agent estimate. Repeated full-task success and success across workflow steps are different quantities. A stateful sandbox can test relevant mechanisms; neither WebArena nor the source's GAIA2-style reference certifies an unrelated production system's safety.

## Novel Insights carried forward

The reread at lines 1995–2037 emphasizes expert participation, invisible workload, and shared review criteria. Preserve those questions without claiming that a two-site qualitative comparison held every relevant condition constant, that bonus/promotion alignment is the only sustainable arrangement, or that participation is the only early metric. Likewise, explicit weights matter for a weighted aggregate; a shared rubric with separate criteria can be disputed and useful without weights.

The original experiment-count caution remains valuable even within one team using a stable definition: a rising count can still reflect smaller, easier tests. Record what decision each test informed, and keep unsupported causal claims out of the program's success story.
