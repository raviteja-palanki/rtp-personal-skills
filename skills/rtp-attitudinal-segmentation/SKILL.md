---
name: attitudinal-segmentation
version: v1.1.1_latest
description: 'Use attitudes toward AI as an additional lens for understanding different onboarding, evidence, control, and feedback needs. Apply the Embracer, Neutral, and Skeptic categories provisionally, alongside the user job, observed behavior, experience, and craft preferences. Use when adoption or retention differs within the same role, when testing AI onboarding, or when deciding whether user-selectable defaults would help. Combine respectful research with relevant behavioral evidence; keep Mixed and Unknown visible and test whether a segment-specific design improves outcomes. Attitude never grants action permissions or lowers safety requirements. Works qualitatively before launch or with small groups; use adequate samples for quantitative claims. Pairs with uncertainty-research, jtbd-analysis, feedback-triage, ai-product-metrics, confidence-tuner, and adoption-launch.'
imports:
  - uncertainty-research
  - jtbd-analysis
  - feedback-triage
  - ai-product-metrics
---

# Attitudinal Segmentation

Use this skill to investigate whether people doing similar work need different support because they approach AI differently. The output is a **segment map, a small set of justified product decisions, and an instrumentation plan**. Recommend one shared experience when the evidence does not justify separate defaults.

Attitude adds a useful lens to role, task, experience, and behavior. It does not replace them or reliably explain every adoption gap. A cautious user may have good evidence that the product is unsuitable; an enthusiastic user may understand the risks well. Treat both as people whose reasons deserve investigation.

## Boundaries that come before segmentation

- **A label is provisional and contextual.** Someone may embrace AI for drafting and reject it for an irreversible decision. Preserve Mixed and Unknown rather than forcing every user into one of three boxes.
- **Preference is not permission or competence.** Enthusiasm does not authorize automatic actions, and caution does not establish expertise. Determine action rights from the task, actual authorization, capability, and consequence controls.
- **Essential protections apply across segments.** Do not hide material uncertainty from enthusiasts, increase unsafe attempts for them, or deliberately over-refuse useful supported work for skeptics. Tailor presentation and assistance within the same justified safety boundaries.
- **Let people choose and revise their mode.** Use plain controls such as “Draft for my review” or “Show supporting evidence.” Avoid presenting identity labels as permanent user types or silently escalating autonomy from behavioral observations.
- **Research should not become workplace labeling.** Collect only relevant information, make its purpose clear, and respect applicable consent, access, and retention requirements. A research hypothesis is not a performance rating or evidence of misconduct.

Reuse customer grounding from `rtp-jtbd-analysis` and uncertainty evidence from `rtp-uncertainty-research`. Apply the shared `UNIVERSAL-SKILL-PROTOCOL.md` at the AI-PM collection or plugin root where relevant. Clarify the user, job, current alternative, outcome standard, and the product decision segmentation could change.

## Three dimensions, kept separate

| Dimension | Working categories | Why it matters |
|---|---|---|
| General adoption attitude | Pioneer, early adopter, pragmatist, conservative, skeptic | How someone tends to approach unfamiliar tools; inspired by technology-adoption frameworks, not a fixed personality test. |
| Attitude toward AI for this job | Embracer, Neutral, Skeptic, Mixed, Unknown | Whether the person is eager, conditional, doubtful, or undecided about this specific use. |
| Craft orientation | Craft-protective, output-focused, collaborative | Whether preserving voice or method, reaching an outcome, or working through a process together is especially important. These preferences can overlap. |

An **Embracer** is interested in using AI and exploring its possibilities. **Neutral** describes conditional interest based on demonstrated value. A **Skeptic** currently wants stronger evidence, more control, or a credible alternative. These are working descriptions, not diagnoses of fear, ignorance, or resistance.

A craft-protective Embracer might use AI extensively while retaining their voice. A daily AI user who wants review before action might simply understand the consequence. Do not infer craft orientation, expertise, or skepticism from that preference alone.

## 1. Establish whether the lens explains a real difference

Pick the decisions in scope—for example, onboarding, evidence visibility, review flow, or feedback collection. Compare users doing similar tasks and ask what they believe the product will do, what they want to retain, and what concerns them.

Separate competing explanations: task difficulty, model quality, integration, access, time, incentives, prior failures, disability-related needs, budget, and organizational policy. Attitude may be a cause, a response to the product, or both. Low use is not sufficient evidence of skepticism.

Hilary Gridley's published practitioner account recommends including enthusiasts and skeptics in early testing and watching engagement over time. It motivates this lens without establishing a universal three-segment classifier or a retention multiplier. [Original practitioner discussion](https://www.lennysnewsletter.com/p/counterintuitive-advice-for-building).

Test usefulness by writing what could change in the next few product decisions. If no meaningful difference emerges, the right result may be to keep one design. Do not invent three variants merely to justify a segment map.

## 2. Combine expressed preferences and observed behavior

Use both sources when feasible, with uncertainty visible. Observations help form questions; they are not invisible ground truth about a person's beliefs.

### A short optional survey

Adapt these five questions to the product:

1. How often do you use AI tools outside this workflow? Include “prefer not to say.”
2. How do you currently feel about using AI for **this task**, and why?
3. Which supported mode do you prefer: draft for review, propose then act after approval, or act within specified limits?
4. If relevant and optional, what experience do you have doing this kind of work?
5. What concern or condition would most affect whether you use this feature?

An approximately 90-second survey can be a design aim, not a requirement. Do not demand personal AI-use history when direct task preferences answer the product question. Avoid leading answers that portray enthusiasm as the desired response.

Daily use plus excitement may suggest Embracer; conditional interest and practical criteria may suggest Neutral; expressed doubt may suggest Skeptic. Confirm the interpretation with the person where useful. Conflicting answers can reflect different tasks or constraints, not noise to eliminate.

### Behavioral evidence to interpret

| Signal | Possible question | Important alternatives |
|---|---|---|
| Feature exploration | Is the person curious about capability? | They may be testing failures, required to explore, or unable to find a basic function. |
| Repeated use of a few features | Has the person found a useful routine? | Limited access, workload, or narrow job scope may explain it. |
| Override or retry | Are they correcting quality or seeking a different style? | Both enthusiasts and skeptics may override; frequency alone does not distinguish them. |
| Source opening | Are they checking a consequential claim? | Opening is not proof of understanding, and no click may reflect other verification. |
| Slow time to first value | What blocks useful completion? | Task frequency, setup, training, or an unsuitable product may matter more than attitude. |
| Quality-related support contact | Which concern or failure needs attention? | A high contact rate can reflect product defects, expertise, access, or support habits. |
| No AI action after login | Was there a relevant opportunity to use it? | Login does not establish need, available time, or permission. |

Sales and support notes can supply context, but they are subjective, purpose-bound observations—not free, pre-labeled truth. Keep provenance and distinguish a direct statement from someone else's interpretation. Do not copy sensitive notes into a broad dashboard without an appropriate basis.

If building a classifier, define labels, use a suitable validation sample, and examine errors, missing data, and whether it adds value beyond direct preferences. The old “about 70% accuracy” was illustrative. Never assign a confident number without evidence.

## 3. Test useful defaults within justified action boundaries

The table offers **design hypotheses**, not mandatory behavior for everyone in a category. Users should be able to choose a different supported mode.

| Design choice | Embracer hypothesis | Neutral hypothesis | Skeptic hypothesis |
|---|---|---|---|
| Onboarding | Offer a quick path to useful work and optional advanced examples. | Demonstrate one concrete job and how to judge its value. | Start with a credible second-opinion or draft use, evidence, limits, and recovery. |
| Messaging | Show relevant capability and possibilities without overpromising. | Show verified practical benefit and reliability. | Explain what the person retains, what the system changes, and how concerns are addressed. |
| Workflow mode | Offer permitted bounded action when explicitly chosen and supported. | Make proposal-and-approval easy where desired or required. | Make review, manual action, or a non-AI alternative easy where supported. |
| Evidence visibility | Keep optional detail unobtrusive while showing material limits. | Put the most relevant evidence near the decision. | Offer expanded evidence and checks if the person finds them useful. |
| Feedback | Open-ended ideas can reveal unmet possibilities. | A quick rating with an optional reason may fit routine use. | An easy correct/incorrect report with relevant context may capture specific failures. |
| Main risk to test | Unwarranted reliance, irrelevant novelty, or unnecessary friction. | Unclear value, disrupted routines, or hidden work. | Unresolved concern, poor evidence, or control that only appears meaningful. |

A skeptic's failure report may be valuable, but expertise and report quality must be assessed directly. Do not assume skeptics are always the most knowledgeable, first to churn, or most loyal later. Equally, avoid assuming enthusiasts dislike every tutorial or approval prompt.

**Keep autonomy vocabulary consistent.** Use `rtp-ai-use-case-readiness` and `rtp-autonomy-spectrum` to assess the actual rights. The older segment table's L1–L4 examples conflict with the library's shared labels and must not be reused as permission rules. Describe “draft,” “review then execute,” or “act within these limits” before adding a level label.

Set refusal and action thresholds from task risk and measured performance. Preferences may affect whether to show a clearly labeled provisional answer in a low-consequence setting, but not whether a prohibited or unsupported action proceeds. Numeric confidence is optional only where its absence does not hide material uncertainty.

Choose onboarding and trial duration from actual opportunities to experience value, task frequency, and support needs. Seven, fourteen, or thirty days are not universal segment requirements. A longer trial may help a low-frequency job regardless of attitude.

## 4. Understand the concern behind the stance

Use the three-needs lens when it helps explain a workplace experience:

| Need | Potential benefit | Potential threat | Response to investigate |
|---|---|---|---|
| Competence | Extending a person's capability | Loss of valued expertise, feedback, or opportunities to learn | Task-specific training, meaningful practice, feedback, and recognition of existing expertise |
| Autonomy | Removing unwanted work and enabling better choices | Mandated use, constrained judgment, or accountability without sufficient influence | Clear decision rights, useful controls, participation, and realistic alternatives |
| Relatedness | More time for useful human interaction | Lost collaboration, unequal access, or isolation | Preserve important relationships and create fair ways to participate |

These are prompts for listening, not proof that every objection is a psychological need violation. Check product shortcomings and material workplace consequences too. Training may help several needs, and greater discretion may support competence; the axes are not sealed compartments with only one possible remedy.

Holding someone accountable for a result they cannot meaningfully influence is a governance problem. Route it to `rtp-needs-guard` and the relevant authority/operating-design skills. Co-authoring a workflow or evaluation standard can help when voice and craft are the concern, but participation is not a substitute for real decision rights or resources.

Distinguish **actual use, declared use, and realized value**. Hidden use may reflect policy confusion, fear, incentives, privacy, or personal advantage. It does not prove the worker is a Skeptic, that the organization is solely at fault, or that misconduct occurred. Mandated use is not voluntary adoption, and minimum compliance is not automatically sabotage.

The [evidence notes](references/evidence-and-examples.md) preserve the needs framework and survey figures with their populations and limitations. Use supportive inquiry and appropriate governance rather than building a covert attitude-monitoring system.

## 5. Track change without prescribing conversion

Users can become more or less confident as they learn what works. A skeptic may move toward conditional use after a credible result; a neutral user may explore more after repeated useful outcomes. An enthusiast may become appropriately cautious after discovering a limitation. All can be successful outcomes if reliance becomes better calibrated.

Design opportunities to experience relevant value, inspect evidence, and retain control. Do not force a Skeptic → Neutral → Embracer path or promise that one impressive answer converts someone. Introducing another use case is useful only when it fits their job and demonstrated needs.

Review labels and preferences after material events—new tasks, failures, capability changes, or explicit user feedback—and at a cadence suitable for the product. Quarterly review can be a starting point. The old month-three decay, week-three conversion, week-four churn, and week-six-to-eight expansion claims were not established timing laws.

When analyzing an experiment, keep the starting segment separate from later changes. If the treatment changes a user's label, regrouping them afterward can distort the comparison. Report the treatment, cohort, period, outcome, uncertainty, and migration rather than quietly changing who belongs in each group.

## Worked example: Sai and Riya on the plant floor

This is an illustrative scenario, not an observed deployment. Sai has substantial plant experience and remembers earlier predictive systems failing. Riya is newer to the work and interested in AI. Those facts motivate questions; age or tenure does not determine either person's attitude, competence, or correct level of control.

Ask both what evidence they need and what decisions they want the tool to support. Suppose Sai wants sensor evidence beside a second opinion and a quick way to report an acoustic cue the system missed. Suppose Riya wants a first-pass work-order draft and a concise review view. Both configurations retain the inspections, sign-offs, and action limits required by the operating process.

Do not let Riya skip a required inspection because the model appears confident. Do not impose an arbitrary weekly walk-around based on her enthusiasm; use the actual maintenance schedule and risk requirements. Give Sai a way to add a useful observation without assuming it is correct or already represented in the model's inputs.

Route corrections through validation and the feedback workflow. A one-click override does not automatically train the model, and “the system learned his ear” would require evidence of a real learning process. Evaluate accepted and corrected work, missed failures, review effort, and outcomes for both people. Different defaults are justified if they improve useful work while preserving required controls—not because the story promises that both will stay.

Similar questions can arise in clinical, financial, or legal work, but do not transfer this vignette into a senior-versus-junior stereotype or a domain-specific operating rule.

## When to simplify or use another lens

- **Before launch or with few users:** interview and observe likely users; test alternative experiences qualitatively. Do not claim stable segment percentages or effects without adequate data. Neither 20 nor 100 users is a universal boundary.
- **AI is invisible or routine:** investigate whether attitude toward automation still changes the decision. A search feature can involve consequential reliance, but segmentation adds little if task needs already explain the differences.
- **Use is mandated:** study actual usefulness, workarounds, effort, and the ability to report problems. Login or compliance counts alone cannot establish adoption.
- **Differences are small or uncertain:** retain one design or a simple user-selectable option. No fixed 95%-similarity rule is necessary.
- **Only one default is feasible:** choose it for task safety, value, accessibility, and the supported population. Add a simple choice or evidence view where possible. Do not assume Skeptics always deserve the default or Embracers always adapt.

Watch three pitfalls: **Persona Trap**—labels without a decision they improve; **Survey-Only Trap**—a one-time answer treated as permanent; **Single-Variant Trap**—ignoring demonstrated different needs because the team resembles only one group. The opposite error is over-segmentation: three attitudes times three craft preferences can become nine configurations whose costs exceed their value.

## Deliver the three-part handoff

1. **Segment map:** task and population; Embracer/Neutral/Skeptic/Mixed/Unknown estimates or qualitative profiles; evidence source, uncertainty, missing coverage, and reassessment trigger. Keep sample descriptions distinct from population estimates.
2. **Product decisions:** the next relevant features; proposed shared or differentiated defaults; user choice; permitted action boundary; why a difference might help; cost and test. Three to five features can be a useful planning slice, not a required quota.
3. **Instrumentation plan:** events and definitions, optional survey wording, authorized data sources, owner, privacy handling, cohort measures, experiment design, and review cadence. Define a meaningful change alert rather than a universal 10% quarter-over-quarter threshold.

`rtp-feedback-triage` compares concerns without weighting a report as truth because of a label. `rtp-ai-product-metrics` examines outcome and workload differences alongside aggregate measures. `rtp-fit-signal` checks whether evidence supports the intended market: success in an Embracer-heavy niche may be real fit for that niche, but does not establish fit for every group. `rtp-uncertainty-research` recruits relevant perspectives with sufficient coverage; a 25-to-5 sample may be inadequate for a desired comparison but does not make the five observations worthless.

`rtp-jtbd-analysis` distinguishes shared jobs from different anxieties and alternatives. `rtp-confidence-tuner` designs understandable signals within justified risk boundaries. `rtp-adoption-launch` owns rollout timing; pass the segment evidence and preferences rather than duplicating its phases. `rtp-needs-guard` investigates the underlying need when relevant.

Conclude with the product decision this analysis changes, the supporting evidence, the complexity-versus-benefit tradeoff, and the next test with its owner. A hypothesis might predict improved useful completion or retention for an underserved group without worsening safety or another group's experience. Choose the target from the decision and baseline; a 30% month-two retention lift is not a universal bar.

A visual can compare preferences and design choices across groups when useful. If showing movement, allow both directions and Mixed/Unknown states. Do not present enthusiasm as the final stage every user should reach.
