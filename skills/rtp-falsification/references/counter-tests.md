# Counter-test examples and evidence boundaries

Use these examples to design a relevant test, not to borrow a launch threshold. All figures below are illustrative unless an actual source and measurement are supplied for the user's task.

## Numerical pre-mortem examples

| Failure | Scenario from the source skill | How to make the decision rule usable |
|---|---|---|
| Degradation | Performance falls from 87% at launch to 79% in month three; a drop greater than five percentage points after sixty days prompts a pause, with a two-week repair window | Define the measure, population, evidence window, severity, and uncertainty. Preserve urgent-response rules; do not wait sixty days for a serious failure. |
| Cost | A feature works economically at 10,000 queries per day but fails at 100,000; $0.08 per query at 50,000 per day triggers an alternative-model test | Check actual cost per successful task. A fallback quality threshold of 80% is only an assumption, and a cheaper model is not a remedy if it breaches requirements. |
| Trust | Enthusiasm in week one becomes avoidance by week eight; over 20% report incorrect information and usage drops over 40% | Define the survey, exposure, baseline, and causes. Verification or a pause may be appropriate; survey and usage changes alone do not select the remedy. The claim that one bad answer erases five good ones is an illustration, not a measured law. |
| Distribution mismatch | Within thirty days, production performance is more than ten percentage points below the evaluation result | Compare matched measures and relevant segments. Add review only if it can detect the failure and is available at the required capacity. |
| Competition | A rival releases a comparable feature in four weeks or within ninety days; a thirty-day strategy review follows | Test what actually changed for customers and differentiation. A hypothetical 12% growth gain does not predict the rival's impact. A competitor release is a reassessment trigger, not automatic proof of failure. |

A proposed pause, repair, model change, or sunset needs an owner and a feasible response. Avoid compound rules that require data from a later window to trigger an earlier decision.

## Claim-specific examples

- **Support:** an AI-caused-ticket count above 15% of deflected tickets could prompt investigation. Count solved problems and displaced work as well, and check whether those denominators support a value claim.
- **Summaries:** an edit or revert rate above 40% could challenge the design. Inspect why people edited and whether the task still became faster or better; editing is not necessarily failure.
- **Segment quality:** a worst-segment score below 70% could be a warning in a hypothetical case. Define sample adequacy and error consequences rather than treating a generic floor as equitable or sufficient.
- **Unsupported claims:** a blinded review of more than 1,000 generations, including relevant adversarial cases, can support a designed test. Keep representative and adversarial results distinguishable. A claimed rate below 2% and an emergency threshold above 5% answer different questions; report the region between them honestly.
- **Trust:** a survey result below 60% willing to use a feature for important decisions is meaningful only if such use is intended. Appropriate distrust of an unreliable or low-stakes feature can be desirable.

## Research connections used in this revision

The local `3_Research/09_hbr-and-journals/_synthesis-engine/NOVEL-INSIGHTS.md` was read in full for this revision. It is a cumulative synthesis ledger with explicit hypotheses, later contradictions, and known defects in its support counts and falsifiers. Its useful contributions here are operational questions, not proof of universal causal rules:

- **04 AUG self-audit:** update a claim and its falsifier together; retain a contradiction as a contradiction and distinguish it from a newly scoped hypothesis. Track shared underlying sources.
- **Q, L, C, and R through the August refinements:** a document, signature, or named role does not prove that someone can act. Establish a disputable decision record, an agreed endpoint for review, real authority, and capacity appropriate to the commitment. Avoid compulsory invented objections or open-ended deliberation.
- **D and M:** a targeted metric can invite gaming, while visible logs can omit hidden rework or include activity with no value. Use a relevant outcome or countermeasure and inspect incentives.
- **H and the 31 AUG default-option finding:** preserve scope and units at the point of use, and assess the current alternative or inaction as seriously as the proposed change.
- **31 AUG Ferriss case:** compare the relevance and quality of private and external evidence instead of treating persistence or rejection as a verdict. The account is autobiographical and selected from a successful outcome.

Use the main skill's self-contained instructions when this local research folder is unavailable. Do not infer that a pattern's label or number of mentions makes it established evidence.
