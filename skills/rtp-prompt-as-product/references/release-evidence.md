# Release evidence and record

## Source notes checked 13 September 2026

[Anthropic, Demystifying evals for AI agents, 9 January 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) describes complementary evaluation methods, early definition of success, representative failure cases, balanced tests, and attention to grader quality. Its guidance supports starting with a useful small suite and extending coverage as the system matures. It does not establish this skill's example suite sizes as universal requirements or guarantee that layered checks eliminate all failures.

[Google's Site Reliability Workbook, Canarying Releases](https://sre.google/workbook/canarying-releases/) treats canarying as a limited deployment compared with a control. Population, duration, metric choice, work-unit length, isolation, and monitoring granularity affect interpretation. Before/after comparisons can be distorted by time and traffic changes. Shared dependencies can affect both populations, so absolute service thresholds also matter. The distinction in this skill between release-health canaries and product-effect experiments describes their decision purpose; it does not claim canarying is unrelated to A/B comparison.

These are engineering practice sources, not proof that every prompt edit needs a particular rollout percentage, duration, or recovery target. The prompt-specific release record and action-recovery cautions are design recommendations derived for this library. Keep empirical claims separate from illustrative numbers.

## Compact release record

| Field | What to record |
|---|---|
| Identity | Current and candidate prompt versions, owner, date, effective dependencies |
| Intent | Problem, expected improvement, proposed mechanism, plausible regressions |
| Criteria | Primary outcome, hard constraints, tolerable trade-offs, decision thresholds |
| Offline evidence | Suite/rubric versions, trial conditions, results, disagreements, untested areas |
| Live evidence | Why needed or omitted; assignment, cohorts, exposure, duration, denominators, uncertainty |
| Decision | Ship, iterate, limit, contain, or recover; exact scope and evidence rationale |
| Recovery | Tested target configuration, trigger, authorized operator, expected recovery time, in-flight handling |
| Action reconciliation | Completed/uncertain external actions, required corrections, owner, status |
| Follow-up | Monitoring, outcome lag, next review, unresolved question, resulting regression cases |

Use only the fields needed to make the current change understandable and recoverable. A prototype may need a few sentences. A consequential production release may need linked evaluation and incident records.
