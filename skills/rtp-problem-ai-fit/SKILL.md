---
name: rtp-problem-ai-fit
description: >
  Determines whether a problem genuinely needs AI or if rules, search, and heuristics
  deliver better outcomes. Use when teams propose AI features, stakeholders say
  "use AI," or during discovery. Runs hypothesis-driven AI-necessity analysis.
imports: [first-principles]
---

# Problem-AI Fit

Determine if the problem needs AI, or if you're adding complexity without value.

> "Almost any feature has some positive return. The only question that matters is: Is this the *absolute best* use of our finite resources?" — Shreyas Doshi

---

## Quick Reference: The Lookup Table Test

Before any AI, ask: "Could a lookup table, decision tree, or regex solve 80% of this?" If yes, build that first. AI is for the remaining 20% where pattern matching across unstructured data creates genuine value.

**The diagnostic:** Describe your input-output mapping in a spreadsheet. If you can do it, you don't need AI. Examples:

```
Input: Support ticket → Output: Route to tier (L1, L2, L3)
Test: Can 3 people write routing rules in an afternoon? If yes, use rules.

Input: Product review text → Output: Sentiment (positive, negative, neutral)
Test: Can you enumerate patterns for each sentiment? If yes, regex + heuristics wins.

Input: Customer purchase history → Output: Next product to recommend
Test: Can you write: IF (customer bought X) THEN recommend Y? If yes, decision tree.
```

**Cost of being wrong:** The lookup table costs $0 in inference and is 100% debuggable. The AI solution costs $X per query and is non-deterministic. Only choose AI if the 20% unlocked by AI is worth 10x the cost.

---

## DEPTH DECISION

**Go deep if:** A team is proposing an AI feature, stakeholders say "we should use AI," or you're choosing between AI and deterministic approaches during discovery.

**Skim to the AI-Necessity Test if:** You've already decomposed the atomic operation and just need the four-question test.

**Skip if:** Architecture decisions are already final, you're deciding between different AI approaches (use invisible-stack instead), or the problem is clearly deterministic (LOOKUP/TRANSFORM on clean data).

---

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this assessment in?**
> 1. **Word Document** — Formatted report with embedded visuals. Best for sharing with stakeholders.
> 2. **Presentation** — Slide deck with key findings. Best for meetings and reviews.
> 3. **Both** — Full report + summary deck.
>
> *Default if no preference: Word Document.*

Follow the [Universal Deliverable Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## Step 0: Ground in the Customer's Reality

Before touching any AI assessment, establish what's actually true about the problem. This prevents the most common failure: starting with "we have AI" and searching for a problem to attach it to.

**Ask the user these questions — don't proceed without answers to at least the first four:**

> **1. Who exactly is the customer?**
> Not "businesses" or "users." Be specific: "Series B SaaS companies with 50-200 employees whose support teams handle 500+ tickets/week." The narrower the segment, the clearer the fit signal.

> **2. What problem do they have — in their words, not yours?**
> How would the customer describe this pain to a colleague over coffee? If you can't state it in their language, you don't understand it yet.

> **3. How do they solve it today?**
> Every problem has a current solution — even if that solution is "they suffer through it" or "an intern does it manually." The current solution is your real competitor, not other AI products.

> **4. How painful is it? Where does it rank?**
> Use the Customer Problem Stack Rank: ask them to list their top 5 problems. Where does this one fall? If it's #4 or #5, solving it won't prevent churn or drive adoption. You're solving a "nice to have."

> **5. Would they pay for a solution? How do you know?**
> Not "would they say yes in a survey" — that's cheap talk. Have they tried to solve this themselves? Have they spent money on workarounds? Skin-in-the-game signals matter more than stated intent.

> **6. What are we saying YES to by pursuing this — and what are we saying NO to?**
> This is the most important question. "By investing engineering in an AI-powered X, we are choosing NOT to invest in ___." If you can't fill in the blank, you haven't thought about opportunity cost.

**Why this comes first:** Teams skip this step because it feels "obvious" or "already done." It almost never is. The customer ground determines whether the rest of the analysis matters at all. A perfect AI-fit assessment for a problem nobody cares about is worthless.

---

## Step 1: Run First-Principles Decomposition

Import and execute `thinking-core/first-principles`. Get the atomic operation and its classification (LOOKUP, TRANSFORM, CLASSIFY, GENERATE).

**The key question:** What is the ONE fundamental operation this feature does? Strip away vendor features, marketing language, and implementation details. Find the atom.

---

## Step 2: Apply the AI-Necessity Test

For each atomic operation, ask these four questions:

```
Q1: Does the output require JUDGMENT (not just processing)?
    Judgment = weighing incomplete evidence, handling ambiguity,
    making subjective assessments.
    If NO → rules or deterministic code. Stop here.

Q2: Is the judgment LEARNABLE from examples?
    Can you show 100 input-output pairs and a human would see the pattern?
    If NO → you need human-in-the-loop, not AI. Stop here.

Q3: Is the cost of being WRONG acceptable?
    What happens when the AI makes a mistake? Is it recoverable?
    If NO → you need deterministic guarantees. AI can assist but
    not decide. Design for human override.

Q4: Is the VOLUME high enough to justify the infrastructure?
    AI infrastructure has fixed costs (embedding pipelines, eval suites,
    monitoring). These costs need volume to amortize.
    If NO → manual process or simple heuristics. Revisit when volume grows.
```

### Score the fit

```
4 YES answers → Strong AI fit. Proceed to architecture decisions.
3 YES answers → Conditional fit. The missing YES is your risk factor.
               Document it and design mitigations.
2 YES answers → Weak fit. Consider whether the problem is worth
               the AI infrastructure cost. Often it isn't.
0-1 YES      → Not an AI problem. Build with deterministic tools.
               This is not a failure — it's good product judgment.
```

---

## Step 3: State Your Hypothesis

This is where most teams stop — they have a score and they move on. But a score is not a decision. A decision requires a hypothesis that can be tested and proven wrong.

**Write the hypothesis:**

```
HYPOTHESIS: We believe [AI approach — e.g., "an LLM-powered draft response system"]
  will [expected outcome — e.g., "reduce average support resolution time by 40%"]
  for [specific customer segment — from Step 0]
  because [reasoning — e.g., "70% of tickets follow patterns learnable from
  our 50K historical ticket-resolution pairs, and the remaining 30% benefit
  from AI-generated first drafts that agents edit"].

IF TRUE, we expect to see:
  • [Leading indicator — observable in days/weeks]
  • [Lagging indicator — observable in months]

IF FALSE, we'd observe:
  • [Counter-signal — e.g., "agent override rate exceeds 60%"]
  • [Counter-signal — e.g., "resolution time stays flat or increases"]

DAMAGE IF WRONG:
  • [Specific cost — e.g., "$200K in infrastructure + 6 months of engineering"]
  • [Opportunity cost — e.g., "We delayed the self-service portal that would have
    reduced ticket volume by 25%"]
  • [Reversibility — e.g., "Two-way door: we can revert to manual workflow in 1 week"]

PIVOT TRIGGER:
  If [specific metric] hits [threshold] by [date], we stop and redirect to
  [alternative approach].
```

**Why this matters:** The hypothesis frame is what separates "we should use AI" (an opinion) from "we believe AI will produce X outcome because Y, and we'd know we're wrong if Z" (a testable bet). The first is what junior PMs produce. The second is what senior PMs produce.

---

## Step 4: Surface Your Assumptions

Every hypothesis rests on assumptions. Most are invisible until you force them into the open. For each assumption, rate the evidence:

| Assumption | Evidence Level | Load-Bearing? | How to Test |
|---|---|---|---|
| *e.g., "Customers want faster responses, not just accurate ones"* | Informed (3 interviews, no quantitative data) | Yes — if they want accuracy over speed, our AI approach is wrong | Survey 50 customers: rank speed vs. accuracy vs. cost |
| *e.g., "We have enough labeled training data (50K examples)"* | Validated (data exists in warehouse) | Yes — without data, model quality collapses | Audit: are labels consistent? Run inter-annotator agreement |
| *e.g., "Support agents will trust AI-generated drafts"* | Assumed (no evidence either way) | Yes — if agents don't trust it, adoption is zero | Pilot with 5 agents for 2 weeks, measure edit rate |
| *e.g., "Inference costs will be under $0.02/ticket"* | Informed (based on current GPT-4o pricing) | Moderate — affects unit economics but not viability | Run 1000 test tickets, measure actual cost |

**Evidence levels:**
- **Validated:** Data exists, tested, confirmed
- **Informed:** Expert judgment, directional data, analogous evidence
- **Assumed:** Seems reasonable but no evidence
- **Unknown:** We're guessing

**The rule:** Any assumption rated "Assumed" or "Unknown" that is also "Load-bearing" is a risk you must address before committing resources. Either test it or explicitly accept the risk.

**Ask the user:** *"Which of these assumptions makes you most nervous? That's probably the one to test first."*

---

## Step 5: Expanded Fit Assessment (Optional — For Deep Dives)

When the four-question test produces a borderline score (2-3), use this 16-point detailed assessment for more precision.

Score the problem 0-4 on four dimensions:

**Dimension A: Input Variability**
- 0 = Fixed inputs (same format every time). Rule engine handles this.
- 1 = Mostly fixed with occasional variants. Light heuristics work.
- 2 = Variable but bounded (20-100 distinct patterns). Rules + fallback.
- 3 = Highly variable, hard to enumerate. Heuristics start failing.
- 4 = Open-ended variability (millions of distinct patterns). Pattern matching needed.

**Dimension B: Output Judgment Required**
- 0 = Pure lookup (answer exists in table). No judgment.
- 1 = Simple transformation (reformat, combine fields). No judgment.
- 2 = Light judgment (choose from 5 options based on clear rules).
- 3 = Moderate judgment (weigh tradeoffs, handle ambiguity).
- 4 = Deep judgment (nuanced reasoning, subjective assessment).

**Dimension C: Data Availability**
- 0 = No labeled data exists. You're guessing.
- 1 = <100 labeled examples. Too small to train.
- 2 = 100-1000 examples. Possible but risky.
- 3 = 1000-10K examples. Good for simple models.
- 4 = 10K+ clean labeled examples. Ready for sophisticated models.

**Dimension D: Error Tolerance**
- 0 = Zero tolerance (one mistake breaks the system). Must be deterministic.
- 1 = Very low (errors accumulate). Need high accuracy (>99%).
- 2 = Moderate (errors are recoverable, costly). Accuracy >90%.
- 3 = High (errors are local, user can override). Accuracy >80%.
- 4 = Graceful degradation (system works acceptably even with errors).

**Scoring:** Add all four dimensions. Max score = 16.

```
13-16 = AI-native problem. Proceed confidently.
 9-12 = Strong AI fit. Build with care.
 5-8  = Weak fit. Rules + heuristics first.
 0-4  = Not an AI problem. Don't use AI.
```

**Assumption check:** After scoring, ask: *"Which dimension score am I least confident about? What evidence would change that score by ±1?"* A swing of 1 point on a borderline assessment can change the recommendation entirely.

> **VISUAL: Invoke `excalidraw-svg` to generate an AI Fit Gauge** — a semicircular gauge from 0 (left, red: "Not AI") through 8 (center, amber: "Weak Fit") to 16 (right, green: "AI-Native"). Plot the score as a needle. Label the four zones. Below the gauge, show the four dimension scores as a stacked bar.

---

## Step 6: Check for AI-Washing Signals

Even with strong fit, watch for these red flags. Each one is a hypothesis that needs testing, not a disqualifier:

**"Our competitors are using AI for this."**
- *Assumption:* Competitors are getting value from AI, not just marketing it.
- *Test:* Can you find evidence of actual user outcomes, or just press releases?
- *If untested:* You might be following a leader into a dead end.

**"The executive team wants AI features."**
- *Assumption:* Executive interest reflects customer demand, not technology fascination.
- *Test:* Show exec team the customer problem stack rank. Does AI solve a top-3 problem?
- *If untested:* You're building for your org chart, not your customers.

**"We already have the model/infrastructure."**
- *Assumption:* Existing infrastructure creates a cost advantage that changes the fit calculation.
- *Test:* Would you build this infrastructure FROM SCRATCH to solve this problem? If not, you're rationalizing sunk costs.
- *If untested:* Sunk cost fallacy — the existence of infrastructure doesn't create user problems.

**"AI makes it more scalable."**
- *Assumption:* Scale is the binding constraint, not reliability or cost.
- *Test:* What's the current volume? Is the bottleneck really scale, or is it quality, speed, or cost? Sometimes a 5-person team handles the volume fine.
- *If untested:* Scale without reliability is a liability, not an asset.

---

## Step 7: See the Decision in Context

Before finalizing your assessment, view the decision through five lenses. This prevents tunnel vision — the tendency to evaluate AI fit in isolation from the business reality.

| Lens | The Question | Signal Color |
|------|-------------|-------------|
| **Customer** | Does the AI approach fit their existing workflow, or require behavior change? Behavior change is expensive and slow. | Green = fits naturally; Red = requires adoption campaign |
| **Business** | What's the unit economics at scale? Include monitoring, eval pipelines, retraining, failure-mode support. Compare to the deterministic alternative. | Green = clear ROI; Red = economics don't close |
| **Market** | First-to-market or fast-following? If following, AI must be meaningfully better — marginal improvements don't drive switching. | Green = clear differentiation; Red = me-too |
| **Team** | Do we have ML/AI expertise to build AND maintain? "We'll hire someone" is an assumption. AI maintenance = 3-5x build cost. | Green = team ready; Red = capability gap |
| **Ethics** | What happens when AI makes a mistake at scale? Who is harmed? Would we be comfortable if the failure was on the front page? | Green = bounded harm; Red = vulnerable populations affected |

**Ask the user:** *"Which of these lenses reveals the biggest risk you haven't fully thought through?"*

> **VISUAL: Invoke `excalidraw-svg` to generate a Five-Lens Radar** — pentagon chart with each lens as an axis scored Green/Amber/Red. Shows at a glance which lenses support the AI decision and which raise concerns.

---

## When ML is Overhead: Real Examples

Teams regularly over-engineer with ML when simpler solutions suffice. Pattern recognition:

**Example 1: Ticket Routing**
- Proposal: "Use ML to route support tickets to the right team."
- Reality: 90% of routing can be done with: IF keyword contains "billing" THEN tier-2, ELSE IF keyword contains "account" THEN tier-1.
- ML investigation: 6 months, $200K, 87% accuracy.
- Rules solution: 200-line script, $0 cost, 92% accuracy (+ human tier-3 fallback).
- Outcome: Rules won. ML team disbanded.
- **The hidden assumption that failed:** "Ticket routing requires understanding context." It didn't — it required matching keywords.

**Example 2: Lead Scoring**
- Proposal: "Use ML to predict which leads will convert."
- Reality: Sales team already knows: company size + industry + engagement = conversion.
- ML investigation: 4 months, feature engineering, retraining pipeline, 74% AUC.
- Heuristic solution: (company_size=enterprise) AND (industry=tech) AND (opened_email OR clicked_link) = score. 2 weeks.
- Outcome: Heuristic deployed. ML model never shipped. Sales team adjusted heuristic 3x/year based on results. Works better.
- **The hidden assumption that failed:** "Conversion patterns are too complex for rules." They weren't — 3 variables explained 80% of variance.

**Example 3: Fraud Detection**
- Proposal: "Use deep learning to detect fraudulent transactions."
- Reality: Fraud pattern: unusual amount + unusual location + high velocity = flag.
- ML investigation: 9 months, false positive rate 15%, costs $500K/year in infrastructure.
- Rule solution: IF (amount > 3x usual) AND (location != home country) THEN flag. 99% accuracy, $5K/year.
- Outcome: Rules launched. ML project shelved. Fraud team is happy.
- **The hidden assumption that failed:** "Fraud patterns are adversarial and evolving." At this company's scale, they weren't — simple rules caught 99%.

**Red flags you're over-engineering:**

1. **Accuracy requirement is binary.** "Yes/no" decisions don't benefit from ML confidence scores. Rules suffice.
2. **Input space is enumerable.** <1000 distinct categories? Write rules, not models.
3. **Rules change rarely.** Domain expert can write rules and they don't change >2x/year? Build the rules engine.
4. **Domain expert can write rules in an afternoon.** If a subject-matter expert can articulate decision logic clearly, that's a signal: this is not a machine learning problem.
5. **The "accuracy" story is exaggerated.** Team says "AI will be 95% accurate" but hasn't validated baseline. Rules might be 90% and cost 10x less.
6. **Data labeling is expensive or inconsistent.** If ground truth is hard to establish (subjective, requires expert review), ML quality will be limited.
7. **The problem hasn't evolved much in 2+ years.** If the rules/patterns haven't changed, it's not a learning problem. It's a lookup problem.

---

## REALITY CHECK

- Approximately 60-70% of "AI feature" proposals in enterprise settings decompose to LOOKUP or TRANSFORM problems that don't need AI. This is a rough heuristic from practitioner experience, not a formal study — but it's directionally useful.
- The remaining proposals that genuinely need AI usually need it for a narrower scope than originally proposed. "AI-powered support" becomes "AI-assisted draft response for human review."
- Teams that score 2/4 on the AI-necessity test often ship anyway due to organizational pressure. Track the outcomes. They almost always underperform the simpler alternative on user satisfaction and cost efficiency.
- Problem-AI fit can change over time. A problem that scores 1/4 today (low volume) might score 4/4 in six months (volume growth). Build the rules engine now, plan the AI migration for later. State this as a hypothesis: "We believe volume will reach [threshold] by [date], at which point AI becomes justified."

---

## THE TRAP

**The mistake:** Assuming AI is the right approach because the problem involves text, images, or unstructured data. Teams conflate "data that looks like AI input" with "a problem that requires AI."

**Why it feels right:** AI is a general-purpose technology. It CAN process text, images, and unstructured data. The fact that it can doesn't mean it should. A screwdriver can open a paint can, but that doesn't make it the right tool.

**The cognitive bias:** Maslow's Hammer — "if all you have is an LLM, everything looks like a generation problem." Reinforced by organizational incentives: AI features get more funding, more press, and more executive attention than infrastructure improvements.

**The cost:** AI-washing. You ship a feature that's slower (API latency), more expensive (per-token costs), less reliable (hallucination risk), and harder to debug (non-deterministic outputs) than the rules engine it replaced. Users don't care that it uses AI. They care that it works.

**The deeper trap:** Even this skill can create false confidence. Scoring 4/4 on the AI-necessity test doesn't mean you should build it — it means AI is technically appropriate. You still need to ask: Is this the highest-leverage use of our engineering time? (LNO framework: is this a Leverage decision?) Is the opportunity cost acceptable? Would solving a different problem create more value?

---

## QUALITY GATE

Before finalizing your assessment, verify:

- [ ] The customer ground is established — you know WHO has the problem and HOW PAINFUL it is
- [ ] The atomic operation has been decomposed using first-principles
- [ ] All four AI-necessity questions have been answered with evidence (not assumptions)
- [ ] A hypothesis has been stated — with IF TRUE, IF FALSE, and PIVOT TRIGGER
- [ ] Load-bearing assumptions have been named and evidence-rated
- [ ] The score has been calculated and the implications acknowledged
- [ ] Red flags for AI-washing have been checked (even if score is high)
- [ ] The decision has been viewed through all five lenses (customer, business, market, team, ethics)
- [ ] If the score is 0-2, the team has explicitly decided whether to proceed and documented why
- [ ] The opportunity cost of this investment has been named — what are we NOT building?

---

## WHEN WRONG

This skill gives bad advice when:

- **The problem is at the frontier of what's possible with AI**, and the four-question test is too conservative. Research applications may need AI even with low scores. *Assumption to check: Are we doing research or building a product? Research tolerates different risk profiles.*

- **The primary goal is learning, not production value.** Building an AI feature to develop team capabilities is a valid strategy even if rules would suffice for the current use case. *Assumption to check: Is the organization willing to treat this as a learning investment with uncertain ROI?*

- **The competitive landscape demands AI as table stakes.** If every competitor has AI-powered search and you don't, the fit test is less relevant than market positioning. *Assumption to check: Do customers actually use competitors' AI features, or is it just marketing?*

- **The user experience improvement from AI is dramatic enough to justify the cost premium.** Sometimes a 10x better experience is worth 10x the infrastructure cost. *Assumption to check: Is the experience improvement real and measurable, or projected and hoped-for?*

- **You're applying this skill too early.** If the problem hasn't been decomposed yet (use first-principles first) or you don't know who the customer is, this skill will produce a technically valid but strategically meaningless assessment.

---

## TRADE-OFF LEDGER

After completing the assessment, fill this out — it's where the thinking becomes a decision:

```
BY CHOOSING [AI / Rules / Hybrid / Don't Build]:
  We are betting on: [the core bet — what must be true]
  We are giving up: [the opportunity cost — what we can't build instead]
  This is reversible within: [timeframe] / This is a one-way door because [reason]

THE HIDDEN TRADE-OFF:
  [The non-obvious consequence — e.g., "Choosing AI means we now need an
  eval pipeline, which means hiring an ML engineer, which means 3-month
  recruiting delay before we can even start"]

CONFIDENCE: [High / Medium / Low]
  What would change our mind: [specific evidence or signal]
```

---

## CONCLUSION

Every Problem-AI Fit assessment MUST end with a clear position:

**1. THE RECOMMENDATION** — "Build with AI" / "Build with rules" / "Build hybrid" / "Don't build this at all" / "Gather more evidence before deciding"

**2. THE HYPOTHESIS** — "We believe [approach] will [outcome] because [evidence]. We'd know we're wrong if [signal] within [timeframe]."

**3. THE KEY TRADE-OFF** — "This means we're prioritizing X over Y because Z."

**4. THE BIGGEST RISK** — "The biggest risk is ___ and we'd mitigate it by ___."

**5. ASSUMPTIONS TO WATCH** — The 2-3 critical assumptions with the weakest evidence, and how/when to test them.

**6. THE NEXT ACTION** — "The next step is ___ by ___ [person/role] by ___ [date]."

Do not leave the user with "here's some analysis, figure it out." Pick a direction. State your confidence. Name what would change your mind.

---

## NATURAL FLOW INTO ADJACENT SKILLS

This skill connects forward to:

- **ai-use-case-readiness** → If AI fit is confirmed, assess WHAT LEVEL of AI (rules → copilot → agent → autonomous). That skill picks up where this one ends.
- **invisible-stack** → If you're choosing BETWEEN AI approaches (not whether to use AI at all).
- **determinism-compass** → If the analysis reveals the problem needs deterministic guarantees with AI assistance.
- **cost-model** → If the hypothesis needs economic validation before committing.

---

## DELIVERABLE FORMAT

The output should be polished enough to forward to a VP without editing.

### Visual Outputs (Excalidraw SVGs)

Generate these visuals inline. A stakeholder should understand the recommendation from visuals alone.

| Visual | When to Generate | What It Shows |
|--------|-----------------|--------------|
| **AI-Necessity Scorecard** | Always | The 4-question test as a visual checklist with Yes/No and score |
| **AI Fit Gauge** | Always | The 16-point score plotted on a gauge (0-4 red, 5-8 amber, 9-12 green, 13-16 deep green) |
| **Five-Lens Radar** | When doing comprehensive analysis | Pentagon chart, each axis Green/Amber/Red |
| **Trade-Off Balance** | When the hidden trade-off is non-obvious | Two sides of a scale: what we gain vs. what we give up |
| **Decision Tree** | When the lookup table test is relevant | Visual decision tree: "Can a lookup table solve it?" → branches to AI path vs rules path |

**Rule:** If in doubt, generate the visual. Text-based frameworks are forgettable. Clean SVGs with the assessment plotted are instantly understood and shareable.

### Document Output

For comprehensive assessments, produce a formatted document (`.docx` or `.pdf`):

1. **Executive Summary** (half page): Recommendation, hypothesis, key trade-off, next action
2. **Visual Story** (1 page): The SVGs above, captioned, telling the story without text
3. **Detailed Assessment** (2-3 pages): Full analysis following the conclusion protocol
4. **Assumptions & Risks** (half page): Load-bearing assumptions with test plans
5. **Examples/Precedents** (half page): Similar cases that went right or wrong

### Inline Output

For quick conversation answers: the recommendation, the hypothesis, one or two visuals (AI Fit Gauge + Five-Lens Radar at minimum), and the assumptions to watch.

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md` for all SVG generation.

---

## GENERATE THE DELIVERABLE

Once the analysis is complete, use this prompt to produce the final output:

```
OUTPUT GENERATION PROMPT:

You have completed the Problem-AI Fit assessment. Now produce the deliverable.

FORMAT: [Word Document / Presentation / Both — as chosen by user]

INSTRUCTIONS:
1. Read the full analysis above.
2. Write the Executive Summary first — recommendation as the first sentence.
3. Generate Excalidraw SVG visuals for:
   - AI Fit Gauge (always — shows the 16-point score)
   - AI-Necessity Scorecard (always — the 4-question test visual)
   - Five-Lens Radar (if comprehensive analysis)
   - Trade-Off Balance (if the hidden trade-off is non-obvious)
   - Decision Tree (if lookup table test is relevant)
4. Structure following the Universal Deliverable Protocol.
5. Plain language throughout — no unexplained jargon.
6. Before delivering:
   - Grammar check all text.
   - Verify recommendation is consistent across all sections and visuals.
   - Confirm all scores populated.
   - Check visuals match text.
7. Deliver to workspace folder.

QUALITY BAR: Forward-ready for a VP. Actionable for an engineer. Clean for a designer.
```

---

## WORKFLOW HANDOFF

When continuing to a downstream skill (ai-use-case-readiness, invisible-stack, determinism-compass, cost-model), **automatically generate a markdown handoff file** carrying forward:
- Customer grounding (so the next skill skips these questions)
- The AI fit recommendation and score
- The hypothesis with IF TRUE / IF FALSE
- Critical assumptions with evidence ratings
- Open questions for the next skill

Follow the Markdown Handoff format in the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 9.

File naming: `problem-ai-fit-handoff-[use-case-slug].md`
