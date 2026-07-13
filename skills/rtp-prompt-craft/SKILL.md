---
name: prompt-craft
description: "How to actually write good prompts — the writing craft, not the process. Prompts are engineering artifacts, not creative writing: the craft has principles, and the counterintuitive first move is to write what the model CANNOT do (hard constraints) before what it should, because LLMs are more consistent at avoiding specific patterns than following general positive ones. Covers the 6-step framework, technique selection, cost-per-success, and the vibe-coding PRD→prototype pattern. Distinct from prompt-as-product (versioning/deployment) and context-spec (what information reaches the window). Use when writing or improving a system prompt, or debugging why one underperforms. Do NOT use when the problem is task decomposition or a model capability gap, not wording. Pairs with: prompt-as-product (the lifecycle), context-spec (the architecture), eval-framework (measures both), judgment-guard (shared make-tacit-explicit backbone). Triggers: 'write a prompt', 'improve this prompt', 'system prompt', 'few-shot'."
imports:
  - determinism-compass
  - prompt-as-product
  - eval-framework
---

# Prompt Craft

**The objective:** write a system prompt that survives real production, and diagnose why one doesn't — for the PM who owns what the AI must never do, how it handles ambiguity, and what the user sees.

## The one idea

You write a prompt, test it on three examples, and it works — ship it. In production it fails on 40% of real inputs: the messy, ambiguous, adversarial ones you never tested. You patch by adding instructions; the prompt bloats to 3,000 tokens; cost is now 4× what you budgeted; and you cannot explain why a five-word change broke everything.

The root cause is a category error: **prompts get treated as creative writing when they are engineering artifacts.** Creative writing has taste; engineering has *principles*, and violating them produces the same predictable failures every time (the kitchen-sink prompt where every task interferes with the others; the demo-magic prompt that works on clean data and dies on reality; the set-and-forget prompt that drifts as the world changes). The craft is learnable, testable, and repeatable — which is the whole reason it's a skill and not a knack.

And the most counterintuitive principle is the one to lead with: **write what the model CANNOT do before what it should.** LLMs are measurably more consistent at *avoiding a specific pattern* than at *following a general positive instruction* — "never cite a source that isn't in the provided context" is a guardrail; "always be accurate" is a wish. So the compliance hierarchy runs hard constraints (NEVER/ALWAYS) > structural formatting (XML/templates) > positive instructions ("be helpful") > implicit hope. Most prompts are written backwards — vague positives first, hoping the model infers intent. Flip the order, and half the failures never happen.

## How to use this skill

1. **Run the 6-step framework** for a production system prompt — constraints → structure → meta-prompt → 20/60/20 test → evals → hill-climb. (THE 6 STEPS.)
2. **Ship a reasoning trail** with any AI-assisted output, so a one-off correction becomes compounding calibration. (THE REASONING TRAIL.)
3. **Vibe-code to think, not to ship** — turn a PRD into a clickable prototype in ~10 minutes to sharpen decisions before engineering invests. (VIBE-CODING.)

*(If the question is versioning, A/B testing, or release process, that's `prompt-as-product` — this skill is the writing; that skill is the change management. If it's what *information* reaches the window, that's `context-spec` — the architecture, not the wording.)*

## KEY TERMS (plain language)

- **Hard constraint** — a specific NEVER/ALWAYS rule ("never cite a source not in context"); the highest-compliance instruction type.
- **Structure-triggers-quality** — the prompt's *format* activates different training-data patterns; a well-structured document triggers higher-quality responses (XML for Claude, JSON/markdown for GPT).
- **The 20/60/20 split** — a test set that is 20% happy path, 60% edge cases, 20% adversarial — because production traffic is mostly edge cases, not the demo.
- **Hill-climb** — climb for quality first (longest, most detailed prompt that hits the target), then descend for cost (compress one element at a time, keeping only what holds the evals).
- **Cost-per-success** — total API cost ÷ *successful* outcomes (not per call); at 60% acceptance, your real cost is ~1.67× the API cost.
- **Meta-prompting** — using the model to optimize its own prompt from failure data (fixes wording, not architecture).
- **Kitchen sink** — one mega-prompt doing classification + routing + generation + safety at once, each task interfering with the others.
- **Reasoning trail** — a 3-line record shipped with AI-assisted output (what the AI produced / what you changed & why / one calibration sentence) that turns a correction into a reusable lesson.
- **Evidence tiers below** — the cost-per-day and "5–10× faster" figures are ⚠ practitioner/illustrative; measure your own.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). **Go deep** for a production system prompt or an underperforming one. **Skip** if you need versioning/A-B/release (that's `prompt-as-product`) or the problem is *what information reaches the model* (that's `context-spec`). Then route depth and output format.

## THE 6 STEPS

1. **Start with hard constraints — lock down failure modes.** Write the top 3 things the model must NEVER do and the top 3 it must ALWAYS do, specific and testable. Hard constraints create guardrails; soft instructions create suggestions.
2. **Structure triggers quality.** Use the target model's native format (Claude → XML tags `<hard_constraints>`, `<task_instructions>`, `<output_format>`, `<examples>`; GPT → JSON + markdown + role separation; open-source → simple markdown). *Why it's a PM concern, not just engineering:* what goes in each section is a product decision — the constraints (what it must never do), the edge-case handling (how to treat ambiguity), the output format (what the user sees). Engineering implements; product specifies.
3. **Use meta-prompting** — after you have a working v1 and failure data, have the model rewrite itself ("identify the top 3 weaknesses, fix with hard constraints + specific examples + structure, predict each improvement, ≤150% of current tokens"). *When NOT to:* when the problem is conceptual (wrong task decomposition), not textual — meta-prompting optimizes wording, not architecture.
4. **Test with the 20/60/20 split.** 10 cases per category (30 minimum): 20% happy path, 60% edge (malformed, ambiguous, multi-language, angry users, partial info — where production lives), 20% adversarial (extract the system prompt, inject competing instructions, bypass safety). Run, find the top 3 failure patterns, fix each *explicitly* in the prompt, re-run until edge-case pass rate >85%.
5. **Build multi-dimensional evals.** Accuracy (domain-set), format compliance (95%+), safety (100% on known attacks), cost-per-success (below the PRD ceiling), latency (P95 within SLA). *The trap:* optimizing one dimension at the expense of others — +5% accuracy for 2× tokens is usually wrong.
6. **Hill-climb — quality first, cost second.** Phase 1: write the longest, most detailed prompt that hits your quality target (5–8 examples, every edge handler; ignore cost). Phase 2: compress one element at a time, re-running the full eval after each removal — keep it if metrics hold, restore if they drop. *Cost economics (⚠ illustrative, Claude Sonnet rates):* a 2,500-token prompt at 100K daily calls ≈ $3K/day; compressed to 500 tokens ≈ $600/day — ~$72K/month for the optimization. *When longer is correct:* complex/high-stakes tasks where a wrong output costs more than the extra tokens.

**Technique selection** (match to the task): Chain-of-Thought for reasoning/math (only effective on large models); Few-Shot for style/format (highest variability — test systematically); Chain-of-Table for structured data; nested/pipelined prompts for multi-step (each does ONE thing); if unsure, start with the Step-2 template and iterate.

## THE REASONING TRAIL — turn a correction into compounding calibration

Ship a three-line trail with any AI-assisted output: **(1)** what the AI produced first, **(2)** what you changed and why, **(3)** one calibration sentence naming where in *this* domain the AI is strong and where it's shaky ("good at X, unreliable on Y"). It works for any human-AI handoff — a prompt output, a code review, an eval writeup, an agent-output audit — because it captures the *delta between your criteria and the model's answer*, which is the reusable lesson. This is the same discipline as the prompt itself: **making tacit criteria explicit enough for a system (or a colleague) to act on** — the shared backbone with `judgment-guard`. *When wrong:* the trail only pays off if a manager actually reads it for coaching; rubber-stamped, it's documentation nobody reads. *Evidence:* conceptual; the "jagged frontier" calibration idea is ✅ Dell'Acqua/Mollick et al., HBS 24-013. *(Secondary application of HBR q2-20; primary home is judgment-guard's forced-pre-articulation checkpoint.)*

## VIBE-CODING — PRD to prototype in ~10 minutes (a thinking tool, not a product)

Turn a PRD into a clickable prototype using Claude / Cursor / v0 / Bolt — so the team can react to the flow before engineering invests (the pattern associated with Colin Matthews / Aparna Chennapragada). **Use it** when the PRD is fresh and unvisualized, a stakeholder is misreading the spec, or an engineer questions whether the flow makes sense — let them click it. **Don't** when it's mostly backend, when production parity matters, or when you're trying to *ship* (this is throwaway).

The template that produces usable prototypes: *"Generate a [HTML/React/Streamlit] prototype of [feature] demonstrating [user flow]. Use Tailwind, match this design system [paste tokens]. Show the happy path, one specific edge case, the error state, and the empty state. Single file, realistic mock data (not Lorem ipsum), 2–3 sample interactions. PRD below: [paste]."* The four states cover ~95% of the UX surface, and demanding all four forces the model to design, not pitch; realistic mock data makes stakeholders react to the real data shape. **The discipline: stop at 3 iterations** — after that you're polishing a thinking tool instead of making decisions. Vibe-coding produces the *artifact* (a mockup); the 6-step framework produces the *brain* (the production system prompt) — don't confuse the prototype with the product, and note it tells you nothing about production unit economics.

## DIAGNOSTIC QUESTIONS

- **Is your prompt doing ONE thing or many?** >2,000 tokens handling 3+ distinct tasks = kitchen sink → split into a pipeline.
- **Are your hard constraints specific enough to be testable?** "Be appropriate" is untestable; "never cite a source not in the provided context" is binary. Can you write a test that fails if it's violated?
- **What % of your test cases are edge cases?** 90/10 = testing the demo; 20/60/20 = matching production. Name 5 edge cases you've never tested.
- **Can you trace a production failure to a specific prompt weakness?** "The output was bad" allows no diagnosis; "it hallucinated because the citation constraint was missing for this input pattern" does.
- **What's your cost-per-success (not per call)?** If acceptance is 60%, effective cost is ~1.67× the API cost.

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

Three "craft" skills act on the model's input; keep them distinct:

- **`rtp-prompt-as-product`** *(import)* — the *lifecycle*: versioning, A/B testing, rollback, release process. Prompt-craft *writes* the prompt; prompt-as-product *manages its changes over time*. ("Why is output bad?" → here. "Why did quality drop after last week's change?" → there.)
- **`rtp-context-spec`** — the *architecture*: what information reaches the window and its token budget. Different object from the prompt text; a perfect prompt on bad context still fails.
- **`rtp-eval-framework`** *(import)* — measures both the prompt and its lifecycle; the 20/60/20 suite and the multi-dimensional evals live in its discipline.
- **`rtp-judgment-guard`** *(shared backbone)* — prompting and professional judgment are the same discipline at different altitudes: both are making tacit criteria explicit enough for a system to act on. The reasoning trail is the bridge.
- **`rtp-determinism-compass`** *(import)* — which parts of the output must be reproducible vs. can vary, which shapes how tight the constraints need to be.

## REALITY CHECK

- **Good craft** starts every prompt with hard constraints, matches structure to the model, tests 20/60/20, tracks cost-per-success, and compresses *after* hitting quality — each prompt doing ONE thing.
- **Not** vibes-based iteration ("this feels better"), demo-only testing, a mega-prompt handling everything, "be helpful and accurate" as the core instruction, or "tokens are cheap."
- **When 3+ optimizations don't hit target, the problem probably isn't the prompt** — check model capability, context correctness, task decomposition, and whether the eval measures the right thing.

## QUALITY GATE

- [ ] Hard constraints defined (NEVER/ALWAYS — specific, testable)
- [ ] Structure matches the target model (XML/JSON/markdown)
- [ ] Test suite built 20/60/20 (≥30 cases); edge-case pass rate >85%
- [ ] Multi-dimensional evals (accuracy, format, safety, cost-per-success, latency)
- [ ] Compression attempted after quality targets met; cost-per-success within budget
- [ ] Each prompt does ONE thing (complex tasks pipelined, not kitchen-sinked)

## WHEN WRONG

- The problem is task decomposition or a model capability gap, not wording.
- The retrieval/context feeding the prompt is broken (garbage in, garbage out) — that's `context-spec`.
- Early exploration with too little failure data to optimize against.
- You need process governance — that's `prompt-as-product`.

## TRADE-OFF LEDGER

By treating prompts as engineering artifacts, you bet that principled craft (constraints-first, 20/60/20-tested, cost-per-success-tracked) beats vibes-based iteration — that the predictable failures are worth preventing up front. You give up the speed of "write it and ship it" for the discipline of a test suite and an eval. **Reversible?** Fully — a prompt is a text file. **The hidden trade:** the failure mode is *optimizing the prompt when the problem is elsewhere* (decomposition, context, capability) — the 3-strikes rule guards against it. **Confidence: High** — the compliance hierarchy and the edge-case-heavy reality of production are well-established. What would change it: a genuine capability gap no wording fixes, or a one-off throwaway where craft is overkill.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (the prompt, constraints-first and 20/60/20-tested), the key trade-off (craft discipline vs. ship-it speed), the biggest risk (optimizing wording when the real problem is decomposition, context, or capability), and the next action (the test suite + the cost-per-success number, with an owner).

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the compliance hierarchy as a pyramid (hard constraints at the wide, high-compliance base → structure → positive instructions → implicit hope at the thin top), beside the 20/60/20 test split and the hill-climb curve (quality up, then cost down). So a viewer sees the two moves that prevent most failures: constrain first, test the edges. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
