---
name: safety-as-moat
version: v1.1.2_latest
description: 'Assess whether safety controls reduce harm, unlock sales, or create a lasting competitive advantage. Use for safety investment, enterprise positioning, guardrail budgets, and regulated-market strategy. Separate essential safeguards from procurement requirements and advantages competitors cannot readily copy. Measure latency, legitimate requests blocked, maintenance cost, customer evidence, and risk reduction on comparable terms. Test controls against relevant attacks and examine recovery costs without treating hypothetical losses as guaranteed savings. Produce a control inventory, evidence-backed moat classification, and investment recommendation with owners and next tests. Pairs with safety-by-design for implementation, responsible-ai-program for governance, and moat-finder for broader defensibility. Triggers: safety strategy, safety moat, alignment tax, trust premium, why fund guardrails.'
imports: ["determinism-compass"]
---

# Safety as Moat

Decide what a safety investment accomplishes and whether its advantage can endure. **A control can be essential without being a moat. A buying requirement can unlock revenue without being difficult to copy.** Keep these conclusions separate so the business case neither oversells safety nor removes a necessary protection.

## Start with the decision

Identify the customer and affected people, the task, what the AI can actually access or do, the failure being prevented, and the investment decision. Use existing context; ask only for missing information that could change the recommendation. Follow the shared Universal Skill Protocol at the depth this decision needs.

- **Quick assessment:** examine one control, its purpose, cost, evidence, and next test.
- **Full assessment:** compare a portfolio of controls, regulated-market entry, contractual dependencies, or competitive positioning through all six phases below.
- **Route elsewhere:** use `safety-by-design` for control design, `agent-risk` for delegated action, or `responsible-ai-program` for operating governance. Internal prototypes, consumer products, and work before product–market fit still need safeguards proportionate to their exposure; they may not need a moat analysis.

First identify requirements and unacceptable harm. An attractive return does not justify violating a binding obligation. An uncertain commercial return does not establish that a protection is unnecessary.

## The distinctions that matter

| Term | Meaning in this assessment |
|---|---|
| Alignment tax | Added latency, blocked legitimate work, engineering effort, infrastructure, and operating cost from a safety control. Measure possible efficiency benefits too. |
| Trust premium | Additional willingness to choose, use, renew, or pay attributable to credible safety. Specify which behavior was measured. |
| Data dependence | Reliance on personal or customer data, and customers’ perception of that reliance. Useful memory can create privacy concerns; neither effect is automatic. |
| Minimum viable safety surface | The smallest useful way to make **adequate, functioning** protections understandable. A visible promise cannot substitute for adequate protection. |
| Hygiene factor | A baseline expectation whose absence hurts demand more than further improvement increases it. Whether safety plays this role is a market question. |
| Defense in depth | Complementary controls that reduce dependence on one protection. Test shared failure paths as well as each layer. |
| Red-teaming | Authorized adversarial testing of harmful behavior and misuse. It contributes to both security and product quality. |
| Bypass rate | Successful attacks divided by eligible attempted attacks under a stated test protocol. It is not automatically a production incident rate. |
| CDR | Corporate Digital Responsibility: governing the effects of data and digital systems on people and business performance. |

Safety can support four different claims: **harm reduction, permission to operate, customer preference, and durable advantage**. State the evidence for each. To claim a moat, explain what competitors would have to reproduce: accumulated trust, proven operations, integrations, contractual assurance, specialist capability, or another costly dependency. A certificate or a copied prompt alone rarely establishes that claim.

## Phase 1 — Map the failure and the applicable requirements

Describe the causal chain: action or output → affected person or asset → potential harm → prevention or recovery opportunity. Include misuse, accidental failure, hallucinated claims, data leakage, unauthorized actions, and physical consequences where relevant.

For each obligation, record jurisdiction, applicable entity and activity, specific provision or contract, effective date, evidence needed, and owner. Distinguish current requirements from proposals and voluntary standards. Confirm consequential legal interpretations with the responsible specialist using current primary sources.

| Framework | What to verify |
|---|---|
| EU AI Act | Applicability, role, risk category, relevant obligation and implementation date. High-risk oversight provisions and maximum penalties do not apply uniformly to every AI product or violation. |
| NIST AI RMF | Voluntary Govern, Map, Measure, and Manage framework; identify any separate contractual requirement to use it. |
| US state laws | Actual jurisdiction, covered use, exemptions, commencement, and amendments. Avoid a generic “2027 rollout” assumption. |
| HIPAA | Covered-entity or business-associate status, PHI, permitted use, safeguards, and applicable agreements. It does not cover every health-related AI use, and individual consent is not the only basis for permitted processing. |
| SOC 2 | Scope and findings of the attestation against relevant Trust Services Criteria. It is not a universal AI certification or a statutory requirement for every enterprise sale. |

Check the dated [evidence notes](references/safety-economics-evidence.md) before using the historical cases or numerical examples.

## Phase 2 — Test customer value and contractual dependence

Examine actual wins, losses, renewals, security reviews, and comparable alternatives. Interview a few relevant buyers to start, then broaden if the evidence is thin or unrepresentative.

1. Which customers require the control? Does its removal trigger a real contractual issue, a procurement objection, or only a preference?
2. Did it change a buying decision, price, renewal, or time to approval? What else changed?
3. Could a competitor offer equivalent assurance quickly? What would remain distinctive?
4. Does the control help users perform the task safely, or merely improve an RFP response?

Report both the number of affected contracts and their revenue concentration. Neither “over 20%” nor “under 5%” is a universal investment threshold. One critical commitment can matter; a widely copied requirement can still be table stakes. Required contracts’ entire ARR is **exposure associated with the control**, not necessarily incremental revenue caused by it.

### Make the trust claim testable

Privacy research provides evidence that credible stewardship can affect stated purchase intent. It does not establish a universal price premium for enterprise agents, a mathematically convex payoff as risk increases, or that the first visible signal is always the best investment. Test the relevant customer, behavior, and alternative.

Where data dependence creates concern, explain what is collected, why, retention and deletion, reuse limits, and meaningful user controls. Lack of switching freedom can weaken a market mechanism; it does not make privacy protection worthless or excuse inadequate disclosure.

### Communicate what each audience can use

Give regulators and auditors accurate, scoped evidence and required disclosures. Give buyers and users information that helps them choose and act: limitations, controls, recourse, and changes that affect them. Protect sensitive security details without substituting vague assurances.

The Novel Insights disclosure cases suggest checking **actionability and timing**, and measuring delayed trust or fit alongside immediate conversion. This is a useful hypothesis, not proof that disclosure always helps sales. Required disclosures and material information can remain necessary even when the recipient has limited recourse. Neither “stay quiet with customers” nor “disclosure earns regulatory leniency” is a reliable general rule.

### Use the CDR Calculus

| Quadrant | Business effect | Customer well-being | Response |
|---|---|---|---|
| Failures | Negative | Negative | Stop, contain, or redesign the harmful arrangement. |
| Temptations | Positive | Negative | Identify who bears the harm and change the incentives or design. |
| Sacrifices | Negative | Positive | Make the cost, purpose, authority, and funding explicit. |
| Sweet Spot | Positive | Positive | Verify both benefits and sustain the conditions that produce them. |

Specify whose outcomes and which time horizon define the placement. Review when circumstances change; a six- to twelve-month review can be a planning cadence, not a proven optimum. Movement between quadrants is possible, not inevitable. Use the CDR playbook—inventory, oversight in design, credible evidence—to turn classification into action.

## Phase 3 — Establish adversarial evidence and a learning loop

Begin with a threat model and the most consequential failure paths. Include domain experts, builders, and fresh reviewers where useful. Use authorized environments and safe test data; never create live harm to demonstrate seriousness.

| Assessment | Purpose | Interpretation |
|---|---|---|
| Baseline | Establish coverage, vulnerabilities, and control cost. | A severe failure can block release immediately; the first run is not exempt from acceptance criteria. |
| Comparable repeat | Retest a stable core after changes. | Compare the same definitions and severity mix; investigate differences. |
| Fresh challenge | Probe new capabilities, attacks, and dependencies. | Report separately from the stable core before combining rates. |
| Targeted checks | Retest fixes and high-consequence paths between broader reviews. | Set cadence by change rate and risk, including model or tool updates. |

Three risk categories with forty attacks each, quarterly broad reviews, and ten to fifteen monthly spot checks are **starting examples**, not sufficient coverage or mandatory schedules. Use `stress-test` for increasing challenge complexity.

Report attack count, successful bypasses, severity, scenario coverage, version, evaluator, and uncertainty. Include legitimate-request tests to measure unnecessary blocks. A falling rate can reflect easier attacks; a rising rate can reflect a stronger test. A flat rate near 2% does not identify an architectural floor. There is no universal “under 2% is safe” target. One consequential bypass may warrant action despite a low aggregate rate.

Route confirmed live harm to incident response. Route test findings to owners, remediation deadlines, and regression coverage. Retain useful failures in evals while adding new challenges; passing known attacks does not establish broad safety.

## Phase 4 — Test first-mover advantage

Map a specific customer opportunity to a credible requirement, readiness gap, and competitor catch-up path. Estimate the period in which preparation might accelerate entry or reduce rework. Compliance capability can enable sales; it does not guarantee six to twelve months of exclusivity or $10M–$100M of market expansion.

Distinguish standards participation from influence over actual rules, and both from favorable regulatory treatment. Refresh assumptions when laws, procurement requirements, or competitor offerings change.

## Phase 5 — Compare costs and benefits at a consistent scale

Measure each layer’s latency distribution, legitimate requests blocked, operating effort, infrastructure, testing, incident handling, and maintenance. **False-positive rate = legitimate requests incorrectly blocked / all tested legitimate requests.** Report the population and severity of lost work.

Model current and plausible future exposure, including a 10× volume scenario when useful. More volume can increase opportunities for failure, but losses need not scale linearly. Consider shared incidents, correlated failures, data sensitivity, and concentration.

Compare alternatives over the same horizon:

`Net benefit = incremental contribution enabled + expected loss reduction − incremental lifecycle cost`

Expected loss reduction compares risk **with and without** the control; it is not the full unmitigated loss. Include residual risk and whether the control actually interrupts the harm. Avoid counting the same lost contract in churn, reputation, and revenue protection. Maximum fines are not expected fines. Use ranges or qualitative judgments where reliable probabilities do not exist.

**Illustration:** a control adds 200 ms, incorrectly blocks 0.3% of legitimate requests, and costs $150,000 annually. Four contracts worth $2.3M ARR require it. This establishes cost and associated exposure. Estimate the feasible alternative, attributable retention or sales benefit, contribution margin, and remaining risk before claiming ROI. A hypothetical $5M–$50M incident range does not settle the decision.

### Include the recovery period

Model immediate response, legal and remediation cost, interrupted operations, customer losses, renewal effects, and the work needed to restore confidence. Use actual incident histories, contract cycles, and recovery plans. The old consumer 3–6 month, enterprise 12–18 month, regulated 24–36 month, and government 3–5 year windows are scenario assumptions, not validated benchmarks.

An illustrative $2M immediate loss plus $4M annual revenue × 1.5 years × a constant 20% shortfall totals $3.2M. This assumes a stable annual revenue base and a sustained shortfall; it is not a general NRR formula. Convert revenue effects to the chosen economic measure and compare the probability-weighted reduction against control costs over that same period. A $300,000 annual protection does not automatically avoid the whole amount.

Legal duties and unacceptable harm remain constraints alongside economics. A failure cost ten times engineering cost is not, by itself, a decision rule.

## Phase 6 — Design protection that supports the claim

State a concise set of testable behavioral principles, then connect each to an enforceable control, an eval, and an owner. Five to ten principles can make a useful workshop draft; the number has no special safety property.

**Constitutional AI** is a specific training approach using principles and AI feedback. A system prompt containing principles can be useful, but is not equivalent to that method or an enforceable security boundary.

| Layer | Useful role | Boundary to test |
|---|---|---|
| Input checks | Detect prohibited requests, suspicious data, or known attack patterns. | Indirect instructions, transformed content, and novel attacks can pass. |
| Model instructions and training | Shape behavior and handle contextual policy decisions. | Compliance is fallible; a prompt cannot grant or constrain external permissions by itself. |
| Output checks | Detect prohibited content or sensitive data before release. | Subtle errors, meaning-dependent harms, and actions already taken may be missed. |
| Monitoring and response | Find regressions and incidents, evaluate controls, and drive corrective action. | Sampling and detectors miss events; detection after harm is not prevention or recovery. |

For agents, also enforce action permissions, identity, spending or rate limits, approvals where needed, and isolation **at the tool or execution boundary**. A filtered final answer cannot undo an unauthorized transaction. Use `tool-architecture` and `agent-risk` for that design.

Measure each layer and the combined system. Their coverage overlaps and their failures can correlate; do not add percentages or assume 100% monitoring coverage. Choose preventive controls where harm arrives before a response is possible. Document tested limits as clearly as benefits.

## Eight diagnostic questions

1. Which buyers value this control, and what behavior demonstrates it?
2. Which actual obligations or upcoming changes matter to this use?
3. What would removal change in existing contracts or customer workflows?
4. Can adversarial findings change the product and be retested?
5. What immediate and prolonged losses could a failure cause?
6. What latency, cost, and legitimate-work burden does the protection add?
7. Is it a basic expectation, a differentiator, or a difficult-to-copy dependency?
8. Is the investment case supported by comparable costs, evidence, and realistic alternatives?

## Deliver the assessment

Lead with the decision and its strongest evidence. Include only the detail needed to review it:

```markdown
## Safety-as-Moat Assessment: [product or feature]
Decision: [invest / maintain / redesign / reduce or retire a control]
Essential protections and constraints:
Classification: [harm reduction / operating requirement / table stakes /
                 customer differentiation / first-mover or switching advantage]
Durability evidence and competitor catch-up path:

| Control | Failure addressed | Cost and latency | Legitimate work blocked | Customer evidence | Obligation | Owner |
|---|---|---|---|---|---|---|

Economics: [horizon, alternative, attributable benefit, expected loss reduction,
            lifecycle cost, ranges, residual risk, nonfinancial consequences]
CDR position: [affected groups, business and well-being measures, time horizon]
Red-team evidence: [date, versions, counts, severity, coverage, open findings]
Requirements: [source, applicability, status, gap, due date]
Next action: [owner, test or change, deadline, decision it will inform]
Key trade-off and condition that would change the recommendation:
```

Use the shared trade-off and conclusion guidance without duplicating the same material. Add a visual summary with the available drawing skill when it makes the architecture or decision easier to understand; a diagram is optional.

## Review before recommending

Check seven things: relevant customer evidence; correct requirement mapping where applicable; comparable economics; functioning monitoring and response; adversarial evidence; measured alignment tax; and complementary controls with known gaps. These checks support judgment. Passing all seven does not prove a moat; a gap does not justify deleting an essential control.

Reconsider the scope when a control adds burden without reducing harm, customer evidence fails to support a premium, rules change, or a competitor provides equally credible safety more efficiently. A control that never fires may be unnecessary, broken, or successfully preventing a rare event—test those explanations before retiring it. Optimize excessive blocking without simply sampling away critical preventive checks. Consumer growth, competitor speed, and early product exploration do not remove responsibility for foreseeable harm.

See [CONCEPT.md](CONCEPT.md) for the business logic and worked scenarios.
