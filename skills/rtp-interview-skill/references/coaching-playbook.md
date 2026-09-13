# AI PM interview coaching playbook

Match the practice to the observed gap. Understanding a mechanism, retrieving it under time pressure, explaining it clearly, and having relevant experience are different needs. Do not prescribe a new project when a focused explanation or delivery drill will solve the problem.

Use the main skill’s six criteria throughout: **clear direction, technical depth, relevant evidence, useful nuance, concise delivery, and honest uncertainty**. There is no evidence here for a universal grade improvement, a guaranteed hiring result, or a fixed share of follow-ups that any drill will cover.

## The practice loop

Select one relevant question, answer aloud if useful, and take one follow-up on the most consequential gap. Review the applicable criteria, repair the gap, and answer again in fresh words. Compare the reasoning and clarity, not just how polished the second attempt sounds. Use existing practice history if available and relevant; do not infer a weakness from the absence of a history file.

## Twelve patterns and matching drills

| Observed pattern | Check before diagnosing | Targeted drill |
|---|---|---|
| Correct definitions, weak application | Was application actually requested? | Explain a concept, then apply it to one decision and a relevant trade-off; use the matching topic question |
| Confident factual errors | Is the mechanism wrong, the fact stale, or the source missing? | Correct the concept, state what is known and unknown, and explain the check needed; do not label every error bluffing |
| Rambling | Is the answer too long for this task or merely poorly ordered? | Give a timed 90-second practice version, then a 30-second direction and an optional deeper version |
| Accurate mechanism without a product consequence | Does this round need a decision as well as an explanation? | Add the specific effect on evaluation, UX, cost, or failure handling |
| Elaborate architecture without justification | Which actual requirement needs the complexity? | Compare a direct call, fixed workflow, and dynamic agent; explain the smallest sufficient design |
| Activity presented as success | Does the metric demonstrate a quality-adjusted outcome? | Define the user’s completed task, denominator, and guardrails; use concept §8 |
| Design assumes correct outputs | Which failure would matter and how is it handled? | Trace a confidently wrong result to detection, fallback, owner, and appropriate action controls; use §13 |
| Platform or model ownership is unclear | What did the candidate personally build, configure, or lead? | Rewrite the story with exact responsibility and dependencies |
| No answer to “what would you change?” | Is there a real relevant lesson or changed decision? | Prepare one verified setback or reconsidered choice, including its consequence; never invent one |
| Weak model-selection reasoning | Can the candidate distinguish the task from the technology label? | Compare churn, fraud, and one language task against simple baselines; use §3 |
| Weak evaluation reasoning | Are the outcome, failure cases, and evidence missing or confused? | Build an evaluation outline and answer the “quietly getting worse” question; use §8 |
| Weak cost reasoning | Is the issue arithmetic, scope, or choosing interventions? | Calculate cost per successful task from actual or explicitly illustrative prices; add retries and review, then diagnose the largest driver; use §9 |

## Plans for the time available

### One day

Review the glossary for recall and the relevant model answers for structure. Confirm one strong personal story, including role, outcome, and a real lesson. Run a short mock and fix its most consequential gap. Keep the six criteria and seven diagnostic patterns in a compact practice note if useful. Prioritize rest and reliable recall over adding many unfamiliar concepts. Use notes during a real interview only when its rules allow them.

### One week

- **Days 1–2:** concepts §1–§5: generation, hallucination, model choice, tools, and agents. Apply each relevant concept aloud.
- **Days 3–4:** §6–§9: routing, RAG, evaluation, and economics. Work through the most relevant follow-ups and one calculation.
- **Day 5:** §10–§14: hardware, adaptation, transformers, safety, and multimodal systems. Set depth from the actual role, not its employer’s reputation alone.
- **Day 6:** practice the same questions with engineering and product emphasis. Compare what each answer needs.
- **Day 7:** repair the weakest recurring gap, verify personal facts, and prepare questions for the employer. Add a small build only if it serves the gap and fits the time.

### One month

In weeks 1–2, study one concept per session and test understanding with spoken applications. In weeks 2–3, undertake a bounded project if hands-on experience is the missing ingredient. During week 3, verify the company and role context, choose relevant stories, and use historical questions as practice prompts. In week 4, run mock loops with both interview lenses and progressively deeper follow-ups.

An optional practice target is five well-supported answers that withstand two meaningful follow-ups each. It is a coaching target, not a validated readiness threshold. Adjust time, difficulty, and scope to the role and the candidate’s needs.

## Reusable self-interviewer prompt

```text
Run a practice interview for an AI Product Manager role.
Use the role and time constraints I provide; otherwise start with a general five-question mock.

Tell me whether this practice emphasizes engineering mechanisms or product decisions.
Real interviews can blend both. Ask one question at a time and wait for my answer.
Follow up on the most consequential gap before giving feedback. Ask for application
when useful, but accept a correct definition when that is what the question requests.
Name a technical error or unsupported claim specifically; do not infer dishonesty
from an error alone. Keep my real experience distinct from hypothetical designs.

Select from these questions:
1. Design a high-level system for how an assistant responds to a user query.
2. Users say the assistant is confident but wrong. How would you fix it?
3. How do you decide which tasks suit an LLM and which do not?
4. A feature calls a tool. What happens under the hood?
5. Explain an LLM feature's economics and how its latency targets affect the design.
6. Describe an evaluation harness: what belongs offline, and what do you watch after launch?
7. The north-star metric rose. How would you detect quietly worsening quality?

After five questions, review clear direction, technical depth, relevant evidence,
useful nuance, concise delivery, and honest uncertainty. Use strong, partial,
material gap, or not applicable, with reasons from my answers. Do not invent quotations.
Watch mechanism fluency, treatment of uncertain outputs, operational follow-through,
and awareness of knowledge limits as diagnostic prompts within those six criteria.
Give an honest assessment, not a deliberately harsh one or a hiring prediction.
End with the single most useful next improvement and a concrete drill.

State the practice emphasis and ask question one.
```

Running the same questions under both lenses can reveal a delivery mismatch. Do not require repeated mocks if one already answers the user’s need. The four diagnostic prompts in the reusable prompt support the shared rubric; they are not a second competing scoring system.

## Build experience where it will help

Scope a project to the available time, permissions, data, and budget. None is guaranteed to fit a weekend or establish production experience.

- **Predictive ML:** compare a simple baseline and an XGBoost model on an appropriate public churn or fraud dataset. Inspect leakage, calibration, and error cases. Feature importance does not establish causality.
- **Tools:** build a calculator or weather-tool demonstration. Inspect structured requests, pre-execution validation, errors, and the boundary between model selection and execution.
- **RAG:** use 20–50 authorized documents as a manageable starting exercise. Compare parsing, retrieval, chunking, and optional reranking on actual questions; the document count is not a quality guarantee.
- **Agents:** create a digest from mock messages or authorized read-only Slack or email data. Define task guidance, tool access, state, and completion checks. Producing a draft does not authorize sending messages, and three files alone do not prove an end-to-end agent.
- **Evaluation:** begin with roughly 20 varied cases if that is practical, then review errors and judge disagreements. A small exercise does not demonstrate all judge biases or production reliability.
- **Cost:** estimate costs first, then compare two suitable models on a bounded sample within an approved budget. A 1,000-query experiment is an optional scale, not mandatory spending. Compare quality and successful outcomes as well as bills.

Record what was actually built, its limitations, observed failures, and the evidence for any improvement. A prototype supplies a truthful prototype story; it should not be promoted into a production claim.

## End with a concrete next step

```text
Target role and round:
Practice evidence: [specific answer or observed pattern]
Most important improvement and why:
Study: [relevant concept]
Drill: [one question or practice set]
Build, only if needed: [bounded scope, data, and budget]
Success check: [what a better answer or result would demonstrate]
Unresolved fact:
```

Select only the actions that fit the available time. Save relevant practice notes in the authorized location when useful; do not create sensitive personal profiles or assume a particular slash command exists. Encourage another mock when it helps measure progress, without promising that a drill will secure an offer.
