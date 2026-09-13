# Natural-language and group interaction patterns

Natural-language UX, or **NLX**, uses language as an important control surface. The framing attributed in the original skill to Aparna Chennapragada treats words as interface elements that deserve the same care as buttons and forms. This is a design lens, not evidence that all GUI principles invert or that conversation should replace every structured control.

## Five inversions to consider

| Familiar GUI function | Language equivalent | Design choice |
|---|---|---|
| Buttons trigger actions | Requests and suggested prompts express intent | Show examples of supported work and what each action does. Interpret reasonable variations without promising to understand every phrasing. |
| Menus organize options | Conversation can reveal choices | Ask at material decision points; use sensible defaults for reversible preferences and show an override where useful. |
| Validation flags bad or incomplete input | A focused follow-up can resolve ambiguity | Ask for the missing detail instead of rejecting a request that can be clarified. Use structured validation when clearer. |
| Error dialogs report failure | A response can explain a limitation and recovery | Keep language consistent and useful. A persistent error view or modal may still be necessary for consequential state. |
| Visual affordances show available actions | Examples and follow-ups make language options discoverable | Combine language with accessible buttons, forms, or other controls when they help. |

### 1. Requests as action labels

At a useful entry point, show concrete examples such as “Summarize this contract” or “Find the liability clauses,” provided the product supports those tasks. Explain scope when the result could be mistaken for a professional determination.

A blank text box can work for experienced users or flexible exploration. For newcomers, relevant examples can reduce the effort of discovering what is possible. Do not assume every blank box causes failure or force the same onboarding onto everyone.

### 2. Conversation as navigation

“Export this” may require a format choice, but a known preference or reasonable default can avoid unnecessary turns. For a reversible export, “I exported it as a PDF” is appropriate only after it succeeds. If proposing rather than doing, say “I can export this as a PDF.” Make alternatives available without forcing a questionnaire.

For an action with material consequences, a guessed default may be inappropriate. Resolve the ambiguity or authorization that matters. Ask one clear question when possible; several independent inputs may be easier to provide together in a form.

### 3. Follow-up as validation

For “Email John about the deal,” use known context to identify the recipient and subject. If multiple plausible people or deals remain, ask a focused question. Mention specific candidate names only when they are actually known and appropriate to disclose.

Distinguish drafting from sending. A request to draft does not authorize delivery. A clear request to send can supply authorization without a second confirmation, subject to any applicable controls. The interface must show which state it is in.

### 4. Failure as a usable conversation turn

“I cannot access that file; reconnect the account or provide another copy” is useful when it reflects the actual failure. Do not claim an expired connection if the cause is unknown. Preserve work already completed and show whether retrying could duplicate an action.

Use ordinary language for the user-facing explanation, with diagnostic details available when useful. A technical code or a persistent banner can aid support and accessibility; the issue is unexplained jargon or missing recovery, not a blanket ban on system messages.

### 5. Discoverable language patterns

Offer relevant examples in onboarding, empty states, and suitable follow-ups. The earlier five to seven onboarding prompts and two to three follow-up suggestions are starting ideas, not required counts. Avoid crowding the interface or appending options after every completed request. Users should be able to state a different need in their own words.

## Four reusable patterns

### 1. Preview or restate consequential actions

Restatement can surface a misunderstanding and side effects. It is **not a substitute for an approval gate** and does not create an opportunity to abort if execution happens immediately.

For a cancellation that still needs approval, show a concrete pending action: “Cancel today's 3 pm Bain meeting? This will notify the attendees.” Provide approve/cancel controls and keep the action blocked until the decision arrives. If the user's explicit instruction already authorizes that exact cancellation and no new approval is needed, execute it and report the verified result. Do not ask again merely to perform a ceremony.

Name the actual meeting, recipients, amount, or data affected only from verified context. Keep unresolved ambiguity visible. For destructive actions, explain what can and cannot be recovered. For routine retrieval, restatement is usually unnecessary overhead.

### 2. Give a useful answer with optional depth

For a complex contract question, identify the material risks and give enough explanation to be useful, then offer detail on each. Do not provide only a teaser when the user requested a complete analysis or when essential limitations would remain hidden.

A simple question such as the time of the next meeting usually needs the answer directly. Choose the depth from the job, not a rule that every first response must be short.

### 3. Put structured choices inside conversation

Buttons or chips can make recurring alternatives easier: “Short summary,” “Risk review,” or “Negotiation points.” Use labels that describe the actual output. Keep keyboard and screen-reader support, clear selected state, and a free-language path where useful.

Three to five options were illustrative. The right number depends on the decision; do not turn every open-ended answer into a menu. An option that triggers an external action should say so rather than masquerade as a harmless request for detail.

### 4. Offer a structured view when precision benefits from it

A recurring meeting every other Tuesday at 2 pm except holidays may be easy to express in language and easier to verify in a calendar preview. Present the interpreted rule, timezone, holiday source, and affected dates before commitment when necessary.

Forms can be a primary interface, a confirmation view, or a fallback. Four parameters do not automatically make language unsuitable, and language does not automatically need to remain the primary mode. Consider the user's preference, error cost, precision, accessibility, and observed effort.

## Exploration and focused retrieval

**Focused retrieval** aims to answer a defined question or find relevant established material. **Exploration** deliberately broadens the frame, for example by drawing from semantically distinct clusters. These are goals, not fixed properties of search engines or a mandate for two separate screens.

Offer visible control over the goal where useful: a mode switch, a diversity option, grouped results, or a clarifying question. Keep provenance, quality, and access boundaries in both modes. Unfamiliar material can help expert recombination, but expertise also benefits from precise retrieval of familiar evidence. A relevant answer is not a defect merely because others receive it too.

For shared ideation, compare usefulness and diversity across people. A shared tool can encourage similar ideas, but shared models, shared retrieval, common constraints, and shared discussion are different mechanisms. If varying retrieval, make material differences inspectable and do not secretly give participants contradictory factual premises. A diversity view or an independent first pass may be more useful than arbitrary variation.

The local HBR source “Algorithms Trap Us in the Familiar. Can They Also Spark Breakthroughs?” is reported as an August 2026 discussion of the authors' exploratory implementation. The supplied note lacks a sample size. Treat ideation bubbles as a risk to investigate, not an inevitable result of a common tool or a universal finding about every recommendation system.

## A team at one keyboard

Group use changes the interaction unit. A single typist can become the unintentional editor of everyone else's views, but not every shared-screen session creates passive spectators.

Design for three questions:

1. **Whose perspectives are represented?** Let the group state relevant roles, objectives, and disagreements. Use role labels or other minimal context when names are unnecessary. Distinguish individual input from an agreed team decision.
2. **What role should the AI play now?** Researcher, critic, facilitator, or simulated stakeholder can be useful modes. Make their limits clear: a simulated customer is not evidence from a real customer.
3. **When should the group deliberate?** A pause before a consequential prompt, individual written views, or a facilitator checkpoint may help. One-question-at-a-time interaction is an option; it should not obstruct an authorized task that the group has already agreed on.

The local Rosani/Farri/Trabucchi/Buganza source reports 60 managers across 12 companies, five sessions over five months, transcript review and prompt templates, and a 30% rise in self-reported engagement. The supplied account has no full-arc control group. It supports testing ownership and deliberation, not claiming a causal 30% lift for a pause or prescribing a universal interface intervention. Clarify relative change versus percentage points before quoting the figure.

## Check the whole interaction

Evaluate whether the user finds a starting point, understands interpreted intent, can correct material ambiguity, sees action state, and recovers from failure. Test the full conversation: an inaccurate paraphrase can become a shared mistaken premise even when individual turns sound reasonable.

For critical claims, retain links to evidence and relevant earlier decisions. Mark assumptions separately from facts, and make meaningful corrections persist for the promised scope. Do not automatically treat the latest phrasing as ground truth or demand a fresh confirmation of every already-settled detail.
