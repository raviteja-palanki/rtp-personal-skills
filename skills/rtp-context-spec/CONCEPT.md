# Context Spec — Concept Guide

The context spec explains how a product gives a model the information it needs and manages that information over time. Ravi’s CONTEXT framework names seven responsibilities: Constitution, Observations, kNowledge, Tracks, Equipment, eXecution, and Template. They help a team distinguish problems that otherwise all look like “the model gave a bad answer.”

There is no measured 90/10 split between these responsibilities and the model. Their relative importance depends on the feature. A citation instruction cannot supply a missing source; an excellent retriever cannot enforce a tool permission; a valid output schema cannot establish that an answer is true. Diagnose the actual dependency.

## From demo to a repeatable information flow

In a demo, someone may hand-pick current documents and provide the right account context. In production, those steps need owners, freshness rules, access boundaries, and recovery paths. Otherwise a model change can leave the underlying problem untouched.

A useful specification connects a business requirement to an observable implementation behavior. “Answer account questions appropriately” becomes “load the authenticated account’s allowed fields; if identity cannot be established, answer only general questions.” The spec should make consequential decisions clear while leaving ordinary implementation choices to the team. It cannot eliminate every future clarification.

The Constitution layer includes behavioral guidance and enforcement responsibilities. It is not identical to Anthropic’s Constitutional AI training method. A prompt or output filter alone is not a guarantee of compliance. Similarly, separate CONTEXT responsibilities need not become separate microservices.

## Example 1: Support assistant

This fictional design supports product questions and creates a ticket within the user’s authorized workflow. Its numbers illustrate budgeting, not production performance.

| Layer | Example design |
|---|---|
| Constitution | Protect credentials and other users’ data. Apply the organization’s policy for showing a user their own account information. Enforce access before retrieval and tool execution; use output checks as another layer. Require applicable evidence for product-policy claims. |
| Observations | Load verified account type and support entitlement. If the session is unavailable, use the anonymous support path; do not infer account facts. |
| kNowledge | Retrieve from product documentation and approved resolutions. Keep source version and effective date. Set freshness by topic: a daily refresh may suit general documentation but miss an urgent policy change. |
| Tracks | Store the state of the request and authorized actions durably. Choose retention and resumption periods for the service and privacy requirements; a one-hour session is one possible design. |
| Equipment | Create a support ticket when the request or established workflow authorizes it. After a timeout, check the operation identifier before retrying; show a support link when recovery is unavailable. |
| eXecution | Load account context, retrieve evidence, generate, check access/grounding/output, and return the result. Some independent reads may run together. |
| Template | Provide the answer, applicable citations, useful next action, and accurate ticket status. Check that citations support the claims, not merely that their URLs are valid. |

**Verification:** test cross-account leakage, missing identity, obsolete documents, contradictory policies, unsupported claims, lost state, and duplicate ticket creation. Passing 100 adversarial examples does not prove all leakage is prevented. A citation rate alone does not establish support or correctness. If retrieval fails, use an approved fresh cache, explain the limitation, or offer a support route; do not improvise current product policy from model memory.

**Latency:** assumed serial allocations of 50ms session loading + 500ms retrieval + 50ms initial checks + 3,000ms generation + 200ms output checks + 50ms formatting total **3.85 seconds**. These are allocated durations. Measure the actual end-to-end percentile under expected traffic and failure conditions; a five-second target needs user and operational justification.

**Cost:** count input, output, retrieval, storage, tools, review, and operations separately using current contracted rates. If, purely for illustration, the complete measured cost were $0.0001 per request, 1,000 users making 100 requests each per day would generate 100,000 requests, costing $10 per day or $300 over 30 days. A token count alone does not establish that price. Compare full cost with a measured service outcome and the fallback baseline.

**Monitoring:** collect the minimum evidence needed to diagnose failures, with access controls and retention. Track correctness and resolution alongside latency, retrieval failures, tickets, and user feedback. Select alert thresholds from service requirements and baseline variation rather than copying the example.

## Example 2: Code-generation assistant

The assistant needs current file context, applicable coding standards, relevant dependencies, and the user’s requested change. Use stated preferences and visible task requirements to set explanation depth; avoid speculative profiling of expertise.

Specify access to the working tree and what may be edited or executed. Preserve current changes and distinguish draft code, tested code, accepted code, and deployed code. Acceptance does not prove deployment or safety.

Tools may include formatting, compilation, behavioral tests, dependency checks, and security analysis. Syntax checks do not detect every insecure design; neither a low sampling temperature nor a scanner guarantees safe code. Match verification to the change and its consequences.

An illustrative serial path is 2s context loading + 1s retrieval + 2s generation + 1s syntax/style checks + 2s security analysis + 0.5s formatting = **8.5 seconds**. Decide whether this meets the user experience and service target. If scanning runs asynchronously, show that it is pending and retain any required release gate. Cache a scan only when the relevant code, dependencies, rules, and tool version match the result’s validity conditions.

Record changes and verification outcomes with appropriate protection for source code and secrets. Escalate consequential findings based on actual exposure; do not interpret every accepted suggestion as a shipped vulnerability.

## Example 3: Clinical review assistance

This is an architecture illustration for a system whose clinical purpose and governance have already been defined by qualified owners. The label “findings for review” does not by itself establish a regulatory category or remove clinical risk.

- **Constitution:** define permitted clinical use, required review, action restrictions, and responsibility for urgent or ambiguous findings.
- **Observations:** verify patient identity, relevant history, imaging context, and data completeness; minimize access to sensitive information.
- **kNowledge:** use validated, applicable sources and record their provenance. Similar cases support review but do not establish a diagnosis.
- **Tracks:** preserve case versions, prior studies, reviewer decisions, disagreements, and the basis for follow-up under the approved retention policy.
- **Equipment:** define imaging tools, review routing, and notifications with explicit permissions and failure handling. Escalation does not automatically authorize a patient notification.
- **eXecution:** validate input, produce findings, check for missing or conflicting evidence, and route through the required clinical review before downstream actions.
- **Template:** distinguish findings, uncertainty, supporting evidence, and action/review status.

Choose sensitivity, specificity, calibration, and subgroup measures for the clinical task and error consequences. Overall accuracy is not sensitivity. A universal 80% confidence threshold cannot determine safe referral, and specialist agreement is valuable evidence rather than infallible ground truth. Investigate overrides with case review and outcome evidence; a fixed override rate should not automatically trigger retraining or deployment.

Illustrative processing costs of $0.01 + $0.10 + $0.01 per image total $0.12; five images cost **$0.60**, before review, integration, monitoring, and other costs. This arithmetic establishes neither clinical benefit nor value for money. Any benefit claim needs appropriate clinical evidence.

## Budget the complete path

A serial path of 0.5s retrieval + 0.1s checks + 3s generation + 0.2s filtering totals **3.8 seconds**. Adding 0.05s session loading, 0.1s history loading, and 0.2s recommendations produces **4.15 seconds**, not 4.5. If the whole path doubled, it would take 8.3 seconds; a tenfold traffic increase does not necessarily double latency.

Allocate from the end-to-end target according to dependencies and user needs. Equal slices across seven conceptual layers rarely make sense. Measure queues, retries, parallel joins, cold starts, and degraded modes. Redesign or revise the service promise when the target is infeasible; do not remove essential logging or controls merely to fit it.

For cost, $0.01 per request × 10 daily requests × 10,000 users is $1,000 daily, or $30,000 over 30 days. Verify that “per request” includes the full processing path and account for attempts that fail or require review.

## Reading and lineage

Ravi’s CONTEXT framework supplies the organizing model. Reliability engineering contributes dependency budgets, observability, and recovery design; it does not imply that every layer needs a service or an equal latency allowance. The [evidence notes](references/context-evidence.md) distinguish practitioner guidance, company cases, and proposed design rules. Use the [main skill](SKILL.md) for the working process.
