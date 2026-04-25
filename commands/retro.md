---
name: retro
description: Post-ship retrospective for AI features. Reads original AI-PRD, compares to shipped state via ai-product-metrics, runs stress-test retrospectively (assumptions held / failed), extracts feedback-flywheel updates. Outputs a structured retro doc with assumption audit, lessons learned, eval-pipeline updates, next-iteration backlog. Triggers on "retro," "post-mortem," "what did we learn from [feature]."
version: 1.0.0
author: RTP (Ravi Teja Palanki)
chains:
  - ai-product-metrics
  - stress-test
  - feedback-flywheel
---

# /retro
**Post-ship retrospective for AI features. The learning loop most teams skip.**

> "If the retro ends with 'we shipped it,' that's a status update, not a retro. The retro ends with 'here's what changes the next bet.'" — RTP

---

## WHEN THIS RUNS

Trigger phrases: "retro," "post-mortem," "what did we learn from [feature]," "post-ship review."

Cadence:
- **T+30:** First retro for any AI feature launch. Even if data is thin, the assumption audit is valuable.
- **T+90:** Second retro for L4+ features. By then, real usage patterns and edge cases have surfaced.
- **Triggered:** Any time a kill-switch is pulled, regardless of timeline.

Do NOT use this for:
- Sprint retros (use `pm-execution:retro` — different scope, different cadence)
- Pre-launch debriefs (no shipped state to measure)
- Strategy reviews (use `/strategy-review`)

---

## INPUT

The user invokes this with the feature name. If empty, ask:

1. "Which AI feature are we retrospecting?"
2. "When did it ship and is there an original AI-PRD I can read?"
3. "Are post-launch metrics available, or are we working from recollection?"

If the original AI-PRD is missing, note this as a process gap and continue with recollection. The retro is still valuable, but the assumption audit will be weaker.

---

## STEP 1 — READ THE ORIGINAL AI-PRD

The retro starts where the PRD ended. Read:

- **Problem statement and JTBD** — has it changed?
- **Autonomy level** — did we hold the level or drift?
- **Dual success metrics** — what targets were set?
- **Acceptance criteria** — what was the eval bar?
- **Cost ceiling** — what was the projected unit economic?
- **Failure modes** — what did we predict could go wrong?
- **Improvement flywheel** — what did we plan to learn from?

If the PRD doesn't exist, the retro becomes a recollection exercise. Note this gap explicitly. Future PRDs need to exist for retros to compound.

---

## STEP 2 — AI-PRODUCT-METRICS COMPARISON

**Skill: `ai-product-metrics`**

Compare predicted to actual across both metric types. AI features need both because shipping a model that hits accuracy targets but kills user adoption is a different failure than shipping a model that users love but burns cash.

### User outcome metrics

| Metric | Predicted | Actual | Delta | Verdict |
|---|---|---|---|---|
| Task completion rate | [%] | [%] | [+/-] | Hit / Miss / Too early |
| Time-to-value | [s/min] | [s/min] | [+/-] | Hit / Miss / Too early |
| Adoption rate (trial → use) | [%] | [%] | [+/-] | Hit / Miss / Too early |
| User satisfaction (CSAT or proxy) | [score] | [score] | [+/-] | Hit / Miss / Too early |

### AI-specific metrics

| Metric | Predicted | Actual | Delta | Verdict |
|---|---|---|---|---|
| Accuracy (overall) | [%] | [%] | [+/-] | Hit / Miss |
| Accuracy by class | [%] | [%] | [+/-] | Hit / Miss |
| Hallucination rate | [%] | [%] | [+/-] | Hit / Miss |
| False positive / negative | [%] | [%] | [+/-] | Hit / Miss |
| Latency P95 | [ms] | [ms] | [+/-] | Hit / Miss |
| Confidence calibration | [%] | [%] | [+/-] | Hit / Miss |
| Cost per call | [$] | [$] | [+/-] | Hit / Miss |
| Daily cost (avg) | [$] | [$] | [+/-] | Hit / Miss |

**Key question:** Did we solve the user problem, OR did we hit AI metrics without moving user outcomes? The honest answer determines the next bet.

---

## STEP 3 — STRESS-TEST (Retrospective)

**Skill: `stress-test`**

Run stress-test in reverse. The PRD made assumptions. Which held? Which failed? Which were never tested?

| Assumption | What we believed | What actually happened | Verdict |
|---|---|---|---|
| Users will tolerate X% accuracy | [%] | [observed tolerance] | Held / Failed / Untested |
| Volume will be ~N calls/day | [N] | [actual] | Held / Failed / Untested |
| Cost will be ~$X/call at GA | [$] | [actual] | Held / Failed / Untested |
| Failure mode A is the dominant risk | [A] | [actual dominant failure] | Held / Failed / Untested |
| User correction rate will be <Y% | [%] | [actual] | Held / Failed / Untested |
| Confidence threshold of Z gates the right cases | [Z] | [actual right setting] | Held / Failed / Untested |

For each:

- **Held assumptions** — strengthen conviction. These are the patterns to apply to the next bet.
- **Failed assumptions** — gold. These prevent repeating mistakes. Capture in `5_Knowledge/rules.md` or `5_Knowledge/hypotheses.md` depending on confirmation count.
- **Untested assumptions** — the riskiest. They didn't fail; they were never put under load. Decide whether to test now or accept the risk.

---

## STEP 4 — FAILURE MODE AUDIT

What failure modes actually happened? Compare the PRD's predicted failure modes to what production showed:

| Predicted | Showed up in production? | Severity | Recovery worked? |
|---|---|---|---|
| Hallucination | Yes/No | H/M/L | Yes/No/Partial |
| Refusal regression | Yes/No | H/M/L | Yes/No/Partial |
| Latency spike | Yes/No | H/M/L | Yes/No/Partial |
| Cost spike | Yes/No | H/M/L | Yes/No/Partial |
| Prompt injection | Yes/No | H/M/L | Yes/No/Partial |
| Bias / unfairness | Yes/No | H/M/L | Yes/No/Partial |

**The unpredicted failure modes are the most valuable.** What broke that nobody anticipated? Add it to the failure-mode catalog for next time.

If a kill-switch was pulled: dedicated section. What was the trip-wire signal? How long from signal to disabled? Did the kill-switch design hold up, or did the team improvise?

---

## STEP 5 — FEEDBACK-FLYWHEEL EXTRACTION

**Skill: `feedback-flywheel`**

The improvement loop. What did production teach us that the eval set didn't catch?

### Eval pipeline updates

For each failure case observed in production that the eval set missed:

- Add the case to the golden set or edge case set
- Update the LLM-as-judge prompt if it failed to detect the issue
- Document the regression detection gap

### Prompt updates

- What prompt versions were rolled out post-launch? Why?
- Which versions improved vs. regressed which metrics?
- Is the prompt versioning discipline holding (every change logged with rationale)?

### Model decisions

- Did we change models? Why?
- Did we add a routing layer (cheap model for simple, expensive for complex)?
- What's the current model + version + system prompt fingerprint?

### Data flywheel

- What user feedback signal is feeding back into the eval set or training data?
- Is the loop running, or stalled? If stalled, what's blocking it?

---

## STEP 6 — LESSONS & DECISION

Distill the retro into three categories.

### What worked (specifics, not generics)

- The PRD gate that caught X early
- The cohort rollout that surfaced Y before GA
- The kill-switch design that disabled cleanly when Z happened
- The eval set composition that matched production patterns

### What didn't work (specifics, not generics)

- The assumption that broke and cost N days
- The metric we tracked that didn't correlate with user outcome
- The failure mode we under-weighted
- The cost surprise we didn't model

### What surprised us (the most valuable category)

- Users using the feature in a way we didn't design for
- A failure mode we didn't predict
- An accuracy class that mattered more / less than expected
- A capability shift in the model that changed the calculation

---

## STEP 7 — DECISION & NEXT-ITERATION BACKLOG

For each open issue, one of four decisions:

- **Double down** — the bet is working; expand it
- **Iterate** — the bet is right but needs refinement; specific changes scoped
- **Maintain** — feature is fine; no further investment needed this cycle
- **Deprecate** — the bet didn't work; sunset with comms plan

Then produce the next-iteration backlog:

| Item | Source | Priority | Owner |
|---|---|---|---|
| [Eval pipeline gap] | Step 5 | H/M/L | [Name] |
| [Prompt update needed] | Step 5 | H/M/L | [Name] |
| [Failure mode to add to catalog] | Step 4 | H/M/L | [Name] |
| [Assumption to retest] | Step 3 | H/M/L | [Name] |
| [Cost optimization to scope] | Step 2 | H/M/L | [Name] |

---

## OUTPUT FORMAT

```
Retro: [Feature Name]
Shipped: [DDMMMYYYY]
Retro date: [DDMMMYYYY]
Retro window: T+30 / T+90 / Triggered

ONE-PARAGRAPH SUMMARY
[What shipped, what happened, what we learned]

OUTCOME VS. PREDICTION
[Tables from Step 2 — both user outcome and AI-specific]

ASSUMPTION AUDIT
[Table from Step 3]

FAILURE MODE AUDIT
[Table from Step 4 + any unpredicted modes]

FEEDBACK FLYWHEEL UPDATES
[Eval pipeline, prompt, model, data updates from Step 5]

WHAT WORKED / WHAT DIDN'T / WHAT SURPRISED US
[Specifics from Step 6]

DECISION: [Double down / Iterate / Maintain / Deprecate]
RATIONALE: [2-3 sentences]

NEXT-ITERATION BACKLOG
[Table from Step 7]

LESSONS FOR THE PM SYSTEM
[3-5 specific lessons that update rules.md, hypotheses.md, or skill learning logs]
```

---

## QUALITY BAR

A real `/retro`:

- Compares predicted to actual with both user outcome AND AI-specific metrics
- Has an assumption audit that distinguishes Held / Failed / Untested
- Captures unpredicted failure modes (the most valuable learning)
- Updates the eval pipeline based on production gaps
- Ends with a clear decision (Double down / Iterate / Maintain / Deprecate), not "we'll see"
- Feeds back into `5_Knowledge/rules.md`, `hypotheses.md`, or skill learning logs
- For kill-switch events: includes a dedicated section on the trip-wire performance

**The test:** Three months later, when the team is starting a similar AI feature, can they pull this retro and learn something specific that changes how they scope, design, or launch? If the retro is generic, it didn't compound.

---

## CROSS-REFERENCES

- **Run after:** any AI feature ships, any kill-switch pulls, T+30 and T+90 milestones
- **Feeds into:** `5_Knowledge/rules.md` (confirmed patterns), `hypotheses.md` (1-2x observations), skill learning logs
- **Related workflows:** `/design-ai-feature` (the next bet learns from this retro), `/strategy-review` (quarterly aggregation of retros)
- **Skill files used:** `ai-product-metrics`, `stress-test`, `feedback-flywheel`
