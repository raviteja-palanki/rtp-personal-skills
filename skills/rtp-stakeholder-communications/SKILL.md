---
name: stakeholder-communications
version: v1.7_latest
description: 'Audience-tailored communication for AI features: exec summaries, engineering briefs, launch announcements, risk escalations, weekly digests. The differentiator is AI-native confidence framing: every claim about a model''s behavior carries an eval-backed band, a named drift surface, and a mandatory "what could be wrong" section. Use when a single piece of information needs to land in three rooms (exec, engineering, customer) and each room is going to ask a different "but what''s the failure rate?" question. Do NOT use for internal team chat, casual PR updates, or comms about deterministic features where probabilistic framing is theater. Triggers: "stakeholder update," "exec briefing," "escalate to leadership," "launch announcement," "weekly digest," "send a note to." Pairs with: dual-lens (business AND technical legibility), trust-under-fog (confident comms on uncertain outcomes), first-principles (read the live need before supplying your default).'
imports:
  - ai-product-metrics
  - eval-framework
  - problem-ai-fit
  - trust-under-fog
  - confidence-tuner
---

# Stakeholder Communications: AI-Native Edition

## DEPTH DECISION

**Go deep** — read the whole skill — when: writing the launch announcement for an AI feature, escalating a model failure to an SVP, drafting a board-facing AI capability briefing, or putting your name on a quarterly update where someone will ask "but what's the failure rate?"

**Skim to AI-NATIVE CONFIDENCE FRAMING** when: you already have a draft, you just need to pressure-test the probabilistic claims before sending.

**Skip** when: you're sending a deterministic-feature update (rules engine, integration ship, CRUD launch) — the AI scaffolding here will read as theater. Use `pm-execution:write-stories` or a normal PRD update instead.

## THE STRUCTURAL INSIGHT

Most PMs treat stakeholder communication as a tone problem. It is not. **It's an evidence problem.** The reason an exec, an engineer, and a customer can read the same AI launch update and reach different conclusions is not that the message was tonally wrong — it's that the message did not anchor any of them to the same eval evidence, the same drift surface, the same boundary condition. They each filled the gap with their own assumption. By the time the model misfires in production, the exec thinks you over-promised, the engineer thinks you under-specced, the customer thinks the product is broken. None of them are wrong. The PM gave them three different mental models of the same feature.

The 0.1% move: **one set of eval evidence, three audience-shaped framings.** Engineers see the eval matrix and prompt diff. Execs see the boundary condition in plain English ("works for use case X, degrades when Y exceeds Z, fallback is W"). Customers see the experience and the human-in-the-loop. All three are anchored to the same number, the same regression test, the same drift watch. You cannot be caught with a different story in different rooms.

This is the Bridger move applied to comms. Not "translate jargon." Translate the *underlying evidence* into each audience's decision language without losing the evidence.

## KEY TERMS (plain language)

- **Boundary condition** — the plain-English statement of where the feature works, where it degrades, and what the fallback is.
- **Drift surface / drift watch** — where and how an AI's quality can quietly decay over time, and the language you use to flag it.
- **Eval-backed claim** — a statement about the model's behavior tied to a specific test result, not a hand-wave.
- **Audience tier map** — the table matching each audience to what they need and the decision they're making.
- **The six needs** — protection, fairness, vision, expertise, affiliation, status; the human need that's live for a given audience.
- **The Bridger move** — translating the same underlying evidence into each audience's decision language without losing the evidence.

## READ THE LIVE NEED FIRST

The tier map below tells you *how to say it* (each audience's decision language). This step tells you *what they need to hear* — the human need that's actually live for them right now. Research on 3,500+ working adults across three countries found people judge a communicator against six recurring needs, and capable people fail by over-supplying the one they're good at while a different one goes unmet:

- **Protection** — reduce my risk before I commit (the engineer's "where does this break?").
- **Fairness** — decide consistently; even a hard call lands if the rule is even (the resource-allocation ask).
- **Vision** — tell me where this is going and why it matters (the exec's "why fund this?").
- **Expertise** — help me understand what I can't yet judge (the cross-functional partner).
- **Affiliation** — include me; keep the group whole.
- **Status** — get me recognition and standing (the board-facing win).

**Why it matters:** this doesn't replace the skill's core rule (anchor everyone to the same eval evidence) — it drives the *framing* of that evidence. A protection-need audience and a status-need audience get the *same* eval number, framed differently: "here's the boundary condition that protects you" versus "here's the win you can take to your board." The trap is supplying the need *you* like giving (usually vision or expertise) rather than the one that's live. So two extra beats before you write: (1) name the live need, (2) name your own default and check it isn't overriding theirs.

**When this is wrong:** in a low-trust or high-fear room the real need is hidden because it's unsafe to voice, so "read the need" fails exactly when it matters most — there, default to protection and fairness, which are safe to over-supply. And don't treat the six needs as a measured law; it's a vocabulary, not a formula.
*(Source: "Are You Meeting the Needs of the People You Lead?", van Vugt, Sheng & Andrews, HBR, 13 May 2026 — self-reported survey, ◆.)*

## AUDIENCE TIER MAP

| Audience | What they need | What they don't | Decision they're making |
|---|---|---|---|
| **Executive (VP/SVP/CPO/CEO)** | Boundary condition. Cost trajectory. Trust trajectory. One ask. | Eval methodology. Prompt internals. Sprint-level status. | Should I keep funding this? Defend it externally? Kill it? |
| **Engineering (EM/Tech Lead/IC)** | Eval matrix. Prompt diff. Failure surface. Open architecture questions. | Customer narrative. ROI framing. | What do I build, ship, instrument, or push back on this sprint? |
| **Cross-functional (Design/Legal/Sales/Support)** | What changes for *their* workflow. Edge cases that hit *their* surface. | The full eval matrix. The prompt history. | How do I represent this to my own audience? What do I need to update on my side? |
| **Customer (External user/buyer)** | What it does. What it doesn't do. What happens when it's wrong. The human escape hatch. | Confidence numbers, model versions, internal benchmarks. | Should I trust this with my workflow? When do I override it? |
| **Board (Quarterly/Strategic)** | Capability trajectory. Risk register. Competitive position. Capital efficiency. | Roadmap detail. Prompt-level debate. | Is the company investing the right amount in the right capability? |

**The mandatory translation rule:** the exec view and the engineering view of the same feature must reconcile to the same eval number. If the exec hears "94% accuracy" and engineering hears "92% on heldout, 87% on out-of-distribution," you have a credibility bomb on a fuse. Pick one number, define it once, frame it in each audience's language.

## THE 5 COMMUNICATION TYPES

### 1. Executive Summary

**When to use:** A decision is needed from leadership, or leadership awareness is required for an event they will be asked about externally. Never both in the same note — pick one.

**Structure (Pyramid Principle / Minto SCR):**
- **Bottom line (one sentence):** "We are on track / at risk / off track on [initiative], because [boundary condition]. Decision needed: [yes/no on specific ask]."
- **Situation:** Where things stand in two sentences.
- **Complication:** What changed or what's in the way. Specific, not "execution challenges."
- **Resolution / Recommendation:** What you're doing about it, and what you need from leadership.
- **AI evidence anchor:** One line. "Eval as of [date]: 91% accuracy on labeled set N=400, degrades to 78% on long-tail queries. Drift watch: weekly. Fallback: rules engine + human review."

**Length:** 150 words. If it's longer than the executive's screen without scrolling, cut it.

**Anti-patterns:**
- "We've made significant progress" with no number behind it
- Five risks listed equally without a recommended priority
- Decision needed and awareness mixed in the same note (the exec will only act on one)
- AI claim with no eval anchor ("model is performing well")

### 2. Engineering Brief

**When to use:** A decision affects what engineering builds, instruments, or reviews this sprint. Or engineering needs context to make better implementation choices on something already in flight.

**Structure (Context-first):**
- **Why this matters (2 sentences):** The user problem and the structural reason this is the right approach.
- **Current state:** What's shipped, what's in flight, what's blocked. Owners and ETAs.
- **The eval matrix:** The actual table. Accuracy by class, latency P50/P95/P99, hallucination rate, cost per inference. Linked to the dashboard.
- **The prompt diff:** What changed since last shipped version. Why. What regressed in evals, what improved.
- **Open architecture questions:** What you need engineering input on *before* the next decision point.
- **What's not changing:** Important. Engineers anchor on stability — explicitly call out the contract that's stable.

**Length:** 400-700 words. Engineers expect more density and less polish than execs.

**Anti-patterns:**
- Marketing language ("game-changing model upgrade")
- Eval claims without methodology or sample size
- "We need to discuss" without a specific question
- Hiding regressions ("v2.1 ships Friday" with no mention that confidence calibration got worse)

### 3. Launch Announcement

**When to use:** Feature is shipping to customers, or a new capability is going GA. Required: an internal version (sales, support, success) and an external version (customer-facing).

**Structure (Narrative):**
- **The user moment:** Open with the situation the user is in when this matters. Not "We are excited to announce." A specific user, a specific Tuesday afternoon.
- **What it does:** Plain language, benefit-first. "You can now..." not "The system supports..."
- **What it doesn't do (mandatory for AI features):** The boundary condition. "It works well for X. It's not designed for Y. If you're trying to do Z, here's the workaround."
- **What happens when it's wrong:** The fallback. The human-in-the-loop. The override. AI features that don't show their failure path lose customer trust the first time the model misfires.
- **How to give feedback:** A real channel. Not "let us know." A link, a name, a Slack channel.

**Internal version adds:**
- Eval results customers don't need to see (the actual confidence band, the regression test status)
- Sales talking points and objection handling
- Support escalation path for the failure mode that *will* happen in week two

**Anti-patterns:**
- AI feature launch with no boundary condition stated
- Confidence claim ("highly accurate," "industry-leading") with no number, no segment, no methodology
- Hiding the human-in-the-loop because "it sounds less impressive"
- Same copy for internal and external (sales needs different evidence than customers)

### 4. Risk Escalation

**When to use:** A model regressed, an eval gate failed, a drift threshold tripped, or a launch is at risk because of an AI-specific issue. Bias toward escalating early — surfacing a 60% probability problem at week two beats surfacing a 100% certain problem at week six.

**Structure (Calm, factual, options-first):**
- **What happened (one paragraph):** Specific incident or trend. Date, scope, magnitude. "Acceptance rate dropped from 78% to 64% over the last 14 days on the enterprise segment, isolated to queries with >2 entities."
- **What we know vs. what we're still figuring out:** Be honest about the uncertainty. "We've ruled out token cost spike and prompt regression. We're testing whether it correlates with the data refresh on March 12."
- **Impact assessment:** Who is affected. What's the revenue / trust / regulatory exposure. Quantify wherever the data exists.
- **Options table:** Three options minimum. For each: action, cost (time, money, opportunity), upside, downside, confidence.
- **Recommendation:** Which option, why, and what would change your mind.
- **Decision needed by:** A real date, with the cost of waiting longer.

**Length:** 300-500 words. Resist the urge to overpad.

**Anti-patterns:**
- Escalating a problem with no recommended action (managers stop reading after the third "we need to discuss")
- Burying the impact in the third paragraph
- Vague magnitude ("significant impact") instead of "$420K of pipeline at risk"
- Claiming certainty you don't have ("model is broken") instead of "we're 70% confident the regression is in the retrieval layer, not the model"

### 5. Weekly Digest

**When to use:** Recurring cadence (Friday EOD or Monday AM) for a stable audience. The point is not novelty — the point is signal continuity. People should be able to skip three weeks and re-enter at week four without confusion.

**Structure:**
- **TL;DR (3 sentences):** What shipped. What's at risk. What you need from them.
- **Shipped this week:** Specifics with impact. Not "Released v2.4." Instead: "Released v2.4 — confidence calibration improved (overconfidence rate 12% → 6%). No regressions on top-100 queries."
- **In flight:** What's progressing, what's blocked, what changed direction. Owners, ETAs.
- **Eval state (for AI features):** One-line per active model. "Recommendation engine v3.1 — 91% acceptance on heldout, drift watch green, no incidents."
- **Risks (top 3 only):** Age, owner, action. If a risk has been on the list for 3+ weeks with no movement, escalate it inside the digest.
- **Asks (specific):** What you need from each named stakeholder this week.
- **Next week's focus:** What's the one thing that matters.

**Length:** 400 words target. The discipline of keeping it short forces prioritization.

**Anti-patterns:**
- Activity log instead of decision log ("we had three meetings on X")
- Risks aging quietly week after week with no escalation
- "All green" status that's lying — execs lose trust the first time the digest said green and the launch slipped
- AI features without an eval state line (signals the PM isn't watching)

## BEFORE THE MEETING — declare goal, roles, and who can block

Most of this skill is about what you write. This is about the thirty seconds before a conversation starts, and it changes outcomes more than any document does.

**State the goal.** Before anyone discusses the issue, finish this sentence out loud: *"By the end of this conversation, we should..."* Close the same way, explicitly, on next steps, ownership and follow-through.

**Declare the roles.** Do not assume people know how they are expected to participate. Four questions, and the wording is the instrument:

1. "Is everyone expected to contribute ideas, expertise, and perspectives?"
2. "Will the group make a collective decision? If so, who gets a vote, and how will decision making occur?"
3. "Are some people present primarily because they need context to carry decisions forward and implement?"
4. **"Does anyone have the authority to block or override a decision? If so, it's far better to make that explicit at the outset than to surprise the group later."**

**The fourth is the one that changes outcomes.** An undeclared block right is the difference between a decision and an ambush, and the cost of finding out late is a month of rework by people who thought they had agreement. Roles here are not hierarchical: a junior person may facilitate, a subject-matter expert may supply the critical view, and a senior executive may spend the meeting listening.

## SOME CHANNELS FORECLOSE FRAMING BEFORE YOU GET TO USE IT

**The rule:** for any message where the framing matters, and could be lost once the message is read out of context, use a synchronous channel instead of an asynchronous one that will be read without you in the room.

**Why:** email circulates without its author present, and it accretes recipients as it gets forwarded. By the time a new reader sees it, the framing you built in is usually gone. They see the claim, not the conversation that would have surrounded it. A live conversation keeps you there to add nuance, watch the reaction, and adjust before the message locks in. This is why, in one documented case, a communicator handling a sensitive stakeholder socialization chose a live conversation over email on purpose: email would have let the message travel past the room before the framing was set.

**When this is wrong:** most of what this skill covers (the weekly digest, the engineering brief) should stay asynchronous and written, because the record matters more than the framing, and a live conversation would only slow it down. Reach for the synchronous-channel rule only when the content is sensitive enough that a reader who encounters it cold, without you present, would draw the wrong conclusion.

*(Source: HBR, "How a Museum Marketing Team Used AI to Bring People Closer to Art," Jul 2026 — weak evidence, no outcome numbers, cited for mechanism only, ⚠.)*

## THE FAILURE MODE OF A VOLUNTARY INITIATIVE IS SILENCE

**Read this before you write another green status report on anything people opted into.**

When a voluntary program dies, it does not announce itself. In a two-year field study of one failing site, the researchers found the participants *"did not refuse or resist AI. They did not lobby against it. Instead, they simply withdrew."* Nobody sent a memo. Nothing was escalated. No gate was failed. The initiative ran out of participants, and **every status report on the way down looked fine**, because every instrument in a normal reporting pack reads objections and none of them reads absence.

**What to change in your reporting:**

- **Report participation rate as a first-class number**, beside usage and outcomes. It is the only one that moves early.
- **Treat a fall in questions, attendance or volunteered contributions as a finding**, not as the program settling down. Quiet is the symptom.
- **Say plainly when a number is silence-shaped.** "No objections raised" and "no concerns outstanding" are not evidence of health on any voluntary initiative, and writing them as if they were is how a communications pack becomes the thing that hid the problem.

## USE AI FOR THE OUTLINE, NOT THE DRAFT

A specific ordering rule for anything that goes out in your name.

**Once AI writes the first draft, its framing, language and assumptions persist through your edits.** You will edit the words and keep the structure, and the structure is where the position lives. The practical form: **ask for an outline, argue with the outline, then write the prose yourself.** Where you do start from a generated draft, rewrite the opening and the ask from scratch, because those two carry the position.

**Then read it aloud.** If you stumble, lose your breath, or hear a sentence you would never say to the person receiving it, rewrite that sentence. This is the same gate the voice section applies, and it catches AI-shaped prose faster than any checklist.

*(Sources: the goal-roles-block instrument, HBR, "How the Best Leaders Shape Conversations," Aug 2026 — ◆ the authors' own dataset across more than a hundred teams; the four questions are verbatim. The withdrawal finding, HBR, "AI Experiments Need Domain Experts," Aug 2026 — ◆ two-year qualitative field study, two sites, n=2. The outline-not-draft ordering, HBR, Lancefield, Aug 2026 — ⚠ asserted with no evidence and considerable face validity; treat as a working rule, not a finding.)*

## GETTING A BIG IDEA THROUGH: work the restraint, not the push

**The instinct when an idea stalls is to push harder. That is the lever with the worst return.**

An organization sits at equilibrium between forces pushing for a change and forces restraining it. Two ways to move it:

- **Increase the push.** Reliably triggers pushback, because people resist being pressured.
- **Decrease the restraint.** Understand the resistant party's actual position and make the change work for them. **Produces movement with far less backlash.**

**So the question to ask is not "how do I make this more compelling." It is "what is this costing the person who is blocking it, and can I remove that cost."**

### The routing rule, and it is the part most people get wrong

Map three groups: **obvious allies, obvious blockers, fence-sitters.** Then map a second, parallel thing: **the decision-maker, and who *they* personally trust.** Those two maps are different, and the second one is the one that moves outcomes.

**Then: mobilize your allies to influence your fence-sitters to pressure the blockers.**

**Never approach the blocker directly.** A direct approach is pure push, aimed at the person most primed to resist it, and it hardens the position you were trying to move.

**Where this sits against the rest of this skill.** The audience-tier map tells you how to word the message per room. This tells you **which room to be in, and in what order.** A perfectly worded escalation delivered straight to the blocker still loses.

*(Source: Sue Ashford on issue selling, HBR, May 2026, building on Kurt Lewin's force-field model of unfreeze, change, refreeze — ⚠ practitioner-tier. The three-faction map and the routing rule are Ashford's operational addition to Lewin, and the source carries no measured effect sizes.)*

## THE SEVEN SHIFTS FROM RUNNING A FUNCTION TO RUNNING A COMPANY

**Every one of these is a communication change before it is a job change**, which is why they sit in this skill rather than in a leadership one.

| From | To | What changes in how you communicate |
|---|---|---|
| Specialist | Generalist | You stop being the person with the answer and start being the person who can tell whose answer is good |
| Analyst | Integrator | You present a resolution across functions, not the best case from yours |
| Tactician | Strategist | You argue for a direction, not for a next step |
| Bricklayer | Architect | You describe a system, and people have to see it before it exists |
| Problem solver | Agenda setter | **You choose what the room discusses, which is a larger lever than what you say about it** |
| Warrior | Diplomat | You stop winning arguments and start building the coalition that makes the argument unnecessary |
| Unit leader | Enterprise leader | Your audience is people whose incentives you do not control |

**Three forces have compressed the runway for making these shifts**, which is what is new about an old list:

1. **AI has made technology use almost indistinguishable from the work itself**, so technical fluency stopped being a differentiator and stopped being a thing you can defer.
2. **Geopolitical turbulence became a primary focal point** rather than background noise that someone else handled.
3. **Leadership pipelines compressed.** Flatter organizations plus the disappearance of entry-level work mean people arrive at senior roles with less time and less accumulated experience than the previous cohort had.

**The consequence for how Ravi should read a room:** the senior person across the table has probably made fewer of these seven transitions than their title implies, because they got there faster. **A communication pitched at a fully-transitioned enterprise leader will overshoot someone still operating as an integrator**, and the tell is which question they ask first. An integrator asks how the pieces fit. An agenda setter asks why this is the thing we are discussing.

*(Source: Michael Watkins, "The New Rules for Becoming an Enterprise Leader," Jul 2026 — ⚠ framework-tier, an update of his own decade-old model with the three forces as his companion argument. No measured population and no outcome data on people who made the transitions against people who did not. **The seven are a well-worn practitioner model; the three forces are the new part.** Falsifier: a cohort of newly promoted enterprise leaders showing no compression in transition time against an earlier cohort.)*

## CANDOR IS A PAYOFF PROBLEM BEFORE IT IS A CULTURE PROBLEM

**Leaders who say they want candor get silence because they did not change the payoff.** Speaking up costs the speaker privately and benefits the organization publicly. That is individually irrational unless the speaker is rewarded, **and the reward that works is social esteem rather than money.** Naming the person who raised the objection, in front of the people whose opinion they care about, does what a bonus does not.

**Psychological safety is the enabling condition, and it is tactical rather than temperamental.** Two behaviors carry most of it:

1. **Equal conversational turn-taking.** Measurable in a meeting, and the cheapest thing to fix.
2. **Listening that is visibly demonstrated.** Not listening. Listening the room can see: restating the point before responding to it, and attributing it by name.

**One more mechanic that explains a lot of failed candor attempts.** Three kinds of conversation run at work: practical, emotional, and social. **Successful communication requires both people to be having the same kind at the same time.** A report raising a concern emotionally, met with a practical answer, reads the answer as dismissal and stops raising things. Match the kind first, then solve.

**A ritual that structures dissent instead of hoping for it, reported from practice.** Circulate a written memo, read it silently together in the room, and collect objections in writing before anyone speaks. **The silent read is the mechanism**: it removes the first-speaker anchor that otherwise sets the range for every response.

**Then the boundary that makes dissent affordable: disagree and commit.** Two phases with a defined line between them. Argue fully until the decision, then execute it fully whether or not you won. **Without the second phase people withhold the objection to avoid owning the loss.** Without the first, commitment is just compliance.

**The diagnostic:** in your last three decisions, can you name who objected and what happened to them afterward? If you cannot name the objector, you did not get candor. If you can name them and nothing good happened, you will not get it again.

*(Source: Charles Duhigg on the HBR IdeaCast, "Why Your Team Won't Speak Up (And How to Fix It)," Jul 2026, drawing on *Supercommunicators* — ⚠ practitioner account. The three-conversation-types model is credited loosely to neuroscience and psychology with no citation; the turn-taking and listening pair compresses a much larger literature, credited to Google's team-effectiveness work and Amy Edmondson. **One number in the transcript is wrong and is not repeated here:** Duhigg says Amazon has fourteen leadership principles; the published figure is sixteen since 2021, and the principle is "Have Backbone; Disagree and Commit." Falsifier: a team where esteem-based recognition for objectors produced no more dissent than a control.)*

## WHEN REVIEW IS THE BOTTLENECK, MOVE THE JUDGMENT DOWN A LEVEL

**AI collapsed the execution timeline, so the constraint moved from how fast people build to how fast one person can evaluate.** Delegate Monday, review Friday assumed execution took the week. When the work ships the next morning, the manager becomes the queue.

**The instinct is to process the queue faster. That does not work**, because the volume grows with the tool and the reviewer does not. The alternative is to stop being the chokepoint, which means changing what you are responsible for evaluating.

**Four standing questions, answered by the report rather than the manager.** Before anyone gets a project, they should be able to answer:

1. What is the core problem we are solving?
2. What specific change are we driving?
3. How will we measure success?
4. Who owns it?

**The shift is from assigning tasks to naming the destination.** AI executes sequential tasks in minutes, so a task list is a low-value thing to hand over. A mission, a single tracked metric, and a report who can answer those four is a high-value thing to hand over. **This is a communication change before it is a management change:** you are moving from instruction to framing, and framing has to be written down or it does not survive contact with the week.

**Three more moves that each remove you from a chokepoint:**

- **Set the quality standard out loud, once.** "Do not send me something you did not read and edit." That single sentence relocates the first line of defense against low-effort AI output from you to the sender. Unstated, you own it by default.
- **Filter, do not flatten.** Blanket AI summarization treats a careful analysis and a padded deck identically, which is worse than useless because it hides the difference. What helps is targeted signal detection: significant metric moves, threads with unusual comment volume, the same data point recurring across decks. Surface the few items worth deep attention rather than compressing everything equally.
- **Compress the loop, do not lengthen it.** Automate status so the standing meeting is judgment and coaching only. Then shorten the interval. A junior person can now burn real time and money running in the wrong direction between weekly checkpoints, which is an argument for daily contact, not for a longer agenda.

**The relational cost nobody prices.** Faster, denser messaging strips out the recognition and tone that a slower cadence carried implicitly. If you compress the loop and change nothing else, the team reads it as surveillance. Say the recognition explicitly, because it no longer arrives on its own.

*(Source: HBR, "Managers Are Struggling to Keep Up with the AI Productivity Boom," May 2026 — ⚠ practitioner-interview tier across several named companies, plus two secondhand survey citations. No study of the authors' own, and no measured before-and-after on any of the five moves. Carry the diagnosis, which is well argued, and treat the prescriptions as sensible defaults rather than tested ones. Falsifier: a team whose review bottleneck cleared by adding reviewer capacity rather than by relocating judgment.)*

## CLAIM THE MODERATOR SEAT WHEN YOU ARE NOT THE EXPERT

Everything above is about what you say. This is about **which role you take**, and it matters more in rooms where you are outranked on technical depth.

**Three roles people take in a meeting, and only one of them reads as senior:**

| Role | What it optimizes for | What it looks like |
|---|---|---|
| **Low** | being liked and accepted | joking, or taking the menial task (getting coffee, running the deck) |
| **Medium** | adding value | discussing the problem, offering solutions. **This is a perfectly respectable position, not a weak one** |
| **High** | adding value **and directing the flow** | asking what the next question is, soliciting input, synthesizing it, handing the synthesis back |

**The move that changes the room, and it is counterintuitive.** When you are *not* the deepest technical expert present, the instinct is to contribute better content. **Moderate instead.** Ask "what do you think" repeatedly, synthesize what you hear, and give the synthesis back to the group. You are directing attention rather than competing for it.

**Why it works:** the person in the spotlight is not the most powerful person in the room. **The person controlling where the spotlight points is.** Power sits in allocating attention, not in being its object.

**This upgrades what this skill already tells you to do.** Translating for the audience is a medium-status move: valuable, and still reactive. Controlling the agenda is the high-status one. Use the audience-tier map above to decide *what* to say, and this to decide *how to hold the room* while saying it.

**One caution on pairing.** Adding value and asserting yourself have to travel together. Value alone under-signals: hierarchies run on contribution, and people-pleasers still do not end up running them. Assertion alone reads as noise. **The moderator role is the cheapest way to do both at once**, because synthesizing is a contribution and directing is an assertion.

*(Source: Chris Lipp, *The Science of Personal Power*, discussed in HBR, Jun 2026 — ⚠ practitioner-tier, a book-and-interview source with no measured effect sizes attached to the meeting-status model. The moderation tactic is credited there to Maggie Neale at Stanford GSB. Treat the three roles as a usable frame, not a validated taxonomy, and do not attach numbers to it.)*

## AI-NATIVE CONFIDENCE FRAMING

This is the section that separates a PM who can ship AI features in a large industrial enterprise scale from a PM who once wrote a Medium post about LLMs.

### The non-negotiable trio

Every claim about an AI feature in any stakeholder communication carries three things. If any one is missing, the comm is incomplete:

**1. The eval-backed confidence band.** Not "highly accurate." Not even "94% accurate." The right form is: *"91% accuracy on N=400 labeled queries from production sample, March 1-15. Degrades to 78% on long-tail queries (>2 entities, ambiguous intent). Confidence calibration verified — model is not overconfident on errors."*

The shape: number + sample size + segment + methodology + calibration check. Without those five, "94% accuracy" is a marketing slogan, not evidence.

**2. The named drift surface.** Where will this number degrade? When? How fast? What's watching for it? *"Drift watch: daily eval on production sample, alert if accuracy drops >3% week-over-week. Most likely drift cause: shift in query distribution as we onboard the manufacturing segment in Q2."*

If you can't name where the model will degrade, you don't understand the model. If you don't know who's watching, you're not running a production AI feature — you're running a demo.

**3. The "what could be wrong" section.** Mandatory in every AI-feature comm to executives, board, customers above a certain trust threshold, or anywhere the model's claim could be quoted back at you. Format:
- *What is the model wrong about today, that we know?* (Known boundaries.)
- *What might it become wrong about, that we don't yet know?* (Unknown boundaries — open evals, watch list.)
- *What happens when it's wrong?* (Fallback path, human-in-the-loop, escalation rule.)

A PM who omits this section is gambling that the model never fails publicly. The model will fail publicly. When it does, the question is whether you said so before or after.

### Audience-specific framing of the same evidence

Same eval result. Three audiences. Three legitimate framings:

**Engineer hears:** "Production sample N=400, March 1-15, accuracy 91% (CI 88-93%). Long-tail bucket (>2 entities) drops to 78%. Calibration: ECE 0.04, no overconfidence on errors. Drift watch: daily eval, alert at -3pp WoW. Last regression: v2.4 on 2026-03-08, retrieval ranking change, contained in 36 hours."

**Exec hears:** "The model is right 9 out of 10 times on the use cases we shipped for, and we know which 1 of 10 it gets wrong. We watch for degradation daily and we have a rules-based fallback if it ever drops below the threshold. The boundary is queries with more than two entities — for those, we hand off to a human reviewer. Cost trajectory and trust trajectory both holding."

**Customer hears:** "When you ask a question with one or two clear entities, the assistant gives you an answer right away. When the question is more complex or ambiguous, you'll see a 'review with a specialist' option instead of a guess. You can override any answer with one click — your override teaches the system."

Three framings. One eval matrix underneath. The PM who can do this without losing fidelity is a PM you trust to ship.

### Drift watch language — what it actually sounds like

PMs lose credibility when they describe drift as if it's hypothetical. It is not. It is happening to your model right now. The language that signals you know this:

- "The model has been live for 47 days. Acceptance rate has held within a 3pp band. We expect drift when [specific event] — the manufacturing segment onboards in Q2, which will shift query distribution by an estimated 15-20%. We've pre-built a regression test for that distribution and we'll re-baseline after week one of onboarding."
- Not: "We monitor for drift."

### Model-version specificity

Every AI claim names the model version, the prompt version, and the eval date. Without those three, future-you cannot reconstruct what was true when you wrote the claim. *"Recommendation engine v3.1.2, prompt v2.4-prod, evals as of 2026-03-15"* — that's the form. Saying "the model" is how PRDs become unfalsifiable later.

### Eval-backed claims vs hand-waving

| Hand-waving | Eval-backed |
|---|---|
| "The model is highly accurate" | "91% on the heldout set N=400, methodology in [link]" |
| "We've improved performance" | "Acceptance rate up 8pp WoW on the enterprise segment, no regression on consumer" |
| "Hallucination is rare" | "Factual consistency 98.2% on RAG outputs, measured against source docs, N=200" |
| "Latency is good" | "P50 180ms, P95 480ms, P99 1.1s on production traffic, last 7 days" |
| "Users love it" | "Acceptance rate 78% on first-pass output, regeneration rate 7%, feature CSAT 4.4 (n=312)" |

The discipline: never let a hand-waving claim into a stakeholder comm. The first time someone calls you on it, your credibility on every other claim drops.

### Pitching AI governance or safety upward: translate to revenue or loss, not importance

**The rule:** when pitching an AI governance or safety topic upward, translate it into a revenue or loss-exposure number, or name the specific incident it would have prevented. Do not argue that it matters in the abstract.

**Why:** a governance topic earns board-level ownership specifically when it is expressed in revenue impact or tied to an attributable loss event, not because someone argues it is important. Boards fund what has a number attached to it and a name attached to the number. "This could damage trust" competes with every other line item that has a dollar figure next to it; "this is the control that would have stopped the exposure in [named incident type]" does not. It is the same discipline as the eval-backed confidence band above, one level up: instead of anchoring a capability claim to an eval number, you anchor a governance ask to a financial or incident number.

**When this is wrong:** a governance topic with no plausible revenue or loss framing yet (a new regulation with no enforcement history, a novel failure mode with no incident precedent) cannot be forced into this shape without inventing a number that will not survive scrutiny. There, say plainly that the exposure is not yet quantifiable, and ask for a scoping budget to make it quantifiable, rather than fabricate a number that looks eval-backed but is not.

*(Source: the sovereign-AI executive survey in HBR, "What CEOs Need to Know About Sovereign AI," Jul 2026, n=1,928 executives, ◆ single-vendor-commissioned — self-reported and commercially interested, treat the figure as directional; paired with a Corporate Digital Responsibility framework.)*

## REAL-WORLD ENTERPRISE-SCALE EXAMPLES

### Example 1: Shipping an AI feature to skeptical execs

**Context:** A predictive maintenance assistant launching to plant managers. The CFO has historically been skeptical — last AI initiative two years ago overpromised and the model degraded inside six months.

**Wrong move:** Lead with the 92% accuracy number and the demo video.

**Right move (exec summary, 140 words):**

> Predictive maintenance assistant goes GA on April 8. Decision needed: confirmation that the rollout sequence (3 plants → 12 plants → all 47) is acceptable.
>
> The boundary condition: the model achieves 91% precision on the 312 fault patterns we trained on, and falls back to the existing rules engine on patterns it has not seen. Eval matrix and drift dashboard linked below. Watch is daily.
>
> What could be wrong: the manufacturing query distribution differs from the training set; we have a pre-built regression test for that, and the rollout sequence is paced to catch drift inside week one of each new plant.
>
> Cost: $0.12 per assisted decision at current scale, holding under $0.20 at 10x. Trust trajectory: plant managers in pilot accepted 78% of recommendations without modification.
>
> Recommendation: proceed with the staged rollout. Default to rules engine if any plant's acceptance drops below 60% in week one.

Why this works: the CFO's prior bad experience is acknowledged structurally (the model has a known boundary, the watch is real, the fallback is concrete). No "highly accurate." No demo video. A boundary, a fallback, a number with a methodology.

### Example 2: Escalating a model failure to leadership

**Context:** Acceptance rate on the enterprise segment dropped 14 percentage points over two weeks. The cause is unclear. Board update is in nine days.

**Wrong move:** Wait three more days hoping the team finds the root cause.

**Right move (risk escalation, 380 words):**

> **What happened:** Acceptance rate on the recommendation engine dropped from 78% to 64% on the enterprise segment over the last 14 days. Consumer segment unaffected. Confidence calibration unchanged.
>
> **What we know:** The drop correlates with the March 12 data refresh — the catalog grew by 23% with new SKUs that have sparse engagement data. We have ruled out prompt regression (v2.4 unchanged), token cost spike (within 4% of baseline), and infrastructure (latency P95 stable at 480ms).
>
> **What we're still figuring out:** Whether the issue is in the retrieval layer (sparse data → low-quality candidates) or the ranking layer (the model overweights popularity). 70% confident it's retrieval. Test running through Friday.
>
> **Impact:** $420K of enterprise renewal pipeline touches the recommendation surface in Q2. Two enterprise champions have flagged the regression. Board update is on April 4.
>
> **Options:**
>
> | Option | Action | Cost | Upside | Downside | Confidence |
> |---|---|---|---|---|---|
> | A | Roll back catalog refresh until retrieval is fixed | 1 day eng + sales explanation to 40 enterprise accounts | Immediate restore of acceptance rate | Lose 23% of new SKU coverage; sales hates it | High |
> | B | Patch retrieval with a popularity-floor heuristic, ship by Wednesday | 2 days eng | Likely 80% restore by board update | Won't fully recover; partial fix carries forward | Medium-high |
> | C | Wait for full root cause before any fix | 0 immediate cost | Permanent fix the first time | Board update lands during the regression; trust hit larger | Low |
>
> **Recommendation:** Option B. The 80% restore by board update preserves trust while the team finishes root cause for a permanent fix in the next sprint. Would change my mind if Friday's test shows it's actually in the ranking layer — then Option A.
>
> **Decision needed by:** EOD Tuesday. Cost of waiting until Wednesday: ship moves to Friday, board update lands red.

Why this works: a 70% confidence claim is honest, three options force a real decision, the recommendation is named, the kill condition is named. A leader can act on this in five minutes.

### Example 3: Weekly digest when the AI feature regressed

**Context:** The week the recommendation engine started drifting. Same digest cadence as always, but the news is bad.

**Wrong move:** Bury it under the good news. Use vague language. Frame it as "monitoring continues."

**Right move (weekly digest, 350 words):**

> **TL;DR:** Recommendation engine acceptance dropped 14pp on enterprise (Option B patch ships Wednesday). Predictive maintenance pilot expanded to plant 4. Need exec sign-off on the staged rollout sequence by Friday.
>
> **Shipped this week:**
> - Predictive maintenance pilot: plant 4 onboarded, 78% acceptance week 1, no incidents.
> - Vendor risk dashboard: alerting integrated with PagerDuty, deployed to ops.
>
> **In flight:**
> - Recommendation engine — patch v2.4.1 in eng, ship Wednesday, target 80% acceptance restore.
> - Onboarding flow refactor — design review Tuesday, no AI dependencies.
>
> **Eval state:**
> - Recommendation engine v2.4 — 64% acceptance enterprise (down from 78%, 14d trend), drift watch RED, root cause 70% retrieval / 30% ranking, full root cause Friday.
> - Predictive maintenance v1.0 — 78% acceptance plant 4, drift watch GREEN, eval baseline holding.
> - Vendor risk classifier v3.2 — 94% precision holding, drift watch GREEN.
>
> **Risks (top 3):**
> 1. **Recommendation engine regression** — 14d old, owner: me, action: Option B patch ships Wednesday, board update preserved.
> 2. **Plant 4 onboarding window** — 7d to plant 5 cutover, owner: ops lead, action: confirm rollout sequence with VP Ops by Friday.
> 3. **Vendor risk model drift watch instrumentation gap** — 21d old, owner: eng lead, action: escalating into next sprint, drift would surface in eval but not in dashboard.
>
> **Asks:**
> - **CFO:** approve the staged rollout sequence for predictive maintenance (3 → 12 → 47) by Friday.
> - **VP Eng:** review the recommendation engine root cause doc Tuesday before Wednesday ship.
> - **VP Sales:** align on customer comms for the recommendation patch — we have two enterprise champions flagging it.
>
> **Next week's focus:** Recommendation engine restore + predictive maintenance plant 5.

Why this works: the bad news leads. The eval state is specific. The risks are aged and owned. The asks are named. No "monitoring continues." A reader who skipped the last two weeks can re-enter cleanly.

### Example 4: Launch comm when AI confidence is below target

**Context:** A summarization feature is shipping to customers. Eval shows 87% acceptance on the labeled set against an 88% target. The CMO wants to ship for an event next Tuesday. The PM has to decide what to say in the launch announcement.

**Wrong move:** Pretend the gap doesn't exist. Or hold the launch over 1 percentage point.

**Right move (customer-facing launch comm, 220 words):**

> **Tuesday morning. You open a 40-page contract. The summary is at the top.**
>
> Starting today, the assistant generates a draft summary for any document in your workspace. Headlines, parties, dates, obligations, risk flags — surfaced at the top so you can decide where to read closely.
>
> **What it's good at:** Standard contract structures, vendor agreements, NDAs, SOWs. The assistant has been evaluated on 312 documents across these categories with 87% accuracy. We will continue to improve this on the categories you use most.
>
> **What it's not designed for yet:** Multi-party agreements with nested obligations, contracts in languages other than English, and contracts longer than 80 pages. For these, the assistant will offer a "review with a specialist" option instead of a guess.
>
> **What happens when it's wrong:** Every summary line is one-click overridable. Your override is logged and used to improve future summaries. If you see a wrong summary on a high-stakes contract, flag it with the "report" button — these go directly to the team.
>
> **Available now in the document workspace.** Beta label stays until we hit 92% accuracy on the labeled set. We'll let you know when we get there.

Why this works: the 87% number is named. The boundary is named. The fallback is named. The override is named. The "we'll tell you when we hit 92%" line earns trust by setting a transparent quality bar customers can hold the team to. The CMO got a launch on Tuesday. The PM kept the credibility for the next launch.

## QUALITY GATE

Before sending any AI-feature stakeholder communication, the following ten items must all be true. Any "no" sends the comm back for a rewrite.

- [ ] **One audience, one purpose.** This comm is targeted at one audience tier with one decision or awareness purpose, not a hybrid.
- [ ] **The bottom-line fits in the first sentence.** A reader who stops after sentence one knows what's happening and what's being asked.
- [ ] **Every AI claim has a number.** No "highly accurate," no "performing well." Every claim is anchored to an eval number with sample size, segment, methodology.
- [ ] **The boundary condition is stated.** What the model is good at AND what it's not good at, in language the audience can act on.
- [ ] **The drift surface is named.** Where will this number degrade? Who's watching? What triggers escalation?
- [ ] **The "what could be wrong" section exists.** Known boundaries + unknown boundaries + fallback path. Mandatory for exec, board, and external customer comms.
- [ ] **Model and prompt versions are named.** Future-you can reconstruct what was true when this was written.
- [ ] **A specific ask is in the comm.** Either a decision the reader needs to make, or an action they need to take, with a real date.
- [ ] **No banned language.** No "leverage," "robust," "seamless," "transformative," "game-changing," "comprehensive ecosystem." No "in today's fast-paced world." No "it is important to note that."
- [ ] **Reconciliation check.** If the same evidence is being framed for a different audience, the underlying number reconciles. The exec view and the engineering view must point to the same eval matrix.

## DELIVERABLE FORMAT

The skill produces output in the following structure. Always.

```
## [Communication Type]: [Topic]
**Audience:** [Executive / Engineering / Cross-functional / Customer / Board]
**Purpose:** [Decision needed / Awareness / Action required]
**Model and prompt version:** [if AI feature — name them]
**Evidence date:** [date of the eval / metric snapshot underneath the comm]

[Body — formatted per communication type]

---

## Communication Notes
- **Tone:** [chosen tone, why]
- **Boundary condition stated:** [yes/no — if AI feature, must be yes]
- **Drift surface named:** [yes/no — if AI feature with eval claim, must be yes]
- **What-could-be-wrong section:** [included / not applicable, with reason]
- **Sensitivities flagged:** [anything stakeholder-specific to be careful about]
- **Suggested follow-up:** [next comm or action this triggers]
- **Reconciliation:** [if multi-audience, the underlying eval anchor that all versions trace back to]
```

When producing multi-audience comms in the same session, output each variant fully, separated by clear audience labels, and end with the reconciliation note showing the single eval anchor underneath all three.

## RED TEAM

This skill is wrong, or should be bypassed, when:

- **The feature is deterministic.** Rules engine, integration, CRUD launch. Forcing AI-native confidence framing onto a deterministic feature is theater that erodes credibility.
- **You're communicating internal team activity, not stakeholder decisions.** Standup notes, sprint planning, design crit. Use lighter-weight formats — this skill's overhead is wasted.
- **The audience is technically junior in AI but the comm is being treated as introductory training.** A new exec who has never seen a confidence band needs onboarding before this skill helps. Run the explanation conversation first; come back to this skill when they're ready to act on the evidence.
- **The eval evidence does not exist yet.** This skill assumes you have an eval matrix to anchor to. If you don't, you're not ready to communicate — you're ready to build the eval. Use `eval-framework` first.
- **The audience explicitly asked for a casual update.** A peer DM, a "just FYI" Slack note. Forcing the structure into casual comms makes the PM look like they only have one mode.
- **Speed-to-decision dominates polish.** A 2-line slack to unblock something in the next 30 minutes shouldn't go through this skill's structure. Send the 2 lines.

The signal you've over-applied this skill: people start saying "the AI launch comms feel formulaic." That's a real cost. Use the skill where it earns its weight; bypass it where it doesn't.
