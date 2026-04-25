---
name: rtp-prompt-craft
id: prompt-craft
title: Prompt Craft
category: craft
description: How to actually write good prompts. The writing craft — hard constraints, structure-triggers-quality, test splits, cost economics, model-specific formatting. Distinct from prompt-as-product (which covers versioning and process). Use when writing or improving system prompts, optimizing prompt quality, or debugging why a prompt underperforms.
difficulty: intermediate
version: "1.0"
imports:
  - determinism-compass
  - prompt-as-product
  - eval-framework
author: ai-pm
last_updated: 2026-04-12
---

## DEPTH DECISION

**Go deep** if: you're writing a production system prompt, optimizing an underperforming prompt, or need to balance quality against cost. Read the full 6-step framework.

**Skim to Step 1 + Step 4** if: you have a working prompt and need to tighten failure modes or reduce cost.

**Skip** if: you need prompt versioning, A/B testing, or release process — that's `prompt-as-product`. This skill is the writing craft; that skill is the change management.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE RELATIONSHIP: PROMPT-CRAFT vs PROMPT-AS-PRODUCT

These two skills are deliberately separated. Confusing them leads to teams that manage prompts rigorously but write them poorly — or write brilliant prompts with no process around them.

| Question | Which Skill |
|----------|-------------|
| How do I write a prompt that actually works? | **Prompt-Craft** (this skill) |
| How do I version, test, and deploy prompt changes? | **Prompt-as-Product** |
| Why is my prompt producing bad output? | **Prompt-Craft** — diagnose the writing |
| Why did output quality drop after last week's change? | **Prompt-as-Product** — trace the version |
| How do I structure a system prompt from scratch? | **Prompt-Craft** — use the 6-step framework |
| How do I A/B test two prompt variants? | **Prompt-as-Product** — use the release process |

**The workflow:** Prompt-Craft writes the prompt. Prompt-as-Product manages its lifecycle. Eval-Framework measures both.

---

## THE TRAP

**The "Vibes-Based Prompting" Problem**

You write a prompt, test it on 3 examples, declare it works. In production, it fails on 40% of real inputs — the messy, ambiguous, adversarial ones you never tested. You iterate by adding more instructions, the prompt bloats to 3,000 tokens, and now cost is 4x what you budgeted. You can't explain why a five-word change broke everything.

Root cause: prompts are treated as creative writing instead of engineering artifacts. The craft has principles. Violating them produces the same predictable failures every time.

**Three failure modes:**
1. **Kitchen Sink** — One massive prompt handling classification, routing, generation, and safety simultaneously. Each task interferes with the others.
2. **Demo Magic** — Works on clean test data, fails on real production inputs. You tested the 20% easy path, not the 60% edge cases.
3. **Set and Forget** — Shipped and never updated. User needs evolve, model capabilities change, edge cases accumulate. The prompt drifts from reality.

---

## THE PROCESS: 6-STEP PROMPT OPTIMIZATION FRAMEWORK

### Step 1: Start With Hard Constraints (Lock Down Failure Modes)

Begin with what the model CANNOT do, not what it should do.

**Pattern:**
```
NEVER:
- [TOP 3 FAILURE MODES - BE SPECIFIC]
- Use meta-phrases ("I can help you with that", "let me assist")
- Provide information you are not certain about

ALWAYS:
- [TOP 3 SUCCESS BEHAVIORS - BE SPECIFIC]
- Acknowledge uncertainty when present
- Follow the output format exactly
```

**Why this works:** LLMs are more consistent at avoiding specific patterns than following general positive instructions. "Never fabricate citations" is more reliable than "Always be accurate." Hard constraints create guardrails; soft instructions create suggestions.

**The hierarchy:**
1. Hard constraints (NEVER/ALWAYS) — highest compliance
2. Structural formatting (XML tags, templates) — high compliance
3. Positive instructions ("Be helpful") — moderate compliance
4. Implicit expectations (hoping the model infers intent) — lowest compliance

Most prompts are written backwards — starting with vague positive instructions and hoping. Flip the order.

### Step 2: Structure Triggers Quality (Format Signals Training Data)

The format of your prompt affects which training data patterns the model activates. Well-structured documents trigger higher-quality responses.

**Model-specific formatting:**
- **Claude (Anthropic):** XML tags work best. `<system_constraints>`, `<task_instructions>`, `<examples>`. Claude's training emphasizes structured XML contexts.
- **GPT-4 (OpenAI):** JSON structure and markdown headers. System/user/assistant role separation.
- **Open-source models:** Simple markdown. Fewer structural assumptions in training.

**The production template:**
```xml
<system_role>
You are [SPECIFIC ROLE], not a general assistant.
You [CORE FUNCTION] for [TARGET USER].
</system_role>

<hard_constraints>
NEVER:
- [Failure mode 1]
- [Failure mode 2]
- [Failure mode 3]

ALWAYS:
- [Success behavior 1]
- [Success behavior 2]
- [Success behavior 3]
</hard_constraints>

<context>
Current user: [USER_CONTEXT]
Available tools: [TOOL_LIST]
Key limitations: [SPECIFIC_LIMITATIONS]
</context>

<task_instructions>
Your job is to [CORE TASK] by:
1. [Step 1 — specific action]
2. [Step 2 — specific action]
3. [Step 3 — specific action]

If [edge_case_1], then [specific_response].
If [edge_case_2], then [specific_response].
</task_instructions>

<output_format>
[Exact structure the output must follow]
</output_format>

<examples>
[2-3 examples: happy path, edge case, complex scenario]
</examples>
```

**Why structure matters for PMs:** This isn't a developer concern. The PM decides what goes into each section — the hard constraints are product decisions (what the AI must never do), the edge cases are product decisions (how to handle ambiguity), the output format is a product decision (what the user sees). Engineering implements; product specifies.

### Step 3: Use LLM Self-Improvement (Meta-Prompting)

Don't optimize prompts manually through trial and error. Use the model itself:

```
You are a prompt optimization specialist.

CURRENT PROMPT:
[Paste the prompt]

PERFORMANCE DATA:
- Top 3 failure modes: [List them]
- Target use case: [Describe]

TASK:
1. Identify the top 3 weaknesses in this prompt
2. Rewrite to fix those weaknesses using:
   - Hard constraints over soft instructions
   - Specific examples over generic guidance
   - Structured format over free text
3. Predict the improvement for each change

CONSTRAINTS:
- Maintain core functionality
- Cannot exceed 150% of current token count
- Must include failure mode handling
```

**When to use:** After you have a working v1 prompt and performance data. Not on first drafts — you need failure modes to feed the meta-prompt.

**When NOT to use:** When the problem is conceptual (wrong task decomposition), not textual (wrong phrasing). Meta-prompting optimizes wording. It doesn't fix architecture.

### Step 4: Test With the 20/60/20 Split

The most common prompt testing failure: over-testing happy paths, under-testing reality.

**Build your test set as:**
- **20% happy path** — Standard, clean, well-formatted inputs. The demo scenarios.
- **60% edge cases** — Unusual inputs, malformed data, ambiguous requests, multi-language, angry users, partial information. This is where production lives.
- **20% adversarial** — Attempts to break the prompt, extract system instructions, inject competing instructions, bypass safety constraints.

**Why 60% edge cases?** Because production traffic is 60%+ edge cases. The clean demo inputs are the minority. Teams that test 80% happy path / 20% edge case ship prompts that fail on the majority of real interactions.

**Process:**
1. Write 10 test cases per category (30 total minimum)
2. Run the prompt against all 30
3. Identify the top 3 failure patterns
4. Address each failure explicitly in the prompt (add to hard constraints or edge case handling)
5. Re-run. Iterate until edge case pass rate > 85%

### Step 5: Build Evaluation Criteria

Define what "good" means before optimizing. Five dimensions:

| Dimension | What to Measure | Target |
|-----------|----------------|--------|
| **Accuracy** | Does it get the right answer? | Domain-specific (set in PRD) |
| **Format compliance** | Does output follow the required structure? | 95%+ |
| **Safety** | Does it handle adversarial inputs correctly? | 100% on known attack patterns |
| **Cost efficiency** | Token usage per successful output | Below cost ceiling (set in PRD) |
| **Latency** | Response time acceptable for UX? | P95 within SLA |

**The trap:** Optimizing one dimension at the expense of others. Improving accuracy by 5% while doubling token cost is usually wrong. The eval criteria must be multi-dimensional.

### Step 6: Hill Climb — Quality First, Cost Second

**Phase 1: Climb for quality**
- Write the longest, most detailed prompt that achieves your quality target
- Include extensive examples (5-8)
- Add every edge case handler you've identified
- Ignore token cost temporarily
- Goal: hit your accuracy/safety/format targets

**Phase 2: Descend for cost**
- Systematically compress: remove one element at a time
- After each removal, run the full eval suite
- If metrics hold, keep the compression
- If metrics drop, restore and try a different compression
- Goal: minimum tokens that maintain quality targets

**Cost economics (real numbers):**
- Detailed prompt: 2,500 tokens @ 100K daily calls = ~$3,000/day (Claude Sonnet rates)
- Compressed prompt: 500 tokens @ 100K daily calls = ~$600/day
- That's $72K/month saved — worth the optimization effort

**When longer is correct:** Complex tasks requiring extensive context, high-stakes decisions where additional examples prevent costly errors, tasks where the cost of a wrong output exceeds the cost of extra tokens.

---

## VIBE-CODING — PRD TO PROTOTYPE IN 10 MINUTES

The 6-step framework above is for production system prompts. This section is for a different use case: turning a PRD into a working prototype in under 10 minutes using Claude, Cursor, v0, or Bolt.

The pattern is associated with Colin Matthews and Aparna Chennapragada — vibe-coding, PRD-to-prototype, AI-native prototyping. The principle: PMs no longer need an engineer to test whether a feature feels right. The PM writes a structured prompt, pastes the PRD, gets a working HTML/React/Streamlit prototype that demonstrates the user flow.

This is not production code. It's a thinking tool. A way to externalize the PRD into something the team can click through, react to, and stress-test before engineering invests real time.

### When to Vibe-Code

Use the pattern when:
- The PRD is fresh and the team has never seen the flow visualized
- A stakeholder is misreading the spec because they can't picture it
- A design review is coming up and a clickable artifact will sharpen feedback
- An engineer is questioning whether the flow makes sense — let them click through it
- You want to see your own design before committing to it

Don't use the pattern when:
- The feature is mostly backend logic with minimal UI
- Production parity matters (the prototype's design will mislead)
- You're trying to ship — vibe-coding is a thinking tool, not a delivery vehicle

### The Prompt Template

The structure below produces clickable prototypes in 5-10 minutes. Paste this into Claude (or your prototyping LLM of choice), filling the placeholders:

```
I have a PRD for [FEATURE_NAME]. Generate a [HTML | React | Streamlit] 
prototype that demonstrates [SPECIFIC_USER_FLOW].

Use Tailwind for styling. Match this design system:
[PASTE DESIGN.md FRONTMATTER OR DESIGN TOKENS HERE]

The prototype must show me:
- The happy path: [DESCRIBE THE CORE USER FLOW]
- The edge case: [DESCRIBE ONE SPECIFIC EDGE CASE — e.g., "what the user 
  sees when the AI has low confidence"]
- The error state: [DESCRIBE WHAT FAILURE LOOKS LIKE]
- The empty state: [DESCRIBE WHAT THE USER SEES BEFORE INTERACTING]

Constraints:
- Single file, no external dependencies beyond Tailwind CDN
- Runnable locally by opening the file in a browser
- Use realistic mock data, not "Lorem ipsum"
- Include 2-3 sample interactions that demonstrate the flow

PRD attached below:
[PASTE PRD]
```

The four placeholders (FEATURE_NAME, USER_FLOW, edge case, error state) are non-negotiable. Generic prompts produce generic prototypes. Specific prompts produce prototypes you can actually use to make decisions.

### Why Each Section Matters

**"[HTML | React | Streamlit]"** — Pick based on the audience. HTML for design reviews and stakeholder demos. React for engineering feasibility checks. Streamlit for data-heavy tools where the prototype needs real Python logic.

**"Use Tailwind for styling"** — Tailwind is the universal default. Models are trained heavily on it. Output looks polished without specifying classes manually. If you're matching a specific design system that doesn't use Tailwind, swap accordingly.

**"Match this design system"** — Critical. Without this, you get generic Bootstrap-looking output. With your DESIGN.md frontmatter, you get a prototype that looks like your product, which is what makes the artifact credible to stakeholders.

**"Show me the happy path / edge case / error state / empty state"** — The four states cover ~95% of UX surface area. Generic prompts produce only the happy path; the edge cases are where the design decisions actually live. Demanding all four forces the model to think through the design, not just the marketing pitch.

**"Realistic mock data, not Lorem ipsum"** — Lorem ipsum prototypes lie. Stakeholders react to the data shape and tone, not just the layout. Realistic mock data (real-looking customer names, real-looking dollar amounts, real-looking error messages) makes the prototype useful for real decisions.

**"Include 2-3 sample interactions"** — A static screenshot prototype is less useful than a clickable one. Asking for sample interactions ("user types a query → sees AI response → clicks 'show more'") forces the model to wire up actual JavaScript or React state.

### The 10-Minute Workflow

1. **Minute 0-2:** Open Claude (or Cursor / v0 / Bolt). Paste the prompt template. Fill placeholders.
2. **Minute 2-5:** Paste PRD. Hit send. Watch the model generate.
3. **Minute 5-7:** Save the output as a file (`prototype.html` or `App.tsx`). Open in browser.
4. **Minute 7-9:** Click through. Note what's right, what's wrong, what's missing.
5. **Minute 9-10:** Send Claude a follow-up: "The error state looks like a dead end. Add a 'try again' affordance and show what happens when the user retries." Iterate 1-2 times.

The discipline: stop at 3 iterations. After that, you're polishing a thinking tool, not making decisions. Move to the next prototype or commit to the design.

### Connecting Vibe-Coding to the 6-Step Framework

The 6-step framework (Steps 1-6 above) is for the production system prompt that runs *inside* the feature. Vibe-coding is for the demo prompt that *creates* the feature's prototype. Different layers:

- **Vibe-coding produces the artifact** — a clickable React/HTML mockup of the feature
- **Prompt-craft produces the brain** — the production system prompt that powers the feature's AI behavior

A team using vibe-coding to externalize the PRD into a prototype, then using the 6-step framework to engineer the production prompt that powers the real version, ships features 5-10x faster than teams that wait for engineering before they can see the design.

### What Vibe-Coding Doesn't Solve

- **Architecture decisions.** The prototype answers "does this flow feel right?" — not "is this the right system design?"
- **Performance and cost reality.** A prototype hitting Claude Sonnet at $0.003/1K tokens for a few demo interactions tells you nothing about production unit economics at 100K daily users.
- **Edge case coverage.** The model generates the edge cases you ask for. The ones it didn't think of (and you didn't either) are still landmines.
- **Production prompt engineering.** The system prompt inside the prototype is throwaway — likely 200 tokens of "you are a helpful assistant." When the real feature ships, you need the 6-step framework's hard constraints, structured templates, and 20/60/20 testing.

The pattern is a thinking tool. Use it to make better PRDs and faster decisions. Don't confuse the prototype with the product.

---

## KEY DIAGNOSTIC QUESTIONS

**On Prompt Architecture:**
- Is your prompt doing ONE thing or MANY things? (Kitchen Sink detector)

*Think through:* Task decomposition
*Low end:* Single prompt handles classification + generation + safety
*High end:* Separate specialized prompts, each doing one thing well
*Red flag:* Your prompt is > 2,000 tokens and handles 3+ distinct tasks
*Sharpen it:* Could you split this into 2-3 prompts that pipeline together?

- Are your hard constraints specific enough to be testable?

*Think through:* Constraint precision
*Low end:* "Be accurate" — untestable, means nothing
*High end:* "Never cite a source that doesn't appear in the provided context" — binary, testable
*Red flag:* Constraints use words like "appropriate," "reasonable," "helpful"
*Sharpen it:* Can you write a test case that would fail if this constraint is violated?

**On Testing Coverage:**
- What percentage of your test cases are edge cases?

*Think through:* Test distribution
*Low end:* 90% happy path, 10% edge — you're testing the demo, not production
*Mid range:* 50/50 — better, but adversarial coverage missing
*High end:* 20/60/20 split — matches production reality
*Red flag:* You've never tested with malformed input, multi-language, or adversarial prompts
*Sharpen it:* Name 5 edge cases your prompt has never been tested on

- Can you trace a production failure back to a specific prompt weakness?

*Think through:* Failure traceability
*Low end:* "The output was bad" — no diagnosis possible
*High end:* "The model hallucinated because the hard constraint on citation was missing for this input pattern"
*Red flag:* You fix failures by adding more instructions without understanding root cause

**On Cost Awareness:**
- What's your cost per successful output (not per API call)?

*Think through:* Cost-per-success = total API cost / successful outcomes
*Low end:* You track API cost but not success rate — so you don't know cost-per-success
*High end:* Cost-per-success tracked daily, segmented by task type
*Red flag:* Cost per success is 3x cost per call (meaning 2 out of 3 outputs fail)
*Sharpen it:* If acceptance rate is 60%, your effective cost per useful output is 1.67x the API cost

---

## PROMPTING TECHNIQUES — WHEN TO USE WHAT

Not every technique works for every task. Match the technique to the problem:

| Technique | Best For | Not For | Key Constraint |
|-----------|----------|---------|----------------|
| **Chain-of-Thought** | Math, logic, formal reasoning | Content generation, classification | Only effective on 100B+ parameter models |
| **Chain-of-Table** | Structured data, table processing, financial analysis | Free-text tasks | Requires tabular input |
| **Few-Shot Examples** | Style matching, format demonstration | Advanced reasoning (o1, R1 models) | Highest variability — test systematically |
| **Multi-Shot Conversations** | Customer support, multi-turn flows | Single-turn tasks | Shows conversation patterns, not isolated examples |
| **Nested/Pipelined Prompts** | Complex multi-step workflows | Simple single-step tasks | Each prompt does ONE thing |

**The decision:** If your task is reasoning-heavy, use Chain-of-Thought. If it's format-heavy, use Few-Shot. If it's multi-step, use Nested Prompts. If you're not sure, start with the production template from Step 2 and iterate.

---

## REALITY CHECK

**What good prompt craft looks like:**
- Every prompt starts with hard constraints (NEVER/ALWAYS)
- Structure matches the target model (XML for Claude, JSON for GPT-4)
- Test suite has 20/60/20 distribution (happy/edge/adversarial)
- Cost-per-success is tracked and within budget
- Prompt compression happened after quality targets were met
- Each prompt does ONE thing — complex tasks are pipelined

**What it doesn't look like:**
- Vibes-based iteration ("this feels better")
- Testing only on demo data
- One mega-prompt handling everything
- "Be helpful and accurate" as the core instruction
- No cost tracking ("tokens are cheap")
- Prompt written once and never revisited

---

## QUALITY GATE

**Prompt craft deliverables require:**
1. Hard constraints defined (NEVER/ALWAYS — specific, testable)
2. Structure matches target model (XML/JSON/Markdown as appropriate)
3. Test suite built with 20/60/20 split (minimum 30 cases)
4. Edge case pass rate > 85%
5. Cost-per-success calculated and within budget
6. Compression attempted after quality targets met

**Blocks shipping if:**
- No hard constraints (prompt relies entirely on positive instructions)
- Test suite is < 20 cases or > 50% happy path
- Edge case pass rate < 70%
- Cost per success unknown or exceeds budget by > 20%
- Single prompt handling 3+ distinct tasks (Kitchen Sink)

---

## WHEN WRONG

**This skill gives bad advice when:**
- The problem is task decomposition, not prompt wording (you need to rethink the architecture, not rewrite the prompt)
- The model genuinely can't do the task (no amount of prompting fixes a capability gap)
- You're in early exploration and don't have enough failure data to optimize against
- The prompt is fine but the retrieval/context feeding it is broken (garbage in, garbage out)
- You need process governance — that's `prompt-as-product`, not this skill

**Recovery:** If you've optimized the prompt 3+ times and quality still doesn't meet targets, the problem is probably not the prompt. Check: Is the model capable? Is the context correct? Is the task decomposition right? Is the eval measuring the right thing?

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
