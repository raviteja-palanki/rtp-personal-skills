---
name: needs-guard
version: v1.2.1_latest
description: 'Investigate how an AI deployment affects workers’ autonomy, competence, relatedness, identity, and workload. Use when designing a rollout, understanding resistance or declining use, or examining unauthorized-tool workarounds. Combine worker accounts with workflow and quality evidence before attributing a cause. Apply the AWARE response and the separate local five-lens review to propose useful changes, clear ownership, and measures of worker experience and task outcomes. Treat the lenses as a discussion aid, not a validated adoption score or psychological diagnosis. Pairs with attitudinal-segmentation, adoption-launch, ai-use-case-readiness, problem-type, eval-framework, and judgment-guard. Triggers: workers resist AI, adoption dropping, shadow AI, loss of autonomy, AI rollout workload.'
imports: [first-principles, bias-spotter]
---

# Needs Guard

Examine what an AI deployment changes for the people doing the work. A tool may help the task while weakening control, learning, connection, or professional identity. It may also be inaccurate, difficult to use, poorly supported, or burdensome. Diagnose the situation with workers rather than beginning with either “they resist change” or “a psychological need must be violated.”

The outcome is an evidence-based explanation, a feasible change to the tool or working arrangement, and a way to assess whether it helps. Sustained appropriate use matters alongside task quality, worker experience, and actual capability.

## Start before assigning a cause

Identify the workers and tasks, the proposed or deployed AI, actual decision rights, and the observed pattern. Separate access, required use, voluntary use, frequency, task completion, and realized benefit. A month-three dip is one possible pattern, not a universal adoption stage or a diagnosis.

Check early for genuine quality problems, unsafe behavior, inadequate access, workload, incentives, training, and usability. These can coexist with need frustration. Contain a consequential product failure promptly while investigating the experience around it. Use `rtp-eval-framework` and `rtp-problem-type` to distinguish technical and adaptive work without forcing a single cause.

Be candid about role and staffing decisions. If work or headcount will change, describe what is decided, uncertain, and available to affected people. Need-supportive design still matters, but it cannot substitute for addressing a real employment conflict. Do not imply job security that the organization cannot promise.

Use this skill during tool selection as well as after rollout: worker needs can inform `rtp-ai-use-case-readiness`. Reuse known context and follow the Universal Skill Protocol at the source library root or packaged plugin root, with proportionate depth and format.

## Understand the three needs

Self-Determination Theory provides a useful foundation for examining motivation and well-being. Its broad research base does not automatically validate every AI-specific prediction in this skill.

| Need | Meaning for this review | Possible experience to investigate |
|---|---|---|
| **Autonomy** | Acting with a sense of willingness and ownership | Being required to approve an answer without meaningful input or a credible way to raise concerns |
| **Competence** | Feeling effective and able to develop mastery | Losing opportunities to practise, receiving unusable feedback, or being accountable for outputs one cannot assess |
| **Relatedness** | Feeling connected to and cared for by other people | Losing useful colleague contact or feeling excluded from the team’s work |

Autonomy does not require unrestricted individual override of every decision. Competence as an experience is different from measured capability. Relatedness is not identical to job security; concerns about replacement can involve identity, finances, fairness, autonomy, and belonging together. A model outperforming a task can support or threaten a worker depending on the circumstances.

## Keep the two AWARE uses distinct

The earlier skill used **AWARE** for two different tools. They serve different purposes:

- **The AWARE response:** Acknowledge, Watch, Align, Redesign, Empower—a sequence described in the local HBR research.
- **The local AWARE lenses:** Autonomy, Work identity, Affiliation, Routine/expertise, Expertise recognition—a practical review aid used in this library.

The lenses are not five separate SDT needs, a validated psychological instrument, or a score that predicts adoption. Use the full label when handing either tool to another skill. [Evidence and terminology notes](references/evidence-and-terminology.md) preserve the source boundaries.

## 1. Acknowledge: map the work and listen

Map the important touchpoints: starting a task, receiving a suggestion, checking evidence, accepting or changing an output, handling an error, learning, escalating, and having work assessed. Include what happens before and after the visible AI interaction.

Ask workers for specific recent episodes. What helped? What became harder? What control, knowledge, time, or connection changed? Compare different tasks and groups rather than assigning needs by age, seniority, or an Embracer/Skeptic label.

A sample of ten to fifteen interviews can be a planning option, not a minimum or proof of coverage. Include users, non-users, and relevant workarounds where feasible. Record the limits of a small or self-selected sample and use `rtp-uncertainty-research` or `rtp-interview-synthesis` when deeper work is needed.

## 2. Watch: separate behavior from its explanation

Look for skill-building, task adjustment, peer learning, and useful collaboration. Also examine avoidance, withdrawal, reduced identification with the work, complaints, and bypasses. Record what was observed and what workers say it means; do not diagnose dissociation, sabotage, or a psychological condition from usage logs or apparent calm.

**Shadow AI** means use outside the organization’s authorization or approved arrangements. It may reflect missing capability, convenience, speed, incentives, uncertainty about policy, or a need for greater control. It can also create a real data or compliance problem. Investigate both the practical reason and the actual risk. Unauthorized use is neither automatic proof of misconduct nor proof that the official system violated a need.

Ask, when appropriate: “What does that tool let you do that the approved option does not?” Avoid punitive assumptions and unnecessary collection of personal details. Retain the distinction between intended use, actual use, declared use, and authorized use.

### Apply the local five-lens review

For each important touchpoint, mark **supported**, **at risk**, **frustrated**, or **unknown**, with evidence. If using Green/Yellow/Red, include the words so color alone does not carry meaning. Unknown must remain visible.

| Lens | Question | Evidence of support might include |
|---|---|---|
| **Autonomy** | Can workers meaningfully influence how the task is done and raise a concern? | Appropriate choices, understood boundaries, and a working escalation or override route |
| **Work identity** | Is their contribution and the change to their role understood honestly? | A credible account of responsibility, growth, and what work will change |
| **Affiliation** | Does the workflow sustain useful human connection and cooperation? | Reachable colleagues, shared learning, and fair credit for joint work |
| **Routine/expertise** | Can people practise, learn, and assess what the tool does? | Appropriate practice, usable evidence, feedback, and demonstrated evaluation skill |
| **Expertise recognition** | Does relevant human judgment have meaningful influence? | A qualified person can question a result, and the organization acts on justified concerns |

Do not infer support from wording alone. “You handle complex cases” may describe an opportunity or an overload. An AI-only throughput metric may be legitimate operationally while insufficient for judging total outcomes. A model explanation may feel helpful without enabling error detection.

Identify leading need-related hypotheses and alternatives. More than one can matter, and none may be well supported yet. Never convert the count of Green cells into a predicted adoption percentage or force a dominant violation from incomplete evidence.

## 3. Align: provide the support the evidence calls for

Match resources, incentives, training, and product support to the diagnosed problem. Training can build competence and agency when lack of knowledge is material; it cannot by itself repair an unusable tool or an unresolved role conflict. A technical repair can also restore confidence and reduce a need-related threat.

Check the full workload, especially when the rollout is described as time-saving:

- **New duty without retired work:** reviewing, correcting, or escalating is added while all previous responsibilities remain.
- **Unassigned operational support:** monitoring or on-call work falls to whoever volunteers rather than a resourced owner.
- **Decision effort grows faster than production:** more drafts or alerts consume the time supposedly saved in generating them.

Name the old work removed, the new work added, who owns it, and who receives the benefit of any saved time. Even after an old workflow is formally retired, check actual practice, transitional duplication, and total burden. Retirement on paper is not proof of realized capacity.

## 4. Redesign: choose a concrete change and test it

| Hypothesis | Candidate response | Check whether it helps |
|---|---|---|
| Meaningful control was lost | Appropriate accept/modify/reject choices, clearer delegation, or a credible escalation path | Can the worker affect the relevant decision within the task’s actual authority? |
| People cannot assess or learn from the output | Evidence, known limits, domain training, practice, or more usable feedback | Can they detect relevant errors and explain the decision using sound evidence? |
| Human connection or contribution is weakened | Peer support, mentoring, collaborative review, or fair recognition | Do workers report useful connection, and does the workflow make it available? |
| Work identity or expertise has no real influence | Clarify roles, involve practitioners in design, and act on qualified objections | Does participation change a consequential choice rather than only collect comments? |
| New review or support duties overload the team | Retire work, staff the new duty, reduce output volume, or narrow scope | Does total workload improve without shifting the burden to another group? |

Use automation, assistance, and human-led work as options. A useful starting question is whether simpler tasks can be automated, comparable performance benefits from assistance, and ambiguous work needs skilled human leadership. Complexity alone does not decide allocation: consider consequence, complementarity, reviewer capability, cost, and real action rights. Hard work is not automatically best assigned to a person without support.

Test explanation design carefully. Show evidence and supported factors when useful; do not claim generated rationale is a faithful view of internal reasoning or that a persuasive account proves competence. The appropriate outcome is better understanding and judgment, not only greater acceptance.

Route worker corrections through a validated, authorized feedback process. An override is input to investigation, not automatic ground truth for shared memory or retraining. Use `rtp-feedback-flywheel` for that loop and `rtp-judgment-guard` for capability formation and retention.

## 5. Empower: make participation and authority real

Explain the system’s role, important limits, escalation routes, and how worker input can change the deployment. Distinguish decisions open for participation from those already made. Honor existing authority and constraints rather than adding approval gates to every action for appearance’s sake.

Provide usable feedback and support on a cadence suited to the work. A weekly error-pattern digest is one option; it should help people learn rather than become another unread duty. Relatedness requires meaningful human relationships, not merely calling the worker and AI a “team.”

## Measure outcomes and revisit the hypothesis

Use a baseline and a suitable follow-up comparison. Choose measures for the claim: experienced autonomy or connection, ability to assess outputs, total task quality, workload, support burden, retention of capability, and appropriate use. State uncertainty and relevant segment differences.

Voluntary use is informative where people can choose. Required use also has real outcomes worth measuring; do not dismiss it as unreal adoption. Avoid covert “when no one is watching” surveillance. Use proportionate, transparent evidence sources and keep anonymous accounts separate from verified operational events.

A five-Green review does not guarantee adoption, and high adoption does not prove needs are supported. If a change improves the measured need but use stays flat, examine task fit, alternatives, incentives, or infrequent demand. If the expected need experience does not improve, revisit the intervention and diagnosis. Neither outcome by itself overturns SDT.

## Deliver and connect

Lead with the supported finding, its limits, the proposed change, and the owner and next check. Include the major touchpoints, worker evidence, local AWARE statuses, competing explanations, workload trade-offs, and outcome measures. A compact table or before/after workflow usually communicates more clearly than a numerical radar chart of subjective color ratings. Use a visual when it helps the decision.

Before finishing, check that the diagnosis includes worker input; actual quality and role conflicts are addressed; unknowns remain visible; proposed authority is real; and the plan tests worker and task outcomes rather than access alone. The previous two-to-three-week estimate and automation percentages are illustrations, not promised costs or required throughput losses.

`rtp-attitudinal-segmentation` examines stance; needs can matter across every stance. `rtp-adoption-launch` organizes the rollout and follow-through, while this skill contributes specific hypotheses and interventions. Neither guarantees a surge–dip–rebound curve. `rtp-ai-use-case-readiness` and this analysis can inform each other. `rtp-problem-type` handles technical/adaptive combinations, and the imports `rtp-first-principles` and `rtp-bias-spotter` help challenge both worker-blaming and unsupported system-blaming explanations.
