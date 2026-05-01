---
name: rtp-agent-spec
description: "Agent spec: autonomy levels (0-4), confidence thresholds, handoff, recovery, state snapshots. Maps uncertainty cascade (90% × 5 steps = 59% end-to-end). Use when: multi-step agents, autonomy levels, checkpoints. Triggers: 'agent autonomy', 'agent spec'"
imports: [trust-ladder, failure-modes, determinism-compass]
---

# Agent Specification

## DEPTH DECISION

**Go deep if:** Designing a multi-step agent with human checkpoints, assigning autonomy levels per step, or scaling an agent to new domains.

**Skim to Process if:** Reviewing an existing agent spec or debugging agent failures — you need the boundary matrix, not the full design.

**Skip if:** Single-turn Q&A, fully deterministic workflows, prototype experiments, or when consequence magnitude is so high autonomy 3-4 are impossible.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## Living Document Concept

Agent specs are **living documents**, not one-time designs. Agent capabilities evolve (model upgrades, new tools, better retrieval), and the spec must evolve with them.

**Revision triggers (update the spec):**
- Major model upgrade: Re-test all autonomy levels and confidence thresholds. Higher capability = potential jailbreaks. Recalibrate.
- New tool added: Rerun failure analysis. Does this tool unlock new failure modes?
- Correction pattern changes: If correction rate stops decaying, step quality has regressed. Investigate and update recovery paths.
- Consequence magnitude increases: Feature goes from 10 users to 1,000. Autonomy levels may need downgrade (Level 3→2).

**Never "set and forget."** Schedule quarterly spec reviews. Compare actual outcomes (correction rate, error rate, churn) against spec assumptions. Update if misaligned.

---

## Tool Specification (MCP Format)

For each tool the agent accesses, specify in MCP format:

```
Tool: search
  Input schema: { query: string, max_results: int, filters?: [string] }
  Output schema: [{ title: string, body: string, confidence: 0-1 }]
  Latency: <500ms p95
  Availability: 99.9% uptime (if fails, agent uses fallback knowledge)
  Cost: 2 tokens per search
  Failure modes:
    - Timeout (>1s): Return cached results or "unable to search"
    - Empty results: Agent should suggest alternatives, not hallucinate
    - Stale index: Knowledge cutoff April 2025; searches for recent events fail
  Trust signal: Confidence score 0-1 (0.9+ is trusted, <0.6 suggest human review)
```

**Why MCP format:** Explicit contracts prevent "the tool is down, what happens?" surprises. Document it upfront.

---

## Error Boundaries Between Components

Agents are networks of tools and steps. When one component fails, what's the consequence magnitude?

Define error boundaries:

```
Step 1 (Retrieve context) ──[boundary]──> Step 2 (Generate plan)
  If Step 1 fails:
    - Does Step 2 have fallback context? (Generic knowledge, cached data)
    - Can Step 2 proceed with uncertainty? (Lower autonomy, require human review)
    - Does Step 1 failure cascade to Step 3+? (No, boundary blocks it)
```

**Boundary rules:**
- If error severity ≤ Medium: Proceed with degraded context, lower autonomy
- If error severity = High+: Stop, route to human, don't cascade

## THE TRAP

You will conflate "the AI does multiple steps" with "an agent." The bias is **autonomy creep** — you'll design a feature where the AI takes one action, then reframe it as "step 1 of a 3-step agent" to justify shipping without human checkpoints.

Real agents have a critical property: they make autonomous decisions that cascade downstream. Each step reduces certainty. The trap is designing as if each step operates in isolation, then watching the system fail when early mistakes compound.

The dangerous variant: designing agents that have no recovery path. The AI commits to a direction at step 1, and step 5 is locked. A single hallucination at step 2 corrupts the entire output.

## THE PROCESS

1. **Map the step graph.** List every discrete operation the agent will perform:
   - What goes in (input)
   - What decision or action happens
   - What state is created or modified
   - What goes to the next step

2. **For each step, answer the autonomy question:** "At this step, can the agent act alone, or does a human need to review before the next step commits?"
   - **Level 0 (Suggest):** AI proposes, human decides. Agent cannot proceed without explicit approval.
   - **Level 1 (Suggest + Explain):** AI proposes with reasoning. Human can approve, reject, or modify with visible cost.
   - **Level 2 (Act + Report):** AI acts and reports. Human can undo within a time window. Undo is simple (rollback).
   - **Level 3 (Act + Monitor):** AI acts. Human monitors for anomalies. Intervention is possible but requires investigation.
   - **Level 4 (Autonomous):** AI acts with no human involvement. Use only when consequence magnitude is near-zero.

3. **Define the trust threshold for each step.** At what confidence level does the autonomy level change?
   - If confidence > X%, the agent operates at level N
   - If confidence < X%, escalate to level N-1 (require more human involvement)
   - If the agent refuses (high uncertainty), what's the fallback?
   - What happens if the confidence calibration is wrong?

4. **Design the handoff protocol.** Between each step:
   - What state is passed forward? (previous inputs, intermediate outputs, reasoning, confidence scores)
   - What state is NOT passed forward? (why did you decide to drop it?)
   - If step N fails, what context does step N+1 have to recover?
   - What happens if step N refuses to proceed?

5. **Specify failure recovery at each step.** For each step:
   - If the AI fails at this step, what's the rollback? (delete the output? flag for review? keep it but mark as unverified?)
   - How far back does recovery go? (just this step, or do earlier steps cascade?)
   - Who gets notified? (user, operations, customer success?)
   - What's the user experience during recovery?

6. **Define state snapshots.** For each step, log:
   - Input to this step (for debugging)
   - Decision made (what did the AI choose and why)
   - Output of this step (what changed)
   - Confidence or uncertainty signals
   - User feedback or intervention (if any)
   - Timestamp and user ID (for audit trail)

7. **Write the boundary matrix.** A table with:
   - Step number
   - Operation (what the AI does)
   - Autonomy level (0-4)
   - Trust threshold (confidence score boundary)
   - Failure mode (what breaks)
   - Recovery cost (time, manual effort, user friction)
   - Consequence magnitude (how many downstream steps are affected)

## SPRINT CONTRACT PATTERN

Before the Generator (AI agent) begins building or executing steps, the Generator and Evaluator negotiate an explicit sprint contract. This contract prevents divergence, scope creep, and burned tokens on style preferences.

**What goes in a sprint contract:**

1. **Implementation details:** Precise description of what the agent must do. Not "build a scheduling system" but "create a Google Calendar API wrapper that checks availability for a given attendee list and returns first 5 free slots (30min each) between 9am-5pm."

2. **Testable pass/fail criteria:** Each criterion must be demonstrable in 2-3 minutes without human judgment. Good: "All 50 test cases pass" or "Latency <200ms p95." Bad: "Works well" or "Feels responsive."

3. **Maximum iterations:** Typically 3-5 attempts. If the agent hasn't nailed it by iteration 5, escalate rather than burn more tokens. Lock this in: "Max 4 iterations; if not done, stop and report blockers."

4. **Kill conditions:** When to stop iterating and escalate. Examples: "If latency exceeds 500ms, stop and escalate" or "If accuracy drops below 85%, request additional training data instead of iterating."

**Why contracts matter:**

Without them, feedback loops diverge. The Evaluator asks for "better formatting," the Generator ships v2, Evaluator says "actually, cleaner look," Generator ships v3, and so on. Contract prevents this: Evaluator and Generator agree upfront on exact criteria. Once those pass, Generator stops.

**Contract template:**

```
Sprint Contract: [Task Name]
Generator: [AI model]
Evaluator: [Human/Process]

IMPLEMENTATION SPEC:
[Precise description of deliverable]

PASS/FAIL CRITERIA:
- Criterion 1: [testable]
- Criterion 2: [testable]
- Criterion 3: [testable]

MAX ITERATIONS: 4
KILL CONDITIONS:
- If [condition], stop and escalate
- If [condition], request [resource] instead

DEADLINE: [date/time]
```

Enforce this discipline. Contracts cost 10 minutes to write upfront and save 2-3 hours of misaligned iteration.

---

## FILE-BASED AGENT COMMUNICATION

Multi-step agents degrade when they pass state through context windows. Each handoff pollutes the context, earlier steps' reasoning gets buried, and the final step makes decisions on corrupted or incomplete state.

**The problem:**

```
Step 1: Agent sees full problem context (4000 tokens).
        Generates 500 tokens of analysis + 1500 tokens of plan.
        Passes 5500 tokens to Step 2.

Step 2: Receives 5500 tokens + original 4000 tokens = 9500 tokens in context.
        Generates 600 tokens of output + passes 10100 tokens to Step 3.

Step 3: Now operating in 10100 token context. Original nuance from Step 1 is buried.
        Decision quality degrades. Step 1 reasoning is now noise.
```

**The solution: File-based state.**

Agents write state to files (progress.md, state.json) instead of keeping it in context. Next agent reads fresh.

**Pattern:**

```
Step 1 (Analysis Agent):
  - Reads: /problem.md
  - Writes: /analysis.md (findings, key insights, open questions)
  - Writes: /state.json (structured decision points, confidence scores)

Step 2 (Planning Agent):
  - Reads: /problem.md, /analysis.md
  - Writes: /plan.md (detailed plan with reasoning)
  - Updates: /state.json (plan version, revised confidence)

Step 3 (Execution Agent):
  - Reads: /plan.md, /state.json
  - Executes plan
  - Writes: /execution-log.md (what ran, results)
```

**Benefits:**

- **Auditable:** Full history of reasoning is in files, not lost in context.
- **Survives context resets:** If an agent crashes or session resets, next agent can resume from file state.
- **Clear handoff boundaries:** Each agent knows exactly what to read and what to write. No ambiguity about "what state should I pass?"
- **Cost reduction:** Step 2 doesn't re-read Step 1's full analysis if it's in a file; it reads summary only.
- **Debugging:** When something breaks at Step 5, review /state.json to see exactly what Step 4 decided.

**File structure discipline:**

- /problem.md: Original user request, immutable.
- /analysis.md: Step 1 findings (append-only; never delete).
- /state.json: Single source of truth for decision state (version-controlled).
- /plan.md: Detailed execution plan from Step 2.
- /execution-log.md: What ran, results, errors.
- /handoff.md: Next agent's entry point (summary of what to do).

Enforce single source of truth: state.json is the canonical version. If an agent disagrees with state.json, it must update it explicitly, not override it in context.

---

## FEATURE LIST AS GUARDRAIL

A common failure mode: agents declare "done" before actually completing the work. They generate a surface-level output, confidence goes up, and you ship incomplete work.

**Prevention: Feature list.**

Before the agent starts, define all features/behaviors as a JSON list:

```json
{
  "features": [
    {
      "id": "auth-login",
      "description": "Users can log in with email + password",
      "passes": false,
      "verified_by": null,
      "test_result": null
    },
    {
      "id": "session-refresh",
      "description": "Sessions automatically refresh every 15 minutes",
      "passes": false,
      "verified_by": null,
      "test_result": null
    },
    {
      "id": "logout",
      "description": "Users can log out and session is cleared",
      "passes": false,
      "verified_by": null,
      "test_result": null
    }
  ]
}
```

**Explicit instruction to agent:**

"Do NOT remove, edit, or skip any features in this list. Mark each feature as passes: true only after you have demonstrated it works. You cannot declare the task done until all features have passes: true."

**Why it works:**

- Prevents premature completion declarations. Agent can't claim "done" if 2 out of 5 features are still failing.
- Auditable. At any point, you can see which features pass and which don't.
- Eliminates ambiguity. Agent can't argue about scope; the list is the scope.

**Enforcement:**

- Before agent starts: "Here is the feature list. Every feature must be implemented and tested."
- During work: "Which features still have passes: false? Iterate on those."
- Before acceptance: "Verify all features have passes: true and test_result is not null."

---

## SESSION INITIALIZATION RITUAL

Agents suffer from "cold start amnesia" — they begin working without understanding what was already done, what the current state is, or whether there are blockers from previous sessions.

**Mandatory initialization sequence (first 10 minutes of every agent session):**

1. **Directory verification:** Agent confirms the working directory is correct and contains expected files.
   ```
   - Project root: [path]
   - Config exists: [file]
   - Build artifacts present: [yes/no]
   - Git repo initialized: [yes/no]
   ```

2. **Progress file review:** Agent reads progress.md to understand what was completed in previous sessions.
   ```
   - Last completed step: [step number]
   - Last completion date: [date]
   - Known blockers: [list]
   - Context from previous agent: [summary]
   ```

3. **Git log check:** Agent reviews last 5-10 commits to understand the code trajectory.
   ```
   - Last commit: [hash, message, date]
   - Feature branches active: [list]
   - Merge conflicts unresolved: [yes/no]
   ```

4. **Feature list examination:** Agent reviews the feature list and identifies which features are failing.
   ```
   - Total features: [N]
   - Passing: [N]
   - Failing: [N]
   - Untested: [N]
   ```

5. **Dev server startup:** Agent starts the local development server and verifies it's responsive.
   ```
   - Server port: [port]
   - Health check: [pass/fail]
   - Recent errors in logs: [summary or none]
   ```

6. **Basic end-to-end test:** Agent runs a minimal happy-path test to confirm the system is functional.
   ```
   - Test: [description]
   - Result: [pass/fail]
   - If failed, blocking issue: [description]
   ```

**Output of initialization:**

Agent produces a /session-init.md file documenting the initialization results:

```markdown
# Session Initialization Report

**Time:** [timestamp]
**Agent:** [model]

## Directory State
- [checklist results]

## Progress Context
- Last completed: Feature X
- Blockers: [list]

## Git Status
- Last commit: [info]

## Feature Status
- Passing: 3/8
- Failing: 5/8 (detail which ones)

## Dev Server
- Status: [running/failed]
- Port: [port]

## Health Check
- E2E test: [pass/fail]
- Critical issues: [list or none]

## Recommended Next Steps
1. [step 1]
2. [step 2]
```

This ritual prevents "I didn't know X was already done" and "I didn't know Y was broken" surprises. It also creates a paper trail: future agents can see exactly what the current state is.

---

## QUALITY GATE

- [ ] Step graph drawn with discrete operations (not abstract "the agent does X")
- [ ] Autonomy level assigned to each step with explicit reasoning
- [ ] Trust threshold defined for each step (confidence score boundary, not vague)
- [ ] Handoff protocol documented (state passed forward, state dropped, reason)
- [ ] Failure recovery specified for each step (rollback, notification, user experience)
- [ ] State snapshot requirements defined (what to log, what to skip, sampling rate)
- [ ] Boundary matrix complete and reviewed by someone who isn't on the team

## WHEN WRONG

- Single-turn interactions (a user asks the AI one question, gets one answer)
- Fully deterministic workflows with no AI autonomy
- When the consequence magnitude of agent failure is so high that autonomy levels 3-4 are impossible
- When you're still exploring what the agent should do (use runbooks, not agent specs)
- When the agent is an experiment with a kill condition (spec this in the experiment doc instead)

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
