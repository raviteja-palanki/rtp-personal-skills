---
name: rtp-bias-spotter
description: Identifies the cognitive bias making a potentially flawed AI product decision feel right or inevitable. Use when evaluating any recommendation, reviewing PRDs, assessing feature proposals, before major resource commits, or when a decision feels 'obvious', 'everyone knows this is right', or 'the competitor did it so we should too'. Triggers on phrases like 'that's just common sense', 'obviously we need to', 'this is our only option', or when urgency is being cited as justification. Also use after hearing from a senior person or consultant to audit for authority bias. Do NOT use as a decision blocker (biases are always present), use it to improve reasoning before deciding. Do NOT use when the team is already paralyzed by analysis and needs to commit.
---
# Bias Spotter

## DEPTH DECISION

**Go deep if:** Making a product decision under ambiguity (model selection, feature scope, rollout strategy). **Skim to questions if:** Quick bias check on a decision already made. **Skip if:** Decision is fully data-driven with clear metrics (A/B test results, hard SLA targets).

## THE TRAP

You will trust your intuition. The bias is **meta-blindness** — the inability to see your own biases while actively looking for them. You'll check for biases, find none, and conclude you're being rational. That conclusion is itself a bias (the bias blind spot).

Most dangerous in AI product decisions because:
- AI capabilities feel magical, triggering optimism bias
- AI failures are probabilistic, triggering normalcy bias ("2% error rate is fine")
- AI costs are deferred (per-token), triggering present bias
- AI competition creates urgency, triggering action bias
- **Automation bias:** You trust the AI output because a computer generated it, without validating against your actual use case
- **Benchmark anchoring:** You trust a published 95% accuracy without knowing if the test distribution matches your production users
- **Novelty bias:** You pursue an AI solution because it's cutting-edge, not because it solves the problem better than the alternative

## THE PROCESS

1. **Name the decision.** State what's being decided in one sentence.

2. **Run the bias checklist.** For each, answer honestly:
   - **Anchoring:** What was the first number/solution I heard? Am I adjusting from it?
   - **Sunk cost:** Have we already invested time/money that's influencing this?
   - **Confirmation:** Am I seeking evidence that supports what I already believe?
   - **Survivorship:** Am I looking at successful examples while ignoring failures?
   - **Optimism:** Am I assuming best-case model performance and adoption?
   - **Authority:** Am I deferring because a senior person or "expert" said so?
   - **Bandwagon:** Am I deciding this because competitors/industry are doing it?
   - **Present:** Am I overweighting short-term gains vs long-term costs?

3. **AI-specific biases to audit:**
   - **Training data bias:** Does the model reflect edge cases, or just majority patterns? Tested on train distribution vs prod distribution?
   - **Evaluation bias:** Are we measuring what matters (user outcomes) or what's easy to measure (benchmark scores)?
   - **Demo bias:** Did the model succeed on a cherry-picked demo, or random samples?
   - **Benchmark anchoring:** Are we trusting a published accuracy % without knowing the test set's relevance to our use case?

4. **Identify the dominant bias.** Usually one or two biases are driving the decision. Name them explicitly.

5. **Apply the inversion test.** Ask: "If the opposite of this recommendation were true, what evidence would I expect to see?" Then look for that evidence.

6. **Restate the decision with bias acknowledged.** "We recommend X. The dominant bias risk is [Y]. We've mitigated it by [Z]."

## AI PRODUCT BIAS TAXONOMY

Biases in AI products fall into three categories. Identifying which category a bias belongs to clarifies how to mitigate it.

### Decision Biases (affect what you build)
These biases shape which problems you choose to solve and which solutions you commit resources to.

- **Anchoring:** Fixating on the first number you heard (a competitor's accuracy, a vendor's demo result, a prior project's estimate)
- **Sunk cost:** Continuing an AI initiative because you've already spent 6 months on it, not because it's the right choice
- **Survivorship:** Building for the customers you kept, not the ones you lost to competitors because of poor AI performance
- **Bandwagon:** Choosing a technology because every other company in your space uses it (LLMs, vector DBs, etc.)
- **Present bias:** Optimizing for a fast MVP instead of investing in robust eval infrastructure, then paying for it in production
- **Novelty bias:** Adopting a new AI architecture because it's novel and exciting, not because it solves your problem better

### Evaluation Biases (affect how you measure)
These biases corrupt how you assess whether a solution is actually working.

- **Confirmation bias:** Cherry-picking eval examples that confirm the model works; ignoring the ones where it fails
- **Demo bias:** Evaluating on a curated dataset that's easier than production; showing impressive live demos that don't represent real usage
- **Benchmark anchoring:** Trusting a published accuracy number without testing on your actual user distribution
- **Optimism bias:** Assuming a model that works at 92% in eval will perform similarly in production (ignoring data drift, distribution shift)
- **Evaluation gap bias:** Measuring what's easy to track (benchmark scores) instead of what matters (user outcomes, business impact)

### System Biases (baked into the AI itself)
These biases are embedded in the model's training process and data, and propagate downstream.

- **Training data bias:** The model learns majority patterns but fails on minorities, edge cases, or underrepresented groups
- **Representation bias:** Certain demographics, languages, or regions are underrepresented in training data
- **Measurement bias:** The metric you optimized for doesn't align with what users actually need
- **Aggregation bias:** The model works well on average but fails systematically for specific user segments
- **Automation bias:** Users and operators trust the model's output uncritically because it came from AI, without human validation

## BIAS IN EVALS

Evaluation is where biases do their most damage in AI products because evals look objective — they're numbers, metrics, test sets. But evaluation processes are where confirmation bias hides most effectively. Watch for these red flags:

- **Cherry-picked eval examples:** "The model worked on 100 examples we tested." Did you test on the 100 hardest examples, or the 100 easiest? Did you test only on queries your support team knows how to answer?
- **Train-eval distribution mismatch:** You train on millions of support tickets from your 500 happy customers, then eval on the same distribution. You ship and hit 50% of production queries that were never in training.
- **Language and localization bias:** You eval on English-only, ship globally, and discover the model fails for Spanish, Arabic, and Chinese users. Evaluation bias masquerading as a surprise.
- **LLM-as-judge bias:** You use GPT-4 to score your model's outputs. GPT-4 tends to prefer verbose, detailed responses and its own style. Your eval looks good. Your users see bloated answers.
- **Sampling bias in error analysis:** You only investigate failures that users reported. You miss silent failures — queries where the model gave a plausible-sounding wrong answer, and users didn't realize it was wrong.
- **Metric-outcome misalignment:** You optimize BLEU score or exact match accuracy. These metrics are easy to measure but don't correlate with user satisfaction or business outcomes.

## BIAS IN MULTI-AGENT SYSTEMS

When you chain AI agents (one agent feeds its output to another), biases compound and propagate in ways that single-agent systems don't:

- **Upstream propagation:** The first agent's training data bias becomes the second agent's input bias. If the first agent systematically misunderstands a category, the second agent inherits that blindness.
- **Coordination bias:** Agents develop implicit agreement with each other. If the first agent makes a confident (but slightly wrong) decision, the second agent amplifies it rather than correcting it. This is confirmation bias between agents.
- **Selection bias in tool routing:** You have a router agent that decides which specialized agent to use. The router was trained to route to the most recently deployed agent (recency bias). Edge cases get routed to the wrong specialist.
- **Error amplification:** Each agent introduces error. Those errors compound. A 5% error rate in agent 1 becomes ~10% in a 2-agent chain, not because the second agent is worse, but because it's working with 95% good inputs.

## WORKED EXAMPLE: AI CUSTOMER SUPPORT AGENT

A real production scenario that illustrates how multiple biases compound:

**The decision:** "We're building an AI agent to handle 50% of inbound support tickets."

**The demo (demo bias + confirmation bias):** The team builds a prototype on curated examples — questions their FAQ answers best. The demo shows 92% accuracy. Everyone sees it working and feels confident. Demo bias: ease of picking good examples. Confirmation bias: the team looked for examples where the model would succeed.

**The eval (confirmation bias + training data bias):** They eval on the support team's historical FAQ dataset — mostly common questions. The team is happy. "92% accuracy proves we're ready." But this is confirmation bias: they eval on exactly the data distribution where the model was trained and where the support team already knew the answers. Training data bias: the FAQ represents 40% of real production queries (the easy ones).

**Launch to production (survivorship bias):** Week 1, the system gets 40% of tickets. Support team notices: accuracy drops to 71%. Why? The 60% of queries that were never in the FAQ dataset — edge cases, complex multi-part questions, requests for custom solutions. These were invisible during eval because they weren't in the support team's training data. Survivorship bias: the team only looked at queries they successfully handled before, missing the ones they'd turned away or escalated.

**The cost:** For a month, users got worse support. Half their queries went to the AI and got mediocre responses. The team rolled back to 10% of traffic and spent 2 weeks rebuilding the eval process.

**Biases identified:**
1. **Demo bias** (5% accuracy overstatement from cherry-picking)
2. **Confirmation bias** (team looked for evidence that worked, not edge cases)
3. **Training data bias** (model trained on easy questions, failed on hard ones)
4. **Survivorship bias** (eval missed the 60% of queries the team had never solved)

Each bias was small. Together they compounded into a 21-point accuracy drop.

**How to prevent:** (a) Eval on a stratified sample that includes low-frequency queries, (b) Eval on production traffic patterns, not your FAQ, (c) Have a neutral party curate eval examples, (d) Report both average accuracy and accuracy by query complexity, (e) Run a shadow deployment for 2 weeks before real rollout.

## REALITY CHECK

- **Failure mode:** Bias-spotting becomes analysis paralysis. Every decision has biases — the goal is to identify the consequential ones, not to achieve perfect rationality. Name the bias, acknowledge the risk, decide anyway.
- **Social cost:** Calling out biases in group settings can feel like personal attacks. Frame as "the decision's bias risk" not "your bias."
- **Diminishing returns:** Beyond 2-3 dominant biases, additional bias identification adds noise, not signal.
- **The meta-trap:** Using bias-spotting to feel rational while still making the biased decision. "We identified automation bias in our thinking, so we're safe now." No — you identified it, then made the same decision anyway without mitigating it. Bias awareness is not bias elimination.
- **Bias awareness is not bias elimination.** The goal is to change the decision or add safeguards, not just to name the bias and feel smarter.
- **The most expensive bias in AI products is optimism bias on model accuracy.** It causes teams to underinvest in fallbacks, error handling, human escalation, and monitoring. A model that's 90% accurate needs more guardrails than a model that's 99% accurate, but teams often do the opposite.

## QUALITY GATE

- [ ] Decision stated in one sentence
- [ ] Full bias checklist answered (not just "checked")
- [ ] Dominant bias named with evidence
- [ ] AI-specific biases audited for this decision
- [ ] Inversion test applied — counter-evidence sought
- [ ] Decision restated with bias risk acknowledged
- [ ] One mitigation or guard specified per identified bias

## OUTPUT FORMAT

Use this structure to document your bias audit:

```
## Bias Audit: [Decision Name]

**Decision:** [One sentence describing what's being decided]

**Dominant biases:** [1-2 named biases with specific evidence]
Example: "Anchoring bias (first quote was 95% accuracy on benchmark); benchmark anchoring (haven't tested on our multilingual queries)"

**AI-specific biases relevant to this decision:**
- [Name and evidence]
- [Name and evidence]

**Inversion test result:** [What counter-evidence was sought and what was found]
Example: "If this model were actually worse than the alternative, what would we see? We'd see higher error rates on multilingual queries. We found exactly that in production shadow data."

**Risk-adjusted recommendation:** [Decision restated with named mitigation]
Example: "Proceed with model. Risk: automation bias from trusting accuracy numbers. Mitigation: 2-week shadow deployment tracking accuracy by language, with automatic rollback if multilingual accuracy drops below 80%."
```

## WHEN WRONG

- Low-stakes decisions where speed matters more than accuracy
- Decisions with clear, measurable outcomes that will self-correct quickly
- When used as a political tool to block decisions rather than improve them
- When the team is already over-analyzing and needs to ship
- When dealing with domain experts who have high signal (e.g., a radiologist's clinical judgment has high base rate accuracy; use bias-spotting to improve reasoning, not to second-guess)

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
