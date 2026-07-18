---
name: agent-harness
version: v1.0_latest
description: "The machine that turns a model's reasoning into work that ships — and how to diagnose it when it breaks. Covers the MHTE frame (Model/Harness/Tools/Environment), the five harness clusters (Identity, Memory Policy, Orchestration, Interception, Observability & Evals) + Governance, Session/Harness/Sandbox, the six failure signatures, the Anatomy Atlas (symptom→cluster→fix), phase-relative perception, the four shippable patterns + feedback flywheel, and the six paradoxes. Use when diagnosing why an agent fails, designing or reviewing a harness, deciding what to change this sprint, or evaluating a vendor's harness. Sibling: harness-operating-model (the economics/org/longevity of the program). Pairs with: agent-ecosystem, tool-architecture, invisible-stack/context-spec, production-observability, eval-framework, safety-by-design. Triggers: 'agent harness', 'why did the agent fail', 'MHTE', 'harness anatomy', 'planner generator evaluator'."
imports: [agent-ecosystem, tool-architecture, eval-framework, production-observability]
---

# Harness Architecture, Diagnosis & Patterns

**The objective:** name the machine around the model precisely enough that, when an agent fails at 2 AM, you can point at the layer and the phase that broke *before* anyone proposes a model swap — and know the small, deterministic change that fixes it. This skill is the *machine*. Its sibling, `harness-operating-model`, is the *program* (what it costs, who owns it, what survives model generations). Build the machine here; fund and staff it there.

## THE ONE IDEA

**The model sets the ceiling of what your agent can do; the harness sets the floor of what it reliably does. Your users live on the floor.** You rent the ceiling from a vendor — it's the same one your competitor rents. You build the floor yourself. That single reframe reorganizes every agent post-mortem, and three consequences fall out of it:

1. **The user is the only fixed point; everything else is a nameable moving part.** When a demo passes and production fails on the same prompt, the request didn't change and the user didn't change. What changed sits *underneath* the agent — the harness, the tools, the environment. Diagnose the moving part, not the model.
2. **"The model failed" is almost always false.** Across 2026's production surveys, most "model failures" are harness failures — lost state, premature stopping, unverified completion, stale context, a missing guardrail. A smarter model in a naive harness is *confident failure at higher speed*. Treat the 90/10 (harness/model) split as a strategic heuristic, not a measured law — but if your eval spend runs model benchmarks while your failures live in the harness, you're shining a flashlight on the one layer that already works.
3. **A change you can't locate on the map is a change you can't make twice.** Every fix must land on a named layer and a named cluster. That's what turns an incident review from theology ("probably the model") into engineering ("Cluster 2 wrote a stale checkpoint at the context-assembly phase").

The proof this is real, not rhetoric: [Harness-Bench (July 2026)](https://arxiv.org/html/2605.27922v1) ran 106 tasks across six harness configs and eight model backends and found the *same model* performs materially differently under different harnesses, same tasks, same budget. The vendor question stops being "which model did you use?" and becomes "which model, under which harness, with which tools, budget, sandbox, memory, evals, and stop policy?"

## KEY TERMS (plain language)

- **Harness** — everything wrapped around the model that turns its reasoning into work that ships: identity, memory, the loop, guardrails, the feedback that catches mistakes. The model is the engine; the harness is the car.
- **MHTE** — Model / Harness / Tools / Environment. Four peer layers, a chain of responsibility: *the model proposes, the harness decides, the tool acts, the environment constrains.*
- **The five clusters** — the working parts inside the harness: Identity, Memory Policy, Orchestration, Interception, Observability & Evals. (Governance is the sixth, elevated in 2026.)
- **Session / Harness / Sandbox** — the three runtime objects you inspect when paged: *Session is memory* (the append-only event log, outside the model), *Harness is decision* (the loop), *Sandbox is blast radius* (the bounded room the agent acts in).
- **Three memories** — history (the full event log), working context (the slice placed in front of the model this turn), durable artifacts (files/checkpoints a future session recovers). An agent has no single "memory."
- **Context durability / context rot** — how reliably an agent performs across many tool calls and resets (durability); the quality decay as the working context fills, *even with relevant material* (rot). Quality falls long before the window is full.
- **Guides (feedforward) vs sensors (feedback)** — guides shape what the model sees *before* it acts (fail silently); sensors check the world *after* it acts and block the next step (fail loudly). Reliability lives in the sensors.
- **Hook vs guardrail** — a hook is any lifecycle checkpoint (observe, log, enrich, route); a guardrail is the subset that enforces a policy (block, rewrite, require approval). Every guardrail is a hook; not every hook is a guardrail.
- **Harness vs runtime** — the harness is what you *design* (prompts, skills, loop, hooks, evals); the runtime is the plumbing that runs it in production (durable execution, checkpoints, multi-tenancy). You build the harness; you usually buy the runtime.

## THE FOUR-LAYER MODEL (MHTE) — Where the Harness Lives

Anthropic's March 2026 [NIST RFI response](https://www.anthropic.com/news/anthropic-nist-rfi-response) set the shared vocabulary: **Agent = Model + Harness + Tools + Environment.** The model reasons, the harness orchestrates, the tools act, the environment contains. The harness is "the natural home for observability and verification."

| Layer | Role | Owns |
|---|---|---|
| **M — Model** | The brain. Reasoning, planning, generation. Stateless, context-window-bound. | Vendor product. |
| **H — Harness** | The control plane. Session continuity, guardrails, evaluation, recovery, the loop. | **You** — the one layer without a default owner. |
| **T — Tools** | The hands. API calls, file edits, queries. Scoped by least privilege. | Platform engineering. |
| **E — Environment** | The room. Filesystem, sandbox, shell, network, credentials, anything that survives a restart. | Security / infrastructure. |

Two disciplines make MHTE pay off:

- **The strict-edge rule.** Every artifact belongs to *exactly one* layer. If you can honestly place something in two, one placement is wrong — and that ambiguity is a bug in your mental model before it's a bug in the code. Blur a tool into the harness and a permission bug shows up as "the harness did something weird"; blur a memory file into the model and a stale file on disk shows up as "the model forgot."
- **Each outer layer is a safety net for the one it wraps.** Model hallucinates → the harness evaluator catches it. Harness misconfigures a call → the tool's permission scope limits it. Tool misbehaves → the environment sandbox contains the blast radius.

**The nested disciplines** (name where the field is, and where you are): Prompt engineering (2023, single-turn) → Context engineering (2024–25, multi-turn, single agent) → **Harness engineering (2025–26, multi-agent, multi-session — you are here)** → Environment engineering (2026+, runtime boundaries). Each contains the previous. Owning only the innermost circle while your failures live in the outer two is the 1990s developer who wrote beautiful functions and had no answer for how the system failed.

## THE FIVE CLUSTERS INSIDE THE HARNESS (+ Governance)

The harness is not one box. It's a control plane with five clusters, each owning a class of decision and each the origin (or catch point) of a class of failure.

1. **Identity** — the operating contract established on boot: who the agent is, its task, which tools it may use, what's forbidden. *Identity declares the contract; Interception enforces it.* A system prompt can *say* "no refunds over ₹5,000"; only a hook makes a ₹50,000 refund architecturally impossible. The shortest cluster to describe, the most underestimated for leverage — every session inherits its answers.
2. **Memory Policy** — what the model sees this turn: context assembly, compaction cadence, boot-time injection (AGENTS.md style), retrieval policy. This is where context rot lives or dies. It is a *database-architecture* problem that happens to live in the harness, not a prompt problem. The sharp design idea: **the session is not the context window** — keep the durable log outside the model, keep window-assembly logic inside the harness, and never let a summarization step be the only copy of anything.
3. **Orchestration** — what happens next after a response, a tool result, a failed check: continue, retry, delegate, escalate, resume tomorrow, or stop. Home of the **Ralph Loop** (intercept the exit signal, check completion *independently* — not by asking the model — reopen with clean context + a progress pointer) and the **Planner/Generator/Evaluator** pattern (one plans, one executes, a *separate* evaluator gates each output — the model grading its own work is the same reasoning running twice). The evaluator need not be another agent: a schema validator, test suite, or policy engine is often the cheapest independent verification. Model routing lives here too — most teams already run multiple models, so routing is the *first* thing Orchestration owns, not a later optimization.
4. **Interception (Hooks)** — the checkpoints between loop steps that ask *should this be allowed?* LangChain's six primitives name the surface: `before_agent`, `before_model`, `wrap_model_call`, `wrap_tool_call`, `after_model`, `after_agent`. **This is where product policy becomes enforceable system behavior.** Compliance lives here, not in a longer system prompt — "you can't prompt your way to HIPAA compliance." The 2026 attack surface makes the placement critical: injection now arrives through five doors (user input, browsed web content, code output, other agents' messages, tool results), and the simplest tool-description injection succeeded ~93% of the time across frontier models — a prompt-layer refusal does not survive that; a runtime hook does.
5. **Observability & Evals** — the part of the harness that watches the harness, and turns yesterday's failure into tomorrow's test. Observability is the raw trace layer; evals are the judgment on top. **This cluster improves all the others** — it's the engine of the feedback flywheel. An observable harness without evals is one you can watch but not improve; an eval suite without observability is a judgment you can't explain.

**Governance (elevated 2026)** — the sixth row the field added after shipping the other five and realizing the on-call rotation was the missing organ: a named owner per cluster, an audit chain that survives the rotation, escalation tied to reversibility class. Treated as a peer, not an afterthought. (The org design of this ownership is the sibling skill's territory.)

### The Anatomy Atlas — Symptom → Missing Cluster → Fix

The one table an incident review starts from. Bring the diagnosis to a *layer*, not a prompt.

| Cluster | What you hear in the war-room | Root gap | The engineered fix |
|---|---|---|---|
| **Identity + Memory** | "It forgot what we agreed 15 min ago." "Every session starts from zero." | Silent instruction drop; window overflow on the highest-value tasks. | Dynamic compaction with importance scoring; session persistence across restart; content-addressed boot files. |
| **Tools** | "It made up a customer ID." "Wrong API, wrong shape." | No schema validation at the boundary; over-broad tool surface. | Permissioned registry; JSON-schema validation on args/returns; reversibility class (read/write/irreversible). |
| **Orchestration** | "Declared done while step 3 failed." "Looped 40 times, burned $80." | No explicit stop rule; success declared by the agent that did the work. | Structured loop with rubric-gated completion; hard step/cost budgets; handoff contracts. |
| **Interception** | "Confident garbage shipped." "Refund fired before approval." | Safety in the prompt, not the runtime; no sensor after the model spoke. | Guides feed forward (context, allowlists); sensors feed back (schema check, test runner, LLM-judge, human-in-loop). |
| **Observability** | "Can't tell which turn regressed." "Trace log has three fields." | Undebuggable runs; regressions caught in prod, not on the PR. | Structured trace per decision + tool call + retry; per-tenant cost meters; yesterday's incident → today's regression eval. |
| **Governance** | "Who owns this at 2 AM?" "Compliance found it after the customer did." | No first-class authority layer; ownership diffuses to whoever answered the page. | Named owner per cluster; audit chain that survives the rotation; escalation tied to reversibility. |

*(The field's survey taxonomy calls the same map **ETCLOVG** — Execution env, Tool interface, Context, Lifecycle/orchestration, Observability, Verification, Governance. Same map, different labels; use whichever vocabulary the room already speaks.)*

## SESSION / HARNESS / SANDBOX — The Runtime Objects You Inspect

MHTE tells you *which layer owns the failure*; Session/Harness/Sandbox tells you *which concrete object to inspect*. **Session is memory** (the append-only log, outside the model, outliving every call). **Harness is decision** (the loop). **Sandbox is blast radius** (the scoped room). The five clusters live inside Harness; they are *how* it decides.

The seven-step production loop every real agent runs (print it above the monitor): load objective/policy/memory/workspace → route to a model → call the model with bounded context → gate every tool request (permission, identity, risk, budget) → execute the tool/sandbox action → record the event in the durable log → decide (continue / retry / branch / escalate / stop). Earlier agents ran three steps (think, act, observe); the extra four — ask permission, record, verify, decide — are where reliability lives.

## DIAGNOSE BY PHASE, NOT BY GUT

### The six failure signatures

Each is an *observable symptom* first, then the diagnostic question it forces:

1. **Premature stop** — declares done before the work is done. *Session-continuity failure.* → *What evidence allowed the system to declare completion?*
2. **Infinite loop** — retries the same (or subtly varied) failed action until budget runs out. *Retry-architecture failure; no circuit breaker.* → *What changes between retries, and what ends the loop?*
3. **Silent drift** — does the wrong work correctly (last quarter's rules, a stale spec). *Context-refresh failure.* → *Which source of truth defined the current objective?*
4. **Shared-vocabulary failure** — answers correctly against its prompt, incorrectly against what the org means ("active users" differs in product vs marketing). *A boundary failure between the agent and the org's language.* The fix is a glossary, and the harness is where it lives. → *Whose definition did the agent use?*
5. **Unauthorized action** — reaches a plausible decision, then does something it shouldn't (sends instead of drafts, refunds beyond threshold). *Permission-design failure — instructions where enforcement was needed.* → *Which control permitted the action?*
6. **Sub-agent divergence** (new, 2026) — an orchestrator fans out to a fleet of parallel workers (Claude Code caps ~1,000); each worker is fine, but their copies of the situation quietly stop matching, and the merge drops correct work or hits an unresolvable conflict. *Coordination failure.* → *Which shared state and merge rule coordinated the parallel work?*

**The debug order (start from evidence, not the model):** outcome (expected vs actual) → session (what state/evidence existed) → harness (which policy selected the next action or allowed the stop) → tool (did it execute and return the expected shape) → environment (was execution constrained/interrupted) → model (given the exact context, was the reasoning itself wrong). Skipping steps means days on the wrong layer; a boring checklist beats a smart guess.

### Phase-relative perception — one file, four lenses

The idea that makes attribution honest: artifacts are *segregated by responsibility* (each belongs to one layer) but *perceived through all four* depending on the run's phase. An `AGENTS.md`: at **boot** the Harness reads it (it's Environment); at **context assembly** its contents become prompt text (Memory Policy decides how much); at **inference** the Model sees only tokens; at the **tool phase** an `fs-read` treats it as bytes. Same file, four perceptions — which is why "the model hallucinated" often traces to the Memory Policy cluster (wrong content injected), the Environment (stale file), or Tools (schema mismatch). On every post-mortem, name the **phase** first (*in what phase did this become visible? in what phase did it become inevitable?* — often different phases, different owners), then the layer.

## THE FOUR SHIPPABLE PATTERNS (+ the flywheel that makes them compound)

Small, deterministic changes that beat model upgrades — each implementable in a sprint, each pinned to a cluster. Guides feed forward; sensors feed back.

1. **Structured retry > naive retry** (Interception + Orchestration). Naive retry resends the identical prompt and hopes — a coin flip, because the model's prior for that input hasn't moved. Structured retry parses the error, extracts the violation, and feeds it back as *new* information ("`amount` was a string '$42.50'; return an integer in cents"). Teams that ship it see drift drop ~60% on the same model. *The specificity of your error signal IS the specificity of your feedback loop* — a generic "error 500" is back to the coin flip.
2. **Strict structured output** (Interception). Not a formatting convenience — a reliability pattern. Strict-mode schema enforcement shrinks the set of things the model is *allowed* to say; invalid paths are pruned at generation, not caught at parse. Three specifics separate a reliability schema from a formatting one: `additionalProperties: false`, regex-bounded strings (a bare `date: string` is a hand grenade; a pattern is a contract), and enums everywhere the value set is finite. Complementary with structured retry: strict mode kills *format* failures at the token level; structured retry handles *semantic* ones (valid integer, but negative). Version the schema like a public API.
3. **The narrow gate** (Memory Policy / Tools). Every tool is a decision the model makes every turn; you are not restricting the agent, you are freeing it from choices it was getting wrong. Vercel cut ~80% of tools and got fewer steps, fewer tokens, faster responses. Shopify's heuristic: past 20–50 tools the boundaries blur. Reveal tools *as needed* (skills = progressive disclosure), name each for its exact verb, and add *negative examples* ("do NOT use this when…") — a tool that says what it's *not* for is a decision the model no longer gets wrong. Tool sprawl is an org problem (each team ships its own tool); the cut is a negotiation, so run it as a product decision with the registry as a single owned surface, or the next sprint reverses it.
4. **Emit artifacts, not answers** (Orchestration + Interception). For any output consumed by another system or verified against criteria, prefer an *executable* artifact (a function, query, diff, test) over prose or even JSON. It buys three properties nothing else does: **stateful checkpointing** (progress survives a crash), **formal verification** (the output can be tested, not just read), **deterministic replay** (the exact failure path reconstructs). When the artifact *is* the migration script, the sandbox catches the constraint violation before approval. The artifact is the eval.

**The meta-move — the feedback flywheel** (Observability & Evals). The three patterns land on a dashboard by Friday; they *compound* only when wired into a loop: every failing trace (early exit, retry-exhausted, wrong tool, failed validation) is mined into a concrete eval, tagged by cluster, added to the suite — so the next occurrence is caught on a PR, not in production. Start with the twenty cases that cover real user failures, not a thousand noisy ones. Without the flywheel, findings scatter across Slack; with it, each becomes a permanent regression test. *A small set of well-tagged evals beats thousands of noisy ones.* (Depth: `eval-driven-development`, `production-observability`.)

**Every pattern is a calibration, not a law.** Each harness edit ships with three tags: the model it was built for, the date it was validated, and the trigger that retires it. Anthropic's own context-reset for Sonnet 4.5's "context anxiety" became dead weight one generation later on Opus 4.5. A workaround with no expiry is technical debt. (The strategy of *which* to build vs. let dissolve is the sibling skill.)

## THE SIX PARADOXES (the judgment that governs harness decisions)

Every consequential harness decision is a *tension to hold*, not a choice to resolve. Name the paradox and a design fight becomes a trade-off decision. The program breaks the moment any one is resolved prematurely.

| # | Paradox | The move |
|---|---|---|
| I | **Intelligence vs. Reliability** — a smarter model isn't a steadier one; a stronger prior confabulates more fluently. | Cap the smartest model with the sharpest verifier. Separate *capability* metrics (best day) from *reliability* metrics (worst day); compare models on the *distance* between them. |
| II | **Constraints vs. Autonomy** — an unbounded agent is a liability nobody trusts with real work; bounds *expand* the surface you can ship. | Permission by reversibility class: broad autonomy on read-only verbs, signature on irreversible ones. Ask "what *can't* this do, and who decided?" |
| III | **Scaffolding vs. Permanence** — every component has a timer; some the model will absorb, some are forever yours. | Keep a two-column list; retire scaffolding aggressively, invest in permanence relentlessly. *(Developed in depth in `harness-operating-model` → the dissolving ladder.)* |
| IV | **Specificity vs. Generality** — no general-purpose *differentiating* harness works; the winners are per-workflow. | Ship a narrow harness per high-value workflow; graduate shared primitives only after two workflows prove them. *(Buy the governance layer, build the differentiating one — sibling skill.)* |
| V | **Demo vs. Production** — what impresses in a Loom is unrelated to what survives five weeks; the gap is failure-mode coverage. | Gate launches on the failure-mode inventory, not demo polish. Ask a vendor: what happens on timeout mid-tool-call, on concurrent users, on a downstream 500, on adversarial input? |
| VI | **Segregation vs. Lifecycle** — the four layers are strictly separated *and* inseparable during a run. | Own each cluster with a named engineer; walk the phase-relative diagram on every post-mortem. This is the paradox that makes the other five legible. |

Multi-agent has its own graduation rule: stay narrow until you know the surface; graduate to multi-agent only when *each sub-agent has a narrow job, each has an explicit eval, and the harness can attribute a failure to the correct agent.* Premature multi-agent multiplies failure modes before you understand any one of them. (Coordination depth: `agent-ecosystem`.)

## HARNESS vs RUNTIME (know what you bought)

The harness is what you design; the **runtime** is the plumbing that runs it — durable execution that survives a crash, checkpoints that resume a long job, multi-tenancy, time-travel replay. You build the harness; you usually *buy* the runtime (LangSmith Deployment, AWS Bedrock AgentCore, Google Vertex Agent Engine) — and most enterprises never name what they bought, thinking they bought a harness. A **meta-harness** (Anthropic's Managed Agents) is a third shape: it rents the hard infrastructure (durable sessions, sandboxes, the loop) through stable interfaces while leaving the judgment — your evals, policies, workflows — in your hands. When an agent fails in production, the failure now lives in one of *five* places: Model, Harness, Tools, Environment, or the runtime that holds them. (The build/buy economics and lock-in wedge are the sibling skill's job.)

## WHERE THIS SKILL ENDS — the boundary, and the siblings it routes to

This skill is the **machine**: the anatomy, the diagnosis, the patterns, the design judgment. It deliberately stops at four edges, each owned by another skill — route there rather than duplicating:

- **The economics, org, and longevity of a harness *program* → `harness-operating-model`** (the sibling): cost shape, reliability dividend, the maturity ladder + Monday kit, the four org models, the Harness PM role, permanent-residents vs the dissolving ladder, the moat. *This skill decides what to build; that one decides how to fund, staff, and future-proof it.*
- **The tool contract and the sandbox depth → `tool-architecture`**: schema, permission scope, reversibility class, MCP/A2A, the registry pattern, environment boundaries. (This is where the "Tools-the-Contract" bonus material lives.)
- **Multi-agent orchestration depth → `agent-ecosystem`**; **autonomy levels & confidence thresholds → `agent-spec` / `trust-ladder`**.
- **The Memory Policy / context layer depth → `invisible-stack` / `context-spec`**; **guardrail enforcement & safety architecture → `safety-by-design`**; **the Observability & Evals cluster → `production-observability` + `eval-framework` / `eval-driven-development`**.

The spine: **this skill names and diagnoses the machine and prescribes the sprint-level fix; every cluster's *depth* and the *program* around it live one hop away.** Never let a diagnosis end at "the harness broke" — name the cluster, name the phase, and route to the owner.

## DIAGNOSTIC QUESTIONS

1. When your agent last failed, can you name the *layer* (MHTE) and the *phase* (boot / context-assembly / inference / tool / observability) it broke in — or did the review end at "probably the model"?
2. Draw your harness as five clusters. Which has no named file, service, or owner? (Most teams are strong on Identity + Orchestration, weak on Memory Policy + Evals.)
3. For your highest-volume call: is there a structured retry (not a naive one), strict-mode output, and a narrow tool gate? If not, that's this sprint.
4. Does completion get checked by the *system* (rubric, test, independent evaluator) or by the agent grading its own work?
5. Is every guardrail a *runtime hook*, or does a refusal you actually need live in the system prompt?
6. Does a failing production trace become a tagged regression eval within a sprint — or does it scatter across Slack?
7. Can you swap the model without rewriting the product? (If not, you've coupled to a vendor; a model recall is now a product outage.)
8. What's your context durability rate (% completing after 50+ tool calls without human restart)? Target >85%. No standard benchmark measures it — you have to test it yourself.

## QUALITY GATE

- [ ] Failure attribution is done by layer + phase, using the debug order, not by gut.
- [ ] The harness is mapped to five clusters + Governance, each with a named owner/file/service.
- [ ] Highest-volume call has structured retry + strict output + a narrow, negatively-scoped tool gate.
- [ ] Completion is gated by independent verification (rubric / test / separate evaluator), with a max-iteration + cost budget + escalation path.
- [ ] Guardrails are runtime hooks (or IAM), never prompt-only; PII/injection defended at Interception, not in the prompt.
- [ ] A trace→eval flywheel exists: failing traces become tagged regression evals; the suite is small and high-signal.
- [ ] Every model-specific workaround carries its three tags (model, validated-date, retire-trigger).
- [ ] The design names which paradox(es) it is deliberately trading, and the harness is model-agnostic enough to survive a model swap.

## WHEN WRONG

This skill over-applies when: you're pre-PMF (validate desirability before building a harness); the task is single-turn Q&A or simple retrieval (assertions, not a harness); latency budget can't absorb the loop; or "we need to design the architecture" has become a delay tactic for not shipping. And a real caveat to consequence #2: model capability is a genuine contributor — a weaker base model can be the true ceiling. The 90/10 split is a heuristic for *where to look first*, not a claim that the model never matters. If a capable model succeeds in a short demo and fails in sustained operation with lost state, premature stopping, or unverifiable completion, investigate the harness first; if it fails the same *reasoning* task on its best single-shot try, the model may actually be the ceiling.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally the MHTE frame with the five clusters inside the Harness and the Anatomy Atlas (symptom → cluster → fix). Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
