# Agent Specification — Concept Guide

## FIRST PRINCIPLES

An agent is not "the AI does multiple steps." An agent is a system where early decisions constrain later possibilities. In step 1, the AI chooses a direction. In step 2, it operates within that constraint. If step 1 chose wrong, step 2's options are limited, and by step 5, you're locked into a bad path.

The atomic insight: **in multi-step agents, uncertainty compounds. A 90% accurate system that runs 5 times in sequence is not 90% accurate anymore — it's 59% accurate.** If you're not designing for that uncertainty decay, you're designing for failure.

## DUAL DEFINITION

**Business definition:** Agent specification is the process of defining which steps in a multi-step AI workflow the system executes autonomously vs which require human review or approval, with explicit trust thresholds, recovery paths for failure, and state preservation across steps.

**Technical definition:** A formal specification of a directed acyclic graph of AI operations, each assigned an autonomy level (0-4) based on confidence thresholds, with rollback mechanisms for failure cascades, state snapshots for each transition, and monitoring requirements for anomaly detection.

## THE TRAP (Expanded)

**Autonomy Creep.** You start with "the AI drafts an email." That's level 0 or 1 — human approves. Then the deadline pressure arrives. "Actually, send the email if confidence > 90%." Now you're at level 2. Then, "let's not notify the user until it's sent." Level 3. Then, "the user has too many emails, so we won't notify unless something fails." Level 4 — and you've arrived at an autonomous email-sending system with no human oversight, built incrementally without ever having a conversation about whether this was acceptable.

**Confidence Collapse.** The model reports 85% confidence. This sounds good. But what does 85% confidence mean in your domain? You test it on your eval set and discover: 85% confidence actually means 78% accuracy. So you adjust your threshold to "only act alone if confidence > 92%." But 92% confidence is rare. Now the agent is escalating everything to human review, defeating the purpose of the agent. You never discovered the confidence miscalibration until it was live.

**State Amnesia.** Step 1 analyzes a document and identifies a key constraint. Step 2 needs that constraint to make the next decision. But the handoff protocol says "only pass the output forward, not the reasoning." Step 2 makes a decision that conflicts with the constraint. Steps 3-5 build on that conflict. By step 5, you discover the error. Rollback is expensive because the context is gone.

**Recovery Theater.** "If the agent fails, we have a rollback mechanism." This is true, but what does rollback cost? If step 1 sends an email and step 3 discovers it was wrong, the rollback is "send an apology email." The consequence magnitude is real. But on the spec, it's written as "rollback: one-click undo." This is recovery theater. Real recovery cost assessment forces that hard conversation.

## INTELLECTUAL LINEAGE

- **Harold Jeffreys on compound probability:** When multiple imperfect decisions cascade, accuracy degrades exponentially, not linearly. Applied to agents: a chain is only as strong as the weakest sequential step.
- **Elaine Wethington on organizational resilience:** The best safety systems don't prevent failures; they make recovery quick and visible. Applied to agents: the agent spec should make recovery cost visible in the design, not hidden until production.
- **Stuart Russell on AI alignment:** Agency (the ability to take action) and uncertainty create risk. The higher the autonomy level, the more rigorous the uncertainty quantification must be.
- **Ravi's trust ladder:** Five discrete autonomy levels that map to business decisions, not technical capabilities. Level 0 doesn't require better ML than level 4 — it requires a different product choice.

## REAL-WORLD EXAMPLES

**Example 1: Contract extraction agent (healthcare).** Step 1: Extract key terms from contract. Confidence calibrated to 96% on test set. In production, 88% accuracy on new contract types. Threshold should have been 97%+. Step 2: Check if terms violate company policy. This step was designed assuming step 1 has high accuracy. With 88% garbage-in, step 2 escalates 3x more often. At level 2 (act + report), users now complain about too many false positives. Lesson: confidence calibration is domain-specific and must be tested in production before autonomy level is committed.

**Example 2: Customer support agent (SaaS).** Step 1: Classify ticket type. Step 2: Generate response. Step 3: Send response. Designed at level 3 (act + monitor). What they didn't spec: what does "monitoring" mean? Who monitors? A Slack message when something breaks? 6 hours later, a customer-facing bug was still live. Monitoring is not a safety mechanism unless it's paired with on-call staff with authority to intervene. The spec looked safe; the org wasn't ready for it.

**Example 3: Research assistant agent (academia).** Step 1: Read paper abstracts. Step 2: Summarize findings. Step 3: Identify conflicts with existing literature. Step 4: Write conclusion. Each step is confident (>85%) individually. But by step 4, the accumulated errors are significant. The solution wasn't building a better LLM — it was inserting human checkpoints at steps 2 and 4, so a human reviews the summary and the conflicts. This moved the agent from level 3 to level 1 or 2, making it slower but trustworthy.

## THE CONFIDENCE DECAY FORMULA

This is the core insight of agent-spec: **don't build 5-step agents with 90% accuracy per step and hope for 90% end-to-end accuracy.**

Accuracy at each step: A₁, A₂, A₃, A₄, A₅
End-to-end accuracy: A₁ × A₂ × A₃ × A₄ × A₅

If each step is 90% accurate: 0.9^5 = 0.59 (59% end-to-end)
If each step is 95% accurate: 0.95^5 = 0.77 (77% end-to-end)

Most teams ship 5-step agents where each step is ~90% accurate and are shocked when end-to-end accuracy is 60%. The spec should calculate this explicitly and either:
- Require higher per-step accuracy (95%+, which is hard)
- Insert human checkpoints to break the chain
- Reduce the number of steps
- Accept 60% end-to-end and design the product for that reality (escalation, user override, monitoring)

A rigorous agent spec calculates end-to-end accuracy before design, not after production failure.

## FURTHER READING

- Stuart Russell, *Human Compatible* — On agency, uncertainty, and misalignment
- Abhijit Banerjee & Esther Duflo, *Poor Economics* — On cascading complexity in systems
- Elaine Wethington, "Social Structures and the Life Course" — On cascading failure
- Daniel Kahneman, *Thinking, Fast and Slow* — On how confidence and accuracy diverge
- Ravi's research: "The Five Levels of Autonomous AI" and "Compound Uncertainty in Multi-Step Systems"

## THE HANDOFF PROTOCOL IN DEPTH

A handoff protocol is where most agent specs fail. Here's what a rigorous one looks like:

```
HANDOFF from Step 1 → Step 2

CONTEXT PASSED:
  - User ID
  - Original request
  - Step 1 output (the decision made)
  - Step 1 confidence score
  - The reason for the decision (reasoning trace)
  - Any constraints identified in step 1

CONTEXT NOT PASSED (and why):
  - Full step 1 intermediate reasoning (too much context window cost)
  - Full previous request history (out of scope for step 2)
  - Embeddings or feature vectors (step 2 has its own encoders)

FAILURE MODES:
  - If step 1 refused: What does step 2 do? (Escalate? Try a different strategy? Abort?)
  - If step 1 confidence < threshold: What autonomy level does step 2 inherit? (Lower level, more human involvement?)
  - If step 1 output contradicts user input: Does step 2 treat it as a correction or an error?

RECOVERY MECHANISM:
  - If step 2 fails: Can step 1 be re-run with different parameters?
  - Cost of re-run: (API call cost, latency, user waiting)
  - Notification: Who knows the step 1 output was suspect? (Just logs, or user sees it?)
```

This is the level of detail required. Vague "pass the output forward" is not a handoff protocol.
