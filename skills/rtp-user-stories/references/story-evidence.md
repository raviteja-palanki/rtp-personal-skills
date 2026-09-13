# Story evidence and review notes

## Primary guidance checked 13 September 2026

[Bill Wake's original INVEST article, 17 August 2003](https://xp123.com/invest-in-good-stories-and-smart-tasks/) presents Independent, Negotiable, Valuable, Estimable, Small, and Testable as qualities that support discussion and delivery. It explicitly permits real dependencies and describes details being developed together. The mnemonic is not an immutable requirements contract or a universal points scale.

[Wake's 2021 reflection](https://xp123.com/all-you-need-is-invest-no/) cautions that INVEST alone is insufficient and that estimates can be overused. [His discussion of testability](https://xp123.com/testable-stories-in-the-invest-model/) recognizes non-determinism, subjectivity, and research questions as issues to handle explicitly. Testable does not require one exact output for every probabilistic or creative task.

[Ron Jeffries, Card, Conversation, Confirmation, 30 August 2001](https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/) describes a story card as a reminder of a requirement, supported by continuing discussion and acceptance tests. This supports lightweight shared understanding and concrete evidence. It does not establish that the story is the last moment when ambiguity can be addressed.

The five-class scenario grid, three main work types, H/M/L labels, and worked enterprise cases are this library's practical synthesis. Their numbers are illustrative. They are not requirements attributed to the authors above.

## Inheritance review against the revised AI-PRD

The AI-PRD v1.2.1 main structure and its revised AI user-story companion are the reference for this pass. The full companion was re-read here. The key interface is **applicable, traceable requirements**, not every field filled on every card:

- Capability work needs actual behavior and authority rules; numerical confidence is conditional on a validated signal.
- Evaluation work needs valid tasks, labels, and measurements; one generated response passing is not evidence of general reliability.
- Fallback work needs useful, authorized alternatives and an unavailable-alternative state.
- Guardrail work needs the relevant failure, control, and response rather than generic safety language.
- Instrumentation work needs correct events, joins, and denominators; a logged key or score is not proof of the business outcome.
- Rollout work needs appropriate stage criteria and recovery; implementation order does not remove exposure dependencies.

Owner, monitoring, examples, and economics may link to shared requirements where appropriate. Updating a requirement needs reconciliation with dependent work; copying an obsolete threshold is not faithful inheritance.

## Desk-review checks

**A shared security upgrade has no next user-story ID.** Record the real risk and verification, rather than declaring it gold-plating.

**A spike ends with inconclusive evidence.** Document what was learned, what remains unknown, and the next decision. The timebox can be completed without pretending the research question is resolved.

**A team uses cycle-time history instead of points.** Keep its method if it supports the planning decision. H/M/L is optional, and point values do not transfer across teams.

**A rule scores generated writing with a graded rubric.** Define reviewer agreement, sample, and acceptance criteria while preserving grades; do not flatten useful quality evidence into an unexplained Boolean.

**An implementation slice has a working happy path but no required failure handling.** It may be ready for integration testing, but not the proposed user exposure. Complete the required safeguards or narrow the scope.

**A payment timeout follows an uncertain commit.** Reconcile the logical operation and use the actual idempotency/transaction design before retrying. A retryable status code does not make an external write safe by itself.

**An invoice exceeds the limit and the next approver is expired.** Follow the controlled policy, including a hold if no authorized route exists. The story must not invent escalation powers.

**An AI draft scores exactly 0.85.** Test the actual validated boundary rule and missing-score state. The score never authorizes a send or refund that the feature does not permit.
