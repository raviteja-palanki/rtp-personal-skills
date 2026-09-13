---
name: rtp-observability-stack
version: v1.0.1_latest
description: 'Choose and operate an AI observability platform with a clear purpose, controlled data collection, and a practical exit path. Connect tracing to evaluation, datasets, experiments, and regression checks. Compare Phoenix, Arize AX, LangSmith, or structured logs against deployment needs, operating cost, useful features, and migration effort. Explain OpenTelemetry, OTLP, OpenInference, and GenAI semantic conventions without promising effortless portability. Check query freshness, export limits, sensitive fields, access, and write-capable tools before production data flows. Use for observability selection, agent instrumentation, trace-to-eval setup, or a tooling audit. Start with production-observability when the monitoring questions are unclear; use eval-framework and eval-driven-development for evaluation design. Triggers include "which observability tool", "Arize vs Phoenix", "LangSmith", "set up tracing", "OpenInference", and "vendor lock-in on traces".'
imports:
  - production-observability
  - eval-framework
  - eval-driven-development
---

# Observability Stack

Choose a stack that helps the team explain system behavior and act on failures. Make the collection boundary and migration plan explicit before connecting production data. A tracing standard can reduce switching work; it does not make the entire platform interchangeable.

## Start with the decision and data boundary

Use a quick pass for an existing setup: check the missing-trace example, data safeguards, and five diagnostic questions. For a platform selection or production audit, work through all five steps and complete the output. The original 10-minute and 60–90-minute estimates are planning aids, not completion guarantees.

This skill consumes the monitoring question, deployment and data constraints, current application framework, and operating capacity. It produces a backend recommendation, an instrumentation plan, an audit of important defaults, and a record of checks still open.

`production-observability` defines what to monitor and why. This skill selects and operates the infrastructure for those signals. `eval-framework` defines evaluation validity; `eval-driven-development` connects tests to development; `gen-ai-experimentation` designs experiments. Read the relevant sibling when its decision is unresolved, rather than repeating work already completed.

Before a real trace is collected or exported, establish its allowed contents, destination, access, retention, and purpose. Reuse existing authorization where it covers the action. A writing or selection task alone does not authorize transferring production prompts.

## Understand the parts that can become expensive to move

The subscription is only one switching cost. Instrumentation at model calls, tool handlers, and retrievers can create dependencies throughout an application. Datasets, annotations, evaluator definitions, dashboards, access rules, and historical traces create additional migration work. This accumulation is **data gravity**.

| Term | Meaning |
|---|---|
| Span | A timed operation, such as retrieval, a model request, or a tool call, with identifying attributes and optional events. |
| Trace | Related spans sharing a trace ID, commonly organized by parent relationships. A request may cross services, queues, or trace boundaries; use appropriate context propagation and links. |
| Session | An application grouping, often a conversation containing several traces. Define its boundaries explicitly. |
| OpenTelemetry / OTLP | OpenTelemetry provides telemetry APIs, SDKs, and collection infrastructure. OTLP is its transport format/protocol for telemetry. Transport support alone does not prove field compatibility. |
| OpenInference / GenAI conventions | OpenInference supplies AI instrumentation and semantic conventions. OpenTelemetry also maintains GenAI conventions. Specify which convention and version each component produces and accepts. |
| Data gravity | The accumulated data and workflows that make a backend costly to replace, even when new spans can be sent elsewhere. |

OpenInference fields such as `llm.input_messages`, `tool.name`, `retrieval.documents`, and `session.id` illustrate semantic content; verify exact names and supported mappings in the selected version. Useful telemetry does not require every prompt, document, or identifier to be stored in full.

## A missing-trace example

At 2 p.m., a team deploys a prompt fix. A query for the last hour returns nothing. They assume ingestion broke and roll back. One possible explanation is delayed indexing: direct trace lookup and filtered search can become available at different times.

Treat that as a diagnosis to test. Check the trace ID, environment/project, permissions, time zone and range, sampling, exporter flushing and errors, clock alignment, pagination, and ingestion status. Compare query paths using a known synthetic event. A direct lookup can also lag or fail; an empty time-range result alone does not establish either a deployment failure or an indexing delay.

The original skill attributed a **6–12-hour** Arize delay to vendor tooling documentation from 29 July 2026. This revision did not recover a supporting primary source or measure the platform. Keep the number as an unresolved historical claim, not a current service expectation. See [source and audit notes](references/platform-and-audit-notes.md).

## The five-step process

### 1. Name the decision the telemetry supports

Complete: “With this telemetry, we will be able to decide ______; today we rely on ______.” Examples include diagnosing a quality regression, attributing token cost, confirming tool execution, investigating an incident, or producing an appropriate audit record.

If the purpose is exploratory diagnosis or future incident readiness, say so and size collection accordingly. There need not be a known failure before instrumentation is useful. Avoid collecting every field merely because a dashboard supports it.

Where record-keeping is required, identify the applicable obligation, system scope, accountable owner, and retention rule. EU AI Act Article 12 addresses logging capabilities for covered high-risk systems; applicability and timing need a current assessment. NIST AI RMF guidance is not itself a universal legal obligation, and MANAGE 2.1 concerns resources and alternatives, not a blanket event-log requirement. An audit need still requires a collection and backend decision; do not skip them.

### 2. Design instrumentation and test its portability

Prefer widely supported telemetry interfaces when they meet the task. Select OpenTelemetry instrumentation, suitable AI semantic conventions, and an exporter/collector arrangement that preserves the fields you need. A vendor SDK can be a reasonable choice when it provides material benefits; document its coupling and alternatives.

Record:

- Required span relationships, statuses, latency/cost units, tool results, retrieval references, and application/version identifiers.
- Actual provider and model identity for each model decision, including retries and fallback routes. Distinguish the requested alias from the served model/version; mark identity unavailable when the provider does not expose it.
- Sampling and redaction location, export failure behavior, buffering limits, and the effect of instrumentation on latency and cost.
- Convention and SDK versions, vendor-specific attributes, mappings, authentication, and endpoint configuration.

Use a small synthetic workflow to verify a second backend or export format when exit risk matters. Check nested spans, links, errors, streaming, model identity, and the fields the evaluations consume. Also test export/reimport of an example dataset and annotation if those are essential assets.

An endpoint change may redirect compatible new traces. It does not automatically migrate history, dashboards, identities, rubrics, experiments, or permissions. Estimate actual work rather than promising an afternoon switch or treating any code change as proof that standardization failed.

### 3. Select the backend against the operating need

Evaluate data location and control alongside useful features, integration, reliability, query behavior, scale, cost, and team capacity. These options are examples, not the complete market:

| Option | A reason to consider it | What to verify |
|---|---|---|
| Arize Phoenix | Self-hosted tracing and evaluation can fit teams that need control of deployment and storage. | Current license, supported instrumentation, authentication, retention, backup, upgrades, and every outbound connection. The repository identifies Elastic License 2.0; do not infer unrestricted use from an “open source” label. |
| Arize AX | A managed environment may reduce the work of connecting traces, evaluations, datasets, and experiments. | The specific deployment offering, residency, access controls, contracts, query freshness, export completeness, cost, and operational support. |
| LangSmith | Integrated tracing/evaluation may fit LangChain/LangGraph applications or other frameworks. | Current OpenTelemetry support and mappings, enterprise/self-hosted licensing where relevant, deployment constraints, migration, and the features actually needed. It is not limited to LangChain applications. |
| Structured logs and a notebook | A small or simple workflow may need only searchable events and focused analysis. | Whether troubleshooting, collaboration, access, retention, and repeated evaluation remain manageable. Volume alone does not determine when to adopt a platform. |

Self-hosting does not automatically prevent data egress: model APIs, evaluators, telemetry, support access, and backups may cross the boundary. It also does not remove the need for an appropriate security/privacy review. For hosted services, determine exactly what leaves which boundary and under whose authorization. Use the applicable review process; do not assume every deployment requires the same assessment.

Features do not reliably converge on a two-quarter timetable. A feature that makes an important investigation possible can justify a platform choice. Record what matters enough to accept additional coupling, then test that capability.

### 4. Connect traces to learning

Build the loop: **trace → investigate failure → curate dataset → run experiment → retain useful regression check → monitor production**.

Preserve enough context to reproduce the failure without copying unnecessary customer data. Label the expected behavior, source of judgment, dataset version, and known limits. Include successes, edge cases, and underrepresented slices where needed; an error-only dataset cannot estimate overall production performance.

Validate the fix using `eval-framework` and `eval-driven-development`, then check the relevant production outcome. A regression test reduces the risk of repeating a known failure; it does not make a fix permanent or cover every related failure.

The original Arize workflow named `arize-instrumentation`, `arize-trace`, `arize-evaluator`, and `arize-experiment` as the four core skills, with `arize-compliance-audit` for relevant compliance questions. Check the installed tool inventory and contracts before relying on these names or the historical count of thirteen skills. Compliance guidance does not itself establish compliance.

A lightweight loop is useful before product-market fit as well as afterward. Let changing failure categories lead to revised datasets and criteria, without turning every exploratory observation into a permanent gate.

### 5. Check collection and tool defaults before production use

Apply these checks to any platform. Scale the effort to the data and consequences, including sensitive data in a scratch project.

| Default to inspect | Safe, useful operating decision |
|---|---|
| Export scope and limits | Set the project, time range, fields, row/byte cap, pagination behavior, and destination. If a limit is reached, report truncation or use the authorized bounded continuation; do not silently rerun unbounded. |
| Sensitive span content | Minimize or redact before the earliest persistent or external capture, including local logs and debug output. Inspect prompts, outputs, retrieval content, identifiers, errors, and custom metadata. Check that downstream collectors and evaluators receive only allowed data. |
| Tool side effects | Read each operation contract. Querying, exporting, annotating, deleting, and running an evaluator have different effects. A tool called “trace” or “read-only” may expose write operations; authorize the actual action and scope. |
| Files and reports | Choose an appropriate destination, access, encryption, retention, and cleanup. Temporary directories are not inherently unsafe or outside organizational control, but a default path is not a data-handling decision. Reports can expose sensitive system details. |

The prior author recorded four Arize source-audit findings on 29 July 2026: unbounded export retry, sensitive span fields, annotation batches of up to 1,000, and a temporary report destination. Retain them as dated audit leads, not verified behavior of every current installation. Distinguish application-level encryption, encrypted storage, and access protection; a JSON file alone does not establish whether its disk is encrypted.

## Five diagnostic questions

1. What would moving vendors require for instrumentation **and** stored assets? Which parts have been tested?
2. How fresh are direct lookup and filtered queries under normal and overloaded conditions? What was measured, and when?
3. What sensitive information can the busiest span capture, and which fields are necessary for its purpose?
4. How does a discovered failure become a useful test, an accountable change, and a production check?
5. Who can collect, view, export, annotate, and delete production telemetry? What authorization covers those actions?

For a quick audit, inspect one authorized, minimized trace or a synthetic trace in the approved environment. Confirm its actual fields and query behavior. Do not begin by bulk-exporting raw production content to a local directory.

## Output: where the setup stands

```markdown
# Observability Stack: [Product]

## Purpose and scope
Decision or audit need: [what this enables]
Data/environment: [allowed contents, destination, access, retention]
Authorization and owner: [existing basis or unresolved decision]

## Instrumentation and exit
Interfaces/conventions/versions: [choices and mappings]
Required fields: [including requested and served model identity]
Sampling/redaction/export behavior: [design and checks]
Migration estimate: [code/config, history, datasets, annotations, dashboards]
Portability check: [tested example, results, limits]

## Backend
Choice and alternatives: [recommendation with reasons]
Capabilities/control/cost/operating trade-off: [accepted cost]
Data movement and approval: [specific boundary, scope, owner]

## Query freshness
Direct lookup: [result/lag or unknown]
Filtered search: [result/lag or unknown]
Evidence: [measured environment/date, documented claim, or unchecked]

## Learning loop
Trace → investigation → dataset → experiment → regression → production
Working links: [evidence] · Gaps and owners: [next action]

## Safeguards and open decisions
Exports: [bounds/destination]
Sensitive data: [minimization/redaction/access/retention]
Write operations: [inventory and authority]
Reports: [storage and handling]
Not checked: [specific limitations]
Next action: [owner, scope, success condition]
```

## Review the recommendation

Label evidence plainly: **observed/tested** with method and environment; **documented** with provider, version, and date; **unverified** with the missing check. Reading a source verifies what it says, not the behavior of the installed product. The historical ✅/◆/⚠ labels may be used if their meaning is explicit and does not merge these tiers.

Confirm that the choice meets the important monitoring need, respects the data boundary, explains operating and migration costs, and states what remains untested. Do not claim a raw span was inspected when only documentation was reviewed.

Reconsider standard-first instrumentation if a required capability is lost, mapping costs exceed the expected exit benefit, or supported conventions diverge. Reconsider the backend when query delays, operating burden, or export gaps prevent useful decisions. These are concrete tests of the recommendation, not reasons to assume portability has no value.

The trade-offs remain explicit: portable instrumentation may give up native convenience; control of data may add operating work; useful native features may add coupling; collection safeguards require setup effort. Use a diagram only when it clarifies the migration dependencies, measured query paths, or the trace-to-evaluation loop.
