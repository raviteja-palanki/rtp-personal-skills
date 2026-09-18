---
name: discover
description: Run the full discovery cycle for a new AI feature or problem space.
---

# /discover

Take a rough problem area or feature idea and run it through the discovery chain — problem framing, JTBD analysis, opportunity-solution tree, assumption mapping, and experiment design. Output is a discovery doc ready for stakeholder review.

**Timeline:** 1-3 days for a focused area, 1-2 weeks for a broad space
**Audience:** PM, design lead, eng lead, AI specialist
**Output:** A discovery brief that names the problem, the hidden job, the opportunity space, the riskiest assumptions, and the next experiments

## When to use

- A team is proposing a new AI feature and needs to test the problem before scoping the solution
- An existing AI feature has flat adoption and the team needs to revisit the problem framing
- A quarterly planning cycle is starting and the team needs a structured way to choose between candidate directions
- A stakeholder said "we should use AI for X" and the PM needs to either confirm the problem-AI fit or push back

## When not to use

- The work is clearly scoped (regulatory deliverable, contract obligation, known bug fix)
- The team is in execution mode on a single committed direction — discovery work is overhead
- The problem has been discovered already and the team is now in solution design — use new-ai-feature workflow instead

## Input

Provide one of:
- A rough problem statement ("operators are ignoring most alerts")
- A feature idea ("AI-powered alert prioritization")
- A user complaint pattern ("we're hearing X from customer success")
- A business outcome ("reduce unplanned downtime 30%")

If the input is empty, ask: "What problem area, user struggle, or rough idea do you want to explore?"

## The chain

This workflow chains five skills. Each output feeds the next.

```
rtp-problem-ai-fit  →  rtp-jtbd-analysis  →  rtp-opportunity-solution-tree  →  assumption mapping  →  experiment plan
   (Step 1)         (Step 2)              (Step 3)                  (Step 4)              (Step 5)
```

### Step 1 — problem and AI fit

Run `rtp-problem-ai-fit`. Establish:
- WHO the customer actually is (segment, not "users")
- WHAT problem they have in their words
- HOW they solve it today (the real competitor)
- WHETHER AI is genuinely needed (the 4-question test, the lookup table test)

**Output of this step:** an AI-fit recommendation. One of: "Build with AI," "Build with rules," "Build hybrid," "Don't build at all," or "Gather more evidence."

If the recommendation is "Don't build at all," stop the workflow. Document the decision and move on.

If the recommendation is "Build with rules," the rest of the workflow doesn't need the AI lens — but the JTBD analysis and OST still apply. Continue with the deterministic framing.

If the recommendation is "Build with AI" or "Build hybrid," continue.

### Step 2 — JTBD analysis

Run `rtp-jtbd-analysis`. Decipher:
- The surface job (what the user says they want)
- The hidden job (what they're actually hiring AI to do — emotional, social, cognitive)
- The four forces (push, pull, anxiety, habit)
- The design implication (what changes when you design for the hidden job)

**Output of this step:** a job statement (two layers), a four-forces diagram, and a one-paragraph design implication.

If the four-forces analysis shows that anxiety + habit > push + pull, flag this. The problem may be real but the solution won't be adopted. The workflow continues, but the assumption map will need to address adoption fragility explicitly.

### Step 3 — opportunity-solution tree

Run `rtp-opportunity-solution-tree`. Build:
- Desired outcome (sourced from problem-AI fit and JTBD analysis)
- 3-7 opportunities (user struggles in user voice)
- 2-4 solutions per opportunity
- AI-feasibility filter on every solution (Deterministic / Probabilistic+Evals / Unevaluable)
- Scoring (impact × confidence × effort) and ranking

**Output of this step:** a ranked tree with explicit "no" list (opportunities considered and rejected, with reasons).

If the tree has zero "Probabilistic+Evals" entries, the recommendation may be to leave this alone as an AI investment, because the work is mostly deterministic. Honor that answer rather than forcing an AI label onto it.

### Step 4 — assumption mapping

For the top 1-2 opportunities, surface every assumption embedded in the framing. Use the format from `rtp-problem-ai-fit` Step 4:

| Assumption | Evidence Level | Load-Bearing? | How to Test |
|---|---|---|---|
| ... | Validated / Informed / Assumed / Unknown | Yes / No | ... |

Sort by: Unknown + Load-bearing first. These are what kill the project if untested.

Pull in `rtp-uncertainty-research` here for the test design — the right research method depends on the assumption type (desirability vs feasibility vs viability).

**Output of this step:** an assumption table with at least 5 assumptions per top opportunity, sorted by risk.

### Step 5 — experiment plan

For the top 2-3 riskiest assumptions, design the cheapest test that would prove or disprove them.

Each experiment includes:
- **Hypothesis:** "If we [intervention], [user segment] will [behavior change], because [reasoning]"
- **Method:** Wizard-of-Oz / concierge / fake door / prototype / switch interview / longitudinal study
- **Sample size:** Calibrated to the variance and the confidence needed
- **Bar:** What result confirms vs disconfirms
- **Timeline:** How long the experiment runs

For probabilistic solutions, the experiment must address the eval surface — not just "do users like it" but "can we measure whether the AI is doing the job well."

**Output of this step:** 2-3 experiments ready to run, each scoped to <2 weeks where possible.

## The discovery brief

Compile the five outputs into one document:

```markdown
# Discovery: [problem area]

## Executive summary
[3-5 sentences. The recommendation, the hidden job, the top opportunity, the riskiest assumption, the next experiment.]

## problem and AI fit
- Customer: [segment]
- Problem: [in user words]
- Current solution: [the real competitor]
- Recommendation: [Build with AI / rules / hybrid / don't build / gather evidence]
- Hypothesis: [if true / if false / damage if wrong]

## JTBD analysis
- Surface job: [statement]
- Hidden job: [statement]
- Four forces: [push / pull / anxiety / habit summary]
- Design implication: [paragraph]

## opportunity-solution tree
- Desired outcome: [sentence]
- Top 3 opportunities (ranked):
  1. [opportunity] — [score, top solution, AI-feasibility]
  2. ...
  3. ...
- Said no to: [opportunities considered and rejected, with reasons]

## Assumption map
[Table — 5+ assumptions for top opportunity, sorted by Unknown + Load-bearing first]

## Experiment plan
1. [Experiment 1] — testing [assumption] via [method] in [timeline]
2. [Experiment 2] — ...
3. [Experiment 3] — ...

## Open questions
[What this discovery cycle didn't answer. What we'd need to learn before committing.]

## Recommended next step
[Singular. One concrete action. Owner. Date.]
```

## Quality bar

A complete discovery cycle:
- Ends with a singular recommendation, not a menu of options
- Names the hidden job, not just the surface job
- Has at least one opportunity flagged "Probabilistic + Evals" with an eval surface specified, OR honestly says "this is deterministic, don't burn AI bandwidth"
- Has at least 5 assumptions ranked, with the top 2-3 having experiment designs
- Names what the team is saying NO to
- Is ready to forward to a VP without editing

If any of those is missing, the cycle isn't done. Loop back to the missing step.

## Closing protocol

Before closing the discovery cycle:
1. State the recommendation in one sentence
2. State the riskiest assumption in one sentence
3. State the next experiment in one sentence
4. Ask: "Are we discovering, or are we rationalizing a pre-decided direction?" If the latter, restart at Step 1 with a different framing.

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.
