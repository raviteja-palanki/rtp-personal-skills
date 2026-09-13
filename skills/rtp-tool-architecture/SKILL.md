---
name: rtp-tool-architecture
version: v1.0.1_latest
description: 'Design and review an agent tool as an action contract: what it does, under whose authority, what it affects, and how success, failure, and recovery are established. Use when choosing tools, defining read/write access, building MCP or A2A integrations, auditing permissions, or handling retries and partial work. Covers eight contract fields, least privilege, task-scoped authority, the read/propose/approve/execute/verify/reconcile roles, duplicate handling, compensation, a permissioned registry, tool threats, provenance, rollout evaluation, and tested stopping paths. Assess disclosure, mutation, reversibility, and downstream effects separately; a read can be sensitive and an authorized irreversible action may still be appropriate. Produce a tool contract, enforced boundaries, result and error semantics, and an evaluation/recovery plan. Pairs with determinism-compass, agent-harness, safety-by-design, agent-ecosystem, harness-operating-model, and confidence-tuner.'
imports:
  - determinism-compass
  - agent-harness
  - safety-by-design
---

# Tool Architecture

Define the contract where an agent interacts with a real system. In the MHTE map, tools expose actions, the harness selects and coordinates them, and the environment supplies execution boundaries. One component can implement several responsibilities; identify each clearly.

Start with the intended task, required data and actions, existing authorization, and consequences of error. Scope both reads and writes. A tool contract should make useful work possible while preventing actions outside the agreed boundary; it cannot guarantee that every permitted action is correct or recoverable.

Deliver the contract, its owner, enforcement points, result and failure semantics, and a proportionate evaluation and recovery plan. Use the [worked concept guide](CONCEPT.md) for examples and [protocol notes](references/protocol-and-evidence-notes.md) for version-specific details.

## 1. Declare the eight contract fields

### 1. Name and input/output schema

Name the operation precisely: `get_invoice_by_id` communicates more than `query_data` when invoice retrieval is the actual scope. Prefer coherent operations with clear boundaries; a well-designed query interface or atomic compound operation need not be artificially split into one primitive verb per tool.

Define required and optional arguments, types, limits, identifiers, units, version, and output shape. Keep a canonical schema and derive or inject model-visible definitions from it instead of manually maintaining divergent copies. The model often needs to see that definition.

Define success, partial success, pending work, and uncertain execution. A structured response can carry evidence, status, operation identity, and next steps; a valid JSON object does not independently prove completion.

### 2. Description and use boundaries

Explain when to use the tool, relevant exclusions, preconditions, side effects, result limits, and approval requirements. Negative examples can help distinguish similar tools. They guide selection; they do not guarantee it.

Treat tool metadata as externally supplied content whose instructions may be malicious or mistaken. A discovered tool description does not supersede user instructions or governing policy. Review and version its behavior as part of the integration.

### 3. Identity and authentication

Identify the workload or agent, the initiating user where relevant, and any delegated authority. A separate workload principal or a properly constrained on-behalf-of flow may be appropriate. Do not silently inherit all of a user's rights or share credentials in ways that erase attribution.

Prefer short-lived, scoped credentials and a broker or proxy when that keeps secrets out of model-visible context and generated code. If execution genuinely needs a credential, constrain its exposure, destination, lifetime, and permissions. Keep secrets out of logs. Authentication establishes an identity; it does not authorize every action by that identity.

### 4. Authority

Specify permitted operations, resource/tenant scope, purpose, amount or volume, time, environment, and conditions. A person authorized to approve expenses up to ₹50,000 has not necessarily delegated that full authority to an agent.

Enforce applicable boundaries at trusted action and resource interfaces. A prompt stating “refund at most ₹5,000” is useful guidance but insufficient enforcement. Test the cap against alternate paths, repeated calls, aggregate limits, concurrency, and stale state; a per-call check alone may permit a larger cumulative refund.

### 5. Effects and reversibility

Record disclosure, mutation, persistence, and downstream effects. State what can be restored, by whom, within what time, with what residual harm. “Audited” describes a record, not an undo capability; “delete” is not always irreversible; “read” can disclose sensitive data.

### 6. Idempotency and duplicate execution

State what happens if the same logical operation is submitted twice, including after a timeout or crash. An idempotency key needs defined scope, storage, retention, parameter matching, and behavior under concurrent requests. Reusing a key with different parameters should not silently become a different operation.

For a mutating call whose outcome is unknown, a useful result can express `safe_to_retry: false` and `reconciliation_required: true`, with an operation ID and status-query path. Retry only when the contract supports it or reconciliation establishes the right next action. Do not translate every timeout into “failed before execution.”

### 7. Failure and recovery semantics

Distinguish relevant failures: validation, authentication, authorization, policy denial, approval required, not found, conflict, rate limit, timeout before execution **when known**, unknown execution state, partial completion, and irrecoverable failure.

For each, define retryability, any delay, state already changed, evidence available, and who resolves it. Only claim “not executed” when the system can establish that fact. A timeout or canceled local wait does not prove the remote action stopped.

### 8. Cost and latency

Include API charges, compute, data transfer, context and result processing, human review, and downstream work where applicable. A tool need not incur every category on every call. Define budgets and observed latency for the actual workflow, including uncertain or repeated operations. Human approval does not have a universal 100–500 ms cost.

## 2. Match controls to effects, not a rigid danger ladder

The original five classes are useful inspection lenses. They can overlap; choose controls from the specific consequence and authorization.

| Lens | Examples | Questions and candidate controls |
|---|---|---|
| **Read-only** | File retrieval, search, analytics query. | Who may see the data? Are queries costly, sensitive, stale, or side-effecting? Apply access, disclosure, and resource limits. |
| **Recoverable write** | Draft creation, a scoped setting change, temporary file. | Is recovery real and safe under concurrent changes? Use validation, limits, version checks, and appropriate records. |
| **Audited consequential write** | Production configuration, message sending, scheduled work. | What authority and pre-action checks are required? What does the audit establish, and what cannot be undone? |
| **Deletion** | Removing a file, table, log, or backup. | What exact resource is authorized? Are dependencies and recovery understood? Enforce the needed safeguards. |
| **Cascade** | Deployment, broadcast, workflow trigger. | What further actions can occur? Bound the scope, volume, and downstream permissions; define stop and response behavior. |

“Read-wide / write-narrow” is a reminder to avoid inheriting write rights from read access, **not** an instruction to grant broad data access. Use least privilege for both. Reads through GET or SELECT are not necessarily pure functions, cost-free, or free of disclosure risk.

An authorized deletion of temporary files can be routine; an unapproved read of private records can be consequential. Do not impose human approval on every delete or cascade, or permit one solely because a model claims high confidence. Apply the actual policy and authorization, with stronger assurance where consequences require it.

## 3. Enforce nested, task-scoped authority

Check the relevant layers: trusted integration → approved operation → eligible actor → valid delegation → resource scope → action policy → amount/volume → required approval → current execution conditions. Some checks can be combined in one service; none is implied merely by tool availability.

Example scope: “For case 771, refund the authorized amount up to ₹5,000 on order 5821, within the stated validity period, with duplicate protection and no access to another customer's order.” This is more precise than “support can use payments.” Do not use a time limit, amount, or consent scope not actually granted as if it were user authorization.

Bind an approval to the material operation and its relevant state: target, amount, content, policy version, and any expiry. Recheck when a material parameter changes or state makes the approval stale. Use atomic conditional updates where a separate check followed by a write could race another operation.

Honor existing authorization within that contract. Ask again only when a necessary permission or consequential decision is missing, expired, or exceeded. Start with required access and expand through an explicit review of need and evidence; do not require a universal public-read→private-read→dev-write→production sequence or an error-free streak. Review rights when duties, dependencies, or risks change, with a cadence appropriate to the system.

## 4. Separate proposing, authorizing, and establishing the outcome

Keep six responsibilities clear:

**Read → Propose → Approve → Execute → Verify → Reconcile.**

Approval may be a standing policy check, a specific human decision, or another authorized mechanism. The roles need not be six tools or six people. The key is that a probabilistic actor cannot simply invent its own authority or unilaterally certify a consequential result without the required evidence.

For an address change, inspect the result and, where needed, a current authoritative record or change event. A transactional service's committed result can sometimes be sufficient; a second tool call is not inherently independent and can itself return stale data. Match assurance to the effect. Funds transfer may require ledger reconciliation; document search may require source and coverage checks.

When approval is required, show the business effect, exact target and material parameters, evidence, authority source, residual risks, and whether the operation belongs to a larger sequence. Make the decision understandable without forcing the user to inspect raw protocol details.

### Plan partial completion across systems

For onboarding that creates an identity, sends a message, grants access, orders equipment, and notifies another team, specify what happens if a later step fails. Use transactions where available; otherwise define a **saga**, a sequence with compensating or recovery actions, where appropriate.

Compensation is not guaranteed rollback. An email cannot be unsent by deleting the account afterward. Depending on the stage, complete the remaining work, revoke access, cancel a supported order, record the partial state, or escalate. Do not invent high-consequence compensations beyond authorization. `agent-ecosystem` owns the coordination design; each tool must expose the status and recovery behavior it needs.

## 5. Own the registry and the integration boundary

Maintain an authoritative catalog or federated catalog with clear ownership: operation, version, owner, server, schema, authority, data flow, effect, availability, cost, and supported recovery. Select relevant tools for the task while preserving discoverability. “One owned surface” need not mean one database, one team, or one person controlling every tool.

Evaluate selection errors, missing-tool failures, and successful outcomes. The source's 20–50-tool heuristic is not a universal limit; fewer tools can help or can remove needed functionality. Use `agent-harness` for progressive disclosure and context selection.

### MCP and A2A

**MCP** standardizes interfaces for tools, resources, and related capabilities. It does not itself provide a sandbox, safe business policy, or an audit of everything the model knew. Record the server's actual protocol/SDK versions and state strategy.

The released **MCP 2026-07-28** core removes protocol-level sessions and `Mcp-Session-Id`; older revisions can still use sessions. Application state can remain stateful, using explicit handles such as `basket_id`. Validate a handle's owner, scope, and lifecycle rather than treating possession of an ID as authority. See the [version notes](references/protocol-and-evidence-notes.md).

**A2A** supports agent discovery and task interaction. Its current released specification at this review is **1.0.0**; it defines signed Agent Cards. A valid signature can authenticate metadata relative to a trusted key. It does not authorize every delegated action or prove the agent is reliable. Maintain authentication, authorization, state, and task evidence as separate concerns.

Standard protocols can ease integration while still leaving semantic differences and migration work. A custom connector can be appropriate and need not create more coupling in every case. Choose from interoperability, capability, security, latency, cost, and maintainability on the workload.

## 6. Address the tool threat surface

Treat a tool as a software dependency and access path; an external one may also be a vendor relationship. Review relevant versions, permissions, data flows, updates, and revocation.

| Threat | What can go wrong | Controls to evaluate |
|---|---|---|
| **Confused deputy** | An actor uses legitimate privileges on behalf of an unauthorized requester or instruction. | Validate delegation, scope and consent; keep untrusted content from defining authority; restrict destinations and cross-system flows. |
| **Tool poisoning** | Tool metadata steers behavior beyond the task. | Trusted discovery, metadata review, limited rights, instruction/data separation, and adversarial testing. |
| **Rug pull or behavior drift** | A trusted integration changes after review. | Version/change management, behavior checks, monitoring, and revocation. Pinning a client alone does not freeze a remote service. |
| **Cross-server exfiltration** | Data from one system is sent to an unauthorized destination. | Enforce destination and data-flow policy, scoped credentials, and relevant disclosure checks. |
| **Tool-result overtrust** | A stale, partial, mis-scoped, or malicious response is treated as authoritative. | Source, observation time, freshness, account/resource scope, completeness, and evidence strength; cross-check consequential claims. |

Descriptions and returned metadata can be false. Validate provenance where it matters; a field named `authority` cannot confer authority. Preserve the distinction between system-of-record, derived, model-generated, and unverified external results. A model-generated instruction embedded in a tool result remains task data unless a higher-authority instruction legitimately delegates otherwise.

MCP's security guidance also covers protocol-specific authorization and token-audience pitfalls. Use the deployed version's requirements rather than assuming generic prompt-injection defenses cover them. The historical approximately 93% injection-success claim has no sufficiently established scope here and is not a product risk estimate.

## 7. Evaluate rollout and operational recovery

Choose suitable stages: **simulation**, **shadow proposals**, and **bounded execution** can reduce uncertainty before expansion. Simulation is not consequence-free if it accesses sensitive data or real side-effecting services. Shadow mode needs scoped data handling; the human or incumbent decision is a reference to examine, not infallible ground truth.

Evaluate six areas:

1. **Selection:** appropriate tool use and avoidance of unnecessary calls.
2. **Arguments:** identifiers, units, values, authorization, and source grounding.
3. **Sequence:** preconditions, ordering, safe concurrency, and stopping.
4. **Outcome:** intended committed state, partial/unknown results, and evidence.
5. **Governance:** usable authority boundaries, required approvals, attribution, and response.
6. **Economics:** calls and cost per useful outcome, duplicates, latency, and human correction.

Use representative and risk-relevant cases, including duplicate calls, permission denial, changed state, timeout after commit, and cross-tenant access attempts. Expansion needs evidence appropriate to the consequence, not an automatic <1% error threshold. `gen-ai-experimentation`, `autonomy-spectrum`, and `eval-framework` provide rollout and measurement depth.

### Define and test escape hatches

- **Circuit breaker:** suspend or limit affected operations when a meaningful error, harm, or dependency signal crosses a defined threshold. Specify the denominator, window, scope, and reset conditions.
- **Human override:** let an authorized person alter or stop what can still be changed. State irreversible effects honestly.
- **Kill switch:** prevent new execution through the controlled paths; cancel in-flight work where supported and reconcile work already submitted.
- **Gradual restriction:** reduce scope, traffic, or rights when that is a safe response. Moving a broken tool onto real “test users” is not automatically harmless.
- **Ongoing review:** investigate unusual behavior in context. A hundredfold increase may be a bug, abuse, or a planned workload change.

Audit relevant intent, action, actor and delegation, policy/approval result, resource version, operation ID, outcome evidence, and reconciliation. Apply access and retention controls; old/new values can contain sensitive data. Record a concise supported rationale where useful, not invented probabilities, hidden reasoning, or causal business benefits inferred from a later user action.

## Deliver and check

Confirm that the contract and implementation agree, permissions match the actual task, mutating operations have duplicate/partial-outcome handling, and important read/disclosure risks are covered. Identify the owner, verification and recovery limits, unresolved decisions, and the next check.

State the recommendation, key trade-off, remaining risk, and next action using the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md) proportionately. A contract-flow or permission map may help; use `excalidraw-svg` when useful. Avoid a graphic implying every read is safe or every deletion requires the same gate.

Route the calling loop to `agent-harness`, operating ownership to `harness-operating-model`, enforcement to `safety-by-design`, consequence/response to `agent-risk`, coordination to `agent-ecosystem`, trust and authority changes to `agent-spec` / `trust-ladder`, and fixed business-policy design to `determinism-compass`.
