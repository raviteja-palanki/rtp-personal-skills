---
name: opportunity-solution-tree
version: v1.1.1_latest
description: 'Connect a desired product outcome to customer opportunities, possible solutions, and assumption tests using Teresa Torres’s Opportunity Solution Tree. Add an AI feasibility and evaluation check at the solution or component level: compare rules, AI, hybrid, and non-software approaches, and identify what can be tested before committing to delivery. Use for discovery, quarter planning, or choosing among directions. Keep the customer need distinct from a proposed technology, rank opportunities on evidence and outcome relevance, and assess effort after considering solutions. Record investments, deferrals, and rejections honestly without a rejection quota. Pairs with jtbd-analysis, determinism-compass, problem-ai-fit, eval-framework, ai-use-case-readiness, and ai-portfolio-management. Triggers: what should we build, map opportunities, quarter planning.'
imports:
  - problem-ai-fit
  - determinism-compass
  - jtbd-analysis
  - eval-framework
---

# Opportunity Solution Tree

Map the paths from a desired outcome to customer needs, candidate solutions, and the assumptions worth testing. Use the tree to choose where to learn and invest. It is a living model of discovery, not automatically a committed roadmap.

The AI-specific addition is an explicit check of **how a candidate could work and how its value and failures could be assessed**. Apply that check to solutions and components. The same customer opportunity may have a simple rules-based solution, an AI solution, a hybrid, or a change to the workflow.

## Establish the outcome and the decision

Name the product area, intended users, planning horizon, constraints, and decision owner. Reuse known context and follow the Universal Skill Protocol at the source library root or packaged plugin root, scaling the artifact to the decision.

Write the desired outcome as an observable change, with a baseline, target, time horizon, and measurement owner where available. For example, “reduce unplanned downtime on Tier-1 assets by 30% over four quarters” is an illustrative goal that still needs a baseline, scope, and feasibility check. Choose a target for its value and evidence, not because people find it bold.

If the outcome is vague, help clarify it. A provisional outcome with an explicit measurement gap can support early exploration; do not invent a number or refuse useful work solely because a baseline is missing. Identify what the team can influence and the safeguards that must hold while pursuing the metric.

A known bug or fixed obligation may need direct execution rather than a full tree. A committed direction can still contain unresolved customer, implementation, or evaluation choices. Use the tree only where comparing paths will improve the decision.

## 1. Build the four layers

| Layer | What belongs here | Example or check |
|---|---|---|
| **Desired outcome** | The change the team is trying to produce | Reduced unplanned downtime for a defined asset population |
| **Opportunities** | Customer needs, pain points, and desires relevant to the outcome | Operators cannot tell which alerts need attention now |
| **Solutions** | Distinct ways to address a selected opportunity | Better rules, model-assisted ranking, a collaboration workflow, or fewer unnecessary source alerts |
| **Assumption tests / experiments** | Focused checks of what a solution or framing depends on | Test whether relevant evidence lets operators identify important alerts accurately and in time |

Ground opportunities in interviews, feedback, observed work, or other traceable evidence. Use customer language without inventing quotations. Preserve unmet desires as well as frustrations. If a proposed opportunity lacks evidence, mark it as a research hypothesis with its source and uncertainty.

Keep a need separate from the implementation: “I need a dashboard” may point to “I cannot see which issues require action.” Ask whether more than one approach could address it. A JTBD statement helps identify those needs; translate its relevance into the product outcome rather than treating the job statement and outcome as interchangeable.

Group opportunities where relationships help understanding. Three to seven is a possible working set, not a rule, and the tree need not stop at one level of opportunity detail. Preserve meaningful distinctions instead of forcing the tree into a target shape.

Choose a target opportunity before exhaustively designing every branch. Explore multiple meaningfully different solutions for that target, often two to four. For a consequential decision, compare alternatives rather than several cosmetic versions of the first idea. Do not require every unselected opportunity to have a full solution and experiment set.

## 2. Select opportunities on evidence and outcome relevance

Compare the importance and reach of the need, its likely contribution to the outcome, available evidence, strategic relevance, and major uncertainties. Consider rare serious consequences as well as frequency. Keep the evidence behind each judgment visible.

An optional compact rubric can use **impact** and **evidence confidence**, each from 1 to 5. Define what the levels mean for this decision. If a numeric sorting aid helps, explicitly compute `impact × confidence`; the result ranges from 1 to 25. It is an ordinal prioritization heuristic, not an expected-value estimate or proof of feasibility. Related interviews, surveys, and behavioral measures are not automatically independent corroboration.

Estimate effort for **candidate solutions**, not for an opportunity before exploring how it could be addressed. A hard-looking need may have a simple remedy. Include a cost range, uncertainty, dependencies, and ongoing work once a candidate is concrete enough.

For comparable solutions, one optional effort scale is 1 = least effort through 5 = greatest effort; lower is easier. Use that direction consistently. The older rubric inverted the scale and then broke ties in the wrong direction. Avoid mixing a vague opportunity score with a precise delivery date.

Choose the number of next bets from capacity and uncertainty, not a quota of three to five. Show why the chosen path deserves attention and what evidence could change the choice.

## 3. Apply the feasibility and evaluation check

Use the following labels as planning aids, adding **hybrid** or **unknown** where needed. They are not labels for the customer need itself and do not authorize release.

| Candidate approach | What the label means | Next action |
|---|---|---|
| **Deterministic / non-AI** | Rules, lookup, ordinary software, a service, or a process change appears suitable | Test correctness, usability, and value; assess delivery normally |
| **Probabilistic with a credible evaluation path** | AI may add value, and a specific way to assess outcomes and relevant failures exists | Compare with the baseline and test the important assumptions |
| **Probabilistic with unresolved evaluation** | The current proposal lacks sufficient evidence or a credible way to judge its consequential behavior | Investigate measurement, narrow the use, find alternatives, or defer exposure |
| **Hybrid or not yet known** | Different parts need different methods, or decomposition and evidence are incomplete | Name the uncertain component and the next discriminating test |

Do not equate “we can draw the logic in thirty minutes” with a correct deterministic solution. Experts can articulate an incomplete rule; a difficult-to-describe task may still have a simple alternative. Use `rtp-determinism-compass` for the component-level distinction and `rtp-problem-ai-fit` for whether AI earns its role.

For a candidate involving AI, specify the **evaluation path**:

- the task, population, reference or comparison, and expected behavior;
- the quality and user-outcome measures, with meaningful denominators;
- the important errors, their consequences, and how they will be detected;
- the test cases or sampling approach, relevant uncertainty, and owner;
- what evidence permits the next bounded step and what blocks or changes it.

Acceptance rate, expert agreement, and a model’s confidence can inform different questions. None is sufficient by itself to establish correctness, safety, or value. Values such as 80% agreement, 70% acceptance, or fewer than 5% confident errors are examples from the previous version, not ship thresholds.

Subjective quality, expert disagreement, delayed feedback, or dependencies outside the team’s control make evaluation harder; they do not automatically make it impossible. Define what can be assessed, how disagreement will be handled, and what a proxy does and does not establish. A useful offline measure can support learning while still leaving end-to-end impact unresolved.

A candidate with unresolved high-consequence evaluation should not proceed into exposure that requires that evidence. It can still merit research or a bounded, authorized prototype. Conversely, “with evals” means a testable candidate, not a decision to build it or increase autonomy.

## 4. Test assumptions before large commitments

For shortlisted solutions, name the assumptions about desirability, feasibility, usability, viability, and important risks. Prioritize the assumptions most capable of changing the decision and least supported by evidence.

Choose the smallest **credible** test, not simply the cheapest activity. A survey can investigate a stated preference but may not test actual behavior. A concierge or Wizard-of-Oz test can explore value while leaving automation feasibility open. A technical spike can investigate capability without establishing demand. An MVP can be an experiment if the hypothesis, scope, evidence, and decision rule are explicit; it is not automatically a valid test merely because it is small.

There is no requirement that an experiment cost less than 10% of a build or finish in one week. Account for exposure, fidelity, participants, opportunity cost, and what decision the result enables. Record support, contradiction, mixed evidence, and an inconclusive result as distinct outcomes.

### Use prototypes to clarify the problem too

A rough prototype can help people compare possible framings before committing to a solution. Link it to the question being investigated, including across opportunities if appropriate. Prototypes have long served exploratory purposes; cheaper production may make that option more accessible in a particular team, rather than inventing a new use universally.

Assess an exploratory prototype by useful distinctions, assumptions, questions resolved, or uncertainties exposed. A polished prototype is not inherently misleading, and agreement is not inherently failure. Choose fidelity for the question. If realistic interaction is essential to the test, deliberate roughness can conceal rather than reveal the problem.

Record new questions as assumptions or research tasks linked to the relevant nodes. Do not relabel every question as a customer opportunity. Give framing work a visible completion criterion—such as an agreed problem statement and a testable uncertain assumption—without making disagreement or a count of new questions the goal.

The local August 2026 buildathon account motivates this practice. A contest rubric emphasizing problem definition cannot independently prove that problem definition is the main source of market advantage. Its framing and prototype observations remain hypotheses to apply and assess in context; see [evidence notes](references/evidence-and-calculations.md).

## Worked example: predictive maintenance

For the illustrative downtime outcome, suppose evidence suggests five opportunities: alert overload, slow diagnosis, schedules disconnected from asset condition, difficulty reconstructing why a recommendation was declined, and parts unavailable when needed. The earlier 78% ignored-alert figure and 4.2-hour mean diagnosis time are scenario values, not measured benchmarks.

For alert overload, compare severity rules, an AI ranking system, a collaboration view, and changes to source alerts. A documented rule can be a baseline; it still needs validation. An AI ranking test should examine both high- and low-ranked cases, appropriate action, missed important issues, false alarms, and task burden. Reviewing only the bottom half or optimizing acceptance can miss consequential errors.

A decision-record workflow may use ordinary software even if the surrounding product uses AI. Its evidentiary integrity, usability, and permissions still require work. Keep it in the overall delivery plan; labeling it deterministic does not make it irrelevant to the AI product.

Parts staging depends on prediction, inventory, procurement, and delivery. “The right part arrived in time” is measurable even when not fully controllable; attribution and feasibility are the difficult questions. Narrowing to five asset classes with known supply conditions could make a test more informative. Pooling parts across customers is a separate operational proposal requiring its own evidence and authority, not an automatic safe first step.

A reasonable provisional sequence might test useful rules and decision records while running a bounded ranking study, then consider wider rollout only if the complete evidence supports it. Q1 or Q3 dates must come from actual capacity and dependencies. Document any deferred staging candidate, its reason, and the condition for revisiting it rather than declaring the whole customer opportunity unevaluable.

## Make the investment and deferral decisions explicit

For each considered path, record **investigate**, **test**, **deliver**, **defer**, or **decline**, with rationale, owner, and relevant review trigger. A rejection list is useful when real alternatives were rejected. An empty list is not automatically a defect, and forcing two or three “no” decisions manufactures rigor rather than demonstrating it.

Explain how selected bets fit capacity and dependencies. Revisit the tree as interviews, tests, delivery, and outcome evidence change it. Preserve earlier decisions so the same proposal is not repeatedly reconsidered without recognizing what changed.

Hand the work forward deliberately:

- `rtp-jtbd-analysis` and `rtp-feedback-triage` supply candidate customer needs; verify their scope and evidence before placing them in the tree.
- `rtp-problem-ai-fit` and `rtp-determinism-compass` assess the proposed approach; `rtp-eval-framework` makes the evaluation design concrete.
- `rtp-uncertainty-research` helps choose research and assumption tests.
- `rtp-ai-use-case-readiness` assesses action rights, controls, and feasible autonomy for a supported candidate.
- `rtp-ai-prd` specifies a delivery decision; `rtp-ai-portfolio-management` coordinates competing investments and shared defer/decline records.

## Deliver and review

Lead with the desired outcome, target opportunity, current decision, biggest uncertainty, and next test or action. Include the tree, evidence links, candidate labels, and decision record in the format the user needs. For a visual tree, use labels as well as colors; distinguish unresolved evidence from a confirmed rejection and avoid green implying permission to ship.

Check that opportunities describe customer needs, solutions remain alternatives, evaluation is specific to the task, score arithmetic is consistent, and commitment reflects capacity. Confirm that important non-AI options remain visible and that no fixed branch count, deterministic-work percentage, rejection quota, or arbitrary threshold shaped the result.
