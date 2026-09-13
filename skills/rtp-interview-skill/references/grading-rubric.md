# Interview answer review rubric

Use this rubric for coaching, mocks, and answer reviews. It describes observable preparation quality, not an employer’s confidential rubric or a validated prediction of hiring success. Review the question and answer together before scoring.

## Review in this order

1. **Identify the task.** Is this a definition, design case, strategy decision, or experience story? Note the intended audience and any agreed time limit.
2. **Check substance.** Verify consequential technical claims, arithmetic, personal ownership, and evidence. Distinguish an unsupported statement from a demonstrated error; distinguish error from intentional fabrication.
3. **Assess the applicable criteria.** Use the six dimensions below. Mark a dimension N/A when the question does not call for it, and say why.
4. **Prioritize the improvement.** Identify the most consequential gap, explain its effect, and give one specific repair or drill.
5. **Rewrite when requested or useful.** Preserve the candidate’s actual experience. Use an explicitly hypothetical example where personal evidence is unavailable.

## Six dimensions

| Criterion | Strong evidence | Partial evidence | Material gap |
|---|---|---|---|
| Clear direction | Answers early or identifies the deciding missing constraint | A direction appears after avoidable setup | Evades the question or lists options without a decision rule |
| Technical depth | Explains the relevant mechanism accurately and connects it to the decision | Broadly correct but missing an important step | A consequential mechanism is wrong or cannot support the proposed design |
| Relevant evidence | Experience claims have clear personal scope and support; cases use explicit assumptions | Ownership or outcome needs clarification | Invented or materially overstated work, numbers, or responsibility |
| Useful nuance | Explains a decision-relevant limit, trade-off, or failure condition | Names a caveat without explaining its consequence | Ignores a constraint that would change the recommendation |
| Concise delivery | Gives sufficient detail in a clear sequence at the requested depth | Repetition or uneven emphasis makes the answer harder to follow | Does not reach the answer within the agreed format or buries the decisive point |
| Honest uncertainty | Separates known facts, inference, proposals, and gaps; corrects mistakes | Qualifies uncertainty but leaves its impact unclear | Presents unsupported certainty or persists in a claim after contrary evidence |

Use **✓ strong, ~ partial, ✗ material gap, or N/A**. These marks describe this answer, not the person. Evidence may be N/A for a short factual definition; a hypothetical design should be evaluated on its stated assumptions and reasoning rather than a demand for a past deployment. Nuance may be unnecessary for a simple definition. Speaking plainly is not a lack of depth.

## Give a useful overall assessment

Summarize the answer’s readiness and its most important limitation. A serious authorization error in an agent design should not disappear inside an average of good presentation scores. Conversely, one unnecessary caveat or an omitted experience story in a factual question should not automatically fail an otherwise sound answer.

If the user wants letter grades, use **A: strong for this practice task; B: sound core with a specific gap; C: substantial repair needed; D: incomplete or unreliable on the central task**. State the basis and uncertainty. Reserve “not assessable” for missing information. Do not promise A+, use a rigid weakest-mark conversion, or equate a practice grade with an employer’s decision.

An honest correction can repair the answer but does not erase a substantive learning need. A gap about a component the candidate claims to have owned warrants a follow-up about actual responsibility. It does not, by itself, prove dishonesty.

## Seven diagnostic patterns

| Pattern | What to check | Useful repair |
|---|---|---|
| Unsupported detail | Is it a missing source, a mistaken recollection, or invented experience? | Verify, correct, or remove; state what remains unknown |
| Overstated architecture | Which components did the candidate and team actually build or operate? | Describe the actual contribution and dependencies |
| Activity substituted for value | Does the metric show a verified outcome or just use? | Define completion, quality, denominator, and causal limits |
| Implausibly perfect story | Is there a relevant setback or changed decision in the real record? | Explore one honestly; never invent a failure |
| Incomplete AI design | Are permissions, evaluation, failure response, monitoring, and ownership sufficient? | Add the missing control; keep useful fixed acceptance criteria |
| Mismatched depth | Did the answer meet the interviewer’s question and follow-up? | Compress or expand the relevant mechanism |
| Unsourced statistic | Are population, timeframe, source, and claim aligned? | Verify the claim or omit it; vague wording is not evidence |

Do not treat seats, closed tickets, accuracy, or satisfaction as inherently invalid metrics. Their meaning depends on definitions and the claim made from them. Do not require a confidence percentage for every system or infer safety from the mere presence of human review.

## Feedback format

For a short answer, a few sentences may be enough. For a full review, use:

```text
Question and practice emphasis:
Overall assessment:
Six criteria: [marks with short, answer-specific reasons]
Most important gap: [what is wrong or missing and why it matters]
Improved answer: [supported experience or labeled hypothetical]
Next drill: [one action and what improvement to look for]
Unresolved fact, if material:
```

Use the actual spoken duration when available. A text answer’s word count is not a reliable measurement of delivery time. After a multi-question mock, identify repeated patterns while preserving differences across topics; an aggregate alone can conceal a weak mechanism or an important cohort of questions.

Read [the coaching playbook](coaching-playbook.md) for drills and [the model answers](model-answers.md) for examples of reasoning, not first-person claims to copy.
