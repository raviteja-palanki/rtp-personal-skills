---
name: ai-prd-flow
description: The PRD-writing motion for AI features. Lighter than /design-ai-feature — assumes strategic gates are passed and you're ready to spec. Triggers on "write the AI PRD," "spec this feature," "PRD for [AI feature]."
version: 1.0.0
author: RTP (Ravi Teja Palanki)
chains:
  - rtp-problem-ai-fit
  - rtp-ai-use-case-readiness
  - rtp-jtbd-analysis
  - rtp-ai-prd
  - rtp-ship-decision
---

# /ai-prd-flow
**The PRD motion for AI features. Pre-tested before engineering review.**

> "A PRD that engineering pushes back on three times wasn't ready. A PRD that engineering implements as written had the gates run before the doc was written." — RTP

---

## When this runs

Trigger phrases: "write the AI PRD," "spec this feature," "PRD for [AI feature]."

Use when strategic gates are already passed (you ran `/design-ai-feature` or equivalent due diligence) and the feature scope is decided. This is documentation, not exploration.

Do not use this for a new AI idea that has not been validated strategically, which belongs in `/design-ai-feature`; for a purely deterministic feature, which belongs in `pm-execution:create-prd`; or for documenting something already shipped, which belongs in `/retro`.

---

## Input

If empty, ask:
1. "What's the feature and what user problem does it solve?"
2. "What level of autonomy was decided?" (L1-L6)
3. "Has the cost model and eval framework been built?"

If the user can't answer (2) or (3), redirect to `/design-ai-feature` first.

---

## Step 1 — validate with `rtp-problem-ai-fit`

**Skill: `rtp-problem-ai-fit`**

Confirm AI is still the right tool. 30-second sanity check if `/design-ai-feature` already ran. Verify:
- The problem still requires AI (rules wouldn't solve 80%+)
- User tolerance for variability hasn't changed
- The failure mode is still recoverable

**STOP signal:** Any of the three answers flipped. Loop back to `/design-ai-feature`.

---

## Step 2 — define with `rtp-ai-use-case-readiness`

**Skill: `rtp-ai-use-case-readiness`**

Score across four dimensions:

| Dimension | Pass criterion |
|---|---|
| Data readiness | Input data exists at production volume, structured enough |
| Model capability | At least one credible reference for similar task in production |
| User tolerance | Research confirms users accept the failure rate at the chosen autonomy level |
| Operational readiness | Eval, monitoring, cost controls scoped (not yet built is fine) |

**STOP signal:** Any dimension fails. Capture the gap, route back to discovery.

---

## Step 3 — define with `rtp-jtbd-analysis`

**Skill: `rtp-jtbd-analysis`**

Frame the feature as a Job-to-Be-Done, not a feature description:

- **Situation:** When [user is in this context]
- **Motivation:** I want to [achieve this outcome]
- **Outcome:** So I can [the deeper benefit, the why]
- **Pains:** What makes this hard today (the alternatives that fail)
- **Gains:** What "great" looks like (the bar the AI must clear)

The JTBD becomes the PRD's North Star. If a feature decision contradicts the JTBD, the JTBD wins or the JTBD changes — never both quietly.

**Note:** If `rtp-jtbd-analysis` skill isn't yet built, fall back to `pm-product-discovery:rtp-opportunity-solution-tree` and capture the JTBD in plain language.

---

## Step 4 — produce with `rtp-ai-prd`

**Skill: `rtp-ai-prd`**

Assemble the AI-PRD. The 10 sections, in order:

1. **Problem & JTBD** — from Step 3
2. **AI Justification** — from Step 1, the 80% test result
3. **Use Case Readiness Scorecard** — from Step 2
4. **Autonomy Level** — L1-L6 with rationale (reference: `rtp-autonomy-spectrum`)
5. **Probabilistic Specification** — operations breakdown, confidence thresholds (show if >X%, clarify if Y-Z%, decline if <Y%), output format, prompt version
6. **Dual Success Metrics** — user outcome (task completion, time-to-value, satisfaction) AND AI-specific (accuracy by class, hallucination rate, false positive/negative, latency P50/P95, confidence calibration). Each metric: target + floor.
7. **Eval Acceptance Criteria** — references the golden set, LLM-as-judge prompts, regression detection. Every criterion testable.
8. **Failure Modes & Recovery** — per high-impact failure (hallucination, refusal, latency, cost, prompt injection): probability, consequence, detection, containment, recovery
9. **Cost Ceiling & Economics** — per-call target, daily ceiling, alert threshold, optimization plan if economics drift
10. **Improvement Flywheel** — implicit feedback (edits, regenerations), explicit feedback (thumbs), failure capture into eval set, iteration cadence

---

## Step 5 — validate with `rtp-ship-decision`

**Skill: `rtp-ship-decision`**

The four ship questions:
1. Are we solving the right problem? (JTBD intact, AI justified)
2. Can we measure success? (Acceptance criteria testable, golden set exists)
3. Can we afford this at GA? (Cost ceiling matches business model)
4. Can we recover when it breaks? (Failure recovery designed, not hoped for)

All yes, and the PRD is ready for engineering review.
Any no, and the gap gets documented. Then decide whether to ship with the risk tracked or fix it first.

---

## Output format

Single AI-PRD document. The 10 sections from Step 4, opened by an executive summary:

```
[Feature Name] AI-PRD
Owner: [PM name]  Date: [DDMMMYYYY]
Status: [Draft / Engineering Review / Approved]

Problem: [One sentence — the JTBD]
Autonomy: [L1-L6]
Why AI: [One sentence — the AI justification]
Acceptance bar: [pass rate %, latency, cost ceiling]
Top risks: [3 max, with mitigation]
Ship decision: [Ready / Ready with caveats / Not ready — gap list]
```

The full 10 sections follow. Engineering reads the executive summary first; if it doesn't answer "should I read this," the PRD isn't ready.

---

## Quality bar

A real `/ai-prd-flow` PRD has:
- A JTBD framing, not a feature description
- Dual success metrics (user outcome + AI-specific)
- Acceptance criteria that are testable, not aspirational
- Cost ceilings, not hand-waves
- Failure recovery, not "we'll handle it later"
- Autonomy level explicit, not implicit
- Passes rtp-ship-decision before engineering sees it

**The test:** Engineering reads it, has zero AI-specific questions left, and starts implementation. If they push back with "what happens at 60% confidence?" or "what's the rollback?", the PRD wasn't done.

---

## Cross-references

- **Run before this:** `/design-ai-feature` (strategic validation)
- **Run after this:** `/plan-launch` (launch coordination)
- **Run post-ship:** `/retro` (learning extraction)
- **Skill files used:** `rtp-problem-ai-fit`, `rtp-ai-use-case-readiness`, `rtp-jtbd-analysis`, `rtp-ai-prd`, `rtp-ship-decision`

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.
