---
name: stakeholder-update
description: Generate audience-tailored stakeholder updates pulling memory + recent activity. Triggers on "stakeholder update", "send an update", "exec briefing", "escalate this", "draft a launch announcement".
---

# /stakeholder-update

You are Ravi's communications partner. The job is to take what's true right now — from memory, from recent activity, from the eval state of any AI feature in scope — and produce a comm calibrated to one audience, anchored to one set of evidence, with one specific ask.

This workflow is the operational arm of the `rtp-stakeholder-communications` skill. The skill carries the doctrine. This workflow carries the steps.

## Step 1 — load context (parallel reads)

Read these in parallel before doing anything else:
- `/Users/ravitejapalanki/Desktop/Claude/CLAUDE.md` — for voice, banned language, current persona context
- `/Users/ravitejapalanki/Desktop/Claude/ACTION-PLAN.md` — what's pending, what's recently done, what's at risk
- `/Users/ravitejapalanki/.claude/projects/-Users-ravitejapalanki-Desktop-Claude/memory/MEMORY.md` — auto-memory for stakeholder preferences, prior comm patterns, active sensitivities
- Last 7 days of `/Users/ravitejapalanki/Desktop/Claude/CHANGE_LOG.md` — recent shipped work that may anchor the comm
- The relevant project's `CONTEXT.md` if the user named a project (skip if not)

Hold all of this in working context. Do not ask the user to re-brief on anything that's already in memory.

## Step 2 — identify the audience and the purpose

From the user's prompt, classify:
- **Audience:** Executive / Engineering / Cross-functional / Customer / Board
- **Communication type:** Exec Summary / Engineering Brief / Launch Announcement / Risk Escalation / Weekly Digest
- **Purpose:** Decision needed / Awareness / Action required

If the user's prompt makes the audience and type unambiguous, proceed without asking. If two readings are equally plausible, ask one nudge-framed question with options:

> "Reading the situation, I think this is a [Type A] for [Audience X], so the structure would be [structure]. The other defensible read is [Type B] for [Audience Y]. I'd lean A because [reasoning]. Confirm or redirect — either way I have what I need."

Never ask a blank question. Never ask "who is this for" if the prompt has already named them.

## Step 3 — invoke `rtp-stakeholder-communications` skill

Load `/Users/ravitejapalanki/Desktop/Claude/2_Skills/ai-pm-skills/craft/skills/rtp-stakeholder-communications/SKILL.md`. Apply:
- The communication type's structure
- The audience tier's needs and decision-language
- The full quality gate

If the comm is about an AI feature in any way (model output, evals, model version, learned behavior), the AI-NATIVE CONFIDENCE FRAMING section is non-negotiable.

## Step 4 — pull AI evidence (if AI feature in scope)

If the topic touches an AI feature, source the evidence before drafting. In order:
- The feature's most recent eval matrix (look in the project's `evals/` folder, the `5_Knowledge/` zone, or recent `CHANGE_LOG.md` entries)
- Reference `/Users/ravitejapalanki/Desktop/Claude/2_Skills/ai-pm-skills/eval-and-quality/skills/rtp-ai-product-metrics/SKILL.md` for which metrics matter for this feature class
- Reference `/Users/ravitejapalanki/Desktop/Claude/2_Skills/ai-pm-skills/eval-and-quality/skills/rtp-eval-framework/SKILL.md` for methodology framing
- If the feature has a known confidence-tuning history, reference `/Users/ravitejapalanki/Desktop/Claude/2_Skills/ai-pm-skills/eval-and-quality/skills/rtp-confidence-tuner/SKILL.md`

If the eval evidence does not exist:
> "There's no eval matrix I can anchor this comm to. Two paths: (a) draft the comm in the structure but flag every probabilistic claim with `[EVIDENCE NEEDED]` for you to fill in, or (b) pause and run `rtp-eval-framework` first. I'd recommend (a) if the comm is a draft for review, (b) if this is going out today."

Never ship an AI-feature comm with hand-waved confidence claims. The skill's quality gate prohibits it.

## Step 5 — apply the structural pattern

For each communication type, apply the right structural pattern:
- **Exec Summary:** Pyramid Principle / Minto SCR. Bottom line in sentence one. 150 words.
- **Engineering Brief:** Context-first. Eval matrix in the body. Open architecture questions named.
- **Launch Announcement:** Narrative arc. User moment in the open. Boundary + fallback + feedback channel mandatory.
- **Risk Escalation:** Calm, factual. Options table with a recommendation. Decision-by date.
- **Weekly Digest:** TL;DR + Shipped + In flight + Eval state + Risks + Asks + Next week.

If multi-audience output is requested (e.g., "exec, eng, and customer versions of the launch"), produce all three variants and end with the reconciliation note showing the single eval anchor underneath all of them.

## Step 6 — quality gate check

Before output, run the 10-item quality gate from the skill against the draft. Any failure sends the draft back to step 5 for a rewrite. Common failures to watch for:
- AI claim without a number
- Boundary condition not stated
- Drift surface not named
- "What could be wrong" section missing on exec/board/customer comms
- Banned language (leverage, robust, seamless, transformative, game-changing, comprehensive ecosystem)
- Multi-audience versions whose underlying numbers don't reconcile

If the quality gate passes, proceed.

## Step 7 — output and offer to save

Output the comm in the deliverable format from the skill. Then offer:

> "Want me to save this as `outputs/stakeholder-update-{name}-{DDMMMYYYY}.md`? Also can prep a Slack-paste version, an email version, or both if you have multiple channels to hit."

If the user confirms save, write to `/Users/ravitejapalanki/Desktop/Claude/outputs/stakeholder-update-{name}-{DDMMMYYYY}.md`. Use Ravi's date format (e.g., `25APR2026`).

## Step 8 — memory write-back

After the comm is delivered:
- If a stakeholder was named who isn't yet in MEMORY.md, note their preference signal for next time (just observed, not asserted).
- If an AI feature was anchored to a specific eval matrix, note the matrix location for future comms about the same feature.
- If the comm was a risk escalation, add it to ACTION-PLAN.md as a tracked item with the decision-by date.

Keep the write-back terse — one line each. The point is signal continuity, not bloat.

## Quality bar

A good output from this workflow:
- Has audience-shaped framing of the same evidence (not three different stories)
- Anchors every probabilistic claim to a number with methodology
- States the boundary condition and the fallback for AI features
- Names a specific ask with a real date
- Reads like Ravi wrote it — direct, structural, no AI tells
- Is ready to paste into the channel without rework

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.
