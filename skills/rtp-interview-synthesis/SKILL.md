---
name: interview-synthesis
version: v1.0.1_latest
description: 'Turn customer interviews into traceable themes, persona signals, opportunity hypotheses, and evaluation candidates. Use three practical passes: describe meaningful observations, connect them into themes, and identify what matters for the decision. Preserve contradictions, source context, and the difference between reported behavior and interpretation. Use for transcript sets or clearly labeled interview notes; scale claims to the quality and breadth of the material. Do not infer motives from silence or manufacture a surprising finding. Pairs with uncertainty-research for study design, jtbd-analysis for switching forces, eval-framework for test design, and failure-modes for consequences. Triggers: synthesize these interviews, what did we hear, customer research themes.'
imports:
  - jtbd-analysis
  - uncertainty-research
  - eval-framework
---

# Interview Synthesis

Make the path from a participant’s account to a product decision visible. Read the material systematically, preserve disagreements, and show which interpretations the evidence supports. Coding helps make judgment inspectable; it does not remove the researcher’s influence or guarantee that the interpretation is correct.

The distinctive handoff is from discovery to evaluation: a theme can suggest a required system behavior or a user-outcome question worth testing. An interview supplies a reason to investigate that behavior, not automatically a correct answer, quantitative threshold, or proven failure mode.

## Establish the research question and evidence limits

Identify the decision, participants, recruitment, interview purpose, available materials, and important missing perspectives. Reuse context already provided. Follow the Universal Skill Protocol at the source library root or packaged plugin root, adapting depth and output to the task.

Prefer recordings or faithful transcripts when available and permitted. Check transcription errors in consequential passages against the source. If only notes or summaries exist, work with them as filtered accounts: label their provenance, avoid presenting paraphrases as quotations, and explain the resulting uncertainty. Do not discard useful evidence solely because it is not verbatim.

Protect participants’ information and observe permitted uses of recordings, transcripts, and excerpts. Material supplied for analysis does not automatically authorize public quotation or model training. Use participant IDs and the minimum identifying context needed for interpretation.

Choose the scope of claims from the study’s purpose, sample specificity, dialogue quality, and analytic depth. Five to fifteen interviews is a common planning illustration here, not a guarantee of sufficiency. Fewer than three can reveal a consequential case or a useful hypothesis; they usually support limited cross-participant claims. Do not infer population prevalence from a purposive interview sample or declare saturation from a fixed count. See [method and evidence notes](references/method-and-evidence.md).

Before coding, record the team’s main assumptions and what the study can actually challenge. Commercial incentives, interviewer relationships, leading questions, and omitted topics affect interpretation. Sales calls can contain valuable observations, but they are not interchangeable with neutral discovery interviews. Seek another perspective or follow-up where the distinction matters.

## Pass 1: Describe meaningful observations

Read each included transcript in full. If any material is unavailable or only partially reviewed, state the coverage. Code meaningful passages relevant to the research question, keeping enough surrounding context to interpret them.

Use short, concrete labels, often three to seven words. Reuse a label for the same phenomenon; do not invent a new code for every line merely to increase the count. More than one code can apply to a passage. Keep an evolving codebook with definitions and examples so later changes can be applied consistently.

Capture:

- what participants say they need, value, fear, or expect;
- reported actions, stopped actions, workarounds, and specific episodes;
- directly observed actions, distinguished from self-report;
- contradictions within an account and differences across accounts;
- emotional wording, hesitations, deflections, or missing answers **when the source actually records them**.

Keep observation and interpretation in separate fields. “Keeps a personal spreadsheet” is an observation if reported or seen. “Distrusts the official tool” is one possible explanation, alongside missing functionality, habit, access, or a different task. A pause before a trust answer does not establish hidden distrust. Silence may reflect uncertainty, privacy, language, interruption, or a question that was never asked.

A useful evidence row contains a source ID and location, exact excerpt or labeled paraphrase, descriptive code, task/context, and a separate interpretation or follow-up note. Never reconstruct an unrecorded pause, feeling, or action to make the account richer.

## Pass 2: Connect codes into themes

Group related observations and examine how they connect: circumstances, actions, consequences, workarounds, tensions, and differences between people or tasks. This skill calls that practical pass **axial coding**. It involves more than sorting similar words.

Name each theme precisely enough to explain something. “Morning review is crowded with low-priority alerts” is more useful than “users experience friction.” Keep alternative explanations and disconfirming cases attached. Move, split, or merge groups as the evidence warrants; retain the trail from the theme back to source passages.

Report how many distinct participants discussed a theme, how many were asked a relevant question, and how it varies by context. Mention counts are different from participant counts: forty excerpts from one talkative person do not equal forty independent accounts. Absence from an interview is not necessarily absence from the person’s experience.

Consider recurrence, consequence, specificity, intensity, and relevance to the decision. A rare but consequential account can justify follow-up. Emotion can indicate importance to that participant; it does not establish prevalence or objective severity.

Eight to fifteen themes may be a workable output for a particular study. It is not a quality requirement: a narrow study may need fewer, and a complex one more. Do not force unlike cases together to hit a target. A sample from one persona can answer a focused question; qualify its breadth and compare other groups when the decision requires it.

## Pass 3: Identify the decision-relevant themes

Choose the themes that most affect the product or research decision. This skill calls that prioritization pass **selective coding**, or the synthesis’s **spine**. It is a practical adaptation, not a claim to have completed a full grounded-theory study.

Ask: if this theme were absent or explained differently, would the recommendation change? Explain why each selected theme matters and what uncertainty remains. Three to five often makes a readable narrative; use the number the evidence and decision require. Preserve supporting and unresolved themes in the evidence record.

For each selected theme, state:

1. **Finding:** what the material supports, with source references and scope.
2. **Interpretation:** the proposed explanation and credible alternatives.
3. **Implication:** the user need, opportunity, or risk to investigate.
4. **Next test:** what would help choose among explanations or assess a candidate change.

Look deliberately for findings that challenge the team’s assumptions. Record whether you found any; agreement is a possible result. Do not manufacture a contradiction, surprise, persona, or design recommendation to make the synthesis appear rigorous.

## AI-product questions: examine actual use

People vary in their understanding of AI and the task. Do not assume they expect magic, understate harm, or lack insight. Translate broad requests into concrete episodes and compare stated expectations with available behavioral evidence.

- **Workflow:** “Walk me through the last time you did this. Where did AI help, and what happened before and after?” Include alternatives and occasions when AI was not used.
- **Failure cost:** ask what happened in a specific error, how it was detected, who corrected it, and the downstream consequence. A missing review step is a question to investigate, not proof of carelessness.
- **Reliance:** ask what people checked, accepted, rejected, or delegated and why. Trust as a feeling is useful testimony, but it is different from calibrated reliance and actual accuracy.

Five prompts for deeper follow-up, when relevant:

1. “Tell me about a time the AI was wrong. What did you do next?”
2. “What would make you stop using it, or use it only for certain tasks?”
3. “If someone asked how you decided to rely on that recommendation, what would you show or explain?”
4. “Has using it changed what you practise or learn, positively or negatively?”
5. “If it were unavailable tomorrow, what would change?”

These are optional probes, not a mandatory interrogation. An inability to answer the third does not prove the person merely tolerates the system. A skill-loss concern is evidence of a concern; a claim of atrophy needs evidence about capability over time. Make it easy to discuss errors without implying the expected answer, and respect a participant’s choice not to elaborate.

## Build the bridge to evaluation

Translate a theme into a hypothesis about needed behavior before designing a test:

```text
Source passage → descriptive code → theme → decision-relevant finding
→ need or risk hypothesis → candidate design/system behavior
→ evaluation question, comparison, and evidence → eval-framework
```

Keep the source IDs, dates, and assumptions with the candidate. Validate the required behavior with domain knowledge and relevant constraints. Some questions need usability research or a longitudinal study rather than a model-output test.

| Interview theme | Useful evaluation direction | Limit to preserve |
|---|---|---|
| Distrust of prioritization | Compare rankings with suitable expert judgments and actual task outcomes; examine disagreements | Expert order is not automatically ground truth, and greater agreement is not always better |
| Concern about audit defensibility | Test whether authorized users can reconstruct the recommendation, evidence, timing, and disposition | A timestamped export alone does not establish adequacy, truth, or compliance |
| Fear of confident errors | Measure reliability within defined confidence groups and the consequence of errors | A proposed 95% target is illustrative; calibration and acceptable risk require task-specific definitions |
| Overload during morning review | Test whether a usable alert set helps people find and act on important issues without excessive burden | “Top five include 90%” may be impossible if more than five important issues exist; define relevance and denominator |
| Concern about losing skill | Test independent performance, practice opportunities, and transfer over a suitable period | An AI-off control establishes an option, not proof that skill is retained |

Treat explanation features as hypotheses. They may help understanding, persuade users to accept errors, or have little effect. Measure decision quality and appropriate reliance as well as uptake. Likewise, an anxiety code identifies a concern to investigate; do not restrict failure analysis to problems participants anticipate.

## Worked example: eight predictive-maintenance interviews

Imagine six operators from three plants and two reliability engineers interviewed for 30–45 minutes each. This is an illustration, not a documented research result.

Descriptive observations include spending 20–40 minutes on morning review, keeping a personal spreadsheet, questioning alert order, and recalling an important failure missing from the top of the list. The prior example’s 1,247 open-code applications and eleven themes show possible analysis volume; neither is a productivity or quality target.

Suppose themes include prioritization concerns in seven interviews, workarounds in eight, audit-related concerns in six, and morning overload and false-alarm fatigue in eight. Keep the original example’s code-application counts—47, 38, 29, 52, and 44 respectively—distinct from those participant counts. Check which questions were asked and how the accounts differ.

Three provisional findings might guide the next decision:

- Some operators re-rank alerts using their own model of the plant. Investigate whether the system lacks relevant context, the operators are mistaken, or the ranking is hard to interpret. Do not sacrifice accuracy simply to match a familiar mental model.
- Records of why an action was taken may serve an audit or coordination need beyond the visible prediction task. Confirm that need with concrete examples and the people who use those records.
- Attention is concentrated in the morning, while failures can develop throughout the day. Test the handoff and alerting workflow across time windows.

A provisional persona signal could describe operators who act only when system and personal rankings align; five of eight in this hypothetical sample would not establish a market segment’s size. A “why this rank?” explanation, disposition logging, and attention-aware alerts are candidate changes. Evaluate them against outcomes and alternatives. Logged dispositions require validation and appropriate reuse rights before becoming training labels.

## Review and deliver

For consequential work, have someone challenge the interpretation or review a suitable sample when available and authorized. Independent coding of a subset can help a shared-codebook project expose ambiguous definitions; 30% is an example, not a universal requirement. In other qualitative approaches, reflexive discussion serves a different purpose. Agreement does not prove correctness, and disagreement does not prove incompetence. A second pass by the same agent is not an independent second coder.

If a reviewer is unavailable, document that limitation and strengthen traceability, alternative explanations, and source checks. Do not halt a useful synthesis or create parallel agents against the user’s preferred workflow.

Deliver the decision-relevant findings first, then their evidence, implications, evaluation candidates, and next research step. Include the sample and material limitations, unresolved contradictions, and what the study did not establish. Use a synthesis document, evidence table, tagged transcripts, or concise inline response as appropriate. A coding-to-evaluation diagram can help explain a substantial handoff; its numbers should reflect this study.

Check that all included material has been reviewed, meaningful observations are traceable, interpretations are labeled, counts use correct units, and quoted text is exact. Confirm that selected themes earn their relevance and that no arbitrary theme count or surprise requirement shaped the conclusions.

`rtp-uncertainty-research` owns sampling and collection design. `rtp-jtbd-analysis` maps switching accounts to the four forces. `rtp-feedback-triage` identifies themes needing depth. `rtp-eval-framework` turns appropriate candidates into tests, and `rtp-failure-modes` examines consequences and responses. Preserve the chain between these skills without assuming customer interviews and production traces require identical methods.
