# Invisible Stack — Concept Guide

The user sees an interface and an outcome. Behind them, a system supplies context, selects models and tools, manages state, enforces boundaries, and handles failures. Production quality depends on how those parts work together. The model can be a decisive constraint; so can the infrastructure and workflow around it.

## Two definitions

**Business:** the operational capabilities that help an AI feature deliver a useful, dependable outcome under actual use. They include data quality, access, coordination, response, and maintenance as well as model performance.

**Technical:** the context and execution architecture around inference: instructions, retrieval, context assembly, state, tools, routing, validation, output contracts, caching, and observability. The seven CONTEXT categories organize responsibilities rather than prescribe seven services.

## Three traps

**Model fixation:** choosing a new model without checking whether the current system supplied the evidence or tools the task required. The opposite error is assuming the model is adequate without testing it.

**A hand-built demo mistaken for a production system:** a researcher supplies the right documents, remembers state, chooses tools, and cleans up the result. Automating those responsibilities changes the system being evaluated even if the model stays the same.

**A platform chosen by its model catalog alone:** missing retrieval, evaluation, access, or operations capabilities later become unplanned work. Compare the platform with the complete task and the team’s ability to operate it.

## Illustrative examples

- Two support products use the same model but report 70% and 30% resolution. Their context, tools, users, task mix, and measurement may differ. The figures prompt investigation; they do not isolate context as the cause. This is not a verified pair of companies.
- A knowledge assistant grows from 500 to 5,000 documents while satisfaction falls from 78% to 34%. Investigate retrieval, conflicting content, freshness, access, user mix, and load. More documents need not degrade search, and tuning a similarity threshold is not automatically the remedy.
- A manually assembled demo scores 95% while production scores 65%. Reproduce matched tasks and inspect each responsibility transferred from a person to software. Manual work is not automatically perfect, and keyword retrieval or deterministic routing is not inherently inferior.
- A document product’s retrieval precision rises from 50% to 81% while satisfaction rises from 65% to 82% after chunking and embedding changes. These hypothetical numbers illustrate a possible upstream improvement, not proof that retrieval was the only problem or a formula relating precision to satisfaction.

## Intellectual connections

Ravi’s CONTEXT framework provides the organizing vocabulary. Sculley and colleagues’ technical-debt work examines system dependencies, feedback, entanglement, and maintenance costs; it does not show that ML failures are exclusively infrastructure problems. Chip Huyen’s production-systems work and Simon Willison’s context-engineering writing are related perspectives, not external validation of a fixed 10/90 allocation. Karpathy’s observation about English as a programming language likewise does not quantify the work split.

The useful diagnostic question is: what evidence would distinguish a model limit, a missing dependency, and a failure of interaction between adequate components? Use the [skill](SKILL.md) for the audit and the [measurement reference](references/measurement-and-evidence.md) for assumptions and source limits.
