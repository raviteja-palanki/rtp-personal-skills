# AI Product Metrics Dashboard Template

Choose the sections needed for the decision. Replace illustrative thresholds with justified local ones. A blank or unavailable value is not zero, and a status cannot be green before its check is defined and evaluated.

**Product / interaction:** [Name and scope]  
**Decision and owner:** [What this review informs]  
**Period / data as of:** [Dates, timezone, and maturation delay]  
**Configuration:** [Relevant model, prompt, harness, retrieval, and metric versions]  
**Population:** [Eligible users/tasks; important exclusions]  
**North Star or primary outcome:** [User value, definition, and limitations]

## Outcome and business view

| View | Measure and definition | Current / baseline | Target or decision condition | Evidence and uncertainty | Owner / action |
|---|---|---|---|---|---|
| Enablement | [Relevant data/capability/control readiness] | — | — | — | — |
| Value created | [Useful work with required quality] | — | — | — | — |
| Value realized | [Actual benefit; distinguish modeled estimates] | — | — | — | — |

## AARRR, where relevant

| Stage | Candidate measure | Interpretation to validate |
|---|---|---|
| Acquisition | Qualified trial conversion by channel. | Eligible exposure and audience differences. |
| Activation | Users reaching a defined first useful outcome. | Time, edits, assistance, and eventual success. |
| Retention | Useful repeat use at the natural task cadence. | Opportunity to return and cohort maturity. |
| Revenue | Revenue plus a separately defined contribution/margin view. | Recognized revenue, included costs, and workload. |
| Referral | Intentional referrals and appropriately measured sharing. | Sharing does not itself establish endorsement or conversion. |

## AI funnel by interaction

| Transition | Eligible count | Reached next stage | Conversion and window | Known drop-off reasons / unknowns | Decision |
|---|---|---|---|---|---|
| Provisioned → first invocation, if relevant | — | — | — | Include censored and revoked access. | — |
| Surfaced → invoked | — | — | — | — | — |
| Invoked → completed | — | — | — | Separate success, correct refusal, cancellation, error, and pending. | — |
| Completed → accepted | — | — | — | Separate edited, as-is, inferred, and unknown acceptance. | — |
| Accepted → useful return | — | — | — | Use a task-appropriate return window. | — |

Some workflows branch or repeat stages; adapt the model and avoid mismatched denominators.

## Quality, effort, and companion measures

| Measure | Current / baseline | Count and denominator | Trend / uncertainty | Companion measure | Response condition |
|---|---|---|---|---|---|
| Verified task success | — | — | — | Severe failures / partial outcomes | — |
| Acceptance | — | — | — | Sampled correctness / review quality | — |
| Corrections and meaningful edit burden | — | — | — | Reason for edit / post-use repairs | — |
| Regeneration | — | — | — | Defect repair versus exploration | — |
| Conversational burden | — | — | — | Task complexity / successful outcome | — |
| Abandonment | — | — | — | Work completed elsewhere / pending | — |
| Escalation and intervention | — | — | — | Missed exceptions / reviewer capacity | — |
| Unsupported or false claims | — | [Claims, outputs, or tasks—specify] | — | Severity / omissions | — |
| False positives / negatives, where applicable | — | [Defined positive class and eligible cases] | — | Precision, recall, prevalence | — |
| Calibration or judge performance | — | — | — | Relevant severe and minority cases | — |
| Satisfaction distribution | — | — | — | Direct feedback / task effort | — |

## Repeated-trial and trajectory evidence

| Task group | Cases / attempts | pass@1 | pass@k, specify k | pass^k, specify k | Actual trajectory checks | Configuration / uncertainty |
|---|---|---|---|---|---|---|
| Representative workload | — | — | — | — | — | — |
| Consequential failure cases | — | — | — | — | — | — |
| Relevant segment | — | — | — | — | — | — |

Do not infer a multi-step success probability from repeated independent-trial formulas without the required assumptions. High scores are evidence for this evaluation, not a complete launch decision.

## Costs and latency

| Cost category | Period cost | Per attempted task | Per successful outcome | Allocation / uncertainty |
|---|---|---|---|---|
| Model/inference | — | — | — | — |
| Tools, retrieval, runtime, infrastructure | — | — | — | Avoid double-counting model compute. |
| Human review and correction | — | — | — | Cases × time/case × loaded rate. |
| Other included costs | — | — | — | — |
| Total | — | — | — | Match the outcome population and window. |

Report tokens separately from currency. Cost per success is undefined when the successful-outcome count is zero. Name fixed-cost allocation and delayed success handling.

| Latency measure | p50 | p95 | p99, if useful | Load / device context | Budget / response |
|---|---|---|---|---|---|
| Response onset | — | — | — | — | — |
| Useful result | — | — | — | — | — |
| Complete task, including relevant human time | — | — | — | — | — |

## Cohorts, discovery, and decisions

Compare relevant user/task/configuration cohorts with sample counts. Keep a fixed task-mix comparison when the live mix changes. Do not publish identifiable small groups without an appropriate basis.

| Failure or unmet-need candidate | Frequency and exposure | Severity / user impact | Representative evidence | Cause confirmed or uncertain | Owner / next check |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

Each important tile may carry a plain-language interpretation, such as “intervention rate—one input to review workload.” Do not attach an unsupported causal forecast or label cost per outcome a minimum selling price.

**Status:** [Pass / concern / unknown against stated criteria]  
**Alerts:** [Threshold, type of change, affected population, and response]  
**Trade-offs accepted:** [Decision and authority]  
**Open questions:** [Evidence needed and owner]  
**Next actions:** [Action, owner, timing, and success check]
