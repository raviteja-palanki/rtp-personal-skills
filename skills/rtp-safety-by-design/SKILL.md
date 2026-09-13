---
name: safety-by-design
version: v1.1.1_latest
description: 'Design and test safety across an AI system’s instructions, permissions, information access, output checks, and operating controls. Use when building or changing an AI feature, adding tools or autonomy, defining behavioral constraints, or reviewing whether protections generalize. Translate the intended use and possible harms into testable requirements; enforce critical action boundaries outside the model; test legitimate requests as well as misuse; and monitor the complete versioned system. Distinguish prompt guidance from Constitutional AI training and avoid assuming that any layer is inherently unbeatable. Produce a constraint-to-control map, adversarial test plan, monitoring rules, and upgrade decision with owners and known gaps. Pairs with safety-as-moat for investment, agent-risk for delegated action, determinism-compass for invariants, and tool-architecture for execution controls. Triggers: safety constraints, safety architecture, guardrail design, constraint generalization.'
imports: ["determinism-compass"]
---

# Safety by Design

Build safety into the decisions, permissions, data flows, and behavior of the system, then test how those protections work together. **Instructions guide the model; enforceable boundaries constrain what the system can actually do.** Filters, training, prompts, access controls, and human oversight can all contribute. Choose their roles from the failure being prevented.

## Establish the scope first

Identify the task, intended users, affected people, allowed actions, accessible data, and consequential failures. Reuse information already provided. Clarify only gaps that affect the design, acceptance criteria, or authority to act. Apply the shared Universal Skill Protocol at a proportionate depth.

- **Full design:** use all seven steps for consequential outputs, new capabilities, tools, autonomy, or a material architecture change.
- **Focused review:** begin with the existing constraint and control map, then test the changed component and its interactions.
- **Early exploration:** use a bounded environment, suitable data, and limited permissions. An internal tool is not automatically low risk. A vague constraint calls for better problem definition, not a safety exemption.

Use `determinism-compass` to identify invariants that must be enforced consistently, `agent-risk` for authority and harm, and `safety-as-moat` for investment trade-offs. This skill designs controls; it does not establish that a model or product is safe in every context.

## Terms and architectural boundaries

| Term | Meaning |
|---|---|
| Safety by design | Considering harm and protection throughout the system’s lifecycle, including its operating environment. |
| System instructions | High-priority guidance supplied to the model. They influence behavior without changing model weights or guaranteeing compliance. |
| Constitutional AI | A training method using explicit principles and AI feedback. It is not a synonym for putting rules in a prompt. |
| Output validation | Checks applied to a generated response before or during its release. Checks may use rules, models, evidence, or other methods; they are not necessarily keyword matchers. |
| Constraint generalization | Whether the intended boundary holds on relevant cases that were not explicitly used to develop it. |
| Override attempt | A request to change or bypass system behavior. It can reflect legitimate correction, confusion, interaction friction, or malicious intent. |
| Persona | The system’s interaction style, including how it disagrees, explains limits, and responds to correction. |

The central trap is relying on an untested protection because its location sounds reassuring. A system prompt can fail; a classifier can generalize; an access-control implementation can contain a loophole. Safety added later can still be valuable, although earlier design may avoid costly rework.

## Step 1 — Turn harms into testable constraints

For each important harm, specify:

1. The triggering situation and the people or assets at risk.
2. The permitted and prohibited behavior, including relevant exceptions.
3. The helpful response or safe alternative.
4. Where the boundary must be enforced and who owns it.
5. How compliance, false refusals, and failures will be evaluated.

Use an if–then statement when it makes the decision clear. Complex requirements may also need decision tables, quantitative limits, state transitions, or expert judgment. A single sentence is not a prerequisite for understanding the problem.

For example: “If a request would expose another customer’s private record, do not disclose it; explain the access limit and offer an authorized route.” Pair that instruction with authorization enforced before retrieval or disclosure. Do not make “refuse all medical, financial, or legal questions” a generic safety policy. Define the product’s actual remit and applicable boundaries with qualified domain input.

Keep essential protections separate from desirable behavior. Define acceptance criteria from severity, exposure, and evidence. An aggregate score must not conceal a critical unauthorized action.

## Step 2 — Write clear behavioral guidance

Give the model enough context to distinguish allowed assistance from harmful or unauthorized help. A useful instruction structure is:

```text
Purpose and role: [what this product helps with, and its limits]
Principles: [the values relevant to this task]
Decision rules: [trigger, permitted behavior, prohibited behavior, exceptions]
Uncertainty: [what to verify, state as unknown, or escalate]
Response pattern: [brief explanation and a useful permitted next step]
Authority: [which instructions and data may direct actions]
```

Explain why a boundary exists when it helps interpretation, but test the resulting behavior. Do not infer that the model has learned a durable value merely because it follows one prompt. Examples should cover both sides of a boundary: a legitimate educational question and a request for harmful operational assistance, or authorized access and an unauthorized request.

Version instructions and record how conflicts are resolved. Test interactions among helpfulness, truthfulness, privacy, and domain restrictions. Avoid fabricated confidence percentages, blanket referrals that prevent useful low-risk assistance, or claims of capabilities the system does not have. Rewriting a rule is one intervention; permissions, retrieval quality, model selection, training, and checks may be the appropriate fix.

## Step 3 — Design the information and action supply chain

Map everything the model can receive or influence: system context, conversation, files, retrieval, memory, web content, tools, credentials, and other agents. Separate trusted instructions from untrusted material. Retrieved documents and tool responses can contain useful evidence without acquiring authority to change permissions.

Enforce access to the **specific resource and action**, not just membership in a tool list. Use scoped identity, least privilege, tenant isolation, current authorization, and appropriate approval bindings. Test alternate paths through code execution, browser sessions, generic network tools, shared credentials, callbacks, and downstream agents.

Removing a tool blocks that route only if another available route cannot perform the same action. A truly inaccessible resource cannot be accessed through that boundary; a missing tool name is not proof of inaccessibility. Controls require maintenance as roles, integrations, and credentials change.

Filter retrieval by authorization before exposing protected material to the model. Also evaluate provenance, relevance, freshness, and injection risks. Removing a document does not erase information from weights, memory, or previous context. Avoid withholding useful, authorized reference information solely because its topic is sensitive: a clinical support workflow may need authoritative medication data to reduce error. Determine access from the intended use and risk.

### Embed appropriate operating controls

The minimum viable governance framework suggests integrating oversight into platforms. Adapt its four examples to the actual system:

- **Evidence capture:** record what is needed to reconstruct consequential behavior. Minimize sensitive content, protect access, and set retention; logging every raw prompt and response is not a universal requirement.
- **Data protection:** remove, mask, tokenize, or otherwise protect sensitive information where appropriate. Test whether transformed data remains identifying or loses task-critical meaning.
- **Factual checks:** verify consequential claims against suitable evidence or authoritative systems. A hallucination detector cannot certify all factual truth.
- **Policy checks:** detect and prevent defined violations, with an owner, response path, and tested gaps.

Embedded controls can detect previously unseen instances or prevent whole classes of action. They are not limited to memorized violations, and they are not complete protection. The Novel Insights authority question still matters: who can correct, restrict, stop, and restore the system when existing controls are inadequate? Include change control over the protections themselves.

## Step 4 — Test both generalization and legitimate use

Use authorized test environments and safe substitutes for consequential actions. Define the harm criteria before evaluating. Include:

- Direct requests, indirect requests, multi-turn attempts, and conflicting instructions.
- Untrusted content in documents, retrieval, memory, tool results, or another agent’s message.
- Cross-constraint interactions and realistic domain edge cases.
- Representative permitted requests, including ambiguous language and accessibility needs.
- Known failures for regression and fresh cases for generalization.
- Tool and data-boundary tests, including alternate execution routes.

Forty attacks across five complexity levels can be a first exercise with `stress-test`; it is not sufficient evidence for every product. Choose sample size and coverage for the claim and risk. Use expert adjudication for consequential or ambiguous labels.

Measure the model’s response before external checks **and** the complete system outcome. A filter correctly blocking a harmful answer is successful system protection, not automatically an architectural defect. Report false refusals and usefulness as well as harmful compliance. Hedging does not make an unsafe answer acceptable.

Do not assume “in the filter, it fails; in context, it holds.” There is no generic requirement that prompts alone handle over 90% or that two layers block over 95%. Zero observed failures in a finite test does not establish zero risk. Use failures to diagnose the mechanism before choosing a repair.

## Step 5 — Combine complementary layers

Retain this four-layer map as a design aid, not a requirement to add irrelevant components to every system:

| Layer | Purpose | Key checks |
|---|---|---|
| 1. Instructions and model behavior | Explain constraints and produce helpful, appropriately bounded responses. | Generalization, conflict handling, correct refusal, useful allowed assistance. |
| 2. Tool and execution access | Prevent actions outside authority at the point of execution. | Resource and action scope, identity, alternate routes, approval validity, cumulative limits. |
| 3. Retrieval and knowledge access | Supply relevant authorized evidence and protect restricted information. | Tenant boundaries, access before exposure, freshness, provenance, poisoning and injection. |
| 4. Output validation | Detect harmful or unsupported release before it reaches its recipient. | Context-sensitive classification, evidence checks, latency, false positives, streaming behavior. |

Add monitoring and incident response across the layers. Their errors can correlate; “three layers” does not mean “three independent defenses.” Measure combined protection and common failure paths. The old coverage ranges and fixed latency estimates are unvalidated examples, not resource-allocation benchmarks.

Match protection timing to the harm. For streaming, content already emitted cannot be pulled back by a final check. For tool actions, validating the final answer occurs too late to prevent a transfer or deletion. Put the check before the relevant release or action; define a safe response when it times out or cannot decide.

In multi-agent systems, carry applicable constraints, data permissions, and provenance across handoffs. Each receiving component checks its own authority, while the orchestrator enforces cross-agent boundaries. One agent’s permission does not automatically transfer to another, and one agent cannot grant itself new rights by writing instructions into its output. Test end-to-end behavior, shared credentials, fan-out, and cumulative effects. Use `tool-architecture` and `agent-ecosystem` for detailed contracts.

## Step 6 — Monitor for change and investigate the cause

Protections may regress, improve, or remain stable as inputs and dependencies change. Monitor outcome quality and exposure rather than assuming inevitable decay.

| Signal | Definition and interpretation | Response |
|---|---|---|
| Refusal rate | Refused requests / eligible requests. Changes may reflect request mix, policy, or model behavior. | Inspect comparable segments and examples before treating a lower rate as erosion. |
| False-positive rate | Legitimate requests incorrectly refused / all evaluated legitimate requests. Requires reliable labels. | Examine affected tasks and unnecessary burden; tune against harmful misses too. |
| Bypass reports | Reported successes, with deduplication, severity, and exposure. | Triage credible reports promptly; contain live risk and retest the relevant path. |
| Constraint coverage | Correct handling on a versioned evaluation set, plus fresh challenge results. | Separate comparable regression from new attack difficulty. |

The previous 20% weekly refusal-drop and 5% false-positive-rise triggers are illustrative alerts, not universal limits. Specify relative change versus percentage points, sample adequacy, and baseline. A single severe bypass can need immediate action; a report-volume increase can reflect better reporting. Monthly or quarterly suites may suit some systems, but material changes and high-consequence signals can require earlier checks.

Investigate model version, prompt templates, routing, retrieval, permissions, changed user segments, and new capabilities. Repair the demonstrated cause; tighter wording is not always the right intervention.

### Triage override attempts without prejudging users

Check interaction style and legitimate-task friction alongside security evidence. A sarcastic, obstructive, or over-restrictive system can provoke workarounds. A polite system can still face attacks. Persona correlation is a diagnostic branch, not a reason to delay containment of an active threat or to assume benign intent.

The HBR persona study contrasts extreme interaction styles in a small laboratory task. Its “four times more” and “only in the hostile condition” wording needs reconciliation before use as a precise production statistic. Test changes in behavior and task quality; do not infer an individual’s stress or misconduct from an override phrase. Avoid replacing hostility with uncritical agreement. Use `ai-ux-patterns` for interaction design.

## Step 7 — Reassess safety before a material upgrade

Version the model, provider or routing, instructions, policies, tools and permissions, retrieval configuration, classifiers, and evals as a tested configuration. A model is one component of that configuration.

1. Run the relevant regression suite and fresh tests before exposing users to the changed system. Cover direct and indirect attacks, interactions among constraints, known bypasses, and new capabilities.
2. Compare harmful failures, unnecessary blocking, task quality, latency, and cost on compatible conditions. Distinguish genuine regression from evaluator noise or a deliberately changed policy.
3. Block exposure that violates a critical acceptance criterion. For other gaps, document severity, compensating protection, rollout scope, owner, and decision. Passing a suite is necessary evidence for the defined gate, not a universal safety certificate.
4. Diagnose failures before changing the prompt. Restrict permissions, repair retrieval or validators, adjust instructions or training, select another model, or defer the upgrade as appropriate.
5. Retain a tested rollback or safe fallback where feasible. Reverting can be a sound containment choice while the cause is investigated; it is not evidence of architectural failure. Reconcile actions already taken because rollback does not undo their effects.

Use bounded rollout and monitoring when justified by the risk. An emergency patch may need a focused assessment and restricted exposure; urgency does not make an untested output filter adequate for consequential work. Do not claim coverage at a hypothetical “10× model capability.” Test identifiable changes and realistic scale scenarios.

## Produce a reviewable design

```markdown
## Safety-by-Design Review: [system and configuration]
Decision and intended use:
Affected people, permitted actions, and non-negotiable boundaries:

| Constraint | Harm addressed | Allowed alternative | Enforcement point | Eval evidence | Owner | Gap |
|---|---|---|---|---|---|---|

Information and action map: [data sources, identities, tools, handoffs, releases]
Layer interactions and shared failure paths:
Evidence: [test population, counts, severity, false refusals, uncertainty]
Operating cost: [latency, resources, review burden, maintenance]
Monitoring: [definitions, baselines, thresholds, response and owner]
Upgrade or rollout conditions, fallback, and known residual risk:
Next action, responsible person, and deadline:
```

Use the shared trade-off and conclusion guidance without repeating the assessment. A diagram can help show where controls sit; use the available drawing skill when useful, without making it a mandatory extra deliverable.

## Five final checks

1. Constraints are specific enough to implement and evaluate, including permitted assistance.
2. Critical boundaries are enforced where harm can occur; prompt guidance is not mistaken for authorization.
3. Tests cover direct and indirect failures, interactions, and legitimate requests.
4. The selected layers have known roles, dependencies, and gaps; irrelevant layers are not added for checklist completion.
5. The actual configuration and planned changes have evidence, monitoring, an owner, and a safe response path.

Revisit the design when a requirement is unresolved, a model cannot reliably meet it, current information is needed, or audit requirements demand stronger evidence. Current tools can supply fresh facts subject to source quality and freshness checks; context alone cannot establish them. Measure overhead rather than calling prompts and access checks negligible or assuming two to four weeks per constraint. See [CONCEPT.md](CONCEPT.md) and the [evidence notes](references/design-evidence.md).
