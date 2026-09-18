---
name: design-ai-feature
description: A validation pass before any new AI feature is built. It runs seven skills in sequence, with stop conditions, before any code is written. Triggers on "design an AI feature," "should we build AI for X," "validate this AI idea."
version: 1.0.0
author: RTP (Ravi Teja Palanki)
chains:
  - rtp-problem-ai-fit
  - rtp-first-principles
  - rtp-autonomy-spectrum
  - rtp-determinism-compass
  - rtp-prompt-craft
  - rtp-eval-framework
  - rtp-cost-model
  - rtp-ai-ux-patterns
  - rtp-safety-by-design
  - rtp-ai-prd
---

# /design-ai-feature
**Run this before the build, not after it.** Each gate below is a question that is cheap to answer now and expensive to answer once the feature exists.

> "If you can't pass all ten gates with honest answers, you're not ready to write the PRD. You're ready to kill the idea or shrink the scope until it survives." — RTP

---

## When this runs

Trigger phrases: "design an AI feature," "should we build AI for X," "validate this AI idea," "is this an AI problem?"

Do not use this for an improvement to something already shipped, which belongs in `/retro`; for a UX change on a deterministic feature, which belongs in `pm-execution:create-prd`; or for exploration that is only research, which belongs in `/discover`.

---

## The structural insight

Most PMs jump from "let's build AI for X" straight to model selection or prompt design. They skip the question that matters: **is this even an AI problem, and at what autonomy level?**

The cost of skipping is high. AI features that ship without these gates fail in predictable ways:

| Gate skipped | Failure pattern in production |
|---|---|
| rtp-problem-ai-fit | Built ML for a problem rules would have solved at 1/100th the cost |
| rtp-autonomy-spectrum | Gave the AI L4 autonomy where L2 would have done, then faced a lawsuit over an irreversible action |
| rtp-determinism-compass | Mixed probabilistic and deterministic steps in one workflow, and behavior became unpredictable at scale |
| rtp-eval-framework | Shipped without acceptance criteria, so nobody can tell when the model has regressed |
| rtp-cost-model | Per-call cost × volume × margin = negative unit economics at GA |
| rtp-safety-by-design | Bolted guardrails on after launch, which broke the experience and did not fix the failure mode |

This workflow runs all ten gates in sequence. If any gate fails, the workflow halts and surfaces "here's why we shouldn't proceed."

---

## Input

The user invokes this with a feature description. If empty, ask:

1. "What user problem does this AI feature solve?" (one sentence)
2. "What's the expected daily volume?" (10 / 1K / 100K / 1M)
3. "Who absorbs the cost when it gets something wrong — the user, the company, a regulator?"

The third question routes the rest of the workflow. If the answer is "regulator," the safety and cost gates get tighter.

---

## Step 1 — gate: `rtp-problem-ai-fit`

**Skill: `rtp-problem-ai-fit`**

Run the AI fit check before anything else. The output is a 0-16 score across four dimensions:

- Unstructured input required (0-4)
- Output varies by context, can't be captured in fixed rules (0-4)
- Users tolerate imperfect accuracy in exchange for speed/scale (0-4)
- Failure mode is recoverable (0-4)

**STOP signal:** Score below 8. Output: "This isn't an AI problem. Rules, search, or heuristics will solve 80%+ at 1/100th the cost. Recommend killing the AI angle. If you still want to ship, here's the deterministic path: [...]"

**Pass signal:** Score 8+. Continue.

---

## Step 2 — gate: `rtp-first-principles`

**Skill: `rtp-first-principles`**

Strip the feature to its irreducible task. Vendor hype, competitor moves, "AI for everything" pressure — all out. What's the ONE atomic operation the user actually needs?

Classify the atomic operation: LOOKUP / TRANSFORM / CLASSIFY / GENERATE / DECIDE.

**STOP signal:** The atomic operation is LOOKUP and the user already has the data structured. AI is overkill. Recommend rules + search.

**Pass signal:** Atomic operation is non-trivial AND the input is genuinely unstructured. Continue.

---

## Step 3 — gate: `rtp-autonomy-spectrum`

**Skill: `rtp-autonomy-spectrum`**

Place the feature on the 7-level spectrum:

| Level | Who decides | Who acts | Example |
|---|---|---|---|
| L0 | Human | Human | Status quo, no AI |
| L1 | Human | Human (AI suggests) | Autocomplete |
| L2 | Human (AI proposes) | Human | Email draft suggestions |
| L3 | Human (AI executes pre-approved actions) | AI | "Send this email after I click send" |
| L4 | AI (reversible actions) | AI | Auto-categorize emails into folders |
| L5 | AI (irreversible, low-stakes) | AI | Auto-archive after 30 days |
| L6 | AI (irreversible, high-stakes) | AI | Trade execution, refund issuance |

**The trap:** Most teams reverse-engineer autonomy from capability. "The model CAN do L4, so let's let it do L4." Wrong direction. Start from consequence: if the AI does this wrong, what's the damage? Who absorbs it? Can we undo it?

**STOP signal:** Recommended level is L4+ AND the team hasn't designed:
- Trip-wire / kill switch
- Human override path
- Audit log per action
- Rollback mechanism

If any of those four are missing, this is L3 max until they're built.

**Pass signal:** Autonomy level matches risk profile. Continue. Capture the level explicitly — every downstream gate references it.

---

## Step 4 — gate: `rtp-determinism-compass`

**Skill: `rtp-determinism-compass`**

Position the feature on the probabilistic vs. deterministic axis. The failure mode this gate catches: **mixing them in one workflow.**

Three patterns:

1. **Pure deterministic** — Use rules. AI is the wrong tool.
2. **Pure probabilistic** — AI is the right tool. Build the eval surface.
3. **Hybrid (the danger zone)** — Some steps need 100% accuracy (deterministic), others tolerate variability (probabilistic). The bug is letting the probabilistic step gate the deterministic one.

**Example failure:** A document parser uses AI to classify document type, then routes to a deterministic extractor. If the classifier is wrong, the deterministic step extracts the wrong fields with 100% confidence. User sees "100% accurate extraction" of garbage data.

**STOP signal:** Hybrid workflow without explicit handoff contracts between probabilistic and deterministic steps. Each handoff needs:
- Confidence threshold for the probabilistic output
- Fallback when below threshold (human review, alternate path, refusal)
- Logging at the boundary

**Pass signal:** The workflow is one of the three patterns AND every probabilistic-to-deterministic handoff has a contract. Continue.

---

## Step 5 — gate: `rtp-prompt-craft`

**Skill: `rtp-prompt-craft`**

Only runs if Step 4 said "probabilistic." Skip otherwise.

Design the prompt as a product artifact, not a string. Required elements:

- Role and identity for the model
- Context (what it knows about the user, the product, the moment)
- Task (the atomic operation from Step 2)
- Constraints, meaning what it must never do
- Output format (JSON schema, structured tags, or strict freeform contract)
- 2-3 few-shot examples covering the common case AND one edge case
- Refusal language for inputs outside scope

**Versioning:** Every prompt gets a version number. Every production request logs the prompt version. Without this, you can't diff regressions.

**STOP signal:** Output format is freeform text AND downstream code parses it with regex. That's a ticking time bomb — first model upgrade breaks production. Recommend: use structured output (JSON mode, tool use) or build a tolerant parser with explicit fallbacks.

**Pass signal:** Prompt is versioned, structured output, edge cases covered. Continue.

---

## Step 6 — gate: `rtp-eval-framework`

**Skill: `rtp-eval-framework`**

Build the eval surface BEFORE the feature. Most teams build the feature first, then realize they can't measure quality. By then, you've shipped fragile.

Required outputs:

| Element | Minimum bar |
|---|---|
| Eval dimensions | 3-5 dimensions, each with definition and pass/fail criteria |
| Golden set | 20-50 curated examples with known-good outputs |
| Edge cases | 10-20 adversarial or unusual inputs |
| Failure cases | 5-10 inputs designed to trigger known failure modes |
| LLM-as-judge prompts | One per dimension that can't be measured automatically |
| Eval pipeline | Automated run on every prompt or model change |

**Reject Likert scales for production evals.** Pass/fail is honest. "Rated 3.4 out of 5" hides whether the output worked or didn't.

**STOP signal:** No golden set exists AND no plan to build one within the first sprint. You're shipping blind.

**Pass signal:** Golden set scoped, eval pipeline planned, regression detection defined. Continue.

---

## Step 7 — gate: `rtp-cost-model`

**Skill: `rtp-cost-model`**

Model production economics before scaling. Required inputs: avg input/output tokens per call, model tier, retrieval cost (if RAG), daily volume at GA (not pilot), revenue or value per call.

**The 1000x problem:** Pilot volume is fine. GA volume blows up cost by 100-10,000x. Run the math at GA volume. If it's negative, you don't have a business — you have a cool demo.

**Cost optimization levers** (apply in order): caching common queries (10x), model routing (3-5x), output length constraints (2x), batching non-real-time (50%), prompt compression (1.5-2x).

**STOP signal (full path):** Unit economics negative at GA volume AND no clear optimization path. Kill or pivot.
**STOP signal (fast path):** Internal-only, <100 daily calls, known cost absorber. Skip detailed model — capture per-call ceiling, daily ceiling, alert threshold.
**Pass signal:** Unit economics positive OR credible optimization path exists. Continue.

---

## Step 8 — gate: `rtp-ai-ux-patterns`

**Skill: `rtp-ai-ux-patterns`**

How users experience probabilistic output. Most AI features fail here, not in the model. Required:

- **Set expectations** — tell users what the AI can and can't do in the UI, not in a help doc
- **Show confidence** — when uncertain, show it. False confidence is the worst trust failure.
- **Enable correction** — every correction is training data and trust repair in one motion
- **Progressive disclosure** — start simple, let users drill deeper
- **Graceful degradation** — when AI fails, the experience is still useful (deterministic → human handoff → "we'll follow up")

**STOP signal:** No fallback for when the model returns nothing useful. Spinner forever or generic error is a UX failure dressed as an AI failure.
**Pass signal:** Each pattern has a designed answer. Continue.

---

## Step 9 — gate: `rtp-safety-by-design`

**Skill: `rtp-safety-by-design`**

Guardrails and human-in-the-loop. The autonomy level from Step 3 determines the depth of this gate.

Required outputs by autonomy level:

| Level | Required safety design |
|---|---|
| L1-L2 | Refusal language for out-of-scope inputs. Logging. |
| L3 | All of L1-L2 + explicit confirmation step before action. Audit log. |
| L4 | All of L3 + reversibility guarantee (undo within X seconds). Per-action audit log. Rate limits. |
| L5 | All of L4 + monitoring dashboard. Alert on anomaly. Human review queue for X% sample. |
| L6 | All of L5 + kill-switch with named owner. Pre-approved escalation paths. Compliance review. |

**STOP signal (full path):** Autonomy level is L4+ AND any of the corresponding safety controls are missing. Pause the feature. Build the safety layer first.

**STOP signal (fast path):** Internal-only, low-stakes, L1-L2. Skip detailed safety review. Capture only: refusal language, logging, escalation contact.

**Pass signal:** Safety controls match autonomy level. Continue.

---

## Step 10 — produce with `rtp-ai-prd`

**Skill: `rtp-ai-prd`**

If all gates passed, assemble the AI-PRD. The PM doesn't rewrite — Steps 1-9 already produced the inputs. The PRD includes: problem and AI justification (Steps 1-2), autonomy level (Step 3), determinism architecture (Step 4), prompt spec with version and golden examples (Step 5), eval framework with acceptance criteria (Step 6), unit economics and cost ceiling (Step 7), UX patterns and fallback design (Step 8), safety controls and kill-switch design (Step 9), improvement flywheel, ship decision criteria.

For the lighter PRD-only motion, use `/ai-prd-flow`.

---

## Output format — one-page decision summary

After all gates run, produce this single page. The PRD is the appendix.

```
AI Feature Decision: [Feature Name]
Date: [DDMMMYYYY]
Owner: [PM name]

DECISION: [BUILD / KILL / PIVOT]

Rationale: [2-3 sentences. What the gates revealed. Why this decision.]

Gates passed: [N / 9]
Gates with concerns: [list, with severity]

Autonomy level: [L1-L6]
Determinism pattern: [Pure prob / Pure det / Hybrid]
Cost ceiling: [$/day at GA]
Eval acceptance bar: [pass rate %]
Kill switch: [Yes/No, with owner]

If BUILD: AI-PRD attached. Next step: engineering review.
If KILL: Documented for future reference. Next step: alternative path memo.
If PIVOT: Specific changes that would unblock. Next step: re-run gates [list].
```

---

## The fast path (internal, Low-Stakes features only)

Triggers: feature is internal-only, low-stakes, expected volume <100/day, autonomy L1-L2 only.

Fast path skips:
- Step 7 (rtp-cost-model) — capture per-call ceiling and daily ceiling, no full model
- Step 9 (rtp-safety-by-design) — capture refusal language, logging, escalation contact

Fast path keeps:
- All other gates (rtp-problem-ai-fit, rtp-first-principles, rtp-autonomy-spectrum, rtp-determinism-compass, rtp-prompt-craft, rtp-eval-framework, rtp-ai-ux-patterns)

Fast path output: same one-page summary, with cost and safety as "fast path" notes.

---

## Quality bar

A real `/design-ai-feature` run produces:

- A binary decision (build / kill / pivot), not a maybe
- The autonomy level made explicit, not implicit
- Cost economics validated at GA volume, not pilot
- An eval surface designed before the feature, not after
- A safety layer that matches the autonomy level
- A PRD ready for engineering review, with no open AI-specific questions

**The test:** If an L4 PM at Anthropic reviewed the output, would they say "this team has done the work"? If not, run the gates again.

---

## Cross-references

- **Universal Skill Protocol:** `2_Skills/ai-pm-skills/UNIVERSAL-SKILL-PROTOCOL.md`
- **Orchestrator deep reference:** `2_Skills/ai-pm-skills/rtp-orchestrator/SKILL.md`
- **Related workflows:** `/ai-prd-flow` (lighter), `/plan-launch` (post-build), `/retro` (post-ship)
- **Fits into:** Phase 1-3 of the canonical 12-day cycle in `workflows/new-ai-feature.md`

---

**Revised 17 SEP 2026.** Skill names carry the `rtp-` prefix and resolve to skills that ship. Removed the roster totals, which counted a library of 39 and drift silently; the steps name the skills they use instead. Headings are sentence case, emphasis is carried by the sentence rather than capitals, and em dashes are out of running prose. `rtp-failure-design` was replaced by `rtp-failure-modes`, which it merged into, and `red-team` by `rtp-stress-test`, since no skill by that name exists. The sequence and the reasoning are unchanged.
