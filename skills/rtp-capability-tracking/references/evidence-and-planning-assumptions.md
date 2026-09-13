# Evidence and planning assumptions

This reference preserves the earlier skill's examples and research connections while separating observations from rules. Consult it when interpreting a forecast or explaining the basis for a recommendation.

## Model progress: use the dated version and its measurement scope

The [MIT FutureTech paper, arXiv v3, 23 July 2026](https://arxiv.org/html/2604.01363v3), examines over 6,000 text-based O*NET tasks and over 60,000 worker evaluations. It finds broad improvement across the studied tasks. The task instances were self-contained; filtering required sufficient information without external inputs. Model responses were evaluated by experienced workers. These observations concern the constructed tasks, not every part of the associated occupations.

Its abstract reports roughly 60% success on tasks estimated to take humans about 1.5 hours in 2024 Q2, rising above 70% by 2025 Q3. Its 88–97% projection for 2030 concerns minimally sufficient quality and assumes continuation of the estimated trend. This is not a commitment about a particular capability. Earlier versions have different counts and projections; cite v3 explicitly when using these figures.

The [MIT Sloan article, 5 August 2026](https://mitsloan.mit.edu/ideas-made-to-matter/how-will-ai-automation-hit-a-crashing-wave-or-a-rising-tide), reports a 2.2–2.8-year failure-halving interval and roughly 50–75% minimally sufficient performance across models. It distinguishes legal text tasks from text tasks associated with maintenance and repair. The latter does not measure turning a wrench. Its explanation also cautions against reading capability success as the share of work that should be automated.

**Application to this skill:** keep task quality, workflow execution, and commercial advantage separate. Gathering information can be a substantial cost, but the evidence does not establish that it is always the more expensive half. Input assembly can be measured alongside model quality; these are connected parts of a workflow rather than mathematically orthogonal outcomes. Benchmark ratings against a worker-quality rubric are not automatically a matched trial of people and AI performing the complete job. Before claiming substitution, inspect the actual comparison design and the operating constraints.

The Novel Insights ledger's H and P entries highlight input assembly and the possibility of shifting acceptance standards. Apply these as questions to investigate. A ticket escalation is one possible indicator of coordination; it is not identical to every handoff. Seed known-bad cases and keep objective task checks where possible, alongside the applicable acceptance rubric. Do not treat an occupation-level ordering as proof that answer invariance caused it: task selection, scoring, familiarity, and other differences remain possible explanations.

## Legacy half-life ranges: retained for traceability, not forecasting defaults

The earlier skill proposed the following ranges without supporting estimates of their general validity:

| Advantage category | Earlier planning range |
|---|---|
| Prompt technique | 3–6 months |
| Retrieval or RAG | 6–12 months |
| Fine-tuning | 12–18 months |
| Data flywheel | 24–36 months |
| Harness or orchestration | 12–24 months |

It also proposed extending a niche advantage by 1.5–2×, shortening a general-market advantage by 0.5×, and using 24–36 months for proprietary data, 18–24 months for integration, or 1–3 months for prompts alone. These are **unvalidated scenario inputs**, not facts to place in a decision register. If used for a sensitivity exercise, label them as assumptions and include alternatives.

The useful mechanisms remain: accessible techniques can spread, base models can narrow a performance gap, data can become outdated or replicable, integrations can be costly to replace, and specialized context can matter. The opposite can also occur. A prompt may retain operational value, a niche may attract strong competition, and a dataset may offer little incremental advantage. Test the mechanism locally.

Earlier examples used a ranking system that was 18 months old to infer a nine-month half-life. Age alone cannot establish the decay rate. Likewise, a calendar passing the estimated half-life is not evidence that an advantage is dead. The example of a January 2022 asset reviewed in January 2025 spans 36 months, not 20.

## Harness examples are hypotheses, not model specifications

Planner, memory, fact-checking, routing, and fallback/cache examples illustrate assumptions worth testing. Earlier named-model examples claimed native 50-step planning, guaranteed deterministic output, particular context thresholds, and date-error rates without adequate supporting measurements; one also placed a model in an inconsistent release chronology. Use neutral model A/model B examples until a current, task-specific test establishes the result.

The useful example is conditional: if direct execution meets the same requirements with less latency, cost, or complexity, consider removing a separate planner. Re-test the responsibilities it served. Larger context capacity does not establish reliable use of all history, and apparently repeatable responses do not remove recovery, freshness, or auditing requirements.

## Other historical connections and their limits

- **Commercial aviation:** the earlier skill relayed an EASA passenger-flight autonomy estimate through Drover and Huang, MIT Sloan Management Review, 18 November 2025. This revision does not verify that forecast or treat autopilot performance as evidence that full flight autonomy was technically solved. The preserved lesson is to check accountability, assurance, safety, and applicable requirements separately from a narrow capability result.
- **AI wall:** the HBR article [“Gen AI Won't Make Your Employees Experts,” March–April 2026](https://hbr.org/2026/03/gen-ai-wont-make-your-employees-experts), discusses limits to assistance outside a person's expertise. The earlier skill describes experts, adjacent outsiders, and distant outsiders on a writing task. Carry that setting; it does not prove experts always gain more on every task or that a novice can never learn effectively with AI.
- **Expertise stock and formation:** Novel Insights P asks whether a study of established expertise can answer a question about future learning. That is useful. Its older assertion that all relevant participants learned before AI, or that no formation research exists, is not established by a small article corpus. Look for longitudinal retention and transfer evidence for the actual cohort.
- **Moving baselines:** Novel Insights M and its later metric discussion warn against mistaking a changed comparator for a changed person. Revenue per employee includes the effects of accumulated assets and business model. It can remain a useful descriptive ratio; the error is attributing its whole value to AI or current staffing without a suitable comparison.
- **Declared AI maturity:** posts, earnings calls, job advertisements, and patents measure different signals from actual use. They may still predict use. Treat the ledger's proposed declaration bias as a hypothesis requiring validation, rather than declaring every such index invalid.

Primary pages were checked on 13 September 2026 for the specific statements attributed above. Historical examples retained from the supplied skill are labeled as such; their presence does not imply a new full-source audit.
