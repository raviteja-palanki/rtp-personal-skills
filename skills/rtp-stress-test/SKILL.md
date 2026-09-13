---
name: stress-test
version: v1.2.1_latest
description: 'Test whether an AI feature can meet its production commitments before launch or a resource, cost, or response-time promise. Examine failure at scale, cost at volume, tail latency, monitoring, adversarial inputs, and agent resilience where applicable. Combine measured tests with a pre-mortem for failures that operational dashboards may miss. Set test boundaries, evidence standards, decision authority, and launch blockers first; report untested areas honestly. Use for production readiness, 10x-load planning, degraded providers, or unit-economics checks. Pairs with ship-decision, cost-model, agent-risk, failure-modes, production-observability, fit-signal, and judgment-guard.'
imports: []
---

# Stress Test

Find consequential failure modes while the team can still change the feature, rollout, or promise. Produce evidence for a launch decision, with clear limits and owned actions.

A successful demo establishes that something worked under those conditions. Production may introduce different inputs, traffic, costs, dependencies, and user expectations. Stress testing reduces uncertainty about that gap; it does not guarantee reliability or discover every failure.

Use two complementary methods:

- **Measure operational failures:** load, cost, latency, quality detection, hostile inputs, and agent recovery.
- **Run a pre-mortem:** imagine a plausible failed outcome despite healthy operational metrics, then turn it into signals and tests.

Both depend on people being able to report a failure and act on it. Set that up before testing, not only after an uncomfortable result arrives.

## 1. Define the commitment and test boundaries

Record the customer, task, release scope, and promise being assessed. What does one bad response or action cost? Is the consequence reversible, detectable, and recoverable? What happens if launch waits?

Before running tests, agree on:

1. **Decision and scope:** prototype, restricted beta, general release, capacity increase, or SLO commitment. Specify intended users, tasks, traffic, and permitted actions.
2. **Pass criteria and blockers:** choose task-appropriate limits for quality, cost, latency, and harm. Define what would require a fix, a narrower rollout, or a no-go. A plausible severe, unrecoverable failure needs an effective control before the exposed release proceeds.
3. **Test environment:** use an authorized environment, suitable test data, a cost ceiling, and a stop condition. Isolate writes and external effects where needed. Load tests, fault injection, and adversarial tests can themselves disrupt systems; do not assume a request for a review authorizes an uncontrolled production exercise.
4. **Owners and authority:** who runs the test, reviews the evidence, decides release, and can stop or override it? Give those people the access, time, and capacity required to act.
5. **Evidence plan:** define the workload, conditions, measures, sample coverage, and comparison. Record estimates separately from observations. Untested is not Pass.

Use the Universal Skill Protocol for grounding and handoffs. It is at `ai-pm-skills/UNIVERSAL-SKILL-PROTOCOL.md` in the source library and the plugin root. Keep the report inline when that is sufficient.

**Depth is proportional to consequence.** Consider all six dimensions and explain exclusions. Dimension 6 applies to systems with agent orchestration, state, or tool actions, including a single agent. A small internal tool may need little capacity testing but substantial access or data protection checks. A time-boxed experiment still needs boundaries appropriate to its exposure.

## 2. Measure the six dimensions

Use a plausible stressed workload, not “10x” as a ritual. Ten times current traffic is a useful scenario when it matches a commitment or uncertainty. Distinguish daily volume, arrival rate, bursts, concurrency, request complexity, and duration.

### Dimension 1 — Failure at scale

Test what users and dependent systems experience when:

- Load or concurrency rises and queues, rate limits, or downstream services become constrained.
- A model produces an incorrect, misleading, or unauthorized result. Examine the consequence and containment, not only its average frequency.
- A provider becomes slower or less useful while still returning successful responses.
- A provider is unavailable for a relevant period; 30–60 minutes is an illustrative scenario.
- Quality degrades without an exception or uptime alert.

Verify the degradation path: limited functionality, a queue, an appropriate cache, a tested alternate route, a human handoff, or a clear safe stop. The fallback must meet the task's constraints. Stale cached answers and a less capable model are not automatically safe. Record recovery time, lost or duplicated work, and what users are told.

### Dimension 2 — Cost at volume

Build the model with explicit units and billing categories. For a daily estimate:

```text
requests/day = active users × requests per active user per day

model cost/day = requests/day × sum across calls of:
  (uncached input tokens × uncached input rate
   + cached input tokens × applicable cached-input rate
   + output tokens × output rate)

total operating cost = model cost + retrieval/embedding/storage/tool costs
  + evaluation and monitoring + attributable human operation/review
  + other relevant infrastructure or service costs
```

Convert provider rates to the matching unit, such as dollars per token rather than per million tokens. Include cache-write charges or other billing categories when applicable. Count retries, evaluator calls, and repeated agent rounds once; do not add them again if the measured call totals already include them. Apply caching savings only to eligible traffic using the actual billing rules. Verify current prices and terms before making a real commitment.

Model present volume, the planned release, and plausible adverse cases. A 10x-volume case and 3x-token-price sensitivity can expose fragility, but choose scenarios that fit the decision. Price rises affect the modeled component, not automatically every cost line.

Watch four commonly omitted mechanisms:

- **Conversation growth:** a scenario moving from 2K to 8K tokens per request quadruples that token quantity. Measure the input/output mix and history strategy; this is not inevitable growth.
- **Evaluation overhead:** recurring evaluation of 10K traces can be material and should be budgeted.
- **Context pressure:** quality may change as context grows, even before a limit is reached. Test the actual model and harness rather than assume a universal usable fraction.
- **Agent iteration:** planner, generator, evaluator, tool, and retry calls add cost. Five to fifteen rounds may be expensive; measure calls and outcomes rather than apply a universal multiplier.

Report cost per request **and per successful outcome**, along with user-level economics where meaningful. Include review, rework, escalation, and unresolved tasks so a faster model step does not conceal work transferred elsewhere. Keep cost estimates distinct from a proven profit or ROI claim. [Calibration notes](references/calibration-and-examples.md) preserve the original token ranges and historical harness example.

### Dimension 3 — Tail latency and the user experience

**P95 latency** is a threshold at or below which approximately 95% of measured request times fall. It is not the worst case or the average experience of the slowest 5%. P99 examines a further tail; timeouts and maximum-duration behavior also matter.

Measure under the stated workload:

- End-to-end completion time and, for streaming, time to first token or first useful output.
- Tail latency, timeout rate, and error rate at expected and stressed concurrency.
- Retrieval, queueing, inference, tool, and post-processing time to locate bottlenecks.
- The user experience while waiting, including cancellation, retries, and duplicate submissions.

Do not add component P95 values and label the sum an observed end-to-end P95. Measure the full path. Streaming can improve perceived responsiveness while the complete result still takes longer. An asynchronous code review and a conversational suggestion need different targets.

An **SLO** is a target for a defined service measure over a specified period and population. Record those details. Estimates help plan tests; they are not measured evidence for a commitment. See [Google SRE on service-level objectives](https://sre.google/sre-book/service-level-objectives/).

### Dimension 4 — Monitoring and observability

Demonstrate how the team will detect and respond to important failures:

- Track relevant quality measures and segments, not just uptime and average latency.
- Capture sufficient provenance: model and prompt versions, retrieval or tool context, timing, outcomes, and relevant configuration. Handle sensitive content, access, retention, and redaction according to the product's requirements.
- Test an alert with a known failure or controlled degradation. Record detection delay and false-alert behavior.
- Name the responder and rehearse the runbook, including fallback, rollback, escalation, and recovery.
- Check whether a failure can be investigated from retained evidence. Exact replay may be impossible because of nondeterminism or changing external state; state that limit rather than promise that logs reconstruct everything.

Ask the “2 a.m.” question: who can act when the responsible person is unavailable? Match coverage to the service, rather than assuming every internal feature needs continuous on-call staffing. A dashboard and a named owner do not establish detection competence or practical stop authority.

### Dimension 5 — Adversarial testing

Name the product's leading abuse and security risks, such as data disclosure, unauthorized actions, policy evasion, or prompt injection. Define expected behavior and severity before testing. Use relevant attack families; the original five-part ladder is retained below as **coverage categories**, not a validated ordering of difficulty.

| Family | Illustrative probe | What to inspect |
|---|---|---|
| Direct override | An explicit request to ignore the task's instructions | Whether instructions and action boundaries hold. |
| Obfuscation | Encoded or transformed content | Whether interpretation changes the enforced boundary. |
| Context or role manipulation | A claimed developer role or fictional exception | Whether unsupported authority claims change behavior. |
| Payload in data | Instructions inside a retrieved page, uploaded file, or code comment | Whether untrusted content is treated as instructions or gains tool authority. |
| Multi-turn escalation | A later request exploiting earlier conversation | Whether state and accumulated permissions remain appropriate. |

Record test input, relevant context, model and tool behavior, pass/fail, severity, and evidence. Repeat important cases where stochastic variation matters. Add variations based on observed failures and the actual attack surface. Forty or more probes can be a useful starter suite; passing 40/40 establishes only performance on those tested cases.

A prompt, scanner, or pattern matcher alone does not establish protection. Test the controls at the action and data boundaries as well as the model response. Review layered controls such as restricted tool permissions, validation, isolation, and appropriate approval gates. [OWASP's prompt-injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) explains the need for layered defenses.

Unresolved high-severity failures block the release scope they expose; escalate critical findings to the responsible security or risk owner. Low-severity findings need explicit disposition and may still block a release in a sensitive context. Retest a fix; a proposed “stronger system prompt” is not evidence that it worked.

### Dimension 6 — Agent and harness resilience

Apply this dimension when the feature coordinates work, retains state, or uses tools. Test:

- **Circuit breakers and isolation:** a failing or looping step trips the intended limit and does not consume the whole budget or corrupt other work.
- **Context pressure:** task completion, constraint retention, and handoff quality near relevant context limits. The original 80/90/95% checkpoints are illustrative, not guaranteed safe zones.
- **State durability:** interrupted sessions, retries, concurrent handoffs, and recovery preserve valid state without duplicate actions. Fifty sessions is a possible scenario, not a reliability standard.
- **Tool failure:** timeouts, partial success, unavailable dependencies, and ambiguous results have defined recovery paths.
- **Budget and termination:** repeated rounds have cost/time limits and a stopping rule that does not merely depend on the generator declaring itself successful.
- **Evaluator quality:** assess a judge against suitable reference judgments or observable outcomes. A separate agent can still repeat the generator's error or reward the wrong qualities.

A **circuit breaker** interrupts a failing operation so it does not cause a cascade. Test the trip and recovery; a configured setting alone is not evidence. Use `rtp-agent-risk` for consequential action boundaries and `rtp-judgment-guard` for review design.

## 3. Assess readiness against the agreed criteria

Use the release's stated requirements, not universal speed or cost thresholds:

| Status | Meaning | Required response |
|---|---|---|
| **Pass** | Evidence meets the applicable criterion under the recorded conditions. | Retain the evidence and monitoring plan. |
| **Marginal** | A bounded, acceptable gap remains for the proposed scope. | State the limit, mitigation, owner, date, and authorized risk decision. |
| **Fail** | An applicable criterion is not met or a material prohibited consequence remains exposed. | Fix, narrow scope, or recommend no-go; do not average it away. |
| **Untested / unknown** | Evidence is missing or insufficient. | Identify the needed test; do not treat this as Pass. |
| **Not applicable** | The dimension does not apply to this release. | Give a specific reason. |

Every applicable dimension needs a supported disposition. A full release with an unresolved Fail is a no-go under that scope. A narrower proposal must be assessed on its own exposure; renaming a launch “beta” does not remove the failure. A Marginal result is not permission to cross a pre-agreed hard boundary. Deadlines and portfolio commitments do not supply missing readiness evidence.

## 4. Run the pre-mortem and connect it to tests

Run a short pre-mortem early enough to influence the test plan; revisit it after the results and before the decision. Imagine a plausible future in which the feature launched but failed to deliver the intended outcome. Six months and a 90-minute discussion are useful example frames, not required settings.

Answer four questions:

1. **What failed?** Describe an outcome, not only a crash. For example: adoption rose to 18% in week 1 and 22% in week 4, then fell to 11% by month 4 as users encountered subtle errors in important work. These are illustrative numbers, not a prediction.
2. **What signals might have warned us?** Consider an evaluation plateau, cost per successful outcome rising, more edits despite stable acceptance, declining use in an experienced-user cohort, or more complex support cases despite steady ticket volume. These are candidate signals with alternative explanations, not proof of quality decay. Complaints can also be valuable evidence; do not discard them because they lag some events.
3. **Which assumption broke?** Select the few load-bearing assumptions: production quality matches evaluation; users understand uncertainty cues; costs stay within budget; model availability lasts through the planned period; abuse remains contained. For each, specify observable contrary evidence and what action it would trigger.
4. **What would we do on Tuesday if we saw that signal?** Name a feasible action and owner: add a missing task segment, test a candidate migration, investigate cohort rework, restrict a risky workflow, or run a bounded beta. “Be more careful” is not an action.

Probe the AI-specific modes in the [pre-mortem reference](references/calibration-and-examples.md): evaluation drift, prompt regression, model deprecation, cost spiral, trust loss, and silent degradation. Preserve a stable comparison set while adding fresh evaluation coverage; otherwise an improving score may merely reflect an easier test. Do not require an arbitrary monthly refresh percentage.

Imagination supplies hypotheses, not measured failures. Investigate plausible material risks and put effective controls in place where consequences cannot be accepted. A severe finding does not disappear because telemetry is green. Equally, an unsupported catastrophe story is not by itself proof that the product must never ship.

## 5. Make candor and decision authority practical

Open the review with its intended outcome and the roles established in Step 1. Make any blocking or override authority visible. Invite missing concerns, unheard perspectives, and assumptions worth challenging.

The source material's three concise prompts are:

1. “What concerns aren't we talking about?”
2. “Whose perspective haven't we heard?”
3. “What assumptions should we challenge?”

These are facilitation prompts, not a guarantee of candor. Ask for evidence, give people time to form a view, and record how concerns were resolved. If the proposal owner facilitates, manage that conflict with proportionate independent review or explicit challenge and stopping criteria; the review is not automatically invalid.

| Reviewer | Role and decision rights | Relevant knowledge | Exposure, incentives, and capacity |
|---|---|---|---|
| [name] | [facilitator / decision-maker / expert / observer; any stop right] | [what they can assess] | [consequences they bear, possible conflicts, time and ability to act] |

Use exposure to understand incentives, not to rank a person's right to be heard. An independent reviewer with no personal downside can provide valuable evidence; a highly exposed reviewer can also have reason to hide a failure. Do not dismiss an objection because its author has no financial or reputational stake.

**Reward early, well-supported bad news.** Give appropriate credit and protection to someone who identifies that their own feature should change or stop. A monetary “self-kill” bonus is one reported practitioner idea, not a requirement. Reward the quality of evidence and judgment, including well-founded continuation, so the process does not encourage unnecessary cancellation. See the source limits in the reference notes.

## Worked example: code-review assistant

**Illustrative scenario.** The assistant provides advisory comments; it does not approve or merge code. A developer remains responsible for the merge decision. This example demonstrates assessment, not actual executed tests.

| Dimension | Evidence in the scenario | Assessment and action |
|---|---|---|
| Failure at scale | Baseline P95 is 30 seconds. A provider-rate-limit scenario reaches four minutes; expected volume is 1,000 PRs/day. | Record arrival rate and concurrency separately. Test queue limits, cancellation, and the fallback to manual review against the chosen waiting-time target. |
| Cost | At 8K billed tokens per review and an illustrative blended $0.003/1K tokens, inference is $24/day. Add $5/day embeddings and $15/week evaluation. | About **$934.29 per 30-day month**, or **$0.0311 per review** for 30,000 reviews, before omitted costs. A 3x inference-price case is about **$2,374.29/month**, or **$0.0791/review**. This is a partial cost estimate, not proven positive unit economics. |
| Latency | A separate, non-rate-limited 50-concurrent-request test has 90-second completion P95 and 45-second first-comment P95. | Compare both with the async workflow's targets. The four-minute degraded-provider result is another condition, not a conflicting measurement. |
| Monitoring | Proposed signals include ignored comments, rework, and weekly sampled review quality. | A proposed >20% zero-engagement alert needs a meaningful baseline and an alert/runbook drill before Pass. Logging diffs also needs appropriate data handling. |
| Adversarial | Two of 40 probes over-praise obfuscated malicious code. | Investigate exploitability and consequence; do not call this low severity from the count alone. Add controls, then retest before the exposed rollout. |
| Harness | One agent comments on PRs and uses repository tools. | Assess tool permissions, duplicate comments, state, and recovery. A single agent is not automatically Not applicable. |

The pre-mortem questions whether security-relevant review quality transfers to production. Candidate actions include testing that cohort and a restricted, four-week repository beta after the necessary controls pass. The duration is illustrative.

**Recommendation: no unconditional go.** Resolve or appropriately bound the adversarial findings, measure the missing readiness criteria, and test recovery before deciding on a scoped beta. General release requires its own supported disposition. Comparing these partial costs with an assumed $15 human review does not establish savings unless the reviews are comparable and displaced work, supervision, and rework are measured.

## Report and hand off

```markdown
## Stress Test Report: [feature and release scope]

Commitment: [customer, task, promise, population and exposure]
Test conditions: [versions, workload, duration, data, environment, limits]
Criteria and decision authority: [agreed thresholds, blockers, decision owner]

| Dimension | Status | Evidence and limits | Action, owner, date |
|---|---|---|---|
| Failure at scale | | | |
| Cost at volume | | | |
| Tail latency | | | |
| Monitoring | | | |
| Adversarial | | | |
| Agent/harness resilience | | | |

Cost: [current/planned/adverse scenarios; units, included and omitted costs]
Token usage: [measured distribution or explicit estimate]
Pre-mortem: [failure, warning signal, breaking assumption, next action]
Human response: [who can report, investigate, stop, and recover; capacity]
Recommendation: [GO / NO-GO / CONDITIONAL for the stated scope]
Conditions: [evidence needed, owner, date, rollback/stop trigger]
Residual uncertainty: [what this work does not establish]
```

Route only the unresolved work that warrants deeper treatment:

- `rtp-cost-model`: full cost and unit-economics analysis.
- `rtp-agent-risk`: risk proportionality, action authority, and stop mechanisms.
- `rtp-failure-modes`: specific failure mechanisms and cascades.
- `rtp-safety-by-design`: structural constraints informed by adversarial findings.
- `rtp-ship-decision`: release decision, conditions, and rollback ownership.
- `rtp-production-observability`: sustained detection and response after release.
- `rtp-fit-signal`: whether real users develop useful, warranted dependence; readiness alone does not establish fit.
- `rtp-judgment-guard`: effective review, challenge, and stopping conditions.
- `rtp-ai-portfolio-management`: reconcile scope and resources using the readiness evidence; schedule pressure cannot erase an exposed blocker.

## Final review

Check that the scope, consequences, criteria, and authority are explicit; each dimension has evidence or an honest exclusion/unknown; costs use consistent units; latency is tied to a workload; detection and recovery have been exercised where claimed; adversarial findings retain severity and retest status; and pre-mortem risks have actionable dispositions.

Do not repeat a rigorous test cycle without a relevant change or unresolved concern. Do not force production-scale testing into early desirability exploration, but retain safeguards for the experiment's actual exposure. Small user counts do not make consequential failures harmless.

**Trade-off:** testing consumes time, money, and release capacity in exchange for evidence that may prevent a larger loss or support a confident launch. The original 6–10-hour estimate describes a possible first pass; complex systems may require much more, and small changes less. Use honest ranges, such as $0.12–$0.18 per user per day when justified, instead of unjustified decimal precision.

End with the recommendation, its decisive evidence, the largest remaining uncertainty, and owned next steps. A visual showing the six dimensions beside the pre-mortem, with the human response underneath, is optional when it improves comprehension.
