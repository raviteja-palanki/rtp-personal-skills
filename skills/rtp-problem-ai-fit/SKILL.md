---
name: problem-ai-fit
version: v1.3.1_latest
description: 'Decide whether AI offers enough value over rules, search, ordinary software, or a human workflow for a specific problem. Decompose the task, compare credible baselines, examine evidence and error consequences, and assess total cost and opportunity cost. If AI helps, distinguish producing a bounded recommendation from assisting a wider decision; neither grants automatic action authority. Use during discovery, when someone proposes an AI feature, or when new evidence challenges an existing approach. Produce a clear recommendation, testable hypothesis, critical assumptions, and next action. Treat fit scores as optional discussion aids, never safety or build approvals. Pairs with first-principles, determinism-compass, ai-use-case-readiness, invisible-stack, build-or-buy, and cost-model.'
imports: [first-principles]
---

# Problem–AI Fit

Choose the approach that best serves the task at an acceptable cost and consequence. Compare AI with credible alternatives rather than treating either AI or rules as the predetermined answer. A technically suitable approach still has to earn its place among competing uses of time and resources.

The recommendation may be **AI**, **rules or ordinary software**, **hybrid**, **human-led work**, **do not build**, or **gather specific evidence first**. State the reason and the condition that would change it.

## Start with the real decision

Use this skill when proposing a feature, testing an AI assumption, or reconsidering an approach after material evidence changes. For a settled implementation detail, a focused check may be enough. For an unresolved model, retrieval, or orchestration choice, use `rtp-invisible-stack` alongside the fit decision.

Reuse the context already available. Follow the Universal Skill Protocol at the source library root or packaged plugin root, choosing depth and format for the request. A concise assessment can be inline; a substantial shared decision may merit a document or presentation. Do not require a format-selection conversation or multiple visuals before answering a narrow question.

### Ground the customer and the opportunity

Establish six things, distinguishing facts from assumptions:

1. **Who has the problem?** Name the task and relevant circumstances, user, buyer, and affected people without narrowing the segment arbitrarily.
2. **What outcome matters?** Use the customer’s language where available. A technology preference is not the outcome.
3. **What happens today?** Include manual work, existing software, workarounds, and doing nothing.
4. **How important is the problem?** Examine frequency, consequence, competing priorities, and the cost of action and inaction. A fourth-ranked problem can still matter; a top-three rank is not a universal adoption gate.
5. **What evidence supports demand or value?** Purchases, workarounds, observed use, and interviews inform different claims. Spent effort does not automatically prove willingness to buy the proposed product.
6. **What does this investment displace?** Name the alternative use of capacity and the opportunity cost.

Ask only for missing information that changes the next decision. Where evidence is incomplete, proceed with a clearly scoped hypothesis or research plan instead of inventing a customer or blocking all useful analysis.

## 1. Find the actual bottleneck and decompose the task

Ask whether the delay or failure primarily involves information, capability or judgment, organizational incentives, workflow, or a combination. The remedy should address that mechanism.

| Bottleneck | What AI might contribute | What still needs attention |
|---|---|---|
| Information volume or format | Search, extraction, classification, synthesis, or comparison | Source quality, coverage, prioritization, and whether the result supports action |
| Judgment under uncertainty | Evidence, scenarios, predictions, alternatives, or decision support | Relevant expertise, valid objectives, uncertainty, and accountable choice |
| Incentives or organizational conflict | Make evidence, consequences, and alternatives easier to inspect | Authority, rewards, resources, and a real resolution of the conflict |

A model upgrade alone does not settle competing interests. A tool can still contribute to an intervention that changes information or incentives. Avoid the opposite absolutes that AI always dissolves information problems or can never help a judgment or incentive problem.

Use `rtp-first-principles` to decompose the feature into its important operations: lookup, transform, classify, generate, and any decision or action they support. A feature can contain several operations. Classifying the whole feature by one verb can conceal the part where AI is useful or risky.

Examples:

- A scheduler may use ordinary calendar and constraint logic, with language understanding to interpret an unusual request.
- Invoice processing may combine fixed-format extraction, image recognition, field validation, and exception handling.
- A support workflow may use rules for some routing, a model for ambiguous text, and a person for consequential cases.

Structured output, a binary label, or a finite set of categories does not establish that the input-to-output mapping is easy to encode. Conversely, unstructured input does not automatically justify a model.

## 2. Compare a simple baseline with the proposed AI

Ask what a lookup table, rules, search, an existing product, or a revised manual workflow can achieve on representative cases. A spreadsheet or an afternoon with a domain expert can help propose a baseline; it does not prove completeness or correctness.

Measure the baseline’s quality, coverage, error consequences, maintenance, and total task cost. Then identify what the AI approach would improve and what it might make worse. If rules cover most cases, examine the remaining cases by consequence and value rather than assuming an 80/20 split justifies either approach.

Rules have compute, integration, maintenance, and failure costs even without a model inference fee. Deterministic behavior means repeatability under defined conditions, not correct data or correct policy. Likewise, AI can be appropriate without introducing a large custom training platform. Compare the actual architectures under consideration.

Keep the comparison fair: same task, population, outcome criteria, relevant exposure, and operating conditions. A rules baseline can reveal that AI adds little; an existing model can reveal that maintaining rules adds unnecessary effort. Prefer evidence over a fixed cost multiplier.

## 3. Run the four-question AI-Necessity Test

Use the four questions as a decision record. Answer **supported**, **unsupported**, or **uncertain**, with evidence and next steps. The name is historical: the test assesses comparative value and feasibility, not whether only AI could ever perform the task.

| Question | What to establish | If the answer is weak or uncertain |
|---|---|---|
| **1. What useful capability does AI add?** | Does it improve a relevant operation or user outcome beyond a credible baseline? | Test or strengthen the baseline; keep non-AI options open |
| **2. Can this approach perform the task, and can we assess it?** | Suitable model capability, data and reuse rights, representative evidence, and a credible evaluation path | Run a capability/evaluation study, narrow the task, or choose another approach |
| **3. Are the consequences acceptable under actual controls?** | Important failures, exposure, detection, authority, prevention, fallback, and recovery | Reduce exposure or redesign controls; do not proceed into unsupported consequential action |
| **4. Does the value justify the full cost at this scope?** | Development, operation, review, support, maintenance, benefit, and opportunity cost | Reduce scope, buy or reuse capability, keep a manual path, or defer |

“Requires judgment” is not a prerequisite for ML: recognition and classification can benefit even when the desired output is precisely defined. Nor does human agreement on one hundred examples establish model learnability. Training data needs depend on whether the approach trains from scratch, adapts a model, retrieves evidence, or uses existing capability; all still need evaluation appropriate to the decision.

A high-volume low-value task can be a poor fit, while a low-volume high-value task can justify assistance. Human review is a control only if the reviewer can detect the relevant error and has time and authority to act. No count of favorable answers offsets an unresolved serious failure or lack of permission.

If a legacy workflow requests a score out of four, report the count with the individual answers and limitations. It is a checklist count, not a validated fit grade or automatic build decision. Use the [optional expanded profile](references/assessment-profile-and-examples.md) when it helps expose an uncertain dimension; it must not override the four questions.

## 4. Decide which role AI should play

Separate **making a recommendation** from **being authorized to act on it**. “Engine” and “helper” describe a role in analysis, not an autonomy level.

- **Bounded recommendation engine:** AI produces a prediction, ranking, or other defined recommendation within a tested task. People or explicit governance set objectives, constraints, evaluation, and authorized use. Classical ML, optimization, statistical methods, generative models, or hybrids may fit different components.
- **Helper for a wider decision:** AI assembles evidence, compares alternatives, surfaces assumptions, or explores scenarios while accountable people resolve the competing objectives and commitments. A generated synthesis can influence that judgment substantially, so inspect its selection and framing too.

Use six questions to understand the decision’s shape:

1. Is the objective sufficiently clear and observable?
2. Are relevant data accessible, reliable, and suitable for reuse?
3. Are the relationships stable enough for the intended decision horizon?
4. Can important boundaries and exceptions be defined and enforced?
5. Can outcomes and important errors be assessed on a useful timescale?
6. What can be reversed, corrected, or learned through bounded iteration?

Clearer answers often support a narrower application. Mixed answers call for decomposition and investigation, not a majority vote. A wide strategy decision can contain narrow forecasting or experiment-design tasks. A seemingly narrow store-location or fraud decision can still involve substantial distributional, political, or financial consequences.

Prediction is not causal identification. An optimization method needs a defensible objective, and a causal claim needs an appropriate design and assumptions. Do not buy generative fluency where the task requires a validated forecast, or presume analytical AI can establish causality merely because it produces a number.

Use `rtp-ai-use-case-readiness` for actual action rights and controls. The narrow/wide distinction differs from `rtp-problem-type`’s technical/adaptive distinction; either kind of organizational work can contain narrow and wide decisions.

## 5. State a testable hypothesis and the critical assumptions

Write the hypothesis at a level that can be checked:

```text
RECOMMENDATION: [AI / rules or software / hybrid / human-led / do not build / research]
HYPOTHESIS: For [task and population], [approach] will improve [outcome]
  compared with [baseline], because [evidence and proposed mechanism].
IF TRUE: [observable leading and later outcomes, with appropriate timing]
IF FALSE OR INCONCLUSIVE: [contrary evidence or evidence gap and its implication]
DAMAGE IF WRONG: [user harm, cost, delayed alternative, and recovery limits]
PIVOT OR STOP TRIGGER: [signal, threshold if justified, date, owner, and alternative]
```

For example, a support-drafting study might compare resolution quality and total handling time against the current workflow. A forty-percent time-saving target, fifty thousand historic tickets, or a sixty-percent edit rate is not evidence by itself. Editing may be appropriate personalization; evaluate why it occurs and whether the user outcome improves.

Record assumptions in a compact table:

| Assumption | Evidence and limits | Why the decision depends on it | Next test or explicit risk decision |
|---|---|---|---|
| Users value the proposed improvement | What was observed, measured, or reported | Which benefit fails if this is wrong | Appropriate behavior or outcome test |
| Data and labels support the task | Availability, permission, quality, coverage, and leakage checks | Capability or evaluation dependency | Representative audit and baseline |
| People can use and assess the result | Evidence about workflow, competence, time, and authority | Whether the proposed human control works | Task-based trial with relevant errors |
| Costs fit the expected benefit | Current workload assumptions and measured or quoted cost scope | Economic viability or deployment limit | End-to-end cost measurement |

Use evidence labels carefully: **validated within scope** means a specific claim has been tested; **informed** means indirect or directional support; **assumed** means an explicit untested belief; **unknown** means information is missing. Data existing in a warehouse validates existence, not label quality, representativeness, or permission.

Prioritize assumptions by consequence, uncertainty, and the value of resolving them. The assumption that makes someone most nervous is useful input, not automatically the one to test first. Address critical uncertainty before the commitment that relies on it, or record a deliberate, authorized, bounded acceptance of that risk.

## 6. Check persuasive claims and hidden constraints

| Proposal claim | What to test |
|---|---|
| “Competitors use AI” | Actual customer value, use, and relevant market expectations rather than announcements alone |
| “Leadership wants AI” | The intended customer or strategic outcome and the alternative use of resources |
| “We already have the infrastructure” | Incremental cost and real reusable capability; sunk expense alone is irrelevant, but existing useful capacity can change the economics |
| “AI makes it scalable” | The actual bottleneck, total quality, cost, and load behavior; scale may not be the constraint |
| “This creates new work” | What tasks, responsibility, expertise, and demand change, rather than whether the pitch uses that phrase |

For the new-work claim, compare tasks before and after at a useful level of detail. Distinguish augmentation, automation, changed value of expertise, and new tasks. An unchanged high-level job description can conceal new subtasks; an expanded checklist can be overhead rather than valuable new expertise. The comparison is evidence to investigate, not a universal predeployment veto. See [research boundaries](references/research-boundaries.md) for the labor-economics taxonomy.

Apply five broader lenses:

- **Customer:** task fit, accessibility, learning and change burden, alternatives, and who gains or loses. A behavior change is a cost to assess, not automatically a red flag that rules out the product.
- **Business:** total cost and plausible benefit, including review, integration, evaluation, support, and maintenance. There is no universal three-to-five-times-build-cost maintenance rule.
- **Market:** differentiation, distribution, and credible customer expectations. Incremental improvements can matter; an AI label alone may not.
- **Team:** ability to build, buy, operate, evaluate, and respond, with real owners and capacity. Hiring or vendor support is a dependency to plan.
- **Ethics and affected people:** actual harms, fairness, privacy, agency, and recourse, including those who do not choose the system. Reputation alone is not the standard for an acceptable outcome.

Do not reduce these lenses to an unexplained colored radar score. State the material trade-off and evidence gap.

## 7. Use research and examples without inheriting their overclaims

The [examples and optional profile](references/assessment-profile-and-examples.md) retain ticket routing, lead scoring, fraud, invoices, moderation, and scheduling illustrations. Their historical numbers were not verified company outcomes. Use them to construct fair comparisons, not as proof that rules always win a type of task.

The [research reference](references/research-boundaries.md) preserves the innovation-bottleneck, engine/helper, Cleveland Clinic, and worker-task discussions with their limits. In particular:

- AI ideation can narrow or broaden options depending on design and use; compare diversity, quality, and fixation rather than assuming a universal effect.
- A common screening format can reduce presentation differences while hiding relevant information; test the rubric and retain appropriate evidence.
- Simulated customers can help generate questions or exercise a process. Their answers are not automatically evidence of real people’s preferences or lived experience, especially for a new category.
- Post-launch synthesis can organize feedback, while selection, interpretation, and action still require testing. A long list of themes is not proof the bottleneck dissolved.

Ask what problem is being solved and whether implementation expectations are realistic before buying a platform. Involve domain experts and technical operators with clear responsibilities; budget stabilization and iteration. A single well-scoped partner can simplify a project, but comparison or multiple specialists may be appropriate. Searching for repeatable decisions in policies and workflows can reveal candidates; if-then structure alone does not prove an AI opportunity or a safe rule.

## Deliver, review, and hand off

Lead with the recommendation, then the hypothesis, trade-off, biggest risk, critical assumptions, and next action with an owner and timing. Explain why the chosen approach beats the relevant alternative and what remains unproven. “Gather evidence” is a clear position when it names the uncertainty and the test that resolves it.

Check that the customer outcome and task decomposition are clear; the baseline is credible; capability, evaluation, consequence, and economics are addressed; and any score is consistent with the stated evidence. Confirm that the recommendation does not infer correctness from determinism or safety from a human checkbox.

For research or deliberate capability-building, name the learning objective, budget, and bounded exposure. Such an investment can be worthwhile even when a simpler production solution exists. Competitive positioning or a dramatically better experience can also matter, but should be tested rather than treated as exemptions from evidence and controls.

Use visuals selectively: a component comparison, four-question evidence table, or trade-off diagram can clarify a substantial decision. The optional sixteen-point profile should never appear as a green “AI-native” gauge that implies permission to build. Avoid duplicating the analysis in unnecessary document, slide, and image formats.

Carry the context forward to `rtp-ai-use-case-readiness`, `rtp-invisible-stack`, `rtp-determinism-compass`, `rtp-build-or-buy`, or `rtp-cost-model` as needed. For a continuing workflow, create `problem-ai-fit-handoff-[use-case-slug].md` using the shared handoff structure: customer grounding, recommendation, evidence, hypothesis, critical assumptions, constraints, and open questions. Include an optional score only with its meaning and limitations. Preserve the user’s requested format and existing context so the next skill can continue without repeating answered questions.
