# Falsification: concept guide

A useful product claim explains what evidence would count against it. Before committing substantially, decide how to collect that evidence and how it would affect the next decision. The point is to learn and act, including stopping when warranted, rather than protect a proposal from every possible result.

**Business explanation:** define failure conditions and the response before momentum makes them difficult to acknowledge.

**Technical explanation:** map a hypothesis to suitable measures, data, evidence windows, and decision rules. Some questions use formal statistical hypotheses; others use observable events or structured qualitative evidence. Not every product test needs a null-hypothesis significance test.

This approach draws on Karl Popper's account of falsifiability. A product experiment rarely disproves a broad probabilistic claim with one counterexample. Interpret results within the test's assumptions, uncertainty, and scope.

## Three ways a claim becomes hard to challenge

**Anecdotes shield the aggregate.** Selected successes can hide a low success rate or severe failures. Show the relevant distribution and selection process.

**The goal moves after results arrive.** The team moves from accuracy to satisfaction to engagement until something improves. Learning that a different measure matters is legitimate; silently presenting it as confirmation of the original claim is not.

**More time is always the answer.** Better data, prompts, or models may help, but the proposal needs a bounded test of that explanation. State what the additional work is expected to change, what it costs, and when to decide whether it did.

## Three illustrative cases

The source guide did not identify company records for these examples. Treat their numbers and events as constructed teaching scenarios.

### Summaries that add work

Suppose use grows after launch, but a six-month study finds that readers repeatedly return to the original because the summary is insufficient or untrusted. More usage has not established time saved.

A measure of completed-task time and quality, including verification and re-reading, could reveal the problem earlier. It cannot be claimed that a particular month-two review would certainly have caught it without evidence about that test.

### A recommendation system with a repairable failure

Suppose the team agrees to investigate click-through below 15% for two consecutive weeks and consider a rule-based fallback below 10%. A 12% reading in week three is an early alert; it satisfies the two-week condition only if the preceding week also qualifies. Immediate investigation may still be sensible under a separately stated alert policy.

The team finds a freshness problem, repairs it, and subsequently observes 22% click-through. That improvement is evidence worth examining, not proof that the repair alone caused it. The case shows why a failure condition can trigger investigation or repair rather than automatic termination.

### A cost rule with consistent units

At an assumed $0.002 per request, ten million requests per day cost $20,000 per day before other costs. Ten million **tokens** cannot be multiplied by a per-request price without knowing requests and token use; the source guide mixed those units.

A proposed $5,000 daily spend threshold sustained for thirty days would be a business decision rule, not a universal budget policy. Include earlier spend controls where necessary so the team does not have to incur a month of unacceptable cost merely to prove it is unacceptable. Measure total cost and value at the relevant volume.

## What makes pre-commitment useful

Choose measures that reflect the outcome and its guardrails rather than selecting easy conditions that cannot plausibly trigger. Give each condition an observation window matched to the decision, and record what to do when the evidence is inconclusive.

For a shared investment, discussion with the people who must execute the response can reveal missing authority, capacity, or disagreement. A signed brief is evidence of agreement only if people actually agreed; operational readiness still needs to be established. A solo reversible experiment can use a much lighter record.

When refining the hypothesis, revise its counter-test at the same time. Preserve the previous claim and result. A claim that keeps adding exceptions while retaining a test of its original narrow wording becomes less accountable as it gets longer.

## Reading connections

- Karl Popper, *The Logic of Scientific Discovery*: falsifiability and the limits of confirmation.
- Nassim Nicholas Taleb, *The Black Swan*: asymmetry between observations supporting a universal claim and a counterexample challenging it.
- Teresa Torres, *Continuous Discovery Habits*: testing consequential assumptions.
- Anthropic's red-teaming research: adversarial evaluation of systems, distinct from treating a generated skeptical persona as evidence.

Inspect the appropriate source before using an exact quotation or empirical attribution. [SKILL.md](SKILL.md) contains the operating method; [counter-tests.md](references/counter-tests.md) contains the numerical examples and the research-led refinements.
