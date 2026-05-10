---
name: rtp-fit-signal
description: 'PMF for AI: trust accumulation (not engagement). Measures: trust curve inflecting, magic moment >60%, correction >50%, feedback loop weekly. Use when: active users, dependency, scale or pivot. Triggers: ''PMF'', ''product-market fit'''
---
# Fit Signal: Detecting PMF in Non-Deterministic Systems

## DEPTH DECISION

**Go deep if:** You have 8+ weeks of active users, need to decide whether to scale or pivot, or diagnosing why trust isn't accumulating.

**Skim to Phase 2 if:** You have trust data already and just need to interpret it — trust curve is the core signal.

**Skip if:** <100 weekly active users, deterministic products (traditional PMF works), or batch/offline AI where users don't see output in real-time.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## AI-Specific PMF Signals (Beyond Engagement Metrics)

Traditional PMF signals (retention, NPS, DAU) break with AI. Look for these instead:

**Signal 1: Trust Progression** (most important)
- Do users accept AI output at increasing rates over time?
- New users: 40% acceptance. Week 4 users: 65% acceptance. Week 8 users: 72% acceptance.
- If acceptance stays flat or declines: No PMF, something is systematically unreliable.

**Signal 2: Accuracy Threshold for Switching**
- At what confidence level do users switch from "manual work" to "use AI output"?
- If users require >90% confidence to trust: You're not PMF, you're a verification tool (limited TAM).
- If users confidently use 70% accuracy output: PMF signal (they've built trust).
- Measure: % of outputs used directly (no edits) at each confidence level. 70%+ acceptance at 70% confidence = PMF threshold hit.

**Signal 3: Correction Rate Decay**
- Users learn the system's failure patterns over time and over-correct less.
- Week 1: 60% of outputs need correction. Week 8: 20% need correction.
- Decay >50% = PMF signal. Decay <30% = users aren't learning, trust isn't accumulating.
- But beware: Flat correction rate could mean (1) quality degraded, or (2) user has given up and accepts low-quality output (over-reliance). Monitor user complaint rate to distinguish.

## THE TRAP

You will measure product-market fit the way you'd measure traditional software fit: NPS (Net Promoter Score), retention curves, feature adoption. These break catastrophically with AI products because the experience is different every time.

The trap is **metric inversion through non-determinism**. Here's the sequence:

1. User tries your AI feature on Monday. It works great. NPS +2 sentiment.
2. Same user tries it on Tuesday with a slightly different query. It hallucinates. NPS -1 sentiment.
3. Same user tries it on Wednesday. Works again. NPS +2 sentiment.
4. You measure NPS over a month and get a "healthy 42." But the user hates you because they can't trust the product.

Your NPS is inflated by variance. Your retention looks healthy because retention is measured in cohorts, and cohorts average out bad weeks with good weeks. Your MAU looks stable when it's actually unstable (users trying it, leaving, coming back, leaving again).

The dangerous variant: you declare PMF based on surface metrics (retention >40%, NPS >40) without noticing the underlying signal: **users are engaging with your product not because they've adopted it, but because they're stress-testing it.** They keep coming back hoping it works, not because they've decided it's reliable enough to depend on.

This is especially pernicious because AI products *feel* like they're reaching PMF. Users are engaged, retention is decent, they talk about the product. But the engagement is fragile — it evaporates the moment a competitor offers higher reliability or lower variability.

## THE PROCESS

### Phase 1: Establish the PMF Null Hypothesis (Import falsification)

1. **Define what PMF would look like for your AI product.** Not "NPS > 40" (that's a symptom, not a cause). PMF is: "A meaningful fraction of users prefer our product to alternatives AND can't imagine going back."

2. **Identify the kill conditions for PMF.** What would prove you DON'T have fit? Write these down:
   - If we removed the AI component entirely, would users still use the product? (If yes, you don't have AI-PMF, you have workflow-PMF.)
   - If we replaced our AI with a competitor's AI, would users notice? (If no, the AI is commoditized.)
   - If we charged 2x our current price, would usage collapse? (If yes, they're using you on price, not preference.)
   - If we went dark for a week, would users seek alternatives? (If no, they don't depend on you.)

3. **Pre-commit to success criteria.** Before you measure, decide what you're looking for:
   - Trust curve: Is user confidence in the AI output increasing over time, or decreasing?
   - Magic moment: Is there a specific interaction that converts new users to engaged users?
   - Correction rate: Are users needing to correct/edit AI output less over time?
   - Feedback velocity: Are users providing more feedback signals (edits, regenerations, ratings) or fewer?
   - Switching cost: How much friction would it take to get a user to try a competitor?

### Phase 2: Measure Trust Curve (The Core Signal)

Trust curve is the only signal that matters. It measures dependence, not engagement.

4. **Define trust operationally:**

   For each AI output, measure:
   - **Acceptance:** User used output as-is (1.0) vs. edited (0.5) vs. rejected (0.0)
   - **Edit depth:** If edited, % of output changed: no changes (1.0) → small fix (0.7) → rewrite (0.0)
   - **Downstream use:** Did user actually use the output in their workflow, or just read it?

5. **Calculate trust score (simple formula):**

   ```
   Weekly Trust = (# accepted outputs / # total outputs) × (1 - avg_edit_depth)

   Example:
   - User generated 10 outputs this week
   - 7 accepted as-is (0.7 acceptance)
   - 2 edited slightly (0.8 edit depth each)
   - 1 rejected (0.0 edit depth)

   Average edit depth = (0 + 0 + 0.8 + 0.8 + 0) / 5 edits or rejections = 0.32
   Trust = 0.70 × (1 - 0.32) = 0.48
   ```

6. **Plot trust curve over time (minimum 8 weeks of data):**
   ```
   Week 1: Trust = 0.42 (users exploring, low confidence)
   Week 2: Trust = 0.45 (marginal improvement)
   Week 3: Trust = 0.48
   Week 4: Trust = 0.51 (approaching inflection point)
   Week 5: Trust = 0.58 (trust curve inflecting upward — PMF signal)
   Week 6: Trust = 0.62
   Week 7: Trust = 0.65
   Week 8: Trust = 0.67 (plateauing at high trust)
   ```

7. **Interpret the trust curve:**
   - **Flat or declining:** Users are not gaining confidence. PMF is NOT present. Something is systematically wrong (hallucination rate too high, quality inconsistent, product doesn't solve the problem).
   - **Inflecting upward then plateauing high (>0.60):** PMF signal is present. Users are learning to trust the system and using it consistently.
   - **Volatile (swinging between 0.3-0.7):** Variance is too high. Competitors can capture these users by offering more reliable output.

8. **Segment trust by use case:**
   - If overall trust is 0.55 but trust on "use case A" is 0.72 and "use case B" is 0.38, you have PMF for A, not for B. This tells you to double down on A and either fix B or kill it.

### Phase 3: Identify the Magic Moment (Conversion Trigger)

Magic moment is the specific interaction that converts "trying it out" to "I'll use this weekly."

9. **Find what precedes trust curve inflection:**

   For users whose trust curve goes from 0.3 → 0.6+ between week 1 and week 4, what did they do differently?

   Look for:
   - **Task completion:** Generated and used 5+ outputs (builds confidence through repetition)
   - **Successful edit:** Edited output, used it, got positive result (overcomes distrust)
   - **Export/share:** Shared output with colleague or used in their workflow (external validation)
   - **Return cadence:** Used product on 3+ separate days (builds habit)

10. **Calculate magic moment hit rate per cohort:**

    ```
    Cohort A (Power Users, >5 queries/day):
      - Hit magic moment (completed 5 queries): 70% of users
      - Of those, 8-week retention: 78%
      - Of non-magic-moment users, retention: 32%
      → Magic moment matters for power users

    Cohort B (Skeptics, 1-2 queries/day):
      - Hit magic moment (edit cycle + accept): 45% of users
      - Of those, 8-week retention: 65%
      - Of non-magic-moment users, retention: 28%
      → Magic moment is critical for skeptics

    Cohort C (Occasional, <1/day):
      - Magic moment (sharing output): 20%
      - Retention if hit: 55%
      - Retention if not: 18%
    ```

    **Insight:** Only 20% of occasional users convert via magic moment. This cohort has low PMF. Focus on power users and skeptics instead.

11. **Design the magic moment into the product.**
    - If the magic moment is "completing 5 outputs," can you guide users there? (Tutorial, guided tour)
    - If it's "successfully editing output," can you make the editing flow more discoverable?
    - If it's "sharing output," can you reduce friction on sharing?

12. **Track magic moment conversion rate over time:**
    - Week 1: 20% of new users hit the magic moment → 40% retention
    - Week 4: 50% of new users hit the magic moment → 65% retention
    - Goal: >60% hitting magic moment, which predicts >70% retention

### Phase 4: Measure Correction Rate Decay

Correction rate is a forward-looking trust signal: as users learn the system, they need fewer corrections.

13. **Define correction metrics:**
    - **Major edit:** User rewrote >50% of AI output (high distrust)
    - **Minor edit:** User changed <30% of output (light personalization, medium trust)
    - **No edit:** User accepted output as-is (high trust)
    - **Regeneration:** User rejected and asked AI to redo (distrust, learning signal)

14. **Calculate correction rate per user:**
    ```
    Correction Rate (week N) = (major edits + regenerations) / total outputs

    User A:
      Week 1: 60% correction rate (6 edits out of 10 outputs)
      Week 2: 45% correction rate
      Week 4: 25% correction rate
      Week 8: 15% correction rate

    User B:
      Week 1: 70% correction rate
      Week 4: 65% correction rate
      Week 8: 60% correction rate (declining trend but higher floor)
    ```

15. **Cohort analysis on correction decay:**
    - Calculate median correction rate for new users, week 1 vs week 8
    - Target: 50-60% reduction in correction rate (from 50% to 20-25%)
    - If correction rate is flat or increasing, the product is not delivering reliable output

16. **Interpret correction rate by use case:**
    - Some use cases should have low correction rates (e.g., code generation) — >90% acceptance
    - Some use cases should have moderate rates (e.g., creative writing) — 60-70% acceptance
    - If a use case has 80% correction rate and you expected 40%, either the use case is wrong or the product is failing

### Phase 5: Measure Feedback Flywheel Health (Import feedback-flywheel)

Feedback flywheel measures whether user corrections are improving the system.

17. **Capture the flywheel signals:**
    - **Input signal:** User corrects AI output (e.g., "this code has a bug")
    - **Processing:** Are you capturing this correction as training data?
    - **Output signal:** Does the system improve based on corrections?
    - **Measurement:** Do subsequent users see better performance?

18. **Design the feedback loop closing mechanism:**
    ```
    Week 1-2: Collect user corrections (zero processing)
    Week 3: Analyze top 10 correction patterns
    Week 4: Update prompt, retrieval, or fine-tuning based on patterns
    Week 5-6: Monitor if new users hit fewer of the same corrections
    Week 7-8: Repeat
    ```

19. **Measure loop health with two metrics:**

    **Feedback velocity:** How fast do user corrections turn into system improvements?
    - Ideal: Weekly or bi-weekly
    - Acceptable: Monthly
    - Concerning: Quarterly or less frequently

    **Correction absorption rate:** What percentage of user corrections lead to system improvements?
    - Target: 60-80% of distinct correction patterns get addressed within 4 weeks
    - If you're capturing lots of feedback but absorbing little, the flywheel is broken

20. **Calculate flywheel multiplier (advanced):**
    - Start cohort: 100 new users, avg correction rate 50%
    - If correction rate decays at historical rate without flywheel: 25% by week 8
    - If correction rate decays with active flywheel improvements: 18% by week 8
    - Flywheel multiplier: 1.4x improvement velocity

### Phase 6: Measure Switching Cost (Lock-in Signal)

Switching cost is an indirect PMF signal. If users won't leave, they've found fit.

21. **Estimate switching cost through behavioral proxies:**

    | Proxy | Interpretation | Target |
    |-------|----------------|--------|
    | Users who deleted account in first 2 weeks | Very low switching cost (no product stickiness) | <15% |
    | Users who tried a competitor and came back | High switching cost (prefer you even after testing alternatives) | >20% |
    | Users who paid for premium tier | Highest switching cost (financial + workflow) | >5-10% |
    | Users with >50 interactions | Moderate switching cost (workflow established) | >40% of retained users |

22. **Design the switching cost test (optional):**
    - Recruit 20-30 active users (trust score >0.60, used for 4+ weeks)
    - Offer them a free trial of a competitor's product
    - Measure: Do they return to your product after the trial?
    - If >70% return, switching cost is real
    - If <50% return, switching cost is weak (danger signal)

23. **Calculate switching cost premium:**
    - If users have switching cost, they tolerate price increases
    - Estimate: If you raised price by 20%, what % of users would leave?
    - If >10% leave, switching cost is insufficient to support premium pricing
    - If <5% leave, switching cost is strong enough to defend price

### Phase 7: Synthesize PMF Diagnosis (Import stress-test)

24. **Create a PMF scorecard (the final verdict):**

    ```
    SIGNAL                      TARGET       ACTUAL       STATUS
    ───────────────────────────────────────────────────────────
    Trust Curve (8-week)        >0.60        0.67         ✓ PASS
    Inflection point            By week 4-5  Week 4       ✓ PASS
    Magic Moment Hit Rate       >60%         52%          ⚠ CAUTION
    Correction Rate Decay       >50%         45%          ⚠ CAUTION
    Feedback Loop Velocity      Weekly       Bi-weekly    ⚠ CAUTION
    Switching Cost              <$200        $350         ✗ FAIL
    LTV:CAC Ratio               >3:1         2.1:1        ⚠ CAUTION
    ```

25. **Read the scorecard:**

    - **PMF CONFIRMED:** Trust >0.60 inflecting upward, magic moment >60%, feedback loop active, switching cost evidence present. **→ Scale with confidence. Ship adjacent features.**

    - **PMF EMERGING:** Trust trending up (not yet at plateau), magic moment 40-60%, feedback loop just closing. **→ Invest heavily in magic moment UX. Re-measure in 4 weeks.**

    - **PMF UNCERTAIN:** Trust flat or declining, magic moment <40%, feedback loop not closing, low switching cost. **→ Investigate root cause. Is output quality too low? Wrong problem? Bad UX? Fix OR pivot.**

    - **NO PMF:** Trust crashing, churn >30%, magic moment <20%. **→ Kill feature or fundamentally pivot. More engagement won't help. This is a product-market FIT problem, not a scaling problem.**

## REALITY CHECK

- **Trust curve is noisy at small sample sizes.** With <100 active users per week, weekly measurements are meaningless. Measure bi-weekly or monthly until you have enough data.

- **Variance in non-deterministic systems is real.** A 20-30% swing in trust score week-to-week is normal if you have a quality regression or an infrastructure spike latency. This is not a failure of the framework; it's a signal to investigate.

- **Different use cases have different PMF curves.** Customer support triage and creative writing have different baseline trust curves. Don't expect all use cases to converge to the same metrics.

- **PMF is not revenue.** You can have PMF (users love the product, use it consistently) but no revenue (freemium, weak monetization). Conversely, you can have revenue (users need you, captive market) without PMF (they'd switch if alternatives existed). Both are different challenges.

- **Magic moment varies by user persona.** Power users and skeptics have different paths to trust. Don't force all users through the same magic moment. Measure per cohort and enable multiple paths.

- **Feedback flywheel requires investment.** You can't declare "broken flywheel" until you've invested in closing the loop. If you're capturing feedback but not processing it, that's a resource issue, not a product issue.

## QUALITY GATE

Before making any scaling decision:

- [ ] **Measurement period:** 8+ weeks of data collected; minimum 100 weekly active users
- [ ] **Trust curve calculated:** Weekly trust scores computed; inflection point identified or noted as absent
- [ ] **Magic moment identified:** Specific interaction per cohort that precedes trust inflection; hit rate calculated
- [ ] **Correction rate tracked:** Week 1 vs. week 8 comparison; >50% decay as target
- [ ] **Feedback loop assessed:** Loop closure mechanism exists (weekly/bi-weekly cadence); 60%+ absorption target
- [ ] **Switching cost tested:** Behavioral proxies measured OR 20+ users offered competitor trial
- [ ] **PMF diagnosis completed:** Scorecard filled with actual measurements; diagnosis written (CONFIRMED/EMERGING/UNCERTAIN/NO FIT)
- [ ] **Root cause documented (if not CONFIRMED):** Why is magic moment low? Why is correction rate flat? Why is trust not inflecting?
- [ ] **Go/no-go decision made:** Scale (if PMF CONFIRMED), iterate (if EMERGING), pivot (if UNCERTAIN/NO FIT)

## WHEN WRONG

- Pre-product stage where you don't yet have users to measure
- Deterministic products where output variance is low (no need for trust curve analysis)
- Batch/offline AI where users don't see output in real-time (no interactive feedback loop)
- Products with <50 weekly active users where signals are too noisy to be statistical
- When PMF analysis is being used as a tool to delay shipping instead of to inform iteration
- When "we'll measure PMF later" is an excuse to ship without defining success criteria upfront

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
