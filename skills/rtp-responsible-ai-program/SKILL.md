---
name: "responsible-ai-program"
description: 'Build or audit a company-wide responsible-AI program that actually functions instead of existing to be seen. Diagnoses the three gaps that make ethics programs fail: nobody truly accountable, no strategy connecting ethics to the business, no budget or people behind it (the MIT Sloan ''3 Gaps'' lens), then designs governance that wires ethics into how products get built (the SHARP system; both explained in plain terms inside). Use when: standing up AI governance, auditing an existing program, translating an ethics risk into a number executives act on. Pairs with: safety-as-moat (the business case), safety-by-design (the technical half), alignment-check (org readiness). Triggers: ''responsible AI'', ''AI governance program'', ''ethics program'', ''SHARP framework'', ''accountability gap'', ''AI ethics by design'
imports: ["safety-as-moat", "safety-by-design", "dual-lens"]
version: v1.5_latest
framework_source: "MIT Sloan Management Review — Öykü Işık & Ankita Goswami, 'The Three Obstacles Slowing Responsible AI', October 2025"
---

# Responsible AI Program

## DEPTH DECISION

**Go deep if:** Building or overhauling an enterprise AI governance program, diagnosing why responsible AI initiatives are failing despite policy documents existing, preparing for board or regulatory scrutiny of AI practices, or embedding ethics into a product development lifecycle.

**Skim to the SHARP checklist if:** You already have a governance program and need a quick health check, or you're coaching a stakeholder on why their "AI ethics committee" isn't working.

**Skip if:** Pre-PMF startup with no external AI risk, internal tool with no customer-facing AI, or context where AI governance is genuinely premature.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions — at minimum: Who is the customer? What problem? What does YES mean saying NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, stakeholder brief?

---

## KEY TERMS (plain language)

- **The 3 gaps** — the accountability, strategy, and resource gaps that make responsible-AI programs fail.
- **SHARP framework** — the skill's system for closing those gaps and hardwiring ethics into product development.
- **Ethical-business risk translation** — expressing an ethics risk as a dollar range (fine + churn + brand) so cost-conscious executives act on it.
- **Checkbox transparency** — treating "the explanation exists" as compliance, without ensuring anyone actually engages it.
- **Inner/outer world lens** — designing your process so it doesn't create the risk (inner world) versus watching whether regulators or press expose it (outer world).
- **Alterability** — whether the person named as accountable can actually change the outcome, by what mechanism, and in what time. Distinct from answerability, and the corpus now treats it as the prior question.
- **Severing mechanism** — a way an independent reporting line stops working while surviving on the org chart. Twelve are known; three leave no trace.
- **Prepared authority** — a stop authority that exists as a name, a job description, and an org chart entry, but has never been tested against a live case. A structural test (does the role exist, does the person know, do they have standing) cannot tell prepared authority apart from authority someone has actually exercised. Only a count of real stops, delays, or forced redesigns can.
- **CDR (Corporate Digital Responsibility)** — the practice of disclosing AI risk to outsiders before you are forced to. This skill's July 2026 sweep found it compounds with regulators and does nothing for customers, which is why it needs two different communication postures, not one.
- **Detection competence** — the ability to tell that something needs stopping. The third leg of stop authority, and the one whose absence is worst.
- **Negotiated artifact** — one the receiving team came back and altered. The opposite of a handed-over artifact, and the difference predicts commitment better than the artifact's quality does.

## THE TRAP

Most organisations build **responsible AI programs that exist to be seen, not to function**.

They create ethics committees that meet quarterly but have no veto power. They publish AI principles that nobody checks before shipping. They hire ethics officers who write policies but aren't in the room when product decisions are made.

The result is three structural gaps that MIT Sloan's research identified in enterprise AI programs:

1. **The Accountability Gap** — When AI causes harm, nobody claims responsibility. The model vendor blames fine-tuning. The fine-tuning team blames the product. The product team blames the business requirement. The business blames market pressure.

2. **The Strategy Gap** — The company has AI initiatives everywhere but no AI governance strategy. Ethics is reactive (we'll add guardrails when something breaks) rather than proactive (ethics reviews are a gate before launch).

3. **The Resource Gap** — Ethics teams are resourced to *write* policies but not to *implement* or *enforce* them. They have influence but not authority. They produce documents but cannot stop a launch.

The hard truth: **These three gaps don't close through awareness campaigns or workshops.** They close through structural change — who owns what, who can stop what, what gets measured.

That's what the SHARP framework is for.

---

## The 3 Gaps Diagnostic

Before prescribing SHARP, diagnose which gaps your organisation actually has.

### Accountability Gap Diagnostic

Ask these questions. If you answer NO to any, the gap exists:

| Question | YES | NO |
|---------|-----|-----|
| Is there a named individual (not a committee) accountable for AI ethics outcomes — with it in their job description? | | |
| When an AI incident occurs, is the escalation path clear within 24 hours? | | |
| Do product teams know whose approval they need before launching a customer-facing AI feature? | | |
| Has anyone been held accountable (positively or negatively) for an AI ethics outcome in the last 12 months? | | |

**Gap severity:** 0 NOs = No gap. 1-2 NOs = Partial gap. 3-4 NOs = Full accountability gap.

### Strategy Gap Diagnostic

| Question | YES | NO |
|---------|-----|-----|
| Does the company have a written AI ethics strategy (not principles — a strategy with goals, timelines, and owners)? | | |
| Are ethics reviews part of the product development process — as a gate, not an audit after launch? | | |
| Does the AI ethics strategy cascade from company values to team-level practices to individual decisions? | | |
| Has leadership made explicit trade-offs about what AI use cases the company will NOT pursue, and why? | | |

**Gap severity:** 0 NOs = No gap. 1-2 NOs = Partial gap. 3-4 NOs = Full strategy gap.

### Resource Gap Diagnostic

| Question | YES | NO |
|---------|-----|-----|
| Does the ethics/AI governance team have authority to delay or block a product launch? | | |
| Do ethics reviewers have technical AI literacy sufficient to evaluate model behavior? | | |
| Is there a dedicated budget for red-teaming, bias auditing, and ethics-related engineering? | | |
| Are ethics reviews resourced proportionally to AI risk level (more review for higher-risk AI)? | | |

**Gap severity:** 0 NOs = No gap. 1-2 NOs = Partial gap. 3-4 NOs = Full resource gap.

---

## What the 3 Gaps Diagnostic Cannot See

The three diagnostics above were built to find accountability that was never assigned. The 2026 corpus describes failures where every question returns YES and the governance still does not work. Run this section after the three gaps, never instead of them.

### The prior question: can the accountable person alter the outcome?

**The rule:** before asking who is accountable, ask whether they can change what happens, by what mechanism, and within what time.

**The case that forces it.** A six-year field study at a German bank, 2019 to 2025 ⚠ (single firm, EU consumer lending, no comparison firm), assigned accountability to named loan officers who could not override the model. Run the Accountability Gap Diagnostic against it. Named individual: yes. Escalation path inside 24 hours: yes. Teams know whose approval they need: yes. Someone held accountable in 12 months: yes. **Four YES answers, and the diagnostic misses the entire failure.**

**The mechanism.** Accountability without alterability is not weak governance. It is a different failure with a different signature, and the diagnostic above was built to detect the absence of an owner. Here the owner was present, named and answerable.

**What the officers did, and why it is worse than silence.** They kept explaining, and the explanations were invented. Applicants were told "weak credit history" in language that did not reflect what the model actually weighted. Silence is detectable. A steady stream of plausible, well-formed, internally consistent explanations reads to every audit in this skill as a functioning process.

**The cheap test, and nobody in the corpus runs it.** In any deployment that holds both, sample delivered explanations against system-generated ones and check whether they match.

**The seniority gradient, which runs opposite to how audits are built.** Fabrication pressure rises with seniority, because a senior person's answerability is public while their alterability is often lower rather than higher. Every audit mechanism in this skill samples downward. Sample upward as well.

**When wrong:** a deployment where named accountability without override authority produced accurate escalation rather than compliance.

### Alterability is necessary and not sufficient

Two further conditions, both from cases where the accountable person could fully alter the outcome and accountability still failed.

- **Be inside the regime you are accountable for.** A holder who can disqualify himself from the regime inverts it rather than weakening it, and that passes every structural audit prescribed here.
- **Have a counterparty, not a parent.** A common parent over two functions in tension removes the artifact rather than the authority. Nothing is left to negotiate when one person can simply decide.

**The one cadence in the corpus that makes a call blocking.** The MedTech 5/20/5 protocol ⚠ (one firm, described qualitatively): five minutes to frame, twenty to debate as equals, five for the accountable person to call it. It works because it is a blocking gate rather than an invitation, and because the twenty-minute segment levels the hierarchy explicitly and then explicitly takes it back. Everything else in this section is a principle. This is something a team can run on Monday.

### Twelve ways an independent reporting line gets cut

The line survives on the org chart in all twelve. Only the first looks like an attack.

| # | Mechanism | What it looks like | Leaves a trace? |
|---|---|---|---|
| 1 | **From below, by prompt** | A profit-maximising instruction in a system prompt suppresses board escalation. Written by someone with no governance remit, in a file no governance process reviews | Prompt file |
| 2 | **From above, by agility** | "Minimum viable governance" prescribes structures that can be introduced, adjusted or retired quickly. A structure retirable quickly is retirable by the person it constrains, and it arrives dressed as a design virtue | Restructure |
| 3 | **From the side, by tooling** | Governance platforms level the expertise a risk review requires. Standing is a function of scarcity, so making the review easy makes the reviewer replaceable | Platform rollout |
| 4 | **From within, by encoding the criterion** | Charter, reporting line, cadence and membership unchanged. The decision criterion moves into a model. The meeting still happens, the minutes still record a decision, and the subject matter is gone | **Nothing** |
| 5 | **From above, by altitude (designed)** | A governance designer promotes the accountable act from the decision to the architecture, on purpose. The answerable person can no longer alter any particular outcome, and it reads on an org chart as strengthened governance | Restructure |
| 6 | **Legitimate termination by protocol** | Disagree and commit ends alterability deliberately, in the open, with the objection recorded first. **Not a pathology** | Stated protocol |
| 7 | **Holder exits the regime** | The holder disqualifies himself, or a common parent over two functions in tension removes the thing there was to negotiate | Varies |
| 8 | **Jurisdictional exit** | The line is never entered, because the actor does not need the institution. Liability shelter substitutes for review, and the actor self-assesses the risk of skipping the assessment | **Nothing, by construction** |
| 9 | **Upward, by promotion** | Nobody designs this one. A leader moves from making the call to designing how calls of that class get made (the analyst-to-integrator move, itself prescribed as career progress), and alterability erodes with no change to title or reporting line | Promotion record |
| 10 | **Visible self-exemption** | The accountable person is seen exempting himself from the rules he enforces on everyone else. Subordinates read the exemption, not the policy, as the actual rule | Usually public |
| 11 | **From above, by structural agility** | "Minimum viable governance" (MVG) trades a measurable term (friction, cycle time) against an unmeasurable one (risk, which its own source says "changes faster than leaders can anticipate"). Optimizing one measurable term against one unmeasurable term collapses onto the measurable one within roughly two quarters, with nobody doing anything wrong. It arrives as a design virtue, not a failure | Restructure, timed to a friction metric |
| 12 | **From the platform, by invisibility** | Controls embedded in the platform itself, such as logging, masking, or filtering, satisfy all four MVG design characteristics with nobody actually able to stop a model. The checklist measures presence of controls, not anyone's standing authority to invoke them | **Nothing** |

**Eleven sharpens two rather than duplicating it.** Two is about power: a structure retirable quickly is retirable by the person it constrains. Eleven is about measurement: balancing one measurable term against one unmeasurable one drifts toward the measurable term on its own, regardless of who holds the power to retire anything. Both describe MVG-style governance; they name two different reasons it erodes.

**Four, eight, and twelve are the ones that matter most, because they are invisible to every question this skill asks.** Four leaves the org chart intact and an audit finds a functioning body. Eight changes nothing inside the institution because the activity was never inside it. Twelve leaves a governance checklist that reads as complete, because completeness of controls is exactly what MVG's four design characteristics measure, not standing authority to invoke them.

**The diagnostic question this skill already asks now carries a second reading.** "How many quarters has this structure stood unchanged, and who can change it without review?" (below, in the second-pass questions) was written for ordinary drift. Structural agility is the same question wearing a design-virtue costume: a body praised for how fast it can restructure itself is a body where the answer to "who can change it without review" is often "whoever it constrains."

*(Eleven and twelve, source: MIT CISR, "minimum viable governance" framework, ◆ company-disclosed, no stated population for its headline figure. The four design characteristics and the friction-versus-risk framing are the source's own; the two-quarter collapse mechanism and the invisibility reading are this corpus's reasoning, not the source's. When wrong for eleven: a self-described "lightweight governance" organization that held or increased measured oversight over four or more quarters against an explicit, independently checkable risk criterion that was not itself a friction, cycle-time, or adoption metric. When wrong for twelve: a platform-embedded control set paired with a named person who has exercised the stop at least once against the platform's own default.)*

**Nine is the one that arrives disguised as success.** Five and nine both cost the person alterability at altitude, but five is chosen by a governance designer above the person, while nine is a side effect of the person's own career path. Nobody is incentivized to flag nine, because the org is busy celebrating the promotion that caused it. The test: for the last three decisions of this class, who could have changed the outcome after the recommendation reached them? If the nominal decision-maker could not, alterability moved down or sideways when the title moved up.

**When the loss was chosen rather than accidental, name it out loud.** A CFO who becomes CEO and delegates the finance function is choosing to lose alterability there, and that can be the right call. What keeps it governance instead of drift is stating it: transfer answerability explicitly to whoever kept control of the mechanism, rather than letting the org assume the new title still carries the old power to alter outcomes.

*(Nine, source: a Watkins-adjacent podcast on the enterprise-leadership transition from analyst to integrator, ⚠ practitioner framework, no measured outcomes. When wrong: a leader who moved up and kept a standing veto over the specific decisions that matter, exercised at least once. That is six wearing an altitude costume, not nine.)*

**Ten sharpens seven rather than repeating it.** Seven already named the holder disqualifying himself. Ten's addition is that the exemption has to be seen by the people the rule governs to sever the line. The clean case is Credit Suisse under João Horta-Osório: the CEO's own conduct fell short of the compliance standard he was enforcing, the shortfall became visible to the organization, and the standard died in every subordinate's judgment at that moment regardless of what the policy manual still said. This bounds the "alterability is necessary and not sufficient" finding below: alterability plus a witnessed self-exemption still produces the failure.

*(Ten, source: HBR, on modeling organizational transformation, citing the Credit Suisse/Horta-Osório case, ⚠ single-company case, publicly reported, not independently verified beyond published reporting. When wrong: a shortfall corrected privately and never visible to the people the rule governed. That is undetected hypocrisy, a different failure, because it never reaches the subordinates who would have to stop believing the rule.)*

**Six is the one to get right in the other direction.** Not every loss of alterability is a severing. What separates a legitimate termination from a cut is whether the objection was captured before the commitment.

**Two questions to run as a second pass.** These are not extra rows in the Accountability Gap table above, whose scoring is calibrated to four questions. Run them separately, and treat a single NO as disqualifying, because each one describes a line that is already cut.

- What does this body still argue about, and has that changed? A governance body that has stopped disagreeing has usually stopped governing.
- How many quarters has this structure stood unchanged, and who can change it without review? This skill has always asked who reports to whom. It has never asked how hard the answer is to alter.

**When wrong:** an organisation whose escalation path held through a system-prompt rewrite, a governance restructure, and a platform rollout.

### Is stop authority real, or just prepared?

**The rule:** a structural test cannot tell a real stop authority from a paper one. Only a count of what actually got stopped can. Both instruments below test whether stated authority is real, and they belong beside the mechanisms table above for the same reason: severing leaves the org chart intact, and so does an authority that was never severed because it was never held.

**The three-question test.** Ask of any named accountable role: does this person have authority to stop a model, do they know it is their job, and do they have standing to exercise it against someone else's roadmap. A practitioner argument built from an Adobe federated-governance example uses this test to separate "infrastructure for visibility" from "infrastructure for action."

**Why the test alone is not enough.** All three questions can be answered yes by preparation: a name assigned, a job description written, an org chart entry added, all inside a week. Preparation and years of real held ground look identical to this test, because it asks about the role rather than about what the role has done.

**The missing fourth question.** What does it personally cost this person to stop a deployment, and who decides their next promotion? The source names this cost in prose and then drops it from its own three-question test. It sharpens the two-sided exposure test already in this skill (what the owner gains if the agent works, what the owner loses if it fails, in "Stop authority is three legs, not one" below): the fourth question asks about the cost of a specific act of stopping, not just the standing incentive structure around the role.

**What actually settles it is a count, not a test.** "The cheapest test in this skill" below turns the three-question test's blind spot into a protocol: count actual stops, delays, or forced redesigns over the last eight quarters, and read a zero against whether there was ever a live case to stop.

**When wrong (three-question test and fourth question):** a role where all three questions score yes and the accountable person carries no promotion or compensation exposure from the people whose roadmap they would stop, because the incentive failure the fourth question is built to catch is simply absent.

*(Source: Joseph Wallace, Adobe, HBR/practitioner piece, ⚠ practitioner position paper, no study, no survey. Adobe's own federated-governance example in the piece reports no outcome and no stops counted. The fourth question, the sharpening against the two-sided exposure test, and the stop-count protocol are this corpus's addition.)*

### Stop authority is three legs, not one

The Resource Gap Diagnostic asks whether the governance team can delay or block a launch. That is one leg of three.

1. **Platform capability.** The technical ability to stop or change model behaviour.
2. **Stop authority.** The organisational authority to stop, independent of the shipping org.
3. **Detection competence.** The ability to tell that something needs stopping.

**Missing leg three is strictly worse than missing leg two, and this is the finding to carry into a room.** No authority at all leaves a decision visibly ungoverned. Authority without detection produces a decision that looks governed and is not, because a governor who cannot detect still signs off, and **the sign-off launders the decision as reviewed.**

The mechanism is specific and uncomfortable. Governance output is document work, which is exactly what a governance platform accelerates, and it is an opinion nobody re-derives.

**The fourth finding is a structural limit, not a maturity gap.** A 272-expert study ⚠ (expert elicitation, no deployment outcomes) shows the three legs are distributed across organisational boundaries, and the boundary is where the authority stops. An enterprise can build platform capability and detection competence and **cannot obtain stop authority over a rented frontier model's behaviour.** No amount of internal governance maturity crosses a firm boundary.

**So model routing is a governance decision before it is a reliability one.** Switching capability is the only stop authority a deployer actually holds over a rented model. Pairs with `tool-architecture`.

**When wrong:** an enterprise demonstrating effective stop authority over a rented frontier model's behaviour, exercised against the provider's commercial preference, without switching providers.

**A checklist can enumerate everything except the one entry that would let it stop itself.** An MIT Sloan CISR webinar recap lists six things a company must name an owner for when deploying an agent: updates, training, token use, embedding, bias control, regulatory compliance. Every item answers "what needs maintaining," and that is exactly why stop-authority never appears. A list built by asking what needs upkeep will not surface who may turn the thing off. Add it as a required seventh item.

**The two-sided exposure test for any named owner.** Ask what the owner gains if the agent works and what the owner loses if it fails. An owner with something to gain and nothing to lose is not accountable, whatever the checklist says.

*(Source: MIT Sloan CISR webinar recap, ⚠ prescriptive checklist, not a research finding. Cite it as a tool to use, not evidence to believe. When wrong: an owner named for a low-stakes agent where a wrong stop decision costs little. The exposure test scales with the harm at stake, the same way the checkbox-transparency exemption above does.)*

**Independence and detection competence often move in opposite directions, and there is no clean fix.** A contested MIT Media Lab preprint (n=54, arXiv, disputed) argues the person best placed to spot a plausible-but-false AI output is usually the reviewer with the least organizational distance from the work, because detection competence tracks proximity to the work. A governance design that maximizes reviewer independence for compliance reasons can be quietly minimizing the one thing that lets a review catch anything. Name this trade-off when you design a review layer. Do not expect to resolve it: the choice is which failure mode you accept, a captured reviewer or a blind one.

*(Source: podcast citing a contested MIT Media Lab preprint, ⚠ small sample, contested, not a stable finding. When wrong: a review layer where the independent reviewer keeps an independent channel back into the work, closing the distance without closing the independence. Rare, and worth building toward.)*

### An artifact nobody negotiated

**The rule:** commitment comes from negotiating the artifact, not from its completeness. Volume is not the variable. A dictated artifact fails at any size, and a co-created one works at any size.

An e-commerce company's RACI ran to thousands of correct rows and was opened once ⚠ (two cases, one article). A healthcare firm reproduced the same failure across a handful of direct reports.

**The instrument is a single observable, and it is available before any adoption metric moves: did the receiving team modify the artifact?** Arrived and adopted unchanged means it was handed over. Came back altered means it was negotiated. That fires early enough to be a leading indicator rather than a post-mortem.

**The sizing rule tells you where to spend the expensive co-creation time.** The negotiation premium rises with the unfalsifiability of the decision. Where a decision can be checked against an outcome, a dictated artifact survives because reality arbitrates. Where it cannot, negotiation is the only thing producing commitment. Most artifacts this skill produces sit at the unfalsifiable end.

This generalises past decision rights to anything a team is handed rather than builds: an eval rubric, a definition of done, an autonomy level, a tracking plan.

**What it costs SHARP.** An independent line policing a process nobody chose produces compliance without commitment, and the two look identical on an audit and behave differently under pressure. The sequencing rule says S before everything else. Add one condition: whatever S produces has to come back altered before H can hold.

**When wrong:** a large, dictated, comprehensive governance artifact that changed behaviour with no co-creation step. One case kills this.

---

### The cheapest test in this skill: what has this body actually stopped?

One question, asked of any AI governance board, ethics committee, review council or steering group:

**"What has this body stopped, blocked or materially changed in the last twelve months? Name it."**

- **A specific answer** means a real control. Ask what happened next, because a body that stopped something and was overruled has a different problem.
- **"It doesn't work like that"** means documentation. So does "it raises areas for the team to investigate as work progresses," and so does any answer that describes influence rather than an event.

**Why this beats a structural audit.** Charters, reporting lines and meeting cadences are all things a body can have while stopping nothing. A stop is an event, it leaves a trace, and people remember it. This question takes ten seconds and it is more informative than a fifty-page terms-of-reference review.

**The longer version of the same question, as a protocol.** For a fuller audit than the twelve-month spot check, count actual stops, delays or forced redesigns made over sponsor objections across the last eight quarters. A zero is ambiguous, not reassuring, on its own; interpret it against a second signal, whether there was ever a live case to stop in that window. A body with no live case in eight quarters has not been tested. A body with three live cases and zero stops has been tested and failed.

**A Goodhart warning: use this sparingly, never as a KPI.** The moment stop-count is measured and reported on a recurring basis, teams learn to route contested decisions around the body being counted, and the function can be quietly dissolved once it starts producing an inconvenient number. Run the count as a diagnostic when you need to know whether a body is real. Do not put it on a dashboard.

**When wrong:** a documented case of a governance function whose stop-count was tracked openly for multiple years without producing avoidance behavior from the teams it oversees. This corpus does not currently have one.

**A named position you will hear quoted, and the reason it is wrong.** A memorable framing doing the rounds asks: *"Is your governance more the steering wheel or is it more the brakes?"* Steering is presented as the mature answer and brakes as the immature one.

**The framing designs the brake out of the system, and it does it in a single word.** The clearest published statement of it, offered approvingly about a healthcare review process: *"Critically, the risk questions don't stop progress; rather, they highlight areas that [the organization] needs to investigate as it makes progress."*

Three things are wrong with that:

1. **A steering wheel with no brake does not steer.** It changes direction at whatever speed the vehicle already has. The choice was never between the two.
2. **The word "critically" marks the removal of stop authority as the feature.** That is the sentence to quote back, because it is the argument stated plainly by someone who thinks it is a strength.
3. **The review process it describes may still be excellent.** Three staged reviews before development, before pilot and before scale, plus periodic re-checks, is a good structure. **The structure is not the question. The authority is.** Everything in that structure survives the addition of a genuine stop, so nothing is gained by removing it.

**What to say when the line is quoted at you.** Agree that governance should shape work early rather than only judging it late, then ask the twelve-month question. The framing and the answer are independent, and the answer is the one that tells you what you are dealing with.

*(Source: MIT SMR, Westerman, "6 questions to guide your AI strategy," 3 Aug 2026 — ◆ reported examples, no measurement anywhere in the article. The steering-and-brakes framing and the "don't stop progress" line are quoted there approvingly; the critique is this corpus's. Note also that the article's only statistic is broken in a way worth knowing about, and it is carried as a teaching case in `rtp-trendslop-check`.)*

### Safety compounds at the regulator, is hygiene at the customer

**The rule:** disclosure to a regulator and disclosure to a customer are not the same communication problem. The article most cited for "responsible AI drives growth" argues against its own headline once you check its own evidence.

**What the evidence in that piece actually shows.** Every well-demonstrated case is risk reduction at the regulator: Amazon's $2.5 billion FTC settlement ✅, Apitor's suspended $500,000 judgment ✅. Early, loud, auditable disclosure to a regulator builds durable regulatory latitude, the kind that shows up later as a lighter consent decree or a shorter investigation. Every "customer loyalty" case in the same piece either has no AI attached to it, or is the authors' own admitted revenue-negative "Sacrifice" quadrant: a company that spent on visible safety and lost money doing it. Safety compounds where the audience is a regulator. At the customer it is a hygiene factor: nobody buys because a product is safe, and everyone leaves the moment it fails, which is the hygiene-factor signature, not the driver signature.

**Why this changes what you say, not just how much.** A trust campaign aimed at customers raises the salience of a risk they were not previously pricing. Telling a customer "we take your data seriously" invites the question of why that needed saying. The same disclosure aimed at a regulator does the opposite: it is exactly the behavior a regulator wants to see, logged before an incident rather than produced in response to one.

**What follows:** publish specifics to regulators, ship reliability quietly to customers. These need opposite communication postures, not one responsible-AI messaging strategy stretched across both audiences.

**The three-stage playbook, from the same piece.** Registry (an inventory of AI systems and their risk class) feeds design-time oversight (review at build time, not after ship), which feeds external signal (the disclosure itself, timed and worded for the regulator audience). Skip the registry and design-time oversight has no reliable inventory to check against. Skip design-time oversight and the external signal describes controls that don't actually run.

**The accountability-selection rule, also from the same piece.** Match the accountability mechanism to how the harm becomes knowable. Reporting-line accountability (a named person, an escalation path, a sign-off) for harm that is foreseeable in advance. Compensation-alignment (bonus and equity tied to the outcome) for harm attributable only after the fact, once the pattern is visible in hindsight. Published non-negotiables (a public commitment the company binds itself to) for neither case: harm too diffuse or too slow-moving for a named owner or a compensation formula to track.

**A concrete failure mode from the same note.** Amazon's Kiro coding agent caused a 13-hour AWS Cost Explorer outage in China ⚠ (single incident, reported). The cause was not bad permission design. An engineer's elevated human credentials were inherited by the agent running inside that engineer's session, which bypassed a standing two-person approval requirement nobody had disabled. An agent executing inside a human's session inherits that human's permission set by default, and no policy written for the agent's own identity reaches a decision made under someone else's. **The structural point:** minimum-per-task permissioning for an agent is unenforceable without a separate machine identity for that agent to hold permissions under. This is the platform-capability leg from "Stop authority is three legs, not one" above, failing for a reason no amount of stop-authority or detection-competence design would have caught.

**When wrong:** a company whose customers named a safety disclosure, specifically, as their reason for staying. That would be a customer-side compounding case, and this corpus does not currently have one.

*(Source: HBR, on responsible AI and growth. Mixed tier: the FTC and Apitor figures are ✅ from primary enforcement actions; the "Sacrifice" quadrant and the CDR three-stage model are the authors' own framework, ⚠ practitioner argument built on the article's own case selection. The Kiro incident is ⚠, a single reported incident, from the same note. Pairs with `safety-as-moat` for the commercial-positioning half of this finding.)*

## The SHARP Framework — Closing the Gaps

> **Attribution:** SHARP was developed by Öykü Işık (Professor at IMD) and Ankita Goswami (external researcher at IMD), published in MIT Sloan Management Review, October 2025. The full framework is titled "The Three Obstacles Slowing Responsible AI." Cite as: Işık, Ö. and Goswami, A. (2025). "The Three Obstacles Slowing Responsible AI." *MIT Sloan Management Review*, 67205.

SHARP is an implementation framework for responsible AI governance. Each letter maps to a structural change, not a workshop. The five strategies are not sequential steps or universal templates — they reflect varied ways organisations reconfigure their structures, incentives, and routines to make responsible AI operational.

**The five strategies:**
- **S** — Structure ownership at the project level
- **H** — Hardwire ethics into everyday procedures
- **A** — Align ethical risk with business risk
- **R** — Reward responsible behaviour
- **P** — Practice ethical judgment, not just compliance

### S — Structure Ownership (at the project level)

**What it means:** Assign a specific individual — not a committee, not a team, not a working group — as personally accountable for AI ethics outcomes. Committees diffuse accountability. One named person concentrates it.

**The problem with committees:** The Accountability Gap exists precisely because committees give everyone cover. When something goes wrong, every committee member can say "I raised it." Nobody can say "I stopped it." A committee can advise. It cannot be held accountable.

**What to do:**
- Designate a Chief AI Ethics Officer (or embed this in an existing role: CPTO, CDO) with explicit AI governance authority in their job description
- Define their authority clearly: Can they delay a launch? (Yes.) Can they kill a feature? (Yes, with CEO agreement.) What requires their sign-off?
- Create a tiered accountability map:
  - Tier 1 (product team): Responsible for completing ethics self-assessment before every AI feature launch
  - Tier 2 (ethics function): Responsible for reviewing high-risk AI (defined by your risk matrix) before launch
  - Tier 3 (CAEO/leadership): Responsible for enterprise AI risk posture and regulatory compliance

**What good looks like:** Every AI incident has a clear owner within 1 hour. Every AI launch has a documented approval trail. Accountability is traceable, not diffuse.

**Where this breaks:**
- Ownership is assigned but authority is not. Owner can flag issues but cannot act on them.
- Owner lacks technical AI literacy and must defer to engineering on every substantive question.
- Accountability map is documented but not actually used when incidents occur.

---

### H — Hardwire Ethics into Everyday Procedures

**What it means:** Embed ethics into everyday product development procedures — not as a separate audit layer bolted on at the end. Ethics steps must feel like "something we do," not "something someone else makes us do." (Direct quote from an engineering lead at a health care analytics company, MIT Sloan research.)

The word "everyday" is intentional. This is not about quarterly ethics reviews. It is about ethics showing up in sprint templates, pull request checklists, design reviews, and deployment gates — the daily rhythm of building.

**The problem with post-hoc ethics:** Most enterprise AI ethics programs are audits: they review AI systems after they're built, deployed, and have users. By then, the cost of change is high, teams are defensive, and "responsible AI" becomes "document why we're fine."

**Ethics as a gate looks like this:**

```
Discovery                Build              Pre-Launch         Post-Launch
    │                      │                    │                  │
    ▼                      ▼                    ▼                  ▼
AI Use Case           Technical          Ethics Review       Ongoing
Risk Assessment       Review             (MANDATORY         Monitoring
(self-assessment      (data, model,      gate — cannot      (monthly
by product team)      architecture)      ship without       review of
                                         sign-off)          live behavior)
```

**The AI Use Case Risk Assessment** — what product teams complete before development begins:

| Dimension | Low Risk | Medium Risk | High Risk |
|-----------|----------|-------------|-----------|
| Who does it affect? | Internal users only | External users, limited scope | Broad public; vulnerable populations |
| What decisions does it influence? | Operational efficiency | Customer experience | Access, safety, legal rights |
| What if it fails? | Inconvenience | Financial loss, reputational damage | Physical harm, discrimination, legal liability |
| Is it human-in-the-loop? | Human reviews every output | Human reviews exceptions | Fully automated decisions |
| Is training data documented? | Fully documented | Partially documented | Unknown provenance |

**Scoring:** Mostly Low → Self-certified. Any Medium → Ethics team review before launch. Any High → CAEO sign-off required before development begins, not just before launch.

**What hardwiring requires:**
- Ethics checkpoints appear in every sprint template, PRD template, and launch checklist
- Product teams cannot mark a launch-ready without completing the risk assessment
- High-risk AI features require ethics sign-off in the same way they require legal and security sign-off

**Where this breaks:**
- The gate exists on paper but isn't enforced. Teams mark "reviewed" without actual review.
- Risk assessments are filled out to pass, not to discover risk.
- Ethics reviewers are overloaded and rubber-stamp to keep pipelines moving.

---

### A — Align Ethical and Business Risk

**What it means:** Frame every ethical risk as a business risk — in the language executives already use — so governance decisions get the same attention as revenue decisions.

**The problem with ethics-only framing:** When an ethics concern is presented as a values question, executives weigh it against quarterly targets and values lose. When the same concern is presented as business risk with a dollar estimate, it gets a line item and an owner.

**The translation table:**

| Ethical Risk | Business Risk Translation | Quantification Approach |
|---|---|---|
| Algorithmic bias in credit scoring | Regulatory fine (CFPB enforcement) + class action liability + brand damage in affected demographic | Estimate fine range from precedent cases + NPS impact in affected segment |
| AI-generated content without disclosure | FTC enforcement risk + user trust collapse when discovered | FTC fine precedents + churn model if trust breaks |
| Data used to train model without consent | GDPR/CCPA fine + contract breach + reputational exposure | Maximum fine calculation + estimated customer defection rate |
| Hiring AI that screens out protected classes | EEOC investigation + lawsuit + brand damage in talent market | Legal cost estimates + reduced talent pool quality |
| Medical AI that fails silently | FDA enforcement (if classified as medical device) + malpractice liability + patient harm | Regulatory timeline + insurance/legal estimate |

**The alignment protocol:**
1. For every high/medium risk AI use case, complete the Ethical-Business Risk Translation
2. Present ethics recommendations with the dollar risk estimate, not just the values argument
3. Frame governance investment as risk mitigation, not cost: "Ethics review costs $50K/year. One CFPB enforcement action costs $500K–$50M."

**The Inner/Outer World lens:** Ethical risk lives in both worlds. The *inner world* (what you can control) is whether your process generates the risk. The *outer world* (what you adapt to) is whether regulators, users, or press expose it. Responsible AI programs manage both — they don't just watch the outer world; they design the inner world to not create the risk in the first place.

**The outer world is not one audience.** Regulators and customers sit on the same "outer world" side of this lens and respond to disclosure in opposite ways: see "Safety compounds at the regulator, is hygiene at the customer" above for the evidence and the two communication postures it requires.

**Where this breaks:**
- Translation is done once for a presentation but not embedded into ongoing risk management
- Estimates are too vague to act on ("reputational damage" without a dollar range)
- Business risk framing works for cost-conscious executives but alienates values-driven stakeholders who feel the ethics are being commodified

**Checkbox transparency — "make the explanation available" is not a control.** This is THE TRAP ("programs that exist to be seen, not to function") in its most common concrete form. Explainability is often logged as a compliance checkbox: the explanation exists, the box is ticked, the regulator is satisfied. The evidence says that's false comfort. When looking at the reasoning might cost the viewer — money or moral exposure — people decline to look even when it's free and one click away, and a bias-disclosure prompt can make them look *less*. For any decision with real bias or compliance stakes (credit, hiring, medical, judicial), voluntary explainability predictably goes unused by exactly the people whose incentives most need it used. **The governance constraint:** require *engagement* with the explanation (mandatory, logged review), not just its *availability* — which is closer to what the CFPB already demands (the credit-scoring row above): "specific" and "accurate" reasons *used in the decision*, not a rationale sitting unread in a log. **Why it matters:** the same liability this register prices (CFPB enforcement, GDPR fines) is not neutralized by an explanation nobody reads — "explainability shipped" and "explainability used" are different lines in the program. **When wrong:** low-stakes, low-bias-risk decisions don't warrant a mandatory review step — the checkbox is proportionate where the harm is trivial. *(Source: "Employees Aren't Questioning AI Advice Enough," Chan / Rand, HBR, 24 Jun 2026 — ◆ study, n=2,512; CFPB circular 2023-03 + GDPR / EU AI Act ✅. Mechanism-level fix in `rtp-judgment-guard`, motivated non-inquiry.)*

**Approval rate and time — the same trap, worn as a percentage.** "Seek human approval for consequential decisions" is the most common accountability capability firms report having for agent deployments, per an MIT Sloan CISR survey (n=132, company-disclosed ◆). It is also the most audit-passing form of accountability that can still be empty in practice, for the same reason checkbox transparency is empty above: the capability exists on paper, and nobody checks whether anyone is using it. **The test:** measure approval rate and median time-to-approval together, never separately. An approval rate above roughly 95%, completed in under 60 seconds, is a rubber-stamp signature rather than a review signature, even though it reports as a functioning accountability capability on every audit this skill describes. **When wrong:** a high-volume, genuinely low-risk approval queue where 60 seconds is real review, because the decision is simple and the reviewer is trained on exactly that pattern. Read the rate-and-time test against the risk tier from the AI Use Case Risk Assessment above before calling anything rubber-stamping.

*(Source: MIT Sloan CISR digital-colleagues survey, n=132, ◆ company-disclosed.)*

---

### R — Reward Responsible Behaviour

**What it means:** Incentive structures must reward ethical decision-making, not just speed and output. If teams are measured only on shipping velocity, ethics reviews will always feel like friction.

**The problem with misaligned incentives:** You can write all the responsible AI principles you want. If the team that skips the ethics review ships a week faster and gets praised for it, the message is clear: ethics is optional when it's inconvenient.

**What rewarding responsible behaviour looks like:**

| Practice | What to Add or Change |
|---------|----------------------|
| Performance reviews | Add ethics hygiene metric: "Completed required AI risk assessments without prompting." Weight it alongside delivery metrics. |
| Launch retrospectives | Standard retrospective question: "Did our ethics review process catch anything we would have missed?" Make findings visible to leadership. |
| Incident response | When a team self-reports an AI risk before it causes harm, treat it as a positive signal — document it as a near-miss prevented, not a failure. |
| Recognition | Publicly recognise teams that voluntarily deepened ethics review beyond the minimum. |
| Promotion criteria | For senior PMs and engineers, include demonstrated ethics judgment as a criterion. |

**What NOT to do:**
- Don't create a separate "ethics bonus" — it signals ethics is add-on, not core
- Don't measure ethics compliance only through audits — that creates paperwork compliance, not judgment
- Don't penalise teams for raising concerns that delay launches if the concern was legitimate — you'll get silence next time

**The judgment muscle:** Reward structures build habits. You're not just rewarding individual decisions — you're building the organisational muscle for ethical judgment at scale. Teams that regularly practice ethics reasoning make better decisions faster over time. Teams that treat ethics as a checklist never develop the judgment.

---

### P — Practice Ethical Judgment, Not Just Compliance

**What it means:** The goal is not compliance — it is building people's capacity to make ethical judgments. Few processes can entirely replace the need for human judgment, especially in contexts where ethical tensions are subtle or evolving. Checklists tell you what to check. Practice builds the ability to handle what isn't on the checklist.

**The compliance trap:** A team trained only on compliance policies freezes when they face a genuinely novel situation. A team that has practiced judgment can reason through novel cases because they've built the muscle — they've done it before in a low-stakes setting.

The MIT Sloan research found that organisations overly reliant on AI-enabled decision-making were at particular risk: without intentional reinforcement of ethical reasoning through practice, even well-designed systems can degrade individual competence over time. People become passive recipients of system suggestions rather than active moral agents.

**The problem with rules-only ethics:** Rules handle known cases. AI creates novel cases that existing rules don't cover. Teams that only know the rules freeze when they face something new. Teams that have practised judgment can reason through novel cases.

**The Practice Protocol:**

**Monthly Case Study Reviews (Team Level)**
- Each team reviews one real-world AI ethics case (internal near-miss or external public incident) per month
- Discussion format: What happened? What was the ethical failure? What structural change would have prevented it? What would we do differently in our context?
- Time: 30 minutes. No slides. Discussion only.
- Outcome: 1 documented learning per session, added to team retrospective

**Quarterly Tabletop Simulations (Cross-Functional)**
- A facilitated scenario: "Our AI system [specific scenario] has just been reported by a journalist. It's 6 PM Friday."
- Participants: Product, Engineering, Legal, Comms, Ethics, and one senior business leader
- The exercise: Work through the first 24 hours. Who calls who? What gets checked? What gets communicated to users? What gets escalated to the board?
- Outcome: Updated incident response playbook + revealed gaps in escalation paths

**Annual Responsible AI Review (Executive Level)**
- Review: AI portfolio risk map, incidents from the year, near-misses, regulatory changes on the horizon
- Decision point: Any AI use cases to sunset, restrict, or redesign based on year's learning?
- Output: Updated enterprise AI ethics strategy for following year

**Where this breaks:**
- Simulations are one-time events, not recurring practice
- Case studies are too generic (Harvard case studies about other companies) rather than grounded in the team's actual AI systems
- Senior leaders attend the annual review but aren't in the monthly practices — judgment builds from the bottom up, not just from strategy documents

---

## The SHARP Self-Assessment

Score each letter 0-2 and identify your weakest area.

| Letter | What you're assessing | Score (0 = not present, 1 = partial, 2 = fully implemented) |
|--------|----------------------|-------------------------------------------------------------|
| **S** — Structure | Is there a named individual with authority and accountability for AI ethics? | |
| **H** — Hardwire | Are ethics reviews a mandatory gate before launch, not an optional audit? | |
| **A** — Align | Are ethical risks translated into business risk language with estimates? | |
| **R** — Reward | Do incentive structures reward ethical decision-making, not just speed? | |
| **P** — Practice | Do teams regularly practice ethical judgment through case studies and simulations? | |

**Scoring:**
- 8-10: Mature program. Focus on deepening, not building.
- 5-7: Developing program. Address the lowest-scoring letter first.
- 3-4: Early-stage program. Start with S (structure) — without ownership, the other letters won't hold.
- 0-2: Program doesn't exist in functional form. Begin with the 3 Gaps Diagnostic before SHARP.

**The sequencing rule:** S before everything else. You cannot hardwire (H) ethics reviews without someone to enforce them. You cannot align (A) risk without someone accountable for the assessment. You cannot reward (R) without someone defining what responsible behavior looks like. You cannot practise (P) without someone designing the exercises. SHARP is sequential, not simultaneous.

---

## Connecting to the Broader Safety Ecosystem

This skill pairs with:

- **Safety-as-Moat** — When your Responsible AI Program creates enterprise switching costs through demonstrably superior governance posture
- **Safety-by-Design** — The technical implementation layer; Responsible AI Program defines the governance; Safety-by-Design encodes it into the product architecture

**The layered view:**

```
Responsible AI Program (SHARP)          ← Organisational governance layer
        │
        ▼
Safety-by-Design (4-Layer Model)        ← Technical architecture layer
        │
        ▼
Safety-as-Moat (Enterprise Positioning) ← Commercial differentiation layer
```

Most organisations get the layers backwards — they try to build a safety moat before they have a functional governance program. The result is safety theater: impressive external positioning, hollow internal practice.

---

## OUTPUT FORMAT

```
## Responsible AI Program Assessment: [Organisation/Product]

### 3 Gaps Diagnosis
| Gap | Severity | Key Evidence |
|-----|----------|-------------|
| Accountability Gap | [None/Partial/Full] | [What's missing] |
| Strategy Gap | [None/Partial/Full] | [What's missing] |
| Resource Gap | [None/Partial/Full] | [What's missing] |

### SHARP Assessment
| Letter | Score (0-2) | Key Gap | Recommended Action |
|--------|------------|---------|-------------------|
| S — Structure | | | |
| H — Hardwire | | | |
| A — Align | | | |
| R — Reward | | | |
| P — Practice | | | |
| **Total** | **/10** | | |

### Priority Actions (Sequenced)
1. [Highest-leverage change — always start with lowest SHARP score]
2. [Second priority]
3. [Third priority]

### Business Risk Translation
[Top 2-3 ethical risks translated into business risk language with estimated financial exposure]

### 90-Day Implementation Plan
| Week | Action | Owner | Definition of Done |
|------|--------|-------|-------------------|
```

---

## WHEN WRONG

This skill gives bad advice if:
- **Pre-PMF with no external exposure:** Building SHARP before you have product-market fit is premature governance. Ship, learn, then build the program as AI risk materialises.
- **Regulation is the primary driver (not values):** If the goal is compliance theater for regulators, SHARP will feel like overkill. But if that's the goal, name it — compliance theater is a conscious business choice.
- **The organisation has no actual AI in production:** Responsible AI programs for hypothetical future AI use cases waste governance resources better spent when AI is real.
- **Leadership is performatively committed:** If the CEO wants a "responsible AI program" for press releases but won't give the function any authority, SHARP won't work — no enforcement mechanism. Name this explicitly rather than designing a program that fails.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

---

*Version 1.5 — 29 AUG 2026 (footer was last synced at 1.0, 5 APR 2026; frontmatter is the version of record between footer updates)*
*Framework Source: MIT Sloan Management Review — Responsible AI Research (3 Gaps + SHARP)*
*Part of: AI PM Skills / safety-and-trust layer*
