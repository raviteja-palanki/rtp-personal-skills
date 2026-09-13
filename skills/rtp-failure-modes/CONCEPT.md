# Failure Modes — Concept Guide

A system can complete a request successfully at the software level and still fail the user's task. The result might be incomplete, false, stale, biased, or inappropriate for the action it informs. That problem exists in deterministic software too; generative AI adds ways to produce plausible-looking unsupported content without an explicit error signal.

Failure analysis makes those possibilities concrete enough to test and address. It does not promise to identify every future failure or reduce every consequence to money.

## Business and technical meaning

**For the business:** identify who is affected, how the failure changes their outcome, how long it could persist, and what prevention or recovery is justified. Include user harm, denied service, lost time, operational burden, and nonfinancial consequences.

**For engineering:** connect a specific failure condition to components, inputs, permissions, state, detection, response, and validation. Test semantic correctness and intended outcomes alongside structure, uptime, and latency.

The central distinction is between **successfully producing an output** and **successfully completing the job**. A current-looking citation can refer to no real source. A well-formatted brief can use stale data. A fast response can be wrong, and a correct response can arrive too late.

## Three recurring traps

**Accuracy alone:** compare task quality with end-to-end time, cost, coverage, and failure consequences. The earlier 95%-accurate/4-second versus 88%-accurate/500-ms example does not establish which product users prefer. The right comparison depends on what the errors and delay cost in the task.

**Untracked change:** model versions, prompts, retrieval data, tools, policy, and user mix can all change behavior. Keep change records and regression checks. Do not assume every provider changes a pinned model silently, or that a model swap is the only possible cause of drift.

**Aggregate performance:** a strong overall score can hide poor results for an important task or group. Check relevant segments, label quality, coverage, and the decision's fairness requirements. Representative sampling and targeted difficult-case testing answer different questions and may both be useful.

## Four illustrative cases

### 1. Fabricated legal citation

A legal-research draft contains a plausible-looking case reference that cannot be verified. Its familiar format may make the defect harder to notice, but the citation is not inherently undetectable. Check that the case exists and that the relevant holding, jurisdiction, date, and quoted passage support the actual claim.

A database lookup can verify existence; it does not automatically validate the entire legal argument. Define behavior when the database is unavailable or coverage is incomplete. The older guide's invented case name, fixed 200-ms verification cost, and unsourced liability narrative are not a documented incident. Use a clearly fictional example unless a real case has been sourced.

### 2. Tone changes in support

A team changes its model or prompt and factual accuracy remains similar, but the new replies violate the product's communication standards. A task-specific tone rubric and representative review may detect the change that a factual test misses.

The older Claude 2-to-Claude 3 story, named customer class, and attributed complaint were unsourced. Treat this as a hypothetical model/prompt-change case rather than a verified provider incident. Record what actually changed, compare suitable versions, and test whether the effect comes from the model, prompt, context, or another factor. A daily cadence is an option, not a guarantee of adequate monitoring.

### 3. Long documents create a cost tail

A document feature usually handles short contracts but occasionally receives much longer material. Measure the cost distribution, retries, tool work, and processing approach; token use does not always track page count or scale linearly with it.

If 5% of documents cost ten times as much as the other 95%, that group contributes about **34.5%** of total cost, not 40%. If “ten times” refers instead to the overall mean, its share is **50%**. The denominator changes the answer. See the [calculation notes](references/examples-and-calculations.md).

Possible responses include an informed document limit, selective analysis, chunking, or a priced extended workflow. Analyzing only the first fifty pages is not an acceptable silent fallback for a task requiring full-document coverage. Show what was processed, what was omitted, and what that means for the conclusion. The old 35% cost saving and 95% retained utility were hypothetical outcomes, not observed benefits.

### 4. Unequal hiring-screening outcomes

A screening model trained on historical outcomes may reproduce or amplify a problematic pattern. Investigate task validity, data, criteria, group-level outcomes, uncertainty, and the effect of the full workflow. An aggregate accuracy score alone does not establish fairness.

The earlier claim of a statistically significant 27% lower callback rate for women was unsourced and is not a verified study. Use the example to explain what must be measured, not to assert that outcome occurred. A disparity does not by itself isolate the cause or establish a legal conclusion. Select remediation with appropriate domain and legal expertise; do not prescribe demographic quotas or “diversity constraints” as a generic technical fix.

## How the disciplines connect

Failure Mode and Effects Analysis provides a useful lineage for identifying modes, effects, causes, and treatments. The standard cited by the old guide is **IEC 60812:2018**, not “ISO 60812.” It covers hardware, software, processes, human actions, and interfaces; its generic scope is not a substitute for application-specific safety requirements. [IEC primary description](https://webstore.iec.ch/en/publication/26359).

Production-observability work associated with Aman Khan and Arize, and Eugene Yan's writing on evaluation, informs the distinction between offline scores and operational behavior. Verify the exact primary article before attributing a specific numerical prescription to either practitioner.

Anthropic's **4D AI Fluency** framework concerns Delegation, Description, Discernment, and Diligence. It is not a four-axis production failure taxonomy. Discernment and diligence are relevant influences, while this skill's register and controls need their own evidence. [Primary framework](https://www.anthropic.com/ai-fluency/overview).

Review both local steps and the whole task. Schema validation, a source list, a human sign-off, and a complete log each do a particular job; none should receive credit for a different check it does not perform. Maintain the failure register as the product, environment, and evidence change.
