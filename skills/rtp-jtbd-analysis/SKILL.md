---
name: rtp-jtbd-analysis
version: v1.2.1_latest
description: 'Understand the progress people seek in a particular situation, including functional, emotional, social, and cognitive needs. Use demand-side Jobs-to-be-Done to examine real switching decisions, workarounds, and adoption barriers. Map the stated task and possible less-visible needs, use the four forces, and connect evidence to a testable design implication. Use for a new feature, unclear demand, or flat adoption; adapt for mandated tools by separating buyer choice from user experience. Do not assume an unspoken motive, treat reassurance as a substitute for correctness, or declare a workaround proof of willingness to pay. Pairs with problem-ai-fit, uncertainty-research, interview-synthesis, failure-modes, and opportunity-solution-tree. Triggers: what job is this hired for, why adoption is flat, customer workarounds.'
imports:
  - problem-ai-fit
  - first-principles
  - uncertainty-research
---

# JTBD Analysis

Understand the progress a person wants to make in a particular circumstance, what they do today, and what would make a different approach worthwhile. The stated task matters. Emotional, social, and cognitive needs may also shape the choice; investigate them without treating the person’s account as a cover story.

The deliverable is a supported job statement, the important forces and trade-offs, and a design implication or next test. A concise analysis is enough when the decision is narrow.

## Establish the decision and the evidence

Name the feature, the person doing the job, other people affected, the buyer or sponsor, and the decision in scope. Separate user progress from the organization’s product or revenue goal. Follow the Universal Skill Protocol at the source library root or packaged plugin root, using available context before asking for more.

If adoption is flat, define the measure before diagnosing it: tried once, weekly active use, paid seats, deployed availability, task completion, and realized benefit describe different things. Compare relevant exposure, cohorts, and time periods. Low use can reflect capability, access, workflow, incentives, pricing, or infrequent need as well as a misunderstood job.

Start with relevant local evidence: use `3_Research` maps, context files, and indexes to find applicable notes, series, and book passages. Read the material needed for the decision in depth; do not make every invocation reread the entire library. Revisit relevant Novel Insights with their evidence limits and later qualifications. Use current primary sources where facts or product details need verification. Posts on X can supply first-hand accounts or research leads; verify them and never invent a post or attribution.

Scale the approach:

- **Unclear demand or a new feature:** investigate the job and alternatives before assuming AI is needed.
- **A known job with uncertain switching:** focus on the four forces and recent episodes.
- **A mandated or captive tool:** separate the buyer’s procurement decision from how employees accomplish the task, comply, resist, or work around it. Lack of a vendor choice does not mean users have no needs.
- **A price-driven or routine purchase:** examine affordability, access, requirements, and switching cost without forcing a concealed emotional explanation.

Use `rtp-first-principles` to keep the outcome clear and `rtp-problem-ai-fit` to assess whether AI is an appropriate way to serve it.

## 1. Map the stated task and possible less-visible needs

Use “surface” and “hidden” as prompts to broaden attention, not a hierarchy in which the functional job is false and the inferred motive is true.

- **Stated or surface job:** the task and outcome the person describes, such as reviewing a contract or preparing a maintenance decision.
- **Less-visible or hidden need:** an emotional, social, or cognitive condition that may matter, such as reducing uncertainty, preserving authorship, staying in flow, or explaining a decision to someone else.

These needs can be explicit, overlap, vary by situation, or remain unknown. A functional outcome may be the dominant job. AI is not the first technology to affect confidence, social standing, or cognitive load.

| Example feature | Stated task | Possible additional need to investigate |
|---|---|---|
| Coding assistant, such as Copilot | Complete or improve code | Maintain flow, find a starting point, or seek help without embarrassment |
| Writing assistant | Draft an email | Resolve tone uncertainty or reduce the effort of starting |
| Document summarizer | Understand a long document | Prepare to answer questions with an accurate account of what is known |
| Predictive maintenance | Anticipate failure and plan maintenance | Make and explain a consequential decision under uncertainty |
| Legal-review assistant | Identify risky clauses | Manage review burden and make the basis of a decision inspectable |

These are hypotheses, not verified motives of those products’ users. Do not present them as explanations for a named product’s success without evidence.

Use this working record:

```text
PERSON AND SITUATION: [who, circumstance, constraints]
STATED JOB: When [situation], I want to [task], so I can [outcome].
ADDITIONAL NEED: [functional, emotional, social, or cognitive need; unknown is valid]
EVIDENCE: [specific episode, observed behavior, quote or labeled paraphrase]
ALTERNATIVES: [other ways to make progress, including doing nothing]
HIRING CRITERIA: [what a useful solution must do]
FIRING CRITERIA: [what would cause rejection, restriction, or abandonment]
TRADE-OFF: [what the person would give up, under what conditions]
DESIGN IMPLICATION: [candidate change and why it might help]
NEXT TEST: [what would support or challenge that interpretation]
```

Keep both functional and additional needs in the product requirements and evaluation where they matter. Do not place the functional job in the PRD and hide the consequential needs only in informal design discussion.

## 2. Investigate workarounds as revealed effort

A workaround can show that someone has spent time, money, or risk to make progress. It is often a useful starting point because it exists in a real workflow. Its effort is not automatic proof of a market, a profitable opportunity, or willingness to buy your proposed solution.

Use the three-stage lens:

1. **Perceived mismatch:** what did the official product or commercial arrangement fail to support?
2. **Workaround engineering:** what did the person build, combine, share, export, or manually repeat, and why?
3. **Closure:** what now meets the need—your product, another supplier, the workaround itself, or nothing adequately?

Inspect the workaround with permission. Record the task, people involved, actual cost and burden, constraints, outcome, and alternatives considered. Ask which parts they value and which they merely tolerate. Treat it as evidence for a better specification, not a blueprint to copy verbatim.

Distinguish two possible findings:

- **Product or workflow gap:** a missing capability, connection, handoff, or supported way of working.
- **Commercial-model gap:** access, packaging, billing, or purchasing terms that do not fit the task or buyer.

Both may coexist. A cross-product workaround suggests examining the unit of value sold; it does not prove the business model is wrong. Effort spent may be sunk, imposed, subsidized, or an attempt to avoid payment. Test budget ownership, willingness to switch, willingness to pay, and the cost of serving the need separately.

Look for independently created workarounds and explain relevant differences. Two similar cases strengthen a pattern but are not a universal validation threshold; one consequential case can reveal a real job. Recurrence, consequence, segment, and evidence quality guide the next research step.

The local Michelin case describes fleet operators combining telematics and manual data to connect tire performance with broader operations. It illustrates how a workaround may cross a product boundary. Its chronology and outcome claims remain case evidence rather than proof of a general sequence. See [evidence notes](references/evidence-and-boundaries.md).

## 3. Examine the four forces of a change

Bob Moesta’s demand-side framework organizes influences that make progress attractive or difficult:

| Force | What to investigate | AI-related examples, if relevant |
|---|---|---|
| **Push** away from the current situation | A struggle, changed circumstance, or cost of staying | Review overload, an error, a deadline, a new responsibility |
| **Pull** toward an alternative | A specific desired outcome and credible reason to expect it | Better coverage, faster drafting, useful assistance, less rework |
| **Anxiety** about change | Uncertainty, risk, loss, or effort associated with the new approach | Incorrect output, data exposure, accountability, lost skill, unexpected cost |
| **Habit** keeping the current approach | Familiar routines, dependencies, accumulated investment, and switching friction | Existing shortcuts, team practices, integrations, procurement constraints |

“Push + pull versus anxiety + habit” is a qualitative way to examine competing forces, not a numerical law of rational choice. Forces can change over time and differ between buyer, operator, manager, and reviewer. A mandate can trigger a formal switch without creating voluntary reliance.

Give each force the attention the evidence warrants. Anxiety may dominate, but it is not universally two or three times larger than expected. There is no requirement to invert a supposed 90/10 effort split, name exactly three anxieties, or fill every quadrant with two invented entries.

Consider both action and inaction. A maintenance operator can face harm from an unnecessary shutdown and from a missed failure. Ask how each is detected, decided, explained, and assigned—not merely how the product can make one choice feel safer.

## 4. Reconstruct real switching episodes

Recent switchers can describe the path from initial struggle to search, decision, first use, and later assessment. Include people who adopted your product, chose a competitor, abandoned a tool, or returned to a manual approach as appropriate. Non-adopters cannot describe a switch they never made, but they can explain a stalled decision or why the current approach remains preferable.

Five to eight interviews is one starting plan, not a guarantee of adequate evidence. Use `rtp-uncertainty-research` for sample design and `rtp-interview-synthesis` for the analysis. Distinguish a one-off episode from a recurring pattern.

Ask about actual events before hypothetical preferences:

1. **First struggle:** “When did you first think you needed a different way? What was happening then?”
2. **Alternatives:** “What had you tried or considered, including keeping the old approach?”
3. **Reservations:** “What concerned you about changing? What might have made you walk away?”
4. **Decision:** “What happened that made you try it at that point?”
5. **First use:** “What was different from what you expected? What helped or made the task harder?”
6. **Continuation or exit:** “What made you keep using it, limit its use, or stop? What would change that?”

Follow the timeline and concrete trade-offs. Capture emotional and social context when the participant supplies it; label exact quotations and paraphrases correctly. Social proof can matter, but not every enterprise switch traces to a person. Thirty days of use does not establish durable adoption for every task.

Do not infer low stakes from absent mentions of risk, or a secret motive from silence. Ask a neutral follow-up where useful and respect an unanswered question. A less-visible need does not have to sound uncomfortable to be real, and an obvious functional need is not automatically superficial.

## 5. Turn the job into a useful, testable design choice

Connect the proposed change to the observed need, the relevant force, and a way to assess benefit. Accuracy, safety, agency, and a faithful record remain important even when reassurance or social acceptance matters. Users defending a product after an error is not by itself a sign that the job is being served well.

### Example: coding support

If a developer describes losing momentum when stuck, test whether a useful starting point and easy rejection improve the task. Avoid humiliating feedback, but keep meaningful error information visible. A supportive interface should help the person recover from a wrong suggestion, not conceal that it was wrong. This is a design hypothesis, not a demonstrated explanation for Copilot’s success.

### Example: support drafts

An agent facing forty queued tickets may value speed, authorship, and evidence that important details were considered. Test editable drafts, source visibility, and relevant disposition records. Measure resolution quality, handling time, rework, and staff experience. The earlier “three times more tickets per hour” claim was illustrative and unverified; do not promise it. Plausible assurance without an actual review is not the desired outcome.

### Example: industrial predictive maintenance

Suppose an operator must decide whether to inspect or shut down an asset. The functional job is to prevent failures while managing maintenance cost. Additional needs may include explaining an action or a reasoned decision to wait. A hypothetical seven-day prediction horizon, $2 million asset, or 92% accuracy does not establish the requirements for a real plant.

Five candidate design moves follow:

- **Preserve the decision record:** relevant evidence, timestamps, recommendation and system versions, changes, and authorized access. A log supports reconstruction; it does not guarantee correctness or a particular legal outcome.
- **Record disposition:** acted, declined, deferred, or escalated, with the reason and context needed for later review. Do not make unnecessary paperwork the price of using the feature.
- **Communicate uncertainty appropriately:** use language or numbers that users can interpret and that reflect demonstrated reliability. “High confidence” is not inherently safer than 0.87. Test understanding and action.
- **Support appropriate abstention and escalation:** insufficient information may require a narrower answer, more data, or a qualified person. Refusal can also cause harm or delay, so assess the relevant alternatives.
- **Review errors fairly:** investigate the model, available evidence, interface, incentives, and operator decision together. An override that later looks wrong is neither automatic retraining truth nor automatic evidence of individual misconduct. Route findings to the accountable owners under the actual policy.

The goal is better decisions with an honest, usable record. An audit trail does not make confident error harmless, and emotional reassurance does not justify an unsafe answer. The relevant job helps prioritize consequences; it does not replace domain risk assessment.

## Hand off and check the result

Lead with the job and evidence, then the proposed change, trade-off, biggest uncertainty, and next action. For example: “Operators need to make and explain a timely maintenance decision. We will test a concise evidence-and-disposition view because six interviews describe reconstructing that record manually; we still need to test whether it improves decisions without adding excessive work.”

Use the sentence shape that fits the evidence. If the job is unresolved, recommend the next discriminating research step rather than asserting a cause for flat adoption. A four-forces diagram and stated/additional-needs map can help a substantial analysis; size the visual elements from evidence rather than always enlarging anxiety.

Check that:

- the person, circumstance, progress, alternatives, and adoption measure are clear;
- observations and inferred needs are distinct, with contrary evidence retained;
- relevant switching forces are explored without a quota or fixed weighting;
- workarounds inform both product and commercial hypotheses where appropriate;
- the design implication preserves functional quality and accountable action;
- the next test can challenge the recommendation, not only confirm it.

`rtp-opportunity-solution-tree` uses the job to identify customer opportunities beneath a measurable product outcome; do not paste a job statement into the outcome node without defining what change will be measured. `rtp-failure-modes` uses the job alongside technical and domain evidence to assess consequences. `rtp-fit-signal` examines whether the intended benefit is realized; a weak trust or use curve can have several causes, not just a mislabeled hidden job. `rtp-gossip-mode` supplies informal observations that may refresh the hypothesis after validation.

If this skill missed a recurring issue, record the proposed lesson with its example and scope through the library’s learning and revision governance. Do not turn a single account into a permanent tenet or silently rewrite a shared skill during routine use.
