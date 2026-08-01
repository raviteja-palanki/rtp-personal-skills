# AI PM Technical Interview — Grading Rubric

How to score an answer in the AI PM technical round. This governs every Grade and every Mock scoring step. The core is the **5 Laws**, scored against **two interviewer archetypes**, with a **weakest-link overall** and a set of **auto-fail mistakes**.

The interviewer's real question, under every technical question, is: **do you understand the systems you build on, or do you only use them?** Grade toward that.

---

## The 5 Laws (the scoring dimensions)

Each answer is read against five laws. Mark each ✓ (present and strong), ~ (partial), or ✗ (missing/wrong). These come from Aakash's mock demonstrations.

### Law 1 — Commit
Did the answer start with a direction, or fence-sit?
- ✓ Opens with the answer or a clear stance: "ML model, but let me explain." / "The answer is RAG here." A deliberate think-aloud counts IF it lands somewhere ("Let's reason through it — on one hand… so I'd land on X").
- ~ Eventually takes a position but buries it after throat-clearing.
- ✗ Never commits. Lists considerations and stops. Reads as not knowing. **A non-committal answer caps the overall at "Borderline" regardless of content** — indecision is itself the failing signal in this round.

### Law 2 — Depth (jargon used correctly)
Did the answer deploy correct technical vocabulary to make a real structural point?
- ✓ Precise terms doing real work: "churn is tabular, clean label," "faithfulness vs. retrieval quality," "the model emits a structured request, my code executes it." The jargon *earns* its place by explaining a mechanism.
- ~ Right terms but decorative — namedrops "XGBoost" or "RAG" without the reason it matters.
- ✗ Wrong or absent. **A technical error is not a ~; it's a ✗ AND it triggers the bluff auto-fail below.** Correct jargon that's misused is worse than plain language.

### Law 3 — Real-world experience
Did the answer show hands-on experience, or just recite?
- ✓ Shows it without a speech about it: "I'd put gradient boosted trees on it… the first question after I ship is why an account didn't get flagged." Operational phrasing ("I'd put," "the first thing I'd check," "what breaks first is…") signals someone who's done it.
- ~ Generic competence; correct but textbook, no fingerprints of having built anything.
- ✗ Pure definition, or claims experience without any concrete texture ("I've built lots of these" with no detail).

### Law 4 — Nuance
Did the answer layer the second consideration / the trade-off?
- ✓ Commits, then shows the other side: "trees predict, the LLM reads and writes — so the real system is hybrid." Names what the choice costs. Every AI answer is shades; the nuance is what moves B+ → A+.
- ~ Gestures at a trade-off but doesn't develop it.
- ✗ One-dimensional. Picks a side and never acknowledges the tension. Reads as junior.

### Law 5 — Succinct
Would this run under ~120 seconds? Was it tight?
- ✓ Makes the point and stops. Two crisp paragraphs, not five. Roughly under ~180 words spoken for a single answer.
- ~ A bit long; one section rambled but recovered.
- ✗ Word salad. Verbosity as a mask for uncertainty. **Over-length gets an automatic ~ minimum on Law 5** and a coaching note: "This runs past 2 minutes — trim to the strongest 60 seconds. If you truly need more, check in: 'does this make sense so far?'"

---

## The Two Archetypes (grade against the one in play)

The SAME answer scores differently depending on who's asking. Announce the archetype at the start of a mock, and grade to it. This is the most-missed subtlety in the round.

### The Engineer in the Room
Wants the **mechanism**. Every answer earns a follow-up one layer down. Rewards depth (Law 2) and penalizes staying at the product layer when a mechanism was asked.
- Up-weight: Law 2 (depth), Law 3 (real experience with mechanism).
- A product-only answer to "what happens under the hood" is a miss here, even if polished.
- Used by: Nvidia, OpenAI, Anthropic, DeepMind, Glean, retrieval/infra roles.

### The Product-Layer PM
Asks a mechanism question but **listens for what you do with it** — validation, failure handling, UX, metrics, cost. If the candidate dives into implementation detail instead, **mark them down** (this is Mistake 6, going too deep).
- Up-weight: Law 4 (nuance/trade-offs), the day-two playbook (evals, fallback, unit economics), Law 5 (succinct).
- Deriving mechanism nobody asked for is a real markdown, not bonus.
- Used by: Microsoft, Amazon, Meta, most applied-AI PM roles.

**Reading the archetype is a graded skill.** In a mock, occasionally give a mechanism question while playing Product-Layer, and mark down a candidate who over-derives. Coach: "Read your interviewer in the first two minutes — depth is only an asset when it's what's being asked for."

---

## Overall Score — Weakest Link, Not Average

The overall is **not** an average of the five laws. It's gated by the worst failure, because this round is about credibility and one crack sinks it.

Compute the overall verdict as one of three levels:

- **Pass (A-/A+):** All five laws ✓ or a single ~, no bluff, archetype matched. The candidate committed, showed correct depth, sounded like they'd built it, layered nuance, and stayed tight.
- **Borderline (B):** Content is right but one law is ✗ (usually no commit, no nuance, or too long), OR the answer was right but pitched at the wrong archetype. Fixable with coaching.
- **Not yet (C or below):** ANY of the auto-fails below fired, OR two-plus laws are ✗. A bluffed fact lands here regardless of how good the rest was — **a confident wrong statement in front of a real engineer is the one unrecoverable error.**

State the calculation: "Overall = gated by weakest link. Laws: Commit ✓, Depth ✗ (called MCP a platform you built), Experience ~, Nuance ✓, Succinct ✓ → **Not yet**, because the depth error is a bluff in front of an engineer."

---

## Auto-Fail Mistakes (the six that end loops)

If any of these fire, the overall is "Not yet" and you name the mistake explicitly. These come from real loop post-mortems.

### Mistake 1 — Bluffing a detail
A confident guess in a room that contains an actual engineer is the one thing they cannot hire. (A *wrong fact you correct in the next sentence* costs almost nothing — self-correction is a positive signal.) When the candidate hits the edge of what they know and guesses instead of naming the edge → auto-fail. **Detector:** any technical claim that's false and stated with confidence, no hedge. Coaching replacement: "I'd confirm with the team, but my instinct is X, and here's what I'd check."

### Mistake 2 — Calling a wrapper a platform
Describing a straightforward API integration as proprietary infrastructure. The fastest tell that someone stood *near* an AI project rather than shipped one. **Detector:** "we built our own [MCP server / model / platform]" where the real work was configuring an existing tool/API. Coaching: claim exactly what you did — "I configured and evaluated the connectors" is more credible than a false infra claim.

### Mistake 3 — Reporting input metrics as success
Sessions, prompts sent, queries served — none say whether the user got what they came for. **Detector:** the candidate names activity/volume metrics when asked how they'd know the feature works. Coaching: task resolution is the number that matters; input metrics go below the fold.

### Mistake 4 — The perfect record
"What would you do differently?" → "nothing." "Have you ever killed an AI feature?" → "no." In a field this experimental, a spotless record reads as a thin one. **Detector:** refusal to name a failure, a kill, or a lesson. Coaching: name a real one with the lesson; it signals you've actually shipped and learned.

### Mistake 5 — The deterministic PRD
A spec that assumes the output is always right — no fallback path, no graceful degradation, no design for the day the model is confidently wrong. **The single most common gap between a traditional PM and an AI PM.** **Detector:** a system/feature design with no answer to "what happens when the model is wrong?" Coaching: every AI PRD needs a fallback — abstain, cite, escalate, HITL.

### Mistake 6 — Going too deep
Deriving backpropagation when the interviewer wanted the product layer. **Detector:** mechanism depth that overshoots a Product-Layer archetype's question; ignoring the "what do you do with it" the interviewer was listening for. Coaching: read the archetype; depth is an asset only when it's what's asked for. (This is the mirror of the Engineer-in-the-Room under-depth miss.)

---

## The Positive Signals (what an A+ answer shows)

Reward these explicitly when present:
- **Pairs mechanism with trade-off.** Naming how something works is half; saying what it costs is the half that gets you hired.
- **Names the edge of knowledge.** "I don't know the exact metric — here's what I'd check" scores *higher* than a confident guess. Every time.
- **Refuses the over-answer trap.** Given a chance to reach for the most sophisticated answer (e.g., "does orchestration come into a single tool call?"), says "no, and here's when it would." Restraint is a senior signal.
- **Self-corrects fast.** A wrong fact fixed in the next sentence is a *plus*, not a minus — it shows they know the terrain well enough to catch themselves.
- **Grounds claims in real experience** with operational phrasing ("the first thing that breaks is…").

---

## Scoring Output Format (for Grade mode)

```markdown
## Grade: [question]

**Fact check:** [errors corrected, or "Clean — mechanism is right."]

**Archetype graded against:** [Engineer in the Room / Product-Layer PM] — [one line why]

| Law | Mark | Read |
|-----|------|------|
| 1 Commit | ✓/~/✗ | [quote their opener] |
| 2 Depth | ✓/~/✗ | [was the jargon correct AND load-bearing?] |
| 3 Experience | ✓/~/✗ | [showed vs. told] |
| 4 Nuance | ✓/~/✗ | [second consideration / trade-off present?] |
| 5 Succinct | ✓/~/✗ | [~word count / under 120s?] |

**Auto-fails triggered:** [none / Mistake N: what happened]

**Overall: [Pass / Borderline / Not yet]** — gated by [weakest link]. [one sentence]

**Highest-leverage fix:** [the single change before a real loop]

### A+ rewrite
[under ~150 words, 5 Laws hit, real experience or bracketed placeholder]
```

## Scoring Output Format (for end-of-Mock summary)

```markdown
## Session Score

Questions: [n] · Archetype: [X]

**Per-law trend across the session:**
- Commit: [strong / inconsistent / weak] — [evidence]
- Depth: [...]
- Experience: [...]
- Nuance: [...]
- Succinct: [...]

**Auto-fails this session:** [list, or none]

**Overall: [Pass / Borderline / Not yet for a real [company] loop]**

**Your one fix:** [the single highest-leverage thing, quoting their words]

**Weakest answer, rewritten:** [full A+ rewrite of the worst one]

**What to do next:** [study §X of concepts / drill Topic Y / build Z / run another mock]
```
