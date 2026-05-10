---
name: rtp-prompt-as-product
description: Treat prompts as versioned product artifacts with the rigor of code deployments — version control, regression testing, A/B testing, rollback capability, and pinned versions. Prompts are the new product surface; a five-word reorder in a system prompt can shift output distribution across the entire user base. Use when shipping prompt changes to production, debugging "the AI started behaving differently", designing a prompt deployment process, or pushing back on "we just tweaked the system prompt". Triggers on "prompt change", "system prompt update", "prompt versioning", "prompt rollback", "prompt A/B test", "prompt regression", "prompt deployment".
---
## DEPTH DECISION

Are you treating prompts as internal implementation details, or as versioned product artifacts?

**Red flag**: "We just tweaked the system prompt." No version, no testing, no rollback plan.

**Green flag**: System prompt changes go through the same release process as code. Pinned versions. Rollback tested. A/B testing plan before production.

The trap is subtle: prompts feel like magic, so changes feel harmless. A five-word reorder in a system prompt can shift output distribution across your entire user base.

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

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

**The "It's Just Text" Problem**

You change a prompt and assume the effect is additive or local. You find out too late it broke downstream behavior in edge cases you never tested. Users see hallucinations spike. Your evals pass but production degrades.

Why? Prompts are non-linear. Small changes compound. The exact phrasing affects:
- Which examples the model attends to
- Confidence calibration
- Reasoning chain depth
- Hallucination tendency
- Token efficiency

You can't eyeball it. You need systematic regression testing.

---

## THE PROCESS

**1. Establish the Baseline**

Document the current system prompt (version it), run your eval suite against it, and log the metrics. Establish the ground truth: what does "production quality" look like for this prompt?

*Why this matters:* Without a baseline, you can't detect regressions. Teams that skip this find themselves comparing the new prompt against vague memories of "how it used to work." You'll ship changes that hurt performance and not notice until users complain.

**2. Propose the Change**

Write the new prompt version and specify the intent: "reduce hallucination in factual questions" or "improve reasoning chain clarity." Document why you're changing it (signal, not noise).

*Why this matters:* Undocumented changes become organizational debt. Six months later, no one knows why the prompt says what it says. When the model changes, you iterate blindly. Teams that skip this end up with prompts shaped by accident rather than design.

**3. Regression Test**

Run the full eval suite on the new prompt. Look for regressions in any category (don't just check your target metric). Measure cost-per-output (did the new prompt make the model more verbose?) and check determinism impact (does output stability change?).

*Why this matters:* Improving one metric while breaking another is worse than no change at all. Teams that test only their primary metric ship changes that kill acceptance rates or double token costs. You need 360-degree visibility.

**4. A/B Test**

Deploy to a small cohort (1-5% of traffic). Monitor: acceptance rate, regeneration rate, edit distance, user corrections. Watch for silent failures (users stuck, abandoning tasks). Let it run for at least 3-5 days (weekly seasonality matters).

*Why this matters:* Evals don't capture production reality. Real users find edge cases your test set missed. Teams that skip A/B testing find production degrades invisibly — users work around the bad prompt, acceptance rates creep down, and the change ships anyway.

**5. Production Release**

Tag the version in your prompt library. Keep the old version accessible for immediate rollback. Monitor the first 24h aggressively. Automate rollback if key metrics degrade > threshold.

*Why this matters:* Rollback takes 5 minutes in theory, 3 hours in practice if you're unprepared. Teams that don't practice rollback hesitate when they should act, and by the time they decide to revert, the damage is visible to users.

**6. Prompt Decision Tables**

For complex prompts, create explicit decision tables that map input conditions to prompt behavior. This replaces vague instructions like "be helpful" with testable logic:

| Input Condition | Prompt Behavior | Expected Output | Test Case |
|----------------|-----------------|-----------------|-----------|
| User asks factual question | Cite sources, be concise | Direct answer + source | "What's the capital of France?" → "Paris (source: ...)" |
| User asks opinion | Acknowledge subjectivity, present multiple views | Balanced response, no single "right" answer | "Is remote work better?" → "There are perspectives..." |
| Confidence < 60% | Express uncertainty, suggest alternatives | Hedged response or "I'm not sure" | Feed ambiguous query |
| Input contains PII | Redact before processing, log sanitized version | PII-free output | Test with SSN, email |

Decision tables make prompt behavior auditable and testable. Each row becomes a test case in your regression suite.

*Why this matters:* Without explicit decision tables, prompts become magical black boxes. What does "be helpful" mean in context? Does this prompt handle PII correctly? Teams that skip this find they can't debug failures — the prompt does something unexpected and no one knows why.

**7. Prompt Regression Testing Framework**

Beyond running evals, structure your prompt testing as:

- **Smoke tests (5 min)**: 10-20 canonical queries that must always pass. Run on every prompt change.
- **Regression suite (30 min)**: 100-200 cases covering known failure modes. Run before any production release.
- **Stress tests (2 hr)**: 1000+ cases including adversarial inputs, edge cases, multi-turn. Run weekly or before major changes.
- **Golden set**: 20-50 hand-curated examples where the "perfect" output is defined by a domain expert. Use for taste calibration, not just accuracy.

*Why this matters:* Automated evals miss taste failures — outputs that are technically correct but subtly wrong. Teams that test only metrics ship prompts that technically pass but feel off-brand or miss context. The golden set catches these.

**8. Output Format**

Document your prompt changes with:

```
## Prompt Spec: [Feature Name]

Version: [semver]
Last Changed: [date]
Changed By: [name]
Change Reason: [why]

Decision Table:
| Condition | Behavior | Test Case | Pass/Fail |
|-----------|----------|-----------|-----------|

Regression Results:
| Suite | Cases | Pass Rate | vs Baseline | Regressions |
|-------|-------|-----------|-------------|-------------|

A/B Test Plan:
- Cohort: [%]
- Duration: [days]
- Primary metric: [acceptance rate]
- Rollback trigger: [threshold]
```

Use this format to ensure every prompt change has decision logic, testing results, and rollout rigor.

---

## KEY DIAGNOSTIC QUESTIONS

**On Prompt Versioning:**
- Can you roll back to the prompt from 2 weeks ago? Without friction?

*Think through:* Your version control capability
*Low end:* Version numbers in comments; rolling back requires code deploy
*Mid range:* Git tracking prompts; rollback is 2-step (revert + deploy)
*High end:* Prompt library with instant rollback; A/B routing by version
*Red flag:* You store the current prompt in code but not historical versions
*Sharpen it:* How long to rollback a prompt change? (Should be < 5 min)

- Do you have a diff showing what changed in your system prompt between releases?

*Think through:* Your visibility into prompt evolution
*Low end:* No diffs; changes documented in Slack
*Mid range:* Git diffs exist; requires engineer to generate them
*High end:* Automated diff reports; changes highlighted with impact assessment
*Red flag:* You can't explain what changed between v1 and v2 of a prompt
*Sharpen it:* Can someone new to the team understand why the prompt changed by looking at the diff?

- Who approved the last prompt change, and when?

*Think through:* Your governance rigor
*Low end:* No approval record; someone just pushed it
*Mid range:* Approval record exists; approval and change timing don't align
*High end:* Approval chain documented; approval required before release
*Red flag:* You don't know who changed the prompt or when
*Sharpen it:* Is there a record of who approved this change and what the approval criteria were?

**On Testing Rigor:**
- Have you run your eval suite on this prompt version?

*Think through:* Your test automation maturity
*Low end:* No eval suite exists
*Mid range:* Evals exist; manual to run, inconsistent baseline
*High end:* Automated eval pipeline; results auto-compared to baseline
*Red flag:* You run evals ad-hoc instead of systematically
*Sharpen it:* What happens if you run evals right now? Do you get consistent results?

- Do you test for regressions outside your primary metric?

*Think through:* Your failure mode awareness
*Low end:* Test only the metric you care about improving
*Mid range:* Test 3-4 key metrics; miss tail failures
*High end:* Comprehensive regression suite; track accuracy, latency, cost, hallucination, confidence
*Red flag:* You improved accuracy but didn't check cost per output (and it doubled)
*Sharpen it:* Name 5 things that could go wrong with your prompt that your current evals don't check.

- What happens to accuracy, latency, cost, hallucination rate, and confidence calibration?

*Think through:* Your measurement holism
*Low end:* You measure one of these; others are unknown
*Mid range:* You measure 3; the rest are estimates
*High end:* All five tracked in dashboard; regression alerts on any
*Red flag:* Cost per output increases 15%+ but you ship anyway
*Sharpen it:* What's your cost-per-output baseline, and what % increase would block a release?

**On Production Monitoring:**
- Are you tracking acceptance rate per prompt version?

*Think through:* Your production observability
*Low end:* No acceptance rate tracking; success is assumed
*Mid range:* Acceptance rate tracked; breakdown by version requires manual query
*High end:* Dashboard shows acceptance rate auto-segmented by prompt version
*Red flag:* You notice acceptance rates drop but can't tie it to a specific prompt change
*Sharpen it:* How would you know if the last prompt change hurt acceptance rate?

- Can you correlate user corrections back to specific prompt versions?

*Think through:* Your correlation capability
*Low end:* No correction tracking; users just use regenerate button
*Mid range:* You track corrections but don't tie them to prompts
*High end:* Corrections auto-tagged by prompt version; regressions flagged
*Red flag:* Users are correcting outputs more often but you don't know why
*Sharpen it:* If correction rate spiked 10%, could you tell me which prompt change caused it?

- Do you have alerts if acceptance rate drops > 5% on a prompt change?

*Think through:* Your alerting discipline
*Low end:* No alerts; you manually check dashboards
*Mid range:* Alerts exist; routed to Slack but often ignored
*High end:* Alerts trigger automatic rollback or escalation
*Red flag:* Bad prompt ships and metrics degrade for hours before anyone notices
*Sharpen it:* What's your SLA for detecting a bad prompt in production? (Should be < 1 hour)

**On Rollback Capability:**
- Can you roll back a prompt change in < 5 minutes without a deploy?

*Think through:* Your rollback friction
*Low end:* Rollback requires code change + full deploy cycle
*Mid range:* Rollback is possible; takes 20-30 min
*High end:* Instant rollback via A/B routing or prompt library swap
*Red flag:* You want to rollback but it's a multi-hour process
*Sharpen it:* Describe the exact steps to rollback the last prompt change. Time yourself.

- Do you practice rollbacks? (Like a fire drill.)

*Think through:* Your operational readiness
*Low end:* Never practiced; untested
*Mid range:* Rolled back once in an emergency; lessons captured
*High end:* Monthly rollback drills; SOP documented and practiced
*Red flag:* First time you rollback is in production during an incident
*Sharpen it:* When was the last time you practiced rolling back a prompt change?

- How long would it take to detect a bad prompt in production? (Should be < 1 hour.)

*Think through:* Your detection latency
*Low end:* Hours to days (manual discovery via user complaints)
*Mid range:* 30-60 min (automated alerts + manual investigation)
*High end:* < 10 min (alerts + automatic rollback triggers)
*Red flag:* Users find the bug before you do
*Sharpen it:* How are you alerted to a bad prompt? Who gets the notification first?

---

## ESTIMATING A/B TEST COSTS BEFORE YOU RUN THEM

A/B testing prompts is not free. Before running an experiment, estimate the cost:

**The formula:**
`Test cost = (daily active users × cohort size %) × avg tokens per session × $/token × test duration (days)`

**Example:**
- 10,000 DAU × 5% cohort = 500 users in test group
- 2,000 tokens avg per session (input + output)
- $0.002 per 1K tokens (Claude Haiku rate)
- 7-day test
- Cost: 500 × 2,000 × $0.000002 × 7 = **$14 for the experiment**

**What this changes:**
At $14/test, you should be running tests weekly, not monthly. The bottleneck is not cost — it's your ability to write and evaluate test variants.

**When cost IS a constraint:**
- High-volume products (1M+ sessions/day): Cost per test scales to $1,000+. Batch testing: run all variants simultaneously rather than sequentially.
- Long-context tasks (100K+ tokens per session): Even a 5% cohort can be expensive. Reduce cohort size, extend duration.

**The minimum viable test:**
5% cohort, 7 days, binary outcome metric (accept/regenerate). Don't design elaborate factorial experiments when a simple A/B will answer your actual question.

---

## RELATIONSHIP TO OTHER SKILLS

**Prompt-as-Product vs. Eval-Driven Development:** These two skills are complementary, not overlapping. Here's the exact division:

| Question | Which skill |
|---|---|
| What should we measure to know if the prompt is working? | **Eval-Driven Development** — sets the measurement framework |
| How do we manage, version, and improve the prompt over time? | **Prompt-as-Product** — governs the change management lifecycle |
| Are our eval scores going up? | Eval-Driven Development |
| Did this specific prompt change improve the right thing? | Prompt-as-Product |

**The workflow:**
1. Eval-Driven Development runs first — defines what "good" means for this feature.
2. Prompt-as-Product runs throughout development — manages every change to the prompt as a versioned, tested artifact.
3. When Eval-Driven Development flags a failure category, Prompt-as-Product governs how you change the prompt in response.

**The anti-pattern:** Using Prompt-as-Product without an eval framework. You're managing changes without knowing if they're improvements.

---

## REALITY CHECK

**What production looks like:**
- You change the system prompt
- Metrics dashboard flags the change (automated)
- You run regression evals (15 min)
- You A/B test (automated cohort selection, automated monitoring)
- You decide: ship, iterate, or rollback (all < 24h)
- Users see no degradation because you caught it early

**What it doesn't look like:**
- "We tweaked the prompt" with no version control
- Eval suite shows improvement but production shows decline
- Rollback takes 3 hours and requires a full redeploy
- You don't know which prompt version users are on
- Hallucination spike but you don't connect it to the prompt change

---

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., eval-driven-development, ship-decision), generate the markdown handoff file as well.

---

## QUALITY GATE

**Prompt changes require:**
1. ✓ Version control (git-like tracking of prompt history)
2. ✓ Regression testing (evals on all prior test sets, no degradation)
3. ✓ A/B test plan (target metrics, cohort size, duration, rollback threshold)
4. ✓ Rollback procedure (documented, < 5 min execution)
5. ✓ Production monitoring (acceptance rate, corrections, cost per output, latency)

**Blocks shipping if:**
- No baseline metrics to compare against
- Regression detected in any eval category
- A/B test shows cost/token increases > 15% (usually a sign of wordy, defensive prompting)
- Rollback procedure untested

---

## WHEN WRONG

**You'll see:**
- Acceptance rate drops post-launch, user corrections spike
- Latency increases (prompt got too long, model overthinking)
- Cost per output climbs (defensive language made output verbose)
- Users report hallucinations they didn't see before
- Regeneration rate increases (users don't trust the output)

**Recovery:**
- Trigger immediate rollback (< 5 min)
- Investigate: what in the new prompt caused this?
- Look at the diff carefully. Usually it's one of:
  - Too much instruction (model got confused)
  - Removed a critical example (model lost signal)
  - Changed tone/framing (affected reasoning path)
- Iterate the prompt with your eval suite first, then re-A/B test

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
