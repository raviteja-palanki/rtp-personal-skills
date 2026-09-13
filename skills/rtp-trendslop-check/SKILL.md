---
name: trendslop-check
version: v1.6.1_latest
description: 'Audit a strategic recommendation for fashionable defaults, unsupported evidence, and assumptions that do not fit the organization. Use before committing resources to AI-generated advice or when a polished strategy needs an independent context check. Preserve the recommendation, identify its decisive assumptions, compare credible alternatives, and decide which claims to retain, revise, test, or reject. Examine differentiation, automation, time horizon, growth, and innovation choices; also consider collaboration, decision authority, and exploration when relevant. The HBR trendslop research motivates scrutiny but does not prove that a popular recommendation is wrong or that prompting cannot help. Check units, chronology, causal claims, missing citations, modeled benefits, and measurement proxies. Produce a concise audit with evidence status, trade-offs, falsifiers, and a next decision. Connect to first-principles, bias-spotter, falsification, and strategy-canvas.'
imports: [first-principles, bias-spotter]
---

# Trendslop Check

Check whether a recommendation follows from the organization's situation or mainly from familiar, appealing management language. The goal is a better-supported decision. Do not assume that AI advice is wrong, that human advice is unbiased, or that the opposite of a popular strategy is better.

A March 2026 HBR article by Angelo Romasanta, Llewellyn D.W. Thomas, and Natalia Levina reports directional preferences in strategic choices made by several LLMs and sensitivity to prompt framing. It motivates this audit. The original research has narrower scope than several claims previously made in this skill; see the [research interpretation](references/research-and-cases.md#what-the-trendslop-article-actually-reports) before quoting its numbers.

## Start with the recommendation and decision

Use the strategy text, available business context, and relevant evidence. Identify the customer, business model, market position, time horizon, resource commitments, decision owner, and action under consideration. Ask only for missing facts that could materially change the audit.

Preserve the exact material wording of the recommendation and its source where available. Then summarize it separately. Do not invent a quotation or rewrite a claim into a stronger one before criticizing it. If the original is missing, label the supplied account as a summary.

For a quick review, examine the decisive assumption, strongest alternative, and most consequential evidence claim. For an investment decision, review the broader dependencies, costs, consequences, and source trail. Use the requested format; a concise inline audit is a reasonable default. Create a document or presentation when it serves the user's intended use.

This check is useful for AI-generated, human-edited, or human-written strategy when unsupported defaults may matter. Skip a separate pass if an existing review already answers these questions adequately. A first-principles label does not itself establish grounding.

## What to watch for

A recommendation deserves examination when it:

- Repeats a favored choice without explaining why the alternatives lose under the stated constraints.
- Adds company-specific details while leaving its decisive assumptions unchanged.
- Uses attractive terms such as differentiation, augmentation, collaboration, or transformation in place of mechanisms, resources, and evidence.
- Recommends “both” without saying how resources, conflicts, and responsibilities will be managed.
- Supports a consequential choice with a statistic whose population, unit, method, or source is unclear.

These are prompts to investigate, not findings of error. Two competitors can reasonably choose similar strategies. A common recommendation may reflect a shared constraint or effective practice. Likewise, a unique recommendation is not automatically good.

## The audit process

### 1. Extract the proposed choice

State the problem, approach, required investment, expected result, and alternatives excluded. Distinguish proposed facts, forecasts, and preferences. Identify the decision it would cause: spending, hiring, positioning, pricing, product scope, or a different commitment.

Illustration: a recommendation proposes a privacy-focused premium product, a $2 million investment over eighteen months, and a target of 20% enterprise-market share. Those are hypothetical planning claims, not validated market facts. A 20% market-share target does not imply a 20% price premium. Encryption and zero-knowledge claims also require an architecture that supports them; a strategy label does not establish feasibility.

### 2. Identify the assumptions that could change the choice

For each decisive assumption, record the claim, evidence, confidence basis, consequence if wrong, and next test. Use clear statuses:

| Status | Meaning |
|---|---|
| Supported for this use | Relevant evidence supports the assumption within a stated scope |
| Contradicted | Relevant evidence conflicts with the assumption |
| Unknown or weakly supported | Evidence is missing, indirect, stale, or insufficient |
| Preference or constraint | A chosen priority, obligation, or boundary rather than an empirical claim |

Deep conviction belongs in the explanation, not in a “known true” evidence category. One contradicted premise can defeat a recommendation; many low-impact unknowns may not. Replace the old two-false/three-unknown counting gate with consequence-based judgment.

For the privacy example, investigate enterprise demand, willingness to pay, available funding, feasible architecture, competitive alternatives, and the durability of any advantage. Do not presume competitors lack privacy features or that privacy alone is a moat.

### 3. Examine the relevant strategic tensions

The five core diagnostic lenses below preserve this skill's practical coverage. They are not five independently validated bias scores. The research studied seven tensions; growth versus profitability is this library's additional lens.

| Core lens | Context questions | A useful alternative to examine |
|---|---|---|
| **Differentiation and cost leadership** | What do customers value? Can the firm provide it profitably? Where are costs, distribution, and competitors strong or weak? | A lower-cost, narrower, or more standardized offer; or a clearly valuable distinction |
| **Augmentation and automation** | Which tasks, errors, responsibilities, and human contributions are involved? What can the system reliably do? What do affected users need? | A different division of work, including selective automation or additional human contribution |
| **Long- and short-term performance** | What must happen before funding or patience runs out? Which immediate actions preserve valuable longer-term options? | A staged investment with near-term milestones, a smaller commitment, or a different horizon |
| **Growth and profitability** | What funds growth? How do unit economics, retention, competition, and capacity behave at greater scale? | Consolidation, better contribution, focused growth, or a deliberately funded expansion |
| **Radical and incremental change** | Are improvements within the current model enough? What would a larger change require, displace, or put at risk? | A bounded incremental test or a more fundamental option, depending on the original recommendation |

Apply each lens to evidence rather than stereotypes. Asset-light firms can differentiate. Bootstrapped firms can invest for the long term, and venture-backed firms can face immediate funding limits. Cost leaders can offer distinctive value. Profitability is not always a prerequisite for growth, and a winner-take-most label does not remove financing risk.

For automation, assess consequences and actual permissions before economics alone. Human involvement can add expertise, consent, accountability, recovery, or customer value; it is not automatically a costly “safety blanket.” Automation may also improve quality and safety. Specify the work rather than assuming either arrangement is superior.

The earlier main diagnostic asserted an incremental bias while its research summary described a radical preference. The revised lens tests both directions and preserves the reported radical tendency only as a study-specific finding to verify for the current system.

When relevant, add the other research tensions:

- **Competition and collaboration:** compare the value created, dependencies, incentives, coordination costs, and value capture. A partnership is not inherently better than competing.
- **Centralization and decentralization:** locate decisions where information, authority, consistency, and accountability support them. Different decisions may belong at different levels.
- **Exploration and exploitation:** compare learning about new possibilities with improving proven work. Variation across tested models does not establish that this axis is free of bias.

### 4. Compare credible alternatives under the same constraints

Develop at least one plausible alternative when the decision warrants it. An opposite framing is a useful prompt, but do not force a false binary or fabricate a viable alternative. Include maintaining the present course, narrowing scope, waiting with a deadline, or stopping where relevant.

For each option, use the same objective, evidence standards, budget, timing, customer needs, and consequential constraints. Identify distinct capabilities and conflicts. A hybrid can be coherent when it specifies segmentation, sequence, allocation, or mutually reinforcing activities. “Do both” without that explanation is incomplete, not proof that every hybrid fails.

An optional prompt exercise is to request the strongest case for each option separately, then ask for failure conditions and missing evidence. Another is to vary option order while keeping substantive information constant. Repeated changes can reveal sensitivity; a single flip can also reflect sampling variation. Record the model/version, prompts, relevant settings, and results if conducting a comparison.

These exercises generate candidate arguments and diagnostic evidence about the output. They do not independently verify market claims or guarantee improved decisions. Rich context remains necessary even though it may not remove all bias. More reasoning, an adversarial persona, or agreement among several models is not a substitute for external evidence.

### 5. Check the evidence carrying the argument

For each consequential claim, establish the exact source, date, population, unit, period, method, and inference being made. Follow the claim to the original evidence when feasible. Separate an inaccessible source, an unlocated source, a source that is silent, and a source that contradicts the claim.

| Check | What to establish |
|---|---|
| Direction | Does the number mean success, failure, increase, decrease, prevalence, or a relative change? Does the surrounding sentence agree? |
| Units and denominators | Are signups, paying subscribers, active users, outputs, people, and work periods being compared appropriately? |
| Chronology and entities | Did the claimed cause precede the outcome? Are a company, an asset sale, and a continuing product being conflated? |
| Composite value | What is in the total, over what period, with what baseline and costs? Are components overlapping? |
| Counterfactuals and attribution | How is the alternative outcome estimated, what assumptions identify the effect, and what else changed? |
| Citation trail | Does the source exist and support this exact claim? Are apparently separate accounts repeating one underlying study? |
| Constructs and proxies | What observable result or behavior represents the claimed capability, and how valid is that measure? |

A missing link is repairable. Search for an identifiable study before declaring it nonexistent. A credible institution's name is not enough, but lack of a citation is not proof of fabrication. Check nearby text, endnotes, appendices, and the full source before reporting an omission.

Counterfactual benefits such as avoided cost or reduced risk can be estimated rigorously. They are not unfalsifiable simply because the alternative was not observed for the same person or firm. Conversely, a before-and-after efficiency number is not automatically causal. State the design, assumptions, uncertainty, and validation limits for both.

Tacit knowledge may be difficult to verbalize but still observable through skilled performance, error patterns, adaptation, or learning. Use transfer measures such as mentoring, attrition, or time to proficiency when helpful; hours or departures do not themselves prove knowledge quality or causal loss.

Keep the original teaching cases and their corrections in [research and cases](references/research-and-cases.md). Use the case that matches the actual failure, rather than applying every warning to every claim.

### 6. Decide what survives the audit

For each material recommendation, choose one status: **retain**, **revise**, **test before committing**, or **reject for this context**. Explain the evidence and trade-off. An “unknown” can warrant a limited reversible experiment rather than either full commitment or refusal.

Illustration: a pre-seed company with $500,000 cash, three engineers, and individual-developer customers receives an enterprise expansion plan. Those facts do not by themselves specify runway or rule out enterprises. Estimate burn, sales cycle, demand, capabilities, and funding options. If the proposed commitment exceeds credible capacity, compare a narrower developer offer, a paid enterprise pilot, reduced burn, or another viable path. Do not automatically replace growth with profitability merely because the company is small.

Name the evidence that would change the choice, the observation period, and the decision owner. Consider execution quality, market changes, and competing explanations when interpreting later results. A bad outcome alone does not prove that the original recommendation was biased; a good outcome alone does not validate every premise.

## Deliver the audit

```text
TRENDSLOP AUDIT — [decision, date, owner]
Original recommendation: [exact material wording and source; summary separately]
Decision context: [customer, objective, market, resources, constraints, horizon]
Decisive assumptions: [status, evidence, consequence, next test]
Applicable tensions: [specific concern or no material issue found]
Alternatives: [comparison under the same constraints; hybrid rationale if relevant]
Evidence corrections: [claim, source, corrected scope, remaining uncertainty]
Disposition: [retain / revise / test / reject, with reasons]
Recommended next step: [commitment limit, owner, date]
Falsifier and review: [observable signal, timing, response]
```

Before finishing, check that the original advice was represented fairly, decisive assumptions were assessed, alternatives were plausible, and the conclusion follows from the context rather than a preference for contrarianism. Do not require a plan to work with 50% fewer resources: use such a stress scenario only if that shortfall is plausible, and explain the contingency. A resource-dependent plan can be valid when those resources are secured.

The audit itself costs time and attention and can overemphasize known failure patterns. Scale the effort to the commitment and uncertainty. Strategy can be revised, but money spent, contracts, lost opportunities, and trust may not be recoverable; name the actual reversibility window.

Use `first-principles` for underlying assumptions, `bias-spotter` for broader reasoning bias, `falsification` for decisive tests, and `strategy-canvas` for the resulting choices. Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) for a proportionate trade-off ledger and handoff. Conclude with the recommendation, hypothesis, main trade-off, biggest risk and mitigation, and next action by role and date.

A visual is optional. An `excalidraw-svg` option-comparison matrix or assumption map can help; avoid a numerical bias radar unless its dimensions and scoring are actually defined. Do not generate three visuals by default for a short audit.
