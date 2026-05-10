---
name: rtp-feedback-flywheel
description: Use when designing data flywheels — capturing user interactions, closing the correction→eval→prompt loop, or auditing feedback pipelines. Diagnostic tool for building data flywheels that turn user interactions into model improvements. Maps feedback signals, designs capture pipelines, closes the loop from correction→eval→prompt→improvement, bootstraps cold start, handles PII/privacy. At maturity 5, products improve 15-20% per quarter from usage data alone. This is your competitive moat.
---
# Feedback Flywheel: The Diagnostic

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You designed a feedback system, not a flywheel. The bias is **disconnection**: your product logs thumbs-downs and user edits, the ML team trains on static evals, and nobody measures the delta between "feedback collected" and "model actually improved." You mistake collection for closure.

Real trap: **99% of products at stages 1-3 collect feedback but only 10-20% actually reach the model as training signal.** The rest accumulates in databases, unlabeled. Data without annotation velocity and model feedback loops is inventory, not leverage.

## THE PROCESS

### 1. Map Signal Hierarchy (not all feedback is equal)

**Rank by quality:** Corrections (user provides right answer) > Explicit feedback (thumbs down) > Implicit signals (edits, regenerate, abandon) > Absence (acceptance).

For each stage, ask: *Is this signal high-SNR enough to update the model?* A user edit where they change 1 word vs. rewrite 80% tells different stories. Design for **signal purity**, not volume.

### 2. Design Implicit vs. Explicit Capture

**Implicit (zero-friction):**
- Edit distance and direction (original → edited version)
- Regeneration attempt (user rejected, tried again)
- Copy-paste time lag (did they use it immediately or hours later?)
- Escalation (user sent to human review; use human resolution as gold label)

**Explicit (one-click, structured):**
- Thumbs up/down with optional error category
- "What was wrong?" radio buttons (tone, accuracy, completeness, irrelevance)
- Consent-gated for PII contexts (healthcare, finance)

Rule: 80% of signal should be implicit. Explicit feedback asks cognitive load; most users won't pay it.

### 3. Annotation Bottleneck & Labeling Velocity

Who labels what, and how fast? Map this:
- **Gold labels** (humans): Only corrections from domain experts or escalations; target 2-3% of feedback volume
- **Silver labels** (LLM-as-judge): Use saved user corrections as reference set; judge flagged outputs weekly
- **Bronze labels** (heuristics): High confidence patterns (user deleted all output = fail; no edits = pass)

**Critical metric: % of feedback reaching model per week.** If <5% of captured feedback becomes training signal, your flywheel is static, not dynamic.

### 4. Cold Start: Bootstrap Before Users Exist

Before you have production users:
- Synthetic user corrections: Generate outputs, have annotators edit them to ground truth
- Implicit signal simulation: Build eval where "regenerate" = failed output, "accept" = passed
- Use simulated user behavior to train LLM-as-judge before you have real data
- Deploy first version with high threshold for feedback (only high-confidence corrections)

At launch: Collect aggressively (log everything), label conservatively (only clear signals). Ramp labeling velocity as signal quality improves.

### 5. The Closed Loop: Signal → Eval → Change → Improvement

Design this as a pipeline, not a wish:

```
Weekly: Top 50 user corrections → pattern analysis → "What failed?"
Monthly: Accumulated corrections → add to eval set → run evals on current model
Quarterly: New eval set → prompt experiment → A/B test → measure delta
Continuous: LLM-as-judge on production flagged outputs using corrections as reference
```

**Most teams break here.** Define the handoff: Who runs the weekly review? Who owns the eval set? Who commits to prompt experiments? If "nobody," your flywheel is broken.

### 6. PII & Privacy Constraints

**Non-negotiable:**
- Users must know their corrections improve the system (in ToS or UI)
- Opt-out must be available; log separately
- Edits on sensitive data (names, account info, medical details): anonymize or aggregate before training
- Retention policy: define how long you keep user-provided corrections (recommended: 12 months unless used in production)

**Reality:** Healthcare and finance feedback loops are harder because you need consent. Compensate with higher signal purity (corrections only, not implicit).

## DIAGNOSTIC QUESTIONS (Ask These Weekly)

1. **How long from user signal to model improvement?** If >3 months, your loop is too slow. Products at maturity 5 iterate weekly.

2. **What % of feedback reaches the model?** Measure: (corrections used in training / total corrections collected). Target: >15% at steady state. <5% = broken flywheel.

3. **Is my annotation velocity keeping up with feedback volume?** If backlog grows monotonically, your bottleneck is labeling, not collection.

4. **Am I measuring the feedback loop in production?** Track: User corrections → eval set expansion → model change → A/B test delta. If you can't show the causal chain, you're guessing.

5. **What signals am I throwing away?** List every feedback type you log but don't use. Why? If the answer is "hard to interpret," that's a labeling problem, not a collection problem.

## REALITY CHECK

- **Echo chambers are real.** Optimizing only on what current users correct misses what non-users need. Audit your feedback distribution; supplement with explicit user research.
- **Implicit signals are noisy.** A user editing AI output might be personalizing, not correcting. Design classifiers that distinguish before feeding to model.
- **Feedback loops can poison evals.** If you only test on user corrections, you'll miss adversarial inputs or distribution shifts. Keep a held-out test set.
- **Privacy isn't optional.** In regulated domains, collection > annotation > training requires explicit flow-through documentation.

## QUALITY GATE

- [ ] Signal hierarchy defined (corrections ranked higher than implicit signals)
- [ ] Annotation bottleneck identified (labeling velocity ≥ feedback collection rate)
- [ ] Closed loop documented (weekly/monthly/quarterly cadence with owners assigned)
- [ ] Cold start plan exists (how to bootstrap flywheel before users)
- [ ] % of feedback reaching model measured weekly (target >15% at steady state)

## Data Flywheel as Competitive Moat

At maturity 5, products improve 15-20% per quarter from usage data alone. This is the strongest moat in AI. Map where you are on the maturity curve (1-5) and what it takes to get to the next level.

### Flywheel Maturity Levels

**Level 1: Collecting data but not using it**
- You log user corrections, edits, rejections
- No annotation pipeline; signals sit in database
- No feedback reaching model
- Use case: complying with "collect feedback" requirements without execution

**Level 2: Using data for manual model improvements (quarterly)**
- Humans review accumulated feedback quarterly
- Occasional manual prompt experiments based on patterns
- Improvement cycles: 3-4 times per year
- Signal latency: >2 months from correction to model update
- Moat strength: weak; competitors can catch up in one cycle

**Level 3: Semi-automated pipeline (monthly improvement cycles)**
- Automated labeling (LLM-as-judge) on flagged outputs
- Monthly eval set expansion from corrections
- Monthly prompt/system experiments with A/B testing
- Signal latency: 2-4 weeks from correction to update
- Moat strength: moderate; 3-4 month head start on competitors

**Level 4: Automated flywheel (weekly improvements from production data)**
- Weekly annotation velocity: 30-50% of feedback reaching model
- Continuous LLM-as-judge labeling with gold standard reference set
- Weekly eval set updates; bi-weekly prompt experiments
- Signal latency: 1-2 weeks from correction to deployment
- Moat strength: strong; competitors struggle to match iteration speed

**Level 5: Self-improving system (continuous learning with human oversight)**
- Daily annotation and model retraining pipeline
- Continuous online learning with human guardrails
- Automated regression testing on new eval cases
- Signal latency: <1 week from correction to production
- Feedback integration: 60-80% of production signal feeds model
- Moat strength: formidable; compounding advantage, nearly impossible to catch up

### Moving Between Levels: What It Takes

**1→2:** Someone owns weekly feedback review. One person, 5 hours/week.

**2→3:** Implement basic LLM-as-judge. Create reference set of 100-200 gold corrections. Automate weekly labeling.

**3→4:** Infrastructure: automated eval set updates, CI/CD for model changes, A/B test framework. Requires engineering.

**4→5:** Online learning infrastructure. Requires trust in your signal quality. Risk: if annotations are noisy, model degrades. Mitigation: strict quality gates and human review of edge cases.

### Signal Hierarchy & Quality

Not all feedback is equal. Rank by confidence:

1. **Gold corrections** (user provides right answer + domain expert validates): confidence 95%+
2. **Silver corrections** (user edits, high edit distance): confidence 70-85%
3. **Implicit signals** (regenerate, abandon, accept): confidence 30-60%
4. **Absence** (no edits, no feedback): confidence ~50%)

Only signal quality >70% should reach the model without human review.

## Feedback-to-Eval Pipeline

User corrections should flow directly into eval datasets. Every thumbs-down or user edit is a potential eval case. A broken pipeline wastes signal.

### Pipeline Steps

1. **User correction:** User edits output or marks as wrong
2. **De-duplicate:** Flag if correction is duplicate of recent signal
3. **Validate:** Is the correction actually right? (automated check: does it align with existing reference set? manual: expert review for edge cases)
4. **Add to eval set:** New correction becomes eval case (question, reference answer)
5. **Run regression:** Does new case break existing model performance? (automated)
6. **Measure impact:** A/B test against current model; measure delta
7. **Iterate:** If +impact, promote to training set; if -impact, investigate why

### Bottleneck Detection

If any step is missing, your flywheel breaks:

- **Missing deduplication:** 20-30% of corrections are redundant; you're training on noise
- **Missing validation:** Incorrect corrections poison eval set; model learns wrong patterns
- **Missing regression testing:** New signal breaks edge cases; you trade one problem for another
- **Missing impact measurement:** You don't know if the loop is working; you're optimizing blind

**Critical metric: % of feedback reaching model per week.** If <5% of captured feedback becomes training signal, your flywheel is static.

## Feedback Loop Latency

How fast does signal reach model improvement? Measure: time from user correction to model update.

### Industry Benchmarks

- **Best-in-class:** 1-2 weeks. Google Maps, Uber, Waze operate here.
- **Average:** 2-3 months. Most AI products; quarterly planning cycles.
- **Worst:** Never. Feedback collected but never used to improve model.

### Why Latency Matters

At latency >3 months:
- User no longer remembers context of correction
- Competitors can copy your feature and fix bugs before you update
- Network effects are weak; current users' needs not reflected in next release

At latency <2 weeks:
- Compounding advantage; each week's data improves next week's model
- Users see rapid improvement; engagement lifts
- Moat deepens weekly; very hard to catch up

### Measurement

Track: Time from user correction logged → correction labeled → added to eval set → model trained → deployed to production

Example: If it's now Wednesday and a user corrected something Monday, is that correction in today's eval set? In this week's training run? Will it be in next week's production model?

## THE EVAL IMPROVEMENT FLYWHEEL (Hamel Husain pattern)

The pipeline above describes the infrastructure. The Husain pattern describes the *cycle that runs on the infrastructure*. They are different things. You can have a working pipeline with a broken cycle — most teams do.

The pattern is five steps. Each step has an owner. Each step has an artifact. The cycle is what turns one-time fixes into compounding improvements:

```
1. Failure mode discovered
        ↓
2. Eval test written for the failure
        ↓
3. Fix shipped (prompt change, retrieval tweak, model swap, harness adjustment)
        ↓
4. Regression test added — the fixed failure can never silently come back
        ↓
5. Next failure mode surfaces (and it's a different one, because the eval suite caught the previous one)
        ↓
[loop back to step 1]
```

The 0.1% angle: **most teams fix and forget.** They find a failure, ship a fix, and never write the eval test that prevents regression. Six months later, a different prompt change brings the original failure back, no one notices, and the cycle never compounds. The Husain pattern demands that every fix becomes a permanent eval test that prevents regression. Without this discipline, AI products degrade silently as the team optimizes for the next thing.

### The Five Steps in Practice

**Step 1: Failure mode discovered.** A user correction, a support ticket, an internal trace review. The discovery itself is not the work; the work starts when you decide to act on it.

**Discipline:** Every failure mode entered into a tracking log within 24 hours of discovery. Not Slack, not memory — a structured log with: failure description, example trace, severity, frequency estimate, owner.

**Step 2: Eval test written for the failure.** Before fixing, write the test that would catch this failure if it happened again.

The test is binary: pass/fail on a specific failure pattern. Not a Likert scale. Not "quality score." A specific case the model should pass, with a specific output the model should produce (or not produce).

**Discipline:** No fix ships without the eval test that catches it. The test is the contract — when the test passes, the fix is real. When the test fails after a future change, the regression is caught immediately, not three months later by a churning customer.

**The trap most teams fall into:** Writing the eval test *after* the fix, copying the post-fix output as the "correct" answer. This validates that the fix works but doesn't prove the test would have caught the original failure. Write the test against the *broken* output first. Confirm it fails. Then ship the fix. Then confirm it passes.

**Step 3: Fix shipped.** Prompt change, retrieval improvement, model swap, harness adjustment, downstream filter. The fix is the part everyone focuses on — and it's the least important part of the cycle.

The fix has to pass:
- The new eval test (for the failure you just discovered)
- The full existing eval suite (no regression on previously caught failures)
- The cost-per-successful-outcome budget (improving quality at the cost of unit economics is a different kind of regression)
- The latency budget (improving quality at the cost of P95 latency is a UX regression)

If any of these fail, the fix isn't ready. Iterate.

**Step 4: Regression test added.** This is the step that turns one-time fixes into compounding improvements. Most teams skip it.

The regression test is permanent. It runs on every prompt change, every model upgrade, every retrieval tweak. It will run a thousand times before it ever catches another regression. That's fine. Its job is not to be useful daily — its job is to be the immune system that catches the failure if it ever tries to come back.

**Discipline:** Eval suite is split into two layers:
- **Capability evals** — hard problems, low pass rate, used for measuring improvement. Refreshed monthly.
- **Regression evals** — every fix you've ever shipped, target 100% pass rate. Permanent. Only grows; never shrinks.

The regression layer is the moat. Six months in, you have 50 regression tests. Twelve months in, 200. Twenty-four months in, 500. A new competitor with a better model still ships worse product because they don't have your regression coverage.

**Step 5: Next failure mode surfaces.** This is the proof the cycle is working. If the same failure modes keep appearing, your regression layer is leaking — fixes aren't permanent. If new and *different* failure modes keep appearing, your regression layer is doing its job and the team is climbing the difficulty curve.

**Discipline:** Quarterly review the failure mode log. Are new categories appearing, or the same ones? If the same ones, audit the regression layer. Find the test that should have caught it, ask why it didn't, fix the test (not just the model).

### Why This Compounds (And Why Most Teams Don't)

The math: every fix without a regression test is a 50/50 chance of returning within 12 months as the team makes adjacent changes. Every fix *with* a regression test is permanently fixed.

After 12 months:
- **Team without the cycle:** Fixed 100 issues. ~50 came back silently. ~50 still in production but discovered by users (not by evals). Quality flat.
- **Team with the cycle:** Fixed 100 issues. 0 came back. 100 permanently retired from the failure space. Quality compounds.

The teams without the cycle work harder. They spend more time on prompt engineering. They have more incident response. They have more support tickets. And their quality flatlines — because every step forward is matched by a quiet step backward.

The teams with the cycle look slower in the first three months. Their first 20 fixes take longer because each one comes with a permanent regression test. By month nine, they're outpacing the no-cycle team because their fix work compounds while the other team's work decays.

### Diagnostic Questions for the Cycle

Run these monthly:

- **What % of fixes shipped this month had a regression test merged within the same week?** Target: >90%. <70% means the cycle is broken.
- **How many regression tests does the suite contain?** This number should grow monotonically. If it shrank, someone deleted tests they shouldn't have.
- **When did the suite last catch a regression on a change that would have shipped otherwise?** If you can't remember, the suite isn't being run — or it's been deleted.
- **Are the failure modes I see this month different from the ones I saw last quarter?** Yes = cycle is working, climbing difficulty. No = regression layer is leaking, audit it.
- **Who owns the eval suite?** If the answer is "everyone" or "engineering," it's no one. The 0.1% AI PM owns the eval suite as a strategic artifact.

### Connection to Loop Latency

The pattern above describes the *quality* of the cycle. Loop latency (above) describes the *speed*. Both matter. A cycle that runs the Husain pattern but takes 3 months per loop produces 4 compounding fixes per year. A cycle that runs the same pattern in 2 weeks produces 26. The compounding math favors the fast cycle by 6.5x.

The discipline: improve cycle speed only after the cycle quality is real. A fast cycle without regression tests just produces more silent regressions, faster.

## OUTPUT FORMAT

When you audit a feature or product for flywheel maturity, use this structure:

```
## Feedback Flywheel Audit: [Feature Name]

Flywheel Maturity: [1-5]
- Current level: [brief justification]
- Limiting factor to next level: [what's missing]

Signal Hierarchy: [ranked by quality]
- Level 1 (Gold): [example correction, confidence %; volume/week]
- Level 2 (Silver): [example, confidence %; volume/week]
- Level 3 (Implicit): [example, confidence %; volume/week]

Annotation Velocity: [% of feedback reaching model per week]
- Feedback collected/week: [number]
- Feedback labeled/week: [number]
- Feedback used in model/week: [number]

Loop Latency: [time from correction to improvement]
- User correction → logged: [hours]
- Logged → labeled: [days]
- Labeled → eval set: [days]
- Eval set → model trained: [days]
- Trained → production: [days]
- Total loop latency: [weeks]

Feedback-to-Eval Pipeline: [exists? automated?]
- Deduplication: [manual/automated/none]
- Validation: [who reviews? gold standard?]
- Regression testing: [automated/manual/none]
- Impact measurement: [A/B test? delta tracked?]
- Broken link: [if any step is missing]

Cold Start Plan: [if pre-launch]
- Synthetic corrections: [how many? coverage?]
- Eval seeding: [size, domain specificity]
- LLM-as-judge readiness: [reference set size, quality]

PII Constraints: [applicable regulations]
- Data types at risk: [medical, financial, identity]
- Retention policy: [how long do you keep corrections?]
- Anonymization: [before training?]
- User consent: [opt-out available?]

Target: [maturity level + timeline]
- Goal maturity: [2-5]
- Timeline to achieve: [quarters]
- Investment required: [labeling, infra, engineering]
```

## WHEN WRONG

- Batch systems with no interactive user output (no feedback loop possible)
- User base too small (<500 active) or feedback patterns too sparse (can't reach statistical significance)
- Privacy requirements prohibit training on corrections without explicit consent you can't get
- AI component is genuinely one-shot (no ongoing interaction with user to close loop)
- Annotation velocity permanently <5% of collection velocity (labeling is not the bottleneck; you don't have it)

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
