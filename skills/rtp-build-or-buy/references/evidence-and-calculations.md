# Evidence and calculation checks

Use [SKILL.md](../SKILL.md) for the decision and the [ownership reference](ownership-and-provider-boundaries.md) for the strategic cases.

## Prompting and tuning: what the evidence supports

[Brown and colleagues’ 2020 paper](https://arxiv.org/abs/2005.14165) studies few-shot performance through examples in context without gradient updates. In-context learning did not begin in 2023. The result does not establish that fifty examples in a current model solve most tuning candidates or match every fine-tuned system.

[Google’s current supervised-tuning documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use) includes a summarization example and recommends 100–500 examples for its described setup. This provides concrete counterexamples to the earlier categorical rules against tuning generation or using fewer than one thousand examples. It does not create a new universal minimum or promise performance at that sample size. Check the actual model, tuning method, limits, and training objective.

The old examples of 400, 4,000, and 40,000 training cases remain useful dataset-review scenarios. None determines overfitting or success by count alone. Coverage, ambiguity, label quality, leakage, and held-out performance decide what the data can support. Synthetic data may be useful when its rights, fidelity, coverage, and validation costs are acceptable.

The earlier 20-row evaluation and 50-example label audit are starting exercises rather than assurance standards. Putting test answers among demonstrations leaks evaluation information. Split related cases appropriately and retain a final held-out evaluation after development choices.

For the original quality example, 72% against an 85% requirement is a **13-percentage-point** shortfall, or about **15.3% relative to the target**. A 62% result against 90% is 28 points, or about 31.1% relative to the target. Neither determines which architecture is warranted. State the metric, uncertainty, and consequence of the gap; do not lower a necessary standard to fit a preferred option.

## Historical approach estimates are not a price list

The earlier table assigned prompt, in-context, RAG, fine-tuning, and SaaS fixed delivery times, price bands, and accuracy improvements. The price units mixed per-call, upfront, and monthly costs, while percentage improvements lacked a shared baseline and task. Treat those entries as historical illustrations only:

| Approach | Earlier illustrative estimates | How to replace them |
|---|---|---|
| Prompt | Hours; $0.001–0.05/call; +5–15% | Measure the specified workload, output length, price and baseline |
| In-context | One-to-three days; $0.01–0.30/call; +10–25%; 50–200 examples | Test selected examples, effective context, tokens, latency, and held-out quality |
| RAG | Two-to-four weeks; $0.10–2/call plus infrastructure; +15–35% | Include ingestion, retrieval, rights, freshness, evaluation, and operation |
| Fine-tuning | Four-to-twelve weeks; $200k–500k upfront plus inference; +20–45%; 1k–50k examples | Estimate the chosen managed or self-hosted route and compare actual tuning results |
| Vertical SaaS | One-to-two weeks; $100–10k/month; no maintenance | Include procurement, implementation, usage units, support, control, and migration work |

The original 2021-versus-2026 token-price comparison did not specify a consistent model, token mix, workload, and contract. Larger context does not necessarily cost pennies, and maximum context does not guarantee effective use of every example. Check dated primary prices instead of carrying those old figures forward.

## Rebuild the cost comparison with consistent units

This is a coherent **illustrative** version of the large-volume case:

```text
Current route:                         $1,800,000/year
Candidate model serving/inference:       $300,000/year
Candidate added maintenance:             $180,000/year
Incremental annual savings:            $1,320,000/year
Upfront change cost:                     $350,000
Simple payback: 350,000 / 1,320,000 × 12 ≈ 3.18 months
```

This assumes equivalent useful outcomes, scope, and costs outside the comparison. Expand the model for differences in review, quality, operating controls, demand, and timing. The earlier $0.08-to-$0.006 per thousand tokens is a unit-price comparison, not a saving per call or a derivation of the annual example.

Other original scenarios, with their assumptions explicit:

- **500 users × 2,000 calls/user/year × $0.001/call = $1,000/year.** Even eliminating that charge entirely would take 200–400 years to recover a $200k–400k build before maintenance, discounting, or new benefits. That is an unattractive savings-only case, not a population estimate about most SaaS features.
- **$250k build / $7k annual savings ≈ 35.7 years**, before maintenance and discounting.
- **$65k savings − $120k annual maintenance = −$55k/year.** There is no positive operating-savings payback under those assumptions.
- **$400k build / ($1.7m savings − $200k maintenance) × 12 = 3.2 months.** A promising cost case still needs quality, feasibility, and control checks.

Labor-cost ratios of 10% or 50%, API-cost-to-margin bands of 2% or 10%, and eighteen- or twenty-four-month payback cutoffs are screening examples, not universal rules. A build may have worthwhile benefits other than lower token cost. Include current and plausible higher volume, such as a threefold scenario when justified, without assuming that growth will occur.

## Product illustrations: preserve what is actually known

**GitHub Copilot.** Subscription price multiplied by subscriber count estimates subscription revenue under strong assumptions; it does not estimate inference expense. The original inference-cost, cost-ratio, and months-to-payback assertions were unsupported by that arithmetic. Do not use them as disclosed GitHub economics. Verify current product, tier, usage and billing definitions for a live comparison.

**Intercom/Fin.** The original 2023–2024 story about tuning on 50,000 support transcripts for deterministic routing was not independently established. Primary [Fin research from September 2025](https://fin.ai/research/finetuning-retrieval-for-fin/) describes tuning retrieval on customer-support data. Intercom’s [March 2026 Apex announcement](https://www.intercom.com/blog/announcing-fin-apex-the-age-of-vertical-models-is-here/) describes a trained customer-service model. These show why retrieval, model adaptation, and a complete product should not be collapsed into one binary decision. Company performance claims remain company claims, and these later accounts do not verify the old dataset count or chronology.

**Notion AI.** The previous “no fine-tuning, including every structured feature” claim was not freshly verified. A product’s use of prompting or retrieval does not prove absence of tuning elsewhere in its stack or at another time.

**Harvey and Glean.** Retain them as historical examples of specialized product categories, not current recommendations or guarantees that a particular legal or search workflow is solved. Evaluate the actual product and terms against the task.

## Orchestration and retries

The original illustrative table assumes 100,000 requests at a $0.01 base cost:

| Assumed cost multiple | Monthly attempted-request cost |
|---|---:|
| 1× | $1,000 |
| 3–5× | $3,000–5,000 |
| 5–10× | $5,000–10,000 |
| 15–22× | $15,000–22,000 |

The multiplication is correct under those assumptions; mapping each band to a named architecture was not established. These are not break-even values per successful outcome until completion rates and all relevant costs are included.

[Anthropic’s research-system engineering account](https://www.anthropic.com/engineering/multi-agent-research-system) reports roughly 4× tokens for agents and 15× for multi-agent systems relative to chat interactions in its data. That is not a universal monetary multiplier or an equal-task cost comparison for every harness.

For same-cost attempts:

- One optional retry on 20% of requests gives expected attempts `1 + 0.20 = 1.20`.
- Repeated independent retries until success, with constant failure probability 0.20 and no cap, give `1 / (1 − 0.20) = 1.25` expected attempts.

Real retries may have different costs, correlated failures, caps, or partial reuse. Model those conditions. No universal >30% quality gain, <15% tuning gain, $0.10 outcome value, or 20% retry boundary establishes whether orchestration is worthwhile. Compare incremental outcome value with incremental lifecycle cost and consequence.

## Maintenance and migration

The earlier quarterly retraining, dedicated-engineer, 40%-allocation, twenty-four-month commitment, and three-to-fourfold debt claims were not general standards. Use a funded service and skill plan for the actual lifecycle. Managed tuning can retain responsibilities while changing who performs them.

The original model-update and migration schedules are also not promises. Some migrations are easy; others require substantial work despite a wrapper because capabilities and behavior differ. A suitable adapter can contain provider-specific logic while supporting task-level tests and permitted fallback. Record the trade-off rather than building a large abstraction by default.
