# Diagnostic questions for clearer decision making

Use these questions when the initial request is vague, when the recommendation feels close between two patterns, or when the case involves customer impact, money movement, compliance, security, or external commitments.

Ask the smallest set of questions that would materially change the recommendation. If time is short, start with the tier-1 questions first.

## Tier 1: questions that most often change the recommendation

| Question | Why it matters | Answers that push lower autonomy or heavier control | Answers that can justify more autonomy |
| --- | --- | --- | --- |
| What exact decision or action is being delegated? | Prevents vague "build an agent" framing. | The action is broad, open-ended, or mixes many unrelated jobs. | The action is narrow, bounded, and clearly defined. |
| Does the system need to advise, decide, execute, or execute with approval? | Separates intelligence need from action rights. | Execution without clear approval design or scoped permissions. | Advisory use or tightly bounded execution with explicit approval points. |
| What happens if it is wrong, late, or fails silently? | Surfaces real downside, not just model quality. | High financial, legal, safety, trust, or customer harm. | Minor rework, low external impact, graceful fallback. |
| Can correctness be checked before or immediately after action? | Verifiability is one of the strongest autonomy constraints. | Success is subjective, delayed, or hard to observe. | Objective checks exist before or right after action. |
| Can a bad action be rolled back quickly and cheaply? | Reversibility often matters more than accuracy alone. | Hard to undo, expensive to recover, or creates customer trust damage. | Easy rollback, low-cost recovery, strong containment. |
| Which parts are explicit rules versus tacit judgment? | Prevents over-using agents for codifiable work. | Most value comes from stable policy, routing, or deterministic logic. | Genuine judgment, exception handling, or context synthesis is required. |
| How often do novel cases or exceptions appear? | Distinguishes workflow automation from real agency need. | Low exception rate; rules cover most cases. | Frequent branching, non-standard paths, or multi-step replanning. |
| Does the environment stay stable during execution? | Dynamic environments raise recovery and coordination needs. | State changes mid-flight, external actors intervene, or timing is fragile. | Stable state during execution with predictable dependencies. |
| What permissions, tools, or decision rights are required? | Permissions can kill a use case even when reasoning is strong. | Broad write access, approvals, money movement, or sensitive systems. | Narrow tools, sandboxed actions, and scoped permissions. |
| What is the smallest bounded slice that still creates value? | Good readiness work starts with a wedge, not the whole dream. | Only a full end-to-end autonomous system seems useful. | A smaller phase delivers clear value and lowers risk. |
| What telemetry, labels, or feedback loops exist? | Deployment quality depends on measurement and learning. | Outcomes are not measured, labels are sparse, and incidents are hard to detect. | Clear telemetry, review queues, labels, and outcome signals exist. |
| Does the economic upside justify the control burden? | Some use cases are technically possible but economically poor. | Low frequency, low leverage, or one-off use with high governance overhead. | High scale, high leverage, or strategic value that justifies controls. |

## Tier 2: architecture-shaping questions

| Question | Why it matters | Lower-autonomy signal | Higher-autonomy signal |
| --- | --- | --- | --- |
| Is the main value in generating content, making a decision, or taking an action? | Content support and action execution deserve different patterns. | The value is mostly draft generation or summarization. | The value depends on multi-step action, orchestration, or stateful follow-through. |
| Who owns the decision today, and why? | Reveals hidden accountability and review logic. | Ownership exists because judgment, trust, or accountability must remain human. | Ownership is human only because the workflow is manual, not because the decision itself is deeply tacit. |
| What policy, audit, or compliance obligations apply? | Governance can dominate architecture. | Strict audit, legal, or policy requirements with weak evidence trails. | Light governance with strong logging and policy clarity. |
| Are there upstream data or process problems masquerading as an agent need? | Many false positives are really process design issues. | Bad inputs, broken workflows, and missing integrations are the real blockers. | Inputs are reliable enough that autonomy is the real frontier. |
| How much coordination across systems or teams is required? | Coordination complexity raises need for orchestration and failure handling. | Many brittle dependencies and unowned handoffs. | A small number of predictable systems and clear ownership. |
| Is the task one-shot, low-volume, or highly repetitive? | Volume helps justify control and integration effort. | Rare use, bespoke cases, or low leverage. | High repetition or large leverage. |
| What latency window is acceptable? | Tight timing changes whether review is viable. | Immediate action required but verification is weak. | Enough time exists for checks, approvals, or staged execution. |
| Can permissions be progressively widened over time? | Strong roadmaps expand scope only with evidence. | The use case starts broad and cannot be staged safely. | The use case can start read-only, then draft, then bounded execution. |

## Tier 3: roadmap and escalation questions

| Question | Why it matters | Lower-autonomy signal | Higher-autonomy signal |
| --- | --- | --- | --- |
| What would have to become true to raise autonomy by one level later? | Turns the assessment into a roadmap. | No obvious control or measurement path exists. | Clear missing enablers can be named and built. |
| What is the safe failure mode and kill switch? | Safe degradation matters in real operations. | No clear containment or stop mechanism. | Human override, rollback, and scoped containment exist. |
| What incident types would force a rollback to lower autonomy? | Defines operational boundaries before launch. | No clear rollback triggers or thresholds. | Clear stop conditions, alerts, and recovery playbooks exist. |
| Where is human review most valuable? | Human review should be targeted, not symbolic. | Review is required everywhere because trust is weak. | Review can focus on high-risk cases and edge conditions. |
| What evidence would prove the next phase is justified? | Prevents autonomy drift without proof. | Success criteria are vague or vanity-based. | Objective thresholds, sample sizes, and decision metrics are defined. |

## Fast interpretation tips
- Strong verification plus cheap rollback can justify more autonomy than raw model confidence alone.
- High tacitness does not automatically mean an agent; it often means a copilot with strong review.
- Low agency need plus high control burden is a strong sign to prefer workflow, policy, and approvals over agentic execution.
- If permissions are broad but the value wedge is narrow, start with a smaller slice and tighter tools.
- If the economics are weak, even a technically feasible agent may still be the wrong answer.
