---
name: problem-type
version: v1.0.1_latest
description: 'Diagnose whether a stuck AI initiative needs a technical fix, changes in how people work, or both. Use when problems recur, adoption remains low after improvements, or stakeholders disagree about the goal. Compare five signals, keep the diagnosis provisional, and sequence the technical and adaptive work. This is a separate question from whether the problem needs AI. Pairs with problem-ai-fit, alignment-check, adoption-launch, needs-guard, bias-spotter, and falsification.'
imports: []
---

# Identify the kind of problem

Before committing to another fix, identify what must change for the problem to improve. Some problems can be addressed through established expertise and implementation. Others require people to learn, adjust incentives, agree on responsibilities, or change how they work. Many initiatives contain both kinds of work.

Use this skill when a problem keeps returning, adoption remains low despite improvements, or the team disagrees about the underlying goal. Keep the diagnosis brief when the cause is already clear. During an incident, take necessary containment action while investigating the broader causes.

**Pairs with:** `problem-ai-fit` for whether and how AI fits the problem; `alignment-check` for organizational dependencies; `adoption-launch` for putting change into practice; `needs-guard` for affected human needs; `bias-spotter` and `falsification` for testing the diagnosis. Read [CONCEPT.md](CONCEPT.md) for conceptual background and additional illustrative cases.

## The distinction that changes the response

The technical/adaptive distinction comes from Ronald Heifetz's leadership work. Use it to choose appropriate work and ownership, not to assign blame or declare that a problem cannot be solved.

| Dimension | Technical work | Adaptive work |
|---|---|---|
| What must change | A component, process, or implementation with an identifiable remedy | Beliefs, incentives, roles, relationships, capabilities, or ways of working that need learning and negotiation |
| How progress happens | Diagnose the fault, apply expertise, implement, and verify | Establish the direction and constraints, involve affected people, test changes, and learn from their effects |
| Role of authority | Can authorize resources and assign the work; implementation still needs verification | Can create conditions and accountability, but cannot produce trust or agreement merely by issuing a mandate |
| Examples | A slow query, missing access, a known integration defect | Conflicting definitions of success, fear of lost competence, or incentives that make the proposed behavior unattractive |

Technical does not mean easy, permanent, or free of resistance. Adaptive does not mean that implementation is irrelevant or that every concern requires months of discussion. Use the distinction to identify the work the current proposal has left out.

This is a different axis from `problem-ai-fit`. A suitable AI use case can still depend on organizational changes, while a problem that does not need AI can contain adaptive work.

## Begin with the observed problem

State the problem, affected people, desired outcome, and previous attempts. Separate observed behavior from your interpretation of its cause. Use the context already supplied and ask only for information that materially changes the diagnosis.

For example, "15% of the intended sales group uses the tool against an assumed 60% target" describes an adoption gap. "The reps do not trust AI" is a hypothesis that needs evidence.

Follow the requested format and depth. The shared `UNIVERSAL-SKILL-PROTOCOL.md` is at the AI-PM source root or plugin root; the method below is usable without it. An inline classification can be sufficient for a quick check.

## Examine five signals

For each signal, record the evidence and mark it **technical**, **adaptive**, **mixed**, or **unclear**. Recurrence or low adoption alone does not establish the cause.

| Signal | Questions to investigate | Possible adaptive evidence | Alternative explanations to check |
|---|---|---|---|
| 1. Recurrence after fixes | Did the fix address the actual failure, and was its effect verified? | The required behavior remains unattractive or untrusted after a relevant technical improvement | An incomplete fix, drift, poor instrumentation, or a new technical fault |
| 2. Cycling through solutions | What stayed constant across the model, interface, or channel changes? | The same incentives, fear, or ownership conflict remains | Every solution may share the same bad data, workflow mismatch, or access problem |
| 3. An explicit or unexplained barrier | Can the team identify and measure the barrier? | Interviews or observed behavior reveal conflicting goals, norms, or concerns | An unmeasured technical defect or missing usability information |
| 4. The effect of authority | What changed after a mandate, and what did not? | People comply under monitoring but cannot see value or exercise needed judgment | The mandate may not provide access, time, training, or a workable process |
| 5. Agreement on the remedy | Do people disagree about implementation, or about the outcome and acceptable trade-offs? | They hold materially different definitions of fairness, value, responsibility, or success | Experts may still be investigating a difficult technical problem |

A three-of-five vote can serve as a rough prioritization aid: three reasonably supported signals in one direction suggest where to start. It is not a validated classifier. Do not turn unclear observations into votes or let a majority hide a consequential requirement in the other category. Classify the problem as **both** when verified technical and adaptive dependencies matter, even if more signals point one way.

Keep evidence strength separate from the classification. "Primarily adaptive, with limited interview evidence" is more useful than a confident label based only on symptoms.

## Sequence the work when both are needed

Identify what must happen before another activity can succeed. Adaptive work often defines a requirement that the technical team needs, but technical evidence or a safe prototype may also enable the adaptive conversation. Some activities can proceed together. Make the dependencies explicit.

Consider a model producing disputed recommendations:

- The technical team may need to investigate data, measures, error patterns, and available constraints.
- The organization may need to agree on the intended outcome, affected groups, accountability, and acceptable trade-offs.
- Applicable obligations still need appropriate review; agreement among stakeholders does not establish that a design is fair or compliant.

Avoid building against an undefined requirement and discovering the disagreement only at deployment. Equally, do not delay a known protective fix while waiting for complete organizational agreement. Define enough shared direction to make a bounded technical test useful, then revisit the decision with evidence.

A six-week conversation is one possible planning choice, not a required duration or a promise of success. Choose the timebox from the decision and its urgency. When activities are independent, start longer-lead work early and coordinate the results.

## Turn the diagnosis into action

1. State the observable problem and the intended outcome.
2. Review all five signals and the competing explanations.
3. Give a provisional diagnosis: technical, adaptive, or both. Explain the evidence and material uncertainty.
4. If both, show which activity unlocks another and which can proceed independently.
5. Assign the appropriate work: a technical remedy and verification plan, an adaptive learning/change plan, or both.
6. Set a decision point and an observation that could disprove the diagnosis. Name the next action and responsible owner without inventing a date or commitment.

Useful diagnostic questions include when the problem first appeared, what each attempted fix actually changed, whether the team agrees on success, and what currently prevents progress. Distinguish "the solution is known but unfunded" from "we disagree on the result we are trying to achieve."

Two common thought experiments need care. Replacing the team while keeping the process and technology does not isolate a technical or adaptive cause; it changes knowledge and relationships as well. Likewise, an expert with unlimited resources is an imagination exercise, not evidence. Use these questions to expose assumptions, not as classification rules.

## Worked example: a sales recommendation tool

This is a constructed teaching case. The percentages and timeframes are assumptions, not reported company results.

Assume a tool improves its measured accuracy from 80% to 96% and later 99%, while adoption remains around 15% against a 60% target. Sidebar, chat, and email versions all see limited use. A mandate raises observed use from an assumed 5% to 15% before it plateaus. For comparison, a mandate might raise use from 10% to 40% in another hypothetical population; that is a separate example, not part of this time series.

The five signals suggest investigating adaptive causes, but do not prove them:

- Repeated technical improvements did not resolve the observed adoption gap.
- Several channels failed while some conditions remained unchanged.
- The team has not established why people avoid the tool.
- A mandate changed use without explaining whether people find it valuable.
- Engineering, sales, and product propose different causes.

Interview and observation could reveal fear of embarrassing recommendations, a commission conflict, threatened competence, or a poor workflow. Check the actual recommendation quality and access conditions as well. A bad experience can affect trust, and subsequent reliable performance may be part of rebuilding it.

If the evidence supports an adaptive explanation, combine a credible technical baseline with practical changes:

1. Listen to affected reps and identify the specific concern.
2. Explain the role of the system and preserve meaningful human judgment.
3. Use a bounded, opt-in pilot where appropriate and examine results against agreed measures.
4. Recognize well-founded overrides, so people can see that sound judgment matters.
5. Correct remaining technical problems and reassess whether the combined approach changes the completed work.

Timebox learning and name the signal that would make another listening period unjustified. Neither "build a better model" nor "run six more weeks of conversations" should become an answer that cannot be challenged.

## Connect the diagnosis to the rest of the library

| Next skill | What it adds |
|---|---|
| `rtp-problem-ai-fit` | Whether the bottleneck needs AI and whether AI should be a bounded decision engine or a supporting helper |
| `rtp-alignment-check` | Which link among purpose, strategy, capability, architecture, and systems is misaligned |
| `rtp-adoption-launch` | How to run the change with affected groups, phases, ownership, and measures |
| `rtp-needs-guard` | Whether competence, autonomy, or belonging is affected, and what evidence supports that interpretation |
| `rtp-bias-spotter` | Whether action bias favors an unnecessary build, or whether the adaptive label has become a comfortable way to avoid technical work |
| `rtp-falsification` | A precommitted observation and decision point that could overturn the diagnosis |

The research connection to `problem-ai-fit` references q2-11, MIT Sloan Management Review, Amorim, Saleh, and Sundling, 6 May 2026. Its source substance belongs in that skill; the internal card identifier is provenance, not a replacement for a complete citation.

## Check the diagnosis before relying on it

- The problem describes observed conditions rather than assuming a solution or blaming a group.
- All five signals were considered, with uncertainty preserved.
- Technical alternatives such as missing access, poor communication, usability, or incomplete fixes were examined where relevant.
- The diagnosis names the work required and, for a mixed problem, its dependencies.
- Owners, evidence needs, and a next decision point are clear.
- There is a specific reason to reconsider the diagnosis or stop further analysis.

The trade-off is time spent diagnosing versus the cost of another misdirected intervention. A one-to-two-week diagnostic period and one-week correction window are possible planning assumptions, not defaults. A clearly known defect may need immediate action; a disputed operating model may need a longer process. State confidence from the actual evidence rather than assigning "High" automatically.

If a visual helps, show the five signals along a technical-to-adaptive spectrum, retain mixed or unclear findings, and add the dependencies beneath it. Use the relevant diagram skill when available. Do not add a diagram that only repeats an already clear table.

**Version 1.0.1, 13 SEP 2026.** Preserves the technical/adaptive distinction, five signals, sequencing method, sales example, diagnostic prompts, library connections, and trade-off review. Clarifies that recurring failure is a signal to investigate, a majority vote is provisional, and technical and adaptive work can both matter. The concept companion labels unsupported numerical cases as illustrative and retains their mechanisms.
