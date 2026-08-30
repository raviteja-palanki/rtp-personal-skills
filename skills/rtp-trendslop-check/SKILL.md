---
name: trendslop-check
version: v1.6_latest
description: 'Catch when AI-generated strategy defaults to trendy advice instead of context-specific strategy. Grounded in a real, named HBR study (Romasanta, Thomas & Levina, Mar 2026): across ~15,000 simulations on 6 frontier models, LLMs showed consistent bias on 6 of 7 classic strategic tensions: differentiation over commoditization (96%), augmentation over automation (93%), plus long-term, collaboration, radical, and decentralization. The one axis with NO bias: exploration vs. exploitation. The counterintuitive finding: adding rich context shifts the bias only ~11%; reversing which option is listed first shifts it ~19%. Prompting harder doesn''t fix this. Use when bootstrapping strategy, running multi-scenario planning, or validating AI-generated recommendations.'
imports: [first-principles, bias-spotter]
---

# Trendslop Check

When you ask an AI to generate strategy, it produces sophisticated-sounding advice. It's also biased in predictable, measurable ways.

A March 2026 *Harvard Business Review* study — Angelo Romasanta (Esade), Llewellyn D.W. Thomas (University of Sydney), and Natalia Levina (NYU Stern), "[Researchers Asked LLMs for Strategic Advice. They Got 'Trendslop' in Return](https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return)" — ran roughly 15,000 simulations across six frontier models (GPT-5, Claude, Gemini, Grok, DeepSeek, Mistral) and seven classic strategic tensions. Six of the seven showed a strong, consistent directional bias across every model tested. Only one — exploration vs. exploitation — showed real variance, meaning the other six are the load-bearing finding, not the whole picture. The authors coined the term **trendslop**: LLMs recommend the side of a strategic tension that sounds better in a management article, not the side that fits your actual constraints.

This is not because LLMs are stupid. The researchers point to how training data assigns emotional valence to words — "augmentation" appears in hopeful contexts, "automation" in anxious ones, regardless of which is economically right for a given company. The model isn't reasoning about your P&L; it's predicting the next token in a management-buzzword pattern.

When you ask an LLM "What's our strategy?" it gives you the strategy that's most common — and most positively framed — in its training data. This is almost never the strategy that's right for your specific context.

> "The AI gave us beautiful strategic thinking. When we shipped it, it didn't match our market position or our constraints. The strategy was right for a different company." — Real quote from a PM

---

## Quick Reference: The Trendslop Signals

When you see these patterns in AI-generated strategy, trendslop is at work. The first two carry precise, verified figures from the HBR study; the rest are confirmed *directionally* biased by the same study but without a disclosed exact percentage in what's publicly available (the primary text is paywalled — see Research Appendix for the sourcing on each):

1. **Differentiation bias (◆ 96% of runs):** The AI recommends "differentiate on X" regardless of whether your market is already differentiated, whether your cost structure allows it, or whether customers actually care. Real companies built empires on the opposite call — Walmart, Costco, Aldi, Ryanair all chose cost leadership.

2. **Augmentation bias (◆ 93% of runs):** The AI recommends "use AI to augment workers" even when the economics or user acceptance require automation. Training data frames "augmentation" hopefully and "automation" anxiously — the model is reflecting that valence, not your unit economics.

3. **Long-term bias (◆ directionally confirmed, exact % not disclosed):** The AI recommends strategic plays on 18-month horizons when your business has 6 months of runway and needs immediate revenue.

4. **Radical-over-incremental bias (◆ directionally confirmed):** The AI recommends bold, discontinuous moves ("pivot," "disrupt") over disciplined incremental improvement, even when a tighter onboarding flow or clearer pricing page is the higher-probability win.

5. **Growth bias (not one of the study's 7 tested tensions — a related pattern, not independently quantified):** The AI recommends scaling and expanding features when profitability, stability, or market consolidation is the actual play. Flagged here because it's a common real-world variant of the same underlying mechanism (positive-valence vocabulary), but don't cite it with the same confidence as signals 1-4.

**Two more the study found, worth knowing even though this skill doesn't build full diagnostics for them:** Collaboration is favored over Competition, and Decentralization over Centralization — both directionally biased across the same six models. **The one exception:** Exploration vs. Exploitation showed real variance between models — it's the one classic tension where trendslop did *not* show up. That itself is a useful fact: it means the bias isn't "AI always picks the exciting answer," it's specific to six particular axes.

**The detection test:** Ask yourself: "Would the AI give this exact same recommendation to our direct competitor in a different market?" If the answer is yes, it's trendslop.

**The counterintuitive fix that isn't "add more context":** the study's most practically important finding is that better prompting barely moves this. Requesting deeper analysis shifted the bias ~2%; adding rich, company-specific context shifted it ~11%. The single biggest lever was almost mechanical: reversing which option the model reads first shifted the bias ~19% — more than 4x what "explain your reasoning" achieves. Don't assume a longer, more detailed prompt fixes trendslop; it doesn't, much.

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

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
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

## TEACHING CASE: A HEADLINE NUMBER WHOSE COMPONENTS CANNOT BE CHECKED

A large asset manager reported roughly **$500 million** of tracked AI value, composed of exactly four categories. The categories are the finding, not the total.

| Bucket | What it counts | Can it be checked? |
|---|---|---|
| **Cost avoidance** | Spend that did not happen | **No.** Counterfactual by construction |
| **Shareholder value creation** | At a client-owned mutual, value returned to fund investors | **No.** The measurement is never defined |
| **Risk reduction** | Losses that did not occur | **No.** Counterfactual by construction |
| **Operational efficiency** | Output against a before-and-after baseline | **Yes.** The only one |

**Three of the four are unfalsifiable, no per-bucket figure is disclosed, and the sum is reported as one number.** Nothing here is fabricated. Every bucket is a legitimate category of value that finance teams really do track. **The problem is that the composite cannot be audited and is presented as though it can.**

**The check this produces, and it generalizes past AI:** when a headline value figure is a sum of categories, **ask for the split before accepting the total.** If the split is not disclosed, ask which buckets are counterfactual. A number that is mostly "losses that did not occur" is a modelling assumption wearing a dollar sign.

**How to cite such a figure honestly if you must.** Name the four buckets, say that three are counterfactual, and say the split was not disclosed. **That sentence is more useful to a reader than the $500 million**, because it tells them what kind of claim they are holding.

**The related signal on the same page.** The same source noted the firm was piloting a few dozen applications and deliberately holding most back until the kinks were worked out. **A large value figure standing next to a small deployed footprint is a prompt to ask which one the number describes.**

*(Source: HBR, "Investing in AI Payoffs at Vanguard," Oct 2025 — ◆ single company, self-reported by its CIO and chief data analytics officer. **No per-bucket split and no method for any bucket is disclosed**, and the firm is client-owned, so "shareholder value creation" means something different there than at a listed company. **Roughly a year old now.** The four-bucket structure is the reusable part; the $500 million is not a number to repeat. Falsifier: a disclosed split showing operational efficiency, the one checkable bucket, carrying most of the total.)*

## TEACHING CASE: TWO NUMBERS FROM ONE ARTICLE, BOTH BROKEN IN DIFFERENT WAYS

A 2026 piece arguing that a new organizational form is replacing the ordinary startup carried two figures. Both are the kind that travel, and each fails a different check.

**Number one, the unit mismatch.** *"It took Netflix years to get to 1 million users, but it took ChatGPT just five days."*

**This is a category error dressed as a comparison.** Netflix's early million were paying subscribers of a DVD-by-mail service carrying warehouse, postage and inventory economics. ChatGPT's five-day million were free signups on a web page. **Provisioning is not usage, and a free signup is not a subscriber.** The two numbers have different units, so the ratio between them means nothing. Population unstated on both sides.

**The check it fails:** before comparing two figures, confirm they count the same kind of thing. A comparison across units is not a fast fact, it is not a fact at all.

**Number two, the out-of-order sequence.** A bookkeeping startup was cited at *"as little as $23,000 in ARR per FTE before filing for bankruptcy in January 2025."*

The date is defensible. **The implied story is out of order, and the order is what carries the argument.** The company announced closure and ceased service on 27 December 2024. It was acquired three days later, on 30 December. The Canadian bankruptcy filing came in January 2025. **So the platform was acquired and revived rather than liquidated**, which is close to the opposite of the "low efficiency ratio kills you" reading the figure is supplying. "As little as" is also doing undisclosed work with no stated method.

**The check it fails:** when a number is offered as the cause of an outcome, reconstruct the sequence of events before repeating it. A correct date attached to a wrong sequence is more persuasive than a wrong date and harder to catch.

**The general rule both cases produce.** These two sit either side of the same line. **The first number is wrong in its units. The second is right in its facts and wrong in its story.** A source-checking pass that only verifies figures against records catches the second and misses the first entirely, because both halves of the Netflix comparison are individually true.

*(Source: MIT Sloan, "Why AI-driven enterprises are the future of entrepreneurship," Jul 2026. Both corrections were checked against primary records during the note pass — ⚠ the article's figures are single-source with no stated method. **Neither number should travel from this corpus.** The ARR-per-FTE metric itself is a reasonable idea and is carried in `rtp-ai-product-metrics` without these two illustrations.)*

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

## WORKED EXAMPLES (5) — statistics and claims that don't survive a source check

Five distinct failure patterns, each pulled from a real sweep. Each one is a different way a number or a claim can look solid and not be. Use them as a checklist of shapes, not a single test to run once.

### Example 1: a statistic that means its own opposite, published under a top-tier masthead

The best short demonstration of why vague attribution gets rejected on sight, and why "it came from a credible outlet" is not a check.

**The sentence, as published in August 2026:**

> "Different studies tell the same dismal story: Somewhere between 70% and 95% of AI pilots actually make it to scale in organizations."

**Read it literally: 70% to 95% of pilots succeed.** That is an excellent story, and it contradicts the word "dismal" three words earlier. The intended claim was almost certainly that 70% to 95% **fail** to reach scale. Somewhere between the interview, the transcription and the edit, a negation was lost.

**Three separate failures stacked in one sentence, and each one is a check this skill already runs:**

1. **"Different studies" is the vague attribution.** No study named, no year, no population, no definition of a pilot or of scale.
2. **A 70-to-95 range across unnamed sources is not measurement spread.** A gap that wide almost certainly reflects incompatible definitions of "pilot" and "scale" rather than genuine variation in findings.
3. **Nobody caught the inversion**, because a number in a quote from a credentialed source reads as a fact rather than as a claim to check. The masthead did the verification work in the reader's head.

**The ruling, and it is stricter than people expect: do not quote this figure in any form, including corrected.** A corrected version is still an unnamed-source range with undefined terms. Fixing the negation fixes the grammar and leaves the evidence problem exactly where it was.

**The transferable check.** When a statistic arrives inside a quote from an authoritative person, run the same two tests you would run on an anonymous blog post: **can I name the study, and does the number's direction match the sentence around it?** The second test costs three seconds and it is the one nobody runs.

*(Source: MIT Sloan Management Review, "6 questions to guide your AI strategy," 3 Aug 2026 — ⚠, attributed directly to the interviewee. The article carries two figures in total; this is one of them and the other is a task-level time saving with no organizational denominator. Recorded here as a teaching case, not as evidence about pilot-to-scale rates.)*

### Example 2: the cited number and the source's own disclosed number are not the same measurement

A July 2026 sweep flagged a "41% sepsis mortality reduction" statistic, cited in an HBR interview about a hospital system's AI deployment. Checking it against the primary source, the health system's own press release on the same deployment, found no mortality figure at all. The press release attributes its outcome improvement to multiple initiatives together, including a human rapid-response team, and separately discloses a financial stake in the AI vendor that the HBR interview does not mention. A real 18% figure does exist in the published literature, but it belongs to a different study run at different hospitals. It is not a smaller, more honest version of the 41%; it is an unrelated number that happens to sound like a fact-check result.

**The rule:** when a cited number doesn't appear in the source organization's own disclosure, check whether that organization discloses an *adjacent* metric before concluding the number is simply unverified. Silence and a substituted metric look identical at a skim.

**The mechanism:** organizations that deploy AI clinically or operationally tend to measure and publish process metrics, like time-to-treatment, alert volume, or response time, because those are what their own systems capture. An outcome metric like mortality often gets attached later, by an interviewer, a secondary article, or the vendor's marketing, and it can migrate in from a different study entirely because it fits the narrative.

**Where this rule is wrong:** if the organization's own primary disclosure states the identical figure the secondary source cites, there's no contest: the citation checks out and this pattern doesn't apply. It also doesn't apply if the organization discloses nothing at all on the topic; that's a plain unverified claim, not a contested one, and gets the ordinary unverified tag instead of this specific check.

*(Tier: ⚠ for the 41% figure. It did not survive comparison against the primary source. Population: one health system's single AI deployment, per the interview; the source press release covers the same deployment but names no mortality figure. The 18% figure is ⚠ pending its own primary-source check and, regardless of its own validity, is not evidence for the 41% claim: different study, different hospitals. Primary source URL: [VERIFY], not confirmed at time of writing.)*

### Example 3: an uncited statistic is not more forgivable than a wrong one

A strategy article built a load-bearing argument on "6,000+ executives, 90% report no measurable productivity gain," attributed to NBER. No footnote, no linked paper, no working-paper number appears anywhere in the piece.

**The rule:** treat an uncited statistic as at least as disqualifying as a statistic with a citation that turns out to be wrong, not as a lesser offense. A wrong citation at least gives you something to check and reject. An uncited one gives you nothing: you cannot verify the population, the method, or whether the study exists at all.

**The mechanism:** naming a credible-sounding institution, such as NBER, McKinsey, or Gartner, does real persuasive work even with no link attached, because the reader's trust in the institution substitutes for the citation trail that was never provided. The number borrows credibility it hasn't earned.

**Where this rule is wrong:** if a citation exists elsewhere in the same document, an endnote, an appendix, a "sources" section at the bottom, this isn't the failure. Check the whole document before flagging a sentence in isolation as uncited.

*(Tier: cannot be assigned. No study named, no population disclosed, no method described. That absence of a tier is the finding, not a gap in this skill's research.)*

### Example 4: an unsourced claim that evidence exists, distinct from an unsourced number

An article on mentoring asserted that "mentoring's ROI is well-documented and supported by research," naming no company, no study, and no number anywhere in the piece.

**The rule:** an unsourced claim that evidence *exists* is a more slippery failure than an unsourced number, because it gives the reader nothing concrete to check or reject. A number invites verification even when uncited: you can go looking for it and come up empty, as in Example 3. A claim like "well-documented" invites the reader to simply assume a citation exists somewhere, without ever presenting anything to look for.

**The mechanism:** phrases like "well-documented," "research shows," and "studies confirm" borrow the authority of citation without paying its cost. The writer gets credit for rigor while offering none.

**Where this rule is wrong:** if the next sentence or paragraph actually names the study or number the claim refers to, this is ordinary framing language, not a violation. Check whether the claim cashes out downstream before flagging it as empty.

*(Tier: not applicable. No number, no study, no population. The claim's entire function is to stand in for evidence that is never produced.)*

### Example 5: a claimed capability defined by its own unrecordability needs a countable transfer channel, not a test of the asset itself

A podcast guest attributed a company's decline to losing "process knowledge," defined, in the guest's own framing, as knowledge too tacit to write down or transfer directly. Generalized: any claimed asset described this way (tacit knowledge, culture, craft, institutional know-how) can be invoked to explain any outcome, because the claim is unfalsifiable by construction. Success proves the asset was present; failure proves it was lost; nothing distinguishes the two in advance.

**The rule:** when a claimed asset or capability is defined by its own unrecordability, write the falsifier against a countable **transfer channel**, a proxy for how the asset moves between people or is lost, not against the asset itself, which by definition offers nothing to measure.

**The mechanism:** an asset defined as something you can't write down makes every observation consistent with the claim. The claim explains everything after the fact and predicts nothing beforehand, which is the definition of unfalsifiable. A transfer channel escapes this because it is a countable proxy: attrition among the specific senior staff who supposedly held the knowledge, time for a replacement to reach full productivity, or documented mentorship hours before a departure. Those numbers can move independently of the story being told about them.

**Where this rule is wrong:** if the original claim already names a measurable proxy, a specific attrition number, an onboarding-time figure, a rate of documented handoffs, it isn't actually unfalsifiable, and this special-case check is unnecessary. Apply the ordinary evidence-tiering process to the proxy instead.

*(Tier: not applicable to the underlying "process knowledge" claim itself, by design. That is the finding. Source: podcast interview, July 2026 sweep; company and guest withheld here since the pattern being cataloged is what matters, not the specific attribution.)*

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

## RESEARCH APPENDIX: The Real Study Behind This Skill

**The citation (verify it yourself — this is a real, named, dated, findable paper, not a composite):**
Angelo Romasanta, Llewellyn D.W. Thomas & Natalia Levina, "[Researchers Asked LLMs for Strategic Advice. They Got 'Trendslop' in Return](https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return)," *Harvard Business Review*, March 16, 2026. ✅ Existence, title, authors, publication date, and abstract independently confirmed by fetching hbr.org directly. The full data tables sit behind HBR's paywall; the specific figures below are ◆ cross-verified against two independent secondary analyses that report identical numbers ([Zenn.dev literature review, May 2026](https://zenn.dev/sigma7641/articles/fcf90de4822321); [Polything, Apr 2026](https://polything.co.uk/blog/ai-strategy-trendslop-why-llms-give-bad-advice)) rather than taken from a single retelling.

**What was actually measured:**

Six frontier models — GPT-5, Claude, Gemini, Grok, DeepSeek, Mistral — were tested across **seven classic strategic tensions**, roughly 15,000 simulations total, under four intervention conditions (reversing which option is presented first, adding company-specific context, requesting deeper/slower analysis, and allowing a "both" hybrid answer):

1. Differentiation vs. Commoditization
2. Automation vs. Augmentation
3. Long-term vs. Short-term
4. Competition vs. Collaboration
5. Radical vs. Incremental innovation
6. Centralization vs. Decentralization
7. Exploration vs. Exploitation

**The findings — six of seven axes showed consistent, cross-model bias; one did not:**

| Strategic tension | AI favored | Precisely quantified? |
|---|---|---|
| Differentiation vs. Commoditization | Differentiation | ◆ **96%** of runs |
| Automation vs. Augmentation | Augmentation | ◆ **93%** of runs |
| Long-term vs. Short-term | Long-term | ◆ Directionally confirmed, exact % not disclosed in secondary sources |
| Competition vs. Collaboration | Collaboration | ◆ Directionally confirmed, exact % not disclosed |
| Radical vs. Incremental | Radical | ◆ Directionally confirmed, exact % not disclosed |
| Centralization vs. Decentralization | Decentralization | ◆ Directionally confirmed, exact % not disclosed |
| **Exploration vs. Exploitation** | **No consistent bias — real variance between models** | This is the control case the other six should be read against |

**The hybrid trap (a separate test, not the same as the table above):** when the models were allowed to answer "both," 63% still picked the trendy side outright, 24% chose the hybrid "do both" answer, and only 12% picked the less-fashionable side. The authors read the 24% "both" as a failure mode too, not a safe middle ground — it mirrors Porter's "stuck in the middle," where running differentiation and cost leadership at once produces neither advantage.

**The counterintuitive finding — prompting harder doesn't fix this:**

| Intervention | Bias shift |
|---|---|
| Reversing which option is presented first | ~19% |
| Adding rich, company-specific context | ~11% |
| Requesting deeper analysis / more careful reasoning | ~2% |

Superficial framing (option order) moved the needle nearly 10x more than asking the model to think harder. This directly contradicts the intuitive fix of "just give it more context" — context helps some, but it is not the lever that works.

**Bias doesn't depend on model quality:** the pattern held across all six models tested, including the frontier ones (GPT-5, Claude). A better model is not a less-biased model on this dimension — it just states the same trendy answer more fluently.

**The five recommendations from the paper itself:**
1. Use AI to broaden the option set, not to make the final choice.
2. Consciously counteract the known biases (the six axes above).
3. Stay alert — the specific trendy answer shifts as management vocabulary shifts over time; today's bias toward "augmentation" may not be tomorrow's.
4. Watch for the hybrid trap — "do both" is a failure mode, not a safe answer.
5. Don't rely on context alone to fix it (see the ~11% finding above).

**A concrete countermeasure worth adding to your own practice (from downstream commentary, not the paper itself — flagged as a technique, not a study finding):** instead of asking an LLM "what's the best strategy?", ask it to argue *against* your current plan as forcefully as possible — "give me the three strongest reasons this positioning fails in three years, assuming competitors go cost-leadership." Trendy-answer bias shows up when you ask for the best path forward; it's harder to trigger when you ask the model to build the strongest case against a specific, named plan.

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
- Evidence: Romasanta, Thomas & Levina (HBR, Mar 2026) — ~15,000 simulations, 6 models, consistent bias on 6 of 7 tested strategic tensions; independently confirmed the paper exists and cross-verified its headline figures against two independent secondary analyses.
- What would change our mind: Evidence that trendslop-corrected strategy underperforms AI-generated strategy when both are properly contextualized, or a follow-up study finding the bias has shifted enough that the six named axes are no longer the right ones to check.

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

Use the output prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## VISUAL SUMMARY

After completing this analysis, invoke the `excalidraw-svg` skill to create:
1. **Bias Radar** — 5-dimensional visualization showing trendslop across Differentiation, Augmentation, Long-term bias, Growth bias, Optimization bias
2. **Strategy Comparison Matrix** — AI-recommended strategy vs. contextualized alternative strategies
3. **Assumption Validation Checklist** — Which assumptions are known/true, known/false, unknown
