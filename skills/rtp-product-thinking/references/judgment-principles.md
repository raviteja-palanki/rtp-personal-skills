# Product judgment principles

These lenses retain the original numbering for easy comparison. Choose the ones that affect the decision. Practitioner aphorisms are invitations to examine a situation, not empirical laws or permission to ignore constraints.

## 2.1 Opportunity cost alongside return

A positive return is not enough when another feasible choice would use the same resources better. Compare the value, cost, risk, and timing of credible alternatives, including preserving capacity or doing nothing. ROI can still be useful; opportunity cost complements it rather than making financial reasoning a junior-level mistake.

Ask what would be displaced and whether the decision remains attractive under the actual constraint. “If we could ship only one thing” can reveal priorities, but portfolios often need multiple complementary bets. Do not require proof that a choice is the unknowable absolute best before acting.

## 2.2 Impact, execution, and optics

| Level | Question | What to watch |
|---|---|---|
| Impact | What changed for users or the organization? | An asserted outcome without appropriate evidence |
| Execution | How well did we implement and operate the work? | Excellent delivery mistaken for proof of a valuable choice |
| Optics | How is the work understood by people who support or depend on it? | A favorable impression substituted for results |

Name the relevant level when a conversation crosses purposes. An executive asking about support experience may be asking about impact while the team explains delivery constraints. Good communication helps resolve that mismatch. Optics can make real work visible and secure resources; it need not be dishonest.

## 2.3 LNO: allocate care by consequence

| Class | Meaning | Working standard |
|---|---|---|
| Leverage | Additional care can materially improve the result | Invest attention where it changes quality, learning, or consequences |
| Neutral | Further polish has limited incremental value | Meet the useful standard and move on |
| Overhead | Necessary work with low additional benefit from polish | Complete it accurately and reliably with minimal waste |

The original 10×–100×, roughly 1×, and below-1× language is a teaching metaphor for different returns, not a measured classification formula. Likewise, “A+ versus B−” means calibrating polish, not accepting avoidable factual or operational errors.

The activity's name does not determine its class. Doshi's interview examples distinguish a routine bug report from a consequential one, and ordinary meeting notes from the precise record of a disputed executive decision. Either can deserve different effort. “Status update” and “PRD” therefore cannot be fixed Overhead or Neutral categories.

The diligent-martyr pattern is overinvesting in polish while important work lacks attention. Check whether that is actually happening before attributing long hours to perfectionism; workload or staffing may be the cause. Match demanding work to the person's productive conditions rather than assuming mornings suit everyone. Do not multitask on sensitive or accuracy-critical administration just because it is labeled Overhead.

## 2.3.1 Time horizon is a separate dimension

| Horizon | Illustrative scope | Example |
|---|---|---|
| Longer term | Often a year or more | Market entry, shared capabilities, long-term evaluation strategy |
| Medium term | Often one to three months | Roadmap sequencing, evaluation refresh, release-process improvement |
| Near term | Current week or immediate need | Incident response, regression diagnosis, a blocking decision |

These bands are illustrative and need not leave intermediate months unclassified. A task's audience or prestige does not set its horizon. A CEO update can concern today's incident; a current evaluation repair can protect a long-term capability. Horizon, leverage, urgency, and risk are different dimensions.

The original calendar examples are retained only as **illustrative allocations, not observations of PM types or optimal ratios**:

| Example allocation | Longer / medium / near term | Possible question |
|---|---|---|
| Mostly immediate work | 5% / 15% / 80% | Is necessary future work repeatedly displaced? |
| Mostly distant planning | 60% / 30% / 10% | Are plans becoming operational decisions? |
| Mixed planning and delivery | 20% / 50% / 30% | Does this balance fit the current product and obligations? |

Six practical ways to protect appropriate strategic work:

1. Reserve time that fits the workload; two two-hour blocks is an optional example, not an automatic calendar instruction.
2. Give operational triage a capable owner, clear escalation rules, and enough capacity. Delegation does not remove responsibility.
3. Set response timing by severity, user harm, scale, and reversibility. A cost change of 8% may or may not be urgent; a hallucination affecting a non-power-user can still be serious. Do not apply a blanket 24-hour delay.
4. Batch routine updates when useful, while communicating urgent or consequential decisions promptly. A 30-minute slot is a scheduling example.
5. Review what future-oriented work actually advanced and whether it was the right use of time. Some weeks legitimately belong to an incident or launch.
6. Separate designing an evaluation capability, scheduling its rollout, and handling today's failure. Each can have a different horizon and leverage.

## 2.4 Check the focusing illusion

A recently discussed problem can occupy more attention than its relative importance warrants. Compare it with the customer's other problems, current workaround, severity, frequency, and actual consequences. Asking where it ranks among their priorities can help; a top-five list is not a universal demand or a substitute for observation.

A problem ranked fourth may still cause churn or harm. A single consequential defect may need action before ranking research is complete. Ask whether the response is proportional to the evidence, not whether the team can dismiss the complaint for a month.

## 2.5 Compare alternatives without discarding the baseline

An opportunity solution tree connects **outcome → opportunities → solutions → assumption tests**. Considering genuinely different solutions can reduce attachment to the first idea. Three candidate approaches is a useful discovery exercise when appropriate, not a requirement for three live experiments.

Compare the relevant assumptions using suitable evidence. Keep the existing solution or control where it helps establish incremental benefit. An A/B test against the current experience is legitimate. If no candidate is clearly better, the result may reflect weak options, insufficient evidence, or a small difference—not necessarily lack of understanding. See [Teresa Torres on assumption testing](https://www.producttalk.org/assumption-testing/).

## 2.6 Adoption, satisfaction, and value

Look at whether people begin using the product, whether it serves them well enough to continue, and whether its value is sustainable for the organization. Define measures suitable to the product and stage. A public-service outcome, accessibility improvement, compliance obligation, or foundational investment can create value without direct feature-level revenue.

The useful warning behind the original “charity work” label is a missing value-and-cost explanation. Do not demean social-purpose work or demand immediate monetization from every feature. Ask who benefits, how the benefit matters to the mission or business, and what sustains delivery.

## 2.7 Simulate before a consequential commitment

Rehearse plausible user, stakeholder, and operational responses before a launch or difficult meeting. Consider low adoption, high adoption with unsustainable support, an unexpected objection, or a failure of the central assumption. Decide what evidence or contingency is worth preparing.

A scenario is a hypothesis, not a prediction of someone's mind. Surprise may reveal missing information rather than a broken character model. A kill condition can be a responsible experiment boundary; its existence does not mean the product should never be launched. For high-consequence actions, complement mental rehearsal with real evidence and appropriate controls.

## 2.8 Separate thinking, execution, and external conditions

When investigating failure, examine the problem choice, assumptions, prioritization, design, implementation, coordination, and external changes. Resource shortages or market timing can reflect a prior decision, an unforeseeable shock, or both. Do not relabel every outcome as a thinking failure.

Decision quality concerns the information and choices available at the time; outcome quality also reflects uncertainty and luck. Identify the controllable improvement without implying the team could have guaranteed success. A retrospective should learn, not merely redistribute blame.

## 2.9 Exercise feedback discernment

Feedback is evidence of a person's experience or concern, not an instruction to implement their proposed solution. Examine segment, context, severity, recurrence, incentives, and source credibility. A non-target user can reveal a critical accessibility or security problem; a repeated target-user request can still point to the wrong remedy.

Record a reason when setting aside consequential feedback. Seek disconfirming examples and missing voices. Do not interpret discernment as discarding most input by default.

## 2.10 Develop taste, then test it

Taste is a reasoned ability to anticipate quality before complete outcome data is available. Explain what makes an interaction, document, or decision good or poor: clarity, coherence, suitability, unnecessary effort, or a failure mode. Compare stronger examples and inspect their underlying choices.

Evidence helps calibrate taste; waiting for a useful test is not proof of incompetence. Observation, critique, deliberate practice, and building can all contribute to learning. AI assistance can support these activities without making the user passive. The relevant question is whether the person can interrogate and improve the result.

## 2.11 Strategy needs insight and coherent choices

A strategy explains a valuable opportunity, why the organization can serve it, which choices reinforce one another, and what it will decline or defer. Insight and creativity can distinguish it from a task list. A competitor need not find the strategy strange for it to be sound.

Optimization, new insight, and creative solutions may all create advantage. Do not assert that AI can only optimize or cannot generate a useful novel idea. Evaluate the actual contribution and retain responsibility for verification, coherence, resource allocation, and commitment. Ask what must be true and how competitor response affects the bet.

## 2.12 Match emphasis to Explore, Expand, and Extract

| Stage | Primary emphasis | Useful evidence | Typical mismatch |
|---|---|---|---|
| Explore | Learn whether a problem and approach deserve commitment | Customer behavior, assumptions, prototypes, early retention and bounded economics | Treating uncertain forecasts as precise commitments |
| Expand | Remove constraints on valuable growth | Adoption, retention, capacity, quality, and unit economics | Scaling faster than reliability or support can sustain |
| Extract | Sustain and improve an established source of value | Margin, customer outcomes, reliability, renewal, and opportunity cost | Optimizing the current system while ignoring replacement threats |

One company can operate products in different stages. Mature products can need new discovery, and exploratory work still needs a responsible budget and controls. Use the detailed stage table to choose methods rather than imposing categorical permissions or prohibitions.

## 2.13 Delegate with clear ownership and review

| Situation | Useful approach |
|---|---|
| Another person can own a lower-leverage task | Agree on the result, constraints, and a light check appropriate to the risk |
| Another person owns a high-leverage or complex task | Define authority, review points, and where closer involvement adds value |
| Only you can do the work today | Calibrate effort; consider whether teaching or changing the dependency is worthwhile |

Neither complete neglect nor universal micromanagement follows from LNO. Explain why closer involvement is needed, what it covers, and when it will reduce. Doshi's micromanagement essay distinguishes mistrust, insecurity, complexity, and taste; use that vocabulary to inspect the reason for involvement, not to certify a manager's self-assessment. Keep delegation within the user's requested mode and host rules.

## 2.14 Separate estimates, targets, and commitments

An estimate expresses an uncertain forecast under stated assumptions. A target is a desired outcome or date; a commitment adds agreed responsibility and consequences. Estimates are not always wrong, and commitments should not conceal uncertainty.

Different internal targets and external commitments can be useful when transparent and consistently understood. Show the basis, dependencies, range, or buffer rather than creating conflicting stories. Review material changes promptly. An aggressive target should not silently become a promise or an excuse for avoidable pressure.

## 2.15 Make difficult conversations clearer

Preparing words can reduce avoidable ambiguity and help address tension respectfully. It cannot resolve every conflict in incentives, authority, resources, or conduct.

For example: “I have noticed friction in our recent discussions. I may be missing something. How are you seeing it?” Ask for advice when you sincerely want it; it is not a technique that forces someone from judging into helping. Check what is unsaid without assuming the other person distrusts your competence.

## 2.16 Attend to task and relationship purposes

The **Capital P** purpose is the practical outcome, such as deciding a launch date. The **lowercase p** purpose is how the interaction affects respect, trust, and future cooperation. Consider both without manipulating emotions or hiding the substantive disagreement.

An unwelcome but necessary decision can strain a relationship without being the wrong decision. Aim for an honest, respectful process rather than approval at any cost.

## 2.17 Use cognitive empathy as a hypothesis

Consider another person's responsibilities, evidence, incentives, and constraints. Translate the proposal into consequences relevant to them while preserving its actual risks and costs. Legal's objection may identify a real defect rather than a fear to be talked away.

Prepare possible reactions and ask to confirm them. A surprising objection updates the model; it does not prove the person is irrational or your entire understanding is broken. Communication is one part of influence alongside authority, incentives, and resources.

## 2.18 Manage up and escalate usefully

Give leadership enough context to make decisions and fulfill its responsibilities. Escalate when the needed authority, trade-off, or resource lies beyond your scope. State the problem, evidence, options, recommendation, and decision needed.

Solving a problem independently can be good judgment; hiding a material problem to appear capable is different. Timely escalation and agency reinforce each other. Avoid flooding leaders with every detail or absorbing a structural problem indefinitely.

## Source and evidence notes

The skill's influences include Shreyas Doshi, Marty Cagan, Teresa Torres, and Kapil Gupta. Not every inherited sentence is attributable to a particular author, and the original skill supplied no traceable source for some numeric allocations and psychological absolutes. Those are now qualified or replaced with decision guidance.

For this revision, the full extracted text of three local primary essays was read: Doshi's [Understanding Micromanagement](https://shreyasdoshi.substack.com/p/understanding-micromanagement), December 1, 2025; [Don't be a full cup](https://shreyasdoshi.substack.com/p/dont-be-a-full-cup), December 12, 2025; and [Becoming great at listening](https://shreyasdoshi.substack.com/p/becoming-great-at-listening), December 4, 2025. The local PDF captures are under `3_Research/04_ai-pm-os/ai-pm-essays/`; their January 2026 capture dates are not the publication dates. Extracted text has some clipped line endings; no new direct quotations or claims about the uninspected embedded audio are made here.

Relevant LNO and agency passages were also read in `3_Research/04_ai-pm-os/podcast-transcripts/Shreyas Doshi.txt`. They explicitly show that the same activity can have different leverage. The full podcast transcript was not reread for this edit.

[Cagan's value-and-viability discussion](https://www.svpg.com/value-and-viability/) supports the product manager's role alongside design and engineering. [Torres's assumption-testing guidance](https://www.producttalk.org/assumption-testing/) supports comparing alternatives through their assumptions. [Rob Fitzpatrick's official Mom Test page](https://www.momtestbook.com/) identifies its purpose as learning from customer conversations; the original question bank incorrectly used “Mom Test” as a synonym for a non-user understanding the product.

Relevant Novel Insights entries were reviewed for the distinction between practice, interrogation, authority, and appearances. Their hypotheses do not establish that every judgment skill requires unaided production or that every apparent alignment reflects a real commitment.
