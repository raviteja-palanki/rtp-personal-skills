---
name: agent-spec
version: v1.1.1_latest
description: "Design an agent's operating contract: the decisions and actions at each step, its permissions, evidence needed to proceed, human handoffs, failure recovery, and accountable owner. Use when building or reviewing an agent, expanding its tools or scope, placing checkpoints, or diagnosing failures across steps. Covers tool contracts, error boundaries, state snapshots, a boundary matrix, sprint acceptance criteria, durable file handoffs, verified feature tracking, and session recovery. Explain reliability assumptions before multiplying step accuracies; confidence never grants permission. Scale the document to the task, including prototypes or single actions with consequential effects. Pairs with autonomy-spectrum for operating mode, agent-risk for consequence screening, tool-architecture for tool boundaries, and ai-prd for the surrounding product requirements. Triggers: 'agent spec', 'agent autonomy', 'agent handoff', 'agent recovery', 'sprint contract'."
imports: [trust-ladder, failure-modes, determinism-compass]
---

# Agent Specification

Make the agent's permitted behavior, stopping conditions, and recovery understandable before implementation. The output is a working contract that another person can use to build, review, operate, and resume the agent.

Start with the user, problem, intended outcome, and authorized scope. Use information already provided. Clarify missing details when they affect a consequential decision; label unresolved assumptions instead of inventing an owner, confidence score, deadline, or permission.

For a new agent, follow the eight design steps below. For a review or incident, start with the affected rows of the boundary matrix and trace their dependencies. A small prototype may need only a short contract. Single actions, deterministic workflows, and high-consequence systems can still need explicit permissions and recovery; they do not automatically need this entire document.

## First define the decision and who may make it

Autonomy is difficult to specify when “handle the request” hides several different decisions. Establish four things before granting a step authority:

1. **A specific call.** State the decision or action in one sentence, including its outcome and limits. Separate “find available meeting times” from “send invitations.”
2. **Shared understanding of rights.** Involve the people who will operate or be affected by the workflow where their participation is needed. Resolve competing expectations about what the agent may do. Existing valid authorization remains valid; a workshop or unanimous agreement is not required for every action.
3. **Observable roles.** Identify who supplies input, evaluates the options, makes the final call, carries it out, and communicates the outcome. “Owner” alone is insufficient.
4. **Expertise and legitimate authority.** Put decisions close to relevant information while respecting actual organizational, user, and legal authority. Better context does not itself authorize an agent or a person to act.

These practices adapt Greer, Jordan, and Sytch's decision-rights guidance. Goals and roles may need to be refined together. Unclear goals are one source of ownership disputes, not the only one; hierarchy is sometimes the appropriate source of authority. See [evidence and interpretation](references/spec-evidence.md).

For a trivial, reversible action with one clear owner, a sentence may establish all four. For a contested decision, test whether people can describe how they would behave in a concrete disagreement. A signed or edited document is evidence of participation, not proof that the rights work in practice.

## Working vocabulary

- **Agent spec:** the operating contract for decisions, actions, state, permissions, and recovery.
- **Permission mode:** what the agent may actually do at a step. Use the explicit modes below; keep any library autonomy label separate.
- **Evidence threshold:** the validated condition needed to proceed, such as a required source, passing check, or calibrated score for a defined event. It can restrict existing permissions; it cannot create new ones.
- **Handoff:** the information and status another step or person needs to continue safely.
- **Error boundary:** a mechanism that contains a failure and determines which dependent work must stop or change.
- **Boundary matrix:** a compact record of each step's authority, evidence, failure behavior, exposure, and recovery.
- **Sprint contract:** a bounded deliverable, acceptance criteria, iteration budget, and stopping conditions.
- **Accountable owner:** the person or organizational role responsible for the outcome, equipped with the authority, information, capacity, and incentives to act.

An agent may take one action or many. A long workflow is not necessarily an agent. Errors can propagate across steps, but additional retrieval or verification can also improve a result. Evaluate the full workflow rather than assuming that every step reduces certainty. The [concept guide](CONCEPT.md) explains the reliability math and failure patterns.

## Eight design steps

### 1. Map operations and dependencies

For each operation, name its input, decision or action, state read or changed, output, and next destination. Include retries, loops, parallel branches where applicable, termination conditions, and external effects. The graph need not be acyclic.

Mark where the agent reads untrusted material, crosses a permission boundary, or commits an effect that cannot reliably be undone. These are candidates for checks before the effect occurs.

### 2. Specify the permission mode at each step

| Mode | What it permits | What the spec must establish |
|---|---|---|
| Suggest | Produce a recommendation for a person to decide on | Whether any preparatory reads are authorized; no implied authority to execute the recommendation |
| Prepare for approval | Create a draft or proposed action and wait at the defined commitment boundary | Who approves, exactly what approval covers, and what material changes invalidate it |
| Execute within bounds | Act under existing authorization and report or monitor as specified | Allowed actions, resources, recipients, duration, aggregate limits, evidence requirements, and intervention route |
| Pause or refer | Stop affected work or transfer it to an authorized person/process | Trigger, preserved state, recipient, response expectations, and safe behavior while waiting |

Use `rtp-autonomy-spectrum` for the library's broader operating labels and `rtp-ai-use-case-readiness` for use-case suitability. Do not reuse the old 0–4 numbering from this skill: it conflicted with the shared library scale. Permission mode and topology are different choices; several cooperating agents do not inherently receive more authority.

Honor permissions already granted within their scope. Reversible work does not always require another approval; irreversible work requires an appropriate authorization boundary, not a promise of an imaginary undo button.

### 3. Define evidence required to proceed

Name the event a score estimates, the population on which it was checked, the acceptable error types, and the consequence of being wrong. Use `rtp-confidence-tuner` when scores need calibration.

For each step specify:

- Required facts, checks, and freshness; a numerical threshold only where it has a defensible basis.
- Behavior when evidence is missing, contradictory, stale, or outside the evaluated domain.
- The fallback on refusal or tool failure, including when to pause.
- What detects calibration failure and who can restrict the operating mode.

A high self-reported confidence score is not a substitute for evidence. If no useful calibrated score exists, use observable requirements and label uncertainty. Do not force a percentage to fill the matrix.

### 4. Design the handoff

Pass the current request and relevant user updates, constraints, decision summary, supporting evidence, source provenance, unresolved issues, permission scope, step status, and references to necessary artifacts. Specify what is omitted and why.

Preserve critical constraints even when compressing the context. A concise rationale and evidence are sufficient; do not require private internal reasoning traces. Distinguish instructions from quoted source material or tool output. A state file records a decision; it does not outrank the user's instructions or establish that its contents are true.

For refusal, partial completion, conflict, and failure, say what the receiver may use and which work is blocked. A downstream step must not silently convert an unverified result into a verified fact.

### 5. Specify recovery and error boundaries

For each failure, define the affected dependencies, containment action, recovery method, expected effort, notification, and user experience. A noncritical branch may continue if it is independent and its reduced result remains useful and authorized. “Medium severity” alone does not justify proceeding with unreliable context.

Separate these outcomes:

- **Rollback:** restore a state that the system can actually restore.
- **Compensation:** take a new action to address an effect that already occurred.
- **Quarantine or marking:** prevent further use or label a result as unverified; this does not undo earlier effects.
- **Reconciliation:** determine whether an external action succeeded before retrying after a timeout or uncertain response.

Bound retries by time, cost, scope, and evidence of progress. Use idempotency or duplicate detection where supported. A stopped agent may still have an in-flight external action; document cancellation limits. Sending an apology is compensation, not recall of an email.

### 6. Define useful, proportionate state snapshots

Record the step/version, timestamp, relevant actor or request identifier, input reference, decision summary, evidence and uncertainty, output or external effect, authorization used, and intervention or feedback. Specify sampling, access, redaction, retention, and deletion requirements.

Keep enough information to reconstruct relevant events without indiscriminately storing raw sensitive inputs. A snapshot supports investigation; it does not reveal an exact internal cause merely because it contains an explanation generated by the model.

### 7. Complete the boundary matrix

| Step and operation | Permission and limits | Required evidence | Handoff/state | Failure and affected scope | Containment/recovery | Cost and owner |
|---|---|---|---|---|---|---|
| [specific operation] | [mode; resources/actions] | [checks; justified threshold if any] | [artifact/status/constraints] | [failure; downstream and external exposure] | [stop/degrade/rollback/compensate/reconcile] | [time, effort, user friction; responsible role] |

Describe consequence magnitude separately from the number of downstream steps. A single payment can matter more than many internal transformations. More users increase exposure and potential aggregate harm; they do not necessarily change the severity of each incident.

### 8. Equip the accountable owner

Name the existing responsible person or role, their decision and intervention rights, backup coverage, and how unresolved issues reach them. If assignment is pending, record that gap and the affected launch or operating restriction. Do not invent a person to complete the template.

Use the three-M lens to make ownership workable:

- **Mindset:** the owner understands where their judgment and intervention matter.
- **Meaning:** they understand the customer or business outcome that makes the work worth checking.
- **Mechanisms:** they have time, access, training, escalation routes, and incentives for sound decisions, justified approvals, error detection, and learning.

Rewarding only errors caught can encourage excessive rejection. Compliance and formal controls can support ownership; they are not automatically empty ceremony. Even a low-consequence autonomous step has an appropriate product or process owner, although no person may need to review each action.

A framing experiment with 1,261 managers found meaningful oversight effects concentrated among respondents whose organizations already placed AI agents on organizational charts. It does not establish that all “AI colleague” language removes accountability or that an owner field is worthless. See the source limits in [spec evidence](references/spec-evidence.md).

## Tool contracts and component boundaries

For each tool, document its input and output schema, side effects, caller identity and permissions, resources, freshness, latency and availability expectations, cost model, and error states. Include partial or empty results, pagination where relevant, timeout/cancellation behavior, and retry or reconciliation rules.

This is a human-readable operating contract. It is **not an MCP wire-format example**. When using MCP, validate the actual tool schema against the deployed protocol version. Latency, cost, and recovery policies need explicit operating documentation even when they are not protocol fields. Use `rtp-tool-architecture` for the full interface and enforcement design.

```text
Tool: search [illustrative operating contract]
Inputs: query, bounded result count, permitted filters
Outputs: results with source, retrieval time, and available publication dates
Authority: read only within permitted collections; no external writes
Freshness: define by the question being answered
Latency/availability/cost: measured baseline, target, and billing unit
Empty results: report the search limit and choose an authorized next step
Timeout: bounded retry or report unavailable; no fabricated result
Cached fallback: use only if age and coverage fit the task; label it
Current facts unavailable: pause the dependent claim or disclose the gap
Result score: define what it measures; do not equate relevance with truth
```

A retrieval failure must not become an authoritative plan based on stale or generic knowledge when current facts are required. Place the boundary before the dependent commitment, and test it with representative failures.

## Sprint contract: agree on completion before iterating

Use this pattern when an agent builds or executes a bounded deliverable. The generator produces the work; the evaluator may be a person, test suite, or suitable review process. These are roles, not a requirement to create multiple agents.

1. **Implementation:** specify the deliverable and constraints. For a scheduling tool, define attendees, timezone, working hours, slot length, result count, and whether sending invitations is authorized.
2. **Acceptance:** describe observable success and required evidence. Automated tests help where appropriate; human judgment can use an explicit rubric. “All tests pass” is insufficient if the tests omit the intended behavior.
3. **Iteration limit:** set a task-appropriate budget if needed. A small fixed number can bound an experiment, but three to five attempts is not a universal limit. Honor the user's existing scope and budget.
4. **Stop or change conditions:** identify harm, authorization failure, lack of progress, missing resources, or infeasible requirements. State the escalation or alternative action.

```text
Sprint contract: [task]
Generator / evaluator: [roles]
Deliverable and constraints: [...]
Acceptance criteria and evidence: [...]
Iteration or resource budget: [agreed limit, if applicable]
Stop/change conditions and next action: [...]
Deadline or review point: [agreed value, if applicable]
Scope changes: [how user updates and accepted revisions are recorded]
```

Once the agreed work passes appropriate checks, finish. If criteria change for a valid reason, record the change and its authority instead of silently moving the target. Do not reinterpret an unmet requirement as optional merely to declare completion.

## Durable state for long tasks

Files can help work survive handoffs and context resets. Use them when their persistence and audit value justify the overhead. Reading a file still consumes context; files save repeated work only when readers select useful summaries and references. They do not guarantee correct state or lower cost.

| File, under a task folder such as `work/agent-state/` | Purpose |
|---|---|
| `problem.md` | Original request plus separately recorded subsequent user steering and scope decisions |
| `analysis.md` | Findings, evidence, assumptions, corrections, and open questions |
| `state.json` | Canonical operational state, version, completion status, and references |
| `plan.md` | Current plan and material decision rationale |
| `execution-log.md` | Actions, results, errors, and external-effect status |
| `handoff.md` | Entry point: what is complete, what remains, constraints, and next action |

For example, analysis reads the problem and records findings; planning reads relevant findings and updates the plan/state; execution reads the current plan and logs results. One agent can perform all these roles sequentially.

Keep provenance for corrections and scope changes; do not make stale conclusions immutable. Retain history according to sensitivity and retention needs. Treat `state.json` as the source of record for operational state, not unquestionable truth. Resolve conflicts against authoritative evidence and current instructions, then update it explicitly. Use atomic writes and suitable version/concurrency controls where multiple writers exist.

## Feature tracking: evidence before “done”

For a multi-part deliverable, track each required behavior and its verification. Keep the list proportional to the task.

```json
{
  "features": [
    {"id": "auth-login", "description": "Authorized users can sign in", "passes": false, "verified_by": null, "test_result": null},
    {"id": "session-refresh", "description": "Refresh follows the agreed session policy", "passes": false, "verified_by": null, "test_result": null},
    {"id": "logout", "description": "Logout invalidates the intended session", "passes": false, "verified_by": null, "test_result": null}
  ]
}
```

Set `passes` to true only with relevant evidence. Preserve required features unless an authorized scope change replaces or removes them; record that change rather than hiding unfinished work. Add explicit blocked, superseded, or waived status when useful. A waiver is not a passing test. Report partial work accurately and continue authorized work that remains feasible.

## Resume a session from verified state

At startup or after a context reset, check what matters for this task:

1. **Location:** confirm the project/task directory and expected files.
2. **Progress:** read the handoff, current request updates, completed work, and blockers.
3. **Repository state, if applicable:** inspect relevant recent changes and uncommitted work; preserve concurrent user changes.
4. **Feature status:** identify unverified or failing requirements and avoid redoing completed work without reason.
5. **Runtime, if needed:** check the required service; start one only when needed and authorized. Do not disrupt an existing service merely to satisfy this checklist.
6. **Health check, if meaningful:** run a small representative check to establish the baseline; record failures before attributing them to new work.

Summarize the current state and next action in the handoff or, when useful, a `session-init.md` in the task folder. A report can contain timestamp, location, last completed item, blockers, repository changes, feature status, runtime status, health-check result, and next steps. Noncoding tasks need no development server, build artifacts, or ritual ten-minute initialization.

## Keep the contract current

Review after a material model/configuration change, a new or changed tool, a meaningful shift in corrections or failure patterns, or an expansion in users, domain, permissions, or consequence. Changes can improve or worsen performance; a flat correction rate alone does not prove regression. Check task mix, labels, and user expectations.

Set periodic review cadence by risk and change rate. Compare observed outcomes with the assumptions behind permissions, thresholds, recovery capacity, and ownership. Retest affected paths and relevant regressions; do not blindly retain or downgrade every permission after each update.

## Review and handoff

Before treating the spec as ready, check:

- Operations and dependencies are concrete, including external effects and termination.
- Each step's actual permission and rationale are clear and enforceable.
- Evidence requirements have a basis; missing evidence and miscalibration have defined behavior.
- Handoffs preserve constraints, provenance, permission scope, and incomplete status.
- Recovery distinguishes rollback, compensation, quarantine, and reconciliation, with owners and user experience.
- Snapshots support investigation with appropriate access, sampling, and retention.
- The boundary matrix has been exercised against realistic failure scenarios and reviewed by someone able to challenge its assumptions; independent review is especially useful for consequential systems.

Deliver the spec and matrix, the recommendation, key trade-off, largest unresolved risk, owner, and next action. State what was reviewed versus tested. Link the surrounding `rtp-ai-prd`, `rtp-agent-risk`, `rtp-failure-modes`, and `rtp-production-observability` work where relevant. A small step graph can help when it clarifies boundaries; it is optional, and no particular drawing tool is required.
