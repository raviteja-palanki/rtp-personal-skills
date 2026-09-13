# Product and organization diagnostic library

Use these frameworks to form and test explanations. A label is not a diagnosis. Record observed behavior, competing explanations, and the evidence needed before recommending a consequential intervention.

## A. Three product-management cultures

| Pattern | Possible behavior | Question and possible improvement |
|---|---|---|
| PM dominated | Product authority overrides engineering or design evidence | Does decision authority depend on title rather than competence and evidence? Clarify shared responsibilities and invite substantive challenge. |
| PM serviced | PM mainly administers requests decided elsewhere | Who owns value and viability? Clarify mandate, decision rights, and the contribution the role can realistically make. |
| PM guided | Product direction and cross-functional solution ownership work together | Are goals, authority, expertise, and accountability aligned in practice? Preserve collaboration rather than treating the label as proof of quality. |

These are patterns within teams, not immutable company identities or predictions of talent loss. A junior PM may influence a local practice even without authority to transform the organization. Strengthening product-minded engineering can help, but it is one route rather than the sole remedy.

## B. Seven product fallacies

All examples below are illustrative.

| Fallacy | What to investigate | Example and repair |
|---|---|---|
| Execution orientation | Is capability determining the problem choice? | A mobile team ignores a stronger desktop opportunity. Compare the opportunity and feasible resourcing alternatives. |
| Bias for building | Is building replacing necessary understanding? | Three months of payment work misses a reporting need. Revisit observed workflows and the decisive assumption. |
| IKEA effect | Is attachment to prior effort sustaining weak work? | A six-month admin panel serves three users. Check those users' value and alternatives before retaining or retiring it. |
| Focusing illusion | Is recent discussion inflating importance? | Interview prompts make page speed dominate discussion. Compare unprompted priorities and actual task effects. |
| Maslow's hammer | Is a familiar method being used beyond its fit? | A team assumes every brand question needs an A/B test. Select evidence appropriate to the claim and available sample. |
| Authority approval | Is internal approval replacing a customer or strategic rationale? | A CEO's AI suggestion becomes a roadmap item without investigation. Examine the actual opportunity and constraints. |
| Catastrophic downside ignored | Is a consequential failure missing from the plan? | Viral sharing enables harassment. Investigate abuse paths and controls before exposure. |

Fast building, existing skills, senior input, and experiments can all be appropriate. Diagnose their use in context rather than treating them as failures by definition.

## C. Feature teams and empowered teams

A feature team primarily implements a prescribed solution; an empowered product team has meaningful responsibility for solving a problem and achieving a defined outcome. In Cagan's framing, product management attends to value and viability, design to usability, and engineering to feasibility; collaboration is still essential.

Ask who chooses the problem, solution, measures, and trade-offs—and whether authority and resources match responsibility. Shipping on time and facilitating clarity can be valuable. Neither is the whole product role, nor evidence that the person works only a few minutes a week. “Time to money” is relevant to some products; public outcomes, reliability, or compliance can be the appropriate result elsewhere.

## D. Functional incentive distortions

| Possible pattern | Observable question |
|---|---|
| Engineering promotion incentives | Is technical work selected for demonstrated product need or mainly for a promotion narrative? |
| Conflict avoidance | Does preserving agreement prevent a necessary decision? |
| Architecture preference | Is architectural sophistication justified by actual users, reliability, or foreseeable needs? |
| Design ideals detached from sustainability | Are usability and inclusion being considered alongside the resources needed to deliver them? |
| Portfolio presentation incentives | Does the design work well for users or mainly look impressive in a portfolio? |
| Executive-request dependence | Can the team challenge a request with relevant evidence? |
| Activity incentives | Is measured efficiency improving work that matters? |

Do not infer these motivations from job function or one disagreement. Incentives, expertise, and legitimate obligations can explain the same behavior. Identify the mechanism before naming a remedy.

## E. Decision quality

Look for relevant alternatives, explicit trade-offs, known unknowns, reversibility, opportunity cost, falsifiable assumptions, and an accountable next action. Inspect what the decision-maker knew at the time.

Watch unsupported certainty, unexplained projections, defensiveness, and favorable presentation substituted for impact. A spreadsheet or analytical request is not inherently false precision. Explain which estimate or test would be useful and which uncertainty cannot reasonably be resolved before acting.

## F. Pre-mortem

For a consequential commitment, ask what could make it fail, which important assumption is untested, what could invalidate the customer need, which severe downside has been overlooked, and what a plausible later failure would look like. Six months is an illustrative horizon; choose the relevant one.

Turn the strongest concern into a proportionate test, control, contingency, or decision boundary. Do not manufacture catastrophe, require a negative finding, or use imagination as proof of likelihood.

## G. Listening quality

Try a deliberate sequence: listen to understand, pause to consider, then respond. Summarize the other person's meaning and check it before rebuttal where useful. Doshi presents separating listening and response planning as a personal practice; it is not a neurological claim that comprehension and thinking cannot overlap.

Watch interruption, selective hearing, rehearsed rebuttals, and reflexive defense. Asking a question can help; a clear statement is not evidence of poor listening. Match the pace to the person and conversation rather than rigidly imposing silence.

## H. Joint alignment conversations

When separate conversations create conflicting accounts, consider a joint discussion. The original “two-on-two” brings a PM lead, engineering lead, PM, and engineer together. Let the people closest to the work help set the agenda; leaders clarify authority and remove blockers rather than interrogate.

Use the participant set that fits the issue. One-to-one conversations can be legitimate and necessary, especially for confidential or sensitive concerns. A joint meeting does not automatically remove power imbalance or distortion. Agree facts, decisions, responsibilities, and follow-up evidence.

## I. AI agency and human control

The original three-row matrix is a **descriptive grouping**, not another numbered autonomy standard:

| Group | What to specify | Example boundary |
|---|---|---|
| Suggest or draft | What the AI proposes and who authorizes use | An email draft remains unsubmitted until the permitted person or process sends it. |
| Act within a bounded workflow | Allowed actions, preconditions, approval points, and recovery | Support routing or extraction may need different controls despite sharing this group. |
| Operate with broader discretion | Scope, consequence limits, monitoring, intervention, and tested reliability | Highly consequential activity requires evidence and controls appropriate to the domain; the label alone cannot approve it. |

Use `rtp-autonomy-spectrum` for the canonical levels and actual permission model. AI risk depends on task, consequence, scale, data, and reversibility—not just agency. Coding suggestions can cause serious harm if accepted without suitable checks. Examples such as trading or driving are not endorsements of unconstrained deployment.

## Failure taxonomy

| Category | Possible issue | Evidence to investigate |
|---|---|---|
| Thinking | Wrong problem, assumption, or decision model | Decision records, ignored alternatives, and information available at the time |
| Execution | Implementation, coordination, capacity, or skill gap | Defects, dependencies, operating conditions, and realistic resource needs |
| Timing | Readiness, market change, or sequencing | Adoption conditions, external events, and what could reasonably have been anticipated |
| Positioning | Value or audience poorly communicated | Buyer understanding, switching behavior, and actual product fit |
| Organization | Authority, incentives, resources, or culture conflict | Decisions, commitments, escalation outcomes, and observed behavior |

Several categories can contribute. Early warnings such as rapid agreement, firefighting, weak conversion, or internal friction are leads, not unique causal signatures.

## Ten recurring failure patterns

| Original pattern | Useful diagnostic core | Recovery and limit |
|---|---|---|
| 1. Product-management theater | Process compliance or shipped features substitute for value | Connect delivery measures to intended outcomes. Ten timely features or a 20% revenue rise alone does not prove the team's contribution. |
| 2. Execution orientation | Easy implementation displaces a stronger opportunity | Investigate an important uncertainty and compare options. Do not force an ambiguous item into every sprint regardless of need. |
| 3. Curse of brilliance | A successful person's tactics are copied without their context | Examine capabilities, constraints, selection effects, and luck. Neither dismiss all expert process advice nor assume success rests on innate gifts. The Apple A/B claim was illustrative and unverified. |
| 4. False-positive promotions | Presentation or team outcomes substitute for evidence of role capability | Use work samples, decision records, role scope, and fair assessment. False negatives can also harm the organization; a poor hire does not inevitably produce ten more. |
| 5. Average product | Undifferentiated work lacks a persuasive value proposition | Identify what matters to the target customer and compare credible alternatives. Reliable parity or small improvements can still create value. |
| 6. Triangulation | Indirect communication yields inconsistent accounts | Establish shared facts and a suitable decision forum; retain private routes where needed. |
| 7. Diligent martyr | Effort goes to low-value polish while consequential work is neglected | Reassess LNO, workload, staffing, and expectations rather than blaming long hours on personality. |
| 8. Repeated difficult-stakeholder accommodation | A recurring behavior remains unaddressed | Describe the behavior, set limits, seek support, or escalate appropriately. Do not label the person a baby or declare them incapable of change. |
| 9. Summary dependence | Condensed material hides evidence, nuance, or disagreement | Return to relevant primary material and test the reasoning. AI synthesis can assist high-value work when the user interrogates it. |
| 10. Missing sustainability | User benefit lacks a viable delivery or funding explanation | Clarify the business or mission value and cost. Non-revenue, public-interest, accessibility, and foundational work can be legitimate. |

Use these patterns to generate an investigation and repair. They are not licenses to invent motives, dismiss constraints, or present a disappointing result as proof of personal failure.
