---
name: capability-tracking
version: v2.10_latest
description: 'Decide whether to build an AI feature now or wait for model capability uplift to deliver it free. The build-vs-wait call for ONE capability''s trajectory. Not the workforce question (apprenticeship erosion, which is judgment-guard''s ''capability debt''), and not harness architecture (what model upgrades absorb). Covers the capability radar, half-life benchmarks, the quarterly capability test, and build-vs-wait signals. Also: capability parity doesn''t guarantee task automation, since friction (judgment, human assurance, error tolerance, regulation) can hold a ready capability at ''assist'' for years. Use when scoping 12-18 month roadmaps, fine-tune-vs-wait calls, or a capability watchlist. Pairs with: harness-operating-model, judgment-guard, strategy-canvas, build-or-buy, cost-model. Triggers: ''should we build this'', ''wait for the next model'', ''18-month roadmap'', ''commoditization risk'', ''build vs. wait''.'
imports: [strategy-canvas, first-principles]
---

# Capability Tracking: Know What the Model Will Do Next

## DEPTH DECISION

You are evaluating whether a feature should be built by your team or acquired through model capability improvements. The question: Is this something we invest in custom engineering for, or do we wait for Claude/GPT-5/Gemini to do it for free in 9 months?

The trap: Treating model capabilities as fixed. They are not. A feature that needs 3 engineers today might be a prompt rewrite next quarter. But the opposite is also true: betting your product on an unreleased capability is how you get stranded.

**Who uses this:** Product managers deciding between build/buy/wait. Founders planning 18-month roadmaps. Tech leads scoping feature work.

**Not this skill:** if the question is "our juniors aren't learning judgment because AI does their first drafts" — that's workforce capability erosion, covered in `judgment-guard`. If the question is "which piece of our agent harness will the next model upgrade make redundant" — that's `harness-operating-model`'s dissolving ladder. This skill is narrower: one capability, one product decision, build now or wait.

## DELIVERABLE FORMAT

Before starting, ask:
> **What format would you like this in?**
> 1. **Word Document** (.docx) — Formatted report with embedded visuals. Best for sharing.
> 2. **Presentation** (.pptx) — Slide deck with key findings. Best for meetings.
> 3. **Both** — Full report + summary deck.
>
> *Default: Word Document.*

If the user specifies format in their request, skip the question.

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

**Trap 1: Assuming capabilities stay flat.** You evaluate the current model, build a feature, ship it. Six months later, the model does it natively. You spent 8 weeks on what is now a prompt.

**Trap 2: Betting on futures that never materialize.** "We'll wait for multimodal." Three years later, you're still waiting and competitors shipped.

**Trap 3: Mistaking capability for product feature.** GPT-4 can do reasoning. That doesn't mean users want a 20-second latency reasoning feature. Capability ≠ Product.

**Trap 4: Building moats that evaporate.** Your 2023 differentiation was a fine-tuned model. By 2024, prompt engineering + RAG obsoleted it. You need capabilities models won't commoditize fast.

**Trap 5: Assuming capability parity means task automation.** A model clearing your accuracy threshold tells you the *capability* is ready. It doesn't tell you the *task* will actually get automated on your timeline — task-level friction that has nothing to do with the model can hold it at "assist" or "reshape" for years. Commercial aviation is the clean example: autopilot has handled most of the actual flying since the 1980s, yet the European Union Aviation Safety Agency doesn't expect full passenger-flight autonomy before 2050 — the barrier is human assurance and regulation, not capability (⚠ EASA estimate as reported by Drover & Huang, "The Forces That Shape AI's Uneven Progress," *MIT Sloan Management Review*, Nov 18 2025). Before you plan around "the model will be ready in Q3, so we ship in Q3," check whether your task carries the same kind of friction: does it need human judgment under real uncertainty, does a user need a human to be accountable regardless of accuracy, is the error tolerance near zero, is there a regulatory or organizational gate that doesn't move on the model's release schedule? If yes to any of those, the model being ready is necessary but not sufficient.
**When this over-warns:** don't let "friction exists somewhere" become a standing excuse to never ship. Apply it task-by-task — routine data entry and first-draft customer replies score low on all four frictions and are already at "replace" in practice. The check exists to separate those from judgment-heavy, high-stakes, regulated tasks, not to stall everything behind a vague appeal to "humans still matter here."

**Trap 6: Reading a stock measurement as a flow prediction.** This one sits underneath the whole capability-debt argument and it is rarely stated.

Every measured finding about AI and human expertise, in this library and in the literature it draws on, was taken on people whose expertise **formed before AI arrived**, and then reported as a property of the technology. Engineers losing calibration when they stop producing. Junior cohorts underperforming the machine while applying real judgment. Evaluators deferring to an explained recommendation. All of them measured on a stock accumulated pre-AI.

**Nobody has measured the cohort the argument is actually about**: people whose expertise is forming under AI assistance from the start. The capability-debt case, that thinning the apprenticeship pipeline leaves you unable to make experts, is a claim about the flow. The evidence is about the stock.

**What this changes in practice, because it is not a reason to stop worrying.**

- **Say which population you are reasoning about, in the register.** "Our seniors will lose calibration" and "our juniors will never gain it" need different evidence and have different fixes, and only the first is well supported.
- **Do not price capability debt off the incumbent studies.** They tell you what removing production does to someone who already had judgment. They are silent on what a different formation path produces, which could plausibly be worse, equal, or in some tasks better.
- **The missing study is specific and cheap to name:** a cohort whose expertise formed under AI assistance, showing the same expertise-distance gradient as the pre-AI cohorts. Until someone runs it, treat the flow claim as a well-argued hypothesis and label it that way when you take it to a room.

The same error shows up in prescriptions, not only findings. Two 2026 articles, in two journals, two weeks apart, both instruct professionals to exercise a judgment capacity and neither explains how a newcomer accumulates it; one describes the capacity as something that "has always distinguished exceptional professionals," which is the assumption said out loud.

**When this over-warns:** it is an evidence-labelling discipline, not an argument that the pipeline is fine. The apprenticeship risk may well be real. The point is to stop citing incumbent-cohort studies as though they measured it.

*(Ledger pattern P. Sources: MIT SMR, Sloan & Glaser, Aug 2026; HBR, Sudakov & Furr, Aug 2026; the KPMG junior-employee study and Liu & Kovács already cited in this library. See `rtp-judgment-guard` for the individual-level version.)*

**Trap 7: A model release can reclassify people without their behavior changing, and the same blind spot hides inside your adoption metrics.**

Four July 2026 findings, from three different sources, point at one mechanism: the measuring instrument holds still while the thing underneath it moves, so a number that once meant something quietly stops meaning it.

**The floor moves under performance ratings.** As a model's baseline quality rises release over release, an employee's "performance relative to AI baseline" classification can flip with no change in what that employee actually does. This is a moving floor, not a moving person (◆ company-disclosed, KPMG/UT Austin, n=523, single site, unpublished, the same study already anchoring Trap 6's population). **Fix:** track capability as a delta against the current baseline, re-measured on the vendor's release cycle, not on your organization's annual or quarterly review cycle. A review cadence set by the HR calendar drifts out of sync with a capability that moves on a lab's ship schedule.

**The floor moves under skills that need repetition to form.** A capability that compounds through exercise, doing the work by hand, repeatedly, is a different thing from one that compounds through being fed a repeated decision. An agent that does the work perfectly and invisibly still gets the work done, which is exactly what removes the exercise condition that built the capability in people. Nothing in output quality warns you before the cliff: capability holds exactly as long as the current cohort stays, then disappears with no prior signal (⚠ argued mechanism from a podcast conversation on process knowledge economics, not a measured rate). **Fix:** for capabilities you believe are exercise-fed, add a countable instrument: hours per month of junior staff observing seniors perform the actual work. For capabilities that are decision-fed instead, decision volume and decision quality remain the right instrument. Don't apply one metric to both kinds.

**One adoption number hides two opposite assignments.** Junior headcount gets used two ways that pull against each other: apprenticeship, unaided production meant to build judgment, and building an AI-power-user pipeline, aided production meant to spread adoption. A tracking system that measures only "AI usage" reads the apprenticeship-track junior as underperforming, when they are doing exactly what they were assigned (⚠ MIT Sloan podcast; the guest, associated with Workhelix, has an undisclosed commercial interest in the framing, flag this whenever citing). **Fix:** record which track a given junior is deliberately on. Don't collapse both tracks into one adoption metric.

**Declared adoption and used adoption are different signals wearing the same name.** An index built on declaration signals, LinkedIn posts, earnings-call mentions, job postings, ranks firms by their incentive to announce AI adoption loudly, not by how much they actually use it. The MIT Sloan piece behind one such index used Bolt.new/StackBlitz as its flagship "AI-native" example; that company is seven years old, not a young AI-native firm, so its ARR-per-FTE framing does not support the claim it was cited for (independently verified; do not carry that framing forward as evidence of anything). **Fix:** keep declared adoption (what gets announced) and used adoption (what shows up in workflow telemetry) as two separate columns. A tracking system built only on the first is measuring PR, not capability.

**The rule underneath all four:** name what you are measuring, against which clock, and for which sub-population, every time you write a capability number down. Skip any one of those three and the number keeps last quarter's meaning while the thing underneath it has already moved.

**When this over-warns:** in a team small enough for one manager to know firsthand who is coasting and who is still building judgment, or where the junior population genuinely does not split into apprenticeship-track and power-user-track, this level of instrumentation is more process than the situation needs. Reach for it once tracking crosses more than a handful of people, or once a capability claim is about to feed a hiring or promotion decision.

*(Sources: KPMG/UT Austin junior-employee study, ◆, n=523, single site, unpublished, already cited in Trap 6; Dan Wang podcast on process knowledge economics, ⚠ argued mechanism; MIT Sloan podcast featuring McAfee, ⚠ undisclosed Workhelix commercial interest; MIT Sloan Management Review article on AI-driven entrepreneurship and the AIDE Index, ⚠ reported, Bolt.new/StackBlitz framing independently verified as unsupported. All July-Aug 2026. See `rtp-judgment-guard` for the apprenticeship-erosion mechanism this tracking fix feeds.)*

## THE PROCESS

### 1. Capability Radar
For each critical capability your product depends on:
- Current state: Does the latest model do this? What's the quality/latency?
- Trajectory: Is this improving? By how much per release cycle?
- Deprecation risk: When does this go from "custom engineering" to "included"?

Create a 3x3 grid:
- X-axis: Time to commoditization (0–3 months, 3–12 months, 12+ months)
- Y-axis: How much your product depends on this (core, differentiating, nice-to-have)

**Quick diagnostic:** Plot your top 5 features. Anything in the "core capability + commoditizing in 3 months" cell is a threat.

### 2. Strategy Half-Life
For each piece of tech/capability your product relies on, ask:
- When was this capability created/integrated?
- How much value has degraded since then?
- What will commoditize it?

**Example:** Your ranking algorithm was state-of-the-art 18 months ago. Models now rank nearly as well with a prompt. Your half-life on this advantage is ~9 months. Decision: Do you hold it or migrate to a model-native approach?

### 2A. The Halving Rate — an external anchor for how fast the floor rises

Half-life reasoning needs a number to anchor on, and until now this skill has had none. The best available one, with its scope attached:

**The failure rate on text-based workplace tasks halves roughly every 2.2 to 2.8 years.** Measured across more than **6,000 tasks** drawn from the US Department of Labor's O\*NET database, using more than **60,000 worker evaluations**. Current capability at the time of measurement: roughly **50% to 75% of text-based tasks completed to a *minimally sufficient* standard without edits.**

**Three scope conditions, and every one of them narrows what you may conclude:**

- **Text-based tasks only.** The rate says nothing about work whose hard part is physical, relational or political.
- **Inputs were already assembled.** The evaluations supplied the information. In a real job, gathering it is a large share of the work, so the rate is measured on the cheaper half of the task.
- **"Minimally sufficient" is the floor rung**, not the substitution threshold. See `rtp-ai-product-metrics` for the three-rung acceptance ladder. **The study's own summary box reports that floor as "completes the task," which overstates its body**, and that is exactly how this figure will reach you second-hand.

**The shape finding is more useful than the rate.** Capability improved **broadly across tasks of very different lengths** rather than surging on a narrow set. The image the researchers use: rather than a wave knocking a few people over, the water rises around everyone step by step. That is an argument for continuous re-tracking over episodic capability reviews, and it is the empirical basis for this skill's existence.

**The trap this closes, and it is the one people fall into with any benchmark.** A benchmark improvement does not translate into an organizational one, because **the two vary on different axes**. A benchmark holds the task fixed and varies the model. An organization holds the model roughly fixed and varies the task, the context, the tooling and the person. This skill already says that capability parity does not guarantee task automation. The halving rate supplies the mechanism and a number for the first axis, and **supplies nothing at all for the second.**

**The consequence for your build-versus-wait call below:** size the *capability* window on the halving rate, and size the *commercial* window on something else entirely. Capability is a smooth curve produced by many labs improving independently. Price is a step function produced by a few vendors making dated decisions on a board's calendar. Organizations routinely compute their adaptation window on the first and get hit by the second. See `rtp-cost-model` section 4B.

*(Source: MIT FutureTech, reported via MIT Sloan, Aug 2026 — ◆ study-disclosed. **No human comparison arm**, so none of this supports a substitution claim on its own. **Decay clock:** a halving rate is itself a claim about the near past; re-verify before citing past end-2027.)*

### 2A-bis. The AI wall: how far the tool carries someone outside their domain

**A capability question this skill has been answering only for the model.** How much does the tool raise a person who does not already know the work?

**The finding: less than expected, and the governing variable is expertise distance.** One study split participants three ways on the same writing task:

| Group | Relationship to the task | What the tool did for them |
|---|---|---|
| **Experts** | do the task routinely | genuine lift |
| **Adjacent outsiders** | same department, no production experience, shared vocabulary | partial |
| **Distant outsiders** | neither production experience nor domain vocabulary | hit the wall |

**The AI wall is the limit on how much a general model can help someone perform a task outside their area of expertise**, and effectiveness falls as expertise distance grows.

**What this changes in a build-versus-wait call.** "The model can do it" and "our people can now do it with the model" are different claims. **A capability arriving does not close a staffing gap if the people you would hand it to are distant outsiders to the domain.** Score expertise distance alongside capability before assuming a tool substitutes for hiring.

**The uncomfortable corollary.** The tool helps most where you already have depth, which means **it widens the gap between teams that have domain expertise and teams that were hoping to buy their way past needing it.**

*(Source: Vendraminelli et al., HBR, "Gen AI Won't Make Your Employees Experts," Apr 2026 — ◆ single study, one company, one writing task. The authors argue the wall generalizes beyond writers and technologists, and that generalization is their claim rather than their measurement.)*

### 2B. Capability Debt: the liability automation creates and nobody books

This skill tracks whether the *model* can do the work. **This tracks whether your people still can**, which is a different question and the one that goes unmeasured.

**The construct, stated as a debt rather than a gap, and the distinction matters.** A skills *gap* puts the burden on individuals to catch up. A **capability debt** is a systemic obligation the organization took on and must repay. It "accumulates silently, one automated function at a time," and does not appear anywhere until it becomes a crisis.

**Why entry-level automation is the expensive kind.** Professional development runs roughly **70% from doing the job, 20% from working alongside experienced colleagues, and 10% from formal training** (the Center for Creative Leadership model). Entry-level roles are the main vehicle for the first two. **So removing the role removes about 90% of the development model, not a training line item.** The training budget survives; the pipeline does not.

**The three-question audit. Run it per automated function, against every entry-level function automated in the last 36 months:**

1. **Who could perform this work without AI if required?**
2. **Who can reliably evaluate AI outputs for accuracy?**
3. **What developmental pathways no longer exist?**

Question 3 is the one nobody asks, and it is where the debt actually sits. Questions 1 and 2 measure today. Question 3 measures whether you can still make someone who passes 1 and 2 in five years.

**Run it cross-functionally or it returns the comfortable answer.** The source specifies a team including the CHRO, the CTO, and at least two business-unit leaders. A single function auditing itself will not name the pathway it removed.

**The repair, if the audit finds debt.** Rebuild entry-level roles as deliberately leaner capability-building cohorts, AI-augmented from day one, designed around **healthy friction**: productive discomfort that stretches people past their current skill. One organization replaced a 200-person program with a structured 50-person cohort on this logic. Pair that with apprenticeship written into performance expectations and compensation, rather than treated as volunteer work.

**How this bounds the build-versus-wait call below.** A capability you wait for is a capability you are also not building people around. **If the wait is long and the function is a training ground, the honest cost of waiting includes a pipeline you stopped filling.** See `rtp-judgment-guard` for the individual-level version of the same mechanism.

*(Source: HBR, "Your Talent Strategy Has to Keep Up with Your AI Transformation," Jun 2026 — ⚠ practitioner-tier. The 70-20-10 model is the Center for Creative Leadership's, named in the article without an individual author. "Healthy friction" and the 200-to-50 cohort redesign are the article's own single unnamed case, so **carry the mechanism and not the numbers**. This is the second independent sighting of capability debt in one month, after the engineering-provenance version; a third would justify its own skill.)*

### 3. Build vs. Wait Decision Tree

START: Do you have a critical need for this capability right now?
- NO → Ask: Is it core to your differentiation in 2027?
  - NO → Don't build. Wait.
  - YES → Go to BUILD.
- YES → Ask: Will a future model provide 80% of the value?
  - NO → BUILD now.
  - YES → Ask: When will that model release?
    - 0–3 months → WAIT.
    - 3–6 months → BUILD minimum viable + plan migration.
    - 6+ months → BUILD, own it, plan obsolescence.

### 4. Deprecation Planning
Once you build something, assume it will be commoditized.

Set a "model capability check" quarterly. For each custom capability:
- Has the model improved against this? By how much?
- Would a migration to model-native be faster than maintaining custom code?
- What's the sunk cost of switching?

Document the switchover path before you forget it.

### 5. Harness Assumption Register (the tracking artifact — the concept lives in `harness-operating-model`)

Every component in a multi-agent harness encodes an assumption about what the model can't do on its own. The framework for reasoning about this — which harness capabilities are "permanent residents" (evals, workflows, audit trail, cost controls, user context) that no model release absorbs, versus which sit on the "dissolving ladder" that model upgrades do absorb (structured output, tool-calling, long context, multi-step reasoning, generic safety), plus the four-question meta-skill for predicting what dissolves by 2027 — is owned by `harness-operating-model`. Read that skill for the reasoning. What belongs here is the practical artifact once you've applied it: a dated register you re-test on every model release.

| Harness Component | Model Limitation Assumed | Still Valid After Latest Release? | If Invalid |
|--|--|--|--|
| Planner agent | "Model can't decompose 50-step tasks without losing coherence" | Test each release | Remove; test direct planning in the task agent |
| Memory shard manager | "Model can't hold full session history without context explosion" | Test each release | Raise the shard threshold or remove |
| Fact-checker node | "Model hallucinates dates in long documents" | Test each release | Narrow scope to the document lengths where it still fails |

**Example:** Opus 4.5 needed scaffolded planning; Opus 4.6 plans 50-step sequences natively. Remove the planner node, re-test on the same tasks — latency drops, complexity halves, and the freed engineering capacity moves to retrieval quality instead.

Every harness component is debt that accrues interest. As models improve, pay it down — don't keep scaffolding you no longer need.

### 6. Strategy Half-Life Quantification

Quantify how fast your AI strategy assumptions decay. This is not a fixed decay (straight-line depreciation). It's exponential, driven by:
- How many competitors are building the same thing
- How close the capability is to commoditization
- How defensible your data/moat is

**Strategy Half-Life Benchmarks:**

| Advantage Type | Half-Life | Example | Why It Decays |
|---|---|---|---|
| Prompt-level advantage | 3-6 months | "We have a 30-turn conversation template that beats baseline" | Competitors copy your prompts; models improve; techniques commoditize fast |
| RAG/retrieval advantage | 6-12 months | "We indexed the full Knowledge Graph; retrieval is 2x faster" | Embedding models improve every 3-4 months; retrieval becomes table-stakes |
| Fine-tuning advantage | 12-18 months | "We fine-tuned on domain data; domain accuracy is 95%" | New base models often exceed fine-tunes; your dataset becomes dated; competitors collect better data |
| Data flywheel advantage | 24-36 months | "We've collected 5 years of user interactions; our signal is unmatched" | Hardest to replicate; stickiest moat; but eventually competitors gather enough data |
| Harness/orchestration advantage | 12-24 months | "Our 4-agent workflow is faster than single-agent baselines" | Orchestration patterns become known; simpler models do it natively; architecture spreads |

**How to track half-life decay:**
1. **At creation:** Log the date, capability, and estimated half-life category
2. **At 50% half-life:** Test the assumption. Has the capability commoditized? Yes/No
3. **At 100% half-life:** If assumption is NOT violated, extend the half-life (you were conservative). If violated, start renewal/replacement planning

**Example tracking:**
- Prompt-level advantage created Jan 2025. Half-life = 3-6 months. Review date = April/May 2025.
- April 2025: "We tested Opus 4.6 on the same prompt template. It matches our performance now."
- Decision: Refresh the prompt to maintain advantage, or accept that advantage is decaying and plan migration to a deeper moat (fine-tuning, data).
- If you don't refresh, the advantage is dead by July 2025.

**Track your top 5 capabilities against these benchmarks:**
- Which are past half-life and stale?
- Which are 50% through half-life and need renewal plans?
- Which haven't decayed yet (why? is your estimate conservative)?

This prevents the trap of "we built something smart 3 years ago and we're still coasting on it."

## RISING TIDE, NOT CRASHING WAVE: WHAT THE SHAPE OF CAPABILITY GAIN MEANS FOR YOUR RADAR

**The planning fear is a shock: one capability jump, a narrow set of tasks suddenly gone.** The largest measurement of this to date says the shape is different.

**The design, because it decides what the number means.** More than 60,000 worker evaluations of AI output on more than 6,000 text-based workplace tasks, drawn from the US Department of Labor's O*NET database. **The finding: capability improved broadly across tasks of very different kinds and lengths, rather than surging on a narrow set.**

The researchers' own image: standing on a beach. In the crashing-wave scenario a few people suddenly get knocked over. What the data shows is the water rising around everyone, step by step.

**Three things this changes about how you run a capability radar:**

1. **Stop watching for the cliff and start watching the waterline.** A radar built to catch a discontinuity will report nothing quarter after quarter and then be surprised by an accumulation. Track the gradient across your whole task inventory, not the maximum on your riskiest task.
2. **Breadth beats depth as an early signal.** If a model release improves your hardest task by a lot and your other twenty by nothing, that is narrower than the trend and probably a benchmark artifact. If it improves all twenty a little, that is the tide and it will keep coming.
3. **Half-life estimates should be smooth, not stepped.** A build-versus-wait call that assumes a step function will systematically wait too long, because the step it is waiting for does not arrive as a step.

**The limit to state alongside it, and it matters.** The study has **no human comparison arm.** It measures AI output quality as rated by workers, not AI against a human doing the same task. **So it supports a claim about the shape of improvement and supports no claim about substitution.** Anyone using it to argue headcount is using it wrong.

*(Source: MIT FutureTech, reported via MIT Sloan, "How will AI automation hit - like a crashing wave or a rising tide?," Aug 2026 — ◆ study-disclosed, n over 60,000 evaluations across over 6,000 O*NET tasks. Text-based tasks only, no human comparison arm. Falsifier: a model release that improved a narrow task cluster sharply while leaving the rest of an O*NET-style inventory flat.)*

## THE QUARTERLY CAPABILITY TEST

Model benchmarks tell you what changed. This tells you what it means for *your* product.

**The protocol (run every quarter, or whenever a major model update ships):**

1. **Pull your golden set.** Take the 100 queries your product handles most frequently. These should already be in your eval dataset. If they're not, sample 100 from production logs today.

2. **Run on old model + new model, same prompts.** No prompt changes — you're isolating the model variable.

3. **Measure three things:**
   - **Accuracy delta:** What % of queries improved? What % regressed? Net movement.
   - **Latency delta:** P50 and P95 latency. Did the new model get faster or slower at your task?
   - **Cost delta:** Input + output tokens per query. Did the new model use more or fewer tokens to reach the same answer?

4. **Categorize results:**
   - **Clear win:** Accuracy up, latency down or same, cost down or same. Switch immediately.
   - **Quality-cost tradeoff:** Better accuracy but higher cost. Run unit economics to see if it's worth it.
   - **Regressed cases:** Any accuracy decrease on previously-working queries. These are your blockers — fix before switching.
   - **Wash:** No meaningful delta. Wait for the next release.

5. **Decide in 48 hours.** Don't let model evaluation drag into a 2-week analysis. The test gives you a decision, not a research paper.

**What good looks like:** You're running this test before model updates ship to users, not after. Proactive testing beats reactive debugging.

## WHICH END OF THE JOB THE MODEL REACHES FIRST DECIDES WHICH WAY PAY MOVES

**Task loss does not mean wage loss, and the direction inverts the intuitive fear.** Two branches, distinguished only by which part of a job gets automated:

| What gets automated | What happens to the job | Wage direction | Mechanism |
|---|---|---|---|
| **The simple parts** | The remaining tasks demand more expertise | **Up** | Fewer people can do what is left |
| **The specialized parts** | The job becomes doable by non-specialists | **Down** | Competition from substitutes |

**Read the table again, because it says the opposite of what most people assume.** Automating your drudgery raises what you are worth. **Automating your specialized skill is what lowers your pay**, because it opens your job to people who could not previously do it.

**What this changes about a capability register.** Tracking "which of our tasks will the model do" is only half the question. **The half that predicts your team's position is which end of each role it reaches first.**

- **Model improving on the routine end of a role** is good news for the people in it. Plan for a smaller, more senior version of that team.
- **Model improving on the specialized end** is the one to watch. The role does not disappear, it de-skills, and the people whose value was the specialization are exposed before any headcount conversation happens.

**A related pressure worth carrying alongside it:** models are disproportionately better at automating shorter tasks than longer ones, and lower-income work tends to be composed of shorter tasks. **So the exposure is not evenly distributed**, and a register that averages across a workforce will miss where it concentrates.

**The honest limit.** There is no stated method for predicting which branch a given occupation lands on. The table is a lens for reading a capability trend, not a forecast you can run.

*(Source: Neil Thompson, reported in an MIT summary piece, "5 things to consider when working with AI," Jun 2026 — ⚠ and the tier matters here. **That article contains no quantitative figure of any kind**: no sample size, no effect size, no percentage. It is a staff summary of conference talks, adapted into an article, and none of the underlying studies is named, cited or dated, so every claim is two removes from the research. Carry the two-branch logic as a way of thinking; do not attribute a magnitude to it. Falsifier: an occupation where automation of its specialized tasks raised wages.)*

## AI MOVES TWO INPUTS TO LEARNING IN OPPOSITE DIRECTIONS

**Skill growth needs two things: effort, and a good learning environment.** AI reliably reduces the first, which should reduce learning. It can raise the second, which should increase it. **Which effect wins is a design question rather than a property of the technology**, and it is the cleanest way to predict whether a rollout will build capability or quietly drain it.

| Input | What AI does by default | What reversing it takes |
|---|---|---|
| **Effort** | Reduces it. The struggle that produced the learning is exactly what the tool removes | Deliberately keep the hard step, or move it somewhere else |
| **Environment quality** | Can raise it a lot: instant feedback, unlimited examples, a patient explainer at any hour | Only realized if someone designs for it. Installing the tool does not do it |

**The common failure is getting the first effect for free and never building the second.** That is the default outcome of any rollout measured on time saved, because time saved is the effort reduction wearing a positive name.

**Three checks on any deployment that is supposed to build capability:**

1. **Which hard step did we remove, and where did we put it back?** If the answer is nowhere, this deployment reduces capability whatever the satisfaction survey says.
2. **What did the tool make possible that was not possible before?** Faster feedback, more attempts, seeing an expert's reasoning made visible. If nobody can name one, the environment gain was never realized.
3. **Is anyone still working at the edge of their ability?** That is the observable signature of a learning curve, and it is not the same as being busy.

**How this reads against the rest of this skill.** The AI wall says a person can only edit inside their own neighborhood. **This section asks whether that neighborhood is still growing.** A team can pass every throughput measure while everyone in it quietly stops expanding what they are able to review.

*(Source: Angela Duckworth at the HBR Leadership Summit 2026, "Inspiring Grit and Growth Amid Unprecedented Change," Jul 2026 — ⚠ conference remarks. The two-input decomposition is general learning science applied to AI in conversation, not a measured finding about AI, and no effect size is given in either direction. Falsifier: a deployment that cut effort substantially and produced measurable capability growth with no deliberate environment design.)*

## MENTORING HAS TO BE REDESIGNED, BECAUSE IT ASSUMED SOMETHING THAT IS NO LONGER TRUE

**Traditional mentoring assumes foundational learning already happened through hands-on work. It did not.** AI absorbed the routine work through which people used to build judgment and pattern recognition, so the mentee now arrives without the base the mentoring model was built on top of. On-demand learning platforms do not close the gap, because the missing thing is tacit and platforms transfer explicit.

**Name the competencies first, so the mentoring has a target.** Seven, offered as the senior-leader set to define before designing anything: critical thinking, professional judgment, pattern recognition, proactive communication, stakeholder management, prioritization, and navigating ambiguity. **The point of the list is not the list. It is that mentoring aimed at "growth" produces nothing and mentoring aimed at one named competency can be assessed.**

**Six design moves, and the fourth and fifth are the ones organizations skip:**

1. Clarify expectations for both sides.
2. Incentivize mentors, because this is real work with no natural reward attached.
3. Offer support, so mentors are not inventing the method themselves.
4. **Match mentors to skills gaps, not to org charts.** The best mentor for pattern recognition is rarely the person two levels up in the same reporting line.
5. **Make invisible thinking visible.** This is the whole transfer. The mentor narrating why they rejected an option is the lesson; the decision itself is not.
6. Build learning into everyday conversations rather than into a monthly slot.

**The one artifact worth copying: a one-page mentoring agreement with four fields.** Goals, competencies to gain or enhance, meeting cadence, and what each party commits to. **Four fields is the right size, because a longer document turns into a process nobody runs.**

**Where this connects to the rest of this skill.** The four-step judgment process below is what a mentee does alone. This is what the pairing adds, and move 5 is why the pairing is not redundant: **a reasoning trail records one person's thinking, and a mentor narrating live shows the thinking that never reaches the trail.**

*(Source: HBR, "Why Mentoring Matters More in the AI Era," Jul 2026 — ⚠ practitioner-tier. **The article names no framework, cites no source for the seven competencies, and draws the six moves from observed practice at unnamed companies.** Carry the lists as a usable starting structure, not as findings. Falsifier: a cohort mentored on org-chart matching that gained the named competencies as fast as one matched on skills gaps.)*

## BUILDING JUDGMENT WHEN APPRENTICESHIP IS GONE

The AI wall says who can edit. **This section is about how someone becomes the kind of person who can.**

**The traditional route was apprenticeship: do the junior work badly, get corrected, slowly acquire the intuition that lets you stop consciously applying rules.** The endpoint is expertise you cannot fully articulate, knowing more than you can tell. AI removed the junior work and left the endpoint in place with no path to it.

**Most organizations respond by training AI fluency: prompting technique, tool certification, internal playbooks. That is a different skill and it does not produce judgment.** Fluency is knowing how to get output. Judgment is knowing what to trust, what to question, and what to refine in it.

**A four-step substitute, sequenced so the human position exists before the model speaks:**

1. **Form your own view first, before opening any tool.** Scope the task: what question, for what audience, what would make the output useful rather than merely competent. Then form a rough hypothesis of the answer's shape. **Self-test: could you critique a finished version specifically, not just say it seems fine?** If not, you are not ready to review anything.
2. **Work the model across several modes, not one.** Generate three versions with different approaches, then compare, challenge, extend. Each mode carries its own self-check, and the variety is the point. A single answer-seeking mode teaches nothing.
3. **Run a gap analysis.** Where did the output differ from your initial view, and which of you was right? This step converts a session into learning rather than into a deliverable.
4. **Deliver a reasoning trail, not only the artifact.** What you concluded, why, and where you overrode the model.

**End every reasoning trail with one sentence naming where in your domain AI is strong and where it fails.** That sentence is a personal calibration of the jagged frontier, and it is the compounding output. The artifact ships once. The calibration is what the person keeps.

**How to track it, since this skill is a register.** Judgment development is invisible in throughput and shows up in override quality. Sample a person's reasoning trails across a quarter and ask whether their overrides became more specific and more often right. **Someone whose overrides are getting rarer is not getting better. They are getting quieter.**

*(Sources: Duncan & Anderson, HBR, "Help Employees Get Better-Not Just Faster-with AI," Jun 2026 — ⚠ practitioner-tier, four steps piloted at one consultancy with no measured outcome. Building on the Dreyfus skill-acquisition model, 1980, Polanyi on tacit knowledge, and the jagged frontier from Dell'Acqua, McFowland, Mollick et al., HBS working paper 24-013, ✅ published. Falsifier: a cohort trained only on prompting fluency whose override quality improved as much as a cohort run through the four steps.)*

## KEY DIAGNOSTIC QUESTIONS

**Q1: Capability Velocity**
What's the quarter-over-quarter improvement rate for your core model capability?
- If > 15% improvement per quarter: This is commoditizing. Stop investing.
- If 5–15% improvement: Build defensible product layers, not capability layers.
- If < 5% improvement: Safe to own this capability long-term.

*Think through:* How are you measuring improvement? Is it on your specific task, or general benchmarks?
*Low end:* <5% QoQ. Capability is stable or improving slowly. Safe to invest in custom engineering.
*Mid range:* 5–15% QoQ. Noticeable improvement every quarter. Your custom work has 12–18 months before commoditization pressure.
*High end:* >15% QoQ. Rapid acceleration. Commodity threat is immediate.
*Red flag:* You haven't actually measured this. You're guessing based on model release notes.
*Sharpen it:* Run the Quarterly Capability Test. Get numbers. Then you can answer Q1 with data.

**Q2: Dependency Strength**
If this capability disappeared tomorrow, how quickly could your product operate without it?
- < 1 week: You're custodian, not dependent. Okay to own.
- 1–4 weeks: You're exposed. Plan a migration path.
- > 1 month: This is critical infrastructure. Owns you. Build flexibility.

*Think through:* What's the manual workaround? How many customers does it affect?
*Low end:* <1 week recovery. You have a fallback path. Low risk.
*Mid range:* 1–4 weeks recovery. You can migrate but it requires coordination. Moderate risk.
*High end:* >1 month recovery. Loss of this capability creates customer outage. Critical risk.
*Red flag:* You haven't identified a fallback. Your entire product depends on one thing the model can do.
*Sharpen it:* Document the recovery plan. Run it as a fire drill quarterly.

**Q3: Copycatting Cost**
A competitor with access to the same model, how long would it take them to match your capability advantage?
- < 1 week: You built prompt engineering. Not defensible.
- 1–4 weeks: You built a system. Defensible but fragile.
- > 1 month: You built proprietary data, training, or novel architecture. Worth protecting.

*Think through:* What would they need to copy? Just your prompts, or your data/training/infrastructure too?
*Low end:* <1 week. Your advantage is prompt-level. Anyone with the same model can match you quickly.
*Mid range:* 1–4 weeks. You've built scaffolding or integration work that's non-obvious. Some defensibility.
*High end:* >1 month. You've invested in data collection, fine-tuning, or custom infrastructure. Harder to replicate.
*Red flag:* You haven't thought about this. Assume your competitor is copying you next week.
*Sharpen it:* What would it cost them in time and money? That's your moat strength.

**Q4: Moat Durability**
Is your advantage from the model, from what you built on top, or from data you collected?
- From model (GPT-4 solves it) → 6-month lifespan.
- From your system (your workflow is better) → 18-month lifespan.
- From data (you trained on real usage) → 3+ year lifespan.

*Think through:* If we switched to the newest, most capable model tomorrow, would we still have an advantage?
*Low end:* Model-driven advantage. Next model release erodes it. 6-month lifespan.
*Mid range:* System-driven advantage. You've built better integration, orchestration, or UX. 18-month lifespan.
*High end:* Data-driven advantage. You've collected proprietary signals. 3+ year lifespan.
*Red flag:* Your advantage is all from the model. You're riding on Claude 3.5 Sonnet's shoulders. When 4.0 ships, what's left?
*Sharpen it:* Which of these three sources should you be investing in? Pick one and build it.

## REALITY CHECK

Check yourself:
- Have you actually tested the latest model on this capability? Or are you extrapolating from knowledge cutoff?
- Are you underweighting the "hidden work" of integrating a new model version? (Costs exist even if the capability is free.)
- Are you overweighting sunk cost? (Yes, you spent 3 months. That cost is gone. What matters is forward cost.)
- Have you asked your users whether they'd wait 3 months for a cheaper solution, or do they want it now?

## HALF-LIFE MODIFIERS: YOUR VERTICAL CHANGES EVERYTHING

The standard half-life benchmarks (prompt advantage: 3–6 months, RAG: 6–12 months, fine-tune: 12–18 months) assume a competitive, commoditizing space. Adjust based on where your vertical sits:

**Modifier table:**

| Your situation | Adjustment | Why |
|---|---|---|
| You're in a niche vertical (healthcare compliance, legal contract review, industrial maintenance) | Extend half-life 1.5–2× | Foundation models train on general data. Your domain stays differentiated longer. |
| You're in a commoditized space (email writing, code completion, customer support) | Shorten half-life 0.5× | Every frontier model release directly attacks your core capability. |
| Your advantage is data (you have proprietary labels, rare documents, specialized corpora) | Fine-tune half-life extends to 24–36 months | Data moats are the most durable. |
| Your advantage is workflow integration (deep CRM/ERP hooks, proprietary context) | Integration advantage: 18–24 months | Switching cost is the moat, not the model. |
| Your advantage is prompt engineering alone | Reduce to 1–3 months | Anyone can copy a prompt. |

**The honest question:** "Is what makes us good about *our capability* or about *the model's capability*?" If the answer is mostly the model, your half-life is whatever the model's release cycle is.

## BUILD OR WAIT: READING COMPETITIVE SIGNALS

Don't wait 6 months because a benchmark said capability half-life is 6 months. Watch the signals that tell you *specifically* when to move.

**Build now signals:**
- A direct competitor just launched a feature in this capability area. Waiting = falling behind.
- A foundation model just crossed your accuracy threshold in your evaluation suite.
- Your current provider announced deprecation or pricing changes.
- Customer feedback explicitly names the missing capability as a blocker to renewal.

**Wait signals:**
- The current leader model is actively degrading (common with rapidly-updated models). Wait for stability.
- You're in an active model race — two frontier labs are leapfrogging on your task every 4–6 weeks. Building now means rebuilding in 2 months.
- Your capability gap is <10% accuracy. The cost of engineering time to close it exceeds the user value.
- Your market doesn't yet reward the capability. No customer has asked for it unprompted.

**The competitive signal check (monthly, 15 minutes):**
1. Check benchmarks for your specific task type (not general leaderboards — find task-specific ones).
2. Check what your top 3 competitors announced in the last 30 days.
3. Check your own support tickets and lost-deal notes for any capability mentions.
4. Decide: build, wait, or monitor.

**The friction check, before you commit to a "build now" signal.** A cleared accuracy threshold means the capability is ready — it doesn't mean the task will actually reach full automation on your timeline (see Trap 5). Score your task on four frictions before locking the roadmap date:
- **Judgment** — does it need discretion under real uncertainty, not just pattern-matching?
- **Human assurance** — do users need to know a human is accountable, independent of accuracy?
- **Error tolerance** — is near-zero error required because a miss is irreversible?
- **Regulation / inertia** — is there a compliance gate or organizational resistance that doesn't move on the model's release schedule?

High on two or more: treat "the model is ready" as a necessary condition, not a shipping date — the adoption timeline is set by the friction, not the benchmark. Low on all four: the capability-readiness signal is trustworthy on its own.

## OUTPUT FORMAT

Use this template to document and track capabilities, strategy decay, and harness assumptions:

```
## Capability Tracking Register: [Product Name]

**Product:** [Product, version, date]
**Maintained by:** [Team, review cadence]
**Last updated:** [Date]

---

### Capability Radar

| Capability | Current Quality vs SOTA | Trajectory (QoQ) | Commoditization Timeline | Renewal Plan | Owner |
|-----------|------------------------|-----------------|-------------------------|------------|-------|
| [Capability A] | [vs GPT-4.5, Opus 4.6, etc.] | [up, flat, down ±%] | [0-3mo, 3-12mo, 12+mo] | [maintain/refresh/replace] | [owner] |
| [Capability B] | [comparison] | [trend] | [timeline] | [action] | [owner] |

---

### Strategy Half-Life Tracker

| Advantage | Category | Created | Half-Life | Expires | Current Status | Renewal Plan |
|-----------|----------|---------|-----------|---------|---|---|
| Prompt template for complex reasoning | prompt-level | Jan 2025 | 3-6mo | Apr-Jul 2025 | Still ahead (Apr) | Upgrade Q2 if Opus 4.7 matches |
| RAG on domain-specific documents | RAG/retrieval | Jun 2024 | 6-12mo | Dec 2024-Jun 2025 | DECAYED (past 50% mark) | Migrate to embedding v4 + hybrid search |
| Fine-tuned model on customer support | fine-tuning | Mar 2024 | 12-18mo | Mar-Sep 2025 | PAST HALF-LIFE | Test base model equivalence Q2; plan deprecation |
| Data flywheel: 3yr of interaction logs | data-flywheel | Jan 2022 | 24-36mo | Jan-Sep 2025 | STILL AHEAD (20mo in) | Continue collection; no threat in next 12mo |
| 4-agent orchestration for workflow | harness/orch | Oct 2024 | 12-24mo | Oct 2025-Oct 2026 | Stable (6mo in) | Monitor Claude agent roadmap for native equivalents |

---

### Harness Assumption Register

| Harness Component | Model Limitation Assumed | Assumption Test Date | Still Valid? | If Invalid, Simplify To |
|--|--|--|--|--|
| Planner Agent | "Claude can't decompose 50-step tasks without losing coherence" | Apr 2026 | No | Remove planner; test direct planning in task agent |
| Memory Shard Manager | "Claude can't handle 200k token session history efficiently" | Apr 2026 | Yes, but Opus 4.7 pushes to 500k | Raise shard threshold from 100k to 250k tokens |
| Fact-Checker Node | "Claude hallucinates dates in long documents >20k tokens" | Apr 2026 | Partially (dates still 15% error at 20k+) | Keep for >15k docs; remove for <15k; test new embedding-based fact grounding |
| Router Agent | "Claude can't dynamically select the right tool for novel tasks" | Apr 2026 | No | Implement simple confidence-based routing; test single-agent with tools |
| Fallback Cache | "Claude's output is inconsistent for repeated queries" | Apr 2026 | No (deterministic outputs in 4.6+) | Remove fallback cache; simplify to single inference |

---

### Decision Log

**Quarterly Reviews:**
- [Date]: Capability A still ahead; prompt template refresh scheduled
- [Date]: Harness assumption X violated; simplified orchestration
- [Date]: Half-life on advantage Y approaching; renewal plan triggered

---
```

**Usage notes:**
- **Capability Radar:** Update quarterly after testing latest model releases. Flag any commoditization acceleration.
- **Strategy Half-Life:** Review at 50% mark and 100% mark. If past 100% and advantage still holds, extend the estimate (you were conservative). If violated, trigger renewal or retirement.
- **Harness Register:** Update after each major model release. Test each assumption against the new capabilities. If violated, simplify and redeploy engineering.
- **Decision Log:** Brief entries of strategic choices. Useful for post-mortems ("We kept this too long") and future planning ("We nailed the timeline on this one").

This format prevents strategic debt from accruing silently.

## GENERATE THE DELIVERABLE

Use the output generation prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

If this skill connects to downstream skills (e.g., build-or-buy, ai-use-case-readiness), generate the markdown handoff file as well.

## QUALITY GATE

Before you commit to building a custom capability:
- [ ] You've tested the latest model release on this exact task. Documented results.
- [ ] You've predicted the trajectory. (Rough estimate: when does this become commodity?)
- [ ] You've costed both paths: build it vs. wait + migrate.
- [ ] You've identified your switchover trigger. (What change in the model would force a pivot?)
- [ ] You have a user waiting to pay for this *now*, not in 6 months.

## WHEN WRONG

**You see this capability commoditizing faster than expected.**
- Your 8-week feature is obsolete in 3 months.
- Trigger: Model release jump in capability. Competitor ships a model-native version.
- Recovery: You have 2 weeks to pivot to a model-native approach or your feature becomes technical debt.

**You waited, but the capability didn't arrive.**
- You expected GPT-5 to do X. It doesn't. Now you're 12 months behind.
- Trigger: Model release doesn't deliver promised capability.
- Recovery: Build it now (late) or acquire a company that did.

**You built defensible, but the moat collapsed anyway.**
- Your fine-tuned model matched GPT-4 in 2023. GPT-4.5 renders it obsolete in 2024.
- Trigger: Capabilities jump unexpectedly.
- Recovery: You own the data + customer relationships. Migrate your value layer, not your capability layer.

**You prioritized capability over product.**
- You built something technically sophisticated that users don't want.
- Trigger: Your capability is solid, but adoption is 10% of forecast.
- Recovery: Reframe. What product problem does this capability actually solve? Start there.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
