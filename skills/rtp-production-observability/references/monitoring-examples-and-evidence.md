# Monitoring examples and evidence

Editorial review: 13 September 2026. No production traces, platform benchmarks, or live seeded-error trials were run for this wording revision.

## Historical threshold examples

These examples from the original skill are retained for discussion, not adopted as defaults:

| Signal | Original example | Clarification needed before use |
|---|---|---|
| Latency | p95 above 5 seconds; p99 above 10 seconds; first token above 2 seconds. | Task, interaction mode, baseline, window, and consequence. A first token may not be useful output. |
| Cost | Per-output cost rises 15%; cost per successful outcome rises 20%. | Relative comparison, price/task mix, success definition, and full cost scope. |
| Quality | Acceptance falls 3%; hallucination rises 1%; regeneration rises 20%; errors rise 2%. | Specify percentage points versus relative change, numerator/denominator, sample, uncertainty, and label quality. |
| Quality-drift examples | Context recall falls 4%; tenant hallucination rises 1.5%; acceptance falls 3% after prompt v7. | Comparable populations and evaluator versions; time association does not establish causation. |
| Handoff/context | Handoff delay exceeds twice baseline; quality falls at 50–60% context use. | Diagnose workload and state. Neither is a universal model threshold. |
| Responsiveness | Detect within 5 minutes, recover within 30 minutes, or automate rollback within 5 minutes. | Derive targets from harm, traffic, evidence delay, and feasible containment. |
| Sampling/retention | 10,000 of one million daily requests; 30- or 90-day retention. | Rare-event coverage, sampling bias, diagnosis needs, privacy, and applicable retention duties. |

## Primary source checks

- [CNCF OpenTelemetry project page](https://www.cncf.io/projects/OpenTelemetry/) records graduation on 11 May 2026; its [announcement](https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/) was published 21 May. Project graduation is distinct from the stability of every semantic convention.
- [OpenTelemetry GenAI events](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-events.md) documents `gen_ai.evaluation.result` and its association with an operation span or response ID. At review, the page is marked Development and notes implementation differences across languages. This contradicts the claim that span attributes are the sole canonical location for evaluation results.
- [Google SRE, Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) evaluates alerting through precision, recall, detection time, and reset time. Its examples use an error-budget context; adapt the method to the product and signal rather than importing thresholds blindly.
- [Anthropic, harness design for long-running applications](https://www.anthropic.com/engineering/harness-design-long-running-apps) describes context anxiety and differing behavior across tested models. It does not establish a universal 50–60% context-occupancy boundary or that most production model failures are harness failures.
- [Gu, Li, and Zhu working paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6417798), written 14 March 2026, posted 23 March and revised 12 June in the checked record, develops a game-theoretic model of adaptive review effort and coordination. The earlier July date describes related coverage, not the paper's origin. This is theory under assumptions, not a validated deployment diagnostic. The seeded-error instrument is the library's separate proposal.

## Hypotheses retained with limits

The original reporting-to-reality account is attributed to a practitioner piece with one anonymized advisory anecdote. It supplies candidate mechanisms—compression, incentives, and selection of voices—not a measured claim that every company has two organizations or that polish reduces accuracy. The original root-cause concentration estimate of 80% from roughly three causes is likewise a heuristic.

Novel Insights entry M highlights ceiling effects and the difficulty of isolating a human contribution from final outputs. Interaction records and controlled error-detection exercises can help; more discriminating tasks, adjudicated comparisons, and other valid outcome measures can also help. A ceiling on one measure does not erase all evidence, and a change in detection performance does not uniquely identify effort. The model-routing entry also supports recording served model identity, with uncertainty and authorization kept separate.
