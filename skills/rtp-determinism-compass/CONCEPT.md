# Determinism compass: concept guide

An AI product combines operations with different requirements. Some must return an exact value; some must reach a consistent substantive decision; others can produce several useful answers. Choose an implementation and evaluation method that fits each operation, and define what happens when one component hands work to another.

**For a business reader:** identify where consistency protects the outcome, where variation adds value, and what the controls and review will cost.

**For a technical reader:** map components to deterministic code, model inference, or hybrid execution; specify input and state assumptions, output invariants, acceptable variation, tests, and recovery.

Deterministic execution means the same relevant inputs and conditions produce the same output. It does not mean the output is right. A probabilistic model can produce a correct answer to a task with one required answer, and several different outputs can all meet a task's requirements. The operating method is in [SKILL.md](SKILL.md).

## Three traps

**Using AI where a simple check suffices.** Checking whether a string contains an `@` character can use ordinary code. That check alone does not establish that an email address is valid or deliverable. Define the real requirement before choosing either a rule or a model.

**Using rules beyond their useful scope.** A large intent decision tree may become hard to maintain and miss relevant language. Compare it with model-assisted alternatives using actual coverage, errors, costs, and maintenance effort. Complexity does not prove that AI is required.

**Leaving the handoff undefined.** Specify which inputs cross the boundary, what the receiver may assume, how invalid or uncertain results are handled, and who owns recovery. An otherwise useful model can fail the product if its output is trusted beyond its demonstrated meaning.

## Three illustrative component boundaries

These cases are constructed design examples. Their numbers are not external mandates or validated operating thresholds.

### Transaction monitoring

A rule can identify transactions above a specified amount; a $10,000 value here would be an illustrative internal threshold, not a universal regulatory rule. A model can help identify patterns that need investigation. The system still needs defined policies, appropriate domain review, and accountable decisions.

Do not turn a model score above 90% into an automatic account-freeze policy by default. A score's meaning, error costs, authority, and intervention process must be established separately. This case illustrates the difference between detecting a pattern and being authorized to act on it.

### Content moderation

A blocklist can match known prohibited entries, subject to normalization, list freshness, and evasion. Deterministic matching does not guarantee zero missed prohibited content. A model can assess novel content against a defined policy, with review and appeal paths matched to the consequences.

A severity scale of 1–10 could route scores 1–3 to no action, 4–7 to review, and 8–10 to removal in a hypothetical tested policy. Those bands need definitions and evaluation; severity is not the same as confidence. Assess both missed violations and unwarranted restrictions.

### Customer support routing

A verified password-reset intent can enter a standard flow. A keyword alone may not establish that intent. Ambiguous requests may benefit from model-assisted classification and urgency assessment.

An internal policy might route customers with three escalations in thirty days or account value above $100,000 to a human regardless of model score. Those are illustrative business choices requiring justification. The essential boundary is that a model's interpretation cannot silently override an explicit routing or permission rule.

## Reading connections

The source guide connects this idea to Ravi's CONTEXT framework, Anthropic's *Constitutional AI: Harmlessness from AI Feedback*, bounded contexts in domain-driven design, and Google's *Rules of Machine Learning*. Use these as reading connections, with the following distinctions intact:

- CONTEXT organizes production concerns; inspect the actual framework before assigning one execution mode to an entire layer.
- Written constitutional principles or model training guidance are not equivalent to deterministic runtime enforcement. A principle can guide behavior without guaranteeing it.
- A bounded context clarifies the meaning and ownership of a domain; it does not itself classify model execution.
- Choosing whether to use machine learning requires evidence about the problem and alternatives, not an "AI first" or "rules only" identity.

## Know whether the boundary is useful

The component map should explain what must be exact, what may vary, how correctness is judged, and which action is permitted. It should make debugging and recovery possible without demanding pointless textual sameness. Check the completed workflow, because local consistency and passing schemas can still produce a wrong final result.
