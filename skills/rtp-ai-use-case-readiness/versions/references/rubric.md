# Scoring rubric and calibration

Use a 1 to 5 scale. Treat 1 as low / easy / explicit / stable / narrow, and 5 as high / hard / tacit / dynamic / broad.

## Core dimension anchors

### knowledge tacitness
- 1 = rules can be written down cleanly; experts mostly agree
- 3 = mix of codified rules and judgment
- 5 = depends heavily on intuition, context fusion, negotiation, or expert craft

### cost of error
- 1 = nuisance or minor rework
- 3 = material business impact but recoverable
- 5 = major financial, legal, safety, regulatory, or trust harm

### verification difficulty
- 1 = correctness is easy to check automatically or immediately
- 3 = partial checks exist but not for every edge case
- 5 = correctness is subjective, delayed, hidden, or hard to observe

### irreversibility
- 1 = easy rollback with low cost
- 3 = recoverable with meaningful effort, delay, or customer friction
- 5 = hard, expensive, or impossible to undo

### process variability
- 1 = repetitive with few branches
- 3 = moderate exceptions and path changes
- 5 = novel, path-dependent, or highly exception-driven

### coordination complexity
- 1 = one system or one step
- 3 = several tools, handoffs, or dependencies
- 5 = many interdependent systems, actors, and sequencing constraints

### environment dynamism
- 1 = static inputs and stable state during action
- 3 = periodic change or moderate drift
- 5 = fast-changing context, external actors, or state changes during execution

### consequence magnitude
- 1 = local or internal impact
- 3 = team or segment-level impact
- 5 = customer-facing, enterprise-wide, or systemic impact

### decision-rights sensitivity
- 1 = low-risk internal actions with narrow permissions
- 3 = meaningful changes with scoped permissions and clear policy
- 5 = sensitive approvals, spending, legal commitments, security actions, or customer-impacting decisions

## Optional modifiers

### compliance sensitivity
How strict policy, legal, audit, or documentation requirements are.

### data quality gaps
How incomplete, stale, ambiguous, or inconsistent the inputs are.

### latency sensitivity
How little time exists for review, verification, or correction.

### economic leverage / frequency / scale
How much repetition, leverage, or strategic value justifies heavier engineering and control effort.

## Readiness bands
- ready now = value is clear, autonomy can be scoped safely, and verification or rollback is strong enough for the recommended pattern
- ready with controls = the pattern is plausible, but approvals, evals, telemetry, or rollback must be built first
- assist only now = reasoning support is useful, but execution should remain human-led for now
- not a fit = non-ai or low-autonomy workflow design is better, or the control burden outweighs the expected value

## Choosing the second effort curve
Default to effort vs verification difficulty.

Switch only when another parameter is clearly more binding.
- Use effort vs knowledge tacitness when expertise capture and judgment calibration are the main blockers.
- Use effort vs environment dynamism when changing state, timing, or external actors dominate.
- Use effort vs consequence magnitude when governance, trust, or operational risk dominate.
- Use effort vs latency sensitivity when response windows are so tight that human review and heavy controls become the main design problem.

## Calibration examples
- invoice matching: usually explicit, fairly verifiable, and often better served by rules, extraction, and workflow than by agents
- knowledge-base answer drafting: often low to medium error cost and reasonably reviewable; strong fit for retrieval plus copilot
- customer refund approval above a threshold: explicit policy may exist, but decision-rights sensitivity and consequence magnitude push toward approval gates
- cross-system meeting scheduling: moderate variability with low consequence magnitude; good candidate for bounded workflow automation or a narrow agent
- security incident triage: often dynamic and coordination-heavy, but verification and consequence magnitude matter enough that copilot or bounded agent is safer than free-running autonomy
- commercial negotiation or executive stakeholder management: high tacitness and high error cost usually favor human-led decision making with strong assistive support
