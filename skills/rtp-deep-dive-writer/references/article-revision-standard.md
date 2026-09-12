# Article Revision Research and Editorial Standard

**Owner:** Raviteja Palanki  
**Version:** 1.0  
**Created:** 29 August 2026  
**Applies to:** AI Evals, AI PM OS, Agentic Systems, Harness Engineering, and future article series

---

## 1. Purpose

This document defines the standard to follow whenever an existing article is researched, updated, or rewritten.

The goal is not to make an article look newer. The goal is to make it more accurate, more useful, easier to understand, and more valuable to a practitioner making a real decision.

A revision is successful only when it improves at least one of these:

- The reader’s understanding of the problem.
- The quality of a product or business decision.
- The accuracy of an existing claim.
- The clarity of the article’s central argument.
- The usefulness of the article in real work.
- The connection between the article and the rest of the series.

Fresh information that changes none of these should not be added.

---

## 2. Core Principle

Every revision must follow this chain:

> **Evidence → mechanism → product decision → practical action → limitation**

### Evidence

What new fact, case, paper, product change, incident, or operating pattern has appeared?

### Mechanism

Why did the observed result happen? What caused it?

### Product decision

What should a product manager, engineer, leader, buyer, or operator decide differently?

### Practical action

What can the reader do in a meeting, PRD, evaluation, architecture review, launch review, or vendor discussion?

### Limitation

What does the evidence not prove? Where could the insight fail to transfer?

A revision that stops at evidence is a news update. A revision that reaches action becomes practitioner guidance.

---

## 3. Revision Philosophy

### 3.1 Fresh does not mean useful

Recent information should be prioritised, but recency is not evidence quality.

Use recent information when it:

- Corrects an important belief.
- Changes a product decision.
- Reveals a previously hidden failure mechanism.
- Introduces a material regulation or standard.
- Changes pricing or product economics.
- Provides a strong real-world case.
- Supplies better evidence for an existing thesis.

Do not include information merely because it is:

- Trending on X or LinkedIn.
- A new product launch.
- A funding announcement.
- A vendor ranking.
- A dramatic market forecast.
- A popular but weakly sourced statistic.
- A new framework with no clear decision value.

Use the newest reliable evidence, not simply the newest information.

### 3.2 Research broadly, verify narrowly

Social platforms and newsletters are discovery tools. They are not automatically final sources.

Use the following research chain:

> Social post or secondary article → original source → methodology → limitations → contradictory evidence → product interpretation

Prefer:

- Original paper over a thread describing the paper.
- Benchmark repository over a leaderboard screenshot.
- Regulator over a compliance vendor.
- Official pricing documentation over a pricing opinion.
- Technical incident report over a dramatic summary.
- Specification and release history over an ecosystem prediction.
- First-party product documentation over a comparison blog.

A secondary source may be used when it provides valuable interpretation, but it must not inherit authority it has not earned.

### 3.3 A case is not a law

A real example can make an article stronger without becoming a universal rule.

Use this pattern:

> “This case demonstrates X. It does not establish Y.”

Examples:

- A benchmark exploit shows that an evaluation system can be manipulated. It does not show that every benchmark is broken.
- An expensive evaluation run shows that eval costs can become material. It does not establish a standard budget.
- A simulation benchmark shows how physical systems can be evaluated. It does not prove real-world safety.
- A seat-plus-credit product shows that AI economics can exceed seat economics. It does not prove seats have disappeared.
- Outcome-priced support shows where outcome pricing can work. It does not prove every business workflow can be priced by outcome.

### 3.4 Contradiction searches are mandatory

The more useful or exciting a claim appears, the harder the research should try to disprove it.

For every important claim, search for:

- Correction.
- Delay.
- Withdrawal.
- Criticism.
- Limitation.
- Replication.
- Contamination.
- Methodology.
- Independent analysis.
- Updated official guidance.
- Exceptions and scope.

The purpose is not to manufacture false balance. The purpose is to test whether the claim survives opposing evidence.

### 3.5 Numbers must retain their conditions

Do not publish a number without understanding where it came from.

For each number, record:

1. Original source.
2. Publication date.
3. What was measured.
4. Models, products, or organisations involved.
5. Sample size or number of runs.
6. Evaluation method.
7. Assumptions.
8. Whether the number was measured, estimated, projected, or self-reported.
9. Conditions under which it may not transfer.
10. Whether a fresher correction exists.

If these details cannot be found:

- Use the number only as a clearly attributed example.
- Label it as directional.
- Or remove it.

Never turn a vendor benchmark, practitioner rule of thumb, or one-company result into a universal threshold.

---

## 4. Source Quality Framework

Classify every source before using it.

### Verified primary

Examples:

- Peer-reviewed paper.
- Formal technical report.
- Regulator announcement.
- Official specification.
- Benchmark paper and repository.
- First-party incident report.
- Official pricing or product documentation.

Use for factual claims within the tested or documented scope.

### Verified case

A dated, documented real-world example with a clear context.

Use to illustrate a mechanism. Do not generalise it automatically.

### Practitioner pattern

Guidance from experienced operators, engineering teams, product leaders, consultants, or vendors.

Use for operating ideas worth testing. Do not present as scientific consensus.

### Author synthesis

A conclusion reached by connecting multiple sources and first-principles reasoning.

Use when the reasoning is made visible. Label assumptions and avoid pretending the conclusion was directly measured.

### Excluded

Exclude a claim when it is:

- Unsupported.
- Contradicted by stronger evidence.
- Too context-specific.
- Based mainly on marketing.
- Precise without methodology.
- Unrelated to the article’s decision.
- Repeated elsewhere in the series.

---

## 5. Research Workflow

### Phase 1: Understand the article

Before external research, read the complete article and record:

- The decision it helps the reader make.
- The central thesis.
- The intended audience.
- Existing examples and evidence.
- Existing frameworks.
- Claims likely to become stale.
- Claims that appear overstated.
- Terms that may confuse readers.
- Overlap with other articles.
- Missing practical actions.

Use this table:

| Field | Notes |
|---|---|
| Article title | |
| Reader | |
| Decision supported | |
| Current thesis | |
| Strongest existing section | |
| Weakest existing section | |
| Claims needing verification | |
| Information likely to be stale | |
| Missing mechanism | |
| Missing example | |
| Missing AI PM action | |
| Related articles | |

Do not begin by searching for news related to the title. Understand the article first.

### Phase 2: Search in time layers

Use several research windows.

#### Last 14 days

Use for:

- Breaking incidents.
- Pricing changes.
- Regulatory changes.
- Standards updates.
- Product removals or major capability changes.

#### Last 60 days

Use as the primary freshness window for:

- New research.
- Production lessons.
- Practitioner shifts.
- Market changes that affect decisions.

#### Last 12 months

Use to decide whether a recent signal is sustained or temporary.

#### Foundational sources

Use older work when it remains necessary for the concept to be correct.

Do not remove a strong foundational source merely because it is old.

### Phase 3: Build an evidence ledger

Record every candidate signal before adding it to an article.

| Field | Question |
|---|---|
| Signal | What changed? |
| Date | When did it happen? |
| Original source | Where is the first-party evidence? |
| Source type | Primary, case, practitioner, synthesis, or excluded? |
| Method | How was the conclusion produced? |
| Scope | What systems, models, users, or domains were covered? |
| Limitation | What does the evidence not prove? |
| Counter-evidence | What challenges the claim? |
| Article fit | Which article should own it? |
| Decision effect | What should the reader do differently? |
| Confidence | High, medium, low, or exclude? |
| Decay risk | How quickly may this become stale? |

### Phase 4: Apply the claim gate

A claim enters an article only if it passes these tests.

#### Truth

Is the claim supported by the source?

#### Transfer

Is it clear whether the result applies beyond the original setting?

#### Relevance

Does it strengthen the article’s central decision?

#### Novelty

Does the article already make this point?

#### Decision value

Does it change a product, architecture, pricing, evaluation, risk, or operating decision?

#### Clarity

Can it be explained in normal language?

#### Durability

Will it remain useful after the news cycle?

#### Placement

Is there a clear location where it belongs?

A claim may be true and still fail because it is irrelevant, repetitive, or too temporary.

### Phase 5: Search against the claim

Before final acceptance:

1. Search for criticism or correction.
2. Check whether the date is being misreported.
3. Check whether the cited source measured the claimed outcome.
4. Check whether a vendor is evaluating its own product.
5. Check whether the comparison used equal conditions.
6. Check whether the metric represents user value.
7. Check whether the result survives outside the test environment.

### Phase 6: Write the revision

Use the standard article-revision block:

```markdown
## Article ID — Title

### Decision
What decision should the article help the reader make?

### Current weakness
What is incomplete, outdated, repetitive, or misleading?

### New evidence
What is the strongest useful signal?

### Evidence strength
Verified primary / verified case / practitioner pattern / author synthesis.

### Why it matters
How does this change the article or decision?

### Exact placement
Insert after or replace: “Exact existing sentence or heading.”

### Publication-ready wording
The exact copy to use.

### Practical action
What should the reader do next?

### What this does not prove
The boundary of the evidence.

### Cross-link
Which related article should be linked, and why?
```

### Phase 7: Review the series

After individual revisions:

- Remove duplicate signals.
- Give each important idea one natural home.
- Use links instead of repetition.
- Check terminology across the series.
- Check that later articles build on earlier ones.
- Check that examples do not contradict each other.
- Verify every number, date, quotation, and product claim.
- Remove unnecessary jargon.
- Check whether each article ends with an action.
- Check whether the revision overwhelms the original teaching.
- Add limitations where evidence could be overread.

---

## 6. Writing Standard

### 6.1 Write from the decision, not the topic

Weak framing:

> What is outcome pricing?

Stronger framing:

> When should we price the result, and what must be true before we do?

Weak framing:

> What is multi-model orchestration?

Stronger framing:

> Which models are permitted, which model should handle this step, and what happens when it fails?

Weak framing:

> What is a golden dataset?

Stronger framing:

> Which failures deserve to become permanent regression tests?

### 6.2 Explain before naming

Do not begin with specialist language.

Use this sequence:

1. Product problem.
2. Plain-language explanation.
3. Example.
4. Decision affected.
5. Technical term, if still useful.
6. Practical action.
7. Limitation.

Example:

Avoid:

> Attach evaluator scores to causally useful spans.

Prefer:

> Score the individual step that helps explain the failure, but keep it connected to the complete task and user outcome. This is often called span-level scoring.

### 6.3 Prefer concrete nouns and verbs

Avoid:

- Leverage.
- Unlock.
- Transform.
- Revolutionise.
- Paradigm shift.
- Rapidly evolving landscape.
- Seamless.
- Robust, unless the failure conditions are named.
- Agentic, when it is being used as an explanation.

Prefer:

- Choose.
- Test.
- Record.
- Compare.
- Stop.
- Approve.
- Reject.
- Escalate.
- Complete.
- Pay.
- Fail.

### 6.4 Keep sentences falsifiable

Avoid:

> This may potentially help teams improve reliability.

Prefer:

> Shorten the required chain and test whether end-to-end completion improves.

A useful sentence can be wrong. A vague sentence avoids being wrong by saying nothing.

### 6.5 Separate fact, interpretation, and recommendation

Use clear transitions:

- **The source found:** measured result.
- **The likely mechanism is:** interpretation.
- **For an AI PM, this means:** recommendation.
- **This does not prove:** limitation.

Do not blend all four into one authoritative-sounding paragraph.

---

## 7. Article Structure

Use this structure for most practitioner articles:

### Opening decision

State the decision or tension, not a broad industry trend.

### Common mistake

Name the belief or operating habit that leads teams astray.

### Mechanism

Explain why the result occurs.

### Practical example

Use a realistic workflow, not a generic chatbot.

### Decision framework

Give the reader questions or criteria.

### Action

Provide something to do this week.

### Limitation

State what the evidence does not establish.

### Reusable artifact

End with a checklist, worksheet, table, memo, or decision template.

---

## 8. Series Architecture

### One idea, one home

Every important idea should have one primary article.

Other articles should:

- Link to it.
- Apply it briefly.
- Avoid redefining it.

This protects each article’s identity and prevents SEO-shaped repetition.

Maintain a map:

| Insight | Primary article | Articles that may link |
|---|---|---|
| | | |

### Cross-link causally

Link articles because one supplies an input to another.

Examples:

- Failure classification → trace debugging → root-cause analysis.
- Golden dataset → first eval suite → production learning loop.
- Rubric → judge validation → judge-system design.
- Agent evaluation → pipeline evaluation → production monitoring.
- Product job → cost model → pricing model → ROI.
- Architecture → authority → trust boundary.

Do not add links only for navigation or SEO.

### Use stable terminology

Define a shared vocabulary for each series and use it consistently.

Suggested core terms:

- **Job:** Work the user or business wants completed.
- **Completed job:** A verified result, not a generated response.
- **Task definition:** Success, acceptable variation, forbidden actions, and escalation.
- **Context:** Information available to the system for the current decision.
- **Test case:** One input and situation used to check behaviour.
- **Golden dataset:** A reviewed and versioned set of important regression cases.
- **Evaluator:** Rule, program, AI judge, human review, or combination used to score behaviour.
- **Trace:** Linked record of steps that produced an outcome.
- **Harness:** System around the model: context, tools, memory, permissions, retries, and checks.
- **Meter:** Unit used for billing.
- **Exception rate:** Share of cases that require human handling.
- **Trust boundary:** Actions requiring approval or prohibited entirely.
- **Proof:** Evidence strong enough to change a ship, scale, or stop decision.

---

## 9. Lessons from AI Evals

### Evaluate the system, not only the model

A product result is produced by the combination of:

- Model.
- Instructions.
- Context.
- Retrieval.
- Tools.
- Permissions.
- Runtime environment.
- Human interaction.
- Evaluator.
- Test runner.

Do not automatically classify a product failure as a model failure.

### Treat the evaluator as part of the uncertainty

AI judges and human reviewers can disagree or drift.

Test:

- Criteria.
- Examples.
- Answer order.
- Formatting.
- Length sensitivity.
- Missing evidence.
- Model updates.
- Repeated-run variation.

Approve an evaluator for a particular decision, not for every future use.

### Treat golden datasets as governed memory

A golden dataset is valuable because:

- Cases have known origins.
- Important journeys and risks are covered.
- Expected behaviour is reviewed.
- Changes are versioned.
- Near-duplicates are controlled.
- Exposure to prompts or training is understood.
- Production failures enter through a reviewed process.

Do not define dataset quality through one universal number of cases.

### Close the production loop

Use this sequence:

> Production behaviour → reviewed failure → first wrong step → tested cause → representative regression case → release decision → production verification

The loop is incomplete if the test passes but production behaviour does not improve.

### State the limit

Evals do not prove universal quality or safety. They show performance under tested conditions and a particular scoring process.

Every major eval report should include:

> **What this does not prove:** The result applies to these cases, system versions, environment, and scoring method. It does not establish universal capability, quality, or safety.

---

## 10. Lessons from AI PM OS

### Own the job

Define products around work completed, not text generated.

Avoid treating these as value:

- Messages generated.
- Tool calls.
- Agent sessions.
- Tokens consumed.
- Drafts created without use.

Prefer:

- Jobs completed.
- Jobs that remained resolved.
- Human takeovers.
- Cost per completed job.
- Time and effort required from the user.
- Serious failures and authority violations.

### Own the context

Before asking for a stronger model, ask:

> Did the system have the information a competent person would have needed at this step?

Investigate:

- Missing context.
- Stale context.
- Excess irrelevant context.
- Conflicting instructions.
- Lost conversation state.
- Wrong customer or permission context.
- Important information removed during summarisation.

Do not claim context causes most failures everywhere unless the product’s own evidence supports it.

### Own the authority

For any system that can act, define:

- Identity used by the system.
- Data it may access.
- Tools it may call.
- Changes it may make.
- Actions requiring confirmation.
- Actions prohibited entirely.
- Evidence retained for later review.

The trust boundary should be explicit:

> The trust boundary is the list of actions the system cannot take alone.

### Own the economics

Track:

> **Cost per completed, trustworthy job**

Include:

- Model calls.
- Context and retrieval.
- Tools.
- Retries.
- Failed runs.
- Evals and monitoring.
- Human review.
- Exception handling.
- Incident cost.

Do not treat cost per token as the complete product metric.

### Own the proof

Use four forms of proof:

- **Task proof:** Important cases pass.
- **User proof:** Real users complete the job with acceptable effort.
- **Cost proof:** Cost per completed job remains inside the planned range.
- **Control proof:** Forbidden actions are tested, logged, and stoppable.

Scale the evidence burden with reversibility and harm.

### Model the exception queue

For service-as-software and outcome-priced products:

\[
\text{Cost per job}
=
\text{automated cost}
+
(\text{exception rate} \times \text{human cost per exception})
+
\text{error and incident cost}
\]

Automation rate does not predict margin by itself. The remaining cases may be the hardest and most expensive.

---

## 11. Final Revision Checklist

### Research

- [ ] Did I read the complete article first?
- [ ] Did I identify the decision it supports?
- [ ] Did I search primary sources?
- [ ] Did I search for corrections and opposing evidence?
- [ ] Did I check dates and versions?
- [ ] Did I inspect the method behind every important number?
- [ ] Did I label vendor-reported evidence?
- [ ] Did I state transfer limits?

### Editorial judgement

- [ ] Does the new information change a decision?
- [ ] Does it strengthen the article rather than distract from it?
- [ ] Does another article already own the insight?
- [ ] Is the signal durable enough to include?
- [ ] Am I turning one case into a universal rule?
- [ ] Have I removed a weaker or outdated claim?

### Writing

- [ ] Does the paragraph begin with the reader’s problem?
- [ ] Is the mechanism clear?
- [ ] Is there one realistic example?
- [ ] Are technical terms explained before being used?
- [ ] Can a non-engineering stakeholder understand it on one reading?
- [ ] Are the sentences direct and falsifiable?
- [ ] Have I removed hype words and empty transitions?

### Practitioner value

- [ ] Is there a clear AI PM decision?
- [ ] Is there an action the reader can take this week?
- [ ] Is there a checklist, table, worksheet, or reusable artifact?
- [ ] Does the article state what the evidence does not prove?
- [ ] Is the responsible team or owner clear?

### Series quality

- [ ] Is terminology consistent?
- [ ] Are repeated signals removed?
- [ ] Do cross-links connect ideas causally?
- [ ] Does the article build on earlier episodes?
- [ ] Does the complete series move from understanding to action?

---

## 12. Scoring Rubric

Rate each revised article from 1 to 10 on five dimensions.

| Dimension | Question |
|---|---|
| Truth | Are claims accurate, sourced, and limited? |
| Usefulness | Does the article improve a real decision? |
| Clarity | Can the intended reader understand it in one pass? |
| Distinctiveness | Does the article own a clear idea? |
| Durability | Will the insight remain useful after the news cycle? |

### Score meaning

- **1–4:** Unsupported, confusing, or mostly news-shaped.
- **5–6:** Useful idea but weak evidence or unclear action.
- **7–8:** Strong article with identifiable gaps.
- **9:** Accurate, clear, distinctive, and practical.
- **10:** Meets the 9 standard and integrates naturally with the original article, contains a memorable mechanism or example, and leaves the reader with a reusable decision artifact.

Do not award 10 when the complete original article has not been reviewed.

---

## 13. Standard Closing Questions

End every major practitioner article with:

1. What decision does this help me make?
2. What evidence would change that decision?
3. What does this still not prove?
4. What should I do next?
5. Which assumption should I validate first?

---

## 14. Final Editorial Rule

> Research broadly. Verify narrowly. Explain the mechanism. Write in normal words. Connect every insight to a decision. State the boundary. Leave the reader with something they can use.

If a new signal does not change the job, architecture, meter, proof, risk, or trust boundary, it is news—not a revision.
