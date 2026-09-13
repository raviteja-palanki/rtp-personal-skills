# Alignment Check — 15 diagnostic questions

Use these questions to gather evidence for the five links. The warning signs are reasons to investigate, not automatic failure verdicts. The stronger answers are examples of specificity, not prescribed decisions. All unnamed numerical scenarios are illustrative.

Assess a useful spectrum for each question and explain the placement. Do not substitute a score for the evidence. For a quick pass, choose at least one relevant question per link.

## Purpose

### 1. Can the sponsor explain the problem without relying on “AI” as the reason?

**Investigate:** “We are implementing AI for customer-support efficiency,” with no description of the work or its cost.

**Stronger evidence:** “Repeated questions consume about 30% of support time. We will test whether the FAQ and a suitable automated route can reduce that work while preserving resolution quality.” If 80% of questions are covered by the FAQ, establish that separately; a share of questions is not a share of staff time or proof of automatable volume.

**Spectrum:** a slogan people repeat → a concrete problem linked to each affected team's work.

### 2. Do affected divisions understand the change to their role?

**Investigate:** sales learns about the release from a customer; operations cannot explain the new handoff.

**Stronger evidence:** relevant teams have reviewed or tried the workflow, understand limitations, and know their responsibilities and escalation routes. Co-design may be useful where their knowledge changes the design.

**Spectrum:** informed only at launch → informed participation with clear operating responsibilities.

### 3. Why use AI rather than a simpler approach?

**Investigate:** the answer is only competitor behavior, available compute, or technical enthusiasm.

**Stronger evidence:** compare a rule-based or process baseline with AI on the intended task. A proposed split of 80% routine cases and 20% ambiguous cases is a hypothesis to test; ambiguity does not itself prove that AI can resolve the remainder well enough.

**Spectrum:** an aspirational preference → a task-specific, evidenced choice with limits.

## Strategy

### 4. Where does AI differentiate the offer, and where is it ordinary capability?

**Investigate:** every feature is labeled a moat or no comparison has been made.

**Stronger evidence:** identify the customer benefit, alternatives, and basis for a durable difference. A 2×2 can compare **customer value** with **distinctiveness** if useful; specify both axes rather than require an unexplained chart. “Explanation quality and warranted trust” may be a proposed advantage, but needs evidence in that market.

**Spectrum:** a wish list → a competitive thesis updated when relevant conditions change.

### 5. Which customer segments are ready for this change?

**Investigate:** “Everyone needs AI,” with no account of workflow, trust, access, or support needs.

**Stronger evidence:** segment by the capabilities and constraints the rollout requires. An enterprise may have a data team yet resist a workflow change; a small customer may be ready through a well-supported service. Company size alone cannot predict immediate adoption.

**Spectrum:** one-size-fits-all messaging → segment-specific value, onboarding, safeguards, and evidence.

### 6. Is the economic thesis complete enough for the commitment?

**Investigate:** costs and volume are deferred until after a consequential launch.

**Stronger evidence:** a model with pessimistic, base, and optimistic assumptions, comparable outcomes, and relevant operating costs. In the original example, 70% of tickets cost $0.02 each through AI and 30% cost $1.50 each through a human route:

```text
Blended listed cost = 0.70 × $0.02 + 0.30 × $1.50 = $0.464 per ticket
```

That does **not** yield the earlier $0.95 figure. Reaching $0.95 would require an additional $0.486 per ticket in specified costs under those assumptions. If $0.02 is only inference per call, include calls per resolution, supervision, retries, unresolved cases, and other operating costs before estimating blended cost or savings.

**Spectrum:** a benefit story → a tested model with explicit uncertainty and comparable outcomes.

## Capability

### 7. Is accountability clear and connected to actual authority?

**Investigate:** “Engineering owns it” without a responsible decision path, or one named person lacks the ability to act.

**Stronger evidence:** “Sarah owns this outcome, with defined authority over the relevant process and resources, and an effective escalation route for changes outside her remit.” Technical stewardship and business accountability may be distinct but must connect.

**Spectrum:** diffuse responsibility → identifiable ownership with practical decision rights.

### 8. Can the organization change course when evidence warrants it?

**Investigate:** the only reason to continue is that the project was already approved.

**Stronger evidence:** a named decision-maker can pivot, narrow, pause, or stop based on agreed evidence. Three months is one possible review point, not a universal deadline for proving value. Record what would trigger an earlier intervention.

**Spectrum:** commitment regardless of outcomes → explicit review and change conditions.

### 9. Can the organization support the required process change?

**Investigate:** the plan assumes the tool will sell itself and nobody has time for transition work.

**Stronger evidence:** relevant experience, learning support, pilot ownership, and allocated capacity. CRM rollouts or data migrations may provide transferable practices, but do not prove readiness for every AI consequence.

**Spectrum:** untested assumptions and no support → demonstrated or deliberately built change capability.

## Architecture

### 10. What happens when the AI gives a wrong answer or takes a wrong step?

**Investigate:** “It does not,” or a fallback exists only as an intention.

**Stronger evidence:** a tested detection, containment, and recovery path appropriate to the task. A proposed two-minute human escalation needs staffing and measured response capacity. Human corrections require review before they become evaluation cases, retrieval changes, or training data; they should not automatically retrain the model.

**Spectrum:** uncontained consequence → proportionate, tested recovery with known detection limits.

### 11. How will degradation be detected and acted on?

**Investigate:** the check cadence misses the time in which harm can occur, or the dashboard tracks only uptime.

**Stronger evidence:** relevant quality, latency, segment, and outcome measures; suitable sampling; tested alerts; and a responder who can act. A one-standard-deviation alert, as used in the old example, is not a universal signal: noise, repeated comparisons, and baseline variation can produce false alarms. Choose and validate detection rules for the setting.

**Spectrum:** weak or delayed visibility → fit-for-purpose detection and response, with limitations stated.

### 12. What data will be unavailable, delayed, or unsuitable?

**Investigate:** design depends on unconfirmed access or freshness.

**Stronger evidence:** an explicit map of unavailable competitor information, delayed signals, permissions, quality, and fallback behavior. A sentiment feed with a two-day delay cannot serve a requirement for current sentiment without a different design. Limited data access does not automatically imply that training a model on internal data is the appropriate solution.

**Spectrum:** wishful access assumptions → verified constraints reflected in the design.

## Systems

### 13. Who investigates a failure and chooses the response?

**Investigate:** “Probably engineering,” or a decision-maker named without coverage, access, or a runbook.

**Stronger evidence:** an available responder investigates the relevant evidence, applies authorized containment or rollback, and escalates decisions beyond their remit. Exercise the process; a written plan alone does not establish response capability.

**Spectrum:** ad hoc response → usable, tested incident ownership and escalation.

### 14. How do valid user corrections improve the service?

**Investigate:** corrections accumulate without review, or every correction is treated as ground truth.

**Stronger evidence:** validate and categorize feedback, investigate recurring or severe patterns, add appropriate regression coverage, and evaluate the proposed fix. The old “50 corrections trigger retraining” example is not a universal rule: one severe case may warrant action, while repeated noisy feedback may not justify retraining. Compare a candidate in shadow mode for suitable output measures; a user-facing A/B experiment answers different behavioral questions.

**Spectrum:** unused or unexamined feedback → validated findings linked to tested improvements.

### 15. Can a new team member understand and operate the system?

**Investigate:** critical rationale and recovery knowledge exist only in one person's memory.

**Stronger evidence:** current purpose, design decisions, dependencies, failure modes, evaluation results, limitations, monitoring, and runbooks. Use a model or system card when it fits, and distinguish documented training information from information the provider has not disclosed.

**Spectrum:** inaccessible tacit knowledge → usable documentation with owners and a maintenance process.
