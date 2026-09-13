---
name: rtp-ai-ux-patterns
version: v1.9.2_latest
description: 'Design AI interfaces that help users understand uncertainty, make appropriate decisions, and recover when something goes wrong. Use for confidence signals, progressive disclosure, loading and error states, explanations, conversation design, persona, and group interaction. Start with the user task, actual system behavior, consequences, and available controls. Choose patterns according to evidence and the action a user can take; do not manufacture confidence, progress, or reassurance. Includes calibration checks, review-effectiveness tests, natural-language UX patterns, and exploration versus focused retrieval. Pairs with trust-ladder, failure-modes, confidence-tuner, judgment-guard, and ai-product-taste.'
imports: [trust-ladder, failure-modes]
---

# AI UX Patterns

Design the interface so people can understand what the system has done, decide how to use the result, and recover when needed. The objective is **appropriate reliance**: accepting useful work, checking what needs checking, and withholding action when the evidence or authority is insufficient. Maximizing trust or minimizing every moment of friction is not the goal.

Use this skill when uncertainty, interpretation, delegation, or recovery affects an experience. Deterministic output can still rely on bad data or be wrong for the task. Skip patterns that do not help the current decision.

## Establish the decision and controls first

Reuse available context and clarify only gaps that change the design:

- Who is doing what, on which surface, and with what task-specific expertise or accessibility needs?
- What does the system actually know and do? What quality evidence exists for this task and user segment?
- What can go wrong: incorrect content, missing coverage, delay, refusal, partial completion, or an unintended action?
- What is the consequence, and how much time does the user have to detect or prevent it?
- Which controls are real: inspect evidence, correct an input, change one part, approve, reject, pause, cancel, undo, or hand off?
- What is authorized, what requires a new decision, and what may continue when the person leaves?

Experts can miss errors and novices can check some well-supported tasks. Test the specific review capability rather than assigning trust behavior from a label. If confidence is unmeasured, record that uncertainty; do not invent a probability range. `rtp-uncertainty-research` and `rtp-confidence-tuner` can establish what signals are defensible while basic clarity and recovery design proceeds.

Use the requested artifact format; a short recommendation can remain inline. Apply the shared `UNIVERSAL-SKILL-PROTOCOL.md` at the AI-PM collection or plugin root where relevant. No mandatory format question or visual is needed before useful work can begin.

## Design commitments

**Say what is true.** A process label, confidence score, citation, learning claim, or success count must have evidence behind it. A status animation is not evidence of correctness. A record being reversible does not mean every external consequence is reversible.

**Keep consequential information visible in time.** Do not place a material limitation, irreversible side effect, or required approval behind an optional expansion. Progressive disclosure should reduce clutter while preserving informed action. The ledger's actionability/timing lens helps prioritize information; it does not justify withholding material or required disclosures because they are unpleasant or offer limited recourse.

**Make control effective.** An approval control must actually block the relevant action until approval arrives. A stop control must describe what it can still stop. Respect standing authorization and avoid repeated confirmations; ask when the intended action or authority remains materially unclear.

**Treat reassurance as a hypothesis.** A warmer voice, explanation, precise-looking number, or popular-use badge can change perceptions without improving the underlying result. Measure task outcomes and appropriately calibrated reliance alongside sentiment.

## 1. Choose an uncertainty response

The five levels below are **response patterns**, not fixed probability bands or a required sequence. Choose using evidence, error cost, user capability, and the next useful action. The previous >90%, 70–85%, 60–75%, <60%, and <40% cutoffs were illustrative and overlapping; they are not universal operating thresholds.

| Pattern | Use when | Example and boundary |
|---|---|---|
| **1 — Direct answer or suggestion** | The result is sufficiently supported for its intended use and any remaining uncertainty need not change the immediate action. | An editable spelling suggestion. Direct wording does not imply infallibility. |
| **2 — Contextual confidence signal** | A reliability or evidence limitation changes how the user should use the result. | “This matches the current policy, but I could not verify the exception in your case.” Use a number only if its meaning and calibration are defensible. |
| **3 — Meaningful alternatives** | Several plausible options matter and the user has information or criteria to distinguish them. | “This could belong under Work or Billing; the invoice number would resolve it.” Explain the difference rather than transferring an unknowable choice to the user. |
| **4 — Focused clarification** | A specific missing answer would improve the result enough to justify asking. | “Which account does this refer to?” Do not ask the user to restate everything or choose among evidence they cannot evaluate. |
| **5 — Abstain, limit, or hand off** | The requested answer or action lacks adequate support, permission, or a safe supported path. | “I cannot determine this from the available record. Here is the information needed and who can resolve it.” Offer useful supported help when possible. |

Verbal labels are not inherently clearer than probabilities; “probably” can mean different things to different people. Test interpretation and action. A calibrated probability is not enough when the possible error remains unacceptable. Conversely, a high-stakes topic does not require refusing every safe informational task within it.

An unqualified “I don't know” can be appropriate. Add the reason, available evidence, or next step when useful. Do not replace a necessary abstention with a risky “best attempt” merely to avoid disappointing the user.

## 2. Layer detail while protecting the decision

Use four layers as a starting point:

1. **Useful output:** the answer, relevant limits, and action the user needs now.
2. **Evidence and explanation:** sources, criteria, calculations, and a concise account of the result's basis.
3. **Alternatives:** other plausible results and the assumptions or tradeoffs that distinguish them.
4. **Adjustment:** relevant filters, preferences, input correction, or advanced controls.

Do not claim these layers suit a fixed 80% of users. Choose what is immediately visible from the task and test whether users find the rest. Avoid hiding essential information behind “Why?” or treating generated reasoning text as a faithful record of internal computation. Show verifiable evidence and actual process records where available.

When a control changes a setting, display the change and its scope: this answer, this session, this project, or a saved preference. Some valid controls intentionally affect only one step. Persistent accumulation is not a requirement for every useful control.

## 3. Match the surface to the task

| Surface | Useful for | Design requirement |
|---|---|---|
| Inline suggestions | Work where accepting, ignoring, or editing fits the existing activity | Make the suggestion distinguishable and easy to dismiss; expose consequential effects before commitment. Code suggestions can have serious consequences even when acceptance is one keystroke. |
| Conversation | Expressing intent, resolving ambiguity, exploring a question, or discussing alternatives | Keep context, action state, and scope clear. Use structured controls when they reduce ambiguity or effort. |
| Dedicated decision view | Comparing evidence, reviewing consequential choices, or managing several actions | Put the relevant evidence, limits, decision, and recovery path together. A special screen does not make a weak review effective. |

These surfaces can coexist. Consistent meanings, permissions, and recovery matter more than physically separating them. There is no general rule that medium confidence makes inline UX wrong or that chat is unsuitable for every consequential workflow.

If showing a historical frequency such as “91% of 2,847 similar cases,” verify the data, cohort, outcome, and relevance. A historical group rate is not automatically a calibrated probability for this individual case. The figures are an example, not a fact to insert in an interface.

## 4. Make waiting and action state understandable

Show progress that corresponds to real system state. Choose frequency and detail according to task duration and user needs; avoid flashing updates that add noise or interfere with assistive technology.

| Situation | Useful pattern |
|---|---|
| Brief work | An unobtrusive busy indicator may suffice; very short tasks may need none. |
| A noticeable wait | A truthful status such as “Searching the selected documents” when that operation is occurring. A neutral loading indicator is appropriate when no reliable stage is available. |
| Several verifiable stages | Update on actual transitions: search complete, draft generated, specified checks running. Do not imply a review occurred unless it did. |
| Long or uncertain duration | Explain that work continues, offer supported cancellation or background completion, and make return, failure, and partial results visible. Use an estimate only when justified. |

The earlier <500 ms / 500 ms–2 s / 2–5 s / >5 s bands were design examples, not universal thresholds. A spinner does not inherently destroy trust, and process detail does not establish correctness. “Analyzed 80% of sources” requires a meaningful known denominator; staged messages on a timer cannot substitute for actual progress.

Prevent repeated refreshes or retries from accidentally duplicating consequential actions. Show whether an action is queued, running, completed, failed, canceled, or only partly reversed. If work can continue after the user leaves, specify what continues and how completion or a decision request reaches them. Do not promise background work the product does not support.

## 5. Design failure and recovery

Name the known limitation plainly, preserve useful work, and offer a relevant next step. Do not guess a technical cause, blame the user, or claim an improvement has been made when it has only been reported.

| Failure | Example response | What the product must support |
|---|---|---|
| Insufficient evidence | “I found the policy, but not the exception record needed to answer your case.” | Show the gap and a way to supply or obtain the missing evidence. |
| Wrong answer discovered | “That amount was incorrect. The corrected calculation is …” | Make the correction visible, address affected actions, and explain verified changes or investigation status. |
| Policy or permission boundary | “I cannot perform that action with the current permissions. You can …” | A valid supported alternative or handoff; do not expose protected internal details or invent policy categories. |
| Timeout or degraded service | “This is taking longer than expected. You can stop now or continue waiting.” | Offer partial output only if it is useful, clearly incomplete, and safe for the task. |
| Connection failure | “I cannot access that file. The connection needs to be restored.” | State an expiry cause only if confirmed; offer a real reconnection or alternative-input path. |

“No results” means the attempted search found none; it does not prove no answer exists. A rejected recommendation does not by itself prove the confidence UI was wrong. Distinguish a system defect, insufficient evidence, a mismatched task, and a preference difference.

Use `rtp-failure-modes` for the failure inventory and `rtp-trust-ladder` for recovery and appropriate reliance. “AI suggestion; you decide” can clarify a role, but it does not transfer all product responsibility to the user.

## 6. Treat persona as behavior that can be evaluated

Define the intended tone, patience, concision, respectful pushback, and handling of disagreement. Warmth, competence, and agreeableness are different properties. A system can be friendly and accurate, or sound authoritative while being wrong. Avoid both hostility and automatic agreement; challenge a premise when the task warrants it, not to manufacture friction.

Measure appropriate channels: interaction behavior, independently assessed output quality, and user reports. In dedicated research, ethically collected physiological measures may add evidence; they are not a routine product requirement. The persona study's physiological/self-report mismatch is a reason to triangulate, not to treat self-report as universally blind. [MIT seminar abstract](https://www.media.mit.edu/events/aha-seminar-series-aleksandra-tamilla/).

Possible behavioral signals include turn-length ratio, rephrasing, resistance messages, and override attempts. Define their denominators and inspect examples. They are proxies affected by task complexity, accessibility, user style, and useful correction—not direct measurements of stress, understanding, or hostility. Use proportionate privacy controls and avoid collecting sensitive content when aggregate events suffice.

Demonstrate competence through reliable work, relevant criteria, honest limitations, and a clear connection to the stated goal. Do not simulate expertise, claim emotional understanding, or hide a known weakness to encourage delegation. The [research notes](references/evidence-and-limits.md) distinguish advisor studies from claims about agents acting in the world.

## 7. Design explanation and review as separate capabilities

An explanation can inform, persuade, satisfy a disclosure need, or support verification. It can also encourage agreement with a wrong result. The effect depends on its content, timing, task, and reader. **Do not claim explanation always improves safety or can never improve error detection.**

Separate the following observations:

| Observation | What it does and does not show |
|---|---|
| Explanation available | The interface offered it; this does not show anyone read it. |
| Explanation opened | The user accessed it; this does not show comprehension or verification. |
| Evidence checked | A relevant source or calculation was inspected; the inspection may still be incomplete or wrong. |
| Decision improved | The final decision or appropriate intervention improved against an independent criterion; this is closer to the intended outcome. |

**Verification substitution** is a risk in which a convincing rationale feels like checking and displaces a more useful check. Test whether an evidence view, concise rationale, known-limit disclosure, or different sequence improves outcomes. A narrative rationale and a disclosure of a specific known weakness are not the same intervention; research has found different effects in different settings.

For decisions where an independent initial view is useful and feasible, collect it before revealing the recommendation. Then show evidence, permit revision, and record the final decision. This reduces one route for initial influence; it is not proof of independence or a universal requirement for routine assistance. Do not withhold information someone needs to make a safe or legally required decision.

Use representative, independently assessed cases to measure correct acceptance, harmful acceptance, useful overrides, and erroneous overrides. Safely isolated known-error tests can help; they are not the only instrument and must not expose real users to consequential fabricated decisions. A reason field, acknowledgment click, or reviewer rotation is a candidate intervention, not an attention guarantee.

**Examine decision directions separately.** In screening, false rejections can remain unobserved because rejected candidates never progress. Other tasks have different visibility. Compare accept and reject paths, consequences, appeal opportunities, and feedback coverage. Oversample hard-to-observe or consequential cases when justified and account for that sampling when estimating population rates. Do not mandate a higher rejection-sampling rate for every product based on one study.

**Make citations usable.** A list of URLs may identify retrieved pages without showing which claim they support. Where feasible, connect a claim to relevant source material, show coverage and provenance, and provide a way to act on a detected issue. Opening a citation is not verification by itself; a useful citation also need not change the artifact to have value. Verify the exact provider API and product surface before making claims about citation behavior.

The Lane/Boussioux screening study and the Rieger explanation research motivate local tests, not a ban on explanation. Detailed source scopes and the earlier numerical claims are retained in [evidence and limits](references/evidence-and-limits.md).

## 8. Check the experience in a useful order

Use these six questions to locate confusing transitions:

| Question | AI interface interpretation | Possible failure |
|---|---|---|
| Where am I? | Purpose, context, and supported scope | An impressive surface without orientation |
| Who am I with? | The AI's role, the people's roles, and who owns the decision | Unclear delegation or a group session treated as one person's request |
| What can I do? | Available actions, permissions, and alternatives | Cosmetic or inaccessible controls |
| What is happening? | Relevant state, evidence, and continuity | Disconnected outputs or ambiguous action status |
| Am I making progress? | Advancement toward the job | Activity shown without useful completion or next steps |
| Why does this matter? | The outcome and its relevance | A memorable demonstration with little value for the task |

This is a design heuristic adapted from experience research, **not a measured universal sequencing law**. Earlier confusion can limit later features, so diagnose dependencies before adding detail. Users may move among these questions, and fixing a later issue can sometimes resolve an earlier one. Do not claim most AI products fail in stages 1 or 2 without evidence.

Audit each control: does it change the intended result, can the user perceive the effect, and does its duration match the promise? A one-time cancel action is useful even though it does not accumulate across sessions. Match persistence to user intent rather than requiring every choice to last indefinitely.

## Language, exploration, and group work

**Natural-language UX:** language can express actions, options, validation, recovery, and discoverability. It can coexist with forms and buttons. Use the [NLX pattern guide](references/natural-language-and-team-patterns.md) for the five inversions and four reusable interaction patterns. Give reasonable defaults for reversible choices; resolve material ambiguity or missing authorization before action. Restatement communicates understanding but does not replace required approval.

**Exploration and focused retrieval:** help users distinguish finding an answer within an established frame from discovering diverse possibilities. A mode switch is one possible design; a blended list, facets, or a clear question may work better. Relevant retrieval is not necessarily popularity ranking, and exploration should not substitute unreliable novelty for evidence. For shared ideation, examine output diversity, provenance, and usefulness. Similar outputs may reflect a correct constraint rather than harmful convergence. Vary inputs or retrieval deliberately when helpful, within access boundaries and with a shared account of material differences.

**Group sessions:** identify whose problem is being discussed, include relevant perspectives, and make roles and decisions visible. Named roles can help without exposing unnecessary personal information. A typist should not silently become the sole decision owner. Role-switching, pauses, individual input, and transcript review can support participation; choose them according to the group rather than forcing one question at a time in every session.

**Long conversations:** a user's inaccurate paraphrase can become a mistaken premise that the system repeats. Check important claims against sources and the agreed task, distinguish user corrections from unsupported assertions, and evaluate the full conversation trajectory. Per-turn fluency can hide a growing error. Concise state summaries and editable assumptions can help when grounded in the actual conversation.

When presenting competing AI views, explain the evidence and decision criteria. Several generated positions are not independent evidence. If the user lacks a basis to choose, provide checks, clarify what would resolve the difference, or route to a qualified reviewer instead of treating an arbitrary selection as informed judgment.

## Evaluate the experience before release

Answer five questions with evidence appropriate to the stakes:

1. **Confidence appropriateness:** do signals match measured performance and lead to appropriate actions? Use the [calibration method](references/evidence-and-limits.md), including uncertainty and segment checks.
2. **Failure transparency:** can users recognize important failures and recover? Include correct and incorrect cases so catch rates are not inflated by a test containing only errors.
3. **Trust after failure:** what changes in behavior, understanding, and outcomes after a visible error? Compare relevant cohorts and intervals; there are no universal enterprise, consumer, or regulated-domain recovery times.
4. **Surface fit:** can users complete and review the task with reasonable effort, including keyboard, screen-reader, and other relevant access needs?
5. **Explanation direction:** how does each evidence or explanation design affect acceptance, rejection, error detection, and final outcomes?

Choose samples, measures, and tolerances for the decision. Five planted errors, ten users, 100 outputs, 50% detection, 10% calibration error, 95% agreement, or a 30% return-rate drop are not validated universal gates. Investigate reliable agreement before calling it rubber-stamping. Low usage may reflect low need, poor fit, or justified caution rather than under-trust.

If users over-rely, inspect evidence quality, signals, review capability, defaults, and authority. If they under-rely, improve the actual product and communicate verified task-specific evidence. Do not hide material uncertainty or invent “95% of users find this helpful” as a remedy. A truthful social-proof measure may describe other users' experience; it is not evidence that this particular output is correct.

Before delivery, confirm that uncertainty patterns have a defensible basis; material limits are visible in time; actions and controls work as described; loading states are truthful; failures and corrections have usable paths; persona and explanations have been evaluated for the intended role; and review checks test outcomes rather than clicks alone.

## Deliver and maintain the design

Provide the recommended pattern, an example of the actual user flow or wording, the decision it supports, and the evidence behind it. Name the principal tradeoff, remaining uncertainty, test that could change the design, and next action with its owner. For a larger design, include a state table linking trigger → visible information → permitted action → failure/recovery → measurement.

`rtp-trust-ladder` calibrates reliance; `rtp-failure-modes` defines failures and recovery; `rtp-confidence-tuner` develops signals; `rtp-judgment-guard` tests human capability and oversight; `rtp-ai-product-taste` sets the domain quality bar. Keep those handoffs specific rather than repeating their full frameworks here.

Consult relevant `3_Research` maps, context, indexes, and source notes; read the passages needed for the claim. Use primary sources for changing product details and technical or empirical assertions. Distinguish direct interaction, a published example, vendor documentation, and a design inference. Social posts can be evidence of what their author said; never invent them or treat virality as adoption. Separate trial, recurring use, paid use, and measured outcomes with population and date.

If experience suggests a reusable improvement to the skill, record its evidence and proposed wording through the library's authorized governance process. One session does not automatically create a permanent tenet. Use a visual only when it clarifies the decision, such as an input-to-action path, an evidence/recovery view, or a correctly labeled calibration plot.
