---
name: rtp-eval-framework
description: "Evaluation approach: what eval problem, what to measure from failures, evolve evals as product matures. Use when: launching features, diagnosing quality, setting monitoring. Triggers: 'how to evaluate', 'eval framework', 'quality metrics'"
imports: [feedback-flywheel, first-principles, stress-test]
---

# Evaluation Framework

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## DEPTH DECISION

**Go deep** if: you're shipping an AI feature to production, you have >50 outputs to analyze, or your eval scores don't match user experience. Read every section.

**Skim to KEY DIAGNOSTIC QUESTIONS** if: you're doing a quick sanity check on an existing eval setup. The questions section alone will surface gaps.

**Skip entirely** if: you're in week 1 of a prototype (just use the product yourself), or the system is fully deterministic (use assertions, not evals).

## THE TRAP

You will reach for a methodology before understanding your problem. The bias is **abstraction comfort** — adopting someone else's eval framework feels like progress but skips the hard work of understanding YOUR product's specific failure modes.

The trap has four variants:

- **Generic metrics theater.** You use Rouge, BLEU, faithfulness, helpfulness scores. A real estate chatbot with perfect "coherence score" that schedules tours for unavailable properties is a failure no generic metric catches.
- **Premature automation.** You build an automated eval pipeline before you've looked at 50 traces. You're automating measurement of the wrong things.
- **Tool-first thinking.** You believe an LLM-as-judge product or eval vendor will solve your problems. Eugene Yan: "This sidesteps the core problem and avoids the real work." Evals are a practice, not a product.
- **Likert scale false precision.** Rating outputs 1-5 hides the real question: does this output work, or doesn't it? Annotators disagree on scale points; they rarely disagree on pass/fail.

## THE PROCESS

### Start Here: Diagnose Your Eval Problem

Before building anything, answer these diagnostic questions. Your answers determine your approach.

**1. What type of AI system are you evaluating?**

| System Type | What Matters Most | Eval Focus |
|------------|-------------------|------------|
| **Chatbot** (Q→A) | Single-turn correctness | Factuality, relevance, safety per response |
| **Copilot** (embedded suggestions) | Context awareness in workflow | Acceptance rate, edit distance, workflow fit |
| **Agent** (multi-step autonomous) | End-to-end task completion | Tool selection, error recovery, outcome correctness |
| **Search/RAG** | Retrieval + generation quality | Retrieval precision, answer grounding, citation accuracy |

Each type needs fundamentally different evaluation. An agent eval that only checks final output misses 80% of failure modes (tool selection, state management, recovery).

**For agents and multi-step systems:** Decompose into sub-agents before evaluating. A contract risk analyzer isn't one agent — it's PDF extraction → key term extraction → rule comparison → risk classification → guardrails. Evaluate each component separately. Not all need AI evals — PDF-to-text is deterministic and testable with assertions. Focus expensive evaluation on the components where ML judgment matters most.

**Risk identification for components:** For each sub-agent, ask: Is ML even necessary here? Do I have training/eval data? Can it meet the accuracy bar users expect? What laws or policies constrain it? Can domain experts reliably judge its output? Components that fail these checks are your high-risk eval priorities.

**2. What's your product maturity?**

| Stage | What You Should Be Doing | What You Shouldn't |
|-------|--------------------------|-------------------|
| **Pre-launch** (< 50 real outputs) | Use the product yourself. Journal failures. | Build automated evals |
| **Early** (50-500 outputs) | Error analysis on 50-100 traces. Build first failure taxonomy. | Optimize for eval scores |
| **Growing** (500-10K outputs) | Separate capability evals (hard, low pass rate) from regression evals (should be ~100%). Validate judges. | Assume your initial taxonomy is final |
| **Mature** (10K+ outputs) | Promote saturated capability evals into regression suite. Build new capability benchmarks. Monitor for drift. | Stop reading traces |

**3. Can you name your top 5 failure modes from memory?**

If no → you haven't done enough error analysis. Stop here and go look at your data. Everything else is premature.

If yes → proceed. Your failure taxonomy IS your eval framework. Each failure mode becomes an evaluator.

### Error Analysis: The Foundation

This is the highest-ROI activity in AI product development. Not optional — foundational.

**What it looks like in practice:**
- Pull 100 representative traces (user query → system reasoning → tool calls → retrieved docs → final output)
- Read each trace yourself or with a domain expert who becomes the quality voice
- Write open-ended notes on anything wrong, surprising, or unexpected. Focus on the FIRST failure in each trace — upstream errors cascade
- This is journaling, not labeling. No rubric. No categories. Just observe.

**Then cluster into failure taxonomy.** Let categories emerge from data, not from a predetermined rubric. Count failures per category. Your top 3-5 categories are your evaluation priorities.

**Real example:** A real estate CRM assistant's error analysis revealed: Failed to transfer to human (8), Inappropriate tour rescheduling (7), Excessive confirmation requests (4), Misunderstood inquiry type (4), Claimed unavailable data access (3). None caught by "helpfulness score."

**When you lack production data:** Generate structured synthetic traces using 3+ dimensions of variation (persona × complexity × topic). Generate tuples manually, convert to natural queries in a SEPARATE prompt. Never ask an LLM for "50 test queries" — you'll get 50 versions of the same question.

**Diagnostic question:** When was the last time a new failure mode surprised me? If >4 weeks ago, I've stopped looking.

### OPEN CODING → AXIAL CODING (Husain + Shankar methodology)

The Error Analysis section above tells you to "let categories emerge from data." That direction is right but vague. Hamel Husain and Shreya Shankar formalized the workflow as open coding → axial coding → selective coding — the same qualitative research methodology used in social science, applied to AI traces.

The methodology is rigorous because the stakes are. Your failure taxonomy IS your eval framework. Get it wrong and you spend the next year measuring the wrong things.

#### Step 1: Open Coding

Read 50-100 traces. For each one, write a label that describes what's wrong, what's notable, or what's surprising. No schema. No predetermined categories. The labels can be long, repetitive, contradictory across traces. That's expected.

**The discipline:**
- One trace at a time. Don't batch — the cognitive load of comparison early kills the methodology.
- Label freely. "Refused but should have helped." "Hallucinated a regulation that doesn't exist." "Confidently wrong about pricing." "Tone too formal for casual user." "Ignored the second half of the question." These are all legitimate open codes.
- Domain expertise matters. The person doing open coding must understand what "good" looks like in this domain. Outsourced annotators break the cycle — they don't know what to notice.
- One pass through 50-100 traces takes 4-6 hours. Block the time. Don't try to do it in 30 minutes between meetings.

**The output:** A spreadsheet with one row per trace and a free-text label column. At the end of step 1, you have ~80 unique labels across 80 traces (with some natural duplication).

**The trap:** Starting with a schema. The moment you have a predefined list of failure categories, you stop seeing new ones. Your evals will reflect the categories you imagined, not the ones in the data.

#### Step 2: Axial Coding

Now cluster the labels. Read through your 80 labels. Group ones that describe the same underlying failure. The clusters are emergent — you find them; you don't impose them.

**The discipline:**
- Sort labels by similarity. Make piles.
- Name each pile with a short, specific category. Not "quality issues" — "fabricated regulatory citations." Not "user experience problems" — "refusal triggered by routine request."
- Some labels won't cluster. They're outliers — interesting, but rare. Park them separately.
- Some piles will be huge. Split them — usually they're hiding 2-3 sub-failures that need separate evaluators.
- Some piles will contain 1-2 labels. Park them too — not enough signal yet, but worth tracking.

**The output:** A taxonomy of 5-12 failure categories, each backed by 3+ traces from the open coding pass. The taxonomy is your eval framework — every category becomes a candidate evaluator.

**The trap:** Forcing labels into existing categories. If a label doesn't fit, that's a signal. Either it's a new category, or your axial coding is too coarse. Re-cluster, don't force.

#### Step 3: Selective Coding

You don't have time to build evaluators for 12 failure categories. Pick the 3-5 that matter most.

**The criteria:**
- **Frequency** — How often does this failure happen? (Count from the open coding pass. Categories with <3 traces aren't yet worth an evaluator.)
- **Severity** — How bad is the user impact? (Hallucinated regulations in a legal product is severe. Slightly formal tone is not.)
- **Customer-visibility** — Will users notice this failure, or is it invisible? (Invisible failures hurt long-term trust; visible failures hurt short-term acceptance. Both matter, but visible ones earn priority.)
- **Fixability** — Can this be addressed with prompt, retrieval, or harness changes? (If the failure requires a different model or fundamentally different architecture, the evaluator still matters but the priority is different.)

**The output:** A ranked list of 3-5 failure modes that become your initial eval suite. Each one gets a binary evaluator (pass/fail) per the existing "Choosing Your Evaluator Type" section above.

**The trap:** Picking by what's easy to evaluate, not what matters. A failure mode that's hard to detect with code is *more* important to evaluate, not less — because no one else is catching it.

#### The Cross-Domain Insight

The 0.1% angle: **the same methodology works on user interviews.** Open coding → axial coding → selective coding is the proven workflow for any unstructured data — AI traces, user research transcripts, support tickets, customer feedback emails.

This is one mental model, two data sources. Cross-link to the `interview-synthesis` skill being built in parallel — when you internalize the methodology for AI traces, you can apply it to user interviews without learning a new framework. The discipline transfers.

The deeper point: AI evaluation and qualitative user research are the same craft. Both are about converting unstructured signal into structured insight without imposing a frame too early. PMs who treat them as separate disciplines build worse products in both directions.

#### When to Re-Run the Full Cycle

Open → axial → selective coding is not a one-time setup. Re-run it:

- **Quarterly** — to catch new failure modes that emerged from changing user behavior or model upgrades
- **After a model swap** — the failure modes shift; old taxonomy may not fit
- **After a major prompt rewrite** — the system you fixed in the prompt may now have different fragility patterns
- **When the eval suite plateaus** — if your existing evaluators all score 95%+ but users still complain, your taxonomy is stale; re-discover

The full cycle takes 6-10 hours. It's the highest-leverage 6-10 hours an AI PM spends per quarter.

### Choosing Your Evaluator Type

For each failure mode, ask: **Can I catch this with code?**

| If... | Then... | Cost |
|-------|---------|------|
| Failure is format/structure (wrong JSON, missing field) | Code-based eval (regex, assertions) | Cheap, fast, deterministic |
| Failure is a specification gap (unclear prompt) | Fix the prompt first. Don't build an evaluator for a spec bug. | Free |
| Failure requires judgment AND persists after prompt fixes | LLM-as-judge (binary pass/fail on ONE narrow failure mode) | $0.01-0.10/eval |
| You're not sure what "good" looks like yet | Human review. Build judgment before automating it. | Expensive but necessary |

**Why binary over scales?** Binary forces clear thinking. Decompose to multiple binary checks for nuance rather than using one Likert scale. "Does the response cite sources? (Y/N)" + "Are cited sources real? (Y/N)" beats "Citation quality: 3.7/5."

### Agent Harness Eval Concepts

When evaluating agents, distinguish clearly between two concepts:
- **Evaluation harness**: The infrastructure running evals (test framework, metrics collection, result tracking).
- **Agent harness/scaffold**: The system that enables model agency (prompt structure, tool bindings, error recovery mechanisms, state management).

You're evaluating both together, not just the model. A strong model with weak scaffolding fails due to tool selection errors or state corruption, not capability gaps. A weak harness makes even capable models look bad because failures aren't detected or tracked properly.

For agent evals specifically, adopt this metric distinction:
- **pass@k (development)**: Did the agent succeed on at least one of k attempts? Useful for identifying when a solution is theoretically possible.
- **pass^k (production readiness)**: Does the agent succeed consistently across k trials? This is your shipping threshold — inconsistency is not acceptable in production.

### Agent-Type-Specific Eval

Different agent architectures need different evaluation approaches. Use this table to tailor your evaluators:

| Agent Type | Primary Success Metric | Evaluator | Notes |
|------------|----------------------|-----------|-------|
| **Coding agent** | Correct implementation | Deterministic graders (unit tests + integration tests) | Code quality rubric: readability, efficiency, style |
| **Conversational agent** | Task completion + interaction quality | Multidimensional: task success (binary) + turn count (< threshold?) + interaction quality (user satisfaction signal) | Set turn limits to catch infinite loops |
| **Research/reasoning agent** | Answer accuracy with evidence | Groundedness (claims backed by sources) + coverage (all key aspects addressed) + source quality (recent, authoritative, no hallucinated citations) | Verify sources exist and support claims |
| **Computer-use agent** | State verification + outcome correctness | Real/sandboxed environment replay + page state validation (before/after screenshots) + backend state checks (DB records, API responses) | State corruption is the #1 failure mode — validate it explicitly |

### Eval Saturation Problem

When agents achieve high pass rates (85%+), your eval stops being useful — you hit a ceiling where meaningful improvements don't register. This creates false confidence: the metric plateaus but the product still has real problems.

**Solution:** Refresh with harder problems. Replace 20–30% of your eval dataset monthly with production-derived failure cases and edge cases from real usage. Track an "eval difficulty score" by measuring your baseline model's pass rate on fresh examples — if it's consistently >95%, your eval is too easy. Aim for 60–75% baseline pass rate on newly added examples.

Stale evals → false confidence → undetected production issues.

### Validating Your LLM Judge

If you use LLM-as-judge, treat it as a classifier — validate it like one.

- Label 100 outputs pass/fail yourself (domain expert, not outsourced)
- Split: 20% few-shot examples → 40% dev set (iterate judge prompt) → 40% held-out test
- Measure True Positive Rate AND True Negative Rate separately
- Do NOT use "accuracy" — a judge that says "pass" on everything is 95% accurate if 95% of outputs pass
- TPR < 80% or TNR < 70%? Refine the judge prompt or switch models
- Anthropic found judge accuracy improvements from 42% to 95% through prompt iteration alone

**Diagnostic question:** If I showed my judge's decisions to my domain expert, how often would they disagree? >20% = judge needs work.

### Eval Cadences

Three rhythms, each serving a different purpose:

- **On every change (CI/CD):** Code-based evals. Deterministic checks. Block deployment on failure. Run in seconds.
- **Weekly (monitoring):** LLM-as-judge on sampled production traces. Flag emerging failure patterns. Trigger review if new category appears.
- **Monthly (deep review):** Human error analysis on 100+ fresh traces. Update failure taxonomy. Refine or retire evaluators.

**Regression thresholds:** Set BEFORE deployment. "If pass rate on [evaluator] drops below X%, block deploy." A 70% pass rate on a challenging eval > 100% on an easy one. If you're passing 100%, your eval isn't challenging enough.

### Setting Your Quality Bar

Don't pick thresholds from thin air. Four inputs determine your bar:

- **Customer tolerance:** Ask users directly — "If we get 7 out of 10 key terms right, is that useful?" Their answer sets your floor.
- **Leadership/legal constraints:** What has been promised to boards, customers, regulators? This sets your ceiling.
- **Competition benchmarks:** Run competitors' products (or foundation model baseline) through YOUR eval. This is your market floor.
- **Progressive release:** Start with a low bar at measurement launch (1% of users), raise it at beta, raise again at GA. Each release adds value AND learning from real interactions. You iterate the quality bar, not just the product.

### Adversarial Testing (Red Teaming)

Before launch, ask: **What happens when users actively try to break this?** Not just edge cases — intentional attacks. Prompt injection, encoded inputs, policy-violating requests disguised as legitimate ones.

You don't need a dedicated red team. Ask: Can I automate adversarial probing for my top 3 risk categories (harm, bias, policy violation)? If your agent survives 40 targeted attacks across varying complexity, you have baseline confidence. If it doesn't, you've found real failures to fix before users do.

### Connecting to Business Outcomes

Eval pass rates are internal. Users don't care about your eval scores. Ask:

- For each failure mode you fixed: **what user behavior should change?** Track the correlation.
- If eval improves but user behavior doesn't → you're measuring the wrong thing.
- Present findings as stories, not dashboards. Show: top failure modes, frequency, impact, fixes already made.

### Criteria Drift

Your evaluation criteria WILL evolve. Shankar et al. showed "criteria drift" — you need criteria to grade outputs, but grading outputs helps you define criteria. Some criteria only emerge after observing specific model outputs.

**What this means:**
- Your initial failure taxonomy is a hypothesis
- Merge or split categories as understanding deepens
- Document WHY criteria changed (not just what)
- Refresh 20-30% of eval examples monthly with recent production traces
- Maintain a "golden set" (50-100 curated examples) as your regression anchor

## KEY DIAGNOSTIC QUESTIONS

Use these to figure out what YOUR product needs — not to check boxes:

- **What's actually breaking?** Not theoretically — what IS breaking when real users interact with this?
- **What kind of system am I evaluating?** Chatbot, copilot, agent, search each need different approaches.
- **Where am I in maturity?** Pre-launch, early, growing, mature each have different eval needs.
- **Am I measuring what matters to users, or what's easy to measure?** If your eval doesn't map to user behavior, it's vanity.
- **Have I personally read 50+ traces this month?** If not, your framework is theoretical.
- **What's the cost of my eval pipeline per week?** LLM judge on 10K examples at $0.01 = $100/run. Daily = $3K/month.
- **Am I evaluating the outcome or the transcript?** For agents, both matter — a correct answer via wrong tool selection is a ticking time bomb.
- **What does "good enough" look like for this specific feature?** Not in general — for THIS use case, with THESE users, at THIS price point.
- **Have I decomposed my agent into sub-agents?** Which components actually need AI evaluation vs. deterministic testing? Don't eval everything equally — focus expensive evaluation on high-risk components.
- **What's my quality bar source?** Customer tolerance × leadership commitments × competitive floor × model baseline. If you can't name all four inputs, your threshold is arbitrary.
- **What happens when users actively try to break this?** If you haven't tested adversarial inputs, you're launching blind.

## REALITY CHECK

- **Evals are a practice, not a product.** No tool replaces the work of understanding your failures.
- **Don't outsource error analysis.** External annotators break the feedback loop. Domain experts must label.
- **Eval-driven development is usually wrong.** Writing evaluators before seeing failures sounds rigorous but you can't anticipate where LLMs break. Exception: known hard constraints ("never mention competitors").
- **One-sided evals hide problems.** Test what should succeed AND what should fail. Only testing "should do X" misses dangerous false positives.
- **Shared state corrupts agent evals.** Each trial needs clean state — cached data, modified files, or leftover context from previous runs invalidates results.
- **The model is not the product.** Evaluation is about whether your product works for users, not whether the model is capable.
- **Eval costs 10-100x building cost.** Every prompt change, new component, or model switch requires re-evaluating edge cases. Budget for this from day one.
- **Evaluation IS the moat.** Anyone can access the same foundation models. The differentiator is attention to detail — understanding your domain's failure modes deeply enough to catch what competitors miss. This is not overhead; this is your product advantage.

## QUALITY GATE

- [ ] I can name my top 5 failure modes from memory
- [ ] Each failure mode has a dedicated evaluator (code-based or LLM-judge, binary pass/fail)
- [ ] LLM judges validated: TPR and TNR measured on held-out human-labeled set
- [ ] Eval approach is tailored to my system type (chatbot/copilot/agent/search)
- [ ] Production trace review happening at regular cadence (not just launch)

## WHEN WRONG

- You haven't used the product yourself yet (use it before evaluating it)
- You're in week 1 of a prototype (journal observations, don't build eval infrastructure)
- The system is fully deterministic (test with assertions, not evals)
- Eval becomes a reason not to ship (it should accelerate shipping by catching real problems)
- Stakeholders want a single quality number ("92% accurate") — push back with the failure taxonomy instead
- You're following this skill as a recipe instead of using it to diagnose your specific situation

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5:
1. State the recommendation
2. Name the key trade-off
3. Acknowledge the biggest risk
4. Define the next action

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable 10x more impactful. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
