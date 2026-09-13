# Tool Architecture: Reading, Changing, and Establishing What Happened

**Business lens:** a tool exposes access to information or an operation that can affect people and systems. Define the useful scope, who may authorize it, and how the result will be checked.

**Technical lens:** enforce the actor, delegation, operation, resource, environment, limits, state preconditions, and approval policy. Human users also need these boundaries; good judgment is not a substitute for least privilege.

## Avoid symmetric access without making reads unrestricted

Permission to inspect an account does not imply permission to refund it. Neither action is intrinsically safe or unsafe: account history can be private, and a routine refund can be explicitly authorized. Split permissions where consequences differ. A broad query tool can still be safe if the server correctly constrains it; a narrowly named tool can still leak data if its implementation does not.

File reads, API queries, database SELECTs, log searches, and analytics are not necessarily pure or cost-free. Results can change between calls, queries can consume resources, and information can be disclosed. A thousand repeated reads need not be harmless.

Drafts, development writes, configuration changes, temporary files, and cache updates may be recoverable. Production writes, messages, scheduling, deletion, and cascading jobs need effect-specific controls. Staging can still contain real data and credentials; an environment's name is not an isolation guarantee.

## Three illustrative permits

These examples describe authorization contracts; their numbers are not default limits.

### Send a support response

- Actor: support responder acting under the user's or organization's valid delegation.
- Operation: `send_email`, separate from draft creation.
- Scope: the authorized support case and recipient; no broadcast or unrelated destination.
- Limits: case-specific message count, content policy, and any applicable rate limit.
- Gate: the actual standing permission or required approval, bound to the material recipient and content.
- Result: operation ID and provider acceptance/delivery state as available.
- Recovery: status reconciliation and duplicate prevention; cancellation only if the provider still supports it.

Marking an email as spam within 48 hours is **not recall**. Provider acceptance is not proof of recipient receipt, reading, or agreement. A self-reported confidence score above 90% does not grant permission to send.

### Update a preference

- Actor: personalization service with a narrowly scoped workload identity or delegation.
- Scope: authorized preference fields for the intended user; exclude credentials and unrelated records.
- Precondition: expected resource version, validated value, and applicable user preference/consent.
- Duplicate/concurrency behavior: idempotent operation identity and a conditional update where appropriate.
- Recovery: restore only when safe against later legitimate changes; otherwise reconcile the conflict.
- Records: relevant old/new state or protected references, with suitable access and retention.

A “24-hour rollback window” is only real if the implementation preserves what is needed and avoids overwriting intervening work. Passing development tests does not itself expand production authority.

### Deploy an approved change

- Actor: deployment service scoped to the actual target environment.
- Scope: reviewed artifact and configuration; staging rights do not imply production rights.
- Gate: the applicable approval and release policy, which may include standing automation.
- Recovery: tested rollback or forward repair, including data and downstream effects.
- Stop: restrict further deployment, assess in-flight work, and reconcile the current version.

One deployment per day, mandatory manual review, and a one-week rollback window were source examples, not universal requirements. Automated deployment can be appropriate under an authorized tested contract.

## Record evidence without inventing causality

An illustrative audit record can include:

```json
{
  "operation_id": "case-771-response-1",
  "actor_id": "support_responder",
  "tool": "send_email",
  "tool_version": "1",
  "target_reference": "case-771-authorized-recipient",
  "authorization_reference": "case-771-response-policy",
  "policy_result": "allowed",
  "execution_status": "provider_accepted",
  "evidence_reference": "provider-event-123",
  "delivery_status": "pending",
  "reconciliation_required": false
}
```

This is an example shape, not a production schema or proof that an event occurred. Production records need appropriate timestamps, integrity, access controls, and retention. Reconciliation status must change if uncertainty arises.

The original log asserted that a reminder raised conversion from 0.15 to 0.35 and generated $12 of benefit. Those are unsupported causal claims unless a valid analysis establishes them. Later onboarding or an email-open signal alone does not prove that benefit. Keep observed events, model estimates, and evaluated business impact separate.

## Test and respond in proportion to the work

Simulation, shadow operation, sandbox/staging tests, and bounded production rollout are possible stages. Use authorized representative data or suitable synthetic/sanitized substitutes. Reading production data during a “test” can itself be consequential. No fixed sequence proves production safety, and a clean log or <1% average error rate does not justify every permission expansion.

Circuit-breaker examples such as ten consecutive errors or 5% over at least ten calls need a useful denominator, time window, dependency scope, and reset rule. The signals may identify very different problems. An undo control cannot reverse an effect the system never made reversible.

## Preserved pitfalls, treated as illustrations

- **Permission growth:** a service expands from S3 reads to writes, deletes, queues, database updates, and role delegation. Each added permission deserves a justified scope; the named AWS sequence is illustrative, not a verified incident.
- **Environment mismatch:** sparse staging data and dense production data can reveal different behavior. Test relevant conditions without using unrestricted production mutation as the first experiment.
- **Messaging excess:** 100 emails per hour being technically allowed does not make sending that many relevant or authorized. A rate limit is an upper bound, not a target.
- **Sparse audit:** “account modified” omits actor, operation, authority, and state needed for investigation.
- **Temporary-file drift:** expanding what counts as temporary can expose production configuration to deletion. Validate resource boundaries rather than trusting a loose name.

Use the [main skill](SKILL.md) to translate these questions into the tool contract and its enforcement.
