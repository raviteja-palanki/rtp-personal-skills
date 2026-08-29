---
name: context-spec
version: v1.4_latest
description: 'Context engineering: the information architecture for reasoning, not the prompt. Everyone tunes the prompt and the model; the invisible 90% is how information flows from sources through layers into the window, and the killer fact is that models degrade at 50–60% of max context (the Pre-Rot Threshold), so context capacity ≠ context quality: a 128K window has a ~70K working budget. You engineer a token BUDGET across stacked layers, each with its own token cost, compaction strategy, and failure fallback, plus multi-agent context isolation and dynamic tool selection. Use when architecting an AI feature with retrieval, tools, or conversation state. Do NOT use for single-turn no-retrieval features (use determinism-compass). Pairs with: invisible-stack (it diagnoses the weak layer, this designs the build spec for all seven), prompt-craft (the prompt text vs. the architecture), determinism-compass, stress-test. Triggers: ''context engineering'', ''context architecture'', ''token budget'', ''context window''.'
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

**Scope check: the same bound holds one level up, at the enterprise altitude.** An HBR piece on AI transformation and mindset (Jun 2026) argues that AI transformation follows data transformation: unified, high-quality data across an organization's systems has to exist before a rollout starts, not as a parallel workstream that catches up later. The piece cites OpenAI's GDPval benchmark, which tracks how close agentic models come to matching human experts on a set of professional tasks, reporting roughly 80 percent parity on that task set, up from roughly 50 percent six months earlier. That specific figure could not be confirmed against the primary GDPval source in this pass; carry it as reported, tier ⚠, not verified.

The mechanism is the same one this skill runs on a single request, moved up a level. At the session altitude, context quality bounds output quality: a model reasoning over stale or fragmented retrieval reasons badly no matter how capable it is. At the organization altitude, "context" means the data infrastructure itself: whether the systems an agent will draw from are unified and accessible, or scattered across silos with no shared schema. An agent layered on top of unreconciled data inherits the same rot the CONTEXT BUDGET section describes for a single window, at the scale of the whole rollout.

**The required check.** Before scoping any enterprise-wide AI rollout, run **data-unification-as-precondition**: has the underlying data actually been unified and made accessible across the systems the rollout will touch, or is the rollout being scoped as if that step is already done? A rollout plan with no answer to this question has skipped the same step a context spec skips when it assumes a source layer exists without checking it.

**Condition this is wrong, and the falsifier.** At small scale, with a single well-scoped tool operating over data that is already clean, this check adds unnecessary process for no real benefit. Reserve it for rollouts spanning multiple existing systems or data sources, where the unification work is real and easy to assume away.

*(Source: HBR piece on AI transformation and mindset, Jun 2026 — cites OpenAI's GDPval benchmark; the roughly 80 percent parity, up from roughly 50 percent six months prior, figure is reported by the piece and unverified against the primary GDPval source in this pass. Carry the data-unification argument; tier the benchmark figure ⚠.)*

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

## JUDGMENT ELICITATION — authoring the judgment before the spec can assume it exists

THE PROCESS assumes the context to assemble already exists somewhere: a document, a tool, a conversation log. Often it does not. An HBR piece on codifying decision-making judgment for AI agents (Jun 2026) traces an ITA Group agent failure to undefined judgment, not engineering. The team had specified data and tools, but nobody had written down the risk tolerance and escalation thresholds a person applies without thinking. (◆ company-disclosed case, self-selected and sourced through the authors' own advisory relationships; no independently audited productivity claim accompanies it. Flag that limitation before citing the case.)

**The mechanism.** A new hire absorbs unwritten judgment by watching a colleague handle an edge case and generalizing from it. An agent has no such channel. It acts only on what has been made explicit, so unwritten judgment - risk tolerance, escalation thresholds, exception handling - is the actual failure surface, not the model or the tool integration. AWP Safety and a VC firm's controller each responded by codifying one narrow slice of their own judgment into markdown files their agents now execute (◆ company-disclosed). Ramp goes further and trains every new hire to build their own agents, on the same premise (◆ company-disclosed).

**The extraction method.** Don't interview the expert alone. One-on-one interviews fail because experts are poor at articulating judgment in the abstract when asked cold; the rule only surfaces when a live case triggers it. Convene a panel of practitioners instead and walk them through real edge cases together. Treat disagreement among them, not agreement, as the signal worth capturing - structured disagreement externalizes reasoning that a solo documentation request never surfaces. The resulting transcript is the first draft of codified judgment.

**A new context-artifact type.** Call the product a precedent transcript: an artifact distinct from a retrieved fact, a RAG-retrieved document, or conversational memory, because panel elicitation produces it rather than assembling it from something that already existed. THE PROCESS step 1 ("what's the actual usable context?") has no answer when the judgment-heavy layer has never been authored. Run panel elicitation first; then feed the transcript into THE PROCESS as a source layer like any other.

**Condition this is wrong, and the falsifier.** The method assumes disagreement in the room is legible and resolvable in one session. Real disagreement is often a proxy for turf or incentive conflict a moderator cannot see, and that risks codifying whoever was most persuasive rather than whoever was most correct. Treat this as a real risk of the method, not a caveat to skip past. Give every precedent transcript the same provenance discipline as EXCEPTION INTERROGATION below: trace each rule to the session and the disagreement that produced it, so a bad call can be retired later.

*(Source: HBR piece on codifying decision-making judgment for AI agents, Jun 2026 — ◆ company-disclosed case studies throughout (ITA Group, AWP Safety, a VC-firm controller, Ramp), self-selected success stories sourced through the authors' own advisory relationships. No independently audited productivity claim accompanies any of them; carry the mechanism and the extraction method, not an implied productivity gain.)*

## EXCEPTION INTERROGATION — getting the knowledge that lives only in someone's head

Every context stack has a layer nobody can populate from documents, because the knowledge was never written down. One estimate puts it at **nearly a quarter of middle-office decisions relying on reasoning that no policy document fully captures.** Interviews do not get it out, because the expert cannot recall the rule outside the case that triggers it.

**The acquisition pattern, and it inverts how knowledge capture is normally attempted.** When the system meets a case it cannot resolve, it **captures the surrounding conditions and asks the expert a targeted question about that specific case**, rather than failing silently or routing the whole thing upward. The answer is distilled into a reusable rule and applied to every similar case afterwards. The expert is not observed and not interviewed. They are asked one specific question, by a system that has already worked out it is stuck, at the moment the exception occurs.

**Why it works when interviews do not:** the unit that transfers is a **rule about a class of cases, produced by a question about one case.** Recall is cued by the live instance. Ask the same expert to enumerate their unwritten rules in a workshop and you get the ones they can already articulate, which are the ones already in the policy document.

**The precondition, and it is absolute: the system has to be able to detect its own boundary.** Interrogation only reaches knowledge the system knows it is missing. A system with weak boundary detection does not ask; it resolves the case, confidently and wrongly, and every downstream provenance record then makes that answer permanent. **So specify boundary detection before you specify the interrogation loop, and never ship the second without the first.** Route to `rtp-failure-modes` for what happens when you do.

**Three things to specify when you build this:**

1. **The trigger.** What counts as "cannot resolve"? Confidence threshold, missing field, conflict between sources, novel category. Write it down; it is the boundary.
2. **The question shape.** Targeted and case-specific. A broad question returns the policy document back to you.
3. **Provenance.** *"Every rule should be traceable to the expert exchange that produced it."* Without it you cannot audit a rule, retire it when the expert was wrong, or tell a learned rule from a written one.

**One open question worth holding rather than resolving.** This pattern replaces an expert who *produces* decisions with an expert who *answers questions about* decisions. Whether the expert who answers a hundred such questions a year keeps the judgment that made the early answers good is unmeasured, and it is the exact question `rtp-judgment-guard` exists to ask. There is a real argument on both sides: interrogation concentrates the expert's remaining attention on boundary cases, which is where judgment is worked hardest. Treat the substitution as unresolved rather than as a loss you have priced.

*(Source: HBR, "4 Steps to Transform the 'Middle Office' with AI," Aug 2026 — ⚠ throughout. Four of six authors work for a consultancy and two for a cloud vendor; the evidence base is their own unpublished cross-industry analysis of unnamed clients. **The quarter-of-decisions figure is the load-bearing number for this pattern and it has no stated method, population or sample.** The claim that a single correction generalizes an entire class of exceptions is the authors' own and is not demonstrated. Carry the pattern, which is reusable; do not carry the numbers.)*

## RETRIEVAL ADJUDICATION — when the corpus disagrees with itself

Retrieval-augmented generation is usually pitched as a findability fix: index everything, retrieve the top-k, and answer. A Jul 2026 MIT Sloan review of RAG deployments across 8 consumer-goods companies (no stated sampling frame; read the count as directional, not a sample) found something else happens in practice. RAG does not just retrieve. It adjudicates between everything it retrieves, and it does that silently.

**The mechanism.** Vector similarity is good at synonymy: two documents using different words for the same idea collapse into one relevant match, which is most of why retrieval works at all. It has no equivalent machinery for homonymy, where the same term means something different in two business units, or for outright contradiction, where two documents in the corpus disagree and both are equally retrievable. The retriever surfaces both with the same fluency it would use for two documents that agree. The model then answers in one confident paragraph, and that confident tone strips the uncertainty signal a person used to get for free: a shelf of visibly conflicting paper binders looks conflicted, a single fluent answer does not.

**The rule this sets for the spec.** Any content-understanding layer built over a multi-unit or multi-source corpus needs an explicit design step for conflict detection before retriever tuning starts, not after launch when the first wrong-but-confident answer surfaces. Specify how the system flags scope mismatches and contradictions at retrieval time, before it commits to an answer.

**A concrete instrument.** Novartis built exactly this as a feature called WatchOut: it flags results that are narrower in scope than the reader is likely to assume, at the point of retrieval, before the tool generates a response (◆ company-disclosed savings of $29M per year; no denominator was given, so treat the dollar figure as unauditable and cite the mechanism instead).

**Condition this is wrong.** A single-source corpus, or a corpus from one business unit where terms are already disambiguated, has no adjudication problem to design for. Apply the ordinary retrieval-quality work in CONTEXT BUDGET and stop there; building a conflict-detection layer for a corpus that cannot conflict with itself is over-spec.

**Falsifier.** Watch the rate of decisions later reversed because of internal data conflicts, in an enterprise RAG deployment over multi-unit content. If that rate holds flat or falls after rollout with no reconciliation work done, the model is adjudicating adequately on its own and this pattern does not hold.

**A worked example one layer down.** Warner Bros. Discovery piloted a tool to help marketing teams find and reuse video assets. The pilot mostly failed at its stated goal. What it found instead, as a byproduct, was that the real blocker sat one layer below what the pilot was built to test: the library had only asset-level tags, no scene- or shot-level metadata, so nothing the tool retrieved was specific enough to reuse. The deployable content-understanding layer was not the retrieval tool; it was the metadata layer underneath it. When a pilot fails at its stated goal, check whether the missing spec is a layer down before concluding the approach was wrong. This does not apply when the failure traces to execution against well-specified data (adoption, UX, model quality) rather than to a missing structural layer; only a failure analysis that actually locates the missing layer earns this diagnosis.

*(Source: MIT Sloan Management Review, Jul 2026, on RAG and customer-insight synthesis across 8 consumer-goods companies (⚠, no stated sampling frame) and a separate Jul 2026 MIT Sloan Management Review case on Warner Bros. Discovery's marketing-asset pilot. The Novartis WatchOut figure is ◆ company-disclosed with no denominator; carry the mechanism, not the dollar amount, as evidence.)*

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
