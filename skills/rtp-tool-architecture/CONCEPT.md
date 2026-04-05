# tool-architecture: Reading vs Doing

## The Dual Definition

**Business lens:** Tool architecture is the API surface by which an agent interacts with your systems. Observation tools are information supply. Action tools are decisions made durable. Trust depends on controlling what actions the agent can durably make.

**Technical lens:** Tools are method calls with permission boundaries. Read tools query state (no mutation). Write tools change state (mutation with rollback). Delete tools make permanent changes. Permission boundaries are (agent_id, tool_id, resource_id, rate_limit, approval_gate). The boundary is where safety lives.

---

## The Trap: Symmetric Access

You give a user (human or agent) access to a database. They can read and write. This is fine for a human because humans have judgment. For an agent, it's dangerous because judgment is missing.

The instinct is symmetry: "If I can read users, I should be able to update users." False. Observation is safe. Mutation is costly. Permission asymmetry is required.

**Real example:** Customer support agent reads customer account history (safe). Agent writes refund to account (unsafe without approval). Same database, different permission model.

The fix: Design read access liberally, write access conservatively. One tool per read, one tool per write, never merge them. Read returns data. Write requires a decision gate.

---

## Tool Categories: From Safe to Dangerous

**1. Observation tools (safe to give widely)**
- File read
- API query (GET)
- Database select
- Log search
- Analytics query

Characteristics: Pure functions, no side effects, fully idempotent. Safe to call 1000 times. Agent can use these to think. High autonomy, no approval gates needed.

**2. Reversible write tools (medium safety)**
- Create draft (email, document, report)
- Modify dev database
- Update configuration (with rollback supported)
- Create temporary files
- Update cache entries

Characteristics: State changes, but undo is possible (usually within hours). Cost is moderate (time to rollback + opportunity cost). Needs post-audit logging. Approval gates optional if agent is confident.

**3. Audited write tools (lower safety)**
- Modify production database
- Publish to staging environment
- Send communication to user (email, SMS, notification)
- Schedule task execution
- Trigger workflow

Characteristics: State changes visible to users, rollback is costly or breaks continuity. Must be pre-approved or post-audited. Requires rate limiting.

**4. Irreversible delete tools (unsafe, needs locks)**
- Delete file
- Drop database table
- Purge user data
- Archive and delete
- Remove backup

Characteristics: No undo. Data is gone forever. Compliance and liability issues. Agent should never have autonomous access. Always requires human approval, preferably multi-level.

**5. Cascade tools (most dangerous)**
- Deploy code to production
- Migrate database schema
- Restart critical service
- Send broadcast message
- Trigger reconciliation job

Characteristics: Single action triggers many downstream actions. One bug cascades. Consequence magnitude is unpredictable. Always requires explicit approval and careful monitoring.

---

## Permission Boundaries: The Permit Matrix

For each tool, you grant (or deny) access per agent, per context.

**Dimensions:**

1. **Agent identity:** which agent is calling? (only specific agents get write access)
2. **Resource scope:** which resources can it touch? (customer A's data, not all customers)
3. **Rate limit:** how often? (1 per second, 100 per day?)
4. **Approval gate:** who approves? (none, pre-approval, post-audit?)
5. **Sandbox vs prod:** is this a safe copy or live system?
6. **Rollback window:** how long to fix mistakes? (5 min, never?)

**Example permits:**

```
PERMIT: email_write
  AGENT: support_responder
  SCOPE: single user (not broadcast)
  RATE: 1 per second, 10 per user per day
  GATE: None if confidence >90%, else ask human
  SANDBOX: User gets email; can be marked as "draft" if pre-approval needed
  ROLLBACK: User can mark as spam within 48h (recall)

PERMIT: database_write
  AGENT: personalization_agent
  SCOPE: specific columns only (preferences, settings, NOT credentials)
  RATE: 1 per user per hour
  GATE: Post-audit logging mandatory, no pre-approval
  SANDBOX: Write to dev replica for testing; prod after testing passes
  ROLLBACK: Automatic rollback on error, manual rollback within 24h

PERMIT: deploy_code
  AGENT: deployment_bot
  SCOPE: staging only (not production)
  RATE: 1 per day
  GATE: Requires human code review + human approval
  SANDBOX: Staging is mandatory; prod requires separate approval
  ROLLBACK: Rollback available for 1 week
```

Notice: each permit is specific. No "give agent full database access." Every access is bounded.

---

## Escape Hatches: Kill Switches and Gradual Rollback

For every tool, design a way to stop it:

**Circuit breaker:** Monitor tool errors in real-time. If error rate exceeds threshold, disable tool.
- Example: Email write tool fails 10 times in a row → disable for all agents → human investigates
- Configuration: error_rate > 5% for 10+ calls → trip circuit

**Rollback window:** For audited writes, user can undo within time window.
- Example: Agent modifies user settings. User discovers 2 hours later, clicks "undo change."
- Configuration: undo available for 24h, then locked

**Graceful degradation:** Rather than all-or-nothing, reduce tool access progressively.
- Example: Agent is misbehaving. Reduce from "any user" scope to "test users only" before full disable.
- Configuration: degradation levels (all → test → none)

**Kill switch:** Human can disable tool instantly across all agents.
- Example: Security discovers vulnerability in delete tool → hit kill switch → tool unavailable → fix in progress

**Audit review:** Regular (weekly, monthly) review of tool usage by humans.
- Example: Detect agent is using write tool 100x more than historical average → investigate → maybe it's normal (feature change) or maybe it's broken

---

## Sandbox vs Production: Copy Semantics

**Observation tools:** No sandbox needed. Reading is safe. Read prod directly.

**Write tools:** Sandbox is essential. Design like this:

1. **Development:** Agent can write to dev database freely (it's a sandbox)
2. **Testing:** Agent reads prod data, writes to test database, human verifies output
3. **Staging:** Agent can write to staging (copy of prod structure) with approval
4. **Production:** Agent can write to prod only after stages 1-3 pass

This way, agent proves it works before touching production.

**Dangerous pattern:** Agent writes to prod directly. Testing is after deployment. Consequence magnitude is uncontrolled.

---

## Audit Trails: Decision + Action

Logging "the action happened" is insufficient. Log the decision:

```json
{
  "timestamp": "2026-03-26T14:32:00Z",
  "agent_id": "personalization_agent",
  "tool": "email_write",
  "action": "send_email",
  "target_user": "user123",
  "decision_confidence": 0.87,
  "approval_gate": "pre_approval_not_required",
  "alternatives_considered": ["resend_existing_email", "wait_for_user_action", "send_different_email"],
  "reasoning": "User has not engaged with onboarding in 7 days, conversion rate 0.15. Email reminder increases conversion to 0.35. Net benefit: $12",
  "outcome": "email_sent",
  "user_response": "opened_after_4h",
  "impact": "user_completed_onboarding"
}
```

This log tells the story: why the agent decided to act, how confident it was, what happened, what the result was. Invaluable for audits and debugging.

---

## Tool Escalation Protocol

Don't grant all tools at once. Escalate tools as agent proves reliability:

**Phase 1 (Observation only):**
- Agent reads data from all systems
- Agent cannot modify anything
- Goal: verify agent can read without errors, can understand data

**Phase 2 (Safe writes):**
- Agent can write to dev/test systems
- Agent can write reversible changes (drafts, configs with rollback)
- Goal: verify agent can make decisions without breaking things

**Phase 3 (Audited prod writes):**
- Agent can modify prod databases with post-audit
- Agent can send communications (email, notification) with logging
- Goal: verify agent makes good decisions and acts predictably

**Phase 4 (High-confidence autonomous writes):**
- Agent gets pre-approval-free access to medium-blast tools
- Error rate must be <1% for phase 3 before phase 4
- Goal: maximize latency improvement while maintaining safety

**Never phase:** Cascade and delete tools. Humans always approve.

---

## Real-World Pitfalls

**AWS Lambda permission explosion:** Service starts with s3:GetObject. Over time: s3:PutObject, s3:DeleteObject, sqs:SendMessage, dynamodb:UpdateItem, iam:PassRole. Now it has broad powers and no one knows when it happened (gradual privilege escalation).

**Database agent testing:** Agent tested on production tables (no sandbox). Works fine. Deployed to staging. Staging has different data distribution (sparse vs dense). Agent does something that was harmless on dense data, catastrophic on sparse.

**Email tool rate limit gap:** Agent can send 100 emails/hour (legitimate). User doesn't expect this. Suddenly customer service ticket goes from 1 email to 100 emails. User thinks it's a bug, actually it's the rate limit being hit.

**Audit trail too sparse:** Agent modifies user account, log says "account modified". Months later, dispute. What changed? Why? Was it the agent or a human admin? Logs don't say. Unresolved.

**Delete tool surprise escalation:** Agent given "delete temp files" access. Over time, temp file definitions expand. Agent deletes production config thinking it's temp. System crashes.

---

## Decision Checkpoints

**When designing tool access:**
1. Is this a read or write tool? (Asymmetric permissions)
2. What's the consequence magnitude if it goes wrong? (Scope matters)
3. Can we undo it? (Reversibility determines gates)
4. How fast does it need to be? (Approval adds latency)
5. Is there a sandbox to test in first? (Prod always risky)

**When escalating tool access:**
1. Did the agent use phase N correctly? (No errors, no surprises?)
2. Is the audit log clean? (Decisions documented?)
3. What's the error rate? (<1% to escalate)
4. Can we undo phase N decisions? (Rollback available?)
5. Is there an escape hatch to revert? (Kill switch ready?)

Get these right, tool architecture becomes invisible. Get them wrong, a single tool becomes a liability.
