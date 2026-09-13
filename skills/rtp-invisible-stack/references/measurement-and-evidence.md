# Invisible Stack: measurement and evidence

Reviewed 13 September 2026.

## When a component creates a mathematical ceiling

If task success S requires event A, with no alternative or recovery, then S is a subset of A and P(S) ≤ P(A). The dependency and population must match. If some tasks do not require retrieval, or a second tool supplies missing information, the blanket dependency does not hold.

Precision@5 is relevant retrieved items divided by five, averaged over a stated query set if applicable. It is not P(A) for “enough evidence to answer the task.” Two of five documents can be sufficient for a correct answer. All five can be relevant yet insufficient. Likewise, raw percentages for rule coverage, retrieval precision, schema validity, and tool success are not interchangeable component reliabilities whose minimum defines overall quality.

An ablation estimates the effect of a particular removal under tested conditions. Interaction and compensation matter. Removing a rarely needed control from ordinary examples may show no drop while leaving an important failure untested. Do not call this its universal “real contribution.”

## Legacy benchmarks are illustrations

The earlier skill suggested rule coverage above 90% and violations below 0.5%; retrieval Precision@5 above 70%, under 500 ms and empty results below 5%; guardrail false positives below 2% and safety-critical false negatives below 1%, with under 200 ms delay; orchestration success above 95%, fallback below 10%, and under two seconds; and monitoring detecting over 80% of problems before users with alerts inside an hour. These were practitioner starting points, not validated release thresholds. A 1% missed-harm rate may be unacceptable, and empty retrieval or fallback can be appropriate.

The three-to-four-second user tolerance, a few hundred baseline queries, quarterly audits, twenty reranking candidates and 100–200 ms reranking cost were also examples. Allocate and measure locally. Do not sum component P95 values or treat nominal mean delay as a tail guarantee.

Old database ranges—hosted $0.001–0.01/query, self-hosted $0.0001–0.001/query, 50–150 ms hosted latency, and a one-million-query migration trigger—were not verified and omit workload and cost scope. Pinecone, Weaviate Cloud, Qdrant, Milvus, and self-managed Weaviate were candidate examples, not a current shortlist recommendation. Verify capabilities and official prices for an actual selection.

## Intuit: platform illustration, not a universal sequence

The local April 2025 HBR case, “TurboTax Meets Turbo Innovation,” reports a curated data foundation and six platform components. The following preserves its component distinctions and historical claims, without treating them as a current architecture inventory:

| Reported component | Role in the case | CONTEXT relationship |
|---|---|---|
| Workbench | Model comparison and selection; 13 base models and up to 70 modified ones reported | Model choice and execution |
| Studio | Importing models in a few days | Development and onboarding |
| Runtime | Planning, orchestration, memory, execution, and company-knowledge retrieval | Several CONTEXT categories |
| Eval | Quality measurement and support for agent development | Evaluation across the system |
| SRF | Security, risk, and fraud controls | Rules and cross-cutting governance |
| UX | More than 140 reusable widgets and patterns | Presentation and interaction |

These are not a one-to-one map to the seven categories. The case’s chief data officer emphasized runtime; its reports of hundreds of teams and thousands of applications describe company-disclosed development activity, not independently established revenue or causal evidence that physical data consolidation is necessary everywhere. The original vague “modest business result” is not carried as a finding without a named metric.

[Intuit’s GenOS overview](https://www.intuit.com/blog/innovative-thinking/accelerating-development-velocity-with-major-enhancements-to-genos/) corroborates Workbench, Studio, Runtime, and a 140-plus-component UX framework. Its displayed update date does not establish that all described components were introduced on that date. A separate [Intuit release](https://investors.intuit.com/news-events/press-releases/detail/1272/intuit-rapidly-advances-genos-to-accelerate-development-of-agentic-ai-experiences-at-scale) describes expert handoffs, evaluation support, and model enhancements. These company accounts illustrate continuing changes across both models and supporting infrastructure, not proof that the model rarely matters.

## Technical debt and Novel Insights

[Sculley and colleagues’ 2014 paper](https://research.google/pubs/machine-learning-the-high-interest-credit-card-of-technical-debt/) identifies system-level maintenance risks including entanglement, hidden feedback loops, and data dependencies. The related [2015 paper](https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/) is the appropriate lineage for investigating the surrounding system; neither establishes a 10/90 quality split.

Novel Insights’ August AI/IT discussion motivates examining classification gaps and ownership across teams. Its anonymous advisory cases disclose no measured outcomes, so use the mechanism as a testable explanation. Reader-guide F separates capability, detection, and authority; K distinguishes useful knowledge from an assumed moat. These support explicit control checks and scoped data-value claims.

The local Hammer/Christensen and Lee–Mantia–McNeill material motivates questioning broken workflows before scaling them. It does not demonstrate inevitable data degradation from automation; a harmful feedback loop requires an actual reuse path. The local July 2026 MIT Sloan agent-economy article distinguishes private customer information from network verification records, with a disclosed author interest. Carry the conditional interoperability distinction, not its ownership forecast or an instruction to expose private records.
