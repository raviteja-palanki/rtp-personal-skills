---
name: agent-risk
version: v1.4.1_latest
description: 'Decide whether an agent should act, within what limits, and with what evidence of containment. Compare expected value, credible severe harm, alternatives, and residual risk. Map how harm can spread; design and test manual stops, automatic limits, time bounds, scope controls, and approval previews. Examine human oversight, effective permissions, shared failure modes, liability, persistent personal memory, and insider misuse. Use for agent design, pre-launch reviews, or changes in action authority. Scale the review for low-consequence tasks; advisory systems may still need a broader safety review. Pairs with autonomy-spectrum for authority, agent-spec for checkpoints, judgment-guard for effective human ownership, and adoption-launch for incentives and participation. Triggers include "agent risk", "kill switch", "can we stop it", "increase autonomy", and "worst-case harm".'
imports: [stress-test, failure-modes, autonomy-spectrum]
---

# Agent Risk

Decide what an agent may do by examining the value, credible harms, and controls of the actual workflow. A stop button is useful only where stopping can still prevent or limit harm. For an irreversible action that completes immediately, authorization and preventive bounds matter before execution.

## Begin with authority, exposure, and the decision

Identify the actions, affected people/systems, business value, deployment, and current authorization. Include advice that predictably drives consequential human actions. Use a short screening for a bounded task; use the full review before a consequential launch or increase in authority. A small user count or a human approval step does not by itself make the harm trivial.

Reuse known context and existing authorization. This skill should clarify material gaps, not introduce repeated approval requests for actions already authorized. The shared Universal Skill Protocol is at the AI-PM library root, or the plugin root in the packaged library. Choose an output depth and format that fit the request.

Bring important boundaries forward: prohibited actions, credible severe harms, who can constrain or stop execution, and what evidence is needed to accept residual risk. Societal AI-risk estimates provide context, not a score for this agent. The source review is kept in [cases and evidence](references/risk-cases-and-evidence.md).

## Terms that guide the review

| Term | Practical meaning |
|---|---|
| Proportionality | Whether the proposed authority and remaining risk are justified by the benefit, alternatives, and applicable constraints. It is not a universal benefit-to-worst-case ratio. |
| Harm cascade | The progression from a failure to downstream effects, including delayed, repeated, or correlated harm. |
| Blast radius | People, assets, decisions, and systems the failure can reach. Reach and severity are separate dimensions. |
| Stop/containment control | A mechanism that blocks new action, cancels pending work where possible, or limits effects. It does not necessarily reverse completed actions. |
| Alert fatigue / override assumption | Excessive alert burden can weaken response; separately, having an override does not establish that a person can and will use it effectively. |
| 3M conditions | Mindset, meaning, and mechanisms that support human ownership of outcomes. They are design prompts, not a validated safety score. |
| Permission inheritance | An agent may act through a user's credentials or session. Determine its effective access and enforcement rather than assuming it always receives the full account privilege. |
| Model monoculture | Shared model dependencies can create correlated failures. Other shared components can create them too. |
| Unallocated liability | Losses may fall outside insurance or contractual coverage. Assign responsibility and funding explicitly; a lack of a quoted price does not mean no risk. |
| Attachment scope | Whether persistent agent state serves a firm/function, an individual, or both. Personal memory adds ownership and offboarding questions to the usual accountability duties. |

## The review process

### 0. Define risk appetite by domain

Translate broad risk appetite into decisions people can use: what is prohibited, what requires specified controls, what can be tried within a bound, and who accepts exceptions. Separate financial reporting, access, personal data, safety, and external commitments from recoverable internal experimentation where relevant.

A numeric dial can help a conversation, but qualitative boundaries with examples can be more actionable than two unexplained numbers. “Low tolerance” still needs enforceable rules; it does not promise zero operational risk. Do not assume an organization without a domain dial takes no risks, or that a stated dial changes behavior.

The original Verizon interview example contrasts a stated risk posture of 1/10 for financial integrity and cybersecurity with 8–9/10 for experimentation, against a described baseline of 2. Retain it as an executive's stated policy, not demonstrated turnaround causation. The useful move is to make permissions and exceptions understandable and test whether they govern real decisions.

### 1. Compare value, harms, alternatives, and residual risk

Ask: **What benefit requires this level of authority, and what credible harm remains after the proposed controls?**

Consider ordinary performance, plausible severe scenarios, likelihood or uncertainty, exposure duration, affected parties, and alternatives. Include human/manual, deterministic, advisory, or more narrowly scoped designs. An average success rate such as 95% says little about safety until the remaining failures and their consequences are understood.

| Dimension | Benefit and alternative | Harm and exposure | Control/evidence | Residual decision |
|---|---|---|---|---|
| Financial | Incremental value, time horizon, operating cost. | Direct loss, cumulative loss, dependencies. | Spending/action caps, reconciliation, tested bounds. | Accept, reduce scope, investigate, or decline. |
| Customer/worker | Useful outcome, time, access, experience. | Severity, affected count, distribution, reversibility. | Prevention, review, appeal, remediation. | Explicitly address who bears harm versus receives value. |
| Trust/reputation | Reliability and confidence in service. | Misleading claims, broken commitments, loss of trust. | Honest status, response, evidence. | Do not automatically rank reputation above personal harm. |
| Legal/policy | Permitted use and documented obligations. | Noncompliance, rights violations, contractual exposure. | Applicable controls and accountable review. | A benefit does not waive a legal prohibition; legal exposure alone is not proof all autonomy is prohibited. |

Use numbers where defensible and ranges where necessary. Keep annual revenue opportunity distinct from net benefit and one-event loss. Do not invent probabilities or convert human rights into an arbitrary dollar score. The old “10× benefit passes, below 3× fails” rule has no adequate basis and leaves important cases undefined.

**Illustrative hiring case:** handling 500 candidates instead of 50 is ten times the throughput, not proof of better hiring. Discriminatory screening or offers can harm individuals and create legal exposure. Examine affected decisions, fairness, accessibility, effective review, appeal, and authorization. Restrict or reject the proposed authority when the evidence and controls are inadequate; do not infer from a generic hiring label that every form of automation has the same risk.

### 2. Map the harm cascade

Draw the initiating failure, first external effect, propagation path, and containment opportunities. Include retries, concurrent agents, batch size, queues, permissions, and common dependencies.

- **Seconds to minutes:** a transfer, deletion, price update, or resource allocation can have an immediate effect.
- **Hours:** repeated routing or operational choices can accumulate and disrupt a service.
- **Days to weeks:** quality drift, misinformation, exclusion, or persistent errors can compound slowly.

These are example time scales, not intrinsic properties of agent categories. A single-person harm can be severe; ecosystem reach is not automatically catastrophic. Map both severity and extent.

For a supply-chain agent that routes shipments to one carrier, test concentration limits, carrier failure, detection delay, alternative capacity, and contractual effects. The original 48-hour discovery/re-routing and weeks of recovery are illustrative assumptions. Do not assume detection will be that quick—or that slow—without evidence.

Estimate the response chain from **failure onset → detection → decision → stop/containment → external stabilization**. Parallel steps and queued/in-flight operations matter. Detection-plus-stop time is a response measure, not the speed at which harm propagates. If the first irreversible harm precedes any possible response, move the relevant control before execution.

### 3. Design a combination of prevention and containment

Use the controls needed for the failure mechanisms and consequences. More layers are useful when their coverage and dependencies are understood; a fixed count of switches is not proof of protection.

| Control | What it does | Main limit and design check |
|---|---|---|
| Manual stop | An authorized person suspends the agent or affected actions. | Availability, attention, access, and propagation delay. A requirement for two people to stop can slow containment; use it only if the consequences justify that design. Separate emergency stop authority from authority to resume. |
| Anomaly-triggered stop | A tested rule or detector pauses a defined activity. | Unknown patterns and false alarms. Use meaningful thresholds, an alert owner, and a safe state; normal-looking actions can still be harmful. |
| Time-elapsed stop | Runtime or credential expiry bounds an execution period. | Harm may occur before expiry. Verify renewal authority, expiry enforcement, and treatment of in-flight work. |
| Scope/action bound | Limits targets, values, tools, destinations, rate, or aggregate exposure. | A per-action bound may permit cumulative harm. Check sequences, parallel runs, aliases, and boundary enforcement. |
| Simulation/preview with approval | Tests or displays proposed effects before authorized execution. | A simulation is a preventive test or approval pattern, not literally a runtime kill switch. Validate its fidelity and bind approval to the actual action, parameters, and relevant state. |

For example, a ±5% per-update price bound still permits large repeated changes. Add an appropriate aggregate floor/budget and scope if needed. A preview of 1,000 emails must represent the actual recipients and content; approval of an earlier draft must not silently authorize changed actions.

Stopping should reach queues, child agents, scheduled jobs, credentials, and relevant gateways. Determine which downstream operations can be canceled and which require reconciliation or compensation. Keep evidence and recovery instructions. A “fail closed” action can itself be harmful in some services; define the safe degraded mode for that domain.

Controls can operate automatically with little user-facing delay. Do not assume all safeguards require repeated human review or necessarily reduce throughput. Cost their actual latency, coverage, and operational burden.

### 3.5. Check whether human oversight is effective

Before counting a human as a control, establish authority, information, competence, capacity, availability, and reason to act. An approval request can provide real stop authority when refusal blocks execution. Approval frequency or a fast response alone cannot establish rubber-stamping; compare task difficulty, errors, and the actual review process.

Use the 3M prompts:

- **Mindset:** does the person understand their contribution and authority? Describe the agent's role without implying that a system absorbs the person's responsibility.
- **Meaning:** is the review worth doing, and can the reviewer see what matters to the affected person or business?
- **Mechanisms:** is useful review supported by time, evidence, training, escalation, and recognition, rather than rewarding only output volume?

A naming/framing experiment involving 1,261 managers found important effects in a subgroup already working in organizations with AI agents on their charts; it does not establish that a human name always removes ownership. The current primary paper distinguishes average and subgroup results. See the evidence note before reusing the percentages.

Test the response through suitable drills and representative cases. A technical stop test alone cannot prove sustained ownership, but an exercise that includes the people and incentives can reveal operational weaknesses. If human review adds no reliable protection, redesign the system without counting that layer; still meet any applicable oversight obligations.

### 4. Test the controls against the required response window

Test in a safely isolated, production-representative environment and use carefully bounded operational exercises where authorized. Do not create real harm to prove that containment works.

- Manual stop: the authorized responder receives the signal, can act, and the affected work actually stops.
- Automatic stop: the chosen condition is detected and enforced, including false-trigger behavior and alert escalation.
- Time bound: expiry halts or safely transitions work and cannot be silently renewed by the same uncontrolled process.
- Scope bound: prohibited actions are blocked at an enforceable boundary, including cumulative and concurrent attempts.
- Preview/approval: no external action occurs before the applicable approval, and changed actions are checked again when needed.
- Recovery: resume requires the agreed evidence and authority; unresolved external effects are reconciled.

Measure the full response chain, missed signals, remaining in-flight work, and actual residual exposure. Exercise loss of the control service, responder unavailability, load, and downstream timeout where relevant. The original one-minute automatic/five-minute manual goals and quarterly cadence are examples. Set the cadence from risk and change frequency, and retest after changes that could invalidate the controls.

### 5. Design detection and monitor its limits

Combine useful evidence: output audits, anomaly checks, constraint thresholds, customer/partner signals, and regression tests. Choose complementary coverage rather than requiring multiple detectors for every trivial action. A single enforceable bound can prevent a specific failure, while no collection of detectors guarantees every harm will be observed.

Specify false alarms, misses, sample coverage, data delay, and who acts. Use `production-observability` for alert design. Measure onset-to-detection, alert-to-action, action-to-containment, affected exposure, and recovery separately. Set review coverage from consequences and the detection method; initial 100% human review can be necessary in some cases and ineffective or infeasible in others.

Do not rely on a daily audit for a failure that can cause unacceptable harm within seconds. Also do not assume every agent has a fast cascade. Test the actual workflow and contain before harm where possible.

### 6. Review identity, dependencies, liability, and memory

**Effective permissions.** Identify who or what executes each action, the delegated scope, session lifetime, environment, and policy enforcement. Prefer attributable task-scoped identities/tokens where practical. A separate service account with broad privileges does not solve least privilege; a controlled delegated user credential is not automatically unbounded. Confirm that tools cannot bypass required approvals and that logs distinguish agent actions from unrelated human actions.

**Correlated failure.** Review shared model, prompt, retrieval, data, evaluator, tool, and infrastructure dependencies. Different providers can still share blind spots, and different prompts on the same model can sometimes add useful diversity. Test joint failure on relevant cases; use an independent verifier, deterministic constraint, architectural separation, or diversity when it improves the actual control. The cited 54-person cognitive study is not evidence about reliability of model fleets.

**Liability and funding.** Identify relevant insurance, contracts, exclusions, limits, indemnities, and incident funding with the appropriate owner. AI-related insurance products exist; coverage for this agent's exact acts remains a separate question. Human sign-off does not automatically insure, price, or transfer legal liability. Record uncovered losses and who can accept them.

**Attachment scope and departure.** For firm-attached, person-attached, or mixed agents, define data ownership, access, portability, retention, revocation, and offboarding. A personal agent needs these rules **in addition to** accountable ownership and controls. Regulated or frontline roles can also create mixed personal/company memory. A portability clause must respect data rights and confidentiality; do not assume private company material may follow the individual. Name how disputes and enforcement work, especially where personal preferences and proprietary context are intertwined.

## Include intentional misuse without mistaking dissent for it

Consider insiders and external users who might misuse tools, disclose data, manipulate outputs, or bypass controls. Also examine poor access, workload, fear, unclear policy, and legitimate concerns about the rollout.

WRITER's 2026 survey reported 29% of employee respondents, including 44% of Gen Z respondents, under its broad “sabotage” framing. Its examples include refusing to use AI as well as unauthorized tools and information sharing. These are self-reports in a sponsored sample, not a universal rate of malicious attacks or evidence against any employee or age group.

Address incentives and participation through `adoption-launch`, while applying proportionate access and integrity controls from the start. Co-creation can help but does not establish that sabotage disappears; technical protection need not wait until cultural concerns are solved. Distinguish constructive challenge, ordinary mistakes, policy noncompliance, and intentional harm using evidence. A low-threat rollout can still expose sensitive data.

## Authority and consequence matrix

These three action patterns summarize the original matrix; they are **not** the seven maturity levels in `autonomy-spectrum`. Use that skill's shared labels and the actual action rights in the final recommendation.

| Action pattern | Bounded, low-consequence use | Consequential or broad use |
|---|---|---|
| Advisory: human decides before action | Appropriate testing and clear status may suffice. | Validate advice and effective human review; examine anchoring, authority, auditability, and appeal where needed. |
| Conditional: agent acts inside approved bounds | Enforced limits and outcome checks sized to the task. | Prevent high-impact acts outside scope; define detection, containment, cumulative limits, and accountable review. |
| Autonomous: acts without case-by-case review | Evidence of acceptable risk, effective bounds, and a suitable recovery path. | Require a strong case for preventive controls and residual risk. Reduce authority or decline when unacceptable harm cannot be prevented or contained. |

Customer-count bands such as 1–10 or 100–1,000 are not severity measures. High-consequence autonomy is not categorically impossible, but a fast stop alone cannot justify an action whose unacceptable harm is immediate.

## Diagnostic questions and readiness

1. What could happen in a representative period of uncontrolled operation, including one irreversible action and cumulative effects?
2. What are the credible severe scenarios, affected parties, and uncertain assumptions?
3. Where does the cascade become irreversible, and which controls act before that point?
4. What did the latest control test demonstrate, under which conditions, and what remains untested?
5. Which signal reveals the harm, how late might it arrive, and who can act?
6. Why is the incremental value worth the remaining risk, compared with safer alternatives? What would change the decision?
7. What can the effective credential and tool chain actually do beyond the task?
8. Who owns and controls persistent state when a person, vendor, or organizational role changes?

Before a consequential deployment, document proportionality, credible cascade/exposure, preventive and stopping controls, representative test evidence, detection, measured response, and residual-risk ownership. Unknowns can lead to a bounded experiment, more evidence, reduced authority, or no deployment. A confident answer is not itself a red flag; confidence needs a basis.

## Output and follow-through

```markdown
# Agent Risk Review: [Agent / workflow]
Decision: [deploy within bounds / reduce authority / investigate / decline]
Actions and authority: [scope, identity, permitted effects]
Domain boundaries: [prohibitions, conditional permissions, risk owner]
Value and alternative: [incremental outcome, cost, evidence]
Credible severe scenarios: [harm, likelihood/uncertainty, reach, horizon]
Cascade: [onset → detection → decision → containment → stabilization]
Controls: [prevention, stop, expiry, aggregate bounds, approval as needed]
Dependencies: [shared failure modes and tested independence]
Human oversight: [authority, capacity, evidence, response]
Liability and memory: [coverage gaps, ownership, offboarding]
Test evidence: [conditions, measured result, limitations]
Residual risk and trade-off: [accepted cost and accountable decision]
Next action: [owner, bounded scope, evidence needed, review trigger]
```

Use `stress-test` and `failure-modes` to challenge scenarios, `autonomy-spectrum` to set authority, `agent-spec` for the enforceable contract, and `judgment-guard` for human contribution. Hand off the decision and evidence when this is part of a wider workflow.

Explore when uncertainty needs a bounded test; exploit when the evidence supports the approved scope; exit or redesign when value or risk no longer supports it. These are decisions, not fixed one-week phases. Increase authority on relevant evidence rather than months elapsed or a run of uneventful operation alone.

The original 95% harm-capture claim was an unvalidated hypothesis. Replace it with a task-specific target and test, including missed harm and shared control failures. A diagram can help show the cascade, control coverage, or authority matrix; use one when it adds clarity.
