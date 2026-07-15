---
name: rtp-tool-architecture
description: "Design an agent's tools as contracts — because a tool is where a model's reasoning becomes an action in the real world, and its load-bearing field isn't what it does, it's what it can't undo. Covers the tool contract (name, schema, identity/auth, authority, reversibility class), read-wide/write-narrow asymmetry, least-privilege escalation, the permissioned registry as a single owned surface, MCP (agent→tools) and A2A (agent→agent) with their 2026 trust shifts, tool presentation as context, and escape hatches (circuit breaker, kill switch, rollback). Use when: selecting an agent's tools, setting read vs write access, designing an MCP/A2A surface, auditing permissions, or specifying the tool layer of a harness. Pairs with: agent-harness (the T layer of MHTE; the narrow-gate pattern), harness-operating-model (governance ownership), safety-by-design (enforcement architecture), agent-ecosystem (multi-agent A2A depth), agent-spec (autonomy levels). Triggers: 'tool access', 'tool permissions', 'MCP', 'A2A', 'agent tools', 'tool contract', 'least privilege agent'."
imports:
  - determinism-compass
  - agent-harness
  - safety-by-design
---

# Tool Architecture

**The objective:** design the layer where an agent's reasoning turns into consequences — its tools — so that a wrong decision costs a recoverable event, not an irreversible one. This is the **T** in MHTE (Agent = Model + Harness + Tools + Environment): the harness decides *when and how* to act; the tool is *the act*; the environment is *where it lands*. Get the tool contract right and most "the agent misbehaved" incidents become "the agent tried something the contract wouldn't let it do."

## THE ONE IDEA

**A tool is a contract between the agent and the world, and its most important field is not what it *does* — it's what it *can't undo*.** Two tools can look identical in a schema and be worlds apart in consequence: `draft_email` and `send_email` differ by one irreversible bit. Design the tool layer around that bit and three consequences follow:

1. **Classify by reversibility, then grant read-wide / write-narrow.** Observation (read) and action (write) are different categories — read is cheap to be wrong about, write carries consequence magnitude. Grant broad autonomy on read-only verbs; require a signature on irreversible ones. Symmetric permission ("if it can read, it can write") is the most common tool-design error.
2. **Enforcement lives in the tool/permission layer, not the prompt.** "Don't refund over ₹5,000" in a system prompt is a soft request the model can talk itself out of; the ₹5,000 cap enforced in the tool's permission scope is architecturally impossible to breach. A tool that says what it is *not for* and cannot exceed its scope is a decision the model never gets wrong. (You can't prompt your way to a hard boundary.)
3. **The registry is a single owned surface, or it becomes tool sprawl.** Tools accumulate because every team ships its own; past ~20–50 tools the model's selection blurs (⚠ Shopify practitioner heuristic). The fix is a permissioned registry with one owner — the same narrow-gate discipline `agent-harness` teaches, seen from the tool side: fewer, sharper, negatively-scoped tools raise reliability *before* they save cost.

The spine in one line: **name the contract, classify the reversibility, grant the minimum, own the registry, and keep a way to kill it.**

## KEY TERMS (plain language)

- **Tool contract** — the full agreement a tool exposes: its name, its schema (typed args + returns), its identity/auth (whose credentials it acts under), its authority (what it's permitted to touch), and its reversibility class. If you can name all five without reading the harness, the tool is in the right layer.
- **Reversibility class** — the load-bearing field: read-only / write-reversible / write-audited / delete-irreversible / cascade (triggers other actions). It sets the gate.
- **Read-wide / write-narrow** — grant broad read access, narrow write access; asymmetric by design.
- **Least-privilege escalation** — start at the minimum access and earn wider access phase by phase, each phase audited before the next.
- **Permissioned registry** — the single, owned catalog of tools with their schemas, scopes, and reversibility classes; the surface that prevents sprawl.
- **MCP (Model Context Protocol)** — the open standard for how an agent calls *outside tools*. Schema, discovery, auth delegation, sandboxed execution.
- **A2A (Agent-to-Agent)** — the open standard for how one agent talks to *another*; 2026 adds Signed Agent Cards (cryptographic identity in the protocol).
- **Escape hatch** — the pre-wired way to stop a tool: circuit breaker, kill switch, rollback window, gradual disable.

## THE TOOL CONTRACT — the five fields every tool declares

A tool is not a function you expose; it is a contract you sign on the agent's behalf. Five fields, each a place a failure originates:

1. **Name & schema.** One tool, one verb, typed args and returns (`get_invoice_by_id`, not `query_data`). The schema is a contract with *both* the model and every downstream consumer — version it like a public API. Never copy the schema into the harness prompt; the harness *references* it, or the two drift and a tool call silently fails.
2. **Identity / authentication.** Whose credentials does the tool act under? The 2026 bar: an agent holds *its own* principal (account, scoped permissions, audit trail) — not a human's borrowed credentials. An agent on borrowed credentials is an audit finding waiting for its auditor. Credentials should never be reachable from the sandbox the agent's code runs in — vault them, proxy the call, keep the harness unaware of the secret (engineer the boundary; don't instruct the model to respect it).
3. **Authority.** What is this tool permitted to touch — all users, one user, one dataset, dev-only? Authority is scoped per compartment, not granted globally.
4. **Reversibility class.** The field that sets the gate (see below). Tag every tool.
5. **Failure mode.** What does it do when it fails — return an error shape, time out, partially complete? A tool whose failure mode you can't name is a tool whose incidents you can't triage.

## CLASSIFY BY MUTATION, GATE BY REVERSIBILITY

Every tool sits in one class, and the class sets the gate:

| Reversibility class | Examples | The gate |
|---|---|---|
| **Read-only** | file read, API query, search | Broad autonomy; rate-limit only. |
| **Write (reversible)** | draft email, dev-DB edit, temp file | Autonomous with post-log; easy undo. |
| **Write (audited)** | prod config, publish to staging | Threshold + audit entry; costly to undo. |
| **Delete (irreversible)** | drop table, purge logs | Human signature or hard confidence gate. No autonomous path. |
| **Cascade** | deploy, trigger workflow, broadcast | Manual approval, period — one bug fans out to many systems. |

**The rule that survives every review:** if an action is low-risk, reversible, and easy to verify, let the agent act autonomously; if it is irreversible, high-consequence, privacy-sensitive, or customer-facing, a control must *enforce* the check — deterministically for clear policy, human-in-the-loop for the rest. (This is the same "let the model reason vs. add a deterministic gate" matrix `agent-harness` applies at the Interception cluster; here it's applied at the tool boundary.)

## LEAST-PRIVILEGE ESCALATION — earn access, don't grant it

Start minimal; widen only after each phase is audited and error-free: (1) read-only on public data → (2) read on private data → (3) write on dev/sandbox → (4) write on prod behind a pre-approval gate → (5) write on prod with post-audit, high-confidence only. Default is *revoke*; access is *granted explicitly and reviewed quarterly*. The failure this prevents is **permission inflation** — an agent gets write on one table, then related tables, and a year later touches the whole database and nobody decided that.

## MCP AND A2A — the two protocols, and their 2026 trust shifts

Read them together: **MCP is how an agent calls outside tools; A2A is how one agent talks to another.** Both moved work *into the harness/tool boundary* in 2026 — this is where identity and state now get enforced.

- **MCP** — standard tool interface (discovery, JSON schema, auth delegation, sandboxed execution). The **July 2026 release candidate removed the protocol-level session** (no more `Mcp-Session-Id`): any request is routable to any server instance, so state that used to be implicit must be passed as *explicit tool arguments* (a `basket_id`, a `browser_id`). Audit implication: tag every MCP server with the version it targets and its state-handle strategy; treat each server as both a portability boundary and an attack surface (audit it like an IAM review — the simplest tool-description injection succeeded ~93% of the time across frontier models ⚠).
- **A2A** — agent-to-agent identity and task delegation. **v1.0 (2026) ships Signed Agent Cards** — a cryptographic ID one agent proves to another, not something claimed in a prompt. This splits one question into two audit trails: A2A answers *"who is this agent?"*; MCP's stateless core answers *"what did it know when it acted?"* Name an owner for each.

**PM decision:** standards (MCP/A2A) buy interoperability and easy tool-swaps at the cost of some latency/abstraction; custom connectors buy control at the cost of lock-in. Pick per workload. And remember every tool you expose costs context — tool descriptions consume tokens the model could spend reasoning, so *tool presentation is context engineering.* The mechanism (dynamic, task-scoped tool loading; skills as progressive disclosure) is the **narrow-gate pattern owned by `agent-harness`** — apply it here, don't re-teach it.

## ESCAPE HATCHES — design the kill before you need it

For every consequential tool, pre-wire the stop: **circuit breaker** (error rate > X% → disable for all agents), **human override** (any action reversible within a window), **kill switch** (consequence-magnitude threshold breached → lock immediately), **gradual disable** (revoke one user / one agent / one context at a time). A kill switch you build during the incident is not a kill switch. (Whether you can pull it faster than harm cascades is the proportionality question in `agent-risk`.)

## WHERE THIS SKILL MEETS YOUR STACK

Tool architecture is one layer of the agent; it hands off cleanly:

- **The whole machine + the narrow-gate pattern → `agent-harness`.** Tools are the T in MHTE; the harness owns *when/which* tool fires and the narrow-gate/skills discipline. This skill owns the *contract and permissions of each tool*; that skill owns the loop that calls them. (This is where the harness "Tool is the Contract" material is fully at home.)
- **Who owns the registry, and the governance of it → `harness-operating-model`** (the Harness PM, the audit chain).
- **Enforcement architecture (guardrails, vaulted credentials, injection defense) → `safety-by-design`**; **can you kill it faster than harm cascades → `agent-risk`.**
- **Multi-agent orchestration + A2A depth → `agent-ecosystem`**; **how much autonomy a tool's reversibility class warrants → `agent-spec` / `trust-ladder`.**
- **What must stay deterministic vs. tolerate model judgment → `determinism-compass`.**

The spine: **this skill decides what each tool may do and undo; the harness decides when to call it, safety-by-design decides how to enforce it, and the operating model decides who owns it.**

## DIAGNOSTIC QUESTIONS

1. For your riskiest tool, can you state its reversibility class and the gate that matches it? (If a delete or cascade tool has an autonomous path, that's the finding.)
2. Does the agent act under its *own* scoped principal, or borrowed human credentials? Are credentials reachable from the sandbox where its code runs?
3. Is your permission model read-wide / write-narrow, or symmetric by default?
4. Is there one owned registry, or do tools accrete per team? How many tools does the agent see per turn — and how many does it actually use?
5. For every consequential tool, name the escape hatch. Which is untested?
6. For each MCP server: do you control it, what does it expose, which MCP version does it target, and how does it carry state now that the protocol session is gone?

## QUALITY GATE

- [ ] Every tool declares its five-field contract (name/schema, identity/auth, authority, reversibility class, failure mode).
- [ ] Tools are classified by reversibility; the gate matches the class (no autonomous path for delete/cascade).
- [ ] Permissions are read-wide/write-narrow, scoped per compartment, revoke-by-default, reviewed quarterly.
- [ ] The agent acts under its own scoped principal; credentials are vaulted and unreachable from the code sandbox.
- [ ] Tools live in one owned, permissioned registry; the exposed set per task is narrow (narrow-gate via `agent-harness`).
- [ ] MCP servers are inventoried (owner, exposure, version, state-handle strategy); A2A identities have a named owner.
- [ ] Every consequential tool has a pre-wired, tested escape hatch (circuit breaker / kill switch / rollback / gradual disable).
- [ ] Audit logs capture action + decision metadata (confidence, gate applied, approval route, old/new value).

## WHEN WRONG

This skill over-applies when: the agent is pure-read with no mutations (rate-limit and move on — the reversibility machinery is overhead); there's no audit infrastructure yet (build logging first, or the permits are unenforceable); or the tools are user-facing rather than agent-facing (a different permission model). And a real caveat on the numbers here — the ~20–50-tool blur point, the injection-success rate, and the per-tool token overhead are practitioner-reported field patterns (⚠), not audited constants; use them to shape the design, then measure your own. Approval gates also add latency (a signature is +100–500ms); if users expect zero latency on a low-consequence action, that gate is friction, not safety — match the gate to the reversibility class, not to every call.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5: state the recommendation, name the key trade-off, acknowledge the biggest risk, define the next action.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally the reversibility ladder (read → write-reversible → write-audited → delete → cascade) with the matching gate on each rung. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
