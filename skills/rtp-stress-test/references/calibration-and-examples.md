# Stress Test: calibration, pre-mortem prompts, and research notes

The main skill defines the process. This reference retains its original teaching ranges and examples while making their limits explicit. Choose real criteria from the product's consequences, expected workload, and commitments.

## Token budget worksheet

These are **illustrative planning ranges**, not current provider specifications or measured industry norms:

| Component | Original example range, tokens/request | What actually determines it |
|---|---:|---|
| System prompt | 500–2,000 | Instructions, tools, and context included; caching eligibility is provider-specific. |
| Retrieved context | 1,000–8,000 | Retrieval selection, chunking, filtering, and context budget; not knowledge-base size alone. |
| User input and history | 500–4,000 | Request content, conversation length, summarization, and state strategy. |
| Model response | 200–2,000 | Task, actual generation, output limits, and model behavior. |
| **Total** | **2,200–16,000** | Sum of these example ranges; input and output still need separate prices. |

The earlier skill suggested that P50 and P95 token use can differ by 4x and that retry rates of 5–15% are normal. Keep these only as possible sensitivity cases. Measure the actual distribution and retry mechanism; do not treat either number as a baseline. A 2K-to-8K request growth scenario, 10K-trace evaluation run, or $0.04-to-$0.80 iterative request similarly illustrates a mechanism rather than an expected outcome.

## Earlier scoring thresholds: examples, not universal gates

The earlier matrix used these labels. They may help a team discuss requirements, but must not be imported as pre-approved launch criteria:

| Dimension | Earlier Pass example | Earlier Marginal example | Earlier Fail example |
|---|---|---|---|
| Failure at scale | Recovery and contained consequences at 10x load | Manual intervention at 10x with a playbook | Cascade at 3x with no recovery |
| Cost | Positive unit economics at 10x with price sensitivity tested | Break-even at 10x with an optimization path | Negative economics at current scale |
| Latency | P95 below 2 seconds under load | P95 of 2–5 seconds | P95 above 5 seconds or highly variable |
| Monitoring | Detection within 5 minutes, tested automatic alert and runbook | Within an hour, manual alert, untested runbook | Detection only from user reports, no runbook |
| Adversarial | 40/40 probes passed | 1–3 low-severity failures with dated fixes | Any high or critical finding |
| Harness | Recovery across relevant steps; breakers exercised | Partial recovery with some manual work | Uncontained failure of the chain |

A 30-second asynchronous review may meet a sound SLO while a two-second response is too slow for another task. Five-minute detection can be too late for an irreversible action. Negative current economics may be a deliberate, bounded experiment rather than an automatic product veto. Conversely, meeting these example numbers cannot excuse an exposed severe failure. Replace the values and disposition rules with explicit criteria for the release.

Cost sensitivity also needs boundaries: a 3x token-price scenario does not imply storage, salaries, and every other line triple. A long-tail or timeout budget may matter more than P95 alone. A forty-probe suite is a coverage starting point, not a security certification.

## AI-specific pre-mortem worksheet

Each row is an illustrative hypothesis to adapt, test, and assign. No listed symptom proves its proposed cause on its own.

| Failure mode | Possible story or signal | A concrete next action |
|---|---|---|
| **Evaluation drift** | The suite still scores 87% while measured satisfaction falls 12%; the task mix may have changed. State whether the satisfaction change is relative or percentage points. | Investigate segment and task coverage. Add fresh cases while retaining a stable comparison set and documenting version changes. The old 20–30% monthly refresh was an example, not a rule. |
| **Prompt regression** | A change fixes one visible bug and breaks three quieter cases. | Run relevant regression and critical-boundary tests, comparing failure types. Use the full required suite where policy or risk warrants it; a targeted test alone may miss the change's broader effects. |
| **Model deprecation** | A provider retires a version and its replacement behaves differently. | Track the actual lifecycle notice, test the candidate, and rehearse migration. The earlier 12–18-month timeframe was not a provider guarantee. |
| **Cost spiral** | Conversation length becomes 4x larger over six months. | Measure token distributions and successful-outcome cost; test history limits, retrieval budgets, or state changes before altering service quality. |
| **Trust loss** | A serious bad output or credible complaint undermines use. | Prepare containment, investigation, communication, and recovery. Do not claim the team “caught” an incident if someone else reported it. Prevention and recovery matter according to the risk; neither universally outranks the other. |
| **Silent degradation** | Aggregate quality looks stable while a demanding cohort has more failures or leaves. | Examine segment and task-level quality, rework, and exposure. Do not assume the slowest requests necessarily belong to the most expert users. |

For each plausible material mode, specify the failed outcome, warning signal, load-bearing assumption, and “Tuesday action.” A four-week beta or six-month future scenario is a planning option, not a mandatory duration.

## Historical harness example

Anthropic's [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps), published 24 March 2026, reports a solo run of **20 minutes/$9** and a fuller harness run of **six hours/$200** for an application-generation example. The cost ratio is approximately **22.2x**. The fuller run also attempted a broader implementation; this is not a controlled estimate of the cost multiplier for identical work or a universal 10–20x rule.

The article describes **5–15** design iterations and model-specific context behavior. It reports context anxiety for Sonnet 4.5 and a materially different experience with Opus 4.5. Carry the practical questions—context handling, handoff quality, evaluator calibration, and complete-run cost—rather than a claim that every 200K-token window becomes unusable at the same fraction.

## Review and incentive sources

The original skill draws its missing-concerns, unheard-perspectives, and challenged-assumptions prompts from **“How the Best Leaders Shape Conversations,” HBR, August 2026**. It describes the authors' work across more than one hundred teams. These prompts are useful facilitation tools; this editorial pass does not newly verify a causal effect or guarantee candid responses.

The reviewer-exposure column is a practitioner idea drawn from an HBR IdeaCast interview in the local source material. It helps identify incentives and conflicts. The stronger assertion that information value is proportional to personal risk is not established and should not guide participation.

The “reward the self-kill” example is attributed in the original skill to **Linda A. Hill, “How Leaders Create the Conditions for Innovative Thinking,” HBR On Leadership / IdeaCast, 24 June 2026**. A leader reportedly paid a bonus for stopping one's own idea. Retain this as a qualitative example, not a proven incentive design. Reward supported learning and sound continuation as well as justified cancellation.

## NOVEL INSIGHTS connections used here

- **B:** reduce test exposure where possible and give the work a real owner with time and capacity. Do not require a particular HR mechanism as the only way to establish ownership.
- **C / R:** practical ability to act differs from accountability on paper. Lack of authority is a risk to investigate, not proof that a reviewer fabricated an explanation.
- **Q:** useful review needs an artifact or evidence the reviewer can inspect, a challenge route, and a proportionate stopping condition. Endless disagreement is not a quality guarantee.
- **H:** test whether preparation, escalation, and rework absorb a local speed gain. Do not infer a fixed productivity haircut from handoff count.
- **10 SEP control-scope finding:** exercise the behavior a control is supposed to protect. A configured breaker, a readable explanation, and an audit log each answer different questions.

## Calculation check for the code-review example

Using the main skill's illustrative blended rate and 30-day month:

```text
Inference/day = 8,000 tokens/review × 1,000 reviews/day × $0.003/1,000 tokens
              = $24/day
Monthly listed cost = ($24 + $5) × 30 + $15 × 30/7 = $934.29
Reviews/month = 1,000 × 30 = 30,000
Listed cost/review = $934.29 / 30,000 = $0.03114

At 3x inference price:
Monthly listed cost = ($72 + $5) × 30 + $15 × 30/7 = $2,374.29
Listed cost/review = $2,374.29 / 30,000 = $0.07914
```

The earlier $0.95-per-PR figure was inconsistent with the listed volume and costs. These corrected figures still omit other operating costs and do not establish equivalent quality or savings relative to a hypothetical $15 human review.
