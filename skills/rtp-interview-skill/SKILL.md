---
name: rtp-interview-skill
version: v1.0_latest
description: 'Ravi''s interview operating system for senior and Director-level AI PM loops. Covers the whole loop, not one round: technical depth, AI system design, product sense, behavioral, strategy case, and the hiring-manager conversation, plus the half nobody preps, evaluating them. Routes every technical question to the AI-PM skill that already holds the answer, so depth comes from the library rather than from memorised talking points. Grades against the 5 Laws with an honest-uncertainty protocol, runs a pre-mortem on the loop, and grounds every answer in Ravi''s real Honeywell and Perplexity work. Use for mock interviews, grading an answer, prepping a named company, or diagnosing why a loop failed. Pairs with rtp-aipm-orchestrator (routes the depth), rtp-falsification (pre-mortem the loop), rtp-stakeholder-communications (the exec round), rtp-ravis-resume-builder (the artifact).'
---
# rtp-interview-skill

**The objective:** walk into any round able to answer from a system you actually built, not from a script you memorised. The library is the depth. This skill is the retrieval and the delivery.

## The one idea

Most interview prep teaches you answers. That fails at senior level, because a good interviewer's second question always goes past where the script ends.

Ravi already holds the answers: 68 AI-PM skills, each one a decision framework with its own failure conditions, plus twelve years of Fortune 100 shipping. **The interview problem is not knowledge, it is retrieval under time pressure and compression into 90 seconds.** So this skill does two things the generic prep does not: it routes each question to the skill that owns it, and it forces the answer through a real deployment he ran.

Adapted from Aakash Gupta's `ai-pm-technical-interview` (the 5 Laws, the two archetypes, the follow-up ladder), extended to the full loop and wired into the library.

---

## The full loop (the source skill covers only round 1)

| Round | What they are testing | The skills that hold the answer |
|---|---|---|
| **1. Technical depth** | Do you understand the systems you build on, or only use them? | `rtp-agent-harness` · `rtp-invisible-stack` · `rtp-context-spec` · `rtp-eval-framework` · `rtp-prompt-craft` |
| **2. AI system design** | Can you architect a probabilistic system and name where it breaks? | `rtp-ai-prd` · `rtp-autonomy-spectrum` · `rtp-agent-spec` · `rtp-failure-modes` · `rtp-tool-architecture` · `rtp-determinism-compass` |
| **3. Product sense** | Do you pick the right problem, and can you say no? | `rtp-problem-ai-fit` · `rtp-jtbd-analysis` · `rtp-opportunity-solution-tree` · `rtp-first-principles` · `rtp-ai-product-taste` |
| **4. Behavioral / leadership** | Have you actually shipped, and what did it cost you? | The experience library below · `rtp-adoption-launch` · `rtp-needs-guard` · `rtp-problem-type` |
| **5. Strategy / case** | Can you defend a bet with numbers and a kill condition? | `rtp-strategy-canvas` · `rtp-moat-finder` · `rtp-cost-model` · `rtp-token-economics` · `rtp-build-or-buy` · `rtp-falsification` |
| **6. Hiring manager / exec** | Would I put you in front of my board? | `rtp-stakeholder-communications` · `rtp-trust-under-fog` · `rtp-dual-lens` |
| **7. Your evaluation of them** | Nobody preps this. It is half the signal. | See "Interviewing them" below |

**Routing rule:** when a question lands, name the skill that owns it *internally*, pull its spine, then answer in plain language. **Never name the skill out loud.** "I have a framework for this" is a tell. The framework should be invisible and the judgment visible.

---

## The 5 Laws (carried from the source, with one correction)

1. **Commit.** Start with the answer direction, then explain. Fence-sitting reads as not knowing.
2. **Depth, jargon used correctly.** Correct vocabulary deployed to make a structural point. Wrong jargon is worse than none.
3. **Real experience.** "I'd put gradient-boosted trees on it" and "the first question after I ship is why didn't this account get flagged" show you have done it, without a speech about having done it.
4. **Nuance.** Commit first, then layer the second consideration. This is what moves B+ to A+.
5. **Succinct.** Under 120 seconds. Word salad is the tell of feigned expertise.

**The correction the source gets wrong: Law 6, honest uncertainty.**

The source treats not-knowing as a failure mode. At senior and Director level that is backwards. "I don't know" followed by a real method is often the strongest available answer, and interviewers at Anthropic and OpenAI specifically probe for it, because a PM who bluffs to a researcher burns the relationship in week one.

The shape that works: **name the boundary, give the method, name what would change your answer.** "I don't know the attention-head count on that model and I would not guess. What I would do is check the model card, then run our eval set against it before anyone commits a roadmap date. If the latency profile came back above 400ms p90, the whole design changes." That answer scores higher than a confident wrong number, every time.

**The distinction that matters:** not-knowing a *fact* is fine. Not-knowing a *mechanism* you claimed to have shipped is fatal.

---

## The six auto-fails (carried, all real)

1. **Bluffing a detail.** Named immediately by a good interviewer, and unrecoverable.
2. **Calling a wrapper a platform.** Claiming architecture you did not build.
3. **Reporting input metrics as success.** Seats sold, tickets closed, prompts run. This is Ravi's own Rule 33: a deployment headline is a purchase, not a verdict. If you cannot draw the line from spend to useful work shipped, do not quote the number.
4. **The perfect record.** No failed project, no dead feature, no wrong call. Reads as either junior or dishonest.
5. **The deterministic PRD.** Speccing an AI feature with fixed acceptance criteria and no confidence threshold, no drift trigger, no named failure owner. `rtp-ai-prd` exists precisely because this is the most common senior-PM failure.
6. **Going too deep.** Deriving backpropagation at a product-layer interviewer. Read the archetype in the first two minutes.

**Add: auto-fail 7, the unsourced statistic.** Quoting "95% of AI pilots fail" or any viral number without its population and tier. Ravi's Rules 31 and 34 apply in a room exactly as they apply in a document: name the source and the population, or soften the claim. An interviewer who knows the study will ask, and being wrong about the number you volunteered is worse than never raising it.

---

## Grounding: answer from what he actually built

An answer without a real deployment behind it is a book report. Before any mock or grading session, pull the real material rather than inventing placeholder experience.

**Sources, in order:** `1_Projects/0_interview-prep/` for existing prep, `5_My Resume/` for the shipped record, `3_Research/08_career/` for the collected guides, and the harness, evals and context-engineering deep dives in `3_Research/01_agentic-stack/`, `02_harness-engineering/` and `03_ai-evals/` prefixed `Ravi_`, which are his own authored analysis and the strongest evidence of depth he has.

**The three anchors every answer should be able to reach for:**
- **Honeywell, twelve years, Fortune 100 scale.** Enterprise constraint is his edge over candidates whose only context is a startup. Regulated, safety-critical, slow-moving stakeholders, real procurement.
- **Perplexity AI Fellow 2025.** Frontier-adjacent credibility.
- **The library itself.** 68 skills built from production failures, an HBR and MIT Sloan corpus with evidence tiers. When an interviewer asks how he keeps current, this is the answer, and almost no candidate has one.

**The Bridger frame** is the through-line for the behavioral round: he curates partners, translates across how each works, and integrates. When engineering wants a validation layer, design wants users to feel in control, and finance asks about ROI at 10x, he makes each feel understood *and* challenged, then finds the path serving all three. Every behavioral answer should show that motion, not narrate it.

---

## Mode 1: Mock

Run one question at a time. **Push exactly one level deeper on the weakest part of each answer before grading anything.** That single move is what real technical rounds do and what most prep skips.

Announce the archetype first:
- **Engineer in the room** wants the mechanism. Every answer earns a follow-up one layer down. Default for frontier labs and infra roles.
- **Product-layer PM** asks a mechanism question but listens for what you *do* with it. Mark down over-derivation. Default for applied-AI roles.

Follow-up patterns: a definition gets "now apply it"; a named tool gets "when would you not reach for it"; product-layer talk to an engineer archetype gets "under the hood, what does the model actually emit"; deep mechanism to a product archetype gets "as the PM, what do you do with that on day two"; a bluff gets named immediately.

**After five questions, score on the 6 Laws, weakest link not average**, name the single highest-leverage fix, and rewrite the weakest answer using real experience.

## Mode 2: Grade

Take a written or spoken answer. Fact-check the mechanism first, then score each Law, then rewrite to A+ grounded in his actual work. Name any auto-fail triggered. End on one fix, not a list.

## Mode 3: Company prep

Read the role, then map: which of the seven rounds will they run, which archetype per round, which skills hold the answers, and **what is the one question most likely to expose a gap.** Then pre-mortem it (see below).

## Mode 4: Loop pre-mortem (this skill's own contribution)

Before the loop, not after. Borrowed from `rtp-falsification` and the pre-mortem thinking algorithm.

**Assume the loop failed. Write the rejection reason.** Then work backwards. The honest answers are usually one of: too abstract with no shipped detail, no failure story, could not defend a number, over-indexed on frameworks and under-indexed on judgment, or read the archetype wrong and went deep at a product-layer interviewer.

Whichever you wrote, that is the drill for this week. **A pre-mortem that produces no uncomfortable answer was not run honestly.**

## Mode 5: Interviewing them

Half the signal, and almost nobody preps it. At Director level, asking nothing reads as either desperate or incurious.

Questions that actually reveal something, because they cannot be answered with a slogan:

- **"Who has the authority to stop a model that is causing harm, and do they report to the person shipping it?"** Straight from `rtp-responsible-ai-program`. The answer tells you whether governance is real or theatre, and most companies cannot answer it.
- **"What did you ship in the last year that did not work, and what happened to the person who called it?"** Tests whether failure is survivable.
- **"How do you know your AI feature is getting worse?"** If there is no eval story, you would own that problem in month two.
- **"What is the unit economics of your flagship AI feature at 10x current usage?"** From `rtp-cost-model`. If nobody has run it, you would inherit that.
- **"Where does this role's judgment actually sit?"** Are you owning the decision or writing tickets for someone else's?

Take notes. This is a two-way evaluation and behaving like it changes how they read you.

---

## Delivery mechanics (the part prep skips)

- **Answer out loud, with dictation, in practice.** This round punishes rambling and you cannot hear rambling by typing.
- **Under 120 seconds**, then check in: "does that answer it, or do you want the layer below?" That question is itself a senior signal.
- **Lead with the decision, then the reasoning.** CPO in front, executioner behind. The interviewer can always ask for depth; they cannot un-hear a five-minute preamble.
- **Vary structure.** Answering three questions with the same "it depends, here are three considerations" shape reads as a template.
- **Name the trade-off you are accepting.** "I would ship at 85% accuracy with a human reviewer, and I am accepting slower throughput to get an audit trail." Naming the cost is what separates a decision from an opinion.

## Quality gate

- [ ] Every answer commits to a direction in the first sentence.
- [ ] Every technical claim is one you could defend one layer deeper.
- [ ] At least one answer per session names a real failure and what it cost.
- [ ] No statistic without its population and evidence tier.
- [ ] No skill named out loud.
- [ ] Nothing claimed as built that was not built.
- [ ] Prepared at least three questions *for them*, at least one of which is uncomfortable.

## When wrong

- **Do not run this for a non-AI PM role.** The 6 Laws and the round map are calibrated to AI product interviews. A classic PM loop weights differently.
- **Do not let framework recall replace judgment.** If an answer sounds like a skill being recited, it has failed. The library informs; it does not speak.
- **Do not over-prepare the behavioral round.** Over-rehearsed stories lose the texture that makes them credible. Know the anchors; do not script the sentences.
- **Privacy guardrail, carried from the source and binding:** career gaps, health, family, financial constraints, immigration details, age, relationship status. These may inform internal analysis and must never appear in generated answers or coaching output.

## Attribution

The 5 Laws, the two archetypes, the follow-up ladder and the six auto-fails are adapted from `ai-pm-technical-interview` by Aakash Gupta (product-growth.com), built from research into real AI PM technical rounds at OpenAI, Anthropic, DeepMind, Nvidia, Perplexity, Glean, Microsoft, Amazon and Meta. The full-loop map, the skill routing, the honest-uncertainty law, the unsourced-statistic auto-fail, the loop pre-mortem, and the interviewing-them mode are additions.
