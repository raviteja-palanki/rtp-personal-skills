---
name: rtp-falsification
description: >
  Tests any AI product recommendation by identifying conditions where it would be WRONG
  and pre-committing to what success actually looks like. Use when reviewing strategies,
  evaluating proposals, before committing resources, before launching features, or when
  someone is confident something "will work" without specifying what failure would look
  like. Triggers on 'this feature will improve X', 'we should launch this', 'our model
  will solve the problem', or 'we need to do this to compete'. Also use when reviewing
  metrics definitions (many teams measure what they can instead of what matters). Do NOT
  use to block action—use to de-risk it. Do NOT use on decisions that are genuinely cheap
  to reverse or in organizations where pre-committing to kill conditions is seen as political
  sabotage. Do NOT use during early exploration when the hypothesis is still forming.
imports: []
---

# Falsification

## DEPTH DECISION

**Go deep if:** Evaluating a significant AI feature investment or major model change. **Skim to questions if:** Quick check on whether success criteria are measurable. **Skip if:** Feature is truly cheap to reverse (quick experiment, low user base).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You will look for evidence that you're right. The bias is **confirmation bias** — the most universal and destructive bias in product work. You'll run a user test, find three users who love the feature, and declare validation. You won't notice the seven who were confused.

In AI products, confirmation bias is weaponized by non-determinism: you can always find an example where the model got it right. Cherry-picking successes from a probabilistic system is trivially easy and devastatingly misleading.

### Success Theater in AI Products

Teams building AI features systematically hide failure:
- **Demo bias:** You showcase the best 5 outputs in your launch presentation. The user never sees the 500 examples where the model hallucinated or failed silently.
- **Average metric masking:** Your model achieves 90% accuracy on average. But accuracy isn't normally distributed. The worst 10% of queries (edge cases, ambiguous requests, adversarial inputs) may have only 40% accuracy. Users interact with exactly those hard cases and remember them. Your 90% average is useless if the tail is broken.
- **Metric gaming:** Teams optimize the metric they measure, not the outcome users need. Example: "Reduce support tickets by 20%" → AI deflects tickets to a new category called "AI-assisted resolution" that doesn't count as a support ticket. Metric hits, problem unsolved.
- **Distribution mismatch:** Your eval set is carefully curated or synthetically generated. Production gets real user inputs: typos, ambiguous language, requests that don't fit the intended use case. Your 85% eval accuracy is 65% in production.
- **Silent failures:** NLP models don't crash. They return confident-sounding garbage. Users may not notice immediately. By the time you detect the failure through user complaints, you've trained the model on contaminated feedback.

## THE PROCESS

1. **State the recommendation as a falsifiable hypothesis.** Bad: "AI search will improve user experience." Good: "AI search will reduce average time-to-answer from 4 minutes to under 90 seconds for 80% of queries, without increasing support escalations."

2. **Identify the kill conditions.** List 3-5 specific, measurable outcomes that would prove the recommendation wrong:
   - What metric declining would invalidate this?
   - What user behavior would signal failure?
   - What cost threshold would make this unviable?
   - What competitor action would make this irrelevant?

3. **Design the counter-test.** For each kill condition, define how you would detect it:
   - What data would you collect?
   - Over what time period?
   - What's the threshold for "failed"?

4. **Pre-commit to the kill decision.** Before launching, write down: "If [kill condition] is true after [time period], we will [specific action: kill/pivot/scale back]." Get stakeholder sign-off on this BEFORE launch, not after.

5. **Run the red team.** Ask: "If I were trying to make this recommendation fail, what would I do?" Then check whether those conditions exist naturally.

6. **For AI hypotheses, test accuracy thresholds.** Replace vague claims with testable boundaries:
   - Claim: "This model can detect fraud" → Test: "At what accuracy? On what distribution (train/prod/adversarial)? Below what threshold does it fail the business?"
   - Claim: "We can launch with this model" → Test: "What's the minimum acceptable accuracy, precision, recall? For which segments? What happens when accuracy drops 2-3% in production?"
   - Accuracy % without context is false precision. Specify what the number means (false positive rate? rare edge cases excluded?).

## PRE-MORTEM FOR AI FEATURES

A pre-mortem forces you to imagine failure before you've invested 6 months and stakeholder credibility. This isn't pessimism—it's realism about what actually kills AI features.

**The Pre-Mortem Question:** "It's 6 months after we launched this AI feature. It failed. What happened?"

Force yourself to complete this for 5 specific failure scenarios:

### 1. Model Degradation
**Scenario:** Accuracy was 87% at launch, 79% after 3 months. Why?
- Distribution shift (user input changed; your eval set didn't capture real variation)
- Data drift (the world changed; the model wasn't retrained)
- Label contamination (feedback loop: you trained on user corrections that were sometimes wrong)
- Adversarial inputs (users learned to break the model and shared exploits)

**Detection speed:** Monthly eval runs on frozen test set. If you only measure "user satisfaction," you'll miss degradation until it's severe.

**Recovery cost:** If caught early (weekly): retrain, 2-3 days. If caught at month 3: retrain + rewrite feature, 2-3 weeks. If caught at month 6: rebrand as "beta," lose user trust.

**Kill condition example:** "If accuracy drops >5% after 60 days, pause serving to new users and investigate. If not resolved within 2 weeks, sunset feature."

### 2. Cost Explosion
**Scenario:** Unit economics looked viable at 10K queries/day. You shipped, scaled to 100K queries/day, and now you're hemorrhaging money.
- API costs scale linearly (you thought 10x traffic = 10x cost, you were right, but you didn't budget for 100x usage)
- Latency requirements force GPU serving instead of batch processing
- You need human-in-the-loop review for 10% of outputs (feasible at 10K queries, impossible at 100K)

**Detection speed:** Real-time cost tracking. If you don't have cost per query visible daily, you won't notice until the finance team escalates.

**Recovery cost:** Quick kill: revenue loss from feature shutdown. Slow kill: months of cost optimization to find a cheaper model or redesigned UX that uses the AI less.

**Kill condition example:** "If cost per query exceeds $0.08 at 50K daily queries, immediately switch to cheaper model. If that drops quality below 80% accuracy, sunset feature."

### 3. User Trust Collapse
**Scenario:** First week: "Wow, the AI is amazing." Week 3: "The AI gave me bad information, I wasted an hour." Week 8: Users actively avoid the feature.
- Hallucinations (the AI confidently stated a false fact as true; user acted on it)
- Inconsistency (same query produces different answers on different days; user doesn't trust variability)
- Opacity (users don't understand why the AI made a decision; they distrust black boxes)
- One bad interaction erases five good ones (loss aversion is real)

**Detection speed:** Never if you only read positive review comments. You'll detect it when daily active users decline 20% and support escalations spike.

**Recovery cost:** Trust is slower to rebuild than to lose. 1 month of damage = 3 months of recovery. If you've lost >30% of users, the feature may be unsalvageable.

**Kill condition example:** "If >20% of users report the AI provided incorrect information in post-session surveys, activate 'human verification required' mode. If that drops usage by >40%, kill feature."

### 4. Data Drift (Production ≠ Training)
**Scenario:** Your model trained on clean, well-formed queries. Production is full of typos, abbreviations, slang, and edge cases your training set never saw.
- Input distribution shift (users write differently than your training data)
- Output distribution shift (the "correct answer" changes; your model is optimizing for yesterday's answer)
- Rare-event blindness (your training set had 0 cases of edge case X; production has 5% of queries hitting that edge case)
- Seasonal shift (quarterly or yearly patterns; model trains on Q1 data, fails on Q4)

**Detection speed:** Compare eval set performance to production performance monthly. Stratify by input characteristics (query length, vocabulary, rare words).

**Recovery cost:** Retrain on production data, 1-2 weeks. Or redesign feature to constrain inputs, losing user flexibility.

**Kill condition example:** "If production accuracy drops >10% below eval set accuracy within first 30 days, activate manual review layer before serving AI results to users."

### 5. Competitive Leapfrog
**Scenario:** You launch an AI search feature and gain 12% user growth. A competitor launches a better AI search in 4 weeks, immediately capturing your new users.
- Your differentiation evaporates
- You're now competing on the AI feature, not your core product
- The cost to keep up with AI improvements accelerates (new models drop every 2 weeks)
- You're trapped in an AI arms race you can't win

**Detection speed:** Weekly competitive monitoring. Monthly feature parity assessment.

**Recovery cost:** Reposition the feature as table-stakes (integration, not differentiation). Accept lower margins. Or kill it and redeploy resources to defensible features.

**Kill condition example:** "If a competitor launches equivalent AI search within 90 days, conduct strategic reassessment. If we can't move into a differentiated use case within 30 days of their launch, sunset feature and reallocate team."

---

## EVAL-INTEGRATED FALSIFICATION

Evals are where you actually test falsification. If your eval doesn't map to a hypothesis, you're not falsifying—you're just scoring.

**The Mapping Rule:**
Every hypothesis should link to a specific eval. Format: "If this claim is true, [specific eval] should pass at [threshold]."

Examples:
- **Claim:** "AI summaries reduce reading time."
- **Mapping:** Run eval on 200 documents with known summaries. Binary pass/fail: "Did the user complete their task faster with the AI summary than without?" Threshold: 80% of users complete tasks faster.

- **Claim:** "The model can detect sarcasm."
- **Mapping:** Run eval on 500 sarcasm-labeled tweets. Binary pass/fail: "Did the model correctly classify sarcasm?" Threshold: 85% accuracy on out-of-distribution tweets.

### Binary Evals > Likert Scales

Use pass/fail evals, not Likert scales (1-5 ratings). Ratings are subjective and creep. "Is this summary good?" (subjective) becomes "Is this summary useful?" (less subjective) becomes "Does it complete the task?" (objective, falsifiable).

**Bad:** "Rate the AI explanation on clarity (1-5)." (One person's 3 = another person's 5. Non-falsifiable.)

**Good:** "Binary pass/fail: Could a user with no domain knowledge complete the task using only the AI explanation, without asking questions?" (Falsifiable.)

### Pre-Register Your Eval Criteria

**Criteria drift** (Shreya Shankar) is confirmation bias in eval. You run an eval, see the results, and then decide what "passing" means.

Fix: Write the eval criteria and passing threshold BEFORE running the eval. Commit in writing. Get stakeholder sign-off. Do not change the threshold after seeing results.

**Dangerous:** "Let's run the eval and see how it looks." (You'll pass whatever you see.)

**Safe:** "The eval passes if 80%+ of users can complete the task. We commit to this threshold now. We run the eval. We report the result, regardless."

### Track Eval Results Over Time

A passing eval isn't proof—a passing eval that used to fail is proof. Maintain an eval registry:

| Eval Name | Hypothesis | Threshold | Launch | Month 1 | Month 3 | Month 6 | Notes |
|-----------|-----------|-----------|--------|---------|---------|---------|-------|
| Sarcasm Detection | Model catches sarcasm at 85%+ accuracy | 85% | 87% ✓ | 84% ✗ | 82% ✗ | 78% ✗ | Model degrading; user feedback shows systematic failures on data drift |
| Task Completion | Users finish tasks with AI help | 70% | 72% ✓ | 71% ✓ | 68% ✗ | 65% ✗ | Increased complexity in user requests; model not keeping pace |

An eval that was always easy passing is false confidence. An eval that dropped from passing to failing is the signal to act.

## AI-SPECIFIC FALSIFICATION PATTERNS

Use this table to translate vague AI claims into testable hypotheses with kill thresholds. Every row represents a common product claim that sounds good in a meeting but fails in production.

| Claim | Falsification Test | Kill Threshold Example |
|-------|-------------------|----------------------|
| "AI will reduce support tickets" | Measure ticket deflection rate AND new ticket types created by AI errors. Track tickets that say "your AI gave me wrong information" separately. | Kill if AI-caused tickets > 15% of deflected tickets |
| "Users prefer AI-generated summaries" | A/B test with option to see original alongside AI summary. Track how many users click to view original. Measure edit distance on AI summaries vs. human baselines. | Kill if >40% of users edit summaries or revert to original |
| "This model is accurate enough" | Test on production distribution, not eval set. Stratify results by user segment, query complexity, and input language. Compare worst-segment accuracy to best-segment. | Kill if accuracy on worst segment < 70% |
| "AI search is better than keyword" | Blind A/B comparison on same query set. Measure time-to-answer, not just click-through rate. Track "gave up searching" as a failure mode. | Kill if time-to-answer improvement < 20% OR "give-up" rate increases |
| "Fine-tuning will fix this" | Measure improvement curve after 100, 500, 1000 labeled examples. Project diminishing returns mathematically. | Kill if improvement plateaus before meeting threshold |
| "Hallucination rate is <2%" | Run blind eval on 1000+ generations. Include adversarial prompts designed to trigger hallucinations. Distinguish confident hallucinations from uncertain outputs. | Kill if hallucination rate > 5% on production distribution |
| "Users trust this AI feature" | Measure behavioral trust: Do users act on AI recommendations without verification? Do they override the AI? Run post-interaction surveys: "Would you trust this system with a high-stakes decision?" | Kill if >25% of users report hesitation OR <60% report they'd use for important decisions |

The pattern: **Always measure the failure mode directly, not just the success rate.**

---

## REALITY CHECK

- **Failure mode:** Falsification becomes nihilism. Everything can be falsified — the goal is to identify the most likely failure modes, not to prove nothing works.
- **Political risk:** Pre-committing to kill conditions is politically dangerous. Stakeholders who championed the feature resist pre-mortems. This is exactly why it's necessary.
- **Time cost:** Serious falsification takes 2-4 hours of dedicated thinking. Budget it explicitly.

## WORKED EXAMPLE: AI-Powered Document Search

**Hypothesis:** "AI-powered document search will reduce average research time from 45 minutes to 15 minutes (67% reduction) for knowledge workers finding relevant documents in a 10,000-document repository, within 30 days of launch."

### Kill Conditions (Pre-Committed)

**Kill Condition 1: Insufficient Time Savings**
- Metric: Average research time after 30 days of use
- Kill Threshold: If average research time > 25 min after 30 days
- Action: Feature is not delivering enough value. Pivot to hybrid (AI + manual search).
- Detection: Instrumentation in search UI logs time from query start to task completion.

**Kill Condition 2: User Distrust / Frustration**
- Metric: Feature usage abandonment rate
- Kill Threshold: If users revert to manual search > 30% of sessions (e.g., 70 out of 200 weekly sessions)
- Action: AI search is causing more friction than it solves. Add explainability layer showing why document was ranked.
- Detection: Track session behavior; flag users who switch back to manual search within same session.

**Kill Condition 3: Cost Unsustainability**
- Metric: Cost per search query at scale
- Kill Threshold: If cost per query > $0.08 at 10,000 queries/day (= $800 daily, unsustainable for this feature's revenue contribution)
- Action: Switch to cheaper embedding model or reduce query frequency (cached results, batch searching).
- Detection: Real-time cost tracking tied to API usage.

**Kill Condition 4: Trust Damage (Hallucination)**
- Metric: Hallucinated citations or irrelevant results
- Kill Threshold: If hallucinated citations > 5% of results (user finds cited document doesn't match the claim)
- Action: Add citation verification layer before showing results; or reduce AI involvement (rerank human results instead of generating).
- Detection: Eval on 100+ real queries with human review; monthly audit on randomly sampled results.

**Kill Condition 5: Model Degradation**
- Metric: Accuracy on held-out evaluation set
- Kill Threshold: If accuracy drops > 10% below launch accuracy, or < 80% on worst-case user segments (specialized domains, rare documents)
- Action: Retrain on production data; or gate feature to specific document types where model performs well.
- Detection: Monthly eval runs on frozen 200-query test set, stratified by document type and query complexity.

### Pre-Committed Actions

| Trigger | Decision | Ownership | Timeline |
|---------|----------|-----------|----------|
| Kill Conditions 1 + 2 both triggered | Pivot to hybrid (AI re-ranking on top of manual search results) | PM + Engineering | 2 weeks |
| Kill Condition 3 | Switch to cheaper model; A/B test with users | Engineering | 1 week |
| Kill Condition 4 | Add explainability + citation verification layer | Engineering | 2 weeks |
| Kill Condition 5 | Retrain on production data OR gate to high-confidence segments only | ML + PM | 1-2 weeks |
| Any 2+ conditions triggered by day 14 | Sunset feature entirely; reallocate team to core product | Leadership | Immediate |

### Eval Mapping

Build evaluation dataset of 200 research queries with ground truth answers (e.g., "Find documents about supply chain disruption in 2023"). Stratify by:
- Query complexity (simple keyword search vs. complex reasoning)
- Document type (public docs, internal memos, archived emails)
- User role (sales, legal, product, operations)

**Primary eval:** Binary pass/fail: "Did the AI find the correct document in top 3 results?" Threshold: 80%.

**Secondary eval:** "Did the AI return any hallucinated citations?" Threshold: < 5%.

**Behavioral eval:** A/B test: 50 users with AI search, 50 users with manual search. Measure task completion time and error rate. Threshold: AI group completes tasks 20%+ faster with no increase in error rate.

### Pre-Mortem Top Risks (Ranked by Likelihood)

1. **Model overfits to training data, fails on production distribution** (Probability: HIGH) – Training data is curated documents; production is messy real-world queries with typos, abbreviations, unclear intent.
   - Detection speed: Weekly (compare eval accuracy to production metrics)
   - Recovery: 2-3 weeks (retrain on production data)

2. **Cost explosion as usage grows** (Probability: MEDIUM) – Embedding calls scale linearly; no caching strategy planned.
   - Detection speed: Real-time cost monitoring
   - Recovery: 1 week (switch to cheaper model) or architecture redesign (cache, batch)

3. **Users find hallucinated documents and lose trust** (Probability: MEDIUM) – Model is confident even when uncertain; users don't verify citations.
   - Detection speed: Monthly (user complaints, support escalations)
   - Recovery: 2-3 weeks (add citation verification layer)

4. **Competitive feature launch makes this obsolete** (Probability: MEDIUM) – Competitors may launch better AI search; differentiation evaporates.
   - Detection speed: Weekly competitive monitoring
   - Recovery: Reposition as table-stakes; accept lower margin OR innovate into new use case (2-4 weeks to pivot)

### Stakeholder Sign-Off (Pre-Launch)

**All parties agree:**
- PM: Kill condition thresholds are achievable and fair
- Engineering: Detection mechanisms are built and tested
- Data Science: Eval criteria are realistic and measurable
- Leadership: We will execute the pre-committed actions, even if they conflict with launch momentum

**Signatures (or explicit agreement):** _______________ Date: __________

---

## DIAGNOSTIC QUESTIONS

Use these questions to gut-check your falsification. If you can't answer them clearly, you haven't done the work.

**On Falsifiability:**
1. "What specific metric would make me stop this project? If I can't name one with a number, I'm not being honest with myself."
2. "Am I testing on the distribution that matters (production) or the distribution that flatters (eval set, synthetic data, cherry-picked examples)?"
3. "What would a skeptic on my team say right now? If I can't articulate the strongest counter-argument, I haven't falsified."

**On Pre-Commitment:**
4. "Have I pre-registered my success criteria, or am I defining success after seeing the results? (Post-hoc criteria = confirmation bias.)"
5. "Do my stakeholders know about the kill conditions, or will they be shocked when I try to invoke them? (Surprise kill decisions become political fights.)"
6. "What's the cheapest experiment that would disprove my hypothesis? Have I run it? (If I haven't run the cheapest test, I'm not confident.)"

**On AI-Specific Risks:**
7. "Where will this model fail? Can I articulate 3 specific failure modes and what triggers them?"
8. "Is my evaluation set representative of production? If not, what will my eval hide?"
9. "If this model's accuracy drops 10% in production, what's my fallback? (If I don't have one, I'm not de-risked.)"

**On Team Alignment:**
10. "Can everyone on the team name the kill conditions from memory? If people are fuzzy, they won't execute them."

---

## OUTPUT FORMAT: Falsification Brief

Use this template to document your falsification thinking. Share it with stakeholders before launch.

```
## Falsification Brief: [Feature/Hypothesis Name]

**Hypothesis:** [Stated with specific numbers, timeframe, and success criteria]
Example: "AI-powered search will reduce research time from 45 min to < 15 min for 80% of users within 30 days of launch, without increasing task error rate above 3%."

**Kill Conditions:**
1. [Metric] < [threshold] after [timeframe] → [specific action]
2. [Metric] > [threshold] after [timeframe] → [specific action]
3. [Cost metric] > [threshold] at [scale] → [specific action]
4. [User behavior metric] indicates [failure signal] → [specific action]

**Eval Mapping:**
- Eval 1: [Name] – Tests [which hypothesis component] – Pass threshold: [number]
- Eval 2: [Name] – Tests [which hypothesis component] – Pass threshold: [number]
- Eval 3: [Name] – Tests [failure mode] – Kill threshold: [number]

**Pre-Mortem Top Risks:**
1. [Risk] – Probability: [High/Medium/Low] – Detection speed: [daily/weekly/monthly] – Recovery: [hours/days/weeks]
2. [Risk] – Probability: [High/Medium/Low] – Detection speed: [daily/weekly/monthly] – Recovery: [hours/days/weeks]
3. [Risk] – Probability: [High/Medium/Low] – Detection speed: [daily/weekly/monthly] – Recovery: [hours/days/weeks]

**Stakeholder Pre-Commitment:**
- [ ] PM: Agrees kill conditions are fair
- [ ] Engineering: Agrees detection mechanisms are built
- [ ] Data: Agrees evals are realistic
- [ ] Leadership: Will execute pre-committed actions

**Signed by:** ________________ Date: __________ Version: 1.0

---

Last Updated: [Date]
```

---

## QUALITY GATE

- [ ] Recommendation stated as falsifiable hypothesis with numbers
- [ ] 3-5 kill conditions identified with specific thresholds and pre-committed actions
- [ ] Counter-tests designed for each kill condition
- [ ] Eval criteria pre-registered before running evals
- [ ] Pre-mortem completed for 3+ failure scenarios
- [ ] Stakeholders have explicitly agreed to kill conditions
- [ ] Red team scenario completed (skeptic's strongest counter-argument documented)
- [ ] Eval registry established for ongoing tracking

## WHEN WRONG

- Very early exploration where the hypothesis isn't yet worth formalizing
- Decisions that are cheaply reversible (just ship and learn)
- When the team has already been through rigorous falsification and needs to commit
- When falsification is being used as a political tool to avoid making decisions

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
