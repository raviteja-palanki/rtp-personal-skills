# AI Use Case Readiness — Concept Guide

The useful question is how much independent operation this job needs and can support. Maximum autonomy is not a product objective by itself. A more independent system may create value by reducing coordination and delay, but it may also require more evaluation, access control, monitoring, recovery, and operational skill. Compare the complete designs.

## Business and technical meaning

**For the business:** choose a way of working that improves the user's outcome and uses scarce resources well. State the benefits, risks, human responsibilities, and conditions under which the design can operate.

**For engineering:** decompose the workflow and specify inputs, knowledge demands, state changes, permissions, verification, failure handling, and supervision. Choose components and an operating model that satisfy those requirements with evidence.

Capability and authority are distinct. A model may generate a plausible plan without reliably executing it; it may execute a tool call correctly without being authorized to take the action. Correct code can also implement an inappropriate decision. Human review must itself be designed and tested.

## Why over-automation is tempting

**Novelty:** an agent may be more interesting to demonstrate than a rules-based solution. Compare it to a credible simpler baseline before accepting the additional burden. Novelty is a possible source of bias, not proof that an agent proposal is wrong.

**An undecomposed workflow:** “automate customer support” hides intake, extraction, classification, drafting, policy decisions, action execution, and escalation. Those parts need not use the same technology or share the same authority.

**Hidden control work:** a prototype can omit the integrations, review staffing, recovery, and incident response needed in operation. Estimate those needs early. The older tenfold-cost and six-month-control-build figures were illustrative, not universal ratios or lead times.

The same diagnostic also catches under-automation: unnecessary approvals, repetitive manual checking, or delayed decisions may remove the intended value. Assess alternatives while preserving the protections justified by actual consequences.

## Five worked scenarios

These are **illustrative designs**, not documented deployments or financial results. Numbers inherited from the previous guide are identified as teaching assumptions.

### 1. Invoice matching

A team proposes an agent that reads invoices, matches purchase orders, approves them, and routes payment. Decompose the work: extract fields, validate the vendor and purchase order, apply matching rules, investigate discrepancies, and authorize payment.

An AI extractor plus deterministic checks may be enough for the first steps. Exceptions can go to an appropriate reviewer; payment authority must be assessed separately. A difficult extraction task does not imply a need for autonomous payment decisions.

The previous 85% extraction / 15% matching breakdown and 40%-of-original-cost outcome were hypothetical. Re-estimate using observed task volumes, exception rates, full review costs, and the permitted payment process. A suggestion reviewed by a person is different from a system that submits a payment instruction itself.

### 2. Support triage

Separate intake, classification, routing, urgency detection, and human handoff. Compare showing a routing suggestion with automatically routing a ticket. The latter may still be a deterministic workflow with an AI classifier; it need not require model-directed planning.

Assess the consequence of a wrong queue or missed urgent case, the opportunity to correct it, and how workload changes for the receiving team. The old “80% of the value for 20% of the burden” was an illustrative framing, not an observed result. Measure resolution and rework, not just successful ticket transfers.

### 3. Security incident triage

Correlating evidence from several sources may justify model-directed investigation. Use scoped read access, appropriate evidence handling, logs, and limits. Keep proposing remediation distinct from executing it. A person may need to authorize an action that isolates a system or disrupts service.

The previous guide called this a level-5 bounded agent while also saying it could only read and recommend. That is compatible with agentic investigation but does **not** grant remediation authority. The revised action contract makes both facts visible. Evaluate the quality of investigation and the effectiveness of the reviewer; neither “read-only” nor “human-approved” makes an incident workflow consequence-free.

### 4. Cross-system scheduling

Four calendar APIs and timezone rules create integration work, but multiple systems alone do not establish the need for an agent. A deterministic workflow may suffice when the choices and rules are known.

If preferences and constraints require dynamic negotiation, consider bounded planning. Check permissions, tentative holds, duplicate actions, changing availability, and what happens when only some calendars are updated. People and calendar state can change while a run is in progress. A meeting invitation may be cancelable, but disclosure of its contents or disruption to attendees may not be fully reversible. The old automatic level-6 recommendation was therefore unsupported without these checks.

### 5. Commercial negotiation

Market research, comparisons, drafts, and talking points can support a human negotiator. Evaluate evidence quality and confidentiality. Keep contractual commitments, concessions, and relationship decisions within explicit authority.

Where a bounded negotiation is supported by clear objectives, constraints, and reliable controls, assess that specific delegation on its merits. High tacitness and consequence often favor human-led work, but the existence of negotiation does not logically forbid all automation. Accountability remains with the defined decision owner, including for actions delegated to software.

## Floor, ceiling, and learning

The **floor** describes how independently work must proceed to meet the intended value and service needs. The **ceiling** describes the action scope currently supported by capability, authority, controls, and operating capacity. Their gap reveals a requirement to change scope, strengthen controls, retain a workable human step, or defer the use.

Use the same library labels as the main skill and preserve the operational description. Older numbering is translated in the [crosswalk](references/level-crosswalk.md). A larger number is not a maturity target, and adding agents changes coordination more directly than it changes authority.

Make each pilot a testable proposition. Specify who will run it, the allocated time, representative cases, allowed exposure, observations, and the next decision. Retained human review needs realistic capacity; apparent efficiency that merely moves work elsewhere is not a complete benefit.

## Influences and limits

The earlier guide drew on Anthropic's advice to start with simple systems, agent-tooling discussions of handoffs and guardrails, safety frameworks, product thinking about opportunity cost, jobs-to-be-done, diagnosis before prescription, and inversion. These inform the questions; they do not validate this library's exact levels or guarantee a result. [Anthropic's primary engineering guidance](https://www.anthropic.com/engineering/building-effective-agents).

Shreyas Doshi's opportunity-cost framing asks whether this is the best use of finite resources, not merely whether a feature has some benefit. Christensen's jobs-to-be-done work helps identify the user's task; Munger's inversion encourages examining where more autonomy would make the situation worse. The earlier Kapil Gupta attribution is a philosophical influence, not empirical evidence.

BCG ASPIRE, Factory AI readiness material, the Knight First Amendment Institute, agent SDKs, and frontier safety frameworks were also named previously. Their taxonomies address different questions. Verify the exact current primary document before citing any as an authority for a numbered level, a mandatory rollback rule, or this skill's decision matrix. A tool supporting a guardrail does not establish the sufficiency of a deployed safety control.

The diagnostic makes reasoning inspectable so it can be challenged and improved. It does not establish that other frameworks all assume an agent, that the method is unprecedented, or that a completed checklist makes a use case safe.
