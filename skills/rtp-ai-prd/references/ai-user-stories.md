# AI user stories

Revision 1.1, 13 September 2026. Companion to AI-PRD v1.2.1 and the [PRD template](ai-prd-template.md).

Turn applicable product decisions into verifiable implementation work. Preserve the user or operational need, permissions, examples, failure behavior, ownership, monitoring, and economics without forcing every story to have a numerical confidence score or its own cost-per-outcome model.

The six areas below help reveal missing work. Existing shared infrastructure can cover an area; a feature does not always need six new tickets. Examples use the fictional draft-only Athena assistant. Numbers are candidate criteria to validate, not production facts.

## 1 Backlog coverage

| Area | PRD source | Required evidence where applicable |
|---|---|---|
| Capability | §1–2, §4–5, §7 | Intended behavior, permitted actions, relevant examples and evidence policy |
| Evaluation | §6 | Dataset coverage, label/rubric quality, judge validation, regressions and review capacity |
| Fallback | §7, §9 | Trigger, useful alternative, permissions/freshness, unavailable-alternative state |
| Guardrails | §2, §9 | Material failure, prevention/detection, containment, actual obligation |
| Instrumentation | §6, §10 | Event correctness, sources/joins, valid metric computation, missing-data behavior |
| Rollout and operations | §8, §12 | Exposure controls, decision criteria, recovery and appropriate experiment design |

Implement evaluation and instrumentation needed for shadow or live decisions before those decisions. A story that emits events has not necessarily produced a valid metric; a story that passes examples has not necessarily established generalization.

## 2 Reusable story template

```text
As a [user or operational role], I want [behavior]
so that [outcome linked to PRD §1 or a necessary enabling outcome].

Type and requirement source: [PRD section/version or shared requirement]
Acceptance criteria:
- Given [context and authority], when [trigger], then [observable behavior].
- Evidence required to proceed: [validated checks/score if relevant].
- Failure, refusal, or unavailable-dependency behavior: [...].
- Verification method and evidence of completion: [...].

Behavior/test examples: [relevant stable IDs and links]
Owner and coverage: [responsible person/role; escalation where needed]
Monitoring or change trigger: [relevant signal and decision, or justified N/A]
Cost implication: [feature target, overhead/budget, and allocation basis]
Assumptions and risks: [unresolved items with checks; or reviewed and none material]
Exposure/rollout dependency: [...]
Out of scope and permissions: [...]
```

Use relevant lines; record why a material field does not apply. Capability and fallback work can inherit the feature cost target. Eval, guardrail, instrumentation, and rollout work can state their overhead and allocation to that target. Do not invent a standalone success denominator. An unresolved assignment is a gap, not “owner: none by design.” No per-action reviewer may be necessary where authorized automation and process ownership are adequate.

## 3 Worked stories

### A1 Reviewable draft capability

As a support agent, I want a source-linked draft for routine tickets so that I can reduce composing time while preserving response quality. The PRD's illustrative target is 15% lower handle time, not an unrelated promise to halve it.

- Given authorized, current context and passing evidence checks, show an editable draft with supporting sources. Test the proposed P95 latency target of two seconds on the defined workload.
- If a calibrated score is used, implement the validated §7 policy. The example 0.85/0.70 bands remain provisional until evaluated; they never authorize sending or issuing refunds.
- Facts and commitments must be supported. With insufficient evidence, use the defined fallback or explain the gap. Preserve normal manual handling.
- Verify the actual permission boundary and representative G1, G2, B1, B2, R1, and R2 cases from PRD §4, plus broader test coverage.

**Ownership and operation:** CX quality role for behavior, engineering for runtime, assignments recorded before dependent exposure. Review quality and task-mix signals before assuming declining acceptance is model drift. Inherit the feature full-cost target and §11 allocation; verify all-attempt costs against verified resolutions. Assumptions: calibration, workload, and quality target need evidence. Auto-send is outside scope.

### A2 Evaluation dataset and regression workflow

As the quality owner, I want representative evaluations and a usable review process so that proposed changes can be assessed against the intended behavior.

- Define coverage by intent, difficulty, important failure, and relevant segment. An illustrative 500 cases is a planning count, not proof of sufficient precision.
- Link behavior examples to regression cases and preserve a separate holdout for generalization checks. Document provenance and sensitive-data handling.
- Validate automated judges against suitable reference labels; report relevant true-positive/true-negative measures with denominators, uncertainty, and disagreement handling.
- Exercise the release decision when a required check fails. Use binary checks for discrete requirements and graded rubrics where they preserve useful quality information.

**Ownership and operation:** evaluation role, with review coverage. Refresh meaningful failure patterns and investigate changes in judge performance or data mix. Estimate per-run and recurring review overhead against the feature budget; a proposed $15 test-run limit requires a billing basis. No invented user-facing confidence band is needed for this infrastructure story.

### A3 Source material when drafting is unavailable

As a support agent, I want useful authorized source material when no draft qualifies so that I can continue the task through the normal workflow.

- Given insufficient drafting evidence, show relevant permitted snippets only if they are available, current enough, and safe to display.
- Exercise empty, stale, unauthorized, and unavailable source states. Explain the actual limitation and preserve the manual path; a fallback cannot guarantee a useful answer for every case.
- Measure latency and log a safe reason code. A proposed three snippets within 800ms is an example to validate, not a universal requirement.

**Ownership and operation:** CX quality and retrieval roles as appropriate. Investigate changes in fallback volume alongside data mix and retained-answer quality; a 25% refusal rate does not itself prove miscalibration. Inherit feature economics and identify snippet-path overhead. Test relevant §4 bad/refer cases and access-boundary cases.

### A4 Disable affected behavior and recover

As the on-call engineer, I want an accessible control to disable the affected draft path so that an incident can be contained without waiting for a new deployment.

- Verify who may activate the control, what it stops, and what remains in flight. Define and measure a response target; “within 60 seconds” is a proposed target, not “immediately.”
- Preserve a validated manual or template path where safe. Exercise the unavailable-fallback case.
- Test the runbook, communication route, and restoration criteria. Use a suitable controlled drill; a production drill requires appropriate scope and authorization.
- Map automatic triggers to severity and evidence. A sampled average error threshold does not cover every critical incident.

**Ownership and operation:** on-call role and backup, with authority and access. Process ownership remains even without a per-action reviewer. Include control/monitoring overhead in feature costs and verify trigger coverage after relevant changes. Test the mapped §9 failure cases, including uncertain external effects; stopping future work does not undo completed effects.

### A5 Valid telemetry and outcome joins

As the product analyst, I want trustworthy events and outcome joins so that the team can compute the agreed metrics and detect gaps.

- Emit applicable safe identifiers, configuration references, elapsed latency, billing inputs, eligibility/display/fallback state, and relevant user action.
- Verify deduplication, population denominators, missing events, and joins to ticket resolution, surveys, or review labels where required.
- Reconcile a small known fixture end to end: eligible → shown → sent → verified outcome. Test failed and missing-label cases too.
- Enforce access, retention, sampling, and redaction requirements. Derive percentiles from event populations rather than storing a purported per-request P95.

**Ownership and operation:** data/analytics role. Alert on meaningful data-quality failures and version schema changes. An illustrative logging overhead limit such as 2% needs an explicit denominator and estimate. The feature may depend on this work before shadow mode; customer outcomes cannot all be inferred from generation logs.

### A6 Shadow operation and controlled exposure

As the PM, I want a bounded shadow phase followed by an appropriate exposure test so that we can verify operation before measuring user benefit.

- Shadow outputs are not displayed or executed. Protect data, bound spend, and evaluate representative outputs against valid reference labels.
- Record what shadow cannot answer: acceptance, review behavior, and causal user-outcome effects require relevant exposure evidence.
- If a controlled experiment is appropriate, verify team assignment, spillover assumptions, cluster count, and the power/evidence plan before ramping.
- Advance only when the checks required for that stage are met. Hold or stop on the defined conditions, and preserve accurate state when evidence is insufficient.

**Ownership and operation:** experiment owner with engineering and operations coverage. A two-week duration or five-percentage-point offline/online gap is illustrative and must fit volume, case mix, and uncertainty. Include shadow and experiment overhead in the budget. Link §8/§12 requirements and controls; running for a fixed number of days is not a passing result.

## 4 Grooming and completion review

- Confirm the user or enabling outcome and the current requirement source.
- Check coverage across the six relevant areas, including shared components and dependencies.
- Verify actual permission, applicable evidence policy, examples, failure behavior, ownership, and cost basis.
- Resolve contradictions between a story and the PRD explicitly; neither becomes current merely because it was edited last.
- Record unresolved assumptions and their decision deadlines. Do not invent uncertainty when review found no material gap.
- Mark completion only with appropriate evidence; distinguish implementation complete from exposure approved.

**User Story Health:** reviewed in-scope items with all applicable inherited requirements traceable and verifiable, divided by all reviewed in-scope items. Review applicability rather than rewarding filled blanks. Complete coverage is a readiness aid; it does not establish real-world quality by itself.
