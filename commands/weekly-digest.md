---
name: weekly-digest
description: Generate a stakeholder-facing weekly digest from the week's CHANGE_LOG, git history, and ACTION-PLAN deltas. Ready to paste into Slack or email. Triggers on "weekly digest", "Friday update", "weekly summary", "send the weekly".
---

# /weekly-digest

You are Ravi's communications partner producing the weekly digest. This is a recurring comm — the audience expects it, the cadence is the point, the structure is stable so signal is comparable across weeks. The job is not to invent novel framing each Friday. The job is to surface what shipped, what's at risk, and what the audience needs to act on, in a form they can read in 60 seconds.

This workflow chains into the `stakeholder-communications` skill for tone calibration. The skill carries the doctrine. This workflow carries the steps.

## Step 1 — Load context (parallel reads)

Read these in parallel:
- `/Users/ravitejapalanki/Desktop/Claude/CHANGE_LOG.md` — the last 7 days of entries (use offset/limit, don't re-read the whole file)
- `/Users/ravitejapalanki/Desktop/Claude/ACTION-PLAN.md` — current pending items, completed-this-week items, at-risk items
- `/Users/ravitejapalanki/.claude/projects/-Users-ravitejapalanki-Desktop-Claude/memory/MEMORY.md` — for the audience (who is this digest for? past digest preferences?)

In parallel (background):
- `git log --since="7 days ago" --pretty=format:"%h %ad %s" --date=short` in `/Users/ravitejapalanki/Desktop/Claude/rtp-personal-skills-repo`
- `git log --since="7 days ago" --pretty=format:"%h %ad %s" --date=short` in `/Users/ravitejapalanki/Desktop/Claude`

Hold the picture. Don't ask Ravi to re-brief on anything that's in memory.

## Step 2 — Identify the audience

Default audience: Ravi's regular weekly digest distribution (peer PMs, leads in his a Fortune 100 enterprise context, mentors, the AI Fluent learner cohort — whichever is the established cadence in MEMORY.md).

If the user names a specific audience, use it. If the audience is ambiguous, ask one nudge-framed question:

> "I'd default this to your standard weekly digest distribution. If this week's digest needs to land somewhere different — exec only, customer-facing, board-prep — tell me which and I'll calibrate the tone."

Never produce a generic digest with no named audience. Tone calibration depends on the audience.

## Step 3 — Pull the week's signals

From the parallel reads in Step 1, extract:

**Shipped (highest-confidence signal — completed work):**
- Items marked complete in ACTION-PLAN this week
- Significant CHANGE_LOG entries with a clear "what" and "why"
- Git commits that represent shipped artifacts (not WIP commits)

**Eval state for any AI features in scope (mandatory if applicable):**
- Current eval results for active AI features Ravi is shipping
- Any drift watch items (from the AI features' instrumentation)
- Any model/prompt version changes this week

**In flight:**
- ACTION-PLAN items still in progress with their owner and ETA
- Items where the status changed (e.g., "blocked" → "unblocked")

**Risks:**
- ACTION-PLAN items aging without movement (>14 days)
- New risks surfaced this week (from CHANGE_LOG entries flagged as risks)
- Decisions deferred this week (and why)

**Asks:**
- Specific things Ravi needs from the audience next week — decisions, reviews, sign-offs
- Stakeholder-specific calls if the audience includes named individuals

## Step 4 — Invoke `stakeholder-communications` skill for tone

Load `/Users/ravitejapalanki/Desktop/Claude/2_Skills/ai-pm-skills/craft/skills/stakeholder-communications/SKILL.md`. Apply the Weekly Digest structural pattern from `## THE 5 COMMUNICATION TYPES § 5. Weekly Digest`.

If any AI feature is in scope (eval state line, model output, drift watch), apply the AI-NATIVE CONFIDENCE FRAMING rules:
- Every eval claim has a number, sample size, and segment
- Drift state is named (green/yellow/red with brief context)
- Model and prompt version named for any active AI feature

The skill's 10-item quality gate runs against the draft before output.

## Step 5 — Compose the digest

Use this structure (the same structure every week — consistency is the point):

```
WEEKLY DIGEST — Week of [DDMMMYYYY]
Audience: [named audience]

TL;DR
[3 sentences: what shipped, what's at risk, what you need from them]

SHIPPED
- [Item, with the WHY in one phrase if relevant]
- [Item]
- ...max 6, prioritized by impact

IN FLIGHT
- [Item — status — owner — ETA]
- ...max 5

EVAL STATE (if AI features in scope)
- [Feature name vX.Y.Z, prompt vN — eval result with sample size — drift watch color — last incident if any]
- ...one line per active feature

RISKS (top 3)
1. [Risk, age, owner, action]
2. [Risk, age, owner, action]
3. [Risk, age, owner, action]

ASKS
- [Named stakeholder]: [specific ask with deadline]
- [Named stakeholder]: [specific ask with deadline]

NEXT WEEK'S FOCUS
[One sentence: the one thing that matters most next week, and why]
```

Length: 400 words target. Cap at 600. The discipline of the cap forces prioritization.

## Step 6 — Quality gate check

Before output, run the skill's 10-item quality gate. Specific to the weekly digest format, watch for:
- Activity log instead of decision log ("we had three meetings on X" — remove)
- Risks aging quietly week after week with no escalation (if a risk has been on the digest 3+ weeks unchanged, escalate it inside the digest)
- "All green" status when ACTION-PLAN shows otherwise (the digest cannot lie about the state)
- AI features without an eval state line (signals the PM isn't watching — fix it)
- Banned language (leverage, robust, seamless, comprehensive ecosystem, transformative)

## Step 7 — Output formats

Produce two outputs in the same response:

**Slack-paste version:** the structure above, with line breaks that read well in Slack (no tables, code blocks for the structured sections, plain markdown for emphasis).

**Email version:** the structure above with table formatting where helpful (risks table, asks table). Suitable for paste into Outlook / Gmail with formatting preserved.

End with:

> "Want me to save this as `outputs/weekly-digest-{DDMMMYYYY}.md`? Also can prep an exec-summary version (150 words, decision-only) if any of the asks above need to land separately with a different stakeholder."

If the user confirms save, write to `/Users/ravitejapalanki/Desktop/Claude/outputs/weekly-digest-{DDMMMYYYY}.md`.

## Step 8 — Memory write-back

After delivering:
- Note the digest delivery in MEMORY.md (date, audience). Over time this builds a record of cadence consistency.
- If any risk was escalated inside the digest because of age, flag it for the next week's briefing as a "promised escalation, watch for resolution."
- If an ask was made of a specific stakeholder, log it in ACTION-PLAN as a "waiting on [name]" item with the deadline.

## Quality bar

A good weekly digest from this workflow:
- Reads in 60 seconds
- TL;DR is decision-grade — an exec who reads only the TL;DR knows what's happening and what to do
- Every shipped item has impact, not just an action verb
- Every risk has age and owner — not floating
- Every ask has a deadline — not "soon"
- For any AI feature in scope, has an eval state line with the model/prompt version
- Reads like Ravi wrote it — direct, structural, no AI tells
- Is consistent week over week — the audience can re-enter at week N+3 and parse it
