---
name: invisible-stack
description: >
  Every AI feature has a visible part — the model writing the answer — and a stack of
  hidden parts that decide whether that answer is any good: which documents got retrieved,
  what the safety layer allowed through, what the system remembered, which tools it called.
  This skill maps those hidden layers, measures each one, and finds the single weakest layer
  that is capping quality — because a perfect model fed bad context still ships a bad product.
  Use when: reviewing an AI architecture, diagnosing why a demo works but production doesn't,
  or writing a feature spec. Do NOT use for simple single-turn features with no retrieval,
  memory, or tools. Pairs with: context-spec (this skill finds the weak layer; context-spec
  writes the build spec for all seven — one diagnoses, one designs), eval-framework (every eval
  failure traces to one broken layer here; run them together to route a failure to its owner),
  production-observability (you can't fix a layer you can't see — it instruments each one),
  failure-modes (each layer's break maps to a named failure: bad retrieval → hallucination,
  missing guardrail → unsafe output).
imports: [determinism-compass, stress-test]
version: "2.0"
---

# Invisible Stack: The Production-Quality Diagnostic

**The objective:** find the one hidden layer that is capping your AI feature's quality, before you waste weeks tuning the wrong thing. The model is the part everyone watches; it is also rarely the part that's broken. This skill makes the invisible infrastructure — retrieval, context assembly, guardrails, memory, tools, monitoring — visible enough to measure, so a PM can point at the specific layer setting the ceiling and fix that, instead of swapping models and hoping.

## KEY TERMS (plain language)

- **The invisible stack** — every processing step between a user's request and the answer they see. The chat box is visible; retrieval, safety checks, memory, and tool calls are not.
- **CONTEXT (the seven layers)** — the checklist for mapping the stack: **C**onstitution (rules and instructions), **O**bservations (live user/session data), k**N**owledge (retrieved documents), **T**racks (memory and conversation history), **E**quipment (tools and APIs), e**X**ecution (orchestration, retries, timeouts), **T**emplate (output formatting). Its whole job is to leave no layer unnamed.
- **Retrieval / RAG** — the step that searches your documents and hands the most relevant ones to the model as context. RAG = retrieval-augmented generation.
- **Weakest-layer ceiling** — the rule that a system's quality is capped by its worst layer, because a later layer can't rebuild information an earlier one destroyed (the model can't cite a document retrieval never found).
- **Precision@5** — of the top 5 documents retrieval returns, how many are actually relevant. A plain quality score for search.
- **P95 latency** — the response time 95% of requests beat; the "slow but not rare" case, more honest than an average.
- **Embedding model** — the model that turns text into numbers so similar meanings sit near each other; its quality decides what retrieval is even able to find.
- **Chunking** — how you cut documents into searchable pieces. Small chunks surface exact facts; large chunks preserve context. Different choices make a different product.
- **Re-ranker** — a second-pass filter that reorders the first ~20 retrieved candidates down to the best few, trading a little latency for better relevance.
- **Vector database** — the store that holds embeddings and answers "what's most similar to this query?" (Pinecone, Weaviate, Qdrant).
- **Ablation test** — remove one layer, measure how much quality drops; that drop is the layer's real contribution.
- **Drift detection** — monitoring that notices when production inputs or outputs quietly shift away from what the system was built for.
- **Guardrail** — a check that blocks or rewrites unsafe or off-policy output before the user sees it.
- **Spotlight effect** — the cognitive bias of over-weighting the one visible thing (the model) and under-weighting everything you can't see.
- **Evidence tiers used below** — ✅ audited/peer-reviewed · ◆ company- or study-disclosed · ⚠ reported or practitioner estimate. Numbers marked *illustrative* are teaching devices, not measured facts — don't quote them as data.

## DEPTH DECISION

**Go deep if:** architecting an AI feature with retrieval, tools, or conversation state; reviewing production failures; or diagnosing why a demo works but production fails.

**Skim to Weakest Layer if:** you have a system already built and just need to identify which layer is causing problems.

**Skip if:** simple single-turn prompt-response features with no retrieval or context dependencies.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

You will focus on the model. The bias is the **spotlight effect**: attention flows to the visible, impressive part — the model generating fluent responses — while the infrastructure that decides whether those responses are any good stays in the dark. Users see the chat interface. They don't see retrieval, context assembly, guardrails, caching, routing, or monitoring. Those invisible layers are where production quality lives or dies.

A useful rough framing is the **10/90 split**: in a production AI system the model is a small share of what determines quality — call it 10% — and the other 90% is retrieval, context engineering, safety, caching, and monitoring (⚠ illustrative proportion, not a measured constant; the ordering is the point, not the exact number). **Why it holds:** the model is the one component you didn't build and can't easily change, so it draws attention it doesn't deserve, while the layers you *can* control go unexamined. **When it over-warns:** for a thin single-turn feature with no retrieval or memory, there is almost no invisible stack and the model really is most of the system — don't manufacture layers that aren't there.

## Retrieval Quality Is a PM Decision, Not Just Engineering

Retrieval is the quiet failure point. A perfect model receiving bad context produces confident hallucinations, and no prompt tweak fixes it. That makes retrieval quality a product responsibility, not something to hand off with "the engineers will handle it."

**Where output quality comes from (illustrative weighting ⚠ — a mental model for where to spend attention, not measured constants):**

```
Retrieval accuracy   — did we find the right documents at all?
Information density   — do those documents actually contain the answer?
Information order      — is the best document first, or buried at position 5?
Clear structure        — are the documents formatted so facts are easy to extract?
Instruction clarity    — does the prompt tell the model how to use them?
```

The list is ordered by leverage, top to bottom. The **defensible claim is ordinal, not cardinal**: retrieval accuracy dominates; structure and prompt-phrasing are real but lower-leverage. Don't cite exact percentages — the ranking is the insight.

**What this means for you (the PM):**
- If retrieval only finds the right document 60% of the time, 60% is roughly your quality ceiling — the model cannot answer from a document it never received. **Spend your first hour on retrieval accuracy.** Polishing document formatting is a smaller gain, further down the list.
- **Embedding choice is a PM decision.** Different embedding models retrieve better for different domains (dense technical docs vs. short customer queries). Test retrieval quality on real queries before committing — this is not a "just implement it" detail, because it sets the ceiling above.
- **Chunking is a PM decision.** 256-token chunks and 2K-token chunks are different products: small chunks surface precise facts, large chunks preserve context. Test with real queries before the engineering locks in.

**Why these are PM decisions and not pure engineering:** each one silently sets the product's quality ceiling, and the trade-offs (precision vs. context, cost vs. accuracy) are product trade-offs wearing technical clothing. Hand them off unexamined and you've outsourced your ceiling.

## THE PROCESS

**1. Map the full stack.** For any AI feature, name every layer between "user input" and "user output." The CONTEXT framework is the checklist that keeps you from missing one:
   - **C**onstitution — system instructions, behavioral constraints, safety rules
   - **O**bservations — real-time data, user context, session state
   - k**N**owledge — retrieved documents, knowledge bases, structured data
   - **T**racks — workflow state, multi-step routing, conversation history
   - **E**quipment — tools, APIs, MCP connectors, function calls
   - e**X**ecution — orchestration logic, retry handling, timeout management
   - **T**emplate — output formatting, response structure, prompt templates

   **Why a checklist and not free recall:** the layers you forget are exactly the ones with no owner and no monitoring — which is why they're the ones that break in production. If you can't list all seven for your feature, the missing ones are your first finding.

**2. Assess each layer.** For each: Does it exist? Who owns it? How is it monitored? What happens when it fails? A layer with no owner and no monitor is a production incident waiting for a date.

**3. Identify the weakest layer.** A system's production quality equals the quality of its weakest layer. **Why:** the layers run in sequence, and a later one cannot rebuild information an earlier one lost — perfect generation on top of 50%-accurate retrieval is still 50% right. **When this frame misleads:** the fault isn't always one weak layer. Sometimes two adequate layers interact badly — a decent retriever and a decent formatter that disagree on structure — and the problem is the handoff, not either layer alone. If fixing the "weakest" layer doesn't move quality, look at the seams between layers, not the layers.

**4. Design the invisible layers before the visible ones.** Reverse the natural order: start from the context architecture and work forward to the UI, not the other way. **Why:** the visible interface inherits whatever ceiling the invisible layers set, so a UI designed first has to be redesigned once you discover the real constraint. **When wrong:** for a genuinely thin feature, this reverses into over-engineering — design the UI and ship.

## REALITY CHECK

- Building the full seven-layer stack for every feature is over-engineering. Match stack depth to how much the feature can hurt someone if it's wrong.
- Every layer adds latency. A seven-layer stack at 100ms per layer spends 700ms before the model even starts generating (illustrative arithmetic ⚠) — latency budget is a real constraint, handled below.
- Invisible layers need their own monitoring. You cannot debug what you cannot see, which is why instrumentation (see `rtp-production-observability`) is part of building a layer, not an afterthought.

## MEASURING EACH LAYER

Analysis without measurement is a guess. For every layer in the stack, run this three-question protocol:

**Coverage — what share of queries does this layer touch?**
- Example (retrieval): what % of queries can be answered from our knowledge base vs. falling back to the bare model?
- **Why it matters:** a layer that fires on 20% of traffic contributes less than it feels like it does; a layer on 80% is critical path and deserves the attention.

**Accuracy — when it fires, how often is it right?**
- Example: when retrieval returns a document, does the final answer use it correctly?
- **Why it matters:** high coverage with low accuracy is worse than the reverse — you're wrong more often *and* it's spread across more traffic, so it's harder to trace.

**Latency — how much time does it add?**
- Example: a safety filter adds 200ms P95; retrieval adds 800ms P95; together that's a full second before generation even starts.
- **Why it matters:** users tolerate roughly 3–4 seconds for a complex AI task (⚠ practitioner rule of thumb; varies by task and expectation). If the stack eats 2 seconds before the model runs, 1–2 seconds is all that's left for generation.

**Per-layer measurement reference.** The thresholds below are **recommended starting points (⚠ practitioner defaults, not laws)** — tune them to your domain and re-baseline. **Why defaults and not fixed rules:** a safety-critical medical feature and an internal drafting tool have different tolerances for the same false-negative rate; a number that's reckless in one is wasteful in the other.

| Layer | Coverage metric | Accuracy metric | Latency metric | Suggested starting threshold (⚠ tune) | How to collect |
|---|---|---|---|---|---|
| Constitution (rules, system prompt) | % of known edge cases with an explicit rule | Rule-violation rate (outputs that break a constraint) | N/A (static) | Coverage >90% of known edge cases; violations <0.5% of outputs | Log violations; run an adversarial prompt suite monthly |
| Retrieval (RAG, search) | % of queries returning ≥1 relevant document | Precision@5 | P95 retrieval latency | Precision@5 >70%; latency <500ms; empty retrieval <5% | Instrument the pipeline; hand-score ~100 sampled queries/week |
| Validation (guardrails, filters) | % of output categories with an active guardrail | False-positive rate (good output blocked) + false-negative rate (bad output passed) | Guardrail latency added | FP <2%; FN <1% where safety-critical; +<200ms | Log every trigger with input/output; review blocks and passes weekly |
| Orchestration (routing, tools) | % of tool calls with error handling | Tool-call success rate; fallback rate | End-to-end orchestration P95 | Success >95%; fallback <10%; routing <2s | Instrument each call; track retries, fallbacks, timeouts |
| Monitoring (observability, drift) | % of production features with a live monitor | Drift caught before users report it | Time from drift to alert | >80% caught before user report; alert <1 hour | Deploy drift detection; compare system-detected vs. user-reported |

*(This one table replaces the two overlapping ones the skill used to carry — a simple template and a detailed protocol that measured the same thing at two granularities.)*

## AUDIT CASE STUDY

**Illustrative scenario — a composite that shows the pattern, not a specific audited company; the numbers are illustrative ⚠:**

A B2B document-analysis product sits at 65% user satisfaction after six months. The team has spent those months on the generation model — new prompts, one frontier model vs. another — with no real movement.

The audit runs the measurement protocol and finds:
- Knowledge layer (retrieval): ~50% precision. Half the documents it surfaced were irrelevant to the query.
- Generation model: strong. Given correct context, it produced excellent answers.
- Safety layer and post-processor: working.

The finding: the model was never the problem. Retrieval was polluting the context with irrelevant chunks, and the model was hallucinating to reconcile them. The fix was upstream — re-chunking plus a better embedding model — lifting retrieval precision from ~50% to ~81% and satisfaction from ~65% to ~82%, with no change to the generation model.

**The lesson (this is the durable part, not the numbers):** never optimize the generation layer until you've audited the layers upstream of it. The weakest layer sets the ceiling for the whole system — so the highest-leverage fix is almost never where the attention naturally goes.

### How to Run an Invisible Stack Audit

**When:** before launch (mandatory), quarterly (recommended), and after any model upgrade or architecture change (mandatory — a model swap silently reshuffles which layer is weakest).

1. **Map the stack.** List every layer between input and output: system prompt, retrieval, pre-processing, model call, post-processing, guardrails, caching, logging. If you can't list them all, you have an invisible-stack problem by definition.
2. **Instrument each layer.** Verify each has latency, error rate, and at least one quality metric. Any layer with zero instrumentation is your first finding.
3. **Measure baseline.** Run a representative query set (a few hundred queries is a reasonable starting scale ⚠) through the full stack and record per-layer metrics. This is your before.
4. **Stress test.** Run a set of adversarial and edge-case queries. For each: does retrieval return garbage? Does the guardrail catch it? Does monitoring alert?
5. **Compute layer contribution (ablation).** Remove a layer, measure the accuracy drop; that drop is the layer's real contribution. A layer contributing near-zero is a candidate for removal to cut latency and cost. **Why ablation and not opinion:** it replaces "this layer feels important" with a measured number.
6. **Document findings.** Per layer: current metric, threshold, gap, recommended fix, owner, timeline. Re-run the same query set after fixes — the audit isn't done until the re-run confirms the improvement.

---

## Vector DB Selection Is a PM Decision

Vector database choice affects unit economics, latency, and competitive positioning — so it's a product decision, not an engineering-only one.

**Trade-offs to own:**
- **Hosted (Pinecone, Weaviate Cloud):** lower operational burden, predictable at small scale; vendor lock-in and higher per-query price at scale.
- **Self-hosted (Weaviate, Qdrant, Milvus):** higher operational burden, lower cost at scale, an escape hatch if a vendor changes pricing; needs infra expertise.
- **Hybrid:** start hosted, migrate self-hosted when volume justifies it.

**Decision points (the numbers below are order-of-magnitude practitioner ranges ⚠, and pricing moves — [VERIFY] against current vendor pricing before committing):**
- Acceptable latency per query? (hosted ~50–150ms, self-hosted ~100–200ms)
- Long-term query-volume forecast? (hosted economics get painful somewhere north of ~1M queries/month)
- Is vendor lock-in acceptable? If retrieval quality is your moat, lean self-hosted for control.
- Cost-per-query budget? (roughly $0.001–0.01/query hosted vs. $0.0001–0.001 self-hosted at scale)

**Why own this as a PM:** the "simplest" choice (hosted) can be the most expensive long-term, and the person who owns the unit economics has to see that before the migration cost is locked in. Map the economics across options first — `rtp-cost-model` and `rtp-token-economics` do that heavy lifting.

## Re-ranking Strategies

First-pass retrieval returns ~20 candidates; a re-ranker filters to the best few, trading latency for relevance.

- **Quality:** retrieval-only tends to land the right answer somewhere in the candidate list; adding re-ranking pushes the *best* answer to the top far more often — a meaningful relevance gain (⚠ illustrative; magnitude depends on your retriever and domain).
- **Latency:** a re-ranker adds ~100–200ms per query (⚠ practitioner range). Fine for a chat or research feature where users wait; too slow for autocomplete, which needs sub-50ms.
- **The trade-off:** high-latency features (research assistant, summarization) should almost always re-rank; low-latency features (autocomplete) should skip it or use a lightweight re-ranker; medium ones (chat) should A/B test to find the tolerable line. **Why not always re-rank:** relevance and latency pull in opposite directions, and the right point on that line is set by the feature's latency budget, not by a universal rule.

## How the Invisible Stack Shows Up in Evals

When an eval fails, trace it to the layer that caused it instead of blaming the model. This is the same object `rtp-eval-framework` works on from the other end — error analysis groups failures; this skill names the layer each group belongs to — and each failure below has a matching entry in `rtp-failure-modes`:

- **Poor retrieval → hallucination.** "The AI said X, but the docs never mentioned X." Owner: retrieval, embedding, chunking. Fix retrieval before touching the prompt.
- **Poor guardrails → safety failure.** "The AI said something unsafe or off-brand." Owner: Constitution layer, output validation. Add the missing guardrail.
- **Poor caching → cost blowup.** "We're burning tokens on cheap repeated queries." Owner: eXecution layer, cache strategy. Cache or reshape the query pattern.
- **Poor context assembly → self-contradiction.** "The AI contradicted itself between turns." Owner: Tracks layer, session state. Version the state or clear session boundaries.

**Every eval failure has a root layer.** Naming it is what turns "the model is bad" into an assignable fix with an owner.

## OUTPUT FORMAT

Use this template when auditing a feature:

```
## Invisible Stack Audit: [Feature Name]

| Layer | Exists? | Owner | Monitoring | Failure Mode | Improvement Priority |
|-------|---------|-------|-----------|--------------|-------------------|
| Constitution | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Observations | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Knowledge | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Tracks | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Equipment | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Execution | Yes/No | [name] | [metric] | [what breaks] | [1-5] |
| Template | Yes/No | [name] | [metric] | [what breaks] | [1-5] |

Weakest layer: [identified with a measured number]
Retrieval quality score: [measured %, with method]
Latency budget: [total ms, per-layer breakdown]
```

## QUALITY GATE

- [ ] Full stack mapped — every layer between input and output named (missing layers are findings, not omissions)
- [ ] Each layer has an owner and a monitoring mechanism
- [ ] Weakest layer identified with a measured number, not a hunch — and the seams between layers checked if fixing the weakest one doesn't move quality
- [ ] Latency budget allocated across layers
- [ ] Vector DB choice justified with unit economics
- [ ] Re-ranking decision (yes/no) made against the feature's latency budget

## GENERATE THE DELIVERABLE

Follow the Deliverable Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11. Deliverables take one of three formats:
1. **Document:** an Invisible Stack Audit report with full layer mapping, per-layer baseline, findings, and an improvement roadmap with owners and timelines.
2. **Presentation:** a deck summarizing the stack, the weakest layer, and the executive recommendation.
3. **Spreadsheet:** a layer inventory with coverage/accuracy/latency and improvement priorities.

Always include a stack diagram (the OUTPUT FORMAT template, or a visual via `rtp-excalidraw-svg`), the per-layer baseline with thresholds, and the gap-to-fix roadmap with owners.

## WHEN WRONG

- Simple prompt-and-response features with no retrieval or context — there's no invisible stack to audit.
- Prototypes where the open question is still "can the model even do this?" — validate capability first.
- When stack complexity has itself become the bottleneck, and the right move is to remove layers, not map more of them.

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

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. This diagram captures the essence of the analysis in one glanceable image — making the deliverable far more useful at a glance. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
