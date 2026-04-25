---
name: triage-feedback
description: Ingest a batch of user feedback, classify and score it, and produce ranked routing recommendations.
---

# /triage-feedback

Take an unstructured pile of user feedback (CSV, Slack export, Notion list, NPS comments, support tickets) and produce a ranked report with routing recommendations — including the AI-failure axis that frequency-only triage misses.

**Timeline:** 1-3 hours for 50-200 items, 4-8 hours for 200+ items
**Output:** A triage report with classified themes, scores, AI-failure breakdown, and routing to fix teams

## When to use

- Triaging a quarter's worth of support tickets to set the next sprint's priorities
- Synthesizing in-product feedback after a feature launch
- Processing a batch of NPS comments
- Reviewing customer success notes for systemic issues
- The team is debating "what are users actually saying?" with different people pointing to different items

## When NOT to use

- Volume below 20 items — read each one individually instead
- The product has no AI features and a simpler 3-axis triage is sufficient
- The "feedback" is internal stakeholder complaints, not user feedback (use stakeholder-mapping)

## Input

Provide one of:
- A pasted list of feedback items
- A file path (CSV, JSON, TXT, Markdown)
- A connected source ("pull from Intercom," "Notion list at [URL]," etc.)

If empty, ask: "Paste your feedback, point me to a file, or tell me which source to pull from."

## The chain

```
ingest  →  feedback-triage  →  failure-modes cross-check  →  ranked routing
(Step 1)     (Step 2)             (Step 3)                     (Step 4)
```

### Step 1 — Ingest and Normalize

Detect the format and normalize to a flat list:
- **Plain text/list:** one feedback entry per line
- **CSV/TSV:** identify the feedback column; preserve metadata (date, severity, user tier, customer)
- **JSON:** extract the text field; note structured fields
- **Transcript:** split into distinct feedback points (one paragraph may contain multiple)
- **Slack/Notion export:** strip metadata, preserve user attribution if available

For volume:
- <50 items: single-pass analysis
- 50-200: cluster first, then score
- 200+: spawn parallel analysis (batches of ~50), then merge

Preserve a unique ID per item so the output can trace back to the source.

### Step 2 — Run feedback-triage

Apply the `feedback-triage` skill. For every item or theme:

**Classify** into one of six categories:
1. UX Issue (non-AI)
2. Performance Issue
3. AI Failure
4. Edge Case
5. Out-of-Scope Request
6. Future Capability Signal

**Score** on the 4-axis scale:
- Frequency (0-5)
- Severity (0-3)
- Strategic Fit (0-2)
- AI-Failure Flag (0-1)
- Total (0-11)

**Sub-classify AI Failures** into:
- Hallucination
- Over-Confidence
- Under-Confidence
- Wrong Refusal
- Wrong Tool / Wrong Routing
- Latency Failure

**Cluster into themes** when items share underlying issue. A theme requires 2+ separate sources mentioning the same problem (or 1 high-severity instance for catastrophic categories).

### Step 3 — failure-modes Cross-Check

For every AI Failure theme, cross-reference with the `failure-modes` taxonomy. This step is the bridge between user-reported failures and the engineering response.

For each AI failure theme, fill out:

| Theme | Failure-Modes Type | Detection Latency | Cost Asymmetry | Recommended Mitigation |
|---|---|---|---|---|
| ... | Fabrication / Conflation / etc. | Immediate / Delayed / Silent | Low / Medium / High / Critical | Calibration / Grounding / Refusal-tuning / etc. |

This cross-check is what turns the triage report into an engineering handoff. The AI eval team needs to know not just "users complained about X" but "this maps to failure type Y, which has detection latency Z, and the fix is W."

### Step 4 — Ranked Routing

Produce the final routing table. Each high-priority theme (score ≥ 5 OR AI-failure flag = 1) gets:

| Theme | Category | Score | Sub-type (if AI) | Route to | Fix Protocol | Cycle Time |
|---|---|---|---|---|---|---|

Routes:
- **Now — current sprint:** Score 8-11, blocking, AI-failure with high cost asymmetry
- **Next — backlog:** Score 5-7, needs scoping
- **Experiment first:** Score 5-7, uncertain solution
- **Discovery cycle:** Future capability signals (don't route to fix; route to /discover)
- **Decline / monitor:** Low score, anti-persona, contradicts deliberate decision

For "Experiment first" items, recommend:
- Hypothesis
- Cheapest test
- Metric

## The triage report

```markdown
# Feedback Triage: [period]

## Executive summary
[Top 3 pain points in one paragraph. The AI-failure rate. The routing recommendations.]

## Classification breakdown
| Category | Count | % of total |
|---|---|---|
| UX Issue | ... | ... |
| Performance | ... | ... |
| AI Failure | ... | ... |
| Edge Case | ... | ... |
| Out-of-Scope | ... | ... |
| Future Capability Signal | ... | ... |

## Themes ranked by score (top 10)
[Table with frequency, severity, strategic fit, AI-failure flag, total, route]

## AI Failure breakdown
[Sub-types with counts, top failure-modes mapping, top recommended mitigations]

## Routing recommendations
[Now / Next / Experiment first / Discovery / Decline]

## Future capability signals (handoff to /discover)
[Items that aren't bugs — they're inputs to the next discovery cycle]

## What to ignore (and why)
[Explicit declines: single mentions, anti-persona, contradicts decision]

## Trend alert
[Any theme that's growing or new compared to last triage period]

## Closing question
[For the team: "Which theme surprised you most? Are we hearing what users are saying, or what we want to hear?"]
```

## Quality bar

A complete triage:
- Classifies every item (no "miscellaneous" bucket)
- Sub-classifies every AI failure
- Cross-references AI failures with failure-modes
- Has unambiguous routing for every high-priority theme
- Includes a "what to ignore" section
- Surfaces future capability signals separately (not routed to fix)
- Reports the AI failure rate as a metric, not just a count

## Closing protocol

Before closing the triage cycle:
1. State the AI failure rate and whether it's trending up/down
2. State the top 3 routing recommendations
3. Tag future capability signals for the next /discover run
4. Ask: "Are any of these themes the same complaint we triaged last cycle that didn't get fixed? If so, why?"

The third question is the hardest one. Repeated unfixed themes are the strongest signal that the routing isn't actually triggering work — and that's the upstream problem to fix before running the next triage.
