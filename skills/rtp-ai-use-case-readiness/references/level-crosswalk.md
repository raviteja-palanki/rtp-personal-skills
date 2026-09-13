# Reading older autonomy assessments

Before v2.6.1, AI Use Case Readiness used a different numbered scale from its imported `rtp-autonomy-spectrum`. In particular, readiness called a copilot level 3 and a supervised agent level 4, while the shared spectrum called a copilot level 4 and an agent level 5. The two uses of level 7 also described different properties.

The revised readiness skill uses the shared seven names, with level 0 as a non-AI comparator. The operational description remains authoritative: what the system may decide or execute, under which conditions, and what a person must do. Labels are shorthand and do not grant permissions.

| Older readiness label | Intended behavior in that version | How to read it now |
|---|---|---|
| 0 — No AI | Deterministic if/then rules | Baseline without AI; specify any automatic actions and controls |
| 1 — Rules engine | Decision trees and business logic | Also a non-AI baseline unless a probabilistic component is actually present; do not relabel it an AI Feature simply because the digit matches |
| 2 — AI for one task | Classification, extraction, ranking, or one generated output | Often an AI Feature; conversational or user-directed use may fit another shared label |
| 3 — Copilot | Drafts reviewed and approved by a person | Shared Copilot, typically label 4, with the review contract retained |
| 4 — Supervised agent | Multiple actions with escalation and asynchronous/batch review | Shared Agent, typically label 5; specify which actions occur before review and their limits |
| 5 — Bounded agent | Scoped permissions and exception audits | Shared Agent or Autonomous Agent depending on independence and supervision; “bounded” remains a requirement, not a unique numeric level |
| 6 — Semi-autonomous | Independent work in a narrow domain with anomaly intervention | Usually shared Autonomous Agent, label 6, after checking the actual rights and operating contract |
| 7 — Fully autonomous across domains | Broad independent decisions with minimal oversight | No automatic mapping. Shared label 7 means multiple agents, not unlimited cross-domain authority; reassess scope explicitly |

Preserve the version of an old assessment when quoting it. During migration, write both the previous label and the current operational interpretation. If the original assessment lacks enough information, mark the rights unresolved rather than guessing a conversion.

The shared spectrum itself is a library taxonomy, not a universal standard or a calibrated risk scale. A scripted workflow can execute consequential actions. A multi-agent system can be read-only. Approval requirements and consequence exposure must therefore be described independently of interface names, agent count, and numbering.

## Earlier numerical examples

The old rollout illustration proposed:

- Phase 1: assistive operation, roughly 20% savings, over 30% acceptance, and zero critical failures.
- Phase 2: bounded operation, roughly 50% savings, under 2% escalation, and under 0.5% critical errors.
- Phase 3: higher independence, roughly 70% savings, zero critical errors for four weeks, and policy approval.

These figures were teaching examples, not measured outcomes or approved release thresholds. They also risked making a later phase appear allowed to have more critical errors than an earlier one. Do not carry them into a deployment by default. Define error severity, denominator, exposure, sample, observation period, required checks, and uncertainty for the intended action.

Likewise, the previous $100,000/100-user consequence limits, $500,000 annual-upside threshold, economic bands below $50,000 / $50,000–$500,000 / above $500,000, tenfold control-cost comparison, and six-month trust-recovery period are illustrative. A small monetary loss can coexist with severe nonfinancial harm. High revenue does not authorize that harm, and low-frequency work may still have substantial value.

The previous hypothesis examples—40% acceptance in two weeks, 50% time reduction in two months, 20% escalation, and bypassing within three weeks—show the kinds of signals to specify. Actual thresholds require a baseline, justified target, outcome relevance, and a defined decision. Low escalation is not inherently good if the system should have asked for help.
