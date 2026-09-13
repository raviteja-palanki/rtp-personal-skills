# Evidence and worked examples

Review date: 13 September 2026. These cases support specific design questions. They do not validate a universal cost curve, staffing ratio, ownership model, or moat.

## Franklin Templeton: make adoption an owned function

The user-provided primary PDF identifies **MIT Sloan Management Review**, not HBR, as the publisher of [“Transforming Investing With AI at Franklin Templeton”](https://sloanreview.mit.edu/article/transforming-investing-with-ai-at-franklin-templeton/) by Thomas H. Davenport and Randy Bean, June 2026. The organization passage was checked directly.

| Unit described | Responsibility in the account |
|---|---|
| Product teams working with business units | Combine product management, engineering, and data science. |
| Common AI platform team | Shared platform; detailed scope is not provided in the passage. |
| Research team | Named, with limited detail in this account. |
| Adoption and solutions team | Supports employee implementation and alignment with business benefits. |

The chief AI officer's remit covers product management, engineering, research, and adoption. This does not establish a fully specified reporting chart, exactly one team per business unit, or measured superiority over another structure. The missing platform detail is a question to investigate, not proof that the company failed to specify it internally. A dedicated adoption team is a useful option, not the only way to staff adoption.

The stated copilot posture can coexist with an analyst that fact-checks or offers contrary views. Clarify advice, approval, and veto rights; disagreement alone is not an incompatible form of autonomy. See `autonomy-spectrum` and `trust-ladder`.

## AI spine: research-informed proposal with bounded evidence

[“Create Generative AI Value at Scale”](https://shop.sloanreview.mit.edu/store/create-generative-ai-value-at-scale), by Kevin Schmitt, Gregory Vial, and Ivo Blohm, was published June 2, 2026. The [authors' university summary](https://iwi.unisg.ch/en/newsuebersicht/news-detail/news/why-most-organizations-fall-short-when-it-comes-to-ai-integration/) reports interviews with **87 practitioners across 23 large organizations** that had scaled GenAI. The source's description of the spine as merely diagrammed should therefore not be read as “no empirical work exists.”

The interviews inform the coordination model; they do not constitute a randomized comparison proving it superior to every center of excellence or business-unit structure. The summary identifies process-wide application, continual refinement, and abandoning unproductive projects. The detailed funding share and role/cadence prescriptions are carried from the user-provided skill and report; their causal effect is not independently established here. Workhuman sponsorship of the compiled special report is relevant context, not a reason to dismiss the underlying research automatically.

## Harness improvements and token usage

LangChain's primary [February 17, 2026 account](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) reports improvement from 52.8 to 66.5 on Terminal Bench 2.0, **13.7 percentage points**, through harness changes with the model held fixed. Its top-30 to top-5 description is a dated leaderboard comparison, not a stable rank or causal estimate for enterprise ROI. The example supports examining traces and system changes; it does not prove that every private eval loop is a moat.

Datadog's [State of AI Engineering report](https://www.datadoghq.com/state-of-ai-engineering/) and [September 2, 2026 explanation](https://www.datadoghq.com/blog/monitor-prompt-caching-optimize-token-usage/) report that **69% of input tokens in Datadog customer traces in March 2026** were system-prompt tokens. That is a particular observed customer set, not all production AI. Repeated instructions can motivate caching and context review; the proportion alone does not prove context rot, unnecessary tokens, or wasted spend.

## Numerical corrections and planning limits

- The historical example's $200 versus $9 is about **22.2×** the cost, an increase of $191. Six hours versus 20 minutes is **18×** the time. With different completion outcomes, neither ratio isolates a harness treatment effect.
- An autonomy share rising from **5% to 30%** is a **25 percentage-point increase** and **six times the original share**. At unchanged total volume it is not five times the resulting autonomous volume. Throughput still depends on capacity and workload.
- The claimed FinOps figures `$18.40 → $6.07 per million tokens`, `2.4 billion calls`, and `$1.2m → $7m` enterprise bills were not located in a primary FinOps source during this pass. Do not cite them as verified. The first change is about a 67% fall; the second is **5.83×**, about a 483% increase, **not tripling**. Model mix, units, customer set, and time window would also need matching.
- The original 3–5× infrastructure/token budget, 30–40% runtime undercount, threefold Year-3 lock-in difference, 60/40 open/closed split, 5–30× agent token use, and 10–100× incident-cost improvement lack sufficient primary scope here. They are historical estimates to replace with actual program data, not default multipliers.
- Staffing counts, nine-day duration, four tickets, five evals, fifty traces, >90% judge agreement, three locked clusters, and recovery-rate ranges are starter examples. No one number substitutes for the action's consequence, workload, and measurement quality.

## Portability and permanence claims needing caution

The original direct quote attributed to Mitchell Hashimoto about models being commodities and harnesses being the moat was not verified against his own publication in this pass. Do not reproduce it as a sourced quotation. A model, data asset, distribution channel, or operating process can also contribute to advantage.

The original June 2026 proof-point list names Claude Tag, Claude Science, an OpenAI hosted-Evals retirement with approximately six months' notice, and a 19-day Fable 5 suspension. Exact products, incidents, dates, and scope were not verified here. Treat them as research leads, not grounds for refusing a vendor or evidence that hosted evaluation can never be used. Verify a current contract and deprecation policy for the actual service.

Likewise, a BloombergGPT comparison is not a universal consequence of private evaluation. The useful question is whether internal quality assessment has independent checks and measures the user's task.

## Novel Insights applied

The ledger's platform cases show recurring organizational investment while explicitly admitting that platform cost and ROI were often missing. Preserve that limit: neither platform-first nor platform ownership alone establishes advantage. A monitoring capability can feed recurring release or intervention decisions, so it should not be excluded simply because it is called a control.

The user-versus-buyer value passage adds a practical communication check: explain the daily benefit to the person using the system and the costs, outcomes, and uncertainty to the person funding it. That distinction does not require a separate team or imply every consumption-priced product must face the same renewal problem.
