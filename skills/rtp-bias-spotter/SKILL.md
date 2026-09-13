---
name: bias-spotter
version: v1.2.1_latest
description: 'Check whether a consequential AI product decision is being distorted by assumptions, selective evidence, incentives, or uncritical trust in AI. Examine what you build, how you measure it, and the biases the system may carry. Name the strongest supported risks, seek contrary evidence, and recommend a practical mitigation. Use before committing resources, when reviewing a PRD or rollout, or when a choice feels obvious because of a demo, competitor, or senior opinion. A sound audit can find no material bias. Pairs with first-principles, falsification, eval-framework, stress-test, trendslop-check, and judgment-guard.'
imports: []
---

# Bias Spotter

Improve a decision by examining the evidence and process that produced it. Identify the most consequential bias risks, test alternative explanations, and make the next action clear.

**Audit the decision, not the person's character.** Confidence, consensus, seniority, and impressive numbers deserve scrutiny, but none proves bias. A failed outcome does not prove that the original decision was biased, either. The useful result is a better-supported choice, including a justified decision to proceed unchanged.

## Start with the choice and its consequences

State the decision in one sentence, the available alternatives, and what a wrong call would cost. Include the cost of waiting or doing nothing. Use a short check for a reversible choice with fast, reliable feedback; use a fuller audit when the commitment, uncertainty, or potential harm is substantial.

Identify the stage that needs attention:

| Stage | Question | Typical response |
|---|---|---|
| **Build: decision biases** | Why are we choosing this problem, solution, or investment? | Reframe the choice, compare alternatives, test assumptions. |
| **Measure: evaluation biases** | Could our method make weak performance look strong? | Repair sampling, metrics, judging, or comparison. |
| **Carry: system and interaction biases** | Who receives different treatment, and how do errors propagate? | Test segments and mechanisms; change data, design, or oversight. |

These are practical lenses, not mutually exclusive diagnoses. Human reasoning, institutional incentives, and model behavior can interact. This is consistent with the broader treatment of bias across the AI lifecycle in [NIST SP 1270](https://doi.org/10.6028/NIST.SP.1270).

Use the shared Universal Skill Protocol for grounding and handoffs: it lives at `ai-pm-skills/UNIVERSAL-SKILL-PROTOCOL.md` in the source library and at the plugin root. Scale the output to the decision; a brief audit does not need a separate document or diagram.

## Run the audit in five steps

### 1. Name the decision

Write the actual choice, rather than the preferred solution's slogan. “Authorize a support-agent pilot for these ticket types” is more useful than “embrace AI.” If the choice is unclear, resolve that ambiguity before assigning bias labels.

### 2. Examine the reasoning

For a full audit, answer each relevant question with evidence or an explicit unknown:

| Possible bias | Check |
|---|---|
| **Anchoring** | What first number, proposal, or demo framed the discussion? What independent estimate have we made? |
| **Sunk cost** | Would we make the same forward-looking choice without the time and money already spent? Which remaining benefits and exit costs are real? |
| **Confirmation** | Have we sought evidence that could change our view, or mainly collected support? |
| **Survivorship** | Are failed, lost, excluded, or silent cases missing from the evidence? |
| **Optimism** | Does the plan assume best-case quality, adoption, operating cost, or recovery? |
| **Authority** | Are we relying on relevant expertise and a sound argument, or mainly on status? |
| **Bandwagon** | What user need or competitive evidence supports copying this choice? |
| **Present bias** | Are near-term gains obscuring later maintenance, evaluation, or user costs? |

Do not manufacture an answer to fill the checklist. Distinguish an observed flaw from a plausible risk and from something not assessed.

### 3. Select the consequential risks

Usually one or two mechanisms deserve action. For each, connect **evidence → possible distortion → decision consequence**. “The demo excludes multilingual tickets, so it cannot establish global readiness” is actionable. “The team is overconfident” is a judgment about people without a test.

Consider alternatives: a missing metric may reflect instrumentation limits; a person may understand the risk but lack permission or time to act. Those situations need different remedies from a reasoning error. If no material bias is supported, report that result and the audit's limits.

### 4. Apply the inversion test

Ask: “If this recommendation were wrong, what would we expect to observe?” Seek that evidence. Use `rtp-falsification` when the choice needs a defined test and action trigger.

Check the source of counter-evidence. Several articles repeating one study are one underlying evidence stream. An AI-generated skeptic can suggest tests; it does not supply independent observations or replace a stakeholder's real objection. Record whether the evidence confirms, extends, bounds, or contradicts the claim, and revise the claim accordingly.

### 5. Restate the decision and response

State whether to proceed, modify, test first, or pause, and why. Assign a concrete mitigation and owner for each material risk. If there is no supported risk requiring a change, explain why proceeding is reasonable. Do not add a safeguard merely to make the audit appear productive.

Bias-spotter informs the responsible decision-maker; it does not create approval authority. It should neither become a political veto nor force progress through a material unresolved risk.

## Stage 1: what you build

The checklist above covers the main decision biases. In AI product work, look especially for:

- **Anchoring:** a vendor's accuracy number becomes the PRD target without a matching task or population.
- **Sunk cost:** six months of investment becomes the main reason to continue, without a fresh comparison of future costs and benefits.
- **Survivorship:** retained customers define the roadmap while lost customers and abandoned workflows are absent.
- **Bandwagon:** an LLM or vector database is chosen because peers use it, before the problem requires it.
- **Present bias:** an early launch excludes evaluation or maintenance whose later cost is predictable.
- **Novelty bias:** a new architecture is presumed better before comparison on the actual job.

### Check the growth blindspot without creating its opposite

Ask which outcome the investment is intended to improve: cost, revenue, retention, service quality, or another explicit objective. Has an efficiency default prevented a credible growth alternative from being considered? Conversely, has enthusiasm for growth displaced a necessary efficiency investment?

Cost savings are bounded by the costs that can actually be removed. That does **not** establish a universal 10% ceiling on firm value. Growth also faces demand, capacity, competition, cost, and risk constraints. Compare the alternatives under the business's own assumptions, including how long benefits may last and who captures them. A temporary, copyable benefit can still be worthwhile if its economics justify it; durability is a separate question.

The original skill draws this diagnostic from Benartzi, Long, and Puntoni's June 2026 HBR article. Its wealth-management valuation examples and executive beliefs are retained, with limits, in [research notes](references/research-notes.md). Use `rtp-moat-finder` for value placement and defensibility, and `rtp-ai-portfolio-management` when the same default may shape an entire portfolio.

## Stage 2: how you measure

Numbers can conceal selection and measurement choices. Check for:

- **Confirmation:** failed cases are dropped or the evaluation changes only to favor the preferred model.
- **Demo bias:** curated examples are easier than the intended workload.
- **Benchmark anchoring:** a published score substitutes for evaluation on your task and users.
- **Optimism:** an evaluation score is carried into production without checking context or distribution shift.
- **Evaluation-gap bias:** an easy proxy substitutes for the outcome users need.

Concrete warning signs include testing only the 100 easiest examples; missing a substantial production segment; evaluating only English before a multilingual rollout; using a judge that rewards length over usefulness; and investigating only errors users noticed and reported. Counts and percentages in these examples are illustrative, not diagnostic thresholds.

Build an evaluation set with representative coverage **and** deliberate hard-case coverage. A stratified sample separates meaningful groups; rare groups may be oversampled to examine them. Report results by segment, and use suitable weights when estimating an overall production rate. Testing only the hardest cases is no more representative than testing only the easiest.

Check the metric itself. **BLEU** measures text overlap using n-grams; **exact match** checks equality against an expected answer. They are different measures, and neither automatically measures user value. An **LLM-as-judge** needs calibration against the task's standards and checks for preferences such as verbosity. **Distribution shift** means the evaluated and deployed inputs or conditions differ; it can be abrupt or gradual.

Look beyond reported activity. Repeated queries can indicate failure, and an adoption target can encourage activity that does not help users. Pair activity or throughput with completion quality, rework, and relevant guardrails. Measure end-to-end outcomes when a faster model step may simply move work to reviewers.

**Shadow deployment** compares an AI's outputs with the live process while keeping its actions isolated. Use authorized data access and prevent unintended writes or messages. It can reveal output differences; it cannot by itself establish how users will behave when they see or act on those outputs. Route the measurement plan to `rtp-eval-framework`.

## Stage 3: what the system carries

Look for mechanisms at the data, model, workflow, and human-interaction levels:

| Mechanism | What to investigate |
|---|---|
| **Training-data bias** | Learned patterns that produce systematic errors or harmful treatment in the target setting. |
| **Representation bias** | Missing or inadequate coverage of relevant languages, populations, or circumstances. |
| **Measurement bias** | Labels or proxies that misrepresent the intended construct. |
| **Aggregation bias** | A pooled model or average that conceals materially different subgroup behavior. |
| **Automation bias** | People accepting AI output without the scrutiny the decision requires. This is an interaction risk, not simply a property stored in training data. |

### Test label effects carefully

An observed group difference may arise from different requests, different treatment of comparable requests, or several interacting causes. To test a specific label effect, hold substantive prompt content fixed and randomize the relevant label or cue. Repeat across prompts and runs, counterbalance conditions, and assess the size and uncertainty of the difference.

A repeatable difference can support an effect of that manipulation in the tested setting. A single changed answer may be ordinary model variation. A name may signal several attributes; refusal or sycophancy may create a different mechanism from the one proposed. Ask whether the attribute is legitimately relevant to the task, and use appropriate domain review. A null result bounds this test; it does not clear every form of bias. The earlier financial-advice research lead is documented in the reference notes, without claiming a general validation of this method for every fairness question.

### Audit agent handoffs

Upstream errors can become downstream assumptions. A later agent may amplify, preserve, detect, or correct them; amplification is not inevitable. Inspect evidence provenance, opportunities to challenge an input, and the final outcome.

For illustration, if two required stages each succeed with probability 0.95 and their successes are independent, both succeed with probability `0.95 × 0.95 = 0.9025`: a 9.75% chance that at least one fails. This is not a formula for how bias multiplies, and one agent's 5% error rate alone cannot determine the chain's rate. Measure the actual chain, including correlated failures and recovery.

## Check ideation bubbles when the task needs diverse options

People working separately can still receive similar information from the same retrieval defaults and produce similar ideas. Apparent independent agreement may therefore reflect a shared input rather than independent corroboration. The risk matters most during divergent ideation; familiar, accurate retrieval can be useful for a well-defined task.

Inspect the ideas for semantic similarity, using clustering as an aid to human review. Examine whether the clusters represent meaningfully different approaches and whether those approaches are useful. Report the clustering choices and check sensitivity; one or two clusters alone do not prove a problem. A narrow task may appropriately have few good solutions.

When more variety would help, **diverge on retrieval and converge on review**: vary sources, query paths, and exploration settings, then compare ideas against shared criteria. A shared workspace can support critique without requiring identical retrieval. Different backgrounds can also yield different interpretations of shared material; common tools do not guarantee identical thinking.

The original four reported cluster counts are preserved in [research notes](references/research-notes.md). Treat them as a reason to test this mechanism locally, not as a universal effect size or proof that experts using standard search are indistinguishable from novices. Related skills: `rtp-uncertainty-research`, `rtp-moat-finder`, and `rtp-alignment-check`.

## Worked example: an AI support agent

**Illustrative scenario; these are teaching numbers, not a documented deployment.** A team proposes handling 50% of support tickets with AI. Its FAQ demo scores 92%, but FAQ-like questions make up only 40% of the production workload. During a rollout covering 40% of tickets, measured accuracy is 71%. The team reduces coverage to 10% and spends two weeks rebuilding evaluation after a month of poor support.

The 21-percentage-point gap is observable in the scenario. Assigning that gap to four biases is not: comparable scoring, samples, routing, and conditions would be needed to explain it. Nor does an FAQ evaluation tell us what the foundation model was trained on.

The audit identifies supported risks: easy-case selection, overgeneralization from the demo, and missing visibility into complex or unreported failures. It recommends a production-grounded, stratified evaluation with an independently reviewed case-selection method; results by language and complexity; and a bounded rollout with escalation and rollback criteria. A two-week shadow period is one possible learning window, chosen for the traffic and evidence needed, not a universal requirement.

## Output and handoffs

Use this compact structure, expanding only where the decision needs it:

```markdown
## Bias Audit: [decision]

**Decision and stakes:** [choice, alternatives, cost of error or delay]
**Stage:** [build / measure / carry; more than one if needed]
**Material bias risks:** [supported mechanism, evidence, consequence;
  or no material bias found, with limits]
**Counter-evidence:** [what was sought, what was found, what remains unknown]
**Recommendation:** [proceed / modify / test first / pause, with reason]
**Mitigation and owner:** [action, owner, evidence or trigger for review]
**Residual risk:** [what the action does not resolve]
```

For example: “Run a bounded pilot. The English-only evaluation does not establish multilingual readiness. The evaluation owner will test the intended languages and define rollout criteria before expanding coverage.” A two-week window or an 80% rollback threshold belongs here only when the team has justified it for the task.

Use the next skill where it adds work the audit has not done:

- `rtp-first-principles`: remove inherited framing before evaluating the choice.
- `rtp-falsification`: turn a contrary-evidence question into a test and response.
- `rtp-problem-type`: separate technical work from changes in behavior, trust, or incentives.
- `rtp-eval-framework`: fix sampling, measures, judging, and segment reporting.
- `rtp-trendslop-check`: examine fashionable defaults in AI-generated strategy.
- `rtp-stress-test`: test material assumptions and failure conditions.
- `rtp-moat-finder` and `rtp-ai-portfolio-management`: examine value placement, durability, and portfolio-wide defaults.
- `rtp-judgment-guard`: design and test a checkpoint that enables effective human judgment.

A small audit can end with its recommendation; it does not always need another skill invocation.

## Review the audit itself

- Is the decision clear, with relevant alternatives and consequences?
- Are named biases supported by specific evidence, and alternative explanations considered?
- Has contrary evidence actually been sought, or is that still the next action?
- Does the response address the mechanism, with an owner able to carry it out?
- Can the audit conclude that the original choice remains sound?

Awareness alone does not remove bias. Repeatedly naming a pattern without changing evidence, incentives, or decision conditions can become ceremony. Use respectful language such as “this sample may overstate readiness.” Do not diagnose a colleague's motives.

More labels are rarely the goal. Prioritize consequences, stop when further checking is unlikely to change the choice, and do not exempt experiments or experts from relevant scrutiny. A fast A/B test can still have a poor metric; an expert's judgment should receive task-appropriate review without reflexive second-guessing. Guardrails depend on failure severity, exposure, detectability, and recovery, not an accuracy percentage alone.

**Trade-off:** a short audit costs time and sometimes social comfort in exchange for a chance to improve a consequential choice. Over-analysis, unsupported accusations, and false reassurance are real costs too. Finish with the recommendation, the main unresolved risk, and the next owned action. Add a three-stage visual only when it would make the explanation easier to use.
