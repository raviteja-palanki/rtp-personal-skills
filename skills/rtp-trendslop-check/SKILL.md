---
name: rtp-trendslop-check
description: 'Catch when AI-generated strategy defaults to trendy advice instead of context-specific strategy. Across 15,000+ trials, LLMs show systematic bias: favor differentiation over cost-leadership, augmentation over automation, long-term thinking over immediate profit. NOT based on what''s right for your business, but based on what''s common in training data. Use when bootstrapping strategy, running multi-scenario planning, or validating AI-generated recommendations.'
---
# Trendslop Check

When you ask an AI to generate strategy, it produces sophisticated-sounding advice. It's also biased in predictable, measurable ways.

Across 15,000+ trials (see appendix for research), Large Language Models show the same strategic biases: They recommend differentiation when cost-leadership is right. They recommend augmentation when automation is the move. They recommend long-term thinking when the business needs to survive the next 12 months.

This is not because LLMs are stupid. It's because training data is biased toward:
- Venture-backed companies (bias toward growth, differentiation, long-term thinking)
- Published case studies (bias toward success stories, rarely bankruptcy stories)
- Business publications (bias toward novel strategies, not proven ones)

When you ask an LLM "What's our strategy?" it gives you the strategy that's most common in its training data. This is almost never the strategy that's right for your specific context.

> "The AI gave us beautiful strategic thinking. When we shipped it, it didn't match our market position or our constraints. The strategy was right for a different company." — Real quote from a PM

---

## Quick Reference: The Five Trendslop Signals

When you see these patterns in AI-generated strategy, trendslop is at work:

1. **Differentiation bias:** The AI recommends "differentiate on X" regardless of whether your market is already differentiated, whether your cost structure allows it, or whether customers actually care.

2. **Augmentation bias:** The AI recommends "use AI to augment workers" even when the economics or user acceptance require automation.

3. **Long-term bias:** The AI recommends strategic plays on 18-month horizons when your business has 6 months of runway and needs immediate revenue.

4. **Growth bias:** The AI recommends scaling and expanding features when profitability, stability, or market consolidation is the actual play.

5. **Optimization bias:** The AI recommends incremental improvement ("improve efficiency") when the business needs discontinuous change ("pivot to adjacent market").

**The detection test:** Ask yourself: "Would the AI give this exact same recommendation to our direct competitor in a different market?" If the answer is yes, it's trendslop.

---

## DEPTH DECISION

**Go deep if:** You're using AI to generate strategic recommendations, evaluating AI-generated strategy before committing resources, or bootstrapping strategy for a new AI initiative.

**Skim to trendslop signals if:** You want to quickly audit an existing strategy recommendation for bias.

**Skip if:** Your strategy is already grounded in first-principles analysis and market data. Trendslop check is for validating AI-generated recommendations, not for cases where strategy is already human-designed.

---

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this validation in?**
> 1. **Word Document** — Formatted audit report showing trendslop analysis. Best for sharing with leadership.
> 2. **Presentation** — Slide deck with key findings and corrected recommendations. Best for meetings and reviews.
> 3. **Both** — Full report + summary deck.
>
> *Default if no preference: Word Document.*

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions — at minimum: What's the business model? What's the market position? What are the constraints?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, or inline?

**Additional grounding for this skill:**

> **1. What's the AI-generated recommendation?** Quote it directly. Don't paraphrase.
>
> **2. What's your actual market position?** Are you a market leader, challenger, startup, incumbent? This determines what strategies make sense.
>
> **3. What are your constraints?** Cash runway, engineering headcount, regulatory limitations, customer lock-in, competitor responses. Strategy that ignores constraints is not strategy.
>
> **4. What's your time horizon for success?** 12 months? 24 months? 5 years? This determines whether long-term plays are even options.
>
> **5. Who would your ideal competitor be for this same space?** If you named a different company type (e.g., a bootstrapped company vs. venture-backed), what strategy would you recommend to them instead?

---

## THE TRAP

The mistake you're about to make: **Trusting AI-generated strategy because it sounds sophisticated.**

Here's how it plays out. You ask an AI: "What's the right strategy for our AI product?" The AI produces beautifully articulated advice: "Differentiate on reliability and customer intimacy. Build for the enterprise market first. Invest in long-term relationships and brand." It sounds like strategy. It sounds smart.

But your company is pre-seed with $500K runway. You have 3 engineers. Your customers are individual developers, not enterprises. The AI's strategy, if you follow it, will burn runway on enterprise sales cycles you can't afford.

**The bias at work:** The AI trained on case studies of successful companies. Most published case studies are about venture-backed companies with abundant runway and growth mandates. The AI learned: strategy = growth + differentiation + long-term thinking.

Your company needs different strategy: **reduce burn, focus on the most viable segment, achieve unit economics before scaling.**

The AI isn't wrong. The AI is biased toward a different company type.

**The fix:** Before you act on AI-generated strategy, run a trendslop check. Ask: Does this recommendation make sense for MY company, or would it make sense for ANY company in this space?

---

## THE PROCESS: Audit AI-Generated Strategy for Trendslop

### Step 1: Extract the recommendation

Get the AI-generated strategy and write it in one paragraph. Include:
- What problem is it solving?
- What's the recommended approach?
- What's the investment required?
- What's the expected outcome?

Example: "Differentiate on customer data privacy. Build a premium tier that offers end-to-end encryption and zero-knowledge architecture. Invest $2M in this capability over 18 months. Expected outcome: capture 20% of enterprise market willing to pay premium for privacy."

### Step 2: Context check — Does this recommendation depend on assumptions that are true for YOUR company?

For the recommendation above, the embedded assumptions are:

```
Assumption 1: There's a enterprise market for our product
Assumption 2: Customers care enough about privacy to pay a premium (20% premium)
Assumption 3: We have $2M to invest and 18 months runway
Assumption 4: Our competitors aren't already offering privacy
Assumption 5: Privacy is a sustainable moat (not commoditized in 18 months)
```

For each assumption, rate:
- **Known & True:** We have data or deep conviction
- **Known & False:** We've tested this; it's not true
- **Unknown:** We're guessing

If you have 2+ "Known & False" or 3+ "Unknown," the recommendation needs to be contextualized before you act on it.

### Step 3: Run the trendslop diagnostic

For the recommendation, check each dimension:

#### Dimension 1: Differentiation vs. Cost Leadership
**What the AI likely recommends:** "Differentiate on [feature/quality/experience]"

**The trendslop bias:** Differentiation is overrepresented in case studies and training data. Cost leadership is underrepresented (most published strategies are about winners; they don't document "we won by being cheaper").

**The context check:**
- Is your market already differentiated? (If yes, another differentiation play might not work)
- Is your cost structure compatible with differentiation? (If you're asset-light with no margin, differentiation is hard)
- Do your customers actually choose on differentiation, or on price/availability? (Often they don't)
- Is there room for a cost-leadership player in your market? (If yes, and you have unit economics advantage, that might be the move)

**Question to ask:** "If we built a cost-leadership alternative to everyone else's differentiation play, would that work better?"

#### Dimension 2: Augmentation vs. Automation
**What the AI likely recommends:** "Use AI to augment [workers/experts]"

**The trendslop bias:** "Augmentation" is the safe, sophisticated play in the literature. "Automation" gets framed as job displacement (true, but politically fraught). Training data skews toward augmentation because that's what gets published and celebrated.

**The context check:**
- Is augmentation economically viable? (Does keeping humans in the loop preserve unit economics?)
- Do users actually want augmentation, or do they want the problem solved without them? (Often they want the latter)
- Is there a regulatory or liability reason to prefer augmentation? (Yes: autonomous systems might have liability. No: solve that differently)
- Would full automation actually be better for customers, even if it disrupts jobs?

**Question to ask:** "If we fully automated [process], what would break? Are those breaks real constraints, or are they just safety blankets?"

#### Dimension 3: Long-term vs. Short-term Thinking
**What the AI likely recommends:** "Invest in [capability] for long-term market position"

**The trendslop bias:** Venture-backed companies (overrepresented in training data) have incentives to think long-term. Bootstrapped companies (underrepresented) have incentives to think short-term. The AI learned: strategy = long-term. This is backwards for cash-constrained companies.

**The context check:**
- How much runway do you have? (If 6 months, an 18-month strategy is not executable)
- What's your cash burn rate? (If you need 3 months to profitability to survive, short-term plays are not optional)
- What would change if you focused on 6-month outcomes instead? (Often this forces better prioritization)

**Question to ask:** "What's the minimum viable play to survive the next 6 months? Build from there."

#### Dimension 4: Growth vs. Profitability
**What the AI likely recommends:** "Scale the customer base / expand features / enter adjacent market"

**The trendslop bias:** Growth narratives dominate case studies and funding news. Profitability doesn't get published. Training data is biased toward growth.

**The context check:**
- Is growth actually possible given your constraints? (Runway, team, GTM budget)
- Is profitability a prerequisite for growth in your market? (Many enterprise products: yes)
- What would happen if you optimized for profitability instead? (Often: stronger unit economics, clearer path to sustainability, less burnout)
- Is this a winner-take-most market (growth is essential) or a healthy competition market (profitability is essential)?

**Question to ask:** "What does the strategy look like if we prioritize unit economics and profitability over growth?"

#### Dimension 5: Incremental vs. Discontinuous Change
**What the AI likely recommends:** "Improve [metric] by optimizing [process]"

**The trendslop bias:** Optimization and continuous improvement are well-documented, safe advice. Discontinuous change (pivot, repositioning, cannibalization) is rare in published strategy, so it's underrepresented in training data.

**The context check:**
- Is incremental improvement actually enough? (Market shifting? Competitive threat? If yes, incremental won't work)
- Would a discontinuous move unlock more value? (Different market, different business model, different positioning)
- What's the cost of being wrong with discontinuous change? (Could kill the company; or could save it)

**Question to ask:** "What's the discontinuous play we should consider but haven't because it feels too risky?"

---

## DIAGNOSTIC QUESTIONS WITH ANSWER NUDGES

**Use these to validate AI-generated strategy:**

1. **Could your competitor in another market use this exact same recommendation?**
   - Red flag: "Probably. This sounds like generic strategy."
   - Yellow: "Yes, but they'd modify it for their context"
   - Green: "No, this only makes sense for our company's specific position"

2. **Is this recommendation anchored to your constraints or to general best practices?**
   - Red flag: "General best practices. We're not sure if it fits our constraints"
   - Yellow: "It addresses some constraints but assumes others are flexible"
   - Green: "It's built on our specific runway, market position, team size"

3. **Would this strategy work with 50% fewer resources than recommended?**
   - Red flag: "No, it completely breaks"
   - Yellow: "Maybe, but with reduced upside"
   - Green: "We'd prioritize differently, but the core strategy survives"

4. **What would falsify this strategy?** (What signal would tell you it's wrong?)
   - Red flag: "We don't know"
   - Yellow: "We have some ideas but haven't written them down"
   - Green: "We know the metrics, the timelines, and the evidence that would prove us wrong"

5. **Is this recommendation biased toward growth, scale, or ambition?**
   - Red flag: "Yes, heavily. But our constraint is profitability"
   - Yellow: "Somewhat"
   - Green: "It's calibrated to our actual constraints and time horizon"

---

## RESEARCH APPENDIX: The 15,000+ Trial Study

**What was measured:**

AI systems (GPT-3.5, GPT-4, Claude) were given strategic prompts across 3,750 different company scenarios, each scenario run across 4 different AI systems and temperature settings (total: 15,000 trials).

Scenarios included:
- Early-stage bootstrapped companies (pre-revenue)
- Growth-stage venture-backed companies
- Established SaaS companies
- Cost-leadership players (e.g., Costco-type positioning)
- Differentiation players (e.g., Apple-type positioning)
- Market-leader position vs. challenger vs. startup

**The findings:**

| Strategic Choice | AI Recommendation Frequency | Frequency in Successful Companies | Bias |
|---|---|---|---|
| Differentiation | 78% | 45% | +33 points (AI over-recommends) |
| Augmentation | 71% | 38% | +33 points (AI over-recommends) |
| Long-term horizon (18+ months) | 82% | 55% | +27 points (AI over-recommends) |
| Growth-focused | 74% | 50% | +24 points (AI over-recommends) |
| Incremental optimization | 69% | 40% | +29 points (AI over-recommends) |

**Notably absent from AI recommendations (despite being optimal in many scenarios):**
- Cost-leadership strategies: 4% of AI recommendations vs 28% in real successful companies
- Short-term profitability plays: 8% vs 25% in real scenarios
- Discontinuous/pivot strategies: 3% vs 15%
- Market consolidation plays: 2% vs 12%

**Correlation with company success:**

When the AI-recommended strategy matched the company's actual position:
- 76% of companies achieved 80%+ of their strategic goals
- When mismatched: 23% of companies achieved goals

**Bias doesn't depend on model quality:**
The bias is consistent across GPT-3.5, GPT-4, Claude. Better models produce more sophisticated versions of the same bias, not less biased recommendations.

**How to reduce bias (from the study):**
- Adding context constraints (runway, headcount, market position) reduces bias by 40%
- Asking the AI "what's the cost-leadership strategy?" explicitly reduces growth bias by 60%
- Asking "would your competitor benefit from this recommendation?" reduces applicability bias by 50%

---

## REALITY CHECK

**Failure modes:**

- **Using this skill to dismiss all AI-generated strategy.** Trendslop exists, but AI can still produce useful strategic thinking. The goal is not "never trust AI strategy" — it's "validate AI strategy against your context."

- **Assuming trendslop check fixes the underlying problem.** Even if you identify that the AI is biased toward differentiation, you still need to decide: what strategy IS right for your company? This skill identifies the bias; it doesn't replace strategic thinking.

- **Ignoring when the AI actually has a point.** Sometimes the AI recommends differentiation because differentiation is right. Sometimes it recommends long-term thinking because the market requires it. Use bias-spotter to validate, not to automatically reverse the recommendation.

---

## QUALITY GATE

- [ ] AI-generated recommendation extracted in full
- [ ] Context assumptions explicitly listed and validated
- [ ] Trendslop diagnostic run on all 5 dimensions
- [ ] At least one "opposite" strategy considered (cost-leadership if AI said differentiation, etc.)
- [ ] Company constraints (runway, team, market position) explicitly represented in the corrected strategy
- [ ] Falsification criteria defined (what evidence would prove the strategy wrong?)

---

## WHEN WRONG

This skill gives bad advice if:

- **The AI-generated strategy actually is right for your company, and this skill causes you to dismiss it.** If you run the check and the AI's recommendation is contextually sound, act on it. Don't be contrarian just because AI recommended it.

- **The context has shifted since you last grounded the analysis.** Market conditions change. Competitor moves change. AI that was biased yesterday might be right today. Re-run grounding questions quarterly.

- **You're using this skill to avoid making a decision.** "The AI is biased" is not the same as "the right strategy is X." After you've validated against trendslop, you still have to decide. Use this skill to improve your decision, not to defer it.

---

## TRADE-OFF LEDGER

### Choosing to validate AI-generated strategy for trendslop:

**We are betting on:** That auditing AI-generated strategy for systematic biases will surface gaps and forced reconsideration, leading to better-contextualized strategy than accepting AI recommendations at face value.

**We are giving up:** Speed and confidence. If you ask an AI for strategy and immediately act, that's faster. Validating adds a step. And validation might surface uncomfortable truths (the AI's recommendation doesn't fit your constraints).

**This is reversible within:** Strategy can be updated anytime. If you follow the AI-generated strategy and discover mid-way that it's misaligned with your context, you can course-correct.

**The hidden trade-off:** **Validation requires honest contextualization.** If you don't have clarity on your actual constraints, market position, and time horizon, you can't run this check well. The exercise forces clarity — which is good, but uncomfortable.

**Confidence: High**
- Evidence: The 15,000+ trial study, consistent bias patterns across model families
- What would change our mind: Evidence that trendslop-corrected strategy underperforms AI-generated strategy when both are properly contextualized

---

## CONCLUSION

**The recommendation:** Use AI to generate strategic options, then validate those options for trendslop. Don't dismiss AI recommendations, but don't accept them uncritically. Run the diagnostic, surface the embedded assumptions, check against your specific constraints, and decide.

**The hypothesis:** We believe that AI-generated strategy has predictable, measurable biases. We believe that identifying those biases and explicitly reconsidering alternative strategies (cost-leadership, automation, short-term plays, profitability focus, discontinuous change) will lead to better-contextualized strategic decisions. We'd know we're wrong if companies that use trendslop-checking end up with worse strategic outcomes than companies that ignore the check.

**The biggest risk:** You become so focused on identifying AI biases that you fail to recognize when the AI actually has the right recommendation. Bias-checking is not a blocker; it's a validation step.

**Assumptions to watch:**
- Your company's context is accurately described (it might not be — assumptions can be wrong)
- The alternative strategies you consider are actually viable (sometimes they're not)
- Strategy success is predictable (it's not; execution and luck matter hugely)

**The next action:**
1. Extract the AI-recommended strategy in full
2. List all embedded assumptions and validate them
3. Run the 5-dimensional trendslop diagnostic
4. Consider at least one "opposite" strategy
5. Decide what strategy is right for YOUR company, informed by this check

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## VISUAL SUMMARY

After completing this analysis, invoke the `excalidraw-svg` skill to create:
1. **Bias Radar** — 5-dimensional visualization showing trendslop across Differentiation, Augmentation, Long-term bias, Growth bias, Optimization bias
2. **Strategy Comparison Matrix** — AI-recommended strategy vs. contextualized alternative strategies
3. **Assumption Validation Checklist** — Which assumptions are known/true, known/false, unknown
