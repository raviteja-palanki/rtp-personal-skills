---
name: gossip-mode
version: v1.1.1_latest
description: 'Help turn an informal AI-product debrief into useful, traceable observations without turning a passing remark into an established fact. Look for evaluation gaps, prompt or model changes, cost and latency concerns, stakeholder preferences, and competitive leads. Separate what was reported from what is inferred, suggest the right existing records, and save only within the user’s authorization. Ask before newly storing sensitive or personal content; respect requests not to record it. Use when the user is thinking aloud or debriefing and would benefit from capture, not when they want only to be heard or have already given a specific task. Pairs with feedback-triage, interview-synthesis, production-observability, and signal-scanner.'
imports:
  - feedback-flywheel
  - eval-framework
---

# Gossip Mode — Informal Product Signals

Help useful observations survive a conversation in a form that a later decision can use. Listen first, distinguish evidence from interpretation, and route the material with its source and limits intact.

A remark may contain several useful leads, one lead, or nothing that needs a durable record. The goal is useful capture, not discovering a hidden pattern in every sentence or creating more files.

## Start with the user's intent and recording boundaries

Use this mode for an informal debrief or stream of observations when extracting and recording signals would help. If the user wants only to vent, acknowledge them without forcing a diagnostic exercise. If they ask a specific product question, request a deliverable, or already say exactly what to add where, handle that task directly.

**Separate listening, proposing, and saving.** An informal remark is not automatically a request to create durable memory. Show the proposed content and destination before a new recording action. When the user has already authorized that content and destination—or given applicable standing authorization—carry out the agreed work without asking again. Keep proposed, saved, verified, and unresolved items clearly distinct.

For sensitive material such as compensation, named complaints, or personal customer details, default to not creating an additional record. Use the minimum necessary detail and an appropriate audience when the user explicitly authorizes storage. Do not generalize a named person's temporary frustration into a permanent character judgment. Respect “do not record this” and similar limits. This governs the files and records you create; it is not a promise about the chat platform's retention.

External messages, tickets, and operational changes are separate actions. Follow the authorization for each action; do not send a complaint or alert to others merely because the conversation contains a concern. If action is needed but not authorized, prepare a concrete proposal or draft.

## The basic method

1. **Acknowledge briefly.** Reflect the situation in one or two sentences without diagnosing motives or turning the response into therapy.
2. **Extract the supported observations.** Preserve the distinction between a direct statement, a secondhand report, and an inference. Record unknown context rather than supply it.
3. **Choose the useful destination.** Inspect the relevant project records and use real paths. Prefer updating or linking an existing entry over duplicating the same source into several files.
4. **Identify any urgent assessment.** Assess potential impact and active exposure before assigning incident severity or interrupting other work.
5. **Save within authorization and verify.** Write only the agreed content, preserve provenance, and report what was actually saved. If confirmation is needed, offer a short, reviewable routing proposal.

## What a signal record needs

For each material item, keep enough context to understand and check it later:

- **Observation:** what the person actually said or what was directly observed.
- **Source and time:** who reported it, when, and how they know, using only authorized identifying details.
- **Scope:** product, task, user segment, prompt/model version, or incident period when known.
- **Interpretation:** the possible implication, clearly labeled as a hypothesis where appropriate.
- **Evidence gap:** what would establish, bound, or contradict the interpretation.
- **Route and next action:** destination, owner if known, and status.

A statement can be explicit and accurately captured while its underlying claim remains unverified. “The user reported four-second responses” is stronger than “production P95 is four seconds” when no distribution was measured.

## Eight signal types, in two families

These are routing lenses, not mutually exclusive labels. Record one source observation and link its implications where useful.

### Family A — The AI system may have changed

| Signal | Listen for | Candidate destination and check |
|---|---|---|
| **1. Evaluation gap or regression** | “It used to handle this,” or a case failing after a change. | Evaluation intake and a hypothesis record. First check whether the case exists, whether prior behavior was measured, and what correct behavior should be. |
| **2. Prompt-version regression** | “We changed the prompt and this stopped working.” | Prompt-version log and relevant regression case; record a rollback decision only if one was made. Establish the versions and other simultaneous changes. |
| **3. Model-version change or drift** | A task or style changing after a model update. | Capability or model-change log; route material economic or strategic implications separately. Preserve uncertainty about whether the model, inputs, or workflow caused the change. |
| **4. Cost or latency surprise** | A bill, response time, retry rate, or per-call cost moving unexpectedly. | Observability or cost-investigation record. Verify units, traffic, timing, and relevant measurements before changing baseline assumptions. |

A **regression** is a deterioration against an established earlier behavior or requirement. A single unexpected result may instead be a new case, ordinary variation, or a measurement difference. **Drift** can involve changing inputs or performance without a model-version change; a reported vendor change is a separate fact to establish.

### Family B — People or market conditions may have changed

| Signal | Listen for | Candidate destination and check |
|---|---|---|
| **5. Stakeholder dynamics** | A new request, objection, deadline, or stated preference. | Appropriate stakeholder notes, open decisions, or communication plan within authorization. Record the position and context, not an inferred enduring attitude. |
| **6. Capability shift in the model landscape** | A release or demo that appears to enable a task. | Capability-research queue and, if material, strategy review. Verify the release and test relevance before updating capability forecasts or half-life estimates. |
| **7. Informal competitive intelligence** | A meetup rumor or a customer's account of another product. | Signal-scanner queue or a clearly labeled competitive-map entry. A firsthand purchasing report establishes that report; it does not prove the competitor's performance. |
| **8. Acceptable-failure preference** | “I would rather it refuse than guess,” or an explicit speed/quality trade-off. | Candidate PRD assumption, evaluation criterion, or JTBD insight. Establish the task, consequence, and relevant population before changing the product's acceptance bar. |

Use `rtp-feedback-flywheel` and `rtp-eval-framework` to turn a validated failure report into useful evaluation coverage. A **golden or regression set** contains curated cases and expected behavior used for comparison. Version changes to it, retain suitable stable coverage, and do not assume adding a case makes recurrence impossible. A reported preference alone is not necessarily the correct test label.

## Route evidence according to its status

| What is established | Appropriate treatment |
|---|---|
| A first concrete report of a possible failure | Record as an observation or hypothesis, with evidence needed. |
| Several reports of a pattern | Check independence, scope, and counterexamples; propose a stronger hypothesis or rule review where justified. |
| A decision made or reversed | Record the decision and rationale in the project's decision record or change log. Do not turn a suggestion into a decision. |
| A relevant stakeholder preference | Store only within the recording authorization and with its context; link a consequential unresolved question. |
| A reproducible production failure with an established expected outcome | Add suitable evaluation coverage through the evaluation workflow and record the change. |
| A claimed new capability | Queue verification; update the assessed capability when evidence supports it. |
| A cost or latency anomaly | Investigate impact and measurement; update the model when the relevant numbers are established. |
| Competitive information | Preserve its source and uncertainty in the appropriate research or map entry. |

The original “three confirmations become a rule” shortcut is not a governance standard. Three people repeating one rumor are not three independent sources. Promotion requires a scoped claim, supporting and contrary evidence, a useful test, and the applicable approval or governance process. Follow the current rules for `hypotheses.md` and `rules.md`; do not promote automatically.

Use existing destinations such as an evaluation intake, prompt log, `CHANGE_LOG.md`, stakeholder record, or cost model only after locating them. If a suitable file does not exist, propose its location rather than pretend it already does. Cross-link records to a common source when multiple implications matter.

## Worked example — a standup debrief

**User says:** “Vinod was annoyed in standup that the AI answered Q3 wrong but Q1 and Q2 right. Said he'd rather it refuse than guess. Also the latency was up—like four seconds for what used to be one and a half.”

**A useful response:** “That sounds frustrating. There are two issues worth separating: the wrong answer and the reported slowdown. The refusal preference may help define acceptable behavior once the question and its context are clear.”

| Signal | Supported extraction | What is not yet established |
|---|---|---|
| Reported quality failure | Q3 was reported wrong while Q1 and Q2 were reported right. | The actual questions, correct answers, reproducibility, and whether the case was in the evaluation set. “Q3” may simply mean the third question, not a stable query class. |
| Failure preference | Vinod reportedly preferred refusal to guessing in this situation. | A general preference for every ambiguous query, or permission to store a named complaint. |
| Reported slowdown | Responses were described as about four seconds versus an earlier one and a half. | P95, affected volume, time window, cause, SLO impact, and incident severity. |
| Possible design implication | The case may warrant examining uncertainty handling or evaluation coverage. | A proven confidence-calibration defect or a decision to change a threshold. |

**Proposed routing, if capture is wanted:**

- [ ] **Located evaluation-intake file** → the reported Q3 failure, with the actual input and expected behavior still to be obtained. A correct answer, clarification, or abstention may be appropriate depending on the task; do not pre-label all Q3-like cases “refuse.”
- [ ] **Located hypothesis record** → a scoped uncertainty-handling or coverage hypothesis, with the observation linked and the missing evidence explicit.
- [ ] **Appropriate preference record, if authorized** → the context-specific refusal preference, minimizing personal detail and omitting the emotional complaint unless it serves an authorized purpose.
- [ ] **Located operations-investigation record** → the reported slowdown, requesting the workload, time window, and observed latency distribution.

These destination labels illustrate the proposal. In actual use, replace them with verified file paths and concrete proposed text before saving. Do not create four copies of the same conversation merely because four implications are possible.

**Immediate assessment:** check whether the slowdown is ongoing and materially affects users or a commitment. Four seconds is not automatically a P0 incident. If evidence warrants escalation, follow the authorized incident workflow and its severity definitions. A universal “open a P0 now” or “root-cause within 24 hours” does not follow from this remark.

## Treat informal disclosure as a clue, not a diagnosis of the team

Trust in an individual and psychological safety in a group are related but different concepts. The original source distinguishes relational trust—care and respect—from transactional trust—competence, reliability, and intentions. Team psychological safety concerns whether people expect interpersonal risks such as questions or concerns to be handled safely. [Edmondson's original study](https://doi.org/10.2307/2666999) examined this at team level.

The local August 2026 HBR account, **“How the Best Leaders Shape Conversations,”** describes teams in which individual trust did not automatically produce group candor. This motivates checking the setting in which people can speak; it does not establish that high-trust teams always produce more gossip, that gossip proves the group channel is closed, or that only psychological safety predicts voice.

If a pattern matters to the user's task, distinguish a concern never raised from one raised and dismissed. Ask about the relevant group setting rather than use a broad colleague-trust question as a substitute. The NOVEL INSIGHTS second-order-candor lens can inform that inquiry, but two survey items do not conclusively diagnose suppression or an override problem. Route deeper assessment to `rtp-judgment-guard` or `rtp-alignment-check` when useful and authorized.

## Response format

Keep the response proportional to the debrief:

1. **Acknowledgment:** one or two sentences.
2. **What I heard:** observations and implications, with uncertainty beside each; use a small table only if it helps.
3. **Routing:** verified destination → proposed content, or a clear report of an already authorized save. Checkboxes can let the user accept a subset.
4. **Immediate assessment or action:** the highest-priority justified item, with its authorization and status clear.
5. **Evidence confidence:** distinguish explicit reporting, supported inference, and unverified claims. Do not assign a false percentage or one confidence label to all layers.

After a save, verify the entry and any links. State what changed and where. Do not claim durable memory merely because a sentence appeared in chat.

## Where this connects to the library

The existing imports remain **`feedback-flywheel`** and **`eval-framework`**. They support evaluation intake and improvement, without authorizing every proposed destination automatically.

- `rtp-feedback-triage` handles structured feedback at volume; `rtp-interview-synthesis` handles structured transcripts.
- `rtp-production-observability` investigates operational signals and appropriate escalation.
- `rtp-signal-scanner` and `rtp-competitive-map` handle market leads with provenance and verification status.
- `rtp-capability-tracking` assesses model changes and capability forecasts; `rtp-cost-model` updates economics from validated inputs.
- `rtp-prompt-as-product` handles prompt versions, regression evidence, and rollback decisions.
- `rtp-stakeholder-communications` develops an appropriate message when communication work is requested; it does not imply permission to send it.
- `rtp-jtbd-analysis` and `rtp-ai-prd` examine failure preferences and user trade-offs before changing requirements.

## Quality and limits

A useful extraction preserves what was said, labels what was inferred, avoids unnecessary personal records, uses real destinations, and makes any immediate action proportionate to the evidence. It can conclude that nothing should be saved.

Skip a separate extraction when the user already supplied structured instructions or when it would interrupt an active workflow without adding value. Keep any needed side notes within the task's authorization and return to them at an appropriate point. Respect requests not to record or route material.

The traceability test is practical: when a future decision uses an entry, can the reader find its source, scope, verification status, and subsequent changes? Review duplicates and stale interpretations. A memorable remark becomes useful evidence through that care, not through the number of files it reaches.
