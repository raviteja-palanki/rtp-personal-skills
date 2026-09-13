---
name: rtp-strategy-canvas
version: v1.2.1_latest
description: 'Choose where an AI product will compete, which customer outcome it will improve, and why the organization can deliver and sustain that value. Use for a new strategy, a quarterly review, a major assumption change, or a roadmap that needs clearer choices. Work through seven connected steps: Objective, Users, Superpowers, Vision, Pillars, Impact, and Roadmap. Separate durable assumptions from uncertain ones; write conditional bets, credible alternatives, and explicit review triggers. Produce a concise canvas with priorities, exclusions, evidence, resource commitments, owners, and a review date. Treat feedback loops, model advantages, and strategy lifetimes as claims to test, not universal rules. Connect to moat-finder, vision-setting, ai-portfolio-management, capability-tracking, harness-operating-model, and token-economics for their deeper analysis. Triggers include AI strategy, strategic direction, product strategy, and quarterly strategy reset.'
imports: [first-principles, moat-finder]
---

# Strategy Canvas — AI Product Strategy

Help the team make a small set of consequential choices: whose problem to solve, what outcome to pursue, where to invest, and what to decline. Produce a concise canvas that an engineer, designer, or business partner can use in an actual decision. Keep evidence and detailed calculations in linked supporting material.

## Start with the decision and its boundaries

Identify the product, customer segment, planning horizon, decision owner, available resources, and decision needed now. Use existing research and approved constraints. Ask only for missing information that could change the choice; otherwise label assumptions and proceed.

Establish what is open to change and what is fixed: commitments, service obligations, rights to data, acceptable harm, budgets, and required approvals. A strategy recommendation does not authorize a deployment or expand an agent's permissions. Separate the decision to investigate a capability from the decision to release it.

A short canvas can help before product-market fit: use provisional choices, small experiments, and limited commitments. In a new market, acknowledge that few assumptions are stable. During execution, revisit strategy when evidence warrants it; avoid repeatedly reopening settled choices without new information.

Three principles guide the work:

- **Direction and execution both matter.** Faster production can increase the cost of choosing poorly, but engineering, distribution, operations, and adoption may still constrain results. Use a thirty-second explanation as a communication test, not a definition of strategic quality.
- **Name the actual source of advantage.** A compounding feedback loop inside an important workflow is one possibility. Distribution, economics, trust, scarce capabilities, and other mechanisms can matter. Using a widely available model alone rarely explains why customers will choose this product; a differentiated model can itself be strategic. Test the case with `moat-finder`.
- **Plan for assumption changes.** Review dates and conditional bets make adaptation deliberate. A new model release does not automatically invalidate the strategy, and a strategy does not need an arbitrary expiry date to be rigorous.

Use AI to propose options, challenge assumptions, synthesize evidence, and draft the canvas. The responsible people own the choices and bring context the system may lack. Neither AI-generated text nor a leader's intuition substitutes for evidence about customers and constraints.

## The seven connected steps

Work in this order when starting from scratch. Revisit earlier steps when later evidence changes them; reuse completed work instead of performing every analysis again.

### 1. Objective — connect purpose to a measurable outcome

State the customer or organizational purpose, then the outcome, baseline, target, population, and date. For example: increase eligible new-user activation from 34% to 45% by Q3 while maintaining the agreed quality and cost limits. A second illustration is improving 30-day retention from 18% to 22%. These are examples, not targets to copy.

Prefer one primary outcome and a small number of supporting outcomes. Three or fewer is a useful focus prompt, not a mathematical limit. Name guardrails and competing obligations separately. Explain what the metric captures and what it misses.

Consider where AI could help: recurring friction, pattern-rich errors, data-intensive decisions, creative work, or an expertise gap. Compare simpler and non-AI alternatives. A technically interesting use case earns investment through its contribution to the objective.

**Check the urgency trap before selecting a solution.** A visible cost or speed metric can crowd out a less measurable but more important need. Connect the use case to purpose and compare opportunity costs. Urgent operational improvements can be entirely appropriate; they do not have to create a new business category. The [nine purpose-and-urgency questions](references/evidence-and-planning-notes.md#nine-questions-for-a-strategy-discussion) help when framing is unclear.

### 2. Users — understand the job and operating context

Specify the customer, user, buyer, and affected people where these differ. Understand the job, current alternatives, stage of experience, pain, and circumstances. Demographics can matter, but they do not replace this explanation. Christensen's milkshake case illustrates looking beyond a product category to the job it serves; it is not a claim that every purchase has one hidden motive.

For AI, identify appropriate reliance, collaboration boundaries, learning needs, error visibility, and fallback. Trust should follow demonstrated reliability for the task. Do not assume every user follows a fixed adoption curve or that greater trust is always better. Route detailed work to `jtbd-analysis`, `uncertainty-research`, and `adoption-launch`.

**Test demanding conditions in the intended market.** Consider an inexperienced user with an unclear prompt, a tired reviewer, incomplete context, and a small screen or unreliable connection. Compare these with the ideal demonstration. Start with the constraints most consequential to the target segment; retain minimum quality and safety. A design that handles constraints may transfer elsewhere, but performance, affordability, and usability can conflict. Validate the transfer rather than promising that the better-resourced case becomes free.

Look for shared core value across markets and specify the adaptations each market needs. Field exposure can challenge organizational assumptions; combine it with analysis and engineering feasibility. Constraint-first design is a useful hypothesis, not a requirement to serve every customer or the most extreme imaginable condition.

### 3. Superpowers — explain why this organization can win

A superpower is a specific advantage relevant to the chosen customer and competition. Distinguish an existing advantage, a temporary lead, and an advantage the team hopes to build. Use `moat-finder` to test the mechanism, replication cost, durability, and value capture.

Ask: if a competitor gained comparable model capability, what would remain distinctive? Investigate data rights and quality, useful feedback, workflow integration, domain knowledge, switching costs, distribution, and other applicable advantages. The model-swap test is a useful stress test, not a complete moat verdict: provider access, integration difficulty, economics, and specialized model quality may differ.

Do not force every strategy to claim a proven moat or a learning loop. An early product may have a credible customer benefit and a plan to investigate defensibility. If claiming a loop, show how authorized usage becomes feedback, how improvements are validated, and who captures the benefit. Activity and data accumulation alone do not establish compounding.

### 4. Vision — make the intended experience concrete

Show the before-and-after experience, the role of people and AI, the benefit, and the recovery path. A short narrative, storyboard, mock-up, or working prototype can do this. A working vision prototype, sometimes called a visiontype, is useful when interaction matters; it is not required for every strategic choice.

Tools such as Bolt, Lovable, v0, or Replit are examples to assess against current needs and permissions, not a prescribed stack. An afternoon prototype can explore an idea; it is not evidence that a production system is feasible, safe, or commercially viable. Label simulated behavior and unproven feedback improvements. Route the deeper work to `vision-setting`.

### 5. Pillars — allocate resources across a few coherent bets

Choose a manageable set of priorities, often two to four, and state what each receives: money, people, attention, dependencies, and an owner. Explain the work deferred or excluded. A list of themes without commitments is incomplete.

Use `ai-portfolio-management` to compare quick wins, strategic investments, and option-building experiments. The old examples of 1–3 months for quick wins and 3–12 months for larger bets are planning ranges, not definitions or delivery promises. Mark investments offensive, defensive, or foundational where that clarifies their purpose. Choose allocation ratios from constraints and objectives; no fixed mix is universally correct.

A small experiment can buy information, a shared foundation can support several bets, and stopping can release resources. Cost the current course and waiting alongside new investment.

### 6. Impact — model value and the mechanism behind it

Estimate benefits, costs, uncertainty, and the alternative baseline over a stated horizon. Include adoption, quality, human review, integration, operating costs, and the destination of any released capacity. Distinguish a reduction in effort from realized cash savings or revenue.

Conventional unit economics and scenario analysis remain useful. Add learning curves, network effects, or second-order benefits only when the mechanism and evidence justify them. An AI product does not automatically improve with each interaction. Feedback may be sparse, biased, unusable, or costly; model updates may regress.

Show a base case and decision-relevant upside and downside. Explain the assumptions most capable of changing the recommendation and how to test them. `cost-model` and `token-economics` own the detailed calculations.

### 7. Roadmap — turn choices into sequenced learning and delivery

Translate the vision and strategic bets into outcomes, experiments, enabling work, and release decisions. Name dependencies, owners, commitments, and what remains conditional. Features should serve those choices rather than originate solely from competitor lists or brainstorming.

Discovery and feasibility findings can revise the vision or strategy; the sequence is iterative. Mandatory maintenance, accessibility, security, or contractual work can be justified explicitly even when it does not map neatly to a growth bet. Pass the strategic frame to `ai-prd` and the relevant discovery or roadmap skill.

Continue learning after release. An early feature may need substantial improvement, but mediocrity is not inevitable or a reason to relax essential acceptance criteria.

## Make the strategy adaptable

### Separate assumptions by stability and consequence

For each important assumption, record evidence, uncertainty, likely change, consequence if wrong, and monitoring owner. Classify it as relatively durable, volatile, or unknown for the chosen horizon.

User needs, market structure, regulation, and organizational capabilities are possible anchors, not guaranteed stable facts. Model performance, cost, context limits, and competitive parity may move quickly or remain unchanged. Weight dependencies by consequence rather than counting how many fall in each column.

### Write conditional bets with usable alternatives

Use this form when a meaningful uncertainty affects the commitment:

> If [observable condition on the relevant task] is met by [date], choose [Path A, subject to its release requirements]. Otherwise choose [Path B], with [owner, resources, and next decision date].

Path B may be assisted operation, a narrower scope, another implementation, a bounded wait, or stopping. It need not be a second product to ship. Describe its costs and benefits so it is a real choice rather than a vague promise to reconsider.

For example, evaluate an autonomous legal-research workflow only if task performance, serious-error limits, review arrangements, data rights, and economics meet agreed criteria on representative evidence. Otherwise retain retrieval-assisted human research or stop the investment if neither option creates enough value. Define the actual action permissions; an autonomy label is insufficient.

The old example of 85% multi-step success and fewer than two errors per ten steps is illustrative and underspecified: task success and step errors have different denominators, and neither establishes safety. Set thresholds from the work and consequences. Qualitative events, such as a confirmed supplier withdrawal, can also be precise triggers.

### Define review triggers and who responds

| Trigger family | Evidence to watch | Decision to revisit |
|---|---|---|
| Capability change | Representative evaluation shows a material change in relevant performance, cost, or limitations | Implementation, scope, or timing of affected bets |
| Competitor parity | A relevant competitor changes the customer's credible alternatives | Differentiation, pricing, distribution, and defensibility |
| Cost change | End-to-end costs cross the investment's viability range | Unit economics, operating approach, and investment level |
| Assumption challenged | Credible customer or operational evidence contradicts a consequential belief | The belief and the bet it supports |
| Regulatory or contractual change | Applicable requirements or rights change | Permitted use, controls, commitments, and release conditions |

For each trigger specify the source, threshold or event, owner, response time, and decision authority. The former 15% benchmark improvement, 40% inference-price decline, and four-week evidence window were examples, not universal gates. Do not delay responding to consequential evidence until a quota or observation period is met.

A trigger starts a review; it does not automatically pivot the strategy. No triggers firing for six months can reflect stability. Check coverage and sensitivity before concluding that monitoring is ineffective.

### Set the next review without inventing an expiry law

Choose a review date based on exposure, commitment size, evidence arrival, and change rate. Quarterly, or within 90 days, is a useful starting cadence for many teams; adjust with a reason.

If using the phrase strategy half-life, state what would be declining and how it is estimated. Prefer a concrete assumption horizon when no measurable quantity exists. The historical bands of 0–3 months for frontier features, 3–6 for competitive features, 6–12 for market structure, and 12+ for user problems are heuristics, not empirical lifetimes. A temporary advantage can still justify investment when timing and returns support it.

## The concise canvas

Aim for one page that makes the choices easy to find. Link necessary evidence rather than shrinking text or omitting consequential constraints to meet a page limit.

```text
STRATEGY CANVAS — [product, date, owner, planning horizon]
PURPOSE / OBJECTIVE | Customer benefit; metric, baseline, target, population, date
USERS / CONTEXT     | Priority segment, job, alternatives, constraints
VISION             | Intended experience and human/AI responsibilities
ADVANTAGE          | Mechanism, evidence, durability, unresolved moat questions
ASSUMPTIONS        | Durable / volatile / unknown; consequences and owners
PILLARS / BETS     | Chosen investments, allocations, dependencies, exclusions
CONDITIONAL PATHS  | If [condition] by [date] → A; otherwise B; commitment limits
IMPACT             | Value, full costs, scenarios, guardrails, evidence gaps
ROADMAP            | Next learning and delivery steps; owners and dates
REVIEW TRIGGERS    | Observable events, response time, accountable decision owner
NEXT REVIEW        | Date and rationale; assumption horizon if useful
```

The seven steps all need a visible result. Do not let the adaptive layer replace the users, vision, allocations, impact, and roadmap that it is meant to support.

## Handoffs and final review

Reuse `north-star-metric` or the business objective; user evidence from `jtbd-analysis` and `adoption-launch`; advantage analysis from `moat-finder`; capability scenarios from `capability-tracking`; economics from `cost-model` and `token-economics`; and market evidence from `competitive-map` and `signal-scanner`.

Pass portfolio choices to `ai-portfolio-management`, the experience direction to `vision-setting`, feature rationale to `ai-prd`, stakeholder reasoning to `stakeholder-communications`, and the next review to `strategy-review`. For a harness investment, `harness-operating-model` assesses operating value and ownership while `agent-harness` develops architecture. Include harness maturity only if it affects a strategic choice. Use `trendslop-check` when fashionable language or a value-per-dollar claim is standing in for analysis.

Invite affected teams to challenge feasibility, trade-offs, and assumptions. Record decisions and meaningful unresolved disagreement. A canvas accepted unchanged can be well understood; forced disagreement or edits do not prove commitment.

Before concluding, check that:

- The priority customer, outcome, choices, and exclusions are understandable and actionable.
- Advantage claims are supported or marked as hypotheses; no feedback loop is invented.
- Resources and operating responsibilities support the bets, including fallback and review work.
- Consequential uncertainties have credible alternatives or bounded exposure.
- Triggers, metrics, denominators, guardrails, owners, and review dates are clear.
- Evidence, forecasts, illustrative numbers, and author synthesis are distinguishable.
- The canvas preserves all seven steps and routes deeper work to the right owner.

Use the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) for a proportionate trade-off ledger and handoff. Conclude with the recommended direction, hypothesis and falsifier, main trade-off, biggest risk and mitigation, and next action by role and date. Record what evidence would change the recommendation.

When a visual helps the audience or is requested, use `excalidraw-svg` to show the seven-step spine, assumptions, conditional paths, and sources of advantage. Show model dependence and defensibility as separate questions rather than labeling every model-based advantage fragile and every workflow durable.

The [concept guide](CONCEPT.md) explains the reasoning; [evidence and planning notes](references/evidence-and-planning-notes.md) retain the research distinctions and diagnostic questions.
