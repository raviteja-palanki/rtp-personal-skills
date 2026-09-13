---
name: ship-decision
version: v1.2.1_latest
description: 'Make an evidence-based go/no-go decision for an AI feature at the proposed launch scope. Use before a pilot, production release, material capability change, or expansion. Review seven areas: safety and authority, reliability, economics, observability, user understanding, graceful degradation, and accountable release approval. Define task-specific constraints and thresholds before evaluating; distinguish observed error rates from what the sample can establish. Include proportionate regression checks, staged exposure, tested recovery, and a day-one review with ten monitoring areas. Compare launch, narrower launch, delay, and stop, including the cost of inaction. Recognize evidence-based decisions to end failing work without rewarding arbitrary cancellations. Internal, experimental, or pre-PMF status changes review depth but does not remove consequential risks. Pairs with eval-framework, stress-test, safety-as-moat, failure-modes, cost-model, agent-risk, and prompt-as-product.'
imports: [stress-test, safety-as-moat, failure-modes, cost-model]
---

# Ship Decision

Decide **whether this version should reach these users, for these tasks, under these controls**. A release decision applies to a defined scope; it is not a declaration that the system is safe for every use.

Start before the final launch week. Agree on the customer problem, intended benefit, permitted actions, hard constraints, evidence needed, and accountable decision owner. Use existing answers rather than repeating grounding questions. A small internal draft tool can have a short review; a tool affecting medical care, money, employment, or sensitive information needs stronger evidence regardless of its “pilot” label.

## Choose the decision and the right review depth

Compare four options: **launch, launch with narrower scope, hold for specific work, or stop**. Record the benefit, cost, risk, and learning each option creates over a comparable horizon. Include the costs of waiting and continuing the current process; do not invent monetary precision where it is unavailable.

A **hard constraint** rules out an option within the current decision authority. A **preference or soft constraint** permits trade-offs under the organization's stated objective. Agree on the distinction before seeing results. A funded loss can be a legitimate business choice; it does not authorize a safety or legal violation.

Revisit the decision at useful points:

1. **Before development:** value, feasibility, scope, and foreseeable risks.
2. **Before pilot exposure:** evidence, protections, measurement, and recovery.
3. **Before expansion:** observed outcomes, new populations, scale, and support capacity.
4. **After launch:** scheduled and event-triggered checks for drift or changed conditions.

These are decision purposes, not four mandatory meetings. Reuse applicable prior reviews after checking their version, scope, and unresolved conditions. Internal use, opt-in, automatic rollback, a short experiment, or pre-PMF status may justify a lighter process; none alone establishes low risk.

## Seven readiness areas

### 1. Safety, authority, and applicable obligations

Describe concrete failure scenarios and affected people. For each, record likelihood or uncertainty, consequence severity, exposure, detectability, recovery limits, mitigation, and owner. Distinguish how many people are affected from how serious the harm is.

Examples to investigate include fabricated legal citations, contraindicated clinical suggestions, unsuitable financial recommendations, discriminatory screening, and unauthorized actions. The consequences depend on how the feature is used; a wrong draft and an executed decision have different exposure.

Check four things:

- **Failure coverage:** use `failure-modes` and `stress-test` to examine normal failures, misuse, adversarial inputs, and dependencies. Document remaining blind spots.
- **Effective mitigations:** appropriate refusals or scope limits, input/output validation, access controls, human review where useful, user recourse, and monitoring. Test both harmful actions and unnecessary refusal of legitimate work.
- **Adversarial evidence:** record what was tried, conditions, outcomes, fixes, and residual risk. A two-hour exercise can start discovery; it does not certify resistance. High-consequence gaps may require stronger testing or narrower exposure.
- **Applicable review:** identify the actual domain, data, jurisdiction, contracts, and organizational rules. Obtain required legal, privacy, security, clinical, or other specialist decisions; a generic checklist is not a legal conclusion.

Do not treat HIPAA, SOC 2, and FedRAMP as interchangeable regulatory approvals. HIPAA obligations depend on the covered activity and entity; private “certification” does not remove them. SOC 2 is a scoped controls examination and report. FedRAMP concerns federal cloud use and has its own applicable requirements. Verify the relevant status rather than assuming every feature needs all three. See [Evidence and calculation notes](references/ship-evidence.md).

For an unmet requirement, choose a mitigation, a narrower scope, a hold, or a documented residual-risk decision by someone who has that authority. Some risks cannot be accepted within the team's authority. An AI label, terms of service, or a board's willingness to fund losses does not substitute for required controls.

### 2. Reliability evidence that matches the claim

Define success and error severity before testing. Include representative tasks, important subgroups, known failures, boundary cases, and adversarial tests as appropriate. Keep separate the set used to estimate typical performance and the set deliberately enriched with rare risks.

**150 cases can be a starting suite, not proof of a rare-error threshold.** Choose sample size, trial design, uncertainty reporting, and acceptance criteria to support the proposed decision. Evaluate the effective prompt, model, context, tools, and configuration that will be released. A run 48 hours before launch is a possible operational checkpoint, not a guarantee of freshness; rerun affected checks after material changes.

| Severity | Meaning to define for this task | Decision implication |
|---|---|---|
| Catastrophic / critical | Severe harm or a prohibited consequence | Treat observed cases and credible uncovered paths as urgent blockers or containment triggers under the applicable risk policy |
| High | Materially wrong outcome, substantial disruption, or significant loss | Set a task-specific tolerance and validate mitigations and recovery |
| Medium | Meaningful degradation with a feasible workaround | Assess rate, burden, affected groups, and accepted trade-offs |
| Low | Minor deviation with limited consequence | Track when it matters to usability or accumulated burden |

The original example tolerances—**<0.1%, <1%, <5%, and <10%**—are retained as an arithmetic illustration in the reference. They are not a safe default for catastrophic errors. With 0 failures in 150 independent, representative trials and reliable detection, the one-sided 95% binomial upper bound is about **1.98%**, not below 0.1%. Even a statistical bound does not replace analysis of plausible severe failures.

If a feature has 98% verified task accuracy across 10,000 comparable daily attempts, the implied expected count is 200 unsuccessful attempts. It is not necessarily 200 hallucinations, 200 distinct harmed users, or an acceptable outcome. User count alone does not provide the attempt volume. Reversibility and uncertainty communication can help but do not decide acceptability on their own.

Set user-relevant latency and availability targets. For an illustrative P50 target of 1,000 ms and P95 target of 3,000 ms, measurements of 950 ms and 4,200 ms meet the median target and miss the tail target. Investigate the user impact and load conditions rather than assuming all users will abandon.

For time-based availability over 30 continuous days:

| Availability | Allowed unavailability |
|---|---:|
| 99% | 7 hours 12 minutes |
| 99.9% | 43 minutes 12 seconds |
| 99.99% | 4 minutes 19.2 seconds |

Choose the service indicator, denominator, window, exclusions, and contract meaning explicitly. Request-success availability differs from time-based uptime. Staging load tests and failure drills inform readiness; they do not verify future production availability.

### 3. Economics and capacity at the intended scale

Use `cost-model` to connect total relevant cost to verified outcomes, account usage, revenue, and capacity. Test plausible growth, heavier tasks, retries, human review, vendor pricing, and failure scenarios. Tenfold usage is a useful stress scenario when relevant, not a universal requirement that every feature must survive unlimited growth profitably.

**Corrected illustrative example:** at $0.08 per user per day, cost is $2.40 per user over 30 days. Against $30 monthly revenue, the margin on this cost scope is **92%**, before omitted costs. At $0.03/day it is 97%. Neither is a loss. Growth can still create a cash, capacity, or quality problem even when unit contribution is positive.

For a material investment, apply four finance disciplines:

1. Compare alternatives, including smaller scope and continuing the current process.
2. Identify the relevant unit's invested capital and returns; scale the accounting effort to the decision.
3. Use a current, appropriate capital cost matched to the cash-flow measure, with finance support where needed.
4. Use explicit scenarios and consistent assumptions instead of a single unexplained forecast.

The historical source's roughly 9% cost-of-equity anchor is not a rate to copy into every AI case. Cost of equity and a discount rate for total firm cash flows are not interchangeable.

Define spend, unit-cost, and capacity alerts with an owner and response. The original 20% monthly-growth and 30%-over-budget triggers are possible local settings, not universal emergencies: healthy usage growth can raise spend. Include budget limits, throttling, scope reduction, or a controlled pause where useful. A planned investment loss needs a funding limit, authorized sponsor, learning objective, and review/exit condition; it does not always require a board meeting.

### 4. Observability and operational response

Before meaningful exposure, confirm that the team can detect important failures, identify affected versions and users, and act. Instrument only data that can be handled appropriately, with access, retention, and privacy controls.

Cover four groups:

- **Quality:** task outcomes, error severity, groundedness where relevant, sampled independent review, user feedback, and important subgroup differences.
- **Performance:** end-to-end latency, timeouts, dependency failures, queueing, and availability under the chosen definition.
- **Cost:** spend, cost per task/outcome/account, token and tool usage, retries, and review burden.
- **Behavior:** eligible exposure, activation, usage, engagement, retention, abandonment, and corrections with defined denominators and windows.

Feedback counts are not verified error rates, and absence of complaints is not proof of quality. Set appropriate evaluation and review cadence; daily full-suite runs or every latency percentile are not mandatory for every feature.

Test alerts and runbooks with the people responsible for responding. Define who has authority to limit or stop the capability, coverage hours, backup coverage, and escalation. A dashboard without usable response ownership is an incomplete control.

### 5. User understanding and recourse

Help users understand the feature's purpose, limits, evidence, and available actions at the point of use. Apply required AI disclosures and suitable product labels without relying on a generic warning to teach the workflow.

State actual scope and information freshness. Do not copy an arbitrary model cutoff into the UI if retrieval or other sources change what the feature knows. Show calibrated probabilities or intervals only when they are defined, validated, and useful; model-written “90% confident” is not enough. Use plain uncertainty and source limitations when numeric calibration is unavailable.

Provide a way to report a bad output, correct information, undo supported actions, or reach appropriate assistance. For consequential use, make the relevant review and escalation path usable and adequately staffed. Test comprehension and behavior; disclosure alone does not guarantee understanding, safe reliance, or reduced liability.

### 6. Graceful degradation and recovery

Choose a response for each failure condition, and test it under realistic limits. A **fallback** supplies a reduced or alternative service. A **rollback** restores a prior configuration. **Containment** limits further harm; completed actions may still need reconciliation or correction.

| Condition | Possible response | Essential check |
|---|---|---|
| Model or dependency unavailable | Explain unavailability, offer a reliable alternative, queue work, or route to staffed assistance | Alternative works at the needed capacity and does not imply completion |
| Latency exceeds the task limit | Show truthful progress, offer cancellation or asynchronous completion, shed approved load | No misleading progress or indefinite waits; state queue and priority rules |
| Budget or capacity limit reached | Apply agreed usage limits, route to a cheaper adequate method, restrict exposure, or pause | Respect contracts, user expectations, and permitted service priorities |
| Quality or safety degrades | Restrict affected tasks, strengthen review, recover a compatible version, or disable the capability | Do not simply lower a displayed confidence number while continuing unsafe work |

Cached output is usable only when its scope, authorization, freshness, and relevance still hold; another session's output is not automatically a valid fallback. Humans and deterministic alternatives also have failure modes and capacity limits.

Set recovery speed from consequence and architecture. The former 30-minute target may suit some services and be far too slow for others. Confirm how in-flight tasks retain coherent versions and how uncertain external writes are reconciled. Restoring a version does not reverse a sent message, payment, disclosure, or data mutation; if the old version is unsafe or incompatible, use another containment path.

### 7. Accountable release decision

Review each applicable area and name any unresolved condition. The authorized owner records the decision, scope, evidence, residual risk, and next review. Product, engineering, operations, legal, finance, and domain specialists participate where the actual policy or decision requires them; unanimity of four job titles is not a universal rule.

| Status | Meaning |
|---|---|
| Ready for stated scope | Evidence and controls satisfy the applicable requirements |
| Ready with bounded conditions | Remaining issues are within authorized tolerance; restrictions, owner, and expiry/review are explicit |
| Hold | A named requirement or evidence gap must be resolved before the proposed exposure |
| Stop or redesign | The present approach lacks a defensible path under the stated constraints |

A recommendation can be complete while an external approval remains pending. Never invent sign-off, deployed dashboards, completed tests, or a scheduled review. Mark actual status and distinguish preparation from authorization to launch.

## Make deployment checks repeatable

Use automated regression gates for relevant prompt, model, context, retrieval, tool, routing, and agent-role changes. Test affected components and important end-to-end workflows against pre-agreed constraints and regression tolerances. Exact test scope depends on impact; combine automated checks with human judgment where necessary.

Do not block on arbitrary fluctuations or require every metric to improve. Express thresholds clearly as relative changes or percentage points, with a baseline, denominator, window, minimum evidence, and response. Distinguish a broken environment from a failed feature. Define an auditable exception or urgent-fix path within existing authority; no exception can override a binding obligation simply because the board approves a loss leader.

For agent systems, component success is not sufficient evidence for the whole workflow. If the pipeline fails, examine handoffs, shared state, tools, orchestration, resource limits, and task composition. It is not necessarily a handoff problem.

Deploy components independently when compatibility permits. A planner-first order and separate role rollouts can aid diagnosis, but coupled changes sometimes require a tested compatible bundle. Record the effective bundle and dependency contracts rather than forcing an incompatible intermediate state.

## Stage exposure according to risk and useful evidence

A progression such as **1% → 5% → 25% → 100%** can limit early exposure. Adapt fractions and timing to traffic, task duration, consequence, and representativeness; test tenants or a small site set may be a better unit. Do not advance merely because a percentage or clock interval has elapsed. `prompt-as-product` explains release canaries and controlled product experiments.

Use quality, safety, cost, and latency triggers grounded in the release criteria. The historical examples of +10% errors, +50% cost, 1.5× P95 latency, or a two-standard-deviation flag increase need local justification; they are not universal failure detectors. Rare events, changing sample sizes, and correlated measures make a generic “2σ” rule unreliable.

Contain known serious harm immediately under the incident plan. Do not wait two hours to understand the root cause before acting. For less consequential deviations, diagnose within the agreed window and decide whether to pause expansion, continue scoped observation, or recover. Preserve the evidence needed to learn.

## Day-one review and continued monitoring

Assign the release owner and operational coverage, including handover. Two named people do not need to remain awake for 24 hours. A review at **+1 hour, +6 hours, and +24 hours** is a useful starting pattern for some launches; adapt it to operating hours, batch duration, user activity, and outcome delay.

The [Day-one review template](references/day-one-review.md) retains ten monitoring areas: severity errors, latency, cost, activation, acceptance/use, groundedness errors, confidence calibration, support volume, recovery health, and safety incidents. For each, set the applicable threshold and record observations, sample size, uncertainty, status, and action. Use **unknown/insufficient data** where appropriate instead of assigning green to an empty sample.

Severity and causal context determine action. One critical incident can require immediate containment; two unrelated adoption metrics below plan need not trigger rollback. Multiple warnings should be investigated for a shared cause without automatically counting correlated signals as independent evidence. A useful color system supports judgment rather than replacing it.

All green at 24 hours means the observed checks passed for that window. It does not establish long-term stability or justify automatically reducing review to weekly. Continue until delayed outcomes, meaningful usage cycles, and relevant failure paths have been observed, then set ongoing and event-triggered review with `production-observability`.

## Make difficult decisions easier to surface

Launch pressure and recent successful demos can hide failures. Indefinite caution can also hide the cost of waiting. Compare evidence for both directions, include reasonable alternatives, and set the next decision point. Do not assume competitors are reckless or that a tired team will inevitably fail; address capacity and coverage concretely.

Ask whether governance can change the work: what has it approved with conditions, narrowed, improved, delayed, or stopped, and can its controls be exercised? A history of stops can be evidence of authority. No stops in twelve months is not proof that a gate is cosmetic; prevention, upstream changes, proposal quality, and tested authority matter too. A helpful review and a real stopping power can coexist.

Recognize people who bring sound evidence that their own initiative should end or change. Protect their reputation, acknowledge avoided waste, and make the decision criteria clear. Linda Hill reports leaders rewarding such decisions, including one offering a bonus; this is qualitative support for a practice to test, not a required incentive program. Reward decision quality and valuable learning as well as successful delivery, and watch for premature cancellation or metric gaming. Do not reward the number of projects killed.

## Final readiness check and output

- [ ] Concrete failure modes, tested controls, and applicable specialist decisions.
- [ ] Reliability evidence with severity, sampling limits, and appropriate performance targets.
- [ ] Economics and capacity assessed for the release scope and credible growth scenarios.
- [ ] Monitoring, alerts, accountable response, and coverage ready for exposure.
- [ ] Users can understand the capability, limits, and relevant recourse.
- [ ] Fallback, containment, recovery, and action reconciliation tested at the needed scope.
- [ ] Decision authority, exact release scope, residual conditions, and approval status recorded.
- [ ] Recovery triggers and operators are clear.
- [ ] Initial and subsequent reviews have owners and an actual plan.

Deliver the **decision, scope, evidence, unmet conditions, principal trade-off, and next action with owner/date**. Link supporting evals and runbooks when available. Match the requested format; use a short memo or inline answer unless a fuller artifact is useful. A diagram is optional if it clarifies exposure stages or recovery ownership. The [concept guide](CONCEPT.md) gives worked scenarios, and the shared Universal Skill Protocol provides cross-skill handoff conventions.
