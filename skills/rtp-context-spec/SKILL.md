---
name: rtp-context-spec
description: "Context engineering: information architecture for reasoning (not prompts). Constitution → Observations → Knowledge → Tracks → Equipment → Execution. Failure modes, latency, Pre-Rot Threshold. Use when: architecting features, design review. Triggers: 'context engineering', 'context architecture'"
imports:
  - invisible-stack
  - determinism-compass
  - stress-test
---

# Context-Spec: Engineering Information Architecture

## DEPTH DECISION

**Go deep if:** Architecting an AI feature with retrieval, tools, or conversation state. You need to design the invisible stack before building.

**Skim to Quality Gate if:** Reviewing an existing context architecture or diagnosing production failures (you need the checklist, not the full methodology).

**Skip if:** Single-turn, no-retrieval feature or purely deterministic flow (use invisible-stack overview instead).

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## THE TRAP

You focus on the prompt and model. The real problem: the invisible 90% — how information flows from sources through layers to the model. You assume context capacity = context quality. **Wrong.** Models degrade measurably at 50-60% of max context window. At 128K tokens, performance drops around 50-60K tokens (proven in Claude evals). Add latency overhead, retrieval noise, and conversation bloat, and you're operating in the degradation zone before you hit 100%.

The trap has variants:
- **Over-spec:** 60-page docs that delay shipping.
- **Under-spec:** Layers missing entirely. Engineers guess. Production fails.
- **Context bloat:** "Retrieve 20 docs! Show the last 50 messages! Include full metrics!" → hits Pre-Rot Threshold by message 3.

## THE PROCESS

### Import invisible-stack first
Map all seven layers. Context-spec operationalizes that map into specific, implementable decisions for each layer **with latency and token costs**.

### KEY PRACTITIONER QUESTIONS (Answer these first)

1. **What's the actual max context you can use?** If your model's context window is 128K, your real working budget is 60-70K tokens (Pre-Rot Threshold). Allocate: system prompt (5K) + retrieved docs (15K) + observation history (10K) + scratchpad (5K) + conversation (20K) + tool results (5K). What's your token per layer?

2. **Which tools are actually relevant to this feature?** Don't present 50 tools. Pre-filter to 3-5 tools specific to this task. Does context engineering determine tool availability, or does the model waste context seeing irrelevant tools?

3. **Where does context rot happen?** Trace one request end-to-end. At what layer does context quality degrade? Retrieved docs getting stale? Conversation history ballooning? Fix that layer first.

4. **Can you compact any layer?** Can observation history be summarized? Can retrieved docs be compressed? Can tool results be stripped to essentials? Every token saved = room for better decisions.

5. **What's the fallback when any layer fails?** Retrieval timeout? Tool error? Constitution conflict? Specify the exact UX and what information is dropped.

### Layered Action Space Architecture

Systems don't have "one context." They have stacked layers with different update frequencies, reliability, and token cost:

```
System Prompt (immutable, 5K tokens)
  ↓
Retrieved Documents (refreshed per-request, 15K tokens, ~500ms latency)
  ↓
Tool Results (one-time, 5K tokens, ~2s latency, unreliable)
  ↓
Observation History (recent state, 10K tokens, <10ms latency, reliable)
  ↓
Conversation History (user-generated, 20K tokens, live, noisy)
  ↓
Scratchpad/Reasoning (model-generated, 5K tokens, current session only)
```

Each layer has different:
- **Update frequency:** System once/month, retrieval once/request, tool results once/call, history continuously
- **Reliability:** System 100%, retrieval 95%, tools 80-90%, history 100% (if properly stored)
- **Token cost:** Varies; system is sunk, retrieval scales with query, tools are call-dependent
- **Failure mode:** System failure = revert code, retrieval failure = degrade to model-only, tool failure = use fallback

**Production example:** Claude Code context stack layers agent access to: system safety rules (immutable) → recent file edits (retrieved) → user session state (observation) → last 10 messages (conversation) → execution logs (tool results from local observability stack) → working memory (scratchpad). Each layer has independent failure recovery.

#### Anthropic Context Management Findings (March 2026)

**Context resets vs. compaction trade-off:** A reset provides a clean slate, at the cost of the handoff artifact having enough state for the next agent to pick up the work cleanly. Compaction (summarizing context) loses detail and introduces drift. For long-running agents, periodic full resets with structured handoff files are better than attempting to compress context in-window. The reset cost is paid once per session; the compaction cost compounds with every summarization.

**Agent-as-Tool pattern:** When tool results exceed 5K tokens (search results, API responses, log dumps), spawn a sub-agent to extract relevant facts instead of sending raw results to the main agent. This saves 60-70% of tokens while preserving signal. Example: search returns 10K tokens → sub-agent extracts top 3 facts → 2K tokens back to main agent, same outcome.

**File-based agent communication (harness model):** Instead of passing context through conversation history, write state to files (claude-progress.txt, feature-list.json, constraints.md). Each agent session starts by reading files, not by receiving summarized context. Reduces context pollution and makes handoffs explicit. Agents can append to shared files to track progress without bloating the conversation.

### Multi-Agent Context Isolation

In harness architectures (planner → generator → evaluator), each agent must have its own context scope. Context bleeding between agents causes poor decisions:

- **Planner scope:** Brief + product vision + constraints. No code, no tool results. ~15K tokens. Planner outputs: sprint contract (JSON), architecture sketch.
- **Generator scope:** Sprint contract + current codebase state + tool access (file I/O, compile, run). ~40K tokens. Generator outputs: code, test coverage, build logs.
- **Evaluator scope:** Success criteria + live application state + test results. No implementation details. ~20K tokens. Evaluator outputs: pass/fail, blockers, quality metrics.

**Context confusion risk:** If the evaluator sees the entire implementation history, it starts making excuses for the generator's mistakes ("the time pressure was tight, so this is acceptable"). Isolate success criteria from implementation context. If the planner sees raw code, it wastes tokens reading syntax instead of reasoning about architecture.

**File-based handoff:** Planner writes `sprint-contract.json` → Generator reads it, writes `build-log.txt` + `code-snapshot.json` → Evaluator reads only the snapshot and test results, not the generator's reasoning.

### Phase 1-7: Constitution through Template

(Phases follow existing structure: Constitution, Observations, kNowledge, Tracks, Equipment, eXecution, Template)

**Key differences from old spec:**
- Add Pre-Rot Threshold: "At 50-60% of max context, performance degrades measurably. Allocate tokens accordingly."
- For each layer, specify **token cost**, not just latency.
- For Observations, Knowledge, Equipment: specify **compaction strategy** — when to summarize vs. offload to external memory vs. compress in-window.
- For Equipment: specify **dynamic tool selection** — which tools are presented to the model and why (don't show the full 50-tool list).
- For eXecution: specify **layered failure handling** — what information is preserved/dropped when a layer fails.

### Context Compaction Strategies

**When to summarize:** Retrieved docs >5 pages? Compress to extractive summary (preserve citations). Token savings: 60-70%.

**When to offload:** Conversation history >30 messages? Move old messages to external memory (vector DB), retrieve only relevant context. Token savings: 80%+. Latency cost: +200ms retrieval.

**When to compress:** Tool results verbose? Extract key facts, drop examples. Token savings: 50%+.

**Agent-as-Tool patterns:** If tool result is too large, have the agent call a sub-tool to extract relevant facts. Example: "Search results are 10K tokens; agent calls a second tool to summarize top 3 results" → 2K tokens, same information.

### Context Budget Template

Use this template to document token allocation for each feature. Update during architecture review and before implementation:

```
## Context Budget: [Feature Name]
Total model window: [X]K tokens
Pre-Rot Threshold (working budget): [Y]K tokens (typically 50-60% of max)

| Layer | Token Budget | Update Frequency | Failure Fallback | Notes |
|-------|-------------|------------------|-----------------|-------|
| Constitution (system prompt) | [X]K | Monthly | Revert to previous version | Safety rules, core behavior |
| Retrieved documents | [X]K | Per-request | Degrade to model-only | Search results, docs, context |
| Tool results | [X]K | Per-call | Use cached/fallback | API responses, execution logs |
| Observation history | [X]K | Continuous | Summarize oldest entries | Recent state, prior decisions |
| Conversation | [X]K | Live | Compact after N messages | User messages, model responses |
| Scratchpad | [X]K | Session | Clear on reset | Working memory, reasoning |
| **TOTAL** | **[Y]K** | | | Must not exceed Pre-Rot Threshold |

**Compaction trigger:** When total context > [Y]K tokens
**Compaction strategy:** [summarize/offload/reset]
**Reset frequency:** Every [N] messages or [M] hours
**Handoff files required on reset:** [list: sprint-contract.json, build-log.txt, etc.]
```

### Worked Examples

#### Worked Example 1: Single-Turn Customer Support Bot (Simple Case)

The simplest context spec. One user question, one knowledge base search, one response. No agents, no multi-turn, no tool calls.

**Scenario:** SaaS company's help center bot. User asks a question → bot searches knowledge base → bot generates answer.

**Context Stack:**

| Layer | Content | Token Budget | Notes |
|---|---|---|---|
| System prompt | Product name, tone guidelines, response format rules, safety constraints | 800 tokens | Static. Cache this — 90% discount on cached tokens. |
| Retrieved documents | Top 3 knowledge base articles matching user query | 4,000 tokens (max) | 3 articles × ~1,300 tokens each. If fewer than 3 match, budget shrinks. |
| Conversation history | Current question only (single-turn) | 200 tokens | No history needed for single-turn. |
| Scratchpad / reasoning | Internal chain-of-thought for answer synthesis | 500 tokens | Optional. Enable for complex questions, skip for FAQ-style queries. |
| **Total context used** | | **5,500 tokens** | |
| **Model context window** | | **128,000 tokens** | |
| **Pre-Rot Threshold (70%)** | | **89,600 tokens** | |
| **Utilization** | | **6.1%** | Extremely safe. No context pressure. |

**End-to-end trace for one request:**

```
User: "How do I reset my password?"
  ↓
[Retrieval] Search knowledge base → 3 results (0.4s)
  - "Password Reset Guide" (relevance: 0.94) — 1,200 tokens
  - "Account Security FAQ" (relevance: 0.82) — 1,100 tokens
  - "Two-Factor Setup" (relevance: 0.61) — 1,300 tokens
  ↓
[Context Assembly] System prompt (800) + 3 docs (3,600) + question (15) = 4,415 tokens
  ↓
[Generation] Model generates response (0.8s) — 150 output tokens
  ↓
[Guardrail] Check: response doesn't contain internal URLs, PII, or contradictions (0.1s)
  ↓
User sees: "To reset your password, go to Settings → Security → Reset Password..."

Total latency: 1.3s | Total cost: ~$0.003 | Context utilization: 3.4%
```

**Decision points in this simple case:**
1. **Retrieval failure** — If zero documents match (relevance < 0.5), fall back to: "I don't have a specific article on this. Here's our help center: [link]." Don't generate from model knowledge alone.
2. **Low-relevance third result** — The third doc (relevance 0.61) might add noise. For production: set a relevance threshold (e.g., 0.70) and only include docs above it. This saves tokens and improves accuracy.
3. **Latency spike** — If retrieval takes >1s, the response feels slow. Set a retrieval timeout at 800ms; if exceeded, generate from top-1 result only.

#### Worked Example 2: Code Analysis Agent (Complex Case)

```
## Context Budget: Code Analysis Agent
Total window: 128K tokens
Pre-Rot Threshold: 70K tokens

| Layer | Budget | Update Freq | Fallback | Notes |
|-------|--------|-------------|----------|-------|
| Constitution | 8K | Monthly | Revert | Safety + analysis rules |
| Retrieved files | 20K | Per-request | Degrade | Codebase snippets (file read) |
| Tool results | 5K | Per-call | Cached result | Compile errors, test output |
| Observations | 15K | Continuous | Summarize | Recent findings, decisions |
| Conversation | 18K | Live | Compact | User questions, analysis steps |
| Scratchpad | 4K | Session | Clear | Working theories |
| **TOTAL** | **70K** | | | At Pre-Rot Threshold |

Trigger: >70K, then summarize observations and reset conversation.
Handoff: analysis-summary.json, test-results.txt
```

### Dynamic Tool Selection

Don't say "the model has access to 50 tools." Say "for this task, the model sees 3 tools: search, calculator, citation-lookup."

**How to decide:**
- Map each tool to task types (search → open-ended questions, calculator → math, citation → docs).
- Pre-filter tools before the model sees them.
- Log which tools were available; monitor if hidden tools would have helped (post-hoc analysis).

**Production example:** Codex harness hides tools based on language context. Python request? Show Python-specific tools. SQL request? Hide Python tools. Saves context, improves accuracy.

### Diagnostic Questions

Ask these before finalizing context architecture. If you can't answer them clearly, the spec is incomplete:

1. **What's my actual working context budget?** Not the model's max window — the Pre-Rot Threshold. At what token count does performance measurably degrade? (e.g., 128K window → 70-75K true working budget). Allocate all layers within this, not the max.

2. **Which layer is consuming the most tokens? Is that allocation justified?** Run a sample request end-to-end. Measure: system prompt (8K), retrieved docs (25K), tool results (3K), conversation (18K), scratchpad (4K). Is retrieval bloated? Is conversation history unbounded?

3. **What happens when a critical layer fails?** Retrieval timeout → degrade to what? Tool error → cached result or fail-open? Retrieved docs are stale → does the model hallucinate or return "information unavailable"? Specify exact UX and fallback data.

4. **Am I presenting the right tools, or showing the full catalog?** Count visible tools at runtime. If >10, pre-filter. If <3, task may lack leverage. Log tool visibility per session; analyze post-hoc whether hidden tools would have helped.

5. **If I reset context entirely, what state must survive?** Plan a reset strategy: every 20 messages? Every 2 hours? What goes into the handoff file (sprint-contract.json, build-log.txt, etc.)? What's discarded? If you can't answer this, you haven't modeled the agent's memory correctly.

6. **Is latency budget included?** Retrieval (500ms) + tool call (2s) + generation (3s) = 5.5s total. If SLA is 6s, you're at 92% of budget. Add 10% margin for retries. Where does that margin come from?

7. **Which layer is the bottleneck for quality?** Is performance limited by stale docs? Noisy tool results? Too much conversation history? Instrument and measure. Fix the bottleneck first, not the obvious layer.

### Phase 8: Quality Gate

Checklist (same as original, but add):
- [ ] Pre-Rot Threshold identified and token budget allocated per layer
- [ ] Layered Action Space documented (what updates when, failure modes per layer)
- [ ] Compaction strategy for each layer with token savings quantified
- [ ] Tool selection strategy: which tools shown to model, why (not "all tools")
- [ ] External dependencies have fallback plan (assume at least one fails per week)
- [ ] Multi-agent isolation defined (if harness architecture): planner scope, generator scope, evaluator scope
- [ ] File-based handoff protocol documented (json/txt files passed between agents)
- [ ] All diagnostic questions answered (7 questions from section above)

## OUTPUT FORMAT

Context-spec deliverables should include:

1. **Architecture diagram** (text or simple visual):
   - Layers stacked top-to-bottom
   - Token budget per layer
   - Update frequencies
   - Fallback paths

2. **Context Budget Table** (from template above):
   - All 6-7 layers
   - Token allocation (must total ≤ Pre-Rot Threshold)
   - Update frequency and failure fallback for each

3. **Layered Action Space callout:**
   - System prompt (immutable): [what it controls]
   - Retrieved docs (dynamic): [source, refresh rate, degradation plan]
   - Tool results (call-dependent): [which tools, failure handling]
   - Observation history (continuous): [what's tracked, compaction strategy]
   - Conversation (live): [retention policy, summarization trigger]
   - Scratchpad (session): [reset frequency, required handoff state]

4. **Multi-agent handoff spec** (if applicable):
   - Agent 1 inputs: [file/context types]
   - Agent 1 outputs: [files written]
   - Agent 2 inputs: [what agent 1 produced + local scope]
   - Isolation boundaries: [what agent 2 does NOT see]

5. **Compaction strategy:**
   - Trigger: "When total > [Y]K tokens"
   - Action: "Summarize [layer] and reset [layer], keeping [list of files]"
   - Expected token savings: "From [A]K to [B]K"

6. **Fallback playbook** (one row per critical failure):
   - Failure: "Retrieval timeout"
   - Immediate action: "Degrade to model-only with notice"
   - Recovery: "Retry in next session"
   - UX impact: "Response slower, less precise"

## REALITY CHECK

- **Latency tax compounds:** Retrieval (500ms) + tool results (2s) + generation (3s) = 5.5s. If your SLA is 6s, you're underwater before user sees output. Allocate latency budget top-down.
- **Context quality ≠ context capacity:** 128K tokens looks great until you hit Pre-Rot Threshold at 50-60K. Design for your actual working budget.
- **Observability sampling:** Don't log everything. Log 100% of failures, 10-20% of successes. Use sampling, not full logging.
- **External API fragility:** 5 external APIs at 99.9% uptime = 0.5% downtime. Spec the fallback for each BEFORE building.

## WHEN WRONG

- Simple features with no retrieval, state, or external APIs (use determinism-compass instead).
- Prototypes validating model capability, not production readiness.
- Context-spec becomes delay-theatre instead of unblocking implementation.
- Features 99% deterministic with thin AI layer (wrong tool).

---

## GENERATE THE DELIVERABLE

Follow the [Deliverable Protocol from Universal Skill Protocol Section 11](../../UNIVERSAL-SKILL-PROTOCOL.md) to package the context-spec analysis.

Your deliverable should include:
- **Executive summary:** 1-2 sentences on the context architecture choice and why it works for this feature
- **Full context-spec document:** Diagram + budget table + layered action space callout + (if applicable) multi-agent handoff spec + compaction strategy + fallback playbook
- **Implementation checklist:** Quality Gate items (8 boxes to check before engineering starts)
- **(If warranted) Visual summary:** One Excalidraw SVG diagram showing the full layer stack, token allocation, and failure recovery paths

Push back if the feature doesn't warrant this level of spec (single-turn, no retrieval → use determinism-compass instead).

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
