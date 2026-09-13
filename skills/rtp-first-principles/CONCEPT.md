# First principles: concept guide

First-principles thinking identifies the user outcome and the operations required to achieve it before selecting a technology. In an AI product, a fluent response or working interface may conceal an incorrect result. Conventional software can also fail silently. Inspect the outcome rather than relying on the appearance of successful execution.

The practical contribution is a decomposition that separates explicit rules, learned patterns, and decisions needing judgment. A workflow may contain several essential operations. Preserve their relationships and the user's context while examining them individually.

## Two ways to explain the method

**For a business reader:** establish the useful customer outcome before deciding what to build. Compare the proposed investment with simpler ways to achieve it.

**For a technical reader:** map the system into operations, dependencies, and completion conditions. Identify where conventional code, learned components, and review belong, then choose component and end-to-end checks.

## Why the first solution can become the only solution

Three common reasoning traps deserve attention:

- **Anchoring:** a competitor's "AI search" becomes the assumed answer before the team asks whether users need search, curation, alerts, or a current authoritative record.
- **Availability:** a technique the team recently learned, such as retrieval or agents, comes to mind more easily than other approaches.
- **Sunk cost:** prior investment makes revisiting the framing uncomfortable, even when new evidence warrants it.

Treat each as a possibility to investigate, not a diagnosis of someone's motives. Ask what evidence supports the need and whether the design still follows from that evidence.

## Intellectual influences retained from the original guide

These are conceptual influences, not empirical proof that a particular design will work:

- **Kapil Gupta:** understand the problem before prescribing a solution; the earlier guide points to *A Master's Secret Whispers*.
- **Physics-style first-principles reasoning, associated in the original with Elon Musk:** examine underlying constraints rather than relying only on what competitors do.
- **Charlie Munger's inversion:** examine where a proposed approach could make the problem worse.
- **Shreyas Doshi's product-sense writing:** give sustained attention to the problem and the opportunity cost of a solution.

Further reading retained from the original includes Daniel Kahneman's *Thinking, Fast and Slow* and Shane Parrish's *The Great Mental Models*. Verify a precise quotation or empirical claim against the relevant source before using it.

## Illustrative cases

The original guide presented the following cases without identifiable company records or supporting citations. Use them as constructed teaching examples. Their numerical assumptions are not verified results or general design thresholds.

### Find the current policy

A team proposes semantic search for internal documents. Decomposition reveals that many users need the current version of a known policy. Explicit metadata and version control may solve those requests, while semantic retrieval may help with open-ended questions.

The original illustration assumed an 80% rules / 20% semantic split and a 60% reduction from an initial cost estimate. Those values require measurement in a real deployment. The preserved lesson is to distinguish locating an authoritative record from interpreting an unfamiliar query before choosing the search architecture.

### Handle a support request

Separate routing, information retrieval, sentiment signals where relevant, response drafting, and escalation. These may use different combinations of code, models, and review. Each needs an appropriate measure, and the completed customer journey needs its own evaluation.

A single agent interface can contain this decomposition. The issue is whether the implementation makes component responsibilities and failure recovery visible, not whether it uses the word "agent."

### Recommend a price

The proposed outcome is to adjust a price using demand signals. If the relevant inputs are structured and the relationship can be modeled appropriately, a conventional statistical method may be a stronger baseline than a language model.

The original example asserted a cost of one hundredth of the LLM approach without a cited comparison. Retain that ratio only as an explicitly assumed teaching value. Compare actual task quality, constraints, implementation effort, and operating costs before selecting a method.

## Use decomposition as a decision check

Before a consequential investment, agree on the user outcome, essential operations, and main uncertainty. The original guide contrasted four hours of decomposition with eight weeks of mistaken building and four weeks of well-directed building. That is an illustrative planning story, not a measured time-saving claim. Use a timebox suited to the uncertainty and commitment.

Watch for conclusions justified only by a demo, a competitor's design, available budget, or a promise to clarify the problem later. A demo can be useful evidence when its limits and representative coverage are understood. Budget does not establish the need, and an incomplete frame should be made explicit rather than hidden in the implementation plan.

Decomposition is complete when it improves the team's ability to choose and evaluate an approach. It does not need to eliminate AI, change every proposed component, or reduce every workflow to an arbitrary 80/20 split.
