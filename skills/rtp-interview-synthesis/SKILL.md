---
name: rtp-interview-synthesis
description: >
  Open coding → axial coding → selective coding for customer interview
  transcripts. NOT for AI trace synthesis (that's eval-framework's job) — for
  human conversations. Use when a stack of 5-15 interview transcripts needs to
  become themes, persona signals, opportunity hypotheses, and eval-test
  candidates. Applies the same machinery that AI eval teams use on traces, so
  the codes that emerge from interviews can become failure-mode tests later.
imports:
  - jtbd-analysis
  - uncertainty-research
  - eval-framework
---

# Interview Synthesis

Turn a stack of interview transcripts into structured insight using the open-coding → axial-coding → selective-coding workflow that serious eval teams already run on AI traces.

> Most PMs synthesize interviews by skimming for quotes that confirm what they already believe. The 0.1% angle: use the same coding discipline on humans as you do on machines, and patterns emerge instead of getting cherry-picked.

---

## DEPTH DECISION

**Go deep if:** You have 5-15 customer interview transcripts to synthesize, you're shaping a problem space, or the team is debating "what did we hear?" with different people pointing to different quotes. Use the full coding workflow when the synthesis will inform a roadmap or PRD.

**Skim to axial coding if:** You already have open codes and need to cluster them into themes.

**Skip if:** Sample size is fewer than 3 (no pattern can be extracted reliably), or the interviews are sales calls in disguise (see RED TEAM).

---

## DELIVERABLE FORMAT

Before starting, ask:

> **Format?**
> 1. **Synthesis doc** — Themes, codes, persona signals, opportunity hypotheses, eval candidates. Best for sharing with the team.
> 2. **Tagged transcripts + synthesis doc** — Coded transcripts plus the rollup. Best for evidence-heavy reviews.
> 3. **Inline summary** — Top 5 themes, top quotes, and design implications. Best for fast iteration.
>
> *Default: Synthesis doc.*

---

## THE STRUCTURAL INSIGHT

Most PMs synthesize interviews by reading transcripts, highlighting "good quotes," and writing a 3-bullet summary. This is fast. It's also useless — you end up with quotes that confirm whatever the PM walked in believing. Patterns nobody noticed don't get surfaced. The quiet contradictions get smoothed over.

**The 0.1% angle: use the same machinery on humans and machines.**

Hamel Husain and Shreya Shankar's open-coding → axial-coding workflow is the core technique that serious AI eval teams run on traces — first you label every observation with a fresh code, then you cluster the codes into categories, then you pick the categories that drive the system's behavior. It's the same workflow grounded theory researchers have used on qualitative data for 50 years.

Apply it to interview transcripts and three things happen:

1. **Pattern emergence beats confirmation bias.** When you label every observation before deciding what's important, the patterns surface from the data rather than being imposed on it.
2. **Codes from interviews become eval failure modes.** The categories that emerge ("user expects faster response," "user doesn't trust the recommendation") translate directly into eval test cases when the AI feature ships.
3. **Coverage is auditable.** You can show that every quote got a label, which means stakeholders can audit your conclusions instead of trusting your judgment.

This skill is the bridge between qualitative discovery and AI evaluation. Most PMs miss the bridge — they treat interviews and evals as separate workstreams. They're not. The codes are the connection.

---

## THE METHOD

Three coding passes. Each pass operates on the output of the previous one. Don't skip passes — the rigor compounds.

### Pass 1: Open Coding (line-by-line)

Read every transcript line by line. For each meaningful observation, write a short code label (3-7 words). Don't try to organize. Don't try to interpret. Just label.

**The discipline:** stay close to the data. The code should describe what the user said or did, not what you think it means. "User mentioned spreadsheet workflow" is open coding. "User feels constrained by tools" is interpretation — save that for axial coding.

**Example excerpt and codes:**

> Interview 03, plant operator: "I usually look at the alert dashboard in the morning, but if there's a lot of red, I just start at the top and work down. I don't really trust the prioritization — half the time the top one is something that's been red for weeks."

Open codes:
- Morning alert review routine
- Top-down processing when overloaded
- Distrust of system prioritization
- Stale alerts in top position
- Workflow doesn't filter resolved issues

> Interview 03 (continued): "Last month we had a real issue and the alert was buried on page 3. So I started checking page 3 and 4 first, just to be safe. My buddy thinks I'm crazy."

Open codes:
- Real failure was deprioritized by system
- Operator developed workaround (checking back pages)
- Workaround mocked by peers
- Distrust translates to extra work

A single 30-minute interview produces 50-150 open codes. Don't worry if codes overlap — that's expected. The clustering happens in pass 2.

**What to code:**
- What the user said (literal observations)
- What the user did or stopped doing (behavioral observations)
- Emotional language (frustration, relief, anxiety, pride)
- Workarounds (the things users built around the official workflow)
- Contradictions (where the user said one thing earlier and another now)
- Silences (questions they declined to answer or pivoted away from)

**What NOT to code:**
- Your interpretations ("user is frustrated" — that's pass 2)
- Your design ideas ("we should add filtering")
- Your judgments ("user is wrong about X")

### Pass 2: Axial Coding (clustering)

Now you have 200-1500 open codes across all interviews. Cluster them into 8-15 axial categories. Each axial code is a theme that connects multiple open codes.

**The technique:** sort the open codes onto sticky notes (or rows in a spreadsheet). Group by similarity. Name each group. Iterate — codes will move between groups as you see the structure.

**Example axial codes (continuing from Pass 1):**

| Axial code | Open codes that cluster here |
|---|---|
| **Distrust of system prioritization** | Distrust of system prioritization (I-03), "ranking is random" (I-05), "I check my own list" (I-07), "system doesn't know what's important" (I-09) |
| **Workarounds for unreliable signals** | Operator developed workaround (I-03), uses Excel for trending (I-05), keeps personal notebook (I-08), "I just memorize critical assets" (I-11) |
| **Anxiety about audit-defensibility** | "If something goes wrong, I need to show I checked" (I-04), "we keep paper logs in case the system loses data" (I-09), "my manager will ask why I didn't act" (I-12) |
| **Cognitive load during morning review** | Top-down processing when overloaded (I-03), "I don't have time to read every alert" (I-05), "I skim and pick the obvious ones" (I-08) |
| **Distinct emotional tones in alerts vs incidents** | "Alerts are background noise" (I-03), "incidents are scary" (I-07), "alert fatigue is real, incidents wake me up" (I-11) |
| ... | ... |

A healthy synthesis has 8-15 axial codes. Fewer than 8 means you're under-clustering (everything is "user wants better experience"). More than 15 means you didn't push past surface differences.

**Frequency matters but isn't sufficient.** A code that appears in 8 of 10 interviews is signal. A code that appears in 2 of 10 interviews but is emotionally loaded ("I cried when I saw this") might be a deeper signal that affects more users than your sample showed.

### Pass 3: Selective Coding (the spine)

Now pick 3-5 selective codes — the categories that drive the most behavior or have the highest design implication. Selective codes are the spine of your synthesis: everything else hangs off them.

**The test:** if you removed this category from the synthesis, would the design implications change? If yes, it's a selective code. If no, it's an axial code that supports a selective code.

From the example:
- **Selective code 1: Distrust of system prioritization is the binding constraint.** If users don't trust the prioritization, they don't act on top alerts — and the AI's accuracy doesn't matter.
- **Selective code 2: Operators are doing audit-defensibility work that the system doesn't capture.** Their paper logs and personal notebooks are evidence that the official audit trail is insufficient.
- **Selective code 3: Cognitive load is concentrated in morning review.** This is when most decisions get made and most alerts get ignored. Time-of-day matters.

These three selective codes drive the design implications, the persona signals, and the eval candidates. Everything else is supporting evidence.

---

## AI-PRODUCT INTERVIEW NUANCE

Interviewing about AI features is harder than interviewing about traditional software, because users can't articulate what they actually want from probabilistic systems. Their expectations are formed by movies, marketing, and a couple of viral demos — not by experience.

Three patterns to watch for:

### 1. Users describe magic, not workflow

When asked what they want from an AI feature, users default to the marketing pitch: "I want it to just do my job." This isn't useful. Probe for the actual workflow:

- "Walk me through the last time you did this task without AI. What were the steps?"
- "Where in that flow does AI fit? What does it replace, what does it augment?"
- "What does the AI need to know that you currently know?"

The gap between "I want it to just do my job" and the actual workflow they describe is where the design lives.

### 2. Users underweight failure cost

Ask "what if the AI is wrong?" and most users say "I'd just correct it." This is rarely true. Watch for these signals:

- They describe a workflow with no review step → they assume AI is right
- They describe high-frequency use ("I'd use it for every email") → they don't realize they'd stop noticing errors
- They describe high-stakes contexts ("this is for client communication") → the cost of confidently-wrong is much higher than they'll admit

The interview job is to surface the failure cost they're underweighting, so the design can compensate.

### 3. Users articulate trust as a feeling, not a behavior

"Do you trust the AI?" gets you "I guess?" or "yes, mostly." Useless. Reformulate:

- "When the AI gives you an answer, what do you do with it? Do you check it? How?"
- "Has the AI been wrong? What happened? What changed after that?"
- "If the AI made a recommendation that you weren't sure about, what would you do?"

Behavior reveals trust. Words obscure it.

### The 5 Hardest Questions to Ask in an AI-Product Interview

These are the questions most PMs skip because the answers are uncomfortable. Skip them and your synthesis will be polite and wrong.

**1. "Tell me about a time the AI was wrong. What did you do?"**

If they can't recall a specific instance, either they're not paying attention to errors, or they don't use the feature often enough to have hit one. Both are signals.

**2. "What would have to be true for you to stop using this feature entirely?"**

Reveals the fragility of adoption. AI feature trust is not durable — small failures can cause large defections. The threshold matters.

**3. "If your manager asked why you trust the AI's recommendation, what would you say?"**

Surfaces the social and audit dimensions. If they have no answer, they don't trust the AI — they tolerate it.

**4. "What does this AI prevent you from getting better at?"**

The skill-atrophy anxiety is rarely volunteered. It's almost always present. Asking directly gives users permission to name it.

**5. "If we removed this feature tomorrow, what would change for you?"**

Tests whether the feature is actually load-bearing in the workflow, or whether it's a nice-to-have that users would shrug off. Most AI features get this answer wrong.

### What to Listen For in the Silence

The pauses, deflections, and topic-pivots in AI-product interviews carry as much signal as the words.

- **Pause before "yes, I trust it":** the trust isn't actual, it's social. Probe further.
- **Topic pivot when asked about errors:** the user doesn't want to admit they got burned. Make it safe ("I'd guess this happens to everyone — what was your experience?").
- **Deflection to "the team uses it differently":** they're describing what they think you want to hear, not what they do. Bring the conversation back to their personal workflow.
- **Nervous laugh when asked about audit-defensibility:** real concern, not joke. Probe.

Code these silences in pass 1. They're as much data as anything spoken.

---

## CROSS-LINK WITH `eval-framework`

This is the integration most PMs miss.

The axial codes that emerge from interview synthesis become eval failure mode candidates when the AI feature ships. Same machinery, same labels, just applied to different inputs.

**Example mapping:**

| Axial code from interviews | Eval failure mode candidate |
|---|---|
| Distrust of system prioritization | "Prioritization order matches expert ranking ≥X% of the time" — eval test |
| Anxiety about audit-defensibility | "Every recommendation has timestamped, exportable audit log" — system property test |
| Confident-wrong fear | "Confidence calibration: when system says 'high confidence,' actual accuracy is ≥95%" — calibration eval |
| Cognitive load during morning review | "Top-5 alerts include 90% of true high-priority issues" — ranking quality eval |
| Skill atrophy concern | "User can disable AI suggestions and feature still functions" — graceful degradation test |

**The chain:**

1. Open codes from interviews → axial codes (themes) → selective codes (drivers)
2. Selective codes → user-need hypotheses → design implications
3. Design implications → required system behaviors → eval test candidates
4. Eval test candidates → eval-framework workstream

Most PMs hand off the synthesis to design and forget about evals. The synthesis is the evidence base for evals — it's what makes the eval design grounded in real user expectations rather than internal speculation.

When the eval team asks "where did this failure mode come from?", the answer should be "axial code 4 from the interview synthesis dated [X]." That's the audit trail that makes evals defensible to leadership.

---

## REAL-WORLD ENTERPRISE EXAMPLE — Fortune 100 / world-class AI-native startup scale

Synthesizing 8 plant-operator interviews about a predictive maintenance UI. Real-world setup: 6 operators across 3 plants, 2 reliability engineers. 30-45 minutes each. Audio recorded and transcribed.

### Pass 1 output (open coding)

Across 8 transcripts: 1,247 open codes. Examples:

- "Morning alert review takes 20-40 mins"
- "I trust my own judgment more than the dashboard"
- "Last week the system flagged a critical asset, I missed it"
- "Reliability engineer reviews my decisions weekly"
- "I keep a personal Excel for my plant"
- "Dashboard order seems random"
- "I look at the asset name first, severity second"
- "Critical asset list is in my head, not in the system"
- "I want a 'snooze' option for known issues"
- "False alarms make me check less often"
- "Real failure last quarter — I wasn't at the top of dashboard"
- "I cross-reference with the maintenance team's report"
- ...

### Pass 2 output (axial coding)

Clustered into 11 axial codes:

1. Distrust of system prioritization (47 open codes across 7 interviews)
2. Workarounds for unreliable signals (38 codes, 8 interviews)
3. Anxiety about audit-defensibility (29 codes, 6 interviews)
4. Cognitive load during morning review (52 codes, 8 interviews)
5. Asset-specific mental models override system rankings (31 codes, 5 interviews)
6. False alarm fatigue (44 codes, 8 interviews)
7. Real-failure fear (the rare case that wasn't in the system) (22 codes, 4 interviews)
8. Lack of "snooze" or known-issue tracking (19 codes, 6 interviews)
9. Implicit collaboration with reliability engineers (28 codes, 7 interviews)
10. Plant-specific knowledge gaps in the system (18 codes, 5 interviews)
11. Time-of-day patterns in attention (24 codes, 6 interviews)

### Pass 3 output (selective coding)

Three selective codes drive the design:

**Selective code 1: Operators don't act on the system's prioritization — they re-prioritize from their mental model.** Codes 1, 5, 8 cluster here. This is the binding constraint. Until the system's prioritization matches operator mental models, the rest doesn't matter.

**Selective code 2: Audit-defensibility is the unspoken use case.** Codes 3, 9 cluster here. Operators are doing audit work the system doesn't capture, and that work is invisible to product.

**Selective code 3: Attention is concentrated in the morning, but failures aren't.** Codes 4, 11 cluster here. The system optimizes for the wrong window.

### Personas and opportunity hypotheses

**Persona signal:** "The mental-model-first operator." Across 5 of 8 interviews, this archetype emerged: experienced operators who layer the system's recommendations onto their own mental ranking, and only act when both align. They ignore alerts that contradict their mental model. Designing for them is different from designing for newer operators.

**Opportunity hypotheses (with evidence):**

1. *Operators would adopt the system more if it explained WHY it ranked an alert highly.* (Evidence: codes 1, 5; 7 of 8 interviews)
2. *A "snooze" or "known-issue" feature would reduce alert fatigue without losing real signals.* (Evidence: codes 6, 8; 6 of 8 interviews)
3. *Surfacing audit-defensibility (timestamped logs of decisions) would shift the perceived value of the system from "alert engine" to "decision record."* (Evidence: codes 3, 9; 7 of 8 interviews)

### Eval test candidates (what flows to eval-framework)

- Test: "Top-5 ranked alerts include 90% of operator-confirmed high-priority issues" — derived from selective code 1
- Test: "When operator overrides system ranking, override rate <40% for first 4 weeks of use" — derived from axial code 5
- Test: "System provides exportable audit log for every recommendation, including operator disposition" — derived from selective code 2
- Test: "Confidence threshold for 'high priority' label produces ≥95% accuracy on Tier-1 assets" — derived from axial code 6 + 7

These tests aren't speculative — they're grounded in the synthesis. When the eval team asks where they came from, the audit trail goes back to specific interviews and specific codes.

### Design implications

Three design moves emerged from the synthesis:

1. **Add a "why this rank?" tooltip to every recommendation.** Operators need to see the reasoning, not just the score, to overcome distrust. Without this, the new prioritization model won't be adopted regardless of accuracy.
2. **Add structured disposition logging.** Every recommendation gets a one-line operator response (acted / declined / deferred + reason). This becomes the audit trail and the training data.
3. **Differentiate alert severity by attention window.** Alerts that arrive outside the morning review get a different UI treatment (notification, escalation) because operator attention is asymmetric across the day.

This is what synthesis output should look like: themes are evidence-grounded, persona signals are surfaced, opportunities are hypothesis-shaped (testable, falsifiable), and the eval candidates flow downstream.

---

## DELIVERABLE FORMAT

Every synthesis produces six artifacts:

### 1. Coded transcripts (or coded transcript summary)

Either tag the transcripts directly (using a tool that supports highlighting + labels) or produce a code-frequency table per interview. The point is auditability — anyone reading the synthesis can trace a theme back to the source.

### 2. Axial codes table

The 8-15 themes with frequency counts and representative quotes.

### 3. Selective codes (the spine)

3-5 categories that drive the most design implication. Each one with a one-paragraph rationale.

### 4. Persona signals

Patterns that suggest a persona update. New behaviors, new motivations, new constraints. Distinct from existing personas — note the difference.

### 5. Opportunity hypotheses

Each opportunity framed as: "If we [intervention], [user segment] will [behavior change], because [evidence from synthesis]." Hypothesis-shaped, not feature-shaped.

### 6. Eval test candidates

The bridge to `eval-framework`. Each test grounded in a specific axial code with a citation back to the synthesis.

---

## CROSS-LINK WITH ADJACENT SKILLS

- **`jtbd-analysis`** — Interview synthesis is one of the input methods for JTBD. Switch interviews are coded with this skill, then mapped to the four forces.
- **`uncertainty-research`** — The research methods in uncertainty-research describe HOW to collect interviews. This skill describes how to synthesize them.
- **`eval-framework`** — Selective codes become eval test candidates. The chain runs from interviews to evals, with this skill as the bridge.
- **`failure-modes`** — Anxiety codes from interviews map to failure modes that hurt most. The user told you what scares them; design and eval for that.

---

## RED TEAM

This skill produces noise instead of signal when:

**Sample size is below 3.** With 1-2 interviews, you can't extract patterns reliably. Anything that looks like a pattern is anecdote dressed up. Either run more interviews, or use a different method (single-user diary study, behavioral analytics).

**The interviews are sales calls in disguise.** When the "interview" is actually a pitch with the user agreeing to be interviewed for politeness, the codes will be polite and useless. Signs you have this problem: the interviewer is also the salesperson, the user has a commercial relationship at stake, the questions are leading ("would you find this helpful?"). Re-interview with someone unaffiliated with the sale, or discard.

**The interviewees are all from one persona.** Synthesis from 10 interviews with one user type produces a deep but narrow view. If the design serves multiple personas, run separate synthesis cycles per persona — don't mush them together.

**The synthesis is being used to confirm a pre-decided direction.** When leadership has already committed and asks for "research to support the launch," the coding will (subconsciously) bend toward confirmation. Run the synthesis with someone who didn't make the decision, or be explicit that the synthesis is post-hoc rationalization, not discovery.

**The transcripts are summaries, not verbatim.** Summary transcripts have already been filtered through someone's interpretation. The codes you'd extract are codes about the summarizer's mind, not the user's. Use verbatim transcripts (audio + transcription tools) for any synthesis that will inform decisions.

---

## WHEN WRONG

This skill misfires when:

- **The PM does the coding alone.** Single-coder synthesis has known reliability problems — different coders see different patterns. For high-stakes synthesis (roadmap-shaping), have at least one other person code 30% of the transcripts independently and compare. Disagreement is informative; never reaching disagreement means one coder is dominating.
- **Codes are too abstract from the start.** "User experiences friction" is not an open code. It's an interpretation. Stay close to the data in pass 1 — abstraction earns its place in pass 2 and 3, not pass 1.
- **The selective codes don't change the design.** If the synthesis ends with "users want a better product," the selective coding wasn't done. Push past the obvious.

---

## QUALITY GATE

Before shipping the synthesis:

- [ ] Every transcript has been read and coded (not just skimmed)
- [ ] Open codes are descriptive, not interpretive
- [ ] Axial codes are 8-15 (not 3 generic ones, not 50 hyper-specific ones)
- [ ] 3-5 selective codes are named and rationalized
- [ ] Frequency counts are present (how many interviews surface each theme)
- [ ] Representative quotes are verbatim, not paraphrased
- [ ] At least one finding contradicts the team's prior beliefs (otherwise the synthesis is confirmation)
- [ ] The synthesis flows downstream — opportunity hypotheses are explicit, eval candidates are listed

---

## CONCLUSION

A complete interview synthesis ends with one paragraph:

> "The pattern that surprised us is [selective code]. The pattern that's most consequential for design is [selective code]. The next research move is [next step]. The eval implications for the AI feature are [list]. We're refining our persona to add [signal]."

If you can write that paragraph confidently, the synthesis is done. If not — go back to selective coding. That's where the work usually skipped.
