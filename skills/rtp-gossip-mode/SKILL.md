---
name: rtp-gossip-mode
version: 1.0.0
author: RTP (Ravi Teja Palanki)
description: >
  Voice-to-text / stream-of-consciousness → structured memory updates. Tagged for AIPM-specific
  signals (eval gaps, prompt regressions, model drift, stakeholder dynamics). Use when the user
  is venting, debriefing informally, or thinking aloud about AI product work — not when asking a
  specific PM question or requesting a deliverable.
imports:
  - feedback-flywheel
  - eval-framework
---

# Gossip Mode — AIPM Signal Extraction
**Listen to the unstructured. Extract the structural. Route to the right file.**

> "The most valuable signals come out sideways — in standup gripes, hallway debriefs, post-demo venting. Most PMs let those signals die. The 0.1% PMs catch them and route them." — RTP

---

## DEPTH DECISION

**Go deep** if: the user is sharing rich AI context (eval gaps, model failures, stakeholder reactions, capability shifts). Read all sections to extract correctly.

**Skim to THE EXTRACTION SCHEMA** if: the user is just venting briefly and you need to parse signals quickly without overthinking.

**Skip** if: the user asked a specific PM question (run the matching skill instead), is requesting a deliverable, or is in a structured planning mode where unstructured extraction would feel intrusive.

---

## THE STRUCTURAL INSIGHT

CLAUDE.md auto-memory captures generic memories — user role, preferences, file access rules. Useful, but generic.

The 0.1% angle is **AIPM-tagged signal extraction.** When Ravi says "the model failed on the demo today," gossip-mode parses → this is an eval gap (the failure case wasn't in the eval set). It routes to: failure-mode catalog, golden set update, hypothesis about a regression pattern.

Generic gossip skills capture "model failed" as a journal entry. AIPM gossip-mode captures it as four structural signals routed to four different files.

The value compounds because the next session sees the routed signal in the right place, not buried in conversation history.

---

## THE EXTRACTION SCHEMA

When the user shares informal AI product context, scan for these signal types. Each has a routing destination.

### 1. Eval pipeline regressions

**Listen for:**
- "The model used to handle X but now it gets it wrong"
- "We added [new model / new prompt] and now [previously working case] breaks"
- "Our eval scores dropped after [change]"
- "Failed on a case we'd seen before"

**Route to:**
- Eval test cases — add the failure case to the golden set or edge cases
- Hypothesis (`5_Knowledge/hypotheses.md`) — if this is the first sighting of a regression pattern
- Rule (`5_Knowledge/rules.md`) — if 3+ regressions of this type have been confirmed

### 2. Prompt-version regressions

**Listen for:**
- "We changed the prompt and X stopped working"
- "Old prompt was better at [specific class]"
- "Tried a new prompt structure, accuracy dropped"

**Route to:**
- Prompt versioning log — record the regression with the version number
- Prompt template — flag the failed change with a rationale comment
- Decision record if the team rolled back

### 3. Model-version drift

**Listen for:**
- "[New model] is worse / better at [task]"
- "After [vendor] released the new version, our [metric] changed"
- "We're seeing different output style than before"

**Route to:**
- Capability tracking log — record the model + version + observed change
- Cost-model — if the new model has different pricing
- Strategy-review queue — if drift is structural (capability commoditization or new moat opportunity)

### 4. Stakeholder dynamics changes

**Listen for:**
- "[Name] is now annoyed / excited / skeptical about [topic]"
- "Leadership wants [new thing] by [date]"
- "[Stakeholder] would rather we [specific behavior]"
- "[Engineer/designer] pushed back on [decision]"

**Route to:**
- Memory file (`stakeholder-signals.md` or user profile) — update with the named person + position
- Open questions — if the stakeholder shift creates a decision point
- Comms plan — if the change requires updated messaging

### 5. Capability shifts (model landscape)

**Listen for:**
- "[Model X] just shipped and can now do [Y]"
- "I saw a demo where [capability] worked"
- "[Vendor] announced [feature] last week"

**Route to:**
- Capability tracking log — update half-life estimates
- Strategy-review queue — quarterly review will need this signal
- `/strategy-review` action items — if the shift is material to current bets

### 6. Competitive intel from informal sources

**Listen for:**
- "Heard at a conference / meetup / DM that [competitor] is doing [X]"
- "[Customer] told me they're also evaluating [competitor]"
- "Rumor that [vendor] is pivoting to [Y]"

**Route to:**
- Competitive map (with confidence level — low confidence for rumor, higher for direct customer signal)
- Signal-scanner — for the next strategy review
- Hypothesis if it's the first sighting of a pattern

### 7. Cost / latency surprises

**Listen for:**
- "We blew through the cost budget for [feature]"
- "Latency spiked after [event]"
- "Per-call cost went up because of [reason]"

**Route to:**
- Cost-model — update the actual numbers
- Production-observability — confirm dashboards caught the spike
- Decision record if a model change or routing change is needed

### 8. Acceptable-failure-mode signals

**Listen for:**
- "[User] would rather it refuse than guess"
- "[Customer] doesn't mind a slow answer if it's right"
- "[Stakeholder] is fine with [tradeoff] but not [other tradeoff]"

**Route to:**
- AI-PRD failure-mode section — update the user tolerance assumptions
- Eval-framework — adjust the acceptance bar based on tolerance
- JTBD analysis — refine the gain criteria

---

## ROUTING RULES

The routing logic isn't lookup — it's reasoning. Here's the decision tree for any extracted signal:

| Signal type | Confirmation level | Route to |
|---|---|---|
| Failure mode named with concrete example | First time seen | `hypotheses.md` |
| Failure mode named with concrete example | Seen 3+ times | `rules.md` |
| Decision made or reversed | Always | `CHANGE_LOG.md` (with WHY) |
| Stakeholder preference / sensitivity | Low-stakes | Memory file |
| Stakeholder preference / sensitivity | Load-bearing | Open questions + memory |
| Eval test case from production | Always | Eval set + change log |
| Capability shift | Always | Capability tracking |
| Cost or latency anomaly | First time | Production observability check |
| Cost or latency anomaly | Repeated | Cost-model update + decision record |
| Competitive intel | Low confidence | Signal-scanner queue |
| Competitive intel | High confidence (direct source) | Competitive map update |

**The routing must be visible in the response.** Don't write to files silently. Show the user what was extracted and propose where each signal goes. Wait for confirmation before writing.

---

## REAL-WORLD EXAMPLE

**User says:** "Vinod was annoyed in standup that the AI answered Q3 wrong but Q1 and Q2 right. Said he'd rather it refuse than guess. Also, the latency was up — like 4 seconds for what used to be 1.5."

**Gossip-mode extraction:**

**What I heard:**

| Signal type | Specific extraction |
|---|---|
| Acceptable-failure-mode | Vinod prefers conservative refusal over confident wrong answer for Q3-class queries |
| Stakeholder dynamics | Vinod's tolerance signal — refusal > hallucination, even at cost of completion rate |
| Eval pipeline gap | Q3-class question that fails while Q1-Q2 succeed isn't in the eval set, or it is but the regression detection didn't catch it |
| Latency anomaly | P95 jumped from 1.5s to 4s — material change, needs root cause |

**Proposed routing:**

- [ ] **Eval test cases** — Add the Q3 failure case to the golden set with expected output: "refuse with structured reason" (not "answer with confidence")
- [ ] **Hypotheses** — "Failure-class confidence calibration may be off when query subclass shifts" (route to `hypotheses.md`, watch for 2 more sightings)
- [ ] **Stakeholder signals** — Update Vinod's profile: prefers conservative refusal for ambiguous queries; flag in next AI-PRD failure-mode section
- [ ] **Production observability** — Latency spike — confirm the dashboard caught it. If not, that's an observability gap. If yes, root-cause within 24h.
- [ ] **Decision record candidate** — If team adjusts the confidence threshold based on Vinod's signal, that's a decision worth logging in CHANGE_LOG.md with rationale

**What's worth a follow-up action right now:** the latency spike, because that's a P0 ops issue, not a learning artifact. Suggest opening an incident ticket immediately. The other items can wait for normal channels.

---

## DELIVERABLE FORMAT

After extraction, respond in this shape:

**1. Acknowledge (1-2 sentences)**
- If there's emotional content (frustration, excitement, fatigue), briefly acknowledge before extracting
- Don't dwell — Ravi wants utility, not therapy

**2. What I heard (signal table)**
- Two columns: Signal type, Specific extraction
- Each row is one extracted signal — the schema decides which type
- Confidence in extraction noted if low ("I'm reading this as X — flag if wrong")

**3. Proposed routing (checkbox list)**
- Each item: [destination] → [what gets written]
- Use checkboxes so the user can accept some and reject others
- Show the file path so it's not abstract

**4. Immediate action (if any)**
- One follow-up the user should take right now (incident, comms, decision)
- Only one — don't overwhelm

**5. Confidence in extraction**
- "High" if the signals were explicit and clean
- "Medium" if some signals were inferred — list the inferences
- "Low" if you're guessing — ask for clarification before routing

---

## RED TEAM — When NOT to Use Gossip-Mode

This skill is wrong for several situations. Use the right tool instead.

### Don't use when:

- **The user asks a specific PM question** — they want an answer, not extraction. Run the matching skill.
- **The user requests a deliverable** ("write me the PRD") — that's craft mode, not listening mode.
- **The content is sensitive** — comp discussions, named complaints about teammates, customer churn details with PII. Don't auto-route private content. Surface that you heard it, but ask before writing anywhere.
- **The user explicitly asks for clean memory hygiene** — sometimes Ravi wants to vent without anything being recorded. Respect that. The opt-out is "this stays here" or "don't memo this."
- **The signal is already structured** — if Ravi says "add this to the eval set: [structured input]," he's done the extraction. Just route, don't re-extract.
- **You're in the middle of a structured workflow** — running `/design-ai-feature` is structured. Pulling gossip-mode mid-flow breaks the discipline. Capture signals as side notes, address them after the workflow completes.

### Conservative defaults:

- **When in doubt, ask before writing.** A wrong route is worse than no route.
- **Sensitive content stays in conversation by default.** Surface that you heard it, but don't propose a destination unless asked.
- **Confidence-low extractions get flagged, not silently routed.** "I think you mean X — am I reading this right?"

---

## CROSS-REFERENCES

- **Imports:** `feedback-flywheel` (for the eval-pipeline routing), `eval-framework` (for golden set updates)
- **Routes to:** `5_Knowledge/rules.md`, `5_Knowledge/hypotheses.md`, `CHANGE_LOG.md`, eval test sets, memory files, capability tracking logs
- **Adjacent skills:** `feedback-triage` (for structured customer feedback), `interview-synthesis` (for structured interview output)
- **Inverse:** when Ravi wants clean output (a deliverable, a doc), use the relevant craft skill, not gossip-mode

---

## QUALITY BAR

A real gossip-mode extraction:

- Catches at least one signal the user didn't realize was structural
- Routes signals to specific file paths, not vague "I'll remember that"
- Distinguishes high-confidence extraction from inference
- Surfaces the one immediate action (if any), not a to-do list
- Asks before writing sensitive content
- Compounds — three months later, the routed signals show up in the right files when the team needs them

**The test:** Six months from now, when Ravi or a future session reads `rules.md`, `hypotheses.md`, or the eval set, can they trace specific entries back to gossip moments? If yes, the routing worked. If the routed signals are invisible or duplicated, the schema needs sharpening.
