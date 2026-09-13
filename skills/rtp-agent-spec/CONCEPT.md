# Why an agent needs an operating contract

The agent spec makes dependencies and consequences visible. Good individual steps do not establish a reliable whole, and a plausible explanation does not establish authority to act.

## Three recurring failures

**Autonomy creep.** A recommendation gains a send, purchase, or update action without a corresponding permission boundary. Define the action and authorization before discussing the agent's confidence.

**State amnesia.** An early step discovers a constraint, but the handoff drops it. Later work then depends on an invalid assumption. Pass the constraint, source, current status, and concise rationale; a complete internal reasoning trace is unnecessary.

**Recovery theater.** A spec calls an apology email “one-click undo.” The original recipient may already have acted. Describe real rollback separately from compensation, containment, and reconciliation, including their time and customer cost.

A fourth issue can connect all three: **miscalibrated confidence**. Raising a numerical threshold may increase review burden without establishing sufficient reliability. Re-evaluate by domain and error type, and measure whether the selected actions actually meet the requirement.

## The chain-reliability example, with its assumptions

If all five steps must succeed, each succeeds independently with probability 0.9, and there is no recovery, then:

```text
P(all five succeed) = 0.9^5 = 0.59049, about 59%
At 0.95 per step:  0.95^5 = 0.7737809375, about 77%
```

These calculations are illustrative, not a prediction for all five-step agents. Multiplying separately measured marginal accuracies requires independence. Without independence, the chain rule uses conditional probabilities:

```text
P(A1 and ... and A5)
= P(A1) × P(A2 | A1) × ... × P(A5 | A1,...,A4)
```

Even that event may differ from final task success: some intermediate errors do not affect the result, and verification or recovery may correct others. Shared causes can correlate failures. Measure complete representative trajectories, including branches, retries, handoffs, and external outcomes.

Possible improvements include better step performance, targeted verification, fewer unnecessary dependencies, and explicit fallback or review. Human checkpoints are fallible interventions, not resets to perfect certainty. Choose them where they detect or prevent material errors and test the resulting end-to-end performance.

## Three illustrative cases

These are design scenarios, not documented company results or benchmark thresholds.

**Contract extraction.** A system measured at 96% on its test set achieves 88% on new contract types. Downstream policy checks escalate three times as often. A change to a “97% confidence” threshold is not automatically the remedy: inspect labels, document mix, calibration, and the cost of missed clauses versus unnecessary review. Restrict affected actions while testing a suitable correction.

**Customer support.** An agent classifies, drafts, and sends a response. A problem remains customer-visible six hours after an alert because no responder owns it. Specify coverage, actionable alerts, stopping authority, and recovery; monitoring alone is incomplete. Consider approval before sending where the consequence and available evidence require it.

**Research synthesis.** An agent reads abstracts, summarizes findings, compares conflicts, and writes a conclusion. Its self-reported confidence exceeds 85%, but it loses a study limitation between steps. Preserve evidence and constraints, and trial checks after summary and conclusion. Human review at steps two and four is one candidate design, not a guaranteed cure or the only alternative to a better model.

## A handoff that supports recovery

```text
From / to: [step, person, or process]
Current request and relevant updates: [...]
Permission scope and approval reference, if applicable: [...]
Outcome and status: [complete / partial / refused / failed / unknown effect]
Output and supporting evidence: [artifact/source references; freshness]
Constraints and assumptions: [...]
Uncertainty: [defined score and basis, or qualitative evidence gap]
Concise decision rationale: [...]
Omitted context and reason: [...]
Receiver's permitted next action: [...]
Conflict/refusal behavior: [...]
Recovery: [retry, reconcile, compensate, or pause; limits]
Affected downstream artifacts or effects: [...]
Owner, notification, and expected cost: [...]
```

Include personal identifiers only when necessary and appropriately protected. If an output conflicts with user instructions, do not assume it silently corrected the user. Verify the source and resolve the conflict at the relevant authority level.

Files can preserve this record across sessions. They still need freshness checks, access controls, and clear ownership; a persistent incorrect assumption remains incorrect.

## Connections and lineage

- `rtp-autonomy-spectrum` describes operating choices; actual permissions belong in the spec.
- `rtp-trust-ladder` separates appropriate reliance from authorization and confidence.
- `rtp-failure-modes` identifies how the workflow can fail; the spec assigns containment and recovery.
- `rtp-determinism-compass` helps decide which steps benefit from predictable rules, generative work, or a combination.
- `rtp-tool-architecture` turns interface and authority requirements into enforceable tool boundaries.

The probability example follows standard conditional probability, not a special agent-specific theorem. Stuart Russell's *Human Compatible* provides broader context on agency and uncertainty; Daniel Kahneman's *Thinking, Fast and Slow* provides broader context on judgment and confidence. These are conceptual reading suggestions, not empirical validation of this spec. Earlier attributions to Jeffreys, Wethington, *Poor Economics*, and locally named essays did not establish the specific agent claims and should not be cited as if they did.

See [spec evidence](references/spec-evidence.md) for the decision-rights, accountability, and protocol sources used in this revision.
