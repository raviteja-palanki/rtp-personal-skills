---
name: gossip-mode
version: v1.1_latest
description: 'Turns venting into memory. When you think aloud (a standup gripe, a post-demo debrief, a hallway observation), this catches the structural signal hiding in the informal stream. That might be an eval gap, a prompt regression, a model drifting, a stakeholder''s shifting stance, or a cost spike. Each one gets routed to the exact file a future session will need. One gripe usually holds several routable facts; most PMs hear a vibe and let it die. Always proposes routing and waits for confirmation; never writes sensitive content without asking. Use when the user is venting, debriefing informally, or thinking aloud about AI product work, not when they ask a specific PM question or want a deliverable. Pairs with: feedback-triage (structured customer feedback, the formal sibling), interview-synthesis (structured transcripts), production-observability (when the vented signal is an ops incident), signal-scanner (when it''s competitive intel). Triggers: user venting, debriefing, or thinking aloud about AI product work.'
imports:
  - feedback-flywheel
  - eval-framework
---

# Gossip Mode — AIPM Signal Extraction
**Listen to the unstructured. Extract the structural. Route to the right file.**

**The objective:** stop valuable signals from dying in conversation — for the PM whose most important product intelligence arrives sideways and evaporates. It catches the informal remark, names the kind of signal buried in it, and files it where the next decision will find it.

## The one idea

Someone says, in standup: *"Vinod was annoyed the AI got Q3 wrong but Q1 and Q2 right — said he'd rather it refuse than guess. Also latency was up, like 4 seconds for what used to be 1.5."*

Most PMs hear a vibe: *Vinod's grumpy today.* Then the moment passes and everything in it is gone.

Listen structurally and that one gripe is not a vibe — it is **four routable facts:** an eval gap (a Q3-class failure that isn't in the test set), a stakeholder tolerance (refuse > guess, for this user), a latency incident (P95 jumped 1.5s → 4s, possibly a P0), and a candidate decision (if you adjust the confidence threshold, that's worth logging). Four signals, four different files.

That's the one idea: **the most valuable product intelligence arrives sideways, and it dies unless something catches it.** The 0.1% PM doesn't have a better memory — they have a *routing habit*: pull the durable structural fact out of the informal remark, and write it to the exact place a future session will look. Generic auto-memory captures "model failed" as a journal line. This captures it as an eval-set update, a hypothesis, and a stakeholder note — three files, not one buried sentence.

The whole test is **traceability:** six months from now, can specific entries in the rules, the hypotheses, and the eval set be traced back to the gossip moment that created them? If yes, the routing worked.

Two disciplines make it safe, and they never bend: **propose the routing and wait — never write silently**, and **never route sensitive content without asking** (comp, named complaints, PII stay in the conversation by default).

## How to use this skill

1. **Scan the informal stream for two families of signal** — *the AI system changed* (eval/prompt regressions, model drift, cost/latency spikes) or *the people and market changed* (stakeholder stance, capability shifts, competitive intel, failure-tolerance). THE EXTRACTION SCHEMA below has the eight types.
2. **Extract the structural fact**, not the emotion — one gripe usually holds several.
3. **Propose the routing** as a checklist with real file paths, flag low-confidence reads, surface the one immediate action — then **wait for confirmation** before writing anything.

## KEY TERMS (plain language)

- **Signal extraction** — pulling the durable structural fact out of an informal remark ("Vinod was annoyed" contains an eval gap, a latency incident, and a tolerance preference).
- **Routing** — writing each extracted signal to the specific file a future session will read: eval sets, hypotheses, rules, stakeholder memory, cost logs.
- **Golden set** — the fixed collection of test cases the AI must keep passing; production failures get added so they can never silently return.
- **Regression** — something that used to work and now doesn't, usually after a prompt or model change.
- **Model drift** — a model's behavior changing over time or across versions, without you changing your product.
- **Hypothesis → rule promotion** — a pattern seen once or twice is a hypothesis; confirmed three times, it becomes a rule applied by default.

## WHEN TO RUN THIS

**Run it** when the user is venting, debriefing informally, or thinking aloud about AI product work — the mode where signals leak out uncatalogued. **Skim to the schema** if they're venting briefly and you just need to parse fast. **Skip it** when they ask a specific PM question (run the matching skill), request a deliverable (that's craft mode), or are mid-structured-workflow (capture as side notes, route after). See RED TEAM below for the full when-not list.

## THE EXTRACTION SCHEMA

Scan for these eight signal types across two families. Each has a routing destination.

### Family A — the AI system changed

**1. Eval-pipeline regression.** *Listen for:* "used to handle X, now gets it wrong"; "added a new model/prompt and a working case broke"; "eval scores dropped after [change]." *Route to:* eval golden set (add the failure case) · `hypotheses.md` (first sighting of a regression pattern) · `rules.md` (if 3+ confirmed).

**2. Prompt-version regression.** *Listen for:* "changed the prompt and X stopped working"; "old prompt was better at [class]." *Route to:* prompt-versioning log (with the version number) · prompt template (flag the change) · decision record if rolled back.

**3. Model-version drift.** *Listen for:* "[new model] is worse/better at [task]"; "output style changed after the vendor's update." *Route to:* capability-tracking log (model + version + change) · cost-model (if pricing shifts) · strategy-review queue (if the drift is structural).

**4. Cost / latency surprise.** *Listen for:* "blew the cost budget"; "latency spiked after [event]"; "per-call cost went up." *Route to:* cost-model (update the real numbers) · production-observability (did the dashboard catch it?) · decision record if a model/routing change is needed.

### Family B — the people and market changed

**5. Stakeholder dynamics.** *Listen for:* "[name] is now annoyed/excited/skeptical about [topic]"; "leadership wants [thing] by [date]"; "[engineer] pushed back on [decision]." *Route to:* stakeholder memory (named person + position) · open questions (if it creates a decision point) · comms plan (if messaging must change).

**6. Capability shift (model landscape).** *Listen for:* "[model] just shipped and can now do [Y]"; "saw a demo where [capability] worked." *Route to:* capability-tracking log (update half-life estimates) · strategy-review queue · `/strategy-review` action items if material to current bets.

**7. Competitive intel (informal source).** *Listen for:* "heard at a meetup that [competitor] is doing X"; "a customer said they're also evaluating [competitor]." *Route to:* competitive map (with a confidence level — low for rumor, higher for a direct customer signal) · signal-scanner · `hypotheses.md` if first sighting.

**8. Acceptable-failure-mode signal.** *Listen for:* "[user] would rather it refuse than guess"; "doesn't mind slow if it's right"; "fine with [tradeoff] but not [other]." *Route to:* AI-PRD failure-mode section (update tolerance assumptions) · eval-framework (adjust the acceptance bar) · JTBD analysis (refine the gain criteria).

## WHY THE ROOM STAYS QUIET WHEN EVERYONE TRUSTS EACH OTHER

This skill exists because things get said outside the room that never get said inside it. Here is the mechanism, and it corrects an assumption most teams hold.

**Trust and psychological safety are different objects, and only one of them predicts group voice.**

- **Trust** is "the willingness to place yourself at risk based on another person's actions," and it **develops one relationship at a time**. It splits two ways: **relational trust** (confidence that others care about and respect you) and **transactional trust** (confidence that others are capable, reliable and aligned in intent).
- **Psychological safety** is a property of the **group**: a shared belief that people can speak candidly without fear of embarrassment, dismissal or retaliation.

**The finding that matters here, stated flatly by the researchers:** *"Strong one-on-one relationships do not automatically create a psychologically safe team."* Teams whose members trusted one another individually still hesitated to speak candidly in group settings.

**So high-trust teams produce more gossip, not less.** If everyone trusts everyone one-to-one and the group is not safe, the honest content has exactly one available channel, and it is the corridor. That is not a culture failure to be scolded; it is the predictable routing of information that has nowhere else to go. **Read a rich gossip stream from a high-trust team as a group-safety signal rather than a loyalty problem.**

**Two consequences for how you use this skill:**

1. **Do not diagnose the trust level from the gossip.** The gossip tells you the group channel is closed. It tells you nothing about whether people respect each other, and they usually do.
2. **When you phrase a trust question in a survey, phrase it group-referenced.** A trust item asked about colleagues measures the one-relationship-at-a-time property and will return high trust for a team that cannot speak, which is the exact false negative you are trying to avoid.

*(Source: HBR, "How the Best Leaders Shape Conversations," Aug 2026 — ◆ the authors' own dataset across more than a hundred teams; the relational and transactional definitions are verbatim, and the psychological-safety definition is theirs citing Edmondson. The reading that high individual trust plus low group safety routes content into the corridor is this corpus's inference, not their finding.)*

## ROUTING RULES

The logic is reasoning, not lookup — but this is the default decision tree. **The routing must be visible in the response: propose where each signal goes and wait for confirmation. Never write to files silently.**

| Signal | Confirmation level | Route to |
|---|---|---|
| Failure mode named with a concrete example | First time seen | `hypotheses.md` |
| Failure mode named with a concrete example | Seen 3+ times | `rules.md` |
| Decision made or reversed | Always | `CHANGE_LOG.md` (with WHY) |
| Stakeholder preference / sensitivity | Low-stakes | Memory file |
| Stakeholder preference / sensitivity | Load-bearing | Open questions + memory |
| Eval test case from production | Always | Eval set + change log |
| Capability shift | Always | Capability tracking |
| Cost / latency anomaly | First time | Production-observability check |
| Cost / latency anomaly | Repeated | Cost-model update + decision record |
| Competitive intel | Low confidence | Signal-scanner queue |
| Competitive intel | High confidence (direct source) | Competitive map update |

## WORKED EXAMPLE — the Vinod standup gripe

**User says:** "Vinod was annoyed in standup that the AI answered Q3 wrong but Q1 and Q2 right. Said he'd rather it refuse than guess. Also the latency was up — like 4 seconds for what used to be 1.5."

**What I heard:**

| Signal type | Specific extraction |
|---|---|
| Acceptable-failure-mode | Vinod prefers a conservative refusal over a confident wrong answer for Q3-class queries |
| Stakeholder dynamics | Vinod's tolerance: refusal > hallucination, even at the cost of completion rate |
| Eval-pipeline gap | The Q3-class failure (while Q1–Q2 pass) isn't in the eval set — or is, and regression detection missed it |
| Latency anomaly | P95 jumped 1.5s → 4s — material, needs root cause |

**Proposed routing (confirm before I write):**
- [ ] **Eval golden set** — add the Q3 failure with expected output "refuse with structured reason," not "answer confidently"
- [ ] **`hypotheses.md`** — "confidence calibration may be off when the query subclass shifts" (watch for two more sightings)
- [ ] **Stakeholder memory** — Vinod: prefers conservative refusal for ambiguous queries; flag in the next AI-PRD failure-mode section
- [ ] **Production-observability** — did the dashboard catch the latency spike? If not, that's an observability gap; if yes, root-cause within 24h

**Immediate action:** the latency spike — it's a P0 ops issue, not a learning artifact. Open an incident ticket now. Everything else can wait for normal channels.

## DELIVERABLE FORMAT

1. **Acknowledge (1–2 sentences).** If there's frustration or excitement, name it briefly, then extract — utility, not therapy.
2. **What I heard** — a two-column table (signal type · specific extraction); note low-confidence reads ("I'm reading this as X — flag if wrong").
3. **Proposed routing** — a checkbox list, each item `[destination] → [what gets written]`, with the real file path. Checkboxes so the user can accept some and reject others.
4. **Immediate action (if any)** — one, not a to-do list.
5. **Confidence** — High (explicit/clean), Medium (some inference — list it), or Low (guessing — ask before routing).

## RED TEAM — when NOT to use gossip-mode

- **A specific PM question** — they want an answer, not extraction. Run the matching skill.
- **A deliverable request** ("write me the PRD") — that's craft mode, not listening mode.
- **Sensitive content** — comp, named complaints about teammates, churn details with PII. Surface that you heard it, but don't propose a destination unless asked.
- **An explicit "this stays here" / "don't memo this"** — respect clean-memory hygiene.
- **Already-structured input** ("add this to the eval set: [X]") — the user did the extraction; just route, don't re-extract.
- **Mid-structured-workflow** (e.g. `/design-ai-feature`) — pulling gossip-mode mid-flow breaks the discipline; capture as side notes and address after.

**Conservative defaults:** when in doubt, ask before writing (a wrong route is worse than no route); sensitive content stays in the conversation unless asked otherwise; low-confidence reads get flagged, not silently routed.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Gossip-mode is a router by design — the extraction schema names eight destinations, so this section is necessarily wider than most skills' (a router-shaped skill earns a wider stack section; don't read the count as padding).

**Imports:**
- **`rtp-feedback-flywheel`** — the eval-pipeline routing machinery a caught regression feeds into.
- **`rtp-eval-framework`** — where a production failure case becomes a golden-set entry.

**Formal siblings — same intake, structured input instead of a hallway remark:**
- **`rtp-feedback-triage`** — structured customer feedback at volume, scored and ranked. Gossip-mode catches the sideways single signal; feedback-triage processes the batch.
- **`rtp-interview-synthesis`** — for structured transcripts.

**Receives a routed signal, named in the schema but missing from this list until now:**
- **`rtp-production-observability`** — signal 4: the vented signal is actually an ops incident (the latency spike); route it as a real alert, not a note.
- **`rtp-signal-scanner`** — signal 7: competitive intel headed for the next strategy review.
- **`rtp-competitive-map`** — signal 7, when the rumor is credible enough to update the actual landscape, not just queue it.
- **`rtp-capability-tracking`** — signals 3 and 6: a model-version drift or a capability shift updates the half-life log this skill owns, not just a mental note.
- **`rtp-cost-model`** — signals 3 and 4: when "the numbers moved" turns out to mean unit economics broke, not just one input ticking up.
- **`rtp-prompt-as-product`** — signal 2: a prompt-version regression is exactly the version/regression-test/rollback discipline that skill owns.
- **`rtp-stakeholder-communications`** — signal 5: when a stakeholder-dynamics read changes what a room needs to hear next, this is where that gets drafted.
- **`rtp-jtbd-analysis`** and **`rtp-ai-prd`** — signal 8: an acceptable-failure-mode preference (refuse > guess) refines JTBD's gain criteria and the AI-PRD's failure-mode section directly.

That's every signal type in the schema mapped to a skill except signal 1 (eval regression — `eval-framework` already covers it as an import). Run gossip-mode to catch and route the informal signal; run the skill above that owns wherever it landed.

## QUALITY BAR

A real gossip-mode extraction: catches at least one signal the user didn't realize was structural; routes to specific file paths, not "I'll remember that"; separates high-confidence extraction from inference; surfaces the one immediate action (if any); asks before writing anything sensitive; and **compounds** — three months later the routed signals are in the right files when the team needs them.

**The test:** six months from now, when a future session reads `rules.md`, `hypotheses.md`, or the eval set, can it trace specific entries back to gossip moments? If yes, the routing worked. If the signals are invisible or duplicated, the schema needs sharpening.
