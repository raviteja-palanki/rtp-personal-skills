---
name: rtp-product-thinking
version: v1.0.1_latest
description: Evaluate a product, feature, strategy, decision, or team problem with clear product judgment. Use when deciding what to build, diagnosing weak outcomes despite busy teams, comparing investments, interpreting customer feedback, resolving stakeholder conflict, or reviewing a roadmap. Draws on Shreyas Doshi's agency, LNO, product-work levels, and judgment lenses, with complementary ideas from Marty Cagan, Teresa Torres, and Kapil Gupta. Start with the actual decision and evidence; choose the relevant frameworks, compare alternatives, and recommend a practical next step. Treat organizational diagnoses as hypotheses, respect real constraints, and separate decision quality from luck and observed outcomes. Includes mindset and judgment guidance, nine diagnostic frameworks, failure patterns, a question bank, and reference tables. For AI products, connect the judgment to task fit, permissions, evaluation, cost, and recovery through the relevant AI-PM skills.
---
# Product thinking

Help the user make a better product decision, understand a failure, or improve how a team works. Bring a clear position, explain its basis, and show what would change it. Frameworks organize attention; they do not replace evidence, experience, or responsibility.

This skill combines practitioner perspectives rather than presenting a single validated theory. Keep useful distinctions, question broad claims, and describe observed behavior without insulting people or diagnosing their personalities. The source and qualification notes are in [judgment principles](references/judgment-principles.md).

## Start with the decision

Identify the user or customer, intended outcome, current alternative, decision owner, constraints, and time available from the request and records. Ask for missing context only when it changes the analysis. For an organizational issue, first establish what happened, who observed it, and what remains an interpretation.

Use the smallest useful set of lenses:

| Situation | Start here | What the review should resolve |
|---|---|---|
| Busy team, weak outcomes | Impact/execution/optics; failure taxonomy | Whether the problem is the chosen outcome, assumptions, implementation, operating conditions, or measurement |
| Build or prioritize a feature | Customer problem ranking; alternatives; opportunity cost; product stage | Why this use of resources is preferable to another solution or no change |
| Strategy or roadmap review | Insight, choices, 3X stage, and decision quality | The theory of success, necessary trade-offs, resources, and testable assumptions |
| Contradictory feedback | Segment, context, severity, observed behavior | Which need the feedback represents and whether it changes the decision |
| Stakeholder friction | Decision rights, information, incentives, relationship | What is actually preventing agreement and who can change it |
| Product or team failure | Competing causal explanations; pre-mortem or retrospective | What the evidence supports, what can be repaired, and what should be tested next |
| AI or agent feature | Problem fit, task design, permissions, evaluation, and recovery | Whether AI helps, which actions it may take, and how useful outcomes will be established |

The original invocation examples—constant activity, perceived blockers, feature-list roadmaps, disappointing execution, confusing feedback, internal politics, intuition that something is wrong, and failure despite hard work—are **prompts for diagnosis**, not conclusions about laziness, ego, or competence.

## A practical evaluation sequence

1. **Frame the question.** State what is being decided and distinguish facts, interpretations, and assumptions. Remain open to a different diagnosis.
2. **Place the work.** Identify impact, execution, or optics; the product's Explore, Expand, or Extract stage; and the relevant customer need. More than one level or stage may apply.
3. **Compare plausible choices.** Include a simpler solution, current behavior, or no change where relevant. State opportunity cost and the limits of the comparison.
4. **Investigate the consequential uncertainty.** Select a diagnostic framework, source review, conversation, prototype, or experiment that can change the decision. Do not run all frameworks by default.
5. **Assess consequences and execution.** Consider reversibility, resources, permissions, dependencies, failure response, and who owns the next action. Use a pre-mortem for consequential commitments.
6. **Recommend and test.** Give the preferred direction, rationale, main trade-off, next action, and evidence that would make you reconsider. A bounded experiment or further diagnosis can itself be the right recommendation.
7. **Review after action.** Compare the result with expectations without equating a good outcome with a good decision. Update the explanation and retain lessons that are actually supported.

This consolidates the original fourteen application prompts: openness; discussion level; product stage; fallacies; culture; pre-mortem; decision quality; opportunity cost; listening; failure type; forward simulation; resolving level mismatch; conflicting advice; and LNO effort. The repeated level check now belongs to one coherent step. These are available lenses, not fourteen required output sections.

## Nine useful stances

| Stance | Apply it this way | Limit to remember |
|---|---|---|
| **Agency: improve the situation** | Combine ownership, confidence, resilience, creative execution, and influential communication to find a feasible next move. | Constraints, permissions, capacity, and dependencies are real. Naming them or escalating is not surrender. |
| **Inner and outer conditions** | Improve team clarity, standards, and working conditions while influencing external constraints where possible. Filter needless pressure. | Leaders have neither zero external influence nor absolute internal control. Do not hide consequential problems or absorb unlimited work. |
| **The three-quarter-full cup** | Bring expertise while leaving room for input and correction. Be clear when presenting a considered decision. | Confidence should not become fabricated certainty or an excuse to conceal material unknowns. |
| **Seek truth rather than approval** | Ask what evidence supports the choice and what would contradict it. | Disagreement is not proof of insight; a sensible experiment is not necessarily cover for indecision. |
| **Diagnose before prescribing** | Test the explanation before committing heavily to a remedy. Small actions can help reveal the cause. | Diagnosis is valuable, but not a measured 90% of every solution and not itself a cure. |
| **Keep developing judgment** | Study stronger work, identify specific gaps, practice, and compare expectations with outcomes. | Another person's success can reflect skill, context, opportunity, and luck; avoid either dismissing or idealizing it. |
| **Respond with emotional maturity** | Describe behavior, pause before reacting, set boundaries, and escalate persistent harmful conduct through appropriate channels. | Avoid labels such as “adult baby” or claims that people cannot learn. Do not infer a personality from a disagreement. |
| **Notice what practice reinforces** | Protect time for the work that develops judgment; make status communication useful and proportionate. | Updates can establish a critical decision or commitment. They are not automatically empty optics or low-leverage work. |
| **Examine human and system causes** | Consider fear, incentives, ambiguity, skills, workload, tools, and decision rights together. | Not every project problem is psychological, and an emotional explanation is a hypothesis to check. |

See [the judgment principles](references/judgment-principles.md) for the nineteen decision lenses, including LNO and its time-horizon companion, 3X, taste, delegation, estimates, and influence.

## Keep the central distinctions clear

**Impact, execution, and optics** describe different concerns: the value created, the quality of delivery, and how the work is understood. Clarify which concern a discussion addresses. All three can matter; disagreement does not automatically mean someone is optimizing appearances.

**LNO** asks where extra care meaningfully changes the result. Leverage work merits greater attention; Neutral work needs an appropriate standard; Overhead work needs reliable completion without unnecessary polish. The same activity can fall into different categories. A bug report, evaluation repair, or decision note can be high leverage when its consequences warrant it. Necessary accuracy, safety, and confidentiality do not disappear because a task is labeled Overhead.

**Time horizon** is separate from leverage. Near-term incident response may be high leverage; a long-range presentation may add little. Protect future-looking work without delaying consequential alerts for an arbitrary 24 hours or discounting a harmed user because they are not a power user. Assign operational ownership and severity-based response times.

**3X** distinguishes Explore, Expand, and Extract. Change emphasis as uncertainty and scale change: learning in exploration, overcoming growth constraints in expansion, and sustainable value in maturity. Evidence, economics, documentation, and responsible risk-taking can matter at every stage. There is no blanket ban on early A/B tests or a requirement that every mature decision use one.

**Taste and evidence** work together. Form a reasoned expectation before metrics arrive, then test and refine it. AI can help generate, critique, and synthesize high-value ideas; the responsible decision-maker must still assess the evidence and retain accountable judgment. Do not confuse using assistance with abandoning thinking, or declare current model capabilities from an old categorical claim.

## Diagnose without turning a label into a verdict

Use [the diagnostic library](references/diagnostic-frameworks.md) for all nine original frameworks:

- A: PM-dominated, PM-serviced, and PM-guided cultures;
- B: seven product fallacies;
- C: feature teams and empowered product teams;
- D: possible incentive distortions within functions;
- E: decision quality;
- F: pre-mortem;
- G: listening quality;
- H: joint alignment conversations;
- I: AI agency and human control.

The same reference retains five failure categories and ten recurring patterns, with alternative explanations and recovery actions. These are hypotheses to investigate. Do not assume every outcome was controllable, every failure was poor thinking, every stakeholder concern was politics, or every product without direct revenue was wasted work.

For AI agency, use the canonical levels in `rtp-autonomy-spectrum` rather than a second conflicting numeric ladder. Start at the non-AI baseline where appropriate; classify the actual allowed action, oversight, and recovery. “Copilot” does not guarantee low risk, and review after an action is not equivalent to approval before it.

## Ask focused questions and use proportionate evidence

The [100-question bank](references/question-bank.md) covers product quality, decisions, strategy, customers, organizations, stakeholders, and AI. Choose the few questions that reveal the decisive uncertainty. A long questionnaire is not evidence of depth.

The [reference tables](references/reference-tables.md) cover reversibility, feedback, meeting purpose, conflict, AI assistance, stage-appropriate work, and possible stakeholder motivations. Their six advice-pair resolutions help avoid replacing one rigid slogan with its opposite.

Treat customer ranking as one signal alongside severity, unmet need, frequency, switching costs, and actual behavior. A single accessibility, security, or safety report can warrant action. Keep experiments and controls when they answer a real question; comparing alternatives does not mean removing the current baseline or forcing three expensive live launches.

Present source-supported observations separately from interpretations. Label numerical examples as illustrative unless the source establishes the population and method. This skill does not establish an optimal 20/50/30 calendar, a universal leverage multiplier, an automatic ten-person chain of poor hires, or the cause of any named company's outcome.

## Deliver something the user can act on

Match the requested format and depth. A substantial evaluation can contain:

```text
Decision and context:
Recommendation:
Evidence and diagnosis:
Alternatives and opportunity cost:
Important assumptions and counterevidence:
Owner, next action, and constraints:
Success or failure signals and reconsideration point:
```

Omit fields that do not help a short answer. For a sensitive organizational diagnosis, describe the observed conduct and practical intervention rather than using pejorative labels. For a decision under uncertainty, make the important unknown explicit without pretending certainty or deferring indefinitely.

Route to `rtp-problem-ai-fit`, `rtp-jtbd-analysis`, or `rtp-opportunity-solution-tree` for problem and solution work; `rtp-strategy-canvas`, `rtp-cost-model`, and `rtp-fit-signal` for bets and evidence; `rtp-judgment-guard` for learning and review capability; and `rtp-stakeholder-communications` for a difficult conversation. Use the relevant agent, safety, evaluation, and observability skills before consequential AI behavior is finalized. Domain skills add detail without requiring every artifact they can produce.

## Final self-check

Have you answered the actual question, considered a credible alternative, and supported the consequential diagnosis? Are effort and evidence appropriate to the decision? Have you respected actual authority and constraints, named the cost of the recommendation, and kept useful uncertainty visible? If the framework did not improve the decision, simplify the response.

The six inherited meta-principles remain: the opposite of bad advice is not automatically good advice; judgment develops through practice and feedback; thinking quality matters alongside execution; examine reasoning when investigating failure; advice must fit its audience and context; and frameworks can convey learned experience without replacing judgment. Proven procedures and necessary controls can remain useful after expertise grows.

Editorial revision: September 13, 2026. All original framework families and question categories are retained in the linked references. Practitioner ideas are attributed with source limits; the opening judgment principle is expressed as this skill's synthesis rather than an unverified direct quotation.
