---
name: judgment-guard
version: v1.4_latest
description: 'Decide, on purpose, where human judgment sits inside an AI system, because if you don''t, adoption decides for you and the default removes the human. Two cases. ATROPHY: leaning on AI silently fades expert judgment over 6–18 months and stops an organization making new experts; design deliberate friction (rotation, calibration, state-first override, repair, reasoning capture) to keep humans sharp. COMPLEMENTARITY: in regulated, catastrophic-cost work (surgery, aviation, lending) the human stays permanently because human and AI together are more precise and more certain than either alone; design the labor split so each brings its best, the tail not the average setting the floor. Use when deploying high-stakes AI, users stop questioning AI outputs, designing human-in-the-loop for regulated work, or rolling AI into a team of experts. Do NOT use for low-stakes work where full automation is intended. Pairs with: determinism-compass, autonomy-spectrum, trust-ladder, agent-risk.'
imports: []
---

# Judgment Guard

**The objective:** decide, deliberately, which human judgment you keep inside an AI system, how you keep it sharp, and when you fuse human and machine into one permanent joint system — for the leader rolling AI into expert, high-stakes, or regulated work. It turns a decision that adoption otherwise makes for you, by default and always against the human, into one you make on purpose.

## The one idea

**AI doesn't just do the work. It changes what your people become — and if you don't decide the change, the default decides it, and the default removes the human.** There are two versions of this, and a serious system needs both.

**The atrophy case.** Every expert got good the same way: by doing the task, clumsily at first, over and over, until the judgment moved into their hands and became instinct. AI removes exactly that step — it does the reps for them. The work still ships, better and faster by every number on your dashboard, so it *looks* like pure gain. Underneath, the thing that made the expert an expert goes quiet from disuse, and no alarm rings. You find out the day the AI is finally wrong about something that matters, and no one in the room can still tell. The shape worth memorizing: **the cost of AI is paid twice — once, small and visible, when you keep a human sharp on purpose; or later, large and hidden, when you didn't.**

**The complementarity case.** Sometimes you keep the human not because they're fading, but because the human and the machine are each irreplaceable and *together* they are better than either could ever be alone. A surgical robot holds the instrument to a tenth of a millimeter with no tremor; the surgeon reads the bleed the scan never showed and owns the life on the table. Neither alone is tolerable. Together they operate more precisely *and* with more conviction — the surgeon acts decisively *because* the system confirms, and the system is safe *because* the surgeon governs it. Here the human is permanent **by design**, and where a wrong answer is catastrophic and irreversible, no amount of AI maturity changes that.

Same skill, one question underneath both: **which judgment stays human, and how do you engineer that on purpose** — before adoption answers it for you.

## How to use this skill — three questions

1. **Which judgment must stay human?** The stakes and the reversibility of a wrong call decide this. Everything downstream depends on it.
2. **How do you keep that judgment from fading?** → **Case 1 (Atrophy)** below: the seven ways it drains, plus a pre-output failure (drain zero) that precedes them all, and the checkpoints that stop each.
3. **When must the human and AI be fused as one permanent system?** → **Case 2 (Complementarity)** below: the design for high-stakes, regulated work where the combination beats either alone.

Most systems live mostly in one case. Read the diagnosis to find yours; read the design to build it.

## KEY TERMS (plain language)

- **Judgment atrophy** — the slow, silent loss of a person's ability to make a call on their own as they lean on AI.
- **The cost paid twice** — you either pay a small, visible cost to keep a human sharp, or a large, hidden cost later when their judgment has quietly gone.
- **The three clocks** — judgment fades inside one *person* (fast, 6–18 months), inside one *organization* that stops making experts (slow, years), or *down a chain* of AI handoffs where each step trusts the last (sideways).
- **Thinkslop (drain zero)** — the judgment never forms because the thinking collapses before the AI produces anything to react to: lost intent, outsourced thinking, unrecorded reasoning, or sycophantic agreement standing in for real scrutiny.
- **Skill-keeping budget** — deliberately keeping people in some learning-by-doing loops even when automating is cheaper, booked as an investment in future capability, not waste.
- **Offloading vs. chosen blindness** — catching fewer errors because a colleague-like AI made you feel less responsible (offloading), versus knowing it's your call and choosing not to look at the AI's reasoning because looking would cost you (chosen blindness).
- **AI gravity** — the pull toward offloading that gets stronger with every model release: conserving mental energy, competitive pressure to match expert output, and peer AI use that's undetectable, which turns individual restraint into unilateral disarmament.
- **Formative-task test** — a task is formative if you couldn't evaluate the AI's output without having done the work yourself; this corpus's own diagnostic, built on top of the AI-gravity source rather than drawn from it, for deciding when offloading costs a skill you still need.
- **The three-question diff** — after stating your own view, compare it to the AI's along three questions: what did it add, what did it get wrong, and what *looks right but isn't* (the costliest error — plausible, well-structured, wrong in a way only domain knowledge catches).
- **Suppression** — the judgment is formed, correct, and privately stated, and it never survives the room. The only drain where nothing cognitive is missing, and the only one no output metric can see.
- **Terminating condition** — the thing that ends a dispute: either a criterion both sides accepted before it started, or a named person who can call it. Friction with a disputant and no terminating condition produces rework, not decisions.
- **Asymmetric cost** — the arrangement where *not concluding* is more expensive than disputing. Effortful review is not enough; the expense has to sit on silence.
- **Pre-emption** — the judgment is present and correctly aimed and never activates, because a plausible answer arrived before the person built one. The only drain that leaves no override to count and no error to catch.
- **Controlled document** — an AI summary a group reasons from when nobody in the room holds the source. Treat it the way compliance treats any controlled document: versioned, owned by a named person, and issued with a note on what it left out.
- **Second-order candour** — whether a person can say their concern was dismissed, as distinct from whether they can raise one. Two survey items, and the pair separates suppression from an override problem.
- **Stock and flow of judgment** — a stock is the expertise a person already had when the tools arrived; a flow is how a newcomer accumulates it now. Nearly all evidence measures the first and is used to predict the second.
- **Complementarity** — a joint human-AI system deliberately designed so each does what it is irreducibly best at, and the combination beats either alone.
- **Tail risk** — the rare, worst-case outcome; in catastrophic-cost domains it sets the design, not the average performance.
- **Convergence / divergence** — two independent judgments agreeing (the source of the joint system's extra conviction) versus disagreeing (the signal to stop and resolve, never average).
- **Evidence tiers used below** — ✅ audited/peer-reviewed · ◆ company- or study-disclosed · ⚠ reported or practitioner estimate. Numbers marked *illustrative* are teaching devices, not measured facts.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md). At minimum, answer: What expertise is at risk, and what does a wrong call cost — reversibly or not? How will anyone *know* judgment is fading? Then route depth (building a new system vs. auditing one) and output format (Document, Presentation, or Both).

---

## CASE 1 — ATROPHY: when leaning on AI quietly fades the human

### The trap

You will celebrate adoption. The bias is the **success illusion**: automation metrics feel like proof ("90% of tickets auto-routed!") while the real cost is invisible. Expertise doesn't erode visibly — it erodes in six-month increments, and the timeline is predictable:

- **Month 0–3 — Adoption.** People use the AI, catch its misses, learn the edge cases.
- **Month 4–6 — Complacency.** "The AI usually works." Exceptions start sliding through.
- **Month 7–12 — Delegation.** People manage exceptions instead of judging; "the AI said so" becomes authority.
- **Month 13–18 — Dependency.** They can't make the call without it. The expert is now a manager of exceptions, not a practitioner.

**Why it's expensive:** restoring judgment costs two to three times what it took to lose — if the expert hasn't already left, feeling their expertise was devalued. It *feels* like a technology problem (blame the AI) when it's a design problem (you built no checkpoints).

**Why disengagement is rational, not a discipline failure.** An unrefereed theory paper (Gu, Li, Zhu, Carnegie Mellon/HBS, ⚠ theoretical, no data, the authors call for empirical validation) proves formally that once AI alone clears the required performance bar, a rational reviewer optimally lets review effort fall toward zero. That is optimal behavior given the incentives, not negligence. The result is a **dead zone**: the AI is good enough that reviewers rationally disengage but not yet good enough to run alone, and every visible metric (throughput up, override rate down, output quality flat) reads as success, because output quality cannot tell "the model got better" apart from "the reviewers stopped looking"; both produce the same output stream. The only thing that separates the two causes is seeded known-bad cases injected at a known rate, with the catch rate checked against it. See `rtp-production-observability`'s catch-rate instrument for the concrete fix, itself a proposed, untested instrument rather than a validated one.

### Drain zero, and the seven drains (diagnosis)

Judgment doesn't drain one way. Look for each: they run on different clocks and need different fixes.

**Sort them by when they fire.** Drain zero happens *before* the AI produces anything, in how the person frames the problem. The seven numbered drains all fire at or after the model's output. Six of those seven are cognitive. The exception is drain six, suppression, which is social: the judgment forms, it is correct, and it never survives the room.

One note on the numbering, because it is historical rather than chronological. **Drain seven, pre-emption, actually fires earliest of the seven:** a frame arrives before the person builds their own.

**0. Thinkslop — the judgment never forms, because the thinking collapsed before the AI produced anything**
- **How it's different from every drain below:** drains 1 through 7 all fire at or after the AI produces output, whether by reviewing it, deferring to it, or being pre-empted by it. This one fires earlier, in how the person frames the problem before the AI answers at all.
- **Four sub-mechanisms:** losing track of your own intent before you've even formed a prompt; outsourcing the thinking itself, not just the production of the work; no longer writing down your own reasoning at all; and false rigor, where a sycophantic AI's agreement stands in for real scrutiny.
- **The fix:** treat the AI as an intellectual foil to argue with, not a co-author to defer to. This is the same posture checkpoint 3's state-first override enforces downstream, just applied one step earlier, before a prompt exists to state a position against.
- **When this is wrong:** a genuinely open-ended brainstorm has no prior intent to lose track of yet. Thinkslop's diagnostic doesn't apply until the person is expected to have formed one.
*(Source: an annual AI use-case census, 12,637 use cases mined from roughly 50,000 records across six platforms, Jun 2026 — ⚠ social-listening methodology, not a probability sample; it skews toward people motivated to post about their AI use publicly, so treat prevalence claims here as directional, not representative. Names the failure "thinkslop.")*

**1. The fast clock — one person dulls (6–18 months)**
- **Mechanism:** the timeline above. A tool that's 90% accurate teaches people to stop attending to the 10% where it fails; the mind stops working the problem, and the heuristics fade.

**2. The slow clock — the organization stops making experts (years)**
- **Mechanism:** junior staff never build judgment because the AI does the work they'd have learned from; senior expertise fades from disuse.
- **Why it's worse than the fast clock:** invisible until the day you need an expert and discover you stopped making them three years ago.
- **Why it happens — the economics trap:** AI cheapens the part of a job you can *measure* and raises the value of the part you can't, so a firm sheds the unmeasurable half without noticing, booking two liabilities as savings — **capability debt** (cut the seniors who trained juniors) and **judgment debt** (the experts you kept only *review*, so their calibration decays).
- **Why software is worse than the classic radiologist case:** a radiologist's miss is caught same-day; a coding error "looks fine at launch and only surfaces when the system is modified, scaled, or secured" — long after the author has left.
- **The one control that slows both:** a named senior stakes their name on each AI-generated production release *with a junior working under them* — one act that fixes accountability AND is the apprenticeship that keeps the pipeline alive.
- **Formation and retention need different feeds, and confusing them breaks the control above.** Process knowledge, the kind that lives in the hands and between heads, transfers only by observation and compounds through exercise. Doing the work accumulates it. Being handed a decision secondhand does not. That splits into two failure modes with opposite remedies:
  - **Formation** is the junior's problem. It needs juniors watching seniors actually do the work. Not narration, not a workshop.
  - **Retention** is the senior's problem. It needs seniors still producing real work themselves, not only reviewing it.

  A program that keeps seniors "in the loop" as reviewers can lose retention *and* fail formation at the same time. So the named-senior-releases-with-a-junior control above works only if the senior is visibly doing the work the junior watches, rather than signing off on it. *(Source: Dan Wang, HBR IdeaCast, 2026 — process knowledge as the third asset in a three-part anatomy of technology, ⚠ conceptual framework, no measured retention data. When this is wrong: a team whose capability held steady on output-only sign-off with no observed production, over a multi-year window, would break the exercise-fed claim.)*
- **Mentoring needs an artifact from the mentee, not narration from the mentor.** Three July 2026 sources land here. Two ran in the same outlet within a fortnight, so call this corroborated rather than independently replicated.
  - One HBR piece on mentoring in the AI era prescribes narrating a senior's own decisions aloud.
  - A sibling finding contradicts it directly. Senior bankers retained expertise by interrogating juniors' actual production, a real draft, analysis or decision, rather than by narrating their own choices.
  - A Watkins podcast on enterprise leadership arrives at the same word, apprenticeship, for the same mechanism.

  **Why the artifact is the active ingredient.** It gives both parties something concrete to reason over. Narration with no artifact from the mentee leaves the mentor nothing specific to correct, so the exchange defaults to generic principles.

  **A near-free fix:** have the mentee write down what they think the mentor is watching for, before the debrief, then compare. That turns narration into a disputable artifact. *(Falsifier: a cohort whose judgment formed through narrated observation alone, with no production of their own, performing at parity with a producing cohort on an independently scored judgment measure.)*
- **When this is wrong:** the expertise is genuinely being retired — book the loss and move on.
*(Sources: MIT Sloan Management Review, Renieris et al., 12 May 2026 — 84% panel poll ◆, opinion not population survey. HBR, Liu & Kovács, "Big Tech's Looming Capability Crisis," 2 Jun 2026. Radiologist pay ~$570k/2025 ◆; Meta ~8,000 cut redirected to AI ⚠.)*

**3. The relay clock — quality decays down a chain of handoffs (sideways)**
- **Mechanism:** the moment one person stops checking ("the next step is AI anyway"), the next rationally does the same, and fidelity to the original truth drops link by link (Holweg & Davenport call it *knowledge decay*). A hiring pipeline where AI writes the JD, AI screens CVs against it, AI runs the interview against that — four checks meant to catch errors instead multiply their misses.
- **The check:** map a real cross-team process and count AI-mediated handoffs; three or more in a row with no human check on the *original* source is a decay risk.
- **The fix:** you can't police AI use (people hide it) — instead tag the earliest ground-truth artifact (the real transcript, the source doc) as the **provenance of record**, and require every downstream summary to point back to it, so a reader can always return to the truth instead of a summary of a summary.
- **When this is wrong:** a chain that each time *re-anchors* to the same source (a well-built retrieval pipeline) holds fidelity nearly flat — count re-anchored passes as low-risk.
*(Source: HBR, Holweg & Davenport, "Don't Let AI Slop Muck Up Your Company's Processes," 16 Jun 2026. Deloitte Australia's ~AUD 440,000 report with ~20 fabricated references ◆. No measured decay rate given — treat as a mechanism to watch, not a constant.)*

**4. Offloading ownership — the AI feels like a colleague, so the human feels off the hook**
- **Mechanism:** owning an outcome was never something you could hand off; it's a choice a person makes each day, and an AI in the chair quietly removes the three conditions under which they'd choose it.
- **Protect Mindset** ("I matter to this outcome" — naming the AI "Kevin" destroys it). *Break signal:* the owner calls themselves a rubber stamp.
- **Protect Meaning** (a reason worth the effort of checking). *Break signal:* no one can say why careful review matters.
- **Protect Mechanisms** (reviews reward *catching the AI's mistakes*, not just shipping fast). *Break signal:* your routines reward speed of shipping.
- **Why it matters:** a controlled trial (BCG, 1,261 people) found treating the AI as an employee dropped personal accountability ~9 points and led reviewers to catch ~18% fewer errors (⚠/◆) — a disclaimer won't fix a direct hit on whether a human still *chooses* to own the result.
- **Why offloading keeps accelerating, which the treatment above does not explain.** Everything above describes what offloading does to judgment. None of it explains why people choose to offload in the first place. A named account, "AI gravity," gives three drivers:
  - **Energy conservation.** More capable AI amplifies the instinct to conserve mental effort, and that loop strengthens with every model release. So a discipline-based fix has a half-life set by the release schedule, not by willpower.
  - **Competitive and aspirational pressure**, pushing people to mimic expert performance.
  - **Peer AI use is undetectable.** This is the decisive one.

  **Why the third driver defeats exhortation.** If nobody can tell who used AI and everyone is judged on the same output, declining to offload is unilateral disarmament. Every judgment-preservation recommendation then asks one person to accept a worse measured result for a benefit no one can see. **That is why the discipline this skill recommends is widely agreed with and rarely followed.**
- **A practical diagnostic this corpus adds on top of that account, not one the source itself offers: the formative-task test.** A task is formative if you could not evaluate the AI's output without having done the work yourself. Run it before deciding whether to offload a given task, not after. The source offers no falsifier for it, and it has a real limit worth stating: it cannot tell erosion of a capability that still matters apart from supersession of one that doesn't. A skill can atrophy because it's obsolete, not because it's endangered.
- **When this is wrong:** full hand-off is intended and human ownership isn't the goal — skip it.
*(Source: HBR, Okposo, "Accountability Must Be Chosen, Not Mandated," 29 Apr 2026, corroborated by the same BCG trial. AI gravity: MIT Sloan Executive Academy, Jun 2026 — ⚠ mostly argued; its one empirical figure is preliminary, second-hand, and uncited, so treat it as unusable and do not cite it as a number.)*

**5. Chosen blindness — people know it's their call and still choose not to look**
- **How it's different from offloading:** here the reasoning is exactly where the risk to *them* lives, and the pointer runs the other way — not "I feel less responsible" but "looking would cost me."
- **The evidence:** in a study of 2,512 people making real $10,000 loan decisions, 80% wanted the AI's score but only ~46% viewed the reasoning behind it; tying pay to the outcome made them ~20% more likely to skip it; warning them the explanation might reveal bias pushed avoidance up 10+ points.
- **The tell it's avoidance, not fatigue:** skipping is *strongest* exactly where the person is most accountable and most exposed.
- **The fix is different from offloading's:** you can't reassign ownership (they already own it) — you remove the payoff to not-knowing by making the "why" a *mandatory, logged* review before the decision finalizes. "Explanation available" is not evidence anyone looked; log whether it was *opened*.
- **The sharp warning:** a bias-disclosure prompt can *backfire*, triggering avoidance of the very information it meant to surface — pair any bias warning with mandatory engagement.
- **When this is wrong:** in low-stakes, low-exposure contexts the cost that drives avoidance isn't present — don't force review where looking costs the viewer nothing.
*(Source: HBR, Chan / Rand, "Employees Aren't Questioning AI Advice Enough," 24 Jun 2026 — ◆ single study, n=2,512, pre-replication. Regulatory stakes ✅ CFPB circular 2023-03, GDPR / EU AI Act. Note: viewing the explanation raised overrides of both *right and wrong* AI calls, not only wrong ones.)*

**6. Suppression — the judgment is formed, correct, and never reaches the decision**
- **How it's different from every drain above:** nothing cognitive is missing. The person has the judgment, can state it, and states it privately. It does not survive the room.
- **The evidence:** in a study of professional-services executives, each one defended keeping junior training, setting firm-wide AI rules, and rebuilding pricing when interviewed alone. The researchers: "Each of them, individually, knew what AI required of the firm." Collectively they dropped all of it without argument. The cleanest instance is a director who "had just refused, out loud, to lower the firm's day rate" and then, "minutes later and on the anonymous post-deliberation scale," accepted exactly that cut. Same person, same information, minutes apart.
- **Mechanism, and it is a first-mover problem rather than a courage problem:** speaking is costly, silence is free, and it is only worth speaking if others will too. To defend those positions out loud is to push the firm to bill less and to train people rivals can hire away.
- **Why it matters more than its position in this list suggests:** every instrument in this skill reads the visible record: the decision, the review, the override log, the reasoning capture. **If suppression is present, that record is wrong in one direction, toward the comfortable answer, at the altitude where the decisions are largest.** Rotation, calibration and reasoning capture all measure a judgment that was never in doubt.
- **The fix is not exhortation, and it is cheap:** give one named person a professional reason to hold the question open. A formal mandate does not make speaking safe. It makes silence expensive, for exactly one person, whose job description now contains the thing everyone else is avoiding. The article is specific about where that person sits: "the people one level down, the AI-governance leads and practice directors, because they sit close enough to the work to keep the questions concrete." One level down, not the CEO. Proximity supplies concrete questions; the mandate supplies the standing they lack by rank.
- **The detection instrument:** an anonymous pre-and-post scale on the same question the room just discussed. The visible record showed no movement; the administered instrument showed judgments moving a few people at a time. This is the same instrument class as seeded known-bad cases in `rtp-ai-product-metrics`, doing the same job at executive level. **Wherever there is a social cost to a position, the visible record is censored toward the safe answer, and only an instrument administered to the person recovers the rest.**
- **When this is wrong:** where the private and public positions match, there is no suppression and the mandate adds a bottleneck for nothing. Test before installing.
*(Source: HBR, Blangeois & Roulet, "'Leadership Drift' Is Stalling Your AI Strategy," Aug 2026 — ◆ qualitative, one professional-services firm, interviews plus convened workshops. The anonymous-scale gap may in part be an artifact of researcher presence; that would show in any study using the instrument without a convened workshop. Ledger pattern E, fifth mode.)*

**7. Pre-emption — the judgment was never exercised, because a frame arrived before the person built one**
- **How it's different from every drain above:** in drains 1 and 2 the judgment decays or never forms. In 3 it degrades across handoffs. In 4 and 5 it exists and is not applied. In 6 it is applied and is not heard. Here the judgment is present, formed, and correctly aimed, and it **never activates**, because a plausible answer was already on the table before the person produced their own.
- **The worked example:** a business-unit president reads an AI summary of a margin review, and the meeting spends most of its time on supplier costs. He was not confused about margins. He had run that review every quarter for years. The summary was not even wrong; supplier costs were genuinely rising. It arrived first.
- **Why it is invisible in both directions:** nobody notices a judgment that was not exercised, and nobody notices that the answer they accepted is not the answer they would have produced. There is no override to count and no error to catch, which is why the four instruments in this skill that read the visible record cannot see it.
- **The severity does not track the model's error rate. It tracks the size of the room.** The exposure is **the number of people whose only view of the evidence is the summary, times the cost to any one of them of going back to the source.** One person can reopen the spreadsheet. A room of eight cannot reopen it mid-meeting, and will not. This is why a summary that is entirely accurate can still be the most expensive thing in the meeting.
- **The design rule:** a summary read by one person who also holds the source is a productivity gain. The same summary read by a group where nobody holds the source is a **controlled document**, and should be handled like one: versioned, attributed to a named owner, and issued with an explicit note on what it left out. That is drain 3's provenance-of-record treatment applied to a room instead of a chain. Most advice on this tells the individual reader to ask what the summary omitted, which is the right instruction pointed at one person when the problem is the group.
- **Where this bites in an AI product, concretely.** Any feature that produces one synthesized artifact for many readers: meeting-summary agents, RAG-generated executive briefs, LLM narrative layers on a BI dashboard, automated incident timelines, agent run summaries in a review queue. The design tell is a **one-to-many fan-out with no cheap path back to source**. If your summary UI has no per-claim citation the reader can open in one click, you have built the pre-emption condition into the product. See `rtp-ai-ux-patterns` on traceability, which is stage 4 of the sequencing law and is capped by whatever is broken earlier.
- **The fix is ordering, and that is the whole of it:** produce your own diagnosis before the model produces one, then hand the model yours to attack. This is the cheapest repair of the seven drains, because nothing has to be rebuilt.
- **An artifact written before a conclusion attaches can still be neutralized at the moment it's read, if the senior person in the room speaks first.** The room anchors on whoever speaks first, and in AI-assisted review a junior reader now faces two anchors (the senior's view and the model's confident draft) instead of one. The fix is not only "state your own view before the AI's" (checkpoint 3 already covers that); it's sequencing who in the room speaks or writes first: collect the lowest-authority reviewer's independent assessment before the highest-authority view, or the AI's, is visible to them.
- **A companion instrument: the dissent log.** A cheap, optional, timestamped field ("I proceeded and disagreed, because [X]") readable by someone other than the person who overrode the dissent. Keep it optional. Making it mandatory converts an honest empty channel into confident fabricated prose, because a compulsory field gets filled whether or not real review happened, while an optional field's emptiness is itself information. *(Source: HBR IdeaCast, Duhigg, on the Amazon memo ritual, 2026 — ⚠ practitioner account, no measured anchoring rate. Falsifier: a setting with a cheap recorded-dissent channel where reviewers who are accountable but cannot alter outcomes still fabricate justification at the same rate as without one.)*
- **When this is wrong:** where the group has no independent judgment to pre-empt, a shared summary raises the floor rather than lowering the ceiling. Pre-emption is a loss only where someone in the room could have produced a competing read.
*(Source: HBR, Lancefield, "Don't Let AI Flatten Your Leadership Style," Aug 2026 — ⚠ anecdote-tier, four anonymized coaching cases, no comparison group, and the article's one external citation is an unrefereed preprint this corpus has already read at primary and struck. Cite the mechanism, never the claim that AI flattens thinking, which the article does not evidence. The group-scaling rule is this corpus's reading of the case, not the author's; he files it as one leader's judgment going slack. Ledger candidate U.)*

### The six checkpoints (treatment)

Deliberate friction, designed to keep the human sharp rather than to slow the AI down. Choose what the stakes justify; two or three, enforced, beat six that aren't. Checkpoint 6 is the exception and is not a choice: it decides whether the readings from the other five mean anything.

**Before any of that: the substitute test.** A leadership method built to widen perspective can fail its own purpose in one specific way: every parameter of the method (which stakeholders, how long, which view to weight) is itself set by the operator's judgment, so running the remedy presupposes the judgment it claims to replace. A sharper case from the same source: an AI-generated "contrary persona" arguing the dissenting view is a recall exercise, not a discovery exercise. A synthetic persona's objection costs the persona nothing and is drawn from the distribution the prompt-writer already anticipated, so it surfaces only the objection types someone already expected, never the unanticipated class that actually matters. A real dissenting stakeholder's objection is costly: they risk relationship capital, being wrong, being remembered as the pessimist. That cost is what makes the objection informative. So before adopting any proposed judgment substitute, this skill's own checkpoints included, ask whether operating it requires the judgment it's meant to replace. Never treat an AI-generated dissent persona as a substitute for a real, costly, human disagreement; it's coverage of anticipated objections, not a red team. *(Source: HBR IdeaCast, Choe & Goldsmith, 2026 — ⚠ practitioner account, a panoramic-leadership method critiqued on its own terms.)*

**Before you choose one: the three requirements every checkpoint has to meet.** Friction that misses any of them produces activity and no decision, and the corpus has now watched that happen at four separate sites.

1. **An artifact.** Something written down. A held opinion is not a checkpoint.
2. **A disputant who bears a cost.** A second person who reads it, can disagree with it, and pays something for being there. This is why the AI cannot review its own output, and why a self-kept reflective log is a measurement instrument rather than an intervention.
3. **A terminating condition, and this is the one everyone omits.** Either a criterion both parties accepted before the dispute, or a named person who can call it.

**The cost has to be asymmetric, and most designs point it the wrong way.** The requirement is not that reviewing is effortful. It is that **not concluding must be more expensive than disputing.** An executive committee with maximum dispute capability, shared technical credibility and no one able to shut a question down argued genuinely and reached no decision. A workshop where a team read its own productivity data recognised what it implied and "asked for time to make sense of it." Both had artifact, disputant and cost. Neither had a terminating condition, and both produced rework instead of a call.

**Why exhortation-shaped checkpoints decay, and what to do instead.** Telling one person to think harder is asking them to be slower than their peers for no measurable quality gain, which is unilateral disarmament in a game where everyone is scored. Two interventions in the corpus change the payoff rather than the appeal, and both work:

- **Remove the scoring inside a bounded venue.** A divisional CEO brought his peer group to external advisory sessions "simply to be rigorously challenged where no one was scoring them." The sessions "became a training ground rather than a performance arena."
- **Make silence expensive for one named person.** See drain 6 above. This is the same move at organisational scale, and it is the only kind that survives a first-mover problem.

**Protect production asymmetrically, not uniformly.** This skill's premise is that judgment is a byproduct of producing the work, so the reflex is to protect all production. Two capacities are in play and they behave differently: **breadth of perception**, noticing weak signals and adjacent patterns, and **independence of interpretation**, forming your own view rather than deferring. A professional's frame is a liability in search and an asset in evaluation. It narrows what you find, and it is the only thing that says which finding matters. **So guard the production that forms evaluation judgment and let exhaustive search go.** A junior who never learns to comb a data set by hand loses less than a junior who never learns to decide which of three surfaced patterns is worth the partner's time. Untested: a cohort whose evaluation judgment degraded after search was automated, holding evaluation practice constant, would show the two capacities are not separable and blanket protection is right.

*(Sources for this block: HBR, Sudakov & Furr, Aug 2026 (RED method, advisory networks, the two-capacity split); HBR, Blangeois & Roulet, Aug 2026 (the executive committee, the workshops, the mandate); MIT SMR, Sloan & Glaser, "Stop Prompting AI. Start Directing It," Aug 2026 (frame as liability in search, asset in evaluation). Ledger patterns Q, O and E.)*

**1. Rotation — keep two decision pathways alive**
- **The practice:** no one uses the same AI tool for more than ~80% of their decisions for more than four weeks straight. A radiologist reads some scans unassisted, some with AI, some as peer reviewer of the AI's reads — rotate every four weeks, not daily (that's chaos).
- **Red flag:** "we can't rotate, they're too busy" — the AI has reached 100% dependency; fix that first.

**2. Calibration — measure the human against ground truth**
- **The practice:** monthly, give the team 10–20 cases where you already know the answer. Human judges blind (no AI answer first, to avoid anchoring), AI judges, reality shows who was right.
- **Red flag:** after six months, human accuracy is flat while AI accuracy improves — that gap is erosion.

**3. Override — its sharpest form is stating your call first, at the right frequency and depth**
- **The practice:** the strongest version of a human review is not "approve unless something looks off" — it's stating your own view *before* you see the AI's, so there is something real to compare against.
- **Mechanism:** gate the AI's output behind a required, timestamped "here's what I think and why" field — a stated position, not a click-through. A click without a prior stance is exactly the theater mandatory review decays into, and it defeats chosen blindness by removing the ability to stay uncommitted.
- **How often it fires, not just what it asks: fewer, well-placed checkpoints can beat many shallow ones.** Where tasks split cleanly into AI-suitable and not, group the AI-suitable ones and remove the repeated per-task handback instead of routing each one back to a human individually. Each handoff is itself a failure surface: a reviewer facing ten small handbacks in a row reviews all ten shallowly, while one well-placed checkpoint covering the batch gets reviewed at real depth. Set this checkpoint's frequency by that trade-off, not by a default of reviewing everything or reviewing nothing.
- **What the checkpoint should ask, restated:** the standard content of a state-first checkpoint should be "why are you following this recommendation," not "do you agree with it." In one internal banking pilot (population unspecified), requiring that written reason before acting measurably reduced uncritical reliance on the AI's recommendation and improved decision accuracy, with no measured cost in time. This is the same "here's what I think and why" field above; the finding is that the why is doing the work, not the field's mere presence.
- **The caution this pairs with, and it matters more than the finding above:** a checkpoint that reduces uncritical reliance cannot currently be told apart from one that simply makes people reject more, including AI outputs that were correct. Track both sides: catch rate on seeded known-bad cases (already this skill's fix for the dead zone under "The trap") and false-rejection rate on seeded known-good cases. The two failure modes diverge further as the underlying model improves, so a checkpoint design's apparent success has a shelf life that can expire without warning. *Falsifier:* a deployment that tracked both catch rate and false-rejection rate over time and saw both stay stable would show that a given checkpoint design is not decaying this way.
- **Then run the three-question diff:** what did the AI add that you missed; what did it get wrong; and — ranked highest, because it's the costliest — what *looks right but isn't* (plausible, well-structured output resting on a wrong assumption, the error only domain judgment catches).
- **Red flag:** override rate under ~1% — either the AI is perfect (unlikely) or no one is engaging. The rate alone can't tell you which; a falling override rate looks identical whether the model improved or the reviewers quietly stopped looking (see the dead-zone note under "The trap"). Only a seeded-case catch rate, via `rtp-production-observability`, distinguishes rational disengagement from erosion. A rate that looks too high has the same blind spot in reverse: it can mean sharper catching, or it can mean the checkpoint now rejects good AI output along with bad. Read the override rate against a false-rejection rate measured on seeded known-good cases, not against the raw rate alone.
*(State-first + the three-question diff and "looks right but isn't" as top severity: HBR, Duncan & Anderson, "Help Employees Get Better, Not Just Faster, with AI," 15 Jun 2026 — conceptual, built on the Dreyfus and Polanyi tradition; the "jagged frontier" calibration idea is ✅ Dell'Acqua/Mollick et al., HBS 24-013. The article's own 90%/10% and two-weeks-to-an-hour figures are ⚠ illustrative. Checkpoint frequency and the "why" standard: MIT Sloan Management Review, 2026 — two practitioner findings, both ⚠ and neither settled: the frequency finding names no model, prompt, or reviewer population; the "why" finding is described in its own source as an ongoing, unpublished internal pilot.)*

**4. Repair after a miss — before you re-engineer the process**
- **The practice:** when an AI-assisted call goes wrong, the reflex is to fix the process. Do the *social* repair first, or the fix lands structurally sound and socially inert.
- **Mechanism:** run an explicit reconciliation — both parties state what they could have done differently — opened with normalization ("there can be multiple good decisions; a call can be reasonable and still be beaten by how events unfold") so it doesn't collapse into blame. *Then* ask the process question — "*why* did this happen," not "what happened" — and change the system so the failure can't recur.
- **Why it matters:** this protects the Mindset condition from drain 4 — skip it, and the person you most need to keep owning the outcome quietly stops.
- **When this is wrong:** where psychological safety is genuinely absent, the "what could I have done differently" confession can be weaponized — fix the safety first, or the repair backfires.
*(Source: HBR, McCall, Wolfberg, Bilsborough, Pruna, "How Elite Sports Coaches Make High-Pressure Decisions," Jul–Aug 2026 — ⚠ anecdote-tier, 11 coaches, no numbers; cite the mechanic, not the quotes.)*

**5. Reasoning documentation — capture the why, not just the decision**
- **The practice:** "I decided [X] because [signals]; I ignored [Y] because [reason]; I'd change my mind if [condition]." Make capture automatic (a prompt after the decision, not extra work).
- **Cadence:** review monthly for patterns; quarterly, look for reasoning that has *disappeared* ("six months ago people flagged X; nobody mentions it now").
- **Red flag:** reasoning drops in complexity over time — "AI seems good" — that's the signal, in the person's own words.

**6. Disclosure safety — the checkpoint that decides whether the other five are measuring anything**
- **The problem it solves:** checkpoints 1 to 5 all read a record a person chooses to produce. An override, a stated prior view, a documented reason, a flagged near-miss. Drain 6 established that the record is censored wherever holding a position has a social cost. This is the treatment side of that finding, and it has to be installed before the other five are trusted, not after.
- **The mechanism, and it comes from outside AI entirely:** people break a rule for four separable reasons. **Self-interested** (to benefit themselves), **prosocial** (to help a customer or colleague), **corrupted** (under situational pressure), **edified** (because they believed breaking it was right). Two questions sort them: was the behavior constructive or destructive, and was it driven by individual choice or by the situation.
- **The error that destroys your data:** responding to all four with the same instrument, which is usually punishment. Punish prosocial or edified rule breaking and people stop exercising judgment, or they keep exercising it and stop telling you. Either way the early-warning signal disappears while the compliance numbers improve.
- **What that means here, concretely:** if someone logged an override that turned out wrong, would they expect curiosity or consequences? If consequences, your override rate is already false and checkpoints 1, 3 and 5 are reporting on a filtered population. The red flag in checkpoint 3 (override rate under ~1%) has two causes, and this is the second one.
- **The detection instrument costs two survey items.** First-order candour asks whether a person can raise a concern. **Second-order candour asks whether they can say their concern was dismissed.** Score both:

| | High second-order | Low second-order |
|---|---|---|
| **High first-order** | working team; the record is usable | **people can speak, and then get overruled with no way to say so.** This is the dangerous cell, because it reports as a healthy engagement score |
| **Low first-order** | rare, probably a measurement artifact | suppression (drain 6); the one-named-person mandate applies |

- **One bound on the trust question you are probably already asking.** A trust item phrased about colleagues measures something held one relationship at a time. What this checkpoint needs is whether someone will say the hard thing in the room where the decision happens, which is a property of the group. Phrase it group-referenced or the instrument returns high trust for a team that cannot speak, which is the exact false negative it exists to catch.
- **When this is wrong:** regulatory and legal violations take a hard line regardless of intent, and triaging them by motive is how a compliance failure becomes a coaching conversation. Run the four-type sort on everything else.
*(Sources: Gill, "Rule Breaking in Organizations: An Integrative Review," Academy of Management Annals 2026, DOI 10.5465/annals.2023.0170 — ✅ integrative review of 250+ studies across four decades; HBR's treatment of it, Aug 2026, for the five-step protocol and the Delinea practitioner rule. ECI 2023 Global Business Ethics Survey, >70,000 employees across 42 countries: 65% of employees report having observed misconduct, up from 60% in 2020 ⚠ single-source. The second-order candour item: HBR, "How the Best Leaders Shape Conversations," Aug 2026 — ◆ the authors scored it across more than a hundred teams and reported only its rank, so the two-by-two above is this corpus's construction and has not been tested as a two-by-two.)*

---

## CASE 2 — COMPLEMENTARITY: when the human stays because human + AI together beat either alone

Case 1 keeps a human sharp against a fading default. Case 2 is the opposite starting point: in a regulated or catastrophic-cost domain, the human is *permanent by design*, and the goal is to fuse human and AI so the combination is more precise **and** more certain than either alone. The neurosurgeon-plus-robot is the clean picture — the robot's tremor-free precision, the surgeon's judgment on the bleed the scan never showed, and an outcome someone is accountable for. Here is how to design it.

### The Complementarity Design — four moves

**1. Split by irreducible strength**
- **The move:** list the task's sub-decisions and give each to whoever cannot lose it. *AI:* precision, consistency, recall across millions of cases, no fatigue. *Human:* the novel situation, the context no data held, the call someone must answer for. Give the robot the tremor-free motion; give the surgeon the bleed and the accountability.
- **Why:** a joint system is only as strong as the fit between the split and each party's true edge — mismatch the split and you get the weaknesses of both.

**2. Set the floor by the tail, not the average**
- **The move:** where the 0.1% is a dead patient or an unlawful denial, "the AI is more accurate on average" is the *wrong number* — you design for the worst plausible case.
- **Why this is precisely why mature AI does not remove the human here:** the tail, not the mean, sets the design, and the human is the tail's last defense.
- **When this is wrong:** where errors are cheap and reversible, designing for the tail is over-engineering — that's a Case 1 or a full-automation problem, not this one.

**3. Make convergence your conviction, divergence a full stop**
- **The move:** two independent judgments agreeing is *why* the joint call carries more conviction than either alone — the surgeon acts more decisively because the system confirms. When they disagree, that is the alarm: stop and resolve it, **never average it**.
- **Why:** averaging two judgments that disagree hides the very signal the joint system exists to surface, and manufactures false confidence in the middle.

**4. Keep the human's hands on the hard part, not just their eyes on the screen**
- **The move:** assign the permanent human the sub-decision that keeps their judgment live — not the rubber-stamp seat.
- **Why:** this is where the two cases fuse — a permanent human who only *watches* still atrophies (Case 1), so the atrophy checkpoints *serve* the complementarity design; oversight-by-watching decays into rubber-stamping within months, oversight-by-doing-the-hard-part stays calibrated.

**The regulated-domain rule, stated plainly:** where a wrong answer is catastrophic *and* irreversible *and* someone must be legally accountable, keep the human in the loop regardless of AI maturity — and still keep them few and elite, because scarcity is not the enemy here; a dull majority is. Complementarity is not a compromise between human and machine. It is a multiplier — done right, the pair is safer *and* more decisive than the sum.

---

## WHERE THIS MEETS YOUR STACK

Judgment-guard owns one seat: which judgment stays human, how you keep it sharp (Case 1), and how you fuse it with the machine when the stakes demand both (Case 2). It has no imports — every companion below is a hand-off, not an input.

**Hands off to, to build the rest of the joint system:**
- `determinism-compass` — which parts must be rule-bound and reproducible vs. which can tolerate the model's variance. Decide this *before* you split the labor in Case 2.
- `autonomy-spectrum` — who holds the decision at each step. In Case 2 the human keeps the final call by design; this skill sets where on the spectrum the rest of the system sits.
- `trust-ladder` — how far to trust the AI's half, calibrated, and how trust is repaired after a miss (the calibrated mirror of Checkpoint 4).
- `agent-risk` — proportionality and the kill-switch when the cost of a wrong call is catastrophic (Case 2's tail is agent-risk's home ground).
- `safety-by-design` — encode the constraints into the system so the joint pair can't be driven outside them.
- `stress-test` — its human gate ("will anyone say it fails?") is a worked instance of this skill's checkpoint pattern, applied to one specific moment: the pre-launch kill decision. Reuse the state-first-override and reward-the-honesty machinery there instead of re-deriving it from scratch.

**Acts on this skill's decision, one hop downstream:**
- `agent-spec` — takes "this judgment stays human" and encodes it as an actual autonomy level and confidence threshold in the technical spec; without that translation, the decision stays a slide, not a system.
- `stakeholder-communications` — carries the "why a human stays in the loop here" case to a board or regulator who will ask for the efficiency number this design deliberately doesn't optimize for.
- `needs-guard` — when the REALITY CHECK below's "some people resent checkpoints" risk materializes into real resistance, that's a need-violation to diagnose, not a training problem to push through.

**Arbitrates when this skill disagrees with a pure efficiency recommendation:**
- If `autonomy-spectrum` or `agent-spec` would otherwise push toward a higher autonomy level for speed or cost, and this skill's Case 2 test says the domain is regulated and catastrophic-cost, **judgment-guard's human-stays-in-the-loop call overrides the efficiency recommendation.** Run judgment-guard first in any domain where the two could conflict, not after.

## REALITY CHECK

- **The failure mode of this skill:** checkpoints without enforcement. "We require override documentation" that no one enforces is theater. Non-negotiable, or nothing.
- **The most expensive mistake:** waiting 12 months to check. Start monitoring at month 1 — by month 12 the judgment is already hard to restore.
- **The social cost:** some people resent checkpoints ("I know my job"). Frame as "we're protecting your expertise," not "we're watching you."
- **The honest inversion:** if the AI is genuinely better than the human on the *average* case and the tail is cheap, maintaining independent human judgment can create harm — then you're building oversight, not restoring judgment (and you may be in Case 2's opposite: full automation with a human only on the tail).

## QUALITY GATE

- [ ] Which judgment must stay human is decided, and *why* (stakes × reversibility), before anything else
- [ ] The case is named: atrophy (Case 1), complementarity (Case 2), or a mix — and the design matches
- [ ] Case 1: the specific drain(s) identified among the seven numbered drains, or drain zero if the failure preceded any AI output, and checkpoints chosen to match (not a generic "add friction")
- [ ] Case 1: at least the state-first override (checkpoint 3) and the repair-after-a-miss step (checkpoint 4) are present for high-stakes work
- [ ] Case 2: the labor split is by irreducible strength, the floor is set by the tail, and divergence triggers a stop
- [ ] Every checkpoint has an owner, a cadence, and a red-flag threshold; enforcement is named
- [ ] Hand-offs to the companion skills (determinism-compass, autonomy-spectrum, trust-ladder, agent-risk, safety-by-design, agent-spec) are named where the design needs them

## DIAGNOSTIC QUESTIONS

1. **When did someone last override the AI?** "Can't remember / >6 months" → eroding. "This week" → still engaged.
2. **If the AI vanished tomorrow, could this person do the job at 70%?** "No, they'd be lost" is a red flag; "slower, but they know the fundamentals" is green.
3. **What's the most recent edge case this person caught that the AI missed?** A blank stare is the signal.
4. **Has their accuracy moved against the AI's over six months?** Diverging (human flat, AI rising) is erosion.
5. **(Case 2)** When human and AI disagree, does the system *stop* — or does it quietly average them into a confident middle?
6. **If someone logged an override that turned out badly, would they expect curiosity or consequences?** "Consequences" means the override rate you are reading is already filtered, and checkpoints 1, 3 and 5 are reporting on a censored population. Fix checkpoint 6 before you trust any of the others.
7. **In your last consequential meeting, how many people in the room had read the source rather than the summary?** Zero or one is the pre-emption condition, and the cost of reframing scales with everyone else in the room.

## OUTPUT FORMAT

```
## Judgment Design: [Role / Decision Type]

**Which judgment stays human, and why:** [the sub-decisions, tied to stakes × reversibility]
**Case:** [Atrophy / Complementarity / mixed] — [one line on why]

**Case 1 — if atrophy applies**
- Drain(s) present: [which of the seven, or drain zero]
- Timeline of concern: [erodes in X–Y months here]
- Checkpoints (owner · cadence · red flag):
  1. Rotation — … 2. Calibration — … 3. State-first override — … 4. Repair-after-a-miss — … 5. Reasoning capture — …

**Case 2 — if complementarity applies**
- Labor split (by irreducible strength): AI does […]; human does […]
- Tail the design must survive: [worst plausible case]
- Convergence/divergence rule: [what happens when they disagree]
- Which sub-decision keeps the human's hands (not just eyes) in it: […]

**Hand-offs to the stack:** [determinism-compass / autonomy-spectrum / trust-ladder / agent-risk / safety-by-design / agent-spec — where each is needed]

**Monitoring:**
| Metric | Baseline | Green | Red | Frequency |
|---|---|---|---|---|
| Override rate | | >Y% | <Z% | Weekly |
| Calibration accuracy | | stable | drops 5%+ | Monthly |
| Reasoning complexity | | stable | drops 30%+ | Monthly |
| (Case 2) divergence-resolved rate | | 100% stopped | any averaged | Per incident |
```

## WHEN WRONG

- Low-stakes, high-frequency decisions where efficiency is the goal and judgment isn't critical.
- The organization has deliberately chosen full delegation and the human isn't meant to own the output.
- The human's prior judgment is genuinely biased and the AI is better on a tail that's cheap — build oversight, not restored judgment.
- The timeline is so short (a six-week project) that judgment maintenance is premature.
- **The organization is centered on friction erasure, and this is the exclusion most likely to be applied wrongly.** A company whose organizing principle is removing friction for the customer will read every checkpoint here as waste, and it will be right about some of them.

  **Sort the friction before you argue:**
  - **Erasing customer friction is on-strategy.** This skill has no claim on it.
  - **Erasing reviewer friction is a different act wearing the same word.** The stakes test still governs it.

  A firm that cannot tell the two apart will automate its own review under the banner of its strategy, and record it as consistency. *(Source: HBR, McGrath, "The Power of Strategic Centering," Aug 2026 — ⚠ framework-tier, five center types, no outcome data. The friction-erasure trap is this corpus's inference from her taxonomy, not her finding.)*

**One caution about the whole evidence base, and it applies to this skill more than to any other in the library.** Almost every measured finding about AI and expertise, including the ones cited above, was taken on people whose expertise formed *before* AI, and then reported as a property of the technology. Nobody has measured a cohort whose expertise formed under AI assistance from the start. **So the drains describe what AI does to a stock of judgment, and this skill is routinely used to predict what it does to the flow.** Those are different claims. Treat the seven drains as well-evidenced on incumbents and as a hypothesis on anyone who joined after the tools arrived, and say which population you are reasoning about before you prescribe.

The same error appears in the prescriptions. Two 2026 articles, in two journals, two weeks apart, both instruct professionals to exercise a judgment capacity while neither explains how a newcomer accumulates it. One of them describes the capacity as something that "has always distinguished exceptional professionals," which is the assumption stated out loud. *(Ledger pattern P. See `rtp-capability-tracking` for the workforce-level version.)*

**Three challenges to this skill's central premise, all live, none settled.** The premise is that judgment is a byproduct of producing the work. Carry these openly rather than defending the premise, because a claim that cannot lose is not doing any work.

**One: the premise is role-relative, and a single deployment can move two people in opposite directions.** An ambient clinical scribe at Mass General Brigham drafts the visit note. The attending stops producing it, so atrophy applies, and the recognition failure is already audible in what they say: "when I read this note, this is not how I would write the note." The resident standing in the same room now hears reasoning that used to happen silently, because the tool requires the clinician to speak it. Non-formation runs backwards for them. **So the premise is production-fed for the person who was producing and observation-fed for the person who was watching, and you have to say which role you are reasoning about before you prescribe anything.** Two consequences. The reviewer who no longer recognizes the output as something they would have written has lost the fastest error signal they had, which is a red flag for checkpoint 3 in the reviewer's own words. And the trainee question ("do we train residents on AI or keep them AI-independent") is probably the wrong variable; whether the senior is now speaking their reasoning where the junior can hear it looks more consequential than either option. *(Source: an MGB deployment discussed in HBR, Aug 2026 — ◆ practitioner interview, roughly 800 self-selected clinicians in the pilot, no controlled comparison. The role-relative restriction is this corpus's reading.)*

**Two: interrogation may preserve judgment, and if it does, the premise's central term is wrong.** One 2026 prescription states the substitution as a goal: "Experts stop being reviewers who inspect output case by case and become teachers who set the unwritten rules once." Read through this skill, that is a designed-in loss. Read the other way, it is the strongest counter-argument in the corpus, because **an expert answering one targeted question per exception is engaged only with the boundary cases, which is where judgment is worked hardest.** The interrogation regime concentrates whatever production the expert has left onto exactly the material the premise says forms judgment. That runs at the premise rather than around it. The study that settles it is ordinary and nobody has run it: does an expert who answers a hundred exception questions a year retain the judgment that made the early answers good? Until someone does, treat a move from reviewing to rule-setting as unresolved rather than as a loss you have already priced. *(Source: HBR, "4 Steps to Transform the 'Middle Office' with AI," Aug 2026 — ⚠ the article asserts that interrogation preserves expertise and demonstrates nothing. Ledger pattern E, fifth falsifier firing.)*

**Three: a controlled comparison against an AI-only baseline finds a failure this skill has no name for.** A KPMG/UT Austin field study split 523 early-career staff against an AI-only baseline (n=523, ◆ single-site, unpublished) and found three profiles, not the two this skill's language expects. **AI apprentices** (24.1%) had high measured skill and were actively engaged, and still finished below the baseline: engaged, skilled, and net value-destroying. **AI delegators** (25.8%) had the lowest skill and the least engagement, and matched the baseline anyway, which is invisible underperformance no dashboard catches. **AI amplifiers** (50.1%) beat the baseline not on higher skill but on sequence: they set their evaluation criteria before seeing the model's output, where apprentices reacted to the output after it appeared, carrying a producing reflex, rewriting and reorganizing, into what should have been a directing role. Foundational skills (critical thinking, domain knowledge, AI literacy) did not separate the three groups; sequence did. **Call this misapplication: judgment formed by producing does not automatically transfer to directing and reviewing.** It's a third failure mode, distinct from atrophy (fading judgment) and non-formation (judgment that never built), and it's a role-relative failure this skill's checkpoints were not built to catch. The fix is cheap: require the evaluation criteria in writing before the AI's output is visible, converting the producing reflex into a directing discipline, a one-line extension of checkpoint 3's state-first override aimed at a failure this section had not named. *(Source: KPMG/UT Austin field study, n=523, ◆ single-site, unpublished — strong but unreplicated. Falsifier: a longitudinal study showing unassisted and AI-assisted judgment scores correlate strongly across a real population would undercut misapplication as a distinct failure mode from atrophy.)*

---

## TRADE-OFF LEDGER

- **The bet:** by designing judgment on purpose, you're betting this expertise is valuable and — in Case 2 — irreplaceable.
- **What you give up:** ~10% of human time to checkpoints, and in Case 2 you refuse the cheaper fully-automated path.
- **Reversible?** Barely. Judgment lost over 18 months takes 9–15 to rebuild — a one-way door.
- **The hidden trade:** you're choosing sustained capability and decisive, accountable decisions over the next 24 months, not the fastest possible decision this month.
- **Confidence: High. What would change it:** the expertise is being retired (Case 1 moot), or the AI has proven itself on a tail that's cheap and reversible (build oversight differently).

## CONCLUSION

Follow the Conclusion Protocol (Universal Skill Protocol, Section 6): state the recommendation (which judgment stays human, which case, which checkpoints or which labor split), name the key trade-off (efficiency vs. sustained, accountable judgment), acknowledge the biggest risk (checkpoints unenforced, or a labor split that mismatches each party's real edge), and define the next action (owner of monitoring, first checkpoint or first convergence-review date).

---

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual. Show the atrophy timeline (drain zero before month 0, then month 0–18) with the six checkpoints placed on it, beside the Case 2 panel showing the labor split (AI precision × human judgment), the tail-set floor, and the convergence-or-stop rule, so a viewer sees both halves of the one idea at a glance. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
