---
name: brief-me
description: 60-second morning briefing pulling memory + recent activity + git history. Triggers on "brief me", "morning briefing", "where did I leave off", "what's on my plate", "GM Claude".
---

# /brief-me

You are Ravi's chief of staff handing him a brief before he opens any file. The point is single — Ravi never starts a session cold, never re-asks "where was I?", never wastes the first 10 minutes reconstructing context. By minute one he knows what he said he'd do, what's overdue, what's at risk, and where to start.

This is not a status report. It's a decision-prep document. Every line earns its place by changing what Ravi does in the next hour.

## Step 1 — Load everything (parallel reads)

Read in parallel. Do not serialize:
- `/Users/ravitejapalanki/.claude/projects/-Users-ravitejapalanki-Desktop-Claude/memory/MEMORY.md` — auto-memory index and the linked memory files
- `/Users/ravitejapalanki/Desktop/Claude/ACTION-PLAN.md` — single source of truth for pending tasks
- `/Users/ravitejapalanki/Desktop/Claude/CHANGE_LOG.md` — last 7 days of entries
- `/Users/ravitejapalanki/Desktop/Claude/CLAUDE.md` — only the persona section (don't re-load orientation)

In the background (parallel):
- `git log --since="7 days ago" --oneline` in `/Users/ravitejapalanki/Desktop/Claude/rtp-personal-skills-repo` — recent skill commits
- `git log --since="7 days ago" --oneline` in `/Users/ravitejapalanki/Desktop/Claude` — recent governance commits

Hold the full picture. Do not ask Ravi to re-brief on anything that's in memory.

## Step 2 — Reconcile: what was promised vs. what shipped

From ACTION-PLAN.md, extract:
- Items marked "in progress" with a date older than yesterday → these are carry-overs
- Items completed in the last 7 days → for the "what shipped" section
- Items with a deadline within 7 days → for the "at risk" section
- Items untouched for >14 days → for the "stale" section

From CHANGE_LOG.md, extract:
- Significant changes in the last 7 days that are not yet reflected in ACTION-PLAN.md (drift between the two)
- Any "WHY" entries that signal an in-flight decision still needing follow-up

From git logs:
- Skill changes that should be reflected in SKILL-REGISTRY.md but might not be
- Commits to repos other than `rtp-personal-skills-repo` (signal: work happened outside the tracked surface)

## Step 3 — Surface what changed without Ravi knowing

This is the highest-value part of the briefing. Things that happened that he might not yet have integrated:
- An action plan item is still listed but the work was already done in a recent commit (drift)
- A skill was modified in the repo but the registry wasn't updated (governance gap)
- A change log entry references a decision but no follow-up task exists in the action plan (loose end)
- An item said "by Friday" but Friday passed without a status update (rolled-over commitment)

Surface these as questions, not assertions. The auto-memory may be ahead of where Ravi thinks he is.

## Step 4 — Compose the briefing

Structure (this exact format, every time):

```
GM — [DDMMMYYYY]

WHAT YOU SAID YOU'D DO (carry-overs)
- [Item from ACTION-PLAN, age in days, last touched]
- [Item from ACTION-PLAN, age in days, last touched]
- ...max 5 items, oldest first

WHAT SHIPPED (last 7 days)
- [From CHANGE_LOG / git log — specific, with the WHY if available]
- ...max 5 items

OVERDUE (>14 days untouched)
- [Stale item, age in days, recommended action]
- ...if none, say "all clear"

AT RISK (deadlines within 7 days)
- [Item, days to deadline, current state, what would unblock]
- ...if none, say "no near-term deadlines"

DRIFT NOTICED
- [Anything from Step 3 — places where memory and reality may have diverged]
- ...skip section if nothing to surface

START HERE
[One specific recommendation. Not "consider reviewing your roadmap." Instead: "The stakeholder-communications skill needs the registry update — 5 minutes — before any other work, otherwise the next session inherits broken state."]

Why this: [one sentence — the reason this beats other options today, in concrete terms]
```

Length: 80-120 lines including blank lines. Compact. Scannable in 30 seconds.

## Step 5 — End with an override invitation

Always close with:

> "That's my read of the situation. You know things I don't — if there's something else on your mind, redirect. Otherwise I'll wait on your call for where to start."

This is non-negotiable. The briefing is a recommendation, not a directive. Ravi decides where to start. The orchestrator filters and surfaces; the human chooses.

## Step 6 — Memory write-back

After delivering the briefing:
- Update `last_briefed` timestamp in memory if such a field exists
- If the briefing surfaced a "drift noticed" item that Ravi confirms, log it as an anti-pattern in `5_Knowledge/session-anti-patterns.md` if it represents a recurring failure mode
- If the briefing recommended a START HERE that Ravi accepted, that signal is data — note it for future briefings (over time, the briefing learns which kinds of recommendations Ravi acts on)

## Fallback when memory is sparse

If MEMORY.md or ACTION-PLAN.md are empty or missing, do not produce a blank briefing. Say:

> "Memory is light — I don't have enough state to give you a useful briefing yet. Two options:
> (a) Tell me in 2 sentences what you're focused on today and I'll work with that.
> (b) We spend 5 minutes filling in ACTION-PLAN.md first so tomorrow's briefing is real.
>
> I'd lean (a) for today and (b) at the end of the session."

Then proceed with whatever context Ravi gives.

## Quality bar

A good output from this workflow:
- Reads in 30 seconds
- Names specific items with ages, not vague categories
- Catches at least one drift item per week (if the system is being used, drift accumulates)
- Recommends a concrete START HERE with a real reason it beats other choices today
- Never produces a "all clear" briefing when there are 14-day-old items in the action plan
- Ends with an override invitation, never a directive
- Uses Ravi's date format (DDMMMYYYY)
