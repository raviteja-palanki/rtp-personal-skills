---
name: rtp-moat-finder
version: v2.15.1_latest
description: 'Assess whether an AI product creates valuable advantages that competitors cannot readily copy, replace, or bypass. Start with the customer problem, value economics, and a credible competitive alternative. Evaluate five mechanisms: useful proprietary data, workflow integration, harness mastery, trust and reliability, and network effects. Then examine distribution, model dependence, learning-loop ownership, portability, and the scarce resources that affect value capture. Produce an evidence-based scorecard, scenarios, open questions, and the next investment or test. Scores are discussion aids, not survival predictions; no fixed number of moats guarantees defensibility. Use for strategy, quarterly reviews, acquisition assessments, or a board narrative. Pairs with strategy-canvas, build-or-buy, safety-as-moat, feedback-flywheel, capability-tracking, and competitive-map. Triggers include defensibility, moat, competitive advantage, and copycat risk.'
imports: [bias-spotter, determinism-compass]
---

# Moat Finder

**Identify what makes the product valuable, what prevents a credible rival from matching or bypassing that value, and whether the business can retain a worthwhile share of it.** A moat is a durable competitive mechanism, not simply an impressive feature or the absence of competitors.

For an application buying broadly available model capability, access to that model alone rarely explains a lasting advantage. Look closely at the system around it: information, operating knowledge, workflow, reliability, and distribution. Keep the claim conditional. Model development, specialized weights, technical efficiency, and exclusive access can themselves contribute to an advantage when evidence supports it.

## Start with the problem and choose the depth

Use the context already supplied. Establish the customer, problem, product boundary, competitive alternative, economic objective, and decision horizon before scoring. Record when the problem frame was last challenged and what has changed. A twelve-month-old frame is a reason to inspect relevance, not an automatic expiry rule. Use `first-principles` when a rival could solve a different version of the problem and avoid your supposed moat entirely.

- **Full assessment:** for a new strategy, acquisition, consequential investment, or board narrative, examine the mechanisms, economics, scenarios, and evidence gaps.
- **Quarterly update:** review the prior assumptions, changed competitor capabilities, useful outcomes, and the most consequential uncertainty. Do not repeat unchanged research for appearance's sake.
- **Provisional assessment:** when time or access is limited, use the output template directly. Mark unsupported claims `OPEN`, distinguish absence of evidence from evidence of absence, and identify the test that would resolve the decision. The [Cursor example](references/moat-assessment-cursor.md) shows this approach without presenting an old public-information snapshot as a current company assessment.

Answer two questions early:

1. **Why would a credible competitor with access to similar models struggle to match or replace this value?** Name the barrier and evidence, not just a feature label.
2. **Who would miss this product if it disappeared, and what would they lose?** Separate useful capability, convenience, habit, access, trust, and migration effort. Being missed supports customer value; it does not by itself establish defensibility.

Before product-market fit, use the analysis to test strategic assumptions without delaying useful customer learning. Internal or single-customer tools may need a lighter analysis of operating advantage, supplier dependence, and continuity; a market-moat narrative may be unnecessary.

## 1. Check the value worth defending

Identify what the capability changes: growth, cost, retention, risk, service quality, or capacity. Several can matter together. Compare incremental benefit with delivery, maintenance, transition, and opportunity costs. Use `cost-model` and `token-economics` for the economic detail.

Cost savings are bounded by the relevant costs, but their effect on profit or firm value is not universally small. Illustratively, revenue of 100 and costs of 90 leave profit of 10. Reducing those costs by 5% saves 4.5 and raises profit to 14.5—a 45% increase before other effects. This is arithmetic, not a valuation forecast. Growth also needs investment and can destroy value if its unit economics or persistence are poor. Do not apply a universal valuation multiple to either path.

Then ask **who can capture the benefit as AI becomes cheaper or more capable**. Examine complementary resources such as capital, distribution, customer access, skilled people, regulatory permission, organizational execution, useful data, and trust. Check whether they are scarce, substitutable, obtainable, and controlled by you or someone else.

Lower input costs can improve your margin, reduce prices for buyers, reward another supplier, or be consumed by additional work. Market structure and customer value matter. An exclusive dataset can support relative performance and margin in some conditions; neither margin retention nor margin loss follows automatically from exclusivity.

## 2. Evaluate five mechanisms without double-counting them

For each claim, record the customer benefit, causal mechanism, comparison, ownership or access, replication path, operating evidence, and likely failure condition. Distinguish current advantage from potential advantage.

| Mechanism | What to examine | Evidence that strengthens the claim |
|---|---|---|
| **1. Useful proprietary data** | Distinctive information plus the rights, quality, and ability to use it | A relevant improvement over credible alternatives; costly or constrained substitution; continued usefulness |
| **2. Workflow integration** | Useful connections to processes, systems, history, and customer habits | Demonstrated value in the workflow and a realistic migration comparison, including exported data and standards |
| **3. Harness mastery** | The tools, context, memory, permissions, evaluations, routing, budgets, recovery, and operating practices around the model | Better outcomes or economics than a simpler or accessible baseline under comparable conditions |
| **4. Trust and reliability** | A record of meeting the promises that matter to this buyer | Relevant operating performance, effective recovery, and evidence that those qualities affect choice, retention, or willingness to pay |
| **5. Network effects** | Additional participants make the product more valuable to other participants | A measured cross-participant benefit that persists after accounting for other changes and can be sustained as the network grows |

An evaluation corpus may support both data and harness quality. Describe the shared mechanism rather than counting it twice as two independent barriers. Likewise, workflow reliability can influence trust without creating a wholly separate source of defensibility.

### Data: test usefulness, accessibility, and renewal

Inspect more than volume:

- **Coverage:** does the data represent the work, including costly exceptions? Rare cases can matter greatly; common cases can also be commercially valuable.
- **Liquidity:** can the data be found, understood, joined, validated, and used under appropriate rights?
- **Vintage:** what does its historical span reveal that current or substitute data cannot? Age can help or hurt.
- **Incremental value:** does removing or replacing the data change an outcome that matters?
- **Race window:** can the organization put it to useful work before a rival closes the gap? Resolve the relevant workflow obstacles; not every use needs an agent or a wholesale redesign first.

A static **stock** and a refreshed **flow** can both have value. An archive may retain historical coverage, repeated-use value, or licensing rights. A flow can support current relevance but may be expensive or easy to substitute. Do not infer that models always degrade without fresh material, or that only flows earn recurring revenue.

Check the rights and relationships sustaining new inputs. Compensation, consent, licensing, voluntary contribution, and operational collection differ by setting. A data flow is not defined by payment alone. Where access depends on contributors or rights holders, evaluate whether the arrangement supports continued participation and appropriate use.

### Workflow: earn the customer's preference

Measure what migration would actually require: export, integration, validation, retraining, interruption, and re-establishing useful context. The earlier “Indispensability Index” is best treated as this documented migration burden, not a validated index with a universal number of quarters.

Habit can matter even when files are portable. Switching costs are stronger evidence when accompanied by continuing customer value. Avoid confusing avoidable obstruction with a good product. Standards may lower one migration cost while leaving others intact.

### Harness: compare the complete operating system

Use the same model where practical to isolate the contribution of context, tools, evaluation, and orchestration. Also compare the best realistic alternative available to the customer. A sophisticated architecture is not evidence of a moat until it improves useful outcomes and a rival faces a meaningful barrier to reproducing them.

Keep domain evaluations and failure knowledge current. Improvements in a model may absorb a workaround while leaving access controls, accountability, customer context, and recovery duties. Route architecture decisions to `harness-operating-model` and timing to `capability-tracking`.

### Trust: test the promise and the response to failure

Assess reliability in the conditions customers face, including rare consequential failures and recovery. A certification, privacy statement, or safety page supports only its actual scope; it is not interchangeable with evidence that customers choose you for reliability. SOC 2, HIPAA-related obligations, and FedRAMP are different kinds of assurance or requirements, not one generic certification.

Trust is not binary. An incident's severity, handling, relevance, prior history, and customer response affect the damage and possible recovery. New products can establish scoped credibility through appropriate evidence and trusted partners; years in market are not the only route.

When extending a trusted product, identify the promise customers expect to transfer and test it in the new use case. Preserve the underlying quality commitment while adapting evaluation and oversight to the new task. The Porsche case illustrates this question; it does not require identical evaluation metrics or human review for every AI product extension.

### Network effects: establish the cross-user benefit

Use four questions as evidence prompts, not a two-failures scoring rule:

1. Does another participant improve an existing participant's experience, directly or through a validated learning or matching mechanism?
2. Would switching lose that network value even if the alternative had attractive features?
3. Could a smaller or differently constructed dataset deliver comparable results? Compare credible substitutes rather than an automatic one-tenth-data test.
4. Does the benefit appear in quality, retention, utility, pricing power, or another relevant outcome?

A network effect need not operate within weeks, require a price premium, or depend on a two-sided marketplace. More users can also create congestion or poor-quality data. Single-customer personalization alone is a learning or switching advantage, not necessarily a cross-customer network effect; collaboration within that customer's network may still create one.

## 3. Understand how the advantages develop

**Vertical-Infinite: focus before expansion when it fits.** Deep domain work can create relevant data, integrations, and credibility that support adjacent expansion. A horizontal strategy can also succeed. Compare customer demand, distribution, reuse, and execution rather than assuming vertical products always win or earn a fixed percentage advantage.

**Living Software and Workspace DNA: learn at three levels.** Micro observations describe individual traces, such as acceptance, correction, or escalation. Meso observations identify workflow patterns. Macro observations capture organization-level context, terminology, and recurring exceptions. Route this work through `feedback-flywheel`: signals are candidates for learning, not automatic truth or permission to train. A customer's history may be valuable without being impossible to export or recreate.

**Cycle time: shorten validated learning.** Use the loop: identify a weakness, form a hypothesis, test safely, evaluate quality and cost, then release within agreed authority and monitor. Fast iterations compound only when changes are useful and retained. Many commits, more experiments, or autonomous operation do not by themselves establish a faster rate of customer-value improvement. Define what can ship automatically and what needs review.

**Process knowledge: include the people and practice.** Useful expertise can be tacit, distributed, difficult to articulate, or dependent on tools. Identify the routines and transfer routes: practice, observation, mentoring, working examples, documentation, hiring, and collaboration. Observation hours are an input, not proof of competence. Measure successful transfer or performance on relevant work. Talent and process can contribute to a moat even when individuals may leave; assess retention, redundancy, and organizational learning instead of dismissing “people” categorically.

## 4. Find where the learning loop closes

Map each step from interaction to stored signal, interpretation, validated improvement, and deployment. Who can access it, who may reuse it, and who receives the resulting benefit? A customer and supplier can both benefit; ownership is not always an either/or outcome.

Distinguish three potential provider-reuse channels:

| Channel | What to verify | Proportionate response |
|---|---|---|
| Voluntary feedback | What the actual service and agreement classify as feedback and permit it to be used for | Appropriate settings, user guidance, negotiated terms, or a different route if needed |
| Synthetic reuse | Whether outputs may be reused under the applicable agreement and data settings | Check obligations on the interaction; do not assume provider-generated output is unrestricted |
| Broader capability learning | Whether there is evidence of the proposed learning from this customer's work | Treat it as a hypothesis unless demonstrated; test the data path and practical alternatives |

The supplied September 2026 article motivates these questions but does not prove ordinary enterprise usage inevitably trains the general product. A sandbox calling an external API differs from isolated local processing. Private deployment or modularization may address a specific risk; neither is an automatic requirement or a guarantee. Use `build-or-buy` for current product, contract, and architecture choices. [Evidence and historical claims](references/evidence-and-historical-claims.md) records the primary terms check and its limits.

## 5. Stress-test the defensibility story

Use these checks where they could change the assessment:

**A public-input loop.** Public information can improve a product; identical inputs do not force identical results. Test whether your transformation, objective, execution, or customer context produces useful differentiation. Unchecked reuse of generated outputs can create degradation, but public data, synthetic data, and recursive training are different things. Multi-model diversity may reduce some correlated errors without proving sector-level independence.

**An agent between you and the buyer.** Separate discovery, recommendation, transaction, and service. Assistants do not have perfect recall or necessarily ignore brand preferences. Investigate which information they can access and which customer constraints they follow. Use `marketing-to-ai-agents`; owning the assistant, controlling data, or building trust are possible responses, not an exhaustive list of defenses.

**Portability and supplier dependence.** Test export and reconstruction of histories, prompts, rules, evaluations, and integrations. Price switching time and the ability to maintain essential work. Retaining expertise can help, alongside alternative suppliers, managed services, contracts, and recovery plans. Do not assume supplier leverage peaks at a fixed renewal.

**Portability versus exclusivity.** Being able to move your own data does not give a rival the right or ability to obtain it. Assess authorized portability and unauthorized access separately. A pre-AI corpus may reveal a valuable operating habit; a deliberately constructed AI dataset can also be distinctive. Neither origin establishes quality by itself.

**Universality versus exclusivity.** Publicly understandable product data helps potential buyers and assistants assess fit. Restricted information may create a separate performance advantage. Score accessible representation and exclusive capability separately; neither guarantees inclusion or margin, and public data can create valuable sales or service outcomes.

**Corpus versus weights.** State what is owned: source data, a retrieval corpus, annotations, model weights, or a combination. Retrieval and fine-tuning can coexist. Both require evaluation and maintenance; both can become stale; either can support a logged model identity. Custom weights can constrain switching without making fallback impossible. `build-or-buy` compares the task-specific quality, rights, cost, and latency tradeoffs.

**Acquisition and transfer.** Ask what a transaction actually transfers: rights, people, relationships, routines, distribution, and usable assets. Test retention and integration rather than assuming a purchase creates the operating system around the asset. An acquirable scarce resource can still be a moat if rivals cannot obtain an equivalent on comparable terms. A study finding no reliable average growth effect does not show that no acquisition can produce innovation.

**Disclosure timing.** Before revealing a distinctive technique, ask whether rivals are independently close, whether disclosure reveals how it works or merely that it works, and whether those answers change the decision. Balance imitation risk with adoption, recruitment, partnerships, and resources. The speedskating case distinguishes copying a visible concept from executing it well; it does not supply a universal delay period.

## 6. Assess distribution and the type of business

Treat distribution as an explicit force outside the five-mechanism scorecard. Check owned or default surfaces, useful developer ecosystems, partner access, and whether a supplier also competes downstream. Access may tighten or improve; use the actual trajectory and alternatives. Multi-model neutrality is a possible hedge whose value must be demonstrated.

Brand presence in model responses can create exposure, but it is not equivalent to attributable traffic or conversion. Open-sourcing a harness can trade some exclusivity for adoption, contributors, and ecosystem reach. Evaluate the licensing, differentiation retained, and route to useful outcomes; openness alone does not create a network effect.

The supplied Shay/Davenport taxonomy is a useful starting lens:

| Type | Typical emphasis to investigate |
|---|---|
| Originators: commercial foundation-model builders | Technical capability, efficiency, capital, talent, access, and distribution |
| Explorers: research-led developers | Research progress, credible milestones, and a path to useful application where relevant |
| Infrastructure builders | Performance, cost, ecosystem adoption, integration, and switching alternatives |
| Enhancers: applications using foundation models | Domain performance, data, engineering, workflow, UX, and customer access |
| Optimizers: organizations using AI internally | Operating advantage, service quality, and the ability to sustain it |
| Experimenters: organizations still testing | What is being learned, why commitment is limited, and the evidence needed for the next decision |

These categories can overlap or change. They do not rank survival rates, establish a five-to-ten-year research horizon, or prove that more pilots are always the wrong next step. Compare businesses with relevant economics and customer needs rather than using category membership as the answer.

## 7. Score the evidence and choose the next move

Use a 1–5 score only when it helps discussion. Suggested anchors are: **1 absent or no demonstrated mechanism; 2 plausible but weakly evidenced; 3 demonstrated useful advantage with a credible imitation barrier; 4 sustained advantage with strong evidence of that barrier; 5 sustained, compounding advantage whose barrier is demonstrably strengthening.** Mark unknown separately. Record evidence and uncertainty beside the score.

Harness and trust claims need appropriate operating evidence before earning 4 or 5; a demo or intention is insufficient. Match the test to the mechanism rather than demanding the same baseline for every form of trust. Do not turn ordinal scores into precise survival probabilities. A total out of 25 is optional and descriptive; overlapping mechanisms limit its meaning. One powerful barrier can matter more than several weak ones. The earlier 12-point and three-moat thresholds are not validated decision gates.

Estimate duration using scenarios and observed competitor progress. Eighteen months is a possible planning horizon, not a survival wall. Link material model assumptions to `capability-tracking`. Choose the next investment by expected impact, feasibility, and opportunity cost; the lowest score is not automatically the best place to spend.

For board audiences, map to Helmer's Seven Powers without forcing a one-to-one equivalence:

| Power | Relevant mechanism or question |
|---|---|
| Scale economies | Does your scale improve useful unit economics, after complexity costs? |
| Network economies | How does participation benefit other participants? |
| Switching costs | What useful value and real transition effort would a customer leave behind? |
| Counter-positioning | Would matching the business model materially harm an incumbent's existing business? |
| Branding | Does reputation affect choice, utility, or willingness to pay? |
| Cornered resource | What valuable resource is available to you on terms rivals cannot readily match? |
| Process power | Which embedded practices create an advantage that rivals struggle to reproduce? |

Mark Strong, Emerging, Absent, or Unknown with the supporting mechanism. A power may sit partly outside the five categories, especially scale or distribution; do not downgrade it simply because the mapping is imperfect.

## Deliver a decision someone can act on

Use this structure at the needed depth:

**Product, customer, problem, owner, date, horizon:** [context]

**Recommendation:** [what to defend, build, test, acquire, partner on, or stop claiming]

**Value engine and economics:** [benefit, costs, capture mechanism, alternatives]

**Two opening tests:** [why matching is difficult; who would miss the product and why]

| Mechanism | Score or unknown | Evidence and comparison | Replication or bypass path | Next test or action |
|---|---|---|---|---|
| Proprietary data | | | | |
| Workflow integration | | | | |
| Harness mastery | | | | |
| Trust and reliability | | | | |
| Network effects | | | | |

Add distribution; model dependence; Micro/Meso/Macro learning; loop ownership; relevant stress-test findings; favorable, central, and adverse scenarios; and `OPEN: [question] — [evidence needed]`. Use numerical probabilities only when their basis is defensible.

Close with the next investment or test, its owner, expected outcome, opportunity cost, main risk, and reconsideration trigger. Pass the evidence-backed position to `strategy-canvas` and `ai-portfolio-management`, trust actions to `safety-as-moat`, learning mechanics to `feedback-flywheel`, and the concise narrative to `vision-setting` when needed. An optional chart should show uncertainty and avoid making a large polygon look like proof.

Before finishing, confirm that the customer value is real, evidence supports the mechanisms rather than just company prestige, duplicated claims are not counted as independent barriers, and the recommendation remains useful if a major forecast is wrong. A moat argument should improve product choices, not excuse poor execution or unmet customer needs.
