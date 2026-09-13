# Calibration examples and research connections

Read this reference when choosing trial settings, discussing numerical targets, or using the sourcing, governance, and commerce cases. The main skill contains the operating method. Numbers below retain teaching examples and their limitations; they are not defaults or verified product results.

## Sampling ranges to investigate, not prescriptions

The following ranges appeared in the source skill. Temperature scales, supported controls, and effects differ by model and service. Check current documentation and evaluate representative tasks before choosing a setting.

| Task illustration | Candidate temperature from the source | Boundary to preserve |
|---|---:|---|
| Legal or compliance assistance | 0 | Does not make model output deterministic, legally correct, or safe to act on |
| Support response | 0.2–0.3 | Wording may vary; factual or policy errors are not acceptable merely because variation is allowed |
| Classification or extraction | 0.3–0.5 | Test the label or extracted value, not just the schema |
| Personalization or reasoning | 0.5–0.7 | A broad task label cannot establish the appropriate sampling setting |
| Creative generation | 0.7–1.0 | Creativity still operates within the requested content and constraints |

The contract example used 0.3 for classification, 0.5 for scoring, and 0.6 for summaries. These were proposed settings, not a demonstrated optimum. A supported seed can help debugging in a controlled environment; record its actual repeatability rather than calling it a guarantee.

## Numerical QA examples

- **Recommendation variation of 20–30%, support variation of 5–10%, and zero variation for critical values:** first define the comparison measure. Recommendation overlap and changed factual claims cannot share an unexplained percentage scale. For critical outputs, enforce substantive correctness, not merely repeated wording.
- **Ten, fifty, or one hundred repeated runs:** possible exploration sizes. Choose a design capable of detecting the failure rate that matters. Repeating a narrow input does not cover a broad population.
- **Two hundred regression examples and a two-percentage-point drop:** possible starting choices. Justify coverage, uncertainty, severity, and response policy. Preserve a stable comparison set while adding relevant new failures.
- **Customer-facing pass^3 above 85%, internal pass@3 above 95%, batch pass@1 above 90%, or filter pass^10 above 99.9%:** illustrative thresholds from the source, not approved launch standards. Report actual results and uncertainty, and evaluate whether the user can identify the successful candidate in a multi-attempt workflow.
- **Three-sample voting:** a candidate intervention to evaluate. Its cost is additional trials and selection work; its benefit depends on error diversity and a valid voting rule.
- **Risk-score variance below 0.2:** incomplete until the scale and statistic are specified. A low-variance score can be consistently wrong.

Snapshot tests can protect exact invariants within any system, including one using AI. Avoid exact text comparisons only when valid differences should pass. Passing format or confidence-range checks does not establish correctness.

## Sourcing and autonomy

The library connects this skill to Abhinav Agrawal's [AI Is Rewriting the Economics of Outsourcing](https://hbr.org/2026/06/ai-is-rewriting-the-economics-of-outsourcing), HBR, 5 June 2026. The source title, author, and date were checked; the full publisher article was not accessible in this review. The operational interpretation is to assess routine work, judgment, liability, and accountability separately. A four-way work classification is mentioned in the earlier source, but its four category names are not supplied there; do not invent them.

Routine, measurable tasks can be candidates for automation, while consequential judgment may require qualified oversight. Neither a service-level target nor a named human alone establishes adequate governance. Check hidden consequences in apparently routine work, such as an intake error that affects a later decision.

The local Q2-09 application card for *Beyond Verification: What Responsible AI Really Demands of Human Experts*, Renieris, Kiron, Mills, and Kleppe, MIT Sloan Management Review, 12 May 2026, explicitly labels the "line you can still check" as a conceptual deduction. Preserve that status. The card connects setup judgment to autonomy, maintenance of human expertise, and review of what the team learned from a pilot. It is not evidence that reviewing every output always destroys efficiency or that setup verification is sufficient.

## Reversibility and the pace of a decision

The July 2026 HBR management-tips compilation and Watkins enterprise-leadership podcast remain incompletely verified sources in this library. The predictability/reversibility matrix is the library's synthesis of their themes, not a validated result from either source.

The useful hypothesis is that a bounded, readily reversible experiment can generate evidence at acceptable cost, while a hard-to-reverse commitment often benefits from additional scrutiny and dissent. Test reversibility, severity, information value, and opportunity cost in the actual case. There can be good reasons to deliberate over a reversible decision; absence of a counterexample in the local corpus is not proof of a universal rule.

When uncertainty is difficult to reduce, consider reducing the cost of being wrong. In the main matrix, this means moving from the hard-to-reverse row toward the readily reversible row—not changing the predictability column.

## Minimum viable governance: a hypothesis to test

MIT CISR's [glossary](https://cisr.mit.edu/research-library/glossary) describes minimum viable governance as sufficient governance to manage risk while enabling opportunity, across principles, policies, people, processes, and platforms. The local research note discusses a 15 June 2026 MIT Sloan *Ideas Made to Matter* summary. It is not a MIT Sloan Management Review article. The underlying briefing's method was not inspected here; verify the exact briefing date before citing the earlier 19 March date.

The library raises a useful concern: if teams measure approval friction but poorly measure residual risk, pressure to reduce friction may weaken necessary controls. Treat that as a mechanism to investigate. The source skill's "roughly two quarters" estimate has no supporting population or study and should not be repeated as a forecast.

Ask what each control prevents, what monitoring can detect in time, who can intervene, and what harm remains after rollback. Monitoring and gates can work together. A monitoring-only design needs evidence that consequences remain acceptable; an upfront gate also needs evidence that it controls the relevant failure. Do not claim that uncertain risk is wholly unmeasurable or that a governance framework must inevitably collapse.

## Commerce case: discovery and commitment

OpenAI introduced Instant Checkout in September 2025. Its launch description included user confirmation and merchant-controlled payment and fulfillment, so the transaction should not be described as unconstrained probabilistic money movement. See the [launch post](https://openai.com/index/buy-it-in-chatgpt/).

On 24 March 2026, OpenAI said it was focusing on product discovery while allowing merchants to use their own checkout experiences, and still described deeper integrations through ChatGPT apps. This supports a change in approach, not a claim that every in-chat purchase option was eliminated. The company's stated explanation concerned flexibility. See [Powering Product Discovery in ChatGPT](https://openai.com/index/powering-product-discovery-in-chatgpt/).

The earlier skill cited secondary reports of roughly one-third retailer-site completion, 8% first-month use among US adult ChatGPT users, and about a dozen Shopify integrations. Those figures were not corroborated in the primary posts inspected for this revision. Keep them out of an evidence-backed performance claim until their definitions, dates, and original measurement sources are checked. The earlier [CNBC citation](https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html) remains a research lead.

**Application, explicitly an inference:** separate exploratory recommendations from consequential commitments, and verify the authority and execution path for each. The case does not prove that model nondeterminism caused the product change. Checkout can use reliable transaction systems even when discovery or intent interpretation involves a model, and discovery can also cause harm. Examine each actual boundary. `marketing-to-ai-agents` covers the commercial interpretation of this case.
