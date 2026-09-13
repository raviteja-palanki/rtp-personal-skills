# Protocol and evidence notes

Checked 13 September 2026. Pin the version the deployment actually supports; current documentation is not evidence that an existing client has migrated.

## MCP

The official [2026-07-28 release announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) confirms a released specification, not only the release candidate described in the original skill. Its core removes the initialization/session exchange and `Mcp-Session-Id`, supports self-contained requests, and leaves application state possible through explicit handles. An application still owns handle authorization, state storage, consistency, and recovery; stateless transport does not establish everything an agent knew or eliminate application coordination.

The [2025-11-25 transport specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) allowed optional Streamable HTTP sessions. Do not remove session handling from an older supported integration merely because the new specification changed. Check protocol negotiation, SDK support, and migration behavior.

The versioned [MCP security guidance](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) distinguishes confused-deputy authorization flows and prohibited unvalidated token passthrough. A legitimate delegated user identity is not the same as forwarding a token with the wrong audience or bypassing consent. Review the relevant version's exact authorization requirements.

## A2A

The [official specification](https://a2a-protocol.org/latest/specification/) identified **1.0.0** as the latest released version at review. It defines `AgentCardSignature` using JWS. Signature verification depends on a trusted key and the signed content; it does not establish permission for a transaction or correctness of a task result. The specification uses major/minor protocol versions, such as `1.0`, for negotiation, distinct from a specification patch or an agent application's version.

The ecosystem skill's explicitly pinned 0.3 reference can remain relevant for that version; implementations seeking current 1.0 behavior must check the newer contract and migration differences. Do not mix version-specific examples.

## Historical heuristics and general design claims

The source's 20–50-tool selection limit, approximately 93% tool-description-injection success rate, and 100–500 ms signature overhead lack adequate primary workload and method scope in this pass. They should not become current limits, security probabilities, or human-review budgets. Tool count, metadata, and approval latency are worth measuring without those fixed numbers.

Descriptions, names, schemas, audit records, and signatures each address a particular problem. None makes every permitted action correct. A deterministic gate can enforce a precise rule only to the extent its implementation, state, and complete action paths support that rule.

## Novel Insights applied

The ledger's governance passage asks who can alter a prompt that influences escalation. Apply that question to tool metadata, routing, and business policy too. Review the trusted controls and their change authority; do not assume a reporting line alone makes escalation work, or that changing a prompt necessarily defeats correctly enforced permissions.

The broader control-scope lens also clarifies this skill: audit is not rollback, schema validity is not business correctness, and a plausible result is not evidence of committed state. Preserve these distinctions in both the contract and the example logs.
