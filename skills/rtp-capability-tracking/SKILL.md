---
name: capability-tracking
version: v2.10.1_latest
description: 'Decide whether to build, buy, bridge, or wait for one AI capability as models and product needs change. Use for capability watchlists, custom-model investments, roadmap timing, and commoditization reviews. Compare measured task performance, the value of acting now, migration costs, and the evidence behind a forecast. Produce a capability radar, an advantage tracker, a dated harness-assumption register where relevant, and a decision with an owner and reconsideration trigger. Capability improvement does not by itself establish product value, safe automation, or workforce substitution. Track workforce dependencies here; use judgment-guard to design learning and oversight, and harness-operating-model to redesign the harness. Pairs with strategy-canvas, first-principles, build-or-buy, cost-model, and ai-product-metrics. Triggers include build versus wait, next-model dependency, capability decay, and roadmap risk.'
imports: [strategy-canvas, first-principles]
---

# Capability Tracking: Decide When to Invest as Models Improve

Use this skill to make one product decision: **what should we do about this capability now, and what evidence would change that decision?** A custom feature may become easier to provide through a newer model. Waiting can also leave a valuable need unmet. Compare both paths without treating a provider roadmap as a promise.

The core output is a dated recommendation: **build, buy, use a limited bridge, wait with a deadline, or stop pursuing the capability.** Explain the customer consequence, evidence, cost, uncertainty, and next review. For a quick decision, keep this inline. Expand into a register when several capabilities or repeated reviews warrant it; use the user's requested format without asking again.

## Start with the decision and its constraints

Use the context already available. Ask only for missing information that could change the decision:

- Who needs this, for what task, and what happens while the need remains unmet?
- What level of quality, latency, cost, reliability, and human oversight makes it useful?
- What do the current product, a simpler method, and available models achieve on this task?
- What investment is proposed, when must it pay back, and what alternatives lose capacity?
- Which data rights, dependencies, approvals, or operating constraints limit the options?

Separate a **measured result**, a **forecast**, and a **planning assumption**. Give each a source or rationale and a date. “Unknown” is useful information; do not invent a commoditization date to fill a table.

**Scope and handoffs.** This skill owns tracking and timing. `build-or-buy` compares implementation and ownership choices. `harness-operating-model` evaluates architecture changes. `judgment-guard` designs human oversight and the formation, retention, and transfer of judgment. Keep linked workforce evidence in this register when it affects the product decision; do not repeat the full learning-design process here.

## Keep seven distinctions in view

1. **Today's capability is a baseline, not a permanent ceiling.** Re-test custom work against credible alternatives as they change.
2. **An unreleased capability is a dependency with uncertainty.** Give a wait decision a bridge, a latest acceptable decision date, and an alternative if the forecast fails.
3. **Capability is one ingredient of a product.** Quality that takes too long, costs too much, or solves the wrong problem may have little customer value.
4. **Technical performance and defensibility differ.** A copied prompt can still provide useful service. Proprietary data, a fine-tune, or a complex harness is not automatically a durable advantage.
5. **Capability parity does not authorize automation.** Examine judgment under uncertainty, human accountability or assurance, consequences of errors, and applicable organizational or regulatory requirements. One consequential constraint can determine the operating mode; a count of two is not a valid gate. Low concern on these four dimensions does not replace the other launch checks.
6. **Present expertise and future expertise formation differ.** Good results from today's experts do not show how newcomers will develop with AI. Equally, do not assume nobody has studied learning with AI: check the population, training exposure, and outcome of each study.
7. **A moving baseline changes what a comparison means.** A person's unchanged score can look worse against a better model. Track absolute competence, assisted performance, and the comparison baseline separately. Public AI declarations and revenue per employee add context; neither directly measures day-to-day AI use or the technology's causal contribution.

## 1. Build a capability radar

Define the capability as a task under specified conditions, such as “answer a renewal-policy question with the correct policy version and a supported citation.” Avoid labels such as “reasoning” that are too broad to test.

Plot capabilities on two axes if a visual helps:

- **Horizontal:** estimated time until an accessible alternative meets the requirement. Optional planning bands are 0–3 months, 3–12 months, 12+ months, and unknown. Show a range and confidence rationale, not a promised release date.
- **Vertical:** business criticality, from low to high. Tag “core,” “differentiating,” or “nice to have” separately where useful; core and differentiating can overlap.

Start with the capabilities that could change the decision. Five is a convenient workshop size, not a required inventory limit. A critical capability approaching broad availability warrants a review of ownership and differentiation; it can also be an opportunity to lower cost.

Record the exact model and product versions, task population, measurement date, accepted quality level, and cost assumptions. A leaderboard result can nominate a candidate for testing; it cannot fill in your own result.

## 2. Measure the advantage before estimating its decay

Ask what advantage matters: fewer costly errors, faster completion, lower cost, access to otherwise unavailable information, or a better customer outcome. Compare against the best realistic alternative available to this customer, including a non-AI option where relevant.

Track the **gap**, not just your own score. If your system stays at 90% task success while an alternative rises from 70% to 80%, the quality gap falls from 20 to 10 percentage points. That is a halving of this gap over the observed interval. It is not a halving of your system's quality or a proof that the next interval will repeat it.

Use a half-life only when a decay model is meaningful and observations support it. Under an explicitly assumed exponential model:

`remaining advantage after t = initial advantage × 2^(-t / H)`

Here `H` is the estimated time for the advantage to halve. At `H/2`, about 71% remains; at `H`, 50% remains; at `2H`, 25% remains. **A half-life is not an expiry date.** Set renewal or migration triggers from customer requirements and forward economics. Advantage may plateau, grow, or change form instead of decaying exponentially.

Record creation or integration date, repeated gap observations, plausible causes, estimate range, review date, and action threshold. A review halfway through an estimated half-life is a scheduling choice, not evidence of obsolescence. If new observations disagree, update the estimate and explain why.

The earlier skill's month ranges for prompts, retrieval, fine-tuning, data, and orchestration were planning heuristics. They are preserved, with their limits, in [Evidence and planning assumptions](references/evidence-and-planning-assumptions.md). Do not use them as measured industry benchmarks or multiply them by a fixed “niche” factor.

### Read broad model progress without turning it into a product forecast

MIT FutureTech's July 2026 paper reports broad improvement across the studied text-based work tasks. Its task construction supplied the information needed for a self-contained response. That makes input gathering, coordination, and execution important local checks before applying the result to a workflow. The reported trend is conditional evidence about model performance; it does not determine your advantage's half-life, a shipping date, or staffing needs. See the linked evidence note for version, counts, quality thresholds, and projection limits.

Track broad incremental improvement **and** task-specific jumps. A narrow gain can be real; a broad gain can stall. Neither smooth model progress nor stepwise provider pricing is a universal law. Maintain separate observations for capability, price, and availability.

## 3. Run a capability comparison before committing

Review on a cadence proportionate to the dependency and rate of change. A quarterly review plus checks after material releases is a useful starting point, not a waiting period for an urgent deprecation.

1. **Choose a representative evaluation set.** Include frequent work, valuable edge cases, consequential failures, relevant customer segments, and current conditions. One hundred frequent queries can be an initial diagnostic; it is neither a sufficient sample for every risk nor a representative sample by definition. Separate a stable holdout from fresh cases, prevent leakage, and document any weighting.
2. **Run a controlled comparison.** Compare old and new models with the same task inputs and compatible prompts, tools, and settings to isolate the model change as far as practical. Record unavoidable differences. Run a separate comparison of reasonably optimized deployable configurations under comparable resource budgets when making the actual product choice.
3. **Measure outcomes.** Report the task-quality metric and uncertainty, improved and regressed cases, important failure classes, end-to-end P50/P95 latency under stated load, and full cost per attempted and successful outcome. Tokens alone are not cost; include prices, retries, tools, review, and operating work. Repeat stochastic cases where variation could change the decision.
4. **Inspect tradeoffs.** An average gain can conceal a consequential regression. Classify regressions by severity, prevalence, recoverability, and the requirements agreed before seeing results. A small acceptable tradeoff need not block every upgrade; a critical violation cannot be averaged away.
5. **Choose an action and a controlled rollout.** A clear improvement supports migration after compatibility and launch checks. A quality-cost tradeoff goes to `cost-model`; uncertainty may call for a targeted experiment. A wash can justify holding the current system. Set a decision deadline appropriate to the stakes, rather than an automatic 48-hour switch.

“Ten percent of cases improved” is different from “accuracy rose ten percentage points.” State both denominators when both measures are useful. Test before exposing users to a change, and retain a recovery path.

## 4. Make the build, buy, bridge, or wait decision

Compare forward costs and consequences over a stated horizon:

| Option | When it may fit | What must be explicit |
|---|---|---|
| Build | A valuable need is unmet and custom work has a credible advantage | Delivery risk, maintenance, payback, and the option to simplify later |
| Buy or adopt an available model capability | An accessible alternative meets the requirements | Integration, rights, operations, total cost, and dependence on the supplier |
| Bridge | The need matters now, but a smaller reversible solution preserves options | Scope, service limits, owner, and replacement or extension trigger |
| Wait | The cost of delay is acceptable and better evidence or availability is worth waiting for | Forecast evidence, review date, latest acceptable date, and failed-forecast fallback |
| Stop | The expected customer or organizational value does not justify pursuing this capability | Evidence, consequences, and what would reopen the decision |

Do not delay a critical unmet need solely because a model might deliver 80% of the solution next quarter. Conversely, current urgency does not automatically justify building a custom model. Consider a narrower product, manual support, a partner, or an existing service. An internal, preventive, or mandatory capability can have value without an external buyer waiting to pay.

Count the benefit lost while waiting and the integration and migration costs after the hoped-for release. Separate already-spent money from forward switching costs. A “free” native feature can still require paid access and substantial product work.

Use four diagnostic questions to sharpen the choice:

- **Velocity:** What changed on our task, by how much, and with what uncertainty? There is no universal 5% or 15% quarterly stop-investing rule. Even a small improvement can matter near a consequential threshold.
- **Dependency:** How would we operate if this capability or supplier became unavailable? Test recovery against the actual continuity requirement, rather than a universal one-week boundary.
- **Replication:** What would a credible competitor need to reproduce the useful result: time, data rights, expertise, distribution, integration, or trust? Copying cost is one part of defensibility, not its whole value.
- **Durability:** What remains valuable if everyone gets a better base model? Several complementary assets may matter; there is no need to choose only data, system, or model.

## 5. Track assumptions and retire work deliberately

A harness can contain temporary workarounds and enduring operating responsibilities. Keep the architecture reasoning in `harness-operating-model`; record its testable assumptions here.

| Component | Assumption to test | Decision after testing |
|---|---|---|
| Planner | Direct execution loses necessary task structure | Compare bounded direct execution and the planner before simplifying |
| Memory manager | Available context handling misses needed history or costs too much | Compare retrieval, summaries, and larger context on the actual history |
| Fact checker | Additional checking catches consequential errors | Test detection and false alarms; preserve required verification duties |
| Router | Explicit routing improves selection or respects access and cost constraints | Separate performance routing from permission enforcement |
| Fallback or cache | Recovery, latency, cost, or consistency needs the component | Test each purpose, including freshness and invalidation |

A better model does not establish deterministic output or remove access controls, audit duties, or required verification. Remove or narrow a component only after a controlled comparison establishes that its responsibilities are still met. Record the version tested, result, owner, rollout, and rollback.

During deprecation reviews, ask whether maintaining the custom capability still beats migration, what conditions changed, and how to preserve customer value through the transition. Simpler architecture can free capacity; do not assume every component is waste or that every upgrade warrants redesign.

## 6. Include workforce effects when they change the decision

Track which tasks AI performs, which people can judge the output, and how the next cohort will learn. A useful capability-debt check asks:

1. Which skills and practice opportunities has this workflow changed over the relevant period?
2. Who can perform or recover the essential work without the usual AI support, where that ability is required?
3. Who can evaluate it, and how will new people acquire that ability?

Choose the period and participants for the decision. A 36-month review or a meeting with HR, technology, and business leaders can help; neither is mandatory for a small product change. Waiting for a model does not itself stop apprenticeship if existing practice continues.

Distinguish the effect of assistance on today's output from retained learning and transfer to unfamiliar work. Expertise distance, learning effort, feedback quality, mentoring, and the changing composition of a role are useful lenses. They are not universal predictions that experts always benefit most, reduced effort always reduces learning, or automation fixes wage direction. Use `judgment-guard` for intervention design and [Workforce observation and learning](references/workforce-observation-and-learning.md) for the preserved practical structures.

Track the quality of warranted acceptance and rejection, including missed failures. A falling override rate alone could reflect a better model, appropriate trust, or missed errors. Do not classify a person or cohort from that rate alone.

## 7. Keep a small, actionable register

Use these tables as needed; one capability may fit in a short decision note.

**Product, scope, owner, last update, next review:** [details]

| Capability and task population | Requirement and measured baseline | Trend, evidence, and uncertainty | Availability or commoditization scenario | Decision, owner, and trigger |
|---|---|---|---|---|
| [Task and conditions] | [Metric, version, date, threshold] | [Observed change; forecast separately] | [Range or unknown] | [Action and reconsideration condition] |

| Advantage | Established and measured dates | Gap and comparison baseline | Decay assumption, if justified | Customer/economic action threshold | Renewal plan |
|---|---|---|---|---|---|
| [Useful advantage] | [Dates] | [Measure with units] | [Range, evidence, or unknown] | [Observable threshold] | [Owner and next test] |

| Harness component | Responsibility and assumption | Test version/date | Evidence and remaining uncertainty | Retain, narrow, or remove | Owner and recovery plan |
|---|---|---|---|---|---|
| [Component] | [Why it exists] | [Details] | [Result] | [Decision] | [Details] |

Add a brief decision log: date; what changed; recommendation; alternatives and tradeoff; assumptions and what would falsify them; next action and owner. Link relevant workforce observations without treating them as automatic employment decisions.

A monthly scan of task-specific evidence, relevant competitor announcements, support feedback, renewal blockers, and supplier notices is a useful starting rhythm. An announcement is a prompt to investigate, not an instruction to copy it. Lack of unprompted requests is not proof of no need. A small quality gap can still carry large value.

## Before finishing

- Is the recommendation tied to a real task and a stated requirement?
- Are measured findings separated from forecasts and illustrative heuristics?
- Were the credible alternatives tested, or is the absence of that test explicit?
- Do economics include delay, integration, maintenance, and migration?
- Are critical regressions and automation constraints addressed?
- Does waiting have a deadline and fallback, and building have a renewal trigger?
- Is the next action clear enough for its owner to carry out?

If capability improves faster than expected, recompare migration with continued ownership. If a forecast fails, use the planned bridge or revisit build, buy, scope, and timing. If technical success produces little value, return to the customer problem with `strategy-canvas` and `first-principles`. None of these situations has a universal two-week recovery deadline.

For a downstream skill, carry the recommendation, task definition, customer grounding, evidence, assumptions, costs, decision triggers, and unresolved questions into the shared handoff. A radar or trajectory chart is optional when it makes the decision easier to understand; it does not replace the evidence.
