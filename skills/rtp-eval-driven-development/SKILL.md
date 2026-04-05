---
title: "Eval-Driven Development"
plugin: "craft"
version: "2.0"
imports: ["eval-framework", "feedback-flywheel"]
tags: ["evaluation", "testing", "ai-development", "quality"]
status: "production"
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

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## THE CORE THESIS: EVAL IS YOUR BACKLOG PRIORITIZER

Most teams treat eval as a quality gate: build the feature, then check if it's good enough. That's the wrong order.

**The right order:** Eval tells you *what to build next*. If your eval shows you're failing on long-document summarization 40% of the time, that failure IS your next sprint. The eval is not downstream of your backlog — it IS your backlog.

**What this means in practice:**
- Before every sprint planning: "What does our eval tell us is broken?" That answer gets on the sprint.
- Every model/prompt iteration is a hypothesis: "We believe this change will move the needle on [specific failure category]."
- Shipping without an updated eval is like merging code without running tests. You don't know what you broke.
- The eval owner should be in sprint planning, not just in QA review.

**The failure pattern:** Teams build evals once, run them periodically, and treat the results as health checks. This misses the core value — evals should actively drive what gets prioritized. If your evals aren't changing your backlog, they're decorative.

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

Use the output generation prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., prompt-as-product, ship-decision), generate the markdown handoff file as well.

## QUALITY GATE

Before you use an eval to ship a feature:
- [ ] Your eval dataset has at least 20–50 representative examples.
- [ ] You have a baseline score (simplest approach). All iterations must beat it.
- [ ] You've done error analysis on at least the top failure category.
- [ ] Your eval scores correlate with real user metrics (not just lab performance).
- [ ] You have an eval owner and a cadence for updating it (weekly, at minimum).
- [ ] You can articulate what each failure category means and how you'd fix it.

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

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
