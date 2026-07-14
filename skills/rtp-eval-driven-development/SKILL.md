---
name: eval-driven-development
description: >
  Build AI features with the eval rubric AS the spec, not as a downstream gate. The eval
  defines what to build next — not whether what you built is acceptable. Use when shipping
  AI features with no clear definition of "done", when the team iterates on prompts without
  a quality compass, when error analysis must come before the next sprint, or when reviewers
  ask "how do you know this is good?". Triggers on "how do we test this AI feature",
  "when is it ready to ship", "eval framework", "quality gate", "definition of done for AI",
  "eval-driven", "ship criteria".
  Pairs with: eval-framework (the harness), confidence-tuner (validates the judge that scores the gate), ai-prd (the spec it feeds), ship-decision (the gate it arms), production-observability (where the loop closes).
imports: ["eval-framework", "feedback-flywheel"]
---

# Eval-Driven Development: The Eval Is Your Spec

## DEPTH DECISION

You are building an AI feature. The question: What does it mean for this feature to be "done"? In traditional software, you have a spec and tests. In AI, the spec is fuzzy ("the AI should be helpful") and the tests are expensive to write.

The trap: Treating evaluation as a testing gate that comes after development. For AI, evaluation must come first. If you can't measure it, you can't ship it. But warning: eval-driven development is usually wrong if you haven't done error analysis first.

**Who uses this:** AI engineers writing prompts and fine-tuning models. Teams shipping AI features. PMs deciding when to launch.

## DELIVERABLE FORMAT

Before starting, ask:

> **What format would you like this in?**
> 1. **Word Document** (.docx) — Formatted report with embedded visuals. Best for sharing.
> 2. **Presentation** (.pptx) — Slide deck with key findings. Best for meetings.
> 3. **Both** — Full report + summary deck.
>
> *Default: Word Document.*

If the user specifies format in their request, skip the question.

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md).

## THE ONE IDEA

**Eval-driven development is not "write tests first for AI." It is an operating model in which one artifact — the eval suite — carries three things that used to live in three different documents: the *definition of done*, the *team's quality-ownership*, and the *regression safety net*. When those co-evolve through a single artifact, the product compounds. When they don't, it rots.**

Three consequences reorganize how you run it:

1. **The eval suite is the new PRD.** The 30-page spec shrinks to a 1-page intent doc plus a living eval suite (Data → Task → Scores). The PM's craft doesn't shrink — it shifts from writing prose to curating datasets, designing rubrics, and interpreting evidence. And *who owns quality climbs a ladder*: Example → System → Constraint → Intent (see below).
2. **An eval case has a lifecycle — it graduates, it doesn't die.** A case is born as a *capability target* (something we can't do yet). When the system masters it, you don't delete it — you *promote it to a regression guardrail* (something we must never lose). That graduation is what stops the suite from going stale and what defends against saturation blindness.
3. **The gate is multi-dimensional, not one number.** Safety is an absolute veto; task-success is a threshold; cost/latency are budgets. "2% better on task" must never buy its way past a safety regression. A single blended score is how unsafe product ships looking green.

Everything below is the machinery for these three. The existing "eval is your backlog prioritizer" thesis is consequence #1 seen from the sprint board.

## THE CORE THESIS: EVAL IS YOUR BACKLOG PRIORITIZER

Most teams treat eval as a quality gate: build the feature, then check if it's good enough. That's the wrong order.

**The right order:** Eval tells you *what to build next*. If your eval shows you're failing on long-document summarization 40% of the time, that failure IS your next sprint. The eval is not downstream of your backlog — it IS your backlog.

**What this means in practice:**
- Before every sprint planning: "What does our eval tell us is broken?" That answer gets on the sprint.
- Every model/prompt iteration is a hypothesis: "We believe this change will move the needle on [specific failure category]."
- Shipping without an updated eval is like merging code without running tests. You don't know what you broke.
- The eval owner should be in sprint planning, not just in QA review.

**The failure pattern:** Teams build evals once, run them periodically, and treat the results as health checks. This misses the core value — evals should actively drive what gets prioritized. If your evals aren't changing your backlog, they're decorative.

## KEY TERMS (plain language)

- **Eval-first development** — writing the eval (the definition of "good") before building, so the eval drives what you build next.
- **Living spec** — an eval dataset treated as the evolving definition of the feature, updated as you learn.
- **Criteria drift** — your definition of "good" shifting as you see more outputs; expected, but must be tracked.
- **Goodhart's law** — when a measure becomes a target it stops being a good measure.
- **Eval debt** — accumulated gaps where the eval no longer covers how the product is actually used.
- **Process-entropy / ground-truth-of-record** — the risk that content reached your eval already degraded by several upstream AI passes; tag the original source so you can tell.
- **Intent Architecture ladder** — how the PM's quality-ownership evolves: Example (write rubrics) → System (design CI/CD + monitoring) → Constraint (govern agents: gates, kill switches) → Intent (define goals the system honors unwatched).
- **Data–Task–Scores** — the three artifacts that replace the 30-page PRD: versioned dataset (real traces), the task being evaluated, and calibrated rubric scores.
- **Capability → regression graduation** — the lifecycle of an eval case: born as a target the system can't yet hit, promoted (not deleted) into a regression guardrail once mastered.
- **Multi-dimensional gate** — a ship gate with separate rules per dimension: safety = absolute veto, task-success = threshold, cost/latency = budget. Never one blended number.
- **HHH** — Helpful / Harmless / Honest: the meta-rubric that forces multi-dimensional scoring so you can tell *which* dimension failed.

## THE TRAP

**Trap 1: Eval debt accumulates.** You write an eval in 2 weeks. Ship the feature. The eval becomes stale. New edge cases emerge. You stop maintaining it. After 6 months, nobody knows whether the feature still works.

**Trap 2: Eval writing becomes the bottleneck.** Creating a good eval takes as long as building the feature. Teams punt on evaluation and ship under-tested features.

**Trap 3: You eval the wrong thing.** Your eval scores look great. Users still complain. The eval measured the wrong problem.

**Trap 4: Gaming the eval without improving reality.** Prompt A scores 76% on your eval. Prompt B scores 81%. You ship B. Users see no difference. You optimized for the eval, not the product.

**Trap 5: Eval-driven without error analysis.** You have an eval but don't understand why it fails. You iterate blindly. The eval improves but the product doesn't.

## THE PROCESS

### 1. Eval-First Development

Before you write a single prompt or fine-tune a model:

**Step 1: Define success metrics.**
What does success look like? Not "helpful" or "accurate." Concrete, measurable metrics.
- Examples: "≥90% of summaries capture the main point." "Response latency < 2 seconds." "User thumbs-up rate > 70%."

**Step 2: Create evaluation dataset.**
Build a small dataset of test cases that represent success and failure.
- Start with 20–50 examples (not 1000s—expensive now, you'll iterate).
- Include edge cases. The cases your feature will definitely see.
- Example: If building a summarizer, include long documents, documents with multiple main points, documents where the conclusion is in the middle.

**Step 3: Write evaluation rubric.**
Define how you'll score each test case.
- Binary (yes/no): "Does the summary capture the main point?"
- Rubric (1–5 scale): "Rate clarity of summary: 1 = incoherent, 5 = perfectly clear."
- Automated metric: ROUGE score, embedding similarity, exact match.

**Step 4: Run baseline.**
Test the simplest possible approach (e.g., "Give me a summary" prompt) on your eval dataset.
- This is your null hypothesis. Everything else must beat this.
- Document the baseline score. You'll compare future iterations against it.

**Step 5: Design the feature.**
Now you build. But you'll build in eval-informed iteration loops.

### 2. Eval Datasets as Living Specs

Your eval dataset is not static. It's a spec that evolves.

**In development:**
- Every time you discover a failure, add it to the eval dataset (if it's a legitimate case your product should handle).
- Every time a user reports a problem, add a test case.
- Rerun the full eval before each feature iteration.

**In production:**
- Sample failures from production. Label them. Add to eval dataset weekly.
- Your eval dataset grows. Your spec evolves.
- **Quarterly refresh:** Re-run the full eval on your production system. Are you still hitting your targets?

**Eval Dataset Refresh Cadence:** Replace 20–30% of your eval dataset monthly with production traces. Stale datasets create false confidence — if >50% of your eval examples are older than 3 months, refresh immediately. Track the age distribution of your eval data. Older examples fade in relevance as users encounter new patterns. Fresh, production-derived failures keep your metrics honest.

**Anti-pattern:** Your eval dataset is frozen. Your feature works perfectly on the static eval. Users encounter new cases in the wild and the feature breaks.

### 3. Criteria Drift

Shreya Shankar's research identified a critical gap in eval methodology: criteria emerge from observing model outputs, not from specification.

You cannot fully define quality criteria before you see what the model produces. Some failure modes only become visible after you've evaluated 50 outputs and noticed a pattern you didn't anticipate. This means your eval framework MUST evolve.

**What this means in practice:**
- Your initial failure taxonomy (from error analysis) is a hypothesis, not truth.
- As you observe more outputs, merge categories that are really the same thing. Split categories that hide two different problems.
- When criteria change, document WHY — not just the new definition, but what observation caused you to update it.
- Budget for criteria revision every 2–4 weeks. If you haven't rethought a failure category in a month, you've stopped learning.
- Maintain a "golden set" of 50–100 curated examples as your regression anchor — these stay fixed so you can measure progress, while the rest of your eval dataset refreshes with production traces.

**Why this matters:** Teams that lock in criteria early end up optimizing metrics that don't matter. Tight, static rubrics prevent you from discovering what actually matters to users.

### 4. Eval Review Meetings

Just like code review, eval results need review.

**Weekly eval review (15 minutes):**
- "Our summarizer is now 84% (up from 79%)."
- "We added 5 new test cases this week. 1 is still failing."
- "Last week's failure mode: long documents with multiple topics. Fixed by adding explicit instruction."

**Monthly deep dive (1 hour):**
- Pick 1 failure category. Dig into 10 examples.
- What's the pattern? Is this a known limitation or a bug?
- Should we fix the model/prompt or update the spec (i.e., this case is out of scope)?

**Quarterly health check (2 hours):**
- Sample 50 cases from production. Re-eval manually. Do our scores still match reality?
- Have new failure modes emerged?
- Is the eval predictive of user satisfaction?

### 5. Error Analysis Before Eval Optimization

**This is critical:** Before you iterate on the eval, you must understand why it's failing.

**Step 1: Collect failing cases.**
Run your current model/prompt on the eval. Identify every failure.

**Step 2: Categorize failures.**
Group them by root cause:
- Hallucination (AI makes stuff up).
- Misunderstanding (AI misread the input).
- Out-of-scope (AI tried to do something the spec doesn't cover).
- Inconsistency (sometimes right, sometimes wrong on similar cases).
- Latency/cost (correct but too slow or expensive).

**Step 3: Prioritize by impact.**
Which failure category affects your product most?
- Hallucinations in a summarizer? Critical. Users act on wrong information.
- Missing edge case details? Medium. Users get 80% of the value.
- Latency? Depends on your use case.

**Step 4: Hypothesize the fix.**
For the top failure category, what would fix it?
- Better prompt? Fine-tuning? Different model? Post-processing filter?

**Step 5: Test the fix on just that category.**
Don't run the full eval yet. Test on the 10 failing cases. Does your fix work?
- If yes, move to full eval.
- If no, iterate on the hypothesis.

**Why this matters:** Without error analysis, you optimize for the metric, not the problem. You'll chase eval points while the real issue stays broken.

### 6. Eval Debt Detection

Eval debt is when you stop maintaining your eval suite. Signals:

- Your eval dataset hasn't grown in 3 months. But your feature has changed 5 times.
- You have eval scores but nobody knows what they mean anymore.
- You shipped a new feature but never updated the eval.
- Users report problems that your eval never caught.

**How to prevent:**
- Assign one person "eval owner" per feature.
- Add eval maintenance to your definition of done. Can't ship without updating eval.
- Run the eval automatically on every model/prompt change.
- Review eval results weekly. Visible metrics. If nobody looks, they don't maintain it.

### 7. The Process-Entropy Check — Has This Content Already Been Laundered Before It Reached Your Eval?

Every eval above scores a *single* model's output. But content often arrives at your eval harness having already passed through several AI steps upstream — one AI summarized the transcript, another rewrote the summary, a third drafted the record you're now testing. Your eval faithfully scores the last hop and misses that the input was already three passes from the truth.

Add one step before scoring: at the point where content *originates* (the raw interview, the real trace, the source filing), tag it as *ground-truth-of-record*. For any content reaching a decision, ask how many AI-mediated passes sit between that origin tag and the eval. If the answer is "we don't know," that *is* the finding — you're scoring a summary of a summary and calling it the source.

**Why it matters:** an eval is only as trustworthy as the provenance of what it scores. A high score on already-degraded input is false confidence — the eval says "good" about content that has already drifted from what it originally meant, and nobody upstream flagged the drift because nobody owned the origin. **When this is wrong:** if every upstream pass *re-anchored* to the tagged source (retrieval-grounded, not free rewriting), chain length doesn't matter — count re-anchored passes as clean. Don't demand provenance tags on throwaway content that never reaches a decision.
*(Source: "Don't Let AI Slop Muck Up Your Company's Processes," Holweg & Davenport, HBR, 16 Jun 2026. Signal: submissions to *Organization Science* up 42% since late-2022 while writing quality declined — ◆ [Forbes, 30 Apr 2026](https://www.forbes.com/sites/johndrake/2026/04/30/ai-slop-is-flooding-academic-journals-a-top-journal-measured-it/). Pairs with the "third clock" in `rtp-judgment-guard`.)*

## EVALS ARE THE NEW PRD — THE INTENT ARCHITECTURE LADDER

In deterministic software the PRD was the spec and the test suite verified it — cleanly separable, because software either passes or fails. AI breaks that: the same input yields different outputs, so the spec can't be a binary prose document. It has to be a *distribution-aware measurement system*. The eval suite becomes the spec.

The operational shift: the PRD shrinks to a **1-page intent doc** (what we're building, who for, why — refuse to make it longer) plus a **living eval suite** built from three artifacts — **Data** (versioned real traces), **Task** (the action being scored), **Scores** (calibrated multi-dimensional rubrics). The PM's leverage is identical; the artifact is different. Less prose specification, more dataset curation, rubric design, judge calibration, annotation review.

As this becomes real, the PM's *quality-ownership climbs a ladder* — this is the frame most teams are missing about where their own role is going:

| Rung | What the PM owns | What "the spec" looks like |
|---|---|---|
| **Example** | Writes rubrics, labels cases | "Here are 50 outputs I graded A/B/C" |
| **System** | Designs the CI/CD gate + monitoring | "Here's the pipeline that scores every change" |
| **Constraint** | Governs the agent: gates, kill switches, network guards | "Here's what it may never do, enforced" |
| **Intent** | Defines goals/rules/verification the system honors *with no human watching* | "Here's the outcome; the system proves it met it" |

Name which rung you're on. Most teams claim to be doing eval-driven development while sitting at Example (a folder of graded screenshots) and wondering why it doesn't scale. The climb from Example to System is where eval-driven development actually starts paying off; the climb to Constraint/Intent is what agentic products demand.

**Multi-dimensional by construction (HHH).** A single "quality" score collapses distinct concerns. Decompose against **Helpful / Harmless / Honest** so a bad output tells you *which* dimension failed — Helpful into accuracy/completeness/relevance, Harmless into safety/policy/bias, Honest into citation/uncertainty/hallucination. This decomposition is what makes the gate below possible. *(Source: Anthropic — [Constitutional AI / HHH](https://www.anthropic.com/research/constitutional-ai); operational framing from Ravi's AI PM OS "Evals as the New PRD.")*

## THE EVAL LIFECYCLE: CAPABILITY TARGET → REGRESSION GUARDRAIL

The single most common way an eval suite rots: teams treat a mastered case as *finished* and quietly stop running it. That's backwards. An eval case has a lifecycle, and the endpoint is not deletion — it's promotion.

- **Birth — capability target.** A case the system *can't* pass yet. It defines the next sprint (consequence #1: the eval is the backlog). Its job is to be *hard* — to expose a gap.
- **Graduation — regression guardrail.** Once the system reliably passes it, the case doesn't retire. It moves into the frozen regression set — the "we must never lose this" tier that runs on every change forever. Its job flips from *exposing a gap* to *defending a win*.

This lifecycle is the structural fix for **saturation blindness** — the trap where a suite hits 100% pass and everyone celebrates, not noticing the suite stopped *challenging* the system months ago (100% pass means you've lost the improvement signal, not achieved perfection). The fix is a two-tier suite in permanent motion: a **frozen regression tier** (graduated cases + a golden set that never rotates — your minimum bar) and a **live challenge tier** that must always contain cases the system is *failing* (fed by adversarial probes, synthetic edge cases, and real production failures). Rule of thumb: if your challenge tier is at 100% pass, it's not done — it's empty. Inject harder cases until it hurts again.

This is why regression evals in CI/CD matter (industry-standard now: re-run a fixed suite against a stable golden dataset on every release to catch quality regressions before deploy). The graduated tier *is* that fixed suite; the challenge tier is what keeps you moving. *(Sources: [Braintrust — Eval-Driven Development](https://www.braintrust.dev/articles/eval-driven-development); [promptfoo regression evals in CI/CD, 2026](https://medium.com/@alexrodriguesj/testing-llm-prompts-like-code-regression-evals-in-ci-cd-with-promptfoo-5242b4dcb9be).)*

## MULTI-DIMENSIONAL CI/CD GATING (safety veto ≠ task threshold)

The ship gate is where eval-driven development becomes enforcement — and the failure mode is subtle: **a single blended score lets a task-success gain buy its way past a safety regression.** "The new prompt is 2% better on task and only slightly worse on safety, net positive, ship it" is how unsafe product ships looking green. The average is the enemy.

Gate each dimension by its own rule:

| Dimension | Gate type | Behavior on a change |
|---|---|---|
| **Safety / policy (Harmless)** | **Absolute veto** | Any regression below the floor blocks the release. No trade against task-success. Non-negotiable. |
| **Task-success (Helpful)** | **Threshold** | Must clear the bar and not regress the golden set beyond tolerance. |
| **Honesty / calibration** | **Threshold** | Hallucination / citation quality within bounds. |
| **Cost / latency** | **Budget** | Ship if within budget; flag if trending toward the cliff. |

Two operational notes. First, the gate is only as trustworthy as the *judge* behind each score — a miscalibrated judge makes the whole gate theater, so calibrate it (`confidence-tuner`, Layer 2) before you arm the gate. Second, the veto dimensions map directly to `ship-decision`: safety veto here is the same veto that skill enforces at launch.

## THE ELITE OPERATING LOOP (the 5 systems)

The teams that make eval-driven development compound run a five-part loop, not a checklist. It's worth naming because each part fixes a specific way the practice degrades:

1. **Transition Failure Matrix** — pin every failure to the *exact* state transition it occurred at (e.g. "Generate SQL → Execute SQL"), not to a vague "the agent got confused." Precise localization is what makes the fix targeted.
2. **Benevolent Dictator** — one person makes the final binary pass/fail call on ambiguous cases. Not a committee. Quality standards averaged across a committee regress to blandness; a single owner keeps the bar sharp.
3. **Binary + Written Critique** — score pass/fail (a "3 vs 4" on a Likert scale is noise), but *attach a written critique* of why. The binary forces clarity; the critique captures what the number loses and becomes training data for the rubric and the judge.
4. **TPR/TNR Judge Calibration** — prove the automated judge against human labels before trusting it (this is the `confidence-tuner` handoff). An uncalibrated judge silently corrupts every number in the loop.
5. **Custom (vibe-coded) annotation tools** — bespoke review interfaces that render the artifact *as it really is* (the email as an email, the trace as a trace). Teams that build these cut annotation cycle time dramatically versus generic spreadsheets — and cycle time is the real constraint on how fast the loop turns.

The capstone of learning this skill is running the whole loop on *one* real use case end-to-end — matrix → dictator → binary+critique → calibrated judge → custom tool → back to the matrix. The loop is the moat: a competitor copies your framework in an afternoon but not the hundreds of graded edge cases and the calibrated judge the loop produced.

## GOODHART'S LAW IN EVAL

"When a measure becomes a target, it ceases to be a good measure." — Goodhart's Law

In AI development, this plays out in a specific and insidious way: your team optimizes the eval metric without improving the actual product.

**Signs your eval has been gamed:**
- Scores improved steadily for 3 months, but user satisfaction didn't move.
- The cases your prompt handles best are suspiciously similar to your eval dataset.
- A new engineer joins and finds the "tricky edge cases" in the eval set are already in the prompt as explicit examples.
- You changed the eval criteria (to be more lenient) more than once in a quarter.

**The structural fix: Rotation**
Replace 20–30% of your eval cases every month with fresh production traces. Not because the old cases were wrong — but because a fixed eval creates a fixed target. Rotating cases forces the system to generalize, not memorize.

**The golden set exception:** Keep a "golden set" of 50–100 core cases that never rotate. This is your regression anchor — cases that represent your absolute minimum bar. Everything else can rotate; the golden set stays.

**The rotation process:**
1. Weekly: Pull 10–20 fresh production failures. Label them (internal or with LLM-as-judge).
2. Monthly: Add the best new cases to the eval, retire the oldest non-golden cases.
3. Quarterly: Review the golden set — are these still the most important cases? Remove any that have become trivially easy.

## WHEN EVAL IS NOT THE CONSTRAINT

Eval-driven development is the right approach when *eval accuracy* is your bottleneck. It's the wrong approach when something else is failing first.

**Don't add more evals if the real problem is:**

**UX/workflow fit:** Your eval scores are 85%. Users are still unhappy. Before building more evals, do 5 user interviews. The failure might be how the output is *presented*, not how it's *generated*.

**Distribution:** You built a great AI feature. Nobody knows it exists, or it's 3 clicks deep in the UI. Eval optimization won't fix a discovery problem.

**Pricing:** Users love the feature in trials. They don't pay for it. No eval improvement changes that.

**Trust deficit:** Users are afraid to act on AI outputs (healthcare, legal, finance). More accuracy doesn't help if the interface never shows them HOW the answer was reached. Build explainability, not eval iterations.

**Data access:** The AI is wrong because it doesn't have the right context (user history, current state, real-time data). Adding a tool/RAG system delivers more value than prompt engineering.

**The diagnostic question:** "If the AI were perfect tomorrow, would the problem go away?" If no — stop iterating on eval and fix the actual constraint.

## KEY DIAGNOSTIC QUESTIONS

**Q1: Eval Predictiveness**

Do your eval scores predict user satisfaction?
- If eval is 85% but user satisfaction is 50% → Your eval measures the wrong thing.
- If eval is 75% but user satisfaction is 85% → Your eval is too strict or misaligned.
- Get specific: Do you have production metrics (user thumbs-up, retention, task completion) that correlate with eval scores?

*Think through:* Whether eval scores track actual user behavior and satisfaction metrics.

*Low end:* Eval and user satisfaction move together — scores in the same direction, correlation coefficient >0.7.

*Mid range:* Loose correlation — eval sometimes predicts satisfaction, sometimes doesn't — correlation 0.3–0.7.

*High end:* No correlation — eval and users in completely different worlds — correlation <0.3.

*Red flag:* Eval improved 10+ points over 60+ days but user satisfaction stayed flat or declined.

*Sharpen it:* "What's the Pearson correlation coefficient between eval score and monthly active user retention this quarter?"

---

**Q2: Error Analysis Depth**

Can you explain the top 3 failure modes in your eval without looking at code?
- If yes: You understand the problem space. Safe to optimize.
- If no: You're optimizing blindly. Stop and do error analysis first.

*Think through:* How deeply your team understands *why* the eval is failing, not just that it's failing.

*Low end:* You can articulate the top 3–5 failure categories with specific examples from your dataset, and explain what causes each one.

*Mid range:* You have failure categories identified, but the explanations are vague ("the model gets confused") rather than mechanistic ("when input exceeds 500 tokens, attention weights diffuse").

*High end:* You have failure categories, but nobody on the team can explain the root cause without diving into logs.

*Red flag:* Your eval score dropped 5% last sprint, and when asked why, the answer is "we don't know yet."

*Sharpen it:* "Of the 12 cases that failed this week, can you bucket them by root cause and name the top 3 categories?"

---

**Q3: Eval Coverage**

Does your eval catch issues your users encounter?
- Sample 20 production issues from the last month.
- Would your current eval have caught them?
- If < 50% of real issues are in your eval → Your eval is incomplete.

*Think through:* How well your eval dataset represents the actual problems users face in production.

*Low end:* You systematically compare production failures to your eval dataset; >70% of user-reported issues would have been caught by the eval.

*Mid range:* You do spot checks; ~50% of real issues would have been caught; some classes of failures are missing.

*High end:* Your eval and production failures are in different worlds; <30% overlap.

*Red flag:* You have a bug in production that users reported last month, but it doesn't appear in your eval dataset at all.

*Sharpen it:* "Of the 15 support tickets this month, how many would your current eval have surfaced?"

---

**Q4: Iteration Speed**

How often do you run the full eval?
- < daily: You're not iterating fast enough. No feedback loop.
- Daily: Good. You can iterate on prompts and see impact.
- Automated: Even better. Eval runs on every commit.

*Think through:* How quickly feedback flows from eval execution back to the development cycle.

*Low end:* Eval runs automatically on every model/prompt commit; results available within 1 hour; team uses results to decide on next iteration.

*Mid range:* Eval runs daily, manual trigger, results available next morning; used weekly for priority decisions.

*High end:* Eval runs weekly or less; manual labor required; results come too slow to inform active development.

*Red flag:* You've shipped 3 prompt changes this week, but you haven't run the eval since last Tuesday.

*Sharpen it:* "How much wall-clock time passes between when a change is committed and when eval results are available?"

---

## REALITY CHECK

Before you declare an eval "done":
- Have you validated it on at least 3 different failure modes and confirmed it catches them?
- Have you run it against your baseline twice to confirm the results are reproducible?
- Do you have a clear definition of what passes vs. fails? (Not subjective "looks good.")
- Have you tested the eval on an old version of your model/prompt? Does it correctly identify that as worse?

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., prompt-as-product, ship-decision), generate the markdown handoff file as well.

## QUALITY GATE

Before you use an eval to ship a feature:
- [ ] Your eval dataset has at least 20–50 representative examples.
- [ ] You have a baseline score (simplest approach). All iterations must beat it.
- [ ] You've done error analysis on at least the top failure category.
- [ ] Your eval scores correlate with real user metrics (not just lab performance).
- [ ] You have an eval owner and a cadence for updating it (weekly, at minimum).
- [ ] You can articulate what each failure category means and how you'd fix it.
- [ ] Your gate is **multi-dimensional** — safety is an absolute veto, not averaged against task-success.
- [ ] Mastered hard cases are **graduated into the regression tier**, not deleted; your challenge tier still contains cases you're failing.
- [ ] The judge scoring your gate is **calibrated** (TPR/TNR) — see `confidence-tuner`.
- [ ] You can name which **Intent Architecture rung** you're on (Example / System / Constraint / Intent).

## WHEN WRONG

**Eval debt has accumulated.**
- You shipped 5 feature iterations. The eval wasn't updated. Now you don't know if the feature still works.
- Trigger: Eval owner left. Nobody adopted it. Results stopped being reviewed.
- Recovery: Freeze feature development. Do error analysis on your current system. Build a new, simpler eval that's maintainable.

**You optimized the eval, not the product.**
- Eval scores went from 72% to 89%. Users see no improvement.
- Trigger: You focused on edge cases that don't matter. Or the eval metric doesn't match user experience.
- Recovery: Stop optimizing eval. Do user testing on real cases. Redefine the eval metric.

**New failure modes appear in production.**
- Users report issues your eval never caught.
- Trigger: Your eval dataset was too small or didn't cover the use cases users actually need.
- Recovery: Add production failures to eval. Rerun. You'll find your eval was incomplete.

**The eval becomes a bottleneck.**
- Writing the eval takes longer than building the feature. Team starts shipping without eval.
- Trigger: You're trying to be too rigorous too early.
- Recovery: Start with a simple eval (10 cases, binary scoring). Iterate. Don't wait for perfection.

**Eval scores plateau but product needs improvement.**
- Your eval says 78% (acceptable). But users are unhappy.
- Trigger: The metric doesn't measure what users care about.
- Recovery: Go back to users. What are they actually dissatisfied with? Change the eval metric to measure that, not what's easy to measure.

---

## WHERE THIS MEETS YOUR STACK

Eval-driven development is the *operating model*; it hands off in every direction:

- **The gate is only as honest as its judge → `confidence-tuner` (Layer 2).** Every threshold and veto here is computed by a scorer. Calibrate that scorer's TPR/TNR *before* you let it gate a release, or you're enforcing a spec you can't trust.
- **The eval suite IS the spec → `ai-prd` / `ai-prd-flow`.** The 1-page intent doc is the upstream half; this skill is the living other half. Don't write a 30-page PRD for a probabilistic feature — write the intent doc and the eval suite.
- **The gate arms the launch decision → `ship-decision`.** The safety veto here is the same veto enforced at GA. This skill decides *per-change*; ship-decision decides *per-launch* on the same dimensions.
- **The loop closes in production → `production-observability` / `feedback-flywheel`.** Graduated cases and challenge cases both come from real traces. Production failures feed the challenge tier; the observability layer is where you catch that the live system drifted below a graduated guardrail.
- **What the agent may never do → `safety-by-design` / `agent-risk` / `tool-architecture`.** The Constraint rung of the Intent ladder (gates, kill switches, permission boundaries) is designed in those skills; eval-driven development is how you *verify* those constraints hold.
- **The numbers this produces feed the dashboard → `ai-product-metrics`.** Eval pass rates, per-dimension scores, and cost-per-successful-outcome are the leading indicators that skill puts in front of the team and translates for execs.

The spine: **this skill turns "how do we know it's good?" into an enforced, evolving, multi-dimensional gate — but it borrows its trustworthiness from `confidence-tuner` upstream and lends its authority to `ship-decision` downstream.**

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
