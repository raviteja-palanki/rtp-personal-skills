---
name: context-spec
description: "Context engineering — the information architecture for reasoning, not the prompt. Everyone tunes the prompt and the model; the invisible 90% is how information flows from sources through layers into the window, and the killer fact is that models degrade at 50–60% of max context (the Pre-Rot Threshold), so context capacity ≠ context quality: a 128K window has a ~70K working budget. You engineer a token BUDGET across stacked layers, each with its own token cost, compaction strategy, and failure fallback — plus multi-agent context isolation and dynamic tool selection. Use when architecting an AI feature with retrieval, tools, or conversation state. Do NOT use for single-turn no-retrieval features (use determinism-compass). Pairs with: invisible-stack (it diagnoses the weak layer, this designs the build spec for all seven), prompt-craft (the prompt text vs. the architecture), determinism-compass, stress-test. Triggers: 'context engineering', 'context architecture', 'token budget', 'context window'."
imports:
  - invisible-stack
  - determinism-compass
  - stress-test
---

# Context-Spec — Engineering Information Architecture

**The objective:** design the token budget and layer architecture that feeds an AI feature's reasoning — before engineers guess and production fails — for the PM architecting anything with retrieval, tools, or conversation state.

## The one idea

The model has a 128K context window, so the team fills it — retrieve 20 documents, show the last 50 messages, include the full metrics dump. And quality gets *worse*. The team is baffled: more context should mean more to reason from.

Here is the fact that explains it, and it's the whole skill: **context capacity is not context quality.** Models degrade measurably at **50–60% of their maximum window** (◆ demonstrated in Claude evals) — a 128K window has a real *working* budget of ~70K tokens, and past that, adding information makes the model *worse*, not better, as the signal drowns in noise. Call it the **Pre-Rot Threshold**. Fill the window and you're reasoning in the degradation zone before you ever hit 100%.

So context engineering is not prompt writing — it is **information architecture for reasoning.** The prompt and the model are the visible part; the invisible 90% is *how information flows from its sources, through stacked layers, into the window* — and each layer (the system prompt, retrieved docs, tool results, observation history, conversation, scratchpad) has its own update frequency, reliability, latency, and token cost. You don't write a prompt; you engineer a **budget**: what gets which slice of ~70K tokens, when each layer compacts, and what happens when each one fails. Get the budget right and a small model reasons well; get it wrong and the best model reasons badly on a window stuffed past its Pre-Rot Threshold.

## How to use this skill

1. **Import invisible-stack first** — map all seven CONTEXT layers; this skill turns that map into a *token budget* with a number per layer. (THE PROCESS.)
2. **Allocate against the Pre-Rot Threshold, not the max window** — ~50–60% of the window is your real budget; every layer's slice, compaction trigger, and failure fallback fits inside it. (CONTEXT BUDGET.)
3. **Isolate agents and filter tools** — in a harness, each agent gets its own context scope; show the model 3–5 relevant tools, not the full catalog. (MULTI-AGENT ISOLATION + DYNAMIC TOOL SELECTION.)

## KEY TERMS (plain language)

- **Context engineering** — designing *what information reaches the model and how*, not the wording of the prompt; the architecture of the window.
- **Pre-Rot Threshold** — the point (~50–60% of max window) past which more context *degrades* reasoning; your real working budget (◆ Claude evals).
- **Layered action space** — the window isn't one blob; it's stacked layers (system prompt, retrieval, tool results, observations, conversation, scratchpad), each with a different update rate, reliability, latency, and token cost.
- **Compaction** — shrinking a layer to fit budget: *summarize* (extractive, keep citations), *offload* (move old context to external memory, retrieve on need), *reset* (clean slate + a structured handoff file).
- **Agent-as-tool** — when a tool result is large, spawn a sub-agent to extract the few relevant facts instead of dumping raw output into the main window (saves ~60–70% of tokens ⚠).
- **File-based handoff** — passing state between agent sessions via files (sprint-contract.json, build-log.txt), not by ballooning the conversation.
- **Multi-agent context isolation** — giving each agent in a harness only its own scope, so the evaluator can't make excuses for the generator it never should have seen.
- **Dynamic tool selection** — presenting only the 3–5 tools relevant to the task, not the full 50, so the model doesn't burn context reading irrelevant options.
- **Evidence tiers below** — ◆ Anthropic/Claude-disclosed · ⚠ practitioner estimate. Token-savings figures are ⚠; measure your own.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md). **Go deep** when architecting a feature with retrieval, tools, or conversation state. **Skip** for single-turn no-retrieval features or purely deterministic flows (use `determinism-compass`). Then route depth and output format. **Import `invisible-stack` first** — it maps the seven layers; this skill operationalizes that map into token/latency budgets.

## THE TRAP

You focus on the prompt and the model; the real problem is the invisible 90% — how information flows through the layers — and the assumption that **context capacity = context quality (wrong).** Three variants: **over-spec** (60-page context docs that delay shipping), **under-spec** (layers missing entirely, engineers guess, production fails), and **context bloat** ("retrieve 20 docs, show the last 50 messages" → past the Pre-Rot Threshold by message 3).

## THE PROCESS

Answer the practitioner questions first, in order:

1. **What's the actual usable context?** Not the max window — the Pre-Rot Threshold (128K → ~60–70K working). Allocate a token budget per layer inside it.
2. **Which tools are actually relevant?** Pre-filter to 3–5 for this task; don't show 50 and let the model waste context reading them.
3. **Where does context rot happen?** Trace one request end-to-end; find the layer where quality degrades (stale docs? ballooning history?) and fix *that* layer first.
4. **What can you compact?** Summarize retrieved docs, offload old conversation to external memory, strip tool results to essentials — every token saved is room for a better decision.
5. **What's the fallback when a layer fails?** Retrieval timeout, tool error, Constitution conflict — specify the exact UX and what information is dropped.

**The layered action space** — the window is stacked layers with different properties (illustrative budgets on a 128K → ~70K working window): System prompt (immutable, ~5K, 100% reliable) · Retrieved docs (per-request, ~15K, ~500ms, ~95%) · Tool results (per-call, ~5K, ~2s, 80–90%) · Observation history (continuous, ~10K, <10ms, reliable) · Conversation (live, ~20K, noisy) · Scratchpad (session, ~5K). Each has its own failure recovery: system → revert; retrieval → degrade to model-only; tool → fallback/cache.

**Anthropic context-management findings (◆ March 2026):** for long-running agents, periodic **full resets with a structured handoff file beat in-window compaction** (the reset cost is paid once per session; compaction's drift compounds with every summarization). The **agent-as-tool** pattern (sub-agent extracts facts from a >5K-token tool result) saves ~60–70% of tokens. **File-based communication** (agents read/write state files rather than passing summarized context) reduces pollution and makes handoffs explicit.

## CONTEXT BUDGET

Document token allocation per layer; the total must not exceed the Pre-Rot Threshold:

```
## Context Budget: [Feature]   Total window: [X]K   Pre-Rot working budget: [Y]K (~50–60% of max)
| Layer | Token budget | Update freq | Failure fallback |
| Constitution | [X]K | monthly | revert to previous version |
| Retrieved docs | [X]K | per-request | degrade to model-only |
| Tool results | [X]K | per-call | cached/fallback |
| Observation history | [X]K | continuous | summarize oldest |
| Conversation | [X]K | live | compact after N messages |
| Scratchpad | [X]K | session | clear on reset |
| TOTAL | ≤[Y]K | | must stay under Pre-Rot |
Compaction trigger: total > [Y]K → [summarize/offload/reset]   Reset every: [N msgs / M hrs]   Handoff files: [list]
```

**Compaction strategy per layer:** *summarize* retrieved docs >5 pages (extractive, keep citations — ~60–70% savings ⚠); *offload* conversation >30 messages to external memory (~80% savings, +~200ms retrieval ⚠); *compress* verbose tool results to key facts (~50% ⚠).

## MULTI-AGENT ISOLATION & DYNAMIC TOOL SELECTION

In a harness (planner → generator → evaluator), each agent gets its **own** context scope — bleeding causes bad decisions:

- **Planner:** brief + vision + constraints (no code, no tool results, ~15K) → outputs a sprint contract + architecture sketch.
- **Generator:** the sprint contract + codebase state + tool access (~40K) → outputs code, tests, build logs.
- **Evaluator:** success criteria + live app state + test results (no implementation details, ~20K) → outputs pass/fail + blockers.

**The isolation that matters:** if the evaluator sees the generator's full history, it starts *making excuses* for it ("time pressure was tight, so this is acceptable") — isolate success criteria from implementation context. Hand off via files (planner writes `sprint-contract.json` → generator writes `build-log.txt` → evaluator reads only the snapshot + results, not the reasoning). **Dynamic tool selection:** present only the task's tools (a Python request shows Python tools, hides SQL) — count visible tools at runtime; >10 means pre-filter, and log tool visibility to check post-hoc whether a hidden tool would have helped.

## WORKED EXAMPLES

**Simple — single-turn support bot** (128K window, ~90K Pre-Rot): system prompt 800 tokens (cached, 90% discount) + top-3 KB articles ~4K + question 200 + optional scratchpad 500 = ~5.5K used (6% utilization — no context pressure). *End-to-end:* retrieve 3 docs (0.4s) → assemble (system + docs + question ≈ 4.4K) → generate (0.8s) → guardrail (0.1s) = **1.3s, ~$0.003**. *Decisions:* if zero docs clear the relevance threshold (say 0.70), fall back to "here's our help center" — don't generate from model knowledge alone; set a retrieval timeout at 800ms → top-1 only if exceeded.

**Complex — code-analysis agent** (128K → 70K Pre-Rot): Constitution 8K + retrieved files 20K + tool results 5K + observations 15K + conversation 18K + scratchpad 4K = **70K at threshold**. Trigger: >70K → summarize observations + reset conversation; handoff: `analysis-summary.json`, `test-results.txt`.

## DIAGNOSTIC QUESTIONS

- **What's my actual working budget** (the Pre-Rot Threshold, not the max)? Allocate all layers inside it.
- **Which layer consumes the most tokens, and is that justified?** Measure a sample request end-to-end; is retrieval bloated, is conversation unbounded?
- **What happens when a critical layer fails?** Specify the exact UX and fallback data for each.
- **Am I showing the right tools or the full catalog?** Count visible tools; >10 → pre-filter.
- **If I reset context entirely, what state must survive?** If you can't answer, you haven't modeled the agent's memory.
- **Is latency budgeted?** Retrieval + tool + generation can eat most of a 6s SLA; where's the 10% retry margin?

## WHERE THIS SKILL MEETS THE REST OF YOUR STACK

- **`rtp-invisible-stack`** *(import — the pair)* — invisible-stack *diagnoses* which of the seven layers is capping quality; context-spec *designs* the build spec (token budget, compaction, fallback) for all seven. One finds, one designs — run in sequence.
- **`rtp-prompt-craft`** — the *prompt text* (how to phrase the instruction) vs. this skill's *architecture* (what information reaches the model at all). Different objects; both matter.
- **`rtp-prompt-as-product`** — completes the craft triad: this skill *designs* the context budget (the system-prompt layer included); prompt-as-product *governs changes to it* over time. A change to the token budget or the system prompt is a versioned release with the same blast radius as any prompt change — run it through that skill's regression + A/B process, don't hand-edit the architecture in production.
- **`rtp-determinism-compass`** *(import)* — which layers must be deterministic/reproducible vs. tolerate variance.
- **`rtp-stress-test`** *(import)* — the latency and cost of the layer stack at production scale (700ms of stacked layers before generation even starts).
- **`rtp-agent-spec` / `rtp-agent-harness`** — the multi-agent isolation here is the context half of harness design; those own orchestration and handoff contracts.
- **Demand-side application (watch-tier):** the same muscle — *structure the context an AI ingests so it decides your way* — applies when the AI is your *buyer*, not your product (influencing an AI buyer is context engineering, not marketing: model decision-rules like position bias and a pull toward citable sources, not human biases). That's a distinct objective flagged as the **`marketing-to-ai-agents`** new-skill candidate; noted here, not folded deep. *(HBR q2-23, Hosanagar, 11 Jun 2026 — conceptual; primary skill target is prompt-as-product/context-spec, marker withheld.)*

## REALITY CHECK

- **Latency tax compounds** — retrieval (500ms) + tool (2s) + generation (3s) = 5.5s; on a 6s SLA you're underwater before the user sees output. Budget latency top-down.
- **Context quality ≠ capacity** — 128K looks great until the Pre-Rot Threshold at ~60K; design for the working budget.
- **Observability sampling** — log 100% of failures, 10–20% of successes; don't log everything.
- **External-API fragility** — 5 APIs at 99.9% uptime = 0.5% downtime; spec each fallback before building.

## QUALITY GATE

- [ ] Pre-Rot Threshold identified; token budget allocated per layer within it
- [ ] Layered action space documented (what updates when, failure mode per layer)
- [ ] Compaction strategy per layer, with token savings quantified
- [ ] Tool-selection strategy: which tools shown and why (not "all tools")
- [ ] Every external dependency has a fallback (assume ≥1 fails per week)
- [ ] Multi-agent isolation defined if a harness (planner/generator/evaluator scopes)
- [ ] File-based handoff protocol documented; all diagnostic questions answered

## WHEN WRONG

- Single-turn features with no retrieval, state, or external APIs (use `determinism-compass`).
- Prototypes validating model capability, not production readiness.
- When context-spec becomes delay-theatre instead of unblocking implementation.
- Features 99% deterministic with a thin AI layer (wrong tool).

## TRADE-OFF LEDGER

By engineering a token budget instead of filling the window, you bet that reasoning quality is set by *what* reaches the model within the Pre-Rot Threshold, not by *how much* — that a well-budgeted 70K beats a stuffed 128K. You give up the simplicity of "just put everything in the prompt" and take on the discipline of per-layer budgets, compaction, and fallbacks. **Reversible?** It's architecture — changing it later means re-plumbing the context flow, so it's cheaper to get right up front (that's the point of a spec). **The hidden trade:** the failure mode is *over-spec* — a 60-page context doc for a feature that needed a paragraph; match spec depth to the feature's real complexity. **Confidence: High** — the Pre-Rot degradation is measured, not opinion. What would change it: a single-turn feature with no retrieval or state, where there's no architecture to engineer.

## CONCLUSION

Follow the Conclusion Protocol ([Universal Skill Protocol](../../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5): the recommendation (the layer budget and the Pre-Rot Threshold it fits within), the key trade-off (a well-budgeted small window vs. a stuffed large one), the biggest risk (the layer that rots first, or a dependency with no fallback), and the next action (the context-budget table + the compaction/reset trigger, with an owner). Deliver as a document (diagram + budget table + fallback playbook), a deck, or inline.

## VISUAL SUMMARY

After the primary output, invoke the **excalidraw-svg** skill for one visual: the stacked layers between sources and the model, each with its token budget, drawn against a window bar that marks the Pre-Rot Threshold (~60%) — so a viewer sees at a glance that the usable budget is well short of the max, and which layer is eating it. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
