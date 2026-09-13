---
name: context-spec
version: v1.5.1_latest
description: 'Design how an AI feature receives, updates, and preserves the information it needs. Use for retrieval, tools, conversation state, or long tasks when the team needs an implementable context architecture. Map the seven CONTEXT layers; specify source authority, freshness, token and latency budgets, compaction, memory, tool visibility, and failure behavior. Measure a working budget for the actual model and task: there is no universal 50–60% quality limit. Include expert judgment and source-conflict handling where needed. Deliver a layer map, budget table, recovery rules, and verification plan. Use a short version for simple features; skip the full process when there is no material context problem. Pairs with invisible-stack for diagnosis, prompt-craft for instructions, prompt-as-product for change control, and agent-spec or agent-harness for orchestration. Triggers: context engineering, context architecture, token budget, context window, agent memory.'
imports:
  - invisible-stack
  - determinism-compass
  - stress-test
---

# Context Spec

Design what information reaches the model, where it comes from, and what happens when it is missing, stale, conflicting, or too large. The result should let an engineer implement the flow and expose unresolved decisions before they become accidental behavior.

**Context capacity is a technical limit; context quality is an empirical result.** A larger window can help when it contains relevant evidence. Additional noise, contradictions, or missing distinctions can hurt. Do not treat 50–60% of a window as a universal “Pre-Rot Threshold,” or describe an advertised 128K window as having a proven 70K usable limit. Anthropic describes gradual, model-dependent degradation rather than a fixed cliff. [Primary context guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## Start with the decision and the scope

Reuse the brief and any `invisible-stack` diagnosis. Identify the user task, permitted actions, consequential errors, sources, latency target, and intended scale. Ask only for missing information that changes the design. Apply the shared Universal Skill Protocol at the depth the task needs.

Use the full process for substantial retrieval, tools, state, or long-running work. A single-turn feature with retrieval may still need it. For a simple prompt, use `prompt-craft`; for a question about deterministic versus probabilistic behavior, use `determinism-compass`. A prototype can use a short source/budget/fallback note and mark production assumptions for later validation.

Answer five questions first:

1. **What fits and works?** Verify the chosen model’s current limits and accounting, then measure quality on representative context sizes and compositions.
2. **Which tools are needed?** Include or make discoverable the capabilities required for the task and its recovery paths.
3. **Which layer is failing?** Trace one request from source to outcome; distinguish missing facts, stale state, ambiguity, retrieval errors, and model errors.
4. **What can be compacted?** Remove repetition while retaining decisions, evidence, constraints, unresolved questions, and the means to recover detail.
5. **What happens when a layer fails?** Define the allowed action, user-visible response, recovery path, and owner.

## 1. Map the seven CONTEXT layers

The layers describe responsibilities. They are not seven equal token slices or seven mandatory services.

| Layer | Specify | Typical failure to test |
|---|---|---|
| **Constitution** | Behavioral rules, instruction authority, action permissions, enforcement points, rule owner/version | Conflicting rules; a prompt rule treated as an enforced permission |
| **Observations** | Current user/task/environment facts, identity and access scope, timestamp, freshness requirement | Wrong account, missing field, stale or misleading observation |
| **kNowledge** | Documents and precedents, provenance, retrieval method, scope, source precedence | Relevant-looking evidence that is obsolete, contradictory, or inapplicable |
| **Tracks** | Workflow state, conversation history, durable decisions, retention and resumption | Lost progress, repeated action, stale memory overriding a correction |
| **Equipment** | Tools, schemas, visibility, credentials, permitted operations, timeouts | Hidden needed tool, untrusted result, ambiguous write outcome |
| **eXecution** | Assembly order, routing, retries, verification, stopping and escalation | Unbounded loop, skipped check, unsafe fallback |
| **Template** | Output structure, citations, uncertainty and action status, validation | Fluent but unsupported answer; “done” when an action is only attempted |

For each relevant layer, record source, owner, update rule, access boundary, token/latency contribution, failure behavior, and an observable check. “System instruction” describes priority, not factual accuracy or guaranteed compliance. Enforce consequential permissions in the application or tool boundary as well as explaining them in instructions.

**Check data readiness at the scope of the rollout.** Can the feature access authoritative, sufficiently fresh information and reconcile identifiers and definitions across the systems it uses? Identify missing ownership, permissions, schemas, or quality controls. A shared repository may help; governed APIs, mappings, or federation may also meet the need. Do not require enterprise-wide data consolidation before a narrow, well-supported use case can proceed. Broader data work can run alongside delivery when the launch boundary is explicit.

## 2. Allocate a working budget

Separate the model’s supported limit, a tested operating target, and reserved capacity. Confirm how the provider counts input, output, tool definitions/results, reasoning, caching, and multimodal content. Do not count hidden reasoning as a controllable input field unless the interface actually exposes that control.

Use representative easy, difficult, long-history, contradictory-source, and tool-heavy cases. Compare task quality, omissions, latency, and cost at different budgets. Choose a provisional target if measurements are unavailable and name the test that will validate it. A budget is revisable when the model, workflow, or source mix changes.

```text
Feature / task / model and version / date:
Supported limits and accounting source:
Working input target and evidence:
Reserved output, expected tool growth, and operational headroom:

| Context representation | Token allocation | Update rule | Compaction | Failure behavior |
| System instructions and tool definitions | ... | ... | ... | ... |
| Retrieved knowledge and precedents | ... | ... | ... | ... |
| Tool results and current observations | ... | ... | ... | ... |
| Workflow and conversation history | ... | ... | ... | ... |
| Visible work notes / handoff summary | ... | ... | ... | ... |
| Total counted input | ... | | | |

Mapping to CONTEXT responsibilities:
Trigger to compact, retrieve detail, stop, or hand off:
Latency target, critical path, and retry policy:
Cost assumptions and measured usage:
```

These token categories can serve several CONTEXT layers; count each representation once. Track total work across calls as well as the current window. Offloading text into a file reduces resident context only until it is read again; retrieval and extra model calls also consume time and money.

## 3. Author missing judgment and resolve source conflicts

### Capture expert decisions through cases

When the missing context is judgment—risk tolerance, customer treatment, exceptions, or escalation—do not assume a policy document already contains it. Use realistic cases with an experienced practitioner or a moderated panel. Ask what changes the decision, which evidence matters, what alternatives were rejected, and when the expert would refer the case. Agreement can reveal a stable rule; disagreement can reveal a missing condition, legitimate discretion, or unresolved authority.

A panel is useful for comparing perspectives. A case-based individual interview is also valid. Abstract requests to “write down everything you know” often miss detail, but agents can learn from examples and observations as well as explicit rules. The practical need is to make the organization’s intended behavior available and testable.

Produce a **precedent record**: case, decision, relevant conditions, rationale summary, alternatives, source transcript or evidence, scope, authority, owner, version, and review/retirement rule. A transcript is input to this record, not automatically an approved policy. Protect confidential material and retain only what the use case needs. Leave unresolved disagreements visible for the authorized owner; do not encode the most persuasive speaker’s preference as settled policy.

### Learn from exceptions without turning one answer into a universal rule

Specify three parts of the exception-interrogation loop:

1. **Trigger:** missing required evidence, conflicting sources, an unfamiliar case, failed validation, calibrated uncertainty, or a human-detected error. Include independent sampling or audits because the system may fail to recognize its own limits.
2. **Question:** capture the relevant conditions and ask a targeted question that resolves the uncertainty. Route the whole case when a short answer cannot support a responsible decision.
3. **Provenance and validation:** link the proposed rule to the expert exchange; test its scope against known good cases, near misses, and counterexamples. Obtain the applicable policy approval before deploying the rule; version, monitor, and retire it when evidence changes.

One case can suggest a useful rule. It does not establish how far the rule generalizes. Fewer escalations count as improvement only alongside correct resolutions, detected mistakes, expert workload, and the consequences of missed exceptions. Whether experts retain judgment when their work shifts toward answering exceptions is an open question for `judgment-guard`, not a predetermined loss.

### Design the whole knowledge flow

For research retrieval, examine **creation, analysis, storage, and access** as connected activities with feedback between them. Tools can help all four. Better retrieval cannot repair missing research or make an unsupported interpretation true.

| Organizational condition | Check and response |
|---|---|
| Shared definitions | Map brands, categories, units, populations, dates, and measures; preserve meaningful differences |
| Use in decisions | Identify who needs the insight and which decision it informs; check whether it is used |
| Data ownership and access | Confirm rights to agency work, originals, metadata, and updates |
| Insights team’s role | Give the team a way to shape questions, assess evidence, and improve decisions |

Address the conditions that constrain the specific use case. Do not infer that a tool must fail everywhere because organizational reform is incomplete.

### Make disagreements visible

Specify how retrieval and synthesis handle conflicting evidence. Similarity is a relevance signal, not an authority ranking. Embeddings and contextual retrieval can help disambiguate terms; metadata, scope checks, source precedence, and explicit uncertainty may still be needed.

Record population, geography, unit, effective date, document version, and authority when these affect meaning. Prefer the applicable source under a stated precedence rule; show unresolved conflicts or seek the missing distinction. A single source or business unit can still contain outdated versions or contradictory records. Scale the checks to the actual corpus.

Novartis’s reported WatchOut feature illustrates scope warnings, such as identifying a finding limited to Europe. The source does not establish that the warning runs before generation. Warner Bros. Discovery’s marketing pilot illustrates a different issue: scene- and shot-level metadata became a useful foundation for finding reusable moments. Diagnose that missing layer when evidence supports it; do not label every disappointing pilot a metadata problem. [Evidence and limits](references/context-evidence.md)

## 4. Design compaction, tools, and handoffs

Choose a strategy for each layer:

- **Summarize** material while retaining citations, decision conditions, unresolved conflicts, and pointers to originals. Test whether omitted details change later answers.
- **Offload** recoverable detail to durable storage with identifiers, access controls, freshness, retention, and a retrieval path.
- **Trim tool output** to task-relevant fields, while preserving errors, action status, and evidence needed to verify the result.
- **Reset with a handoff** when useful for the actual model and task. Preserve completed work, current state, permissions, constraints, uncertainty, and the next step. Test resumption and duplicate-action prevention.

Do not hard-code resets after a fixed number of messages or promise percentage savings. Anthropic’s March 2026 harness report used resets for Sonnet 4.5’s context anxiety, then removed them when Opus 4.5 largely addressed that behavior and automatic compaction sufficed. Treat this as model-specific engineering evidence. [Harness report](https://www.anthropic.com/engineering/harness-design-long-running-apps)

**Tool visibility:** expose a clear, sufficient set and support discovery when the task changes. Three to five tools may suit one workflow; there is no universal limit of ten. Measure selection errors and whether filtering hides required capabilities. Log relevant visibility decisions without exposing secrets. Tool availability does not grant permission to use it.

**If a multi-agent harness is appropriate and authorized**, define each role’s context and handoff. Do not create subagents solely because a tool result is large; targeted queries or local extraction may be enough. Respect a request to work sequentially.

| Role | Context needed | Handoff |
|---|---|---|
| Planner | Goal, constraints, source evidence, relevant system facts | Scope, architecture choices, acceptance criteria, open questions |
| Generator | Agreed task, current artifacts, authorized tools, relevant standards | Changes, verification evidence, unresolved issues |
| Evaluator | Independent criteria and the artifacts needed to judge them | Findings, evidence, pass/fail where appropriate, remaining uncertainty |

Protect evaluator independence from excuses and self-reported success. Supply implementation details when code quality, security, or diagnosis requires them. Files such as `sprint-contract.json` and `build-log.txt` can support handoffs; they still need versioning, source checks, and access rules. Preserve concise decision rationale and evidence, not private chain-of-thought. File content does not acquire instruction authority merely because it is saved.

## 5. Define failure behavior and operating limits

Specify the permitted fallback for each dependency. Options include fresh authorized cache, bounded retry, reduced scope, an explicit inability to answer, or referral. A retrieval failure must not silently become an unsupported product-policy answer. A timeout on a write may mean the action succeeded: reconcile its status before retrying. A Constitution conflict requires resolution under the applicable authority, not automatic reversion to a less restrictive old rule.

Budget latency along the actual dependency path. Add serial stages; model parallel stages and joins. Individual stage P95s do not sum to the end-to-end P95. Measure queueing, retries, and load effects. For example, 0.5s retrieval + 2s tool use + 3s generation totals 5.5s, leaving 0.5s under a 6s target; whether that headroom is adequate requires measurement.

Choose logging, redaction, sampling, retention, and alerts based on consequence, diagnosis needs, privacy, and cost. Avoid blanket “log everything” or “sample 10%” rules. Preserve necessary verification and audit controls when optimizing latency.

For an illustrative request that needs all five independent services, each available 99.9% of the time, availability is `0.999^5 ≈ 99.501%`. Real systems have correlated failures, caching, optional dependencies, and recovery paths. This calculation is not a forecast that a dependency will fail every week.

## Worked examples

**Support answer with retrieval.** An illustrative input contains 800 instruction tokens + 4,000 retrieved tokens + a 200-token question = 5,000 tokens. A 500-token visible work-note allocation brings counted input to 5,500; reserve output separately under the provider’s accounting. Assumed serial durations of 0.4s retrieval + 0.8s generation + 0.1s validation total 1.3s. These are planning values, not benchmark results or a price quote. If no applicable article is found, provide an appropriate help path or explain the gap. A timeout permits a smaller result only if it already contains sufficient evidence.

**Code-analysis agent.** A provisional 70K input target might allocate 8K instructions, 20K retrieved files, 5K tool results, 15K observations, 18K conversation, and 4K visible work notes. The arithmetic totals 70K; the target needs task-specific evaluation. On a hypothetical 128K shared limit, the remaining 58K must accommodate output and future growth under the actual accounting rules. Trigger compaction before reserves are exhausted; keep findings and reproducible checks in `analysis-summary.json` and `test-results.txt`.

See the [concept guide](CONCEPT.md) for fuller support, coding, and clinical review examples.

## Review and hand off

Answer six diagnostic questions: Is the working budget evidenced? Is the largest context allocation justified? Does each critical failure have an explicit response? Can the model find needed tools? Can a reset recover the right state? Does the complete path meet latency and cost targets?

- [ ] Supported limits, working target, and reserves are distinct and checked.
- [ ] Relevant CONTEXT layers have sources, owners, update rules, and failure behavior.
- [ ] Compaction preserves consequential information; claimed savings are measured or labeled assumptions.
- [ ] Tool visibility and action permissions are explicit and recoverable when needs change.
- [ ] Dependency failures and ambiguous action outcomes have tested responses.
- [ ] Role isolation is defined where a harness is used; it does not hide evidence needed for review.
- [ ] Durable state and handoffs support resumption; diagnostics and unresolved decisions are recorded.

Deliver the recommended layer design, budget table, fallback playbook, largest unresolved risk, and next action with an owner. A small feature may need one page or an inline table. Add a diagram when it clarifies the flow; use `excalidraw-svg` if appropriate, without a fictional universal threshold line.

The trade-off is between enough relevant evidence and the cost, delay, and maintenance of supplying it. Excessive trimming can remove the decisive fact; excessive specification can delay a useful test. Change the design when representative task evidence shows a better allocation or a simpler flow.

## Connections

- `invisible-stack` diagnoses layer failures; this skill specifies their information flow.
- `prompt-craft` writes instructions; `prompt-as-product` governs tested, versioned changes to prompts and context behavior. Use an appropriate release evaluation, not an automatic A/B test for every edit.
- `determinism-compass` locates reproducibility needs; `stress-test` checks the whole system under load and failure.
- `agent-spec` and `agent-harness` define execution contracts; `failure-modes` and `judgment-guard` cover missed exceptions and human capability.
- `marketing-to-ai-agents` applies related information-design questions to agent-mediated buying. Its commercial objective is distinct; providing useful, accurate product context does not guarantee a buyer’s decision.
