# Day-one review template

**Feature/version:** [identity and effective dependencies]  
**Scope and launch time:** [users/tasks/exposure]  
**Decision owner and coverage:** [owner, on-call or equivalent, handovers]  
**Observation points:** [for example +1h/+6h/+24h, adjusted to the workflow]  
**Recovery/containment reference:** [tested procedure, authorized operator, limitations]

Set thresholds before exposure. For every observation include time window, denominator, coverage, baseline or target, and uncertainty where relevant. Status can be **green** (within the stated bar), **yellow** (investigate), **red** (act under the defined response), or **unknown** (not enough useful evidence). Blank and zero are different.

| # | Area | Measure and interpretation | Current observation / action |
|---:|---|---|---|
| 1 | Errors by severity | Verified outcomes per task/attempt; separate critical, high, medium, and low under the task's definitions | [counts/rates, coverage, threshold, owner] |
| 2 | P95 latency | Comparable end-to-end measure under stated load and sample; also examine blocking delays that a percentile hides | [baseline/target, observed, action] |
| 3 | Cost per user or outcome | Match period and population to the model; short-window extrapolation can be distorted by caches, setup cost, or traffic | [spend, units, scope, forecast uncertainty] |
| 4 | Activation | Eligible people exposed who perform the defined first action; low activation can reflect visibility, relevance, timing, or friction | [eligible/exposed/activated, window, follow-up] |
| 5 | Acceptance/use | Defined disposition with missing data shown; distinguish reuse from independently verified quality | [used/edited/rejected/unknown, reasons] |
| 6 | Groundedness or factual errors | Verified unsupported/incorrect outputs from an appropriate sample; user flags are leads, not the error-rate denominator | [reviewed outputs, errors, coverage] |
| 7 | Confidence calibration | If a meaningful numeric confidence signal exists, compare predictions with verified outcomes; acceptance is not calibration | [method, sufficient data?, result or not applicable] |
| 8 | Support volume | Feature-related contacts relative to exposed users/tasks; classify severity, repeat contacts, and reporting delay | [counts, rate, themes, capacity] |
| 9 | Recovery health | Known compatible recovery target, drill evidence, access, in-flight handling, and completed-action reconciliation | [ready/gap, owner, action] |
| 10 | Safety incidents | Actual incidents and near misses; distinguish detection signals from verified harm and confirm containment | [event, severity, scope, response] |

## Compact time-series record

| Review time | Metric and sample | Observation against bar | Status and reason | Decision/action | Owner and next check |
|---|---|---|---|---|---|
| [time] | [defined measure] | [value, denominator, uncertainty] | [green/yellow/red/unknown] | [continue/limit/investigate/contain/recover] | [person/time] |

Use the actual thresholds agreed for this release. Do not copy the former universal 5% activation, 70% acceptance, 3% flagged-output, eight-second latency, or 0.5% support gates. Those values have no general validity across products, and a flag rate is not a hallucination rate.

Respond to the consequence and its cause. A single critical event can override the schedule. Multiple signals can share one cause and should not be counted as independent proof. A green first day does not close unresolved long-term quality or retention questions.
