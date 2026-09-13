# Dual-lens: concept guide

A shared AI product decision has consequences for both the business and the implementation. Express those consequences in language each audience can act on, then connect them explicitly. Some decisions need only a short translation; consequential commitments deserve a fuller check.

**Business explanation:** make the intended outcome, cost, risk, and decision clear to the people committing resources.

**Technical explanation:** connect stakeholder requirements to system behavior and measurable constraints, while showing how design choices affect the outcome.

The connection matters more than producing two polished paragraphs. A technically precise statement can still leave a business reader unable to decide. An ambitious commercial statement can leave engineers guessing about scope, cost, performance, or failure handling.

## Three ways translation goes wrong

**Precision without actionability.** An engineering explanation is accurate, but the approving stakeholder does not understand its implications. Approval then appears to mean more agreement than it does.

**Ambition without constraints.** "AI-powered personalization by Q3" sets a direction without specifying the relevant user outcome, cost ceiling, behavior, or quality expectations. The implementation team fills those gaps with assumptions.

**Simplification that changes the meaning.** "The model is pretty accurate" loses the meaning of an F1 score of 0.87 with materially weaker results on long-tail queries. The score, affected population, and decision implication should survive translation. A statement such as "12% variance" also needs a defined measure before reuse.

## Teaching cases

These examples are illustrative. The original guide did not identify evidence supporting its numerical results. Verify equivalent claims in the actual product before presenting them as measured outcomes.

### Explain unsupported answers to a board

Suppose a test finds unsupported or incorrect claims in 3–8% of responses across different query groups. Explain what counts as an error, the test population, and the consequences for the product. A confident tone does not establish factual support.

Do not translate a response-level rate into "3–8 out of every 100 users" unless the user-level exposure and calculation support it. A proposed mitigation target below 1% remains a target until evaluated. Even a passing test is evidence within its scope, not a guarantee that all future responses are correct.

The business decision is which uses and failure consequences are acceptable, what mitigation and review cost, and what evidence is needed to proceed.

### Explain retrieval-augmented generation

A retrieval system can find relevant material and provide it to the model when answering. Vector similarity is one approach; structured queries, keyword search, or a combination may also fit. An open-book analogy helps explain the idea, provided the reader understands that the system can retrieve the wrong material or misinterpret the right material.

The business implication is that knowledge can be maintained in external sources rather than relying only on model training. The organization still needs source ownership, access controls, refresh processes, and evaluation. A claimed 60–80% reduction in unsupported answers requires a specified baseline and study; it is not a general benefit of adopting RAG.

### Explain a two-second response requirement

First establish whether two seconds means acknowledgment, the first useful content, or the complete result—and whether abandonment was actually measured. The technical team can then evaluate retrieval, ranking, caching, model choice, context, output length, and streaming against that requirement.

A two-second target does not automatically rule out cross-document search or sophisticated ranking. Feasibility depends on the workload and implementation. Streaming can change when users start receiving content without proving that the complete answer meets the target. The bridge should expose the actual trade-off between responsiveness, completeness, freshness, quality, and cost.

## Reading connections

The original guide points to these influences, which are useful for further reading rather than proof that this particular framework has been empirically validated:

- Marty Cagan, *Inspired*: product work across business and engineering.
- Edward Tufte, *The Visual Display of Quantitative Information*: preserving meaning while making information understandable.
- Shreyas Doshi, writing on product sense: customer understanding and technical depth.
- Anthropic's technical research and public-facing safety material: examples of explaining related ideas to different audiences.

Inspect the relevant source before using an exact quotation or attributing a specific finding. The operating method is in [SKILL.md](SKILL.md).

## Recognize whether it worked

Business readers should understand the consequence and decision; technical readers should understand what to build or test. Both should identify the same scope and material uncertainty. A PRD that one audience finds compelling and another cannot act on still needs work.

Fluency in both domains can help credibility, but the practical test is whether the explanation supports compatible action. Confirm that with readers where possible. A self-review can find inconsistencies; it cannot stand in for stakeholder understanding or approval.
