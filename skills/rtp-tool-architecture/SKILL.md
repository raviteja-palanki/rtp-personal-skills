---
name: rtp-tool-architecture
description: 'Design tool access and permission boundaries to control consequence magnitude. Use when: selecting agent tools, read vs write access, sandboxing, audit infrastructure. Do NOT use: runtime enforcement (use determinism-compass), post-incident forensics (use stress-test).'
---
# Tool Architecture

## DEPTH DECISION

**Go deep if:** You're shipping agents to production, designing tool governance across multiple agents, building an MCP ecosystem, or need to audit tool access extensively.

**Skim to diagnostic questions if:** You want a quick permission audit for an existing agent.

**Skip if:** Single agent with limited tool access, or tool access already governed by external system.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

## WHERE TOOLS SIT (The T in MHTE)

In Anthropic's four-layer model (Agent = Model + Harness + Tools + Environment), tools are the **actionable surface** — the discrete, invokable functions or services the agent is allowed to call. They define *what* the agent can affect. The harness decides *when and how* tools are invoked. The environment defines *where* they execute and what persists.

Tools follow least-privilege scoping because overly broad tools shift risk downstream — a tool that can "run any shell command" effectively bypasses every harness guardrail. Single-purpose tool design (one tool per action, never a general-purpose shell) is now standard practice in production harnesses. Tools are invoked *by* the harness; their results feed back into the model *via* the harness. This separation is what makes tool governance possible.

## THE TRAP

You grant tools symmetrically: "if agent can read, it can write." The trap: observation (read) and action (write) are different categories. Read is safe. Write has consequence magnitude. Production requires asymmetric access: read widely, write narrowly.

## THE PROCESS

**Layer 1: Inventory tools by mutation**

Classify every tool your agent will touch:

1. **Read-only** (no state change): file read, API query, search, observe
2. **Write (reversible)** (state changes, can undo): modify dev database, draft email, create temporary files
3. **Write (audited)** (state changes, can undo but costly): modify production config, publish to staging
4. **Delete (irreversible)** (cannot undo): delete files, drop database table, purge logs
5. **Cascade** (triggers other actions): deploy code, trigger workflow, send broadcast message

**Layer 2: Define permission scopes**

For each tool, bind access to constraints:

- **Scope:** what resources can the tool touch? (all users, single user, specific dataset, dev-only)
- **Rate limit:** how often can it be called? (per second, per hour, per decision)
- **Approval gate:** does this require pre-approval, post-logging, neither?
- **Sandbox:** does this tool modify prod or a safe replica?
- **Rollback window:** if it fails, how long do we have to fix it? (5min, 1hr, never)

**Layer 3: Construct the tool permit**

For each (agent, tool, context) combination, specify:

```
TOOL: modify_user_settings
AGENTS: [personalization-agent, admin-agent]
SCOPE: [single-user only, not org-wide]
RATE: 1 per second, 100 per hour
APPROVAL: None (confidence >80%) | Post-log (confidence <80%)
SANDBOX: staging DB replica for testing; prod for confirmed actions
AUDIT: [agent_id, action, target_user, old_value, new_value, timestamp, confidence]
ROLLBACK: User can revert via UI within 24h
```

**Layer 4: Implement least privilege escalation**

Start with minimal access. Earn wider access.

- **Phase 1:** Read-only tools on public data
- **Phase 2:** Read tools on private data (with encryption in transit)
- **Phase 3:** Write tools on dev/sandbox (non-production)
- **Phase 4:** Write tools on prod with pre-approval gates
- **Phase 5:** Write tools on prod with post-audit (high confidence only)

Escalate only after each phase is audited and error-free.

**Layer 5: MCP at Scale**

Model Context Protocol has become the universal standard for AI-tool connections. MCP handles:

- **Tool discovery:** What tools are available? Model learns capabilities from introspection.
- **Schema negotiation:** What are the exact parameters, types, error codes? Each tool publishes JSON schema.
- **Authentication delegation:** Tools authenticate independently. Model never touches credentials.
- **Sandboxed execution:** Each tool runs in its own process, isolated from the model and other tools.

At 97M+ monthly downloads, MCP is the de facto standard. Adoption pattern: (1) Use pre-built connectors (GitHub, Slack, Postgres, Google Drive, Jira, HubSpot). (2) Build custom connectors for proprietary tools. (3) Compose complex workflows from standardized connectors.

**PM decision:** Which tools to expose? More tools = more tokens spent describing them = less context for actual task work. Every tool shown to the model consumes ~500 tokens of description overhead. Selective tool exposure is actually a form of context optimization.

**Layer 5b: A2A Protocol Patterns**

Agent-to-Agent protocol enables cross-agent communication and task delegation. Key patterns:

- **Capability advertisement:** Agent A declares to Agent B: "I can do X, Y, Z. Here's my schema."
- **Task negotiation:** Agent A proposes a task. Agent B accepts/rejects based on confidence, quota, or delegation rules.
- **Result verification:** Agent A doesn't trust Agent B's output blindly. Both agents verify results using shared checkpoints.
- **Error propagation boundaries:** If Agent B fails, Agent A decides: retry, escalate, degrade gracefully, or abort entire task.

**Critical PM decision:** Which agent-to-agent connections create value vs which create cascade risk? A2A enables loose coupling at organization scale. But a single failed agent in the chain can break the entire workflow. Implement explicit handoff checkpoints (human review, verification step, rollback trigger) before trusting multi-agent systems in production.

**Layer 5c: AG-UI Protocol for User Interface**

Agent-to-User-Interface (AG-UI) protocol streams agent state and actions to the frontend in real-time. Enables:

- **Real-time progress visibility:** User sees agent reasoning as it unfolds ("searching for...", "analyzing...", "deciding between...").
- **Human-in-the-loop checkpoints:** Agent reaches decision point, pauses, shows options, waits for user confirmation.
- **Transparent decision display:** When agent picks Tool A over Tool B, show the scoring. When confidence is low, flag it visually.

Implementation pattern: Agent publishes state updates to event stream. Frontend subscribes. User sees execution as it happens, can interrupt at any point.

**Layer 5d: Tool Presentation as Context Engineering**

Which tools you show the model IS context engineering. The constraint:

- 1 tool: ~200 tokens of schema description
- 5 tools: ~1000 tokens
- 20 tools: ~4000 tokens
- 100 tools: ~20000 tokens

At 20K tokens of tool description, you've lost 20% of a 100K token context window just to tell the model what it can do.

**Strategic approach:** Dynamic tool selection. Classify incoming tasks. For task type "send_email", load only email tools. For "code_review", load only code tools. For "data_analysis", load only data tools.

**Impact:** This alone improves agent quality 15-25% by freeing context for reasoning. The model can think deeper about fewer, relevant tools. Test: compare agent quality with 50 tools always loaded vs 5 tools selected per task. Newer models benefit even more from this (they're more context-sensitive).

**Layer 5e: Playwright MCP for Visual Testing**

Browser automation MCP (Playwright) enables agents to test their own output visually, not just code-level. Patterns:

- **Generative agents** build UIs (HTML, React, CSS). Playwright agent tests: "Does the generated button actually click?" "Does the form validation work?"
- **Evaluator agents** assess UX quality. Playwright agent navigates the live running application, takes screenshots, compares to golden images.
- **Regression testing** by agents. After deployment, agent runs Playwright tests against new environment, alerts if visual regressions detected.

This is distinct from traditional automated testing: agent can reason about visual appeal, layout consistency, accessibility, not just functional correctness.

**Layer 6: MCP and A2A Protocol Awareness**

Modern tool architectures converge on these protocols for agent-to-tool communication:

- **MCP (Model Context Protocol):** Standardized agent-to-tool interface. 97M+ downloads. Each tool is a connector (GitHub, Slack, Postgres, Google Drive). Adoption: buy a connector or build one. Advantage: interoperability, easier to swap tools. Disadvantage: abstraction overhead (~10-20ms per call), less control.

- **A2A (Agent-to-Agent):** Agent-to-agent communication across trust boundaries. Enables multi-vendor orchestration (my agent calls your agent calls their agent). Emerging standard. Advantage: loosely coupled, organization-scale. Disadvantage: versioning, error handling, protocol negotiation.

**PM decision point:** Are you betting on standard protocols (MCP, A2A) for long-term maintainability, or building custom connectors for short-term speed? Standards add latency; proprietary connectors add lock-in.

**Layer 7: Tool Selection Strategies**

When an agent has multiple tools that could do the job, which does it pick?

1. **Primary selection:** Agent picks the first matching tool (simplest, fastest, but naive)
2. **Scoring (preferred):** Agent scores all matching tools by: (accuracy expected, latency, cost) and picks highest score
3. **Fallback chain:** Try tool A; if fails, try tool B. Graceful degradation.
4. **User-directed:** Agent proposes tools, user picks. High confidence overhead.

Implement scoring for read tools (low cost). Use primary selection for common-path tools (optimization). Require fallback chains for critical paths.

**Layer 8: Tool Composition Patterns**

How do agents combine multiple tool calls into a workflow?

- **Sequential:** Tool A outputs feed Tool B inputs. Simple, but failures propagate.
- **Parallel:** Multiple independent tool calls, combine results. Faster, but requires merge logic.
- **Conditional:** IF tool A returns X, call tool B; ELSE call tool C. Adds complexity.
- **Iterative:** Loop over results, refine. Tool A generates candidates, Tool B scores, loop until threshold met.
- **Fan-out/fan-in:** Call tool A once, tool B N times on results, merge. Useful for batch operations.

Most agents use sequential + conditional. Avoid iterative unless explicitly scoped (max 3 loops).

**Layer 8.5: Design escape hatches**

For every tool, design a way to kill it:

- **Circuit breaker:** if error rate > X%, disable tool for all agents
- **Human override:** any agent action can be reversed by human within time window
- **Kill switch:** if consequence magnitude threshold breached, lock tool immediately
- **Gradual rollback:** disable access progressively (one user, one agent, one context)

## REALITY CHECK

**Failure modes:**

1. **Permission inflation:** Agent gets write access to one table, slowly gets access to related tables, now has access to entire database and no one knows.
   → FIX: Document every tool access grant. Review quarterly. Revoke by default, grant explicitly.

2. **Sandbox drift:** You test in sandbox, deploy to prod, sandbox rules don't apply. Agent does what it did in test (and it was safe there, unsafe here).
   → FIX: Prod tools must have explicit isolation. Read prod, write sandbox. If write prod, require approval or high confidence.

3. **Audit trail gone dark:** Tool logs "action happened" but not "why agent decided to act" or "what confidence level triggered it?"
   → FIX: Log decision metadata alongside action (confidence, approval_route, error_rate, alternatives_considered).

4. **Cascade trap:** Agent calls Tool A (modify config), Tool A triggers Tool B (restart service), Tool B triggers Tool C (reload data). One bug in A breaks three systems.
   → FIX: Cascade tools need manual approval. Period. Or require explicit opt-in by user.

5. **Rate limit ambush:** You limit writes to 100/hour. At 80/hour, agent is fine. At 90/hour, system degrades. Agent doesn't know until it hits the wall.
   → FIX: Implement soft limits (warn at 70%, slow down at 80%, block at 100%). Agent knows when it's approaching boundary.

**Cost at 10x scale:**
- 1 tool: you hand code permissions, works fine
- 10 tools: patterns emerge, you need a permission matrix
- 100 tools: you need a policy language (RBAC, ABAC, policy-as-code)
- 1000 tools: you're building a full capability model with formal verification

**Latency impact:**
- No gates: +0ms, maximum consequence magnitude
- Pre-approval: +100-500ms (wait for human signature)
- Post-audit logging: +10-50ms (write to audit DB)
- Permission check (on-the-fly): +1-5ms per tool call (cache hits matter)

## QUALITY GATE

- [ ] Every tool is classified by mutation type (read, write-reversible, write-audited, delete, cascade)
- [ ] Permissions are scoped: (agent, tool, resource, rate, approval_gate, sandbox)
- [ ] Audit logs capture: action + decision metadata (confidence, gate applied, approval route)
- [ ] Escalation path is explicit: read → sandbox write → prod write with approval → prod write with post-audit
- [ ] Escape hatches exist: circuit breaker, rollback window, kill switch, gradual disable

## WHEN WRONG

This skill gives bad advice if:

1. Pure-reading agent (no mutations). Use determinism-compass for read policies.
2. No audit infrastructure. Build logging first.
3. Writes always reversible. Focus on rate limiting instead.
4. Users expect zero latency. Approval gates add time. Accept tradeoff.
5. Tools are user-facing, not agent-facing. Use different permission model.

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
