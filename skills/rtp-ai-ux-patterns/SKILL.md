---
name: rtp-ai-ux-patterns
description: Interface patterns for AI products where output confidence varies. Uncertainty communication ladder, progressive disclosure, trust calibration, AI-specific loading states, and error states. Use when designing AI features or evaluating why users over-trust or under-trust AI output.
---
# AI UX Patterns: Communicating Uncertainty Without Destroying Trust

## DEPTH DECISION

You are designing an interface where the system's confidence varies. Sometimes the AI is 95% sure. Sometimes 60%. Sometimes it doesn't know at all. The question: how do you show the user the AI isn't sure without making them lose faith in the system?

**Who uses this:** Product designers building AI features. PMs deciding how much AI to expose to users. Anyone shipping features where AI output quality varies.

**Skip if:** The AI component of your feature is deterministic (always produces the same output for the same input) — use standard UX patterns instead.

## DELIVERABLE FORMAT

Before starting, ask: Word Document, Presentation, or Both?
Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

## GROUNDING (Before Starting)

Before designing uncertainty patterns, answer:
1. What confidence range does the AI actually operate in for this feature? (e.g., 55-90%, not "it varies")
2. Who is the user — expert (catches errors) or novice (trusts output)?
3. What is the cost of a wrong answer? (Annoying vs. dangerous vs. compliance-critical)
4. Have you measured actual AI accuracy on this task, or are you estimating?

If you can't answer #1 and #4, run uncertainty-research first. Designing confidence UI without knowing the real accuracy distribution leads to miscalibrated trust — which is worse than no confidence signal at all.

---

## THE TRAP

**Trap 1: False certainty.** You hide the uncertainty. The AI is wrong 30% of the time. Users don't know. When it fails, trust collapses catastrophically — and takes months to rebuild.

**Trap 2: Uncertainty paralysis.** You show a raw confidence score (0.72). The user stares at it. Doesn't know what to do. Feels worse than just giving them a clear answer. Numeric confidence without context is worse than no confidence signal.

**Trap 3: Uncanny valley of assistance.** Too helpful → users assume it's omniscient and get angry when it's wrong. Too cautious → users think it's useless and ignore it.

**Trap 4: Mixing modalities badly.** Chat interface for high-stakes decisions, inline suggestions for low-stakes ones. Users can't build a consistent mental model of when to trust which interface.

**Trap 5: Error states that blame the user.** "I couldn't understand that." Translation: "You explained it wrong." Users stop trying.

---

## THE PROCESS

### 1. Uncertainty Communication Ladder

For each AI decision, place it on this ladder based on confidence level AND error cost:

**Level 1: Assertion**
"The answer is X."
- Use when: Confidence > 90%, stakes are low (autocomplete, search suggestion)
- Cost: Users assume you're always right. One wrong answer damages trust.
- Example: Search autocomplete. Typo correction.

**Level 2: Confidence Signal**
"The answer is X. I'm pretty sure."
- Use when: Confidence 70-85%, user needs signal to decide next step
- Cost: Numeric confidence scores mean nothing to most users. "82%" is uninterpretable.
- Better: Verbal confidence. "Very likely" beats "82%." "Probably" beats "0.78."
- Example: Spam detection. "This looks like spam (high confidence)."

**Level 3: Alternative Ladder**
"The answer is X, but it could also be Y or Z."
- Use when: Confidence 60-75%, meaningful alternatives exist
- Cost: You're asking the user to pick. Increases friction. Use only when alternatives matter.
- Example: Email category is "Work" but could be "Billing." Let the user confirm.

**Level 4: Question Back**
"I'm not sure. Can you help me understand better?"
- Use when: Confidence < 60%
- Cost: User now has to do the work the AI couldn't. Use sparingly — this breaks flow.
- Example: "I'm not sure what you're looking for. Is it related to your previous search?"

**Level 5: Abstain**
"I can't help with this."
- Use when: Confidence < 40% OR error cost is high regardless of confidence
- Cost: User gets no help. But wrong help at high stakes is worse than no help.
- Example: Sensitive decisions (legal, medical, financial). Regulated decisions.

---

### 2. Progressive Disclosure Pattern

Don't show the user the full complexity of the AI upfront. Layer it.

**Layer 1: Simple output.** "Article A is the most relevant."
- Show only if confidence > 75%.

**Layer 2: Why? (optional reveal).** User clicks "Why this?"
- Show relevant keywords, sources, reasoning fragments.

**Layer 3: Alternatives (deep reveal).** User clicks "Show other results."
- Show ranked list with confidence signals (verbal, not numeric).

**Layer 4: Adjust (power user).** User clicks "Customize."
- Show filters, weights, confidence thresholds.

This keeps the interface simple for 80% of users who trust the AI. Advanced users can dive deeper. The mistake is building Layer 4 first and making everyone use it.

---

### 3. Modality-Specific Patterns

**Inline suggestions (low stakes, high confidence):**
- Use confidence silently — just rank by it. Don't surface the number.
- Show top option as the assertion. Alternatives available via subtle affordance (chevron, underline).
- Example: Gmail autocomplete, IDE code suggestions.

**Chat interface (medium stakes, mixed confidence):**
- State uncertainty directly in natural language prose.
- "I found three relevant articles. The first one directly answers your question."
- Offer alternatives conversationally. "Would you like to see the other two?"
- Example: Customer support chatbot, research assistant.

**Dedicated decision interface (high stakes, explicit confidence):**
- Show confidence explicitly with context that makes it interpretable.
- "Based on 2,847 similar cases, 91% ended with outcome A."
- Provide a "I disagree" or "Override" button. Capture that feedback.
- Example: Risk assessment, fraud detection, hiring recommendations.

---

### 4. AI Loading States

Generic UX guidance: show a spinner. AI-specific reality: the spinner destroys trust because it makes the process invisible.

**The insight:** Users who see *what the model is doing* during loading trust the output more than users who see a generic spinner. Process transparency reduces the "magic black box" feeling that makes errors feel betrayals rather than mechanical failures.

**Redesign loading states for AI:**

| Wait time | Generic (wrong) | AI-specific (right) |
|---|---|---|
| < 500ms | No loading state | No loading state |
| 500ms–2s | Spinner + "Loading..." | "Thinking..." — neutral, process-aware |
| 2–5s | Spinner + "Please wait" | Process steps: "Searching documents... Analyzing context... Drafting response." Updates every 1-2 seconds. |
| 5s+ | Full spinner | Full process: "Analyzed 80% of sources. Generating response..." Give user permission to leave and return. |

**What to show during 2-5s AI waits:**
- "Searching [documents/your history/similar cases]..."
- "Analyzing the context..."
- "Generating response..."
- "Reviewing for accuracy..."

Each step tells the user something real is happening. When the output arrives, users have a frame for what it is — not magic, but a process. This makes errors feel mechanical (the process made a mistake) rather than broken (the thing I trusted failed me).

**Anti-pattern:** 8-second spinner with no update. Users assume it broke and refresh — triggering a second inference call that duplicates cost and increases frustration.

---

### 5. Error States for Probabilistic Failures

Traditional software: "Error 404 File Not Found." Clear cause. User knows what went wrong.

AI software: "I couldn't generate a response." Users don't know: was it a hallucination? A timeout? Unsafe content? A context limit? The ambiguity makes them feel incompetent — not the AI.

**For wrong answers or low-confidence outputs:**
- Don't say "I don't know." (User thinks the AI is useless.)
- Say: "I'm not confident enough to answer this reliably. Here's what I found: [fragments]. Want to try rephrasing, or should I give you my best attempt with a warning?"

**For refusals (safety/policy blocks):**
- Be transparent: "I can't help with this specific request because it looks like [category]. Here's what I *can* help with instead: [alternatives]."
- Never blame the user. The AI has constraints — name them.

**For timeout/degradation:**
- "I'm taking longer than usual. Want me to keep going, or give you a faster partial answer?"
- This gives the user agency instead of making them wait blind.

---

## NLX — NATURAL LANGUAGE AS UX (Aparna Chennapragada)

The five sections above describe how to add AI to traditional GUIs — buttons, suggestions, inline assertions, dedicated decision interfaces. This section is for the inverse case: when language IS the interface.

The Chennapragada framing: in an NLX product, users don't navigate menus or click buttons. They type or speak. The AI's response IS the UI. ChatGPT, Claude, conversational copilots, voice assistants, AI-first search products — these are all NLX. And they break every assumption that GUI design carries.

### The Five Inversions

When language is the interface, the design rules of GUI products invert:

| GUI World | NLX World |
|---|---|
| Buttons trigger actions | Prompts trigger actions |
| Menus organize options | Conversation reveals options |
| Validation errors live in red text | Validation lives in the AI's follow-up question |
| Errors are modal dialogs | Errors are dialog turns |
| Affordances are visual (icons, hover states) | Affordances are discoverability of language patterns — "what can I ask?" |

Each inversion is a design lever. Get one wrong and the product feels broken even when the model behind it is excellent.

### Inversion 1: Buttons Become Prompts

In a GUI, the button copy is the action label. "Save," "Send," "Delete." Three words.

In an NLX product, the equivalent is the prompt template — the language the user types or selects to invoke an action. And prompt templates are *much harder to design* than button labels because:

- The same intent can be expressed in 50 ways. Your prompt-handling needs to interpret all of them.
- The button is always visible. The prompt template is invisible until the user types it (or you suggest it).
- The button's outcome is fully scoped. The prompt's outcome depends on the model's interpretation.

**The design pattern:** Prompt suggestions visible at the start of a session — the NLX equivalent of a homepage. "Try asking: 'summarize this contract' or 'find the liability clauses.'" The suggestions teach the user what the system can do without forcing them to learn a query language.

**The anti-pattern:** A blank text box with a tiny placeholder ("Ask anything..."). Users freeze. They don't know what's possible. They type something underspecified, get a generic response, and conclude the product doesn't work.

### Inversion 2: Menus Become Conversation

In a GUI, menus organize functionality hierarchically. The user navigates: File → Export → PDF.

In an NLX product, the equivalent is multi-turn conversation. The user says "export this." The AI responds "what format?" The user says "PDF." Three turns instead of three clicks.

**The design pattern:** Treat the AI's questions as menu nodes. Each question represents a choice point. Design which questions to ask, in what order, with what defaults — the same design rigor you'd apply to a menu hierarchy.

**The anti-pattern:** Asking too many questions. NLX feels exhausting when the AI interrogates the user for every preference. Better: AI commits to a sensible default, names it, and asks only when the stakes are high. "Exporting as PDF with default formatting. Want a different format or layout?" — gives the user the option to override without forcing the conversation through every menu node.

### Inversion 3: Validation Becomes Follow-Up

In a GUI, validation errors appear in red below the input field. "Email format invalid."

In an NLX product, the equivalent is the AI's clarifying question. The user types "email John about the deal." The AI responds "Which deal? You're working on three this week."

**The design pattern:** The follow-up question is the validation. Frame it conversationally, not interrogatively. "Which deal — the Klarna one or the Bain one?" beats "Please specify deal."

**The anti-pattern:** Treating ambiguity as failure. Error message: "I don't have enough information to complete this request." That's GUI thinking translated badly into NLX. The right move is to ask the question that resolves the ambiguity, not declare failure.

### Inversion 4: Errors Become Dialog

In a GUI, errors are interruptive. A modal pops up. "An error occurred. Please try again."

In an NLX product, the equivalent is the AI naming the limitation in conversational language and offering an alternative path. "I can't access that file right now — it looks like the connection to your Drive expired. Can you reconnect, or want me to work from what's already in our conversation?"

**The design pattern:** The error is a turn in the conversation. Same voice, same warmth, same framing as success. The user shouldn't feel the temperature change between "it worked" and "it didn't."

**The anti-pattern:** Robotic system messages embedded in conversational AI ("ERROR: API_TIMEOUT"). Users perceive it as the product breaking character — and once that happens, trust drops sharply.

### Inversion 5: Affordances Become Discoverability of Language Patterns

In a GUI, affordances are visual cues that signal what the user can do. The hand cursor on a hyperlink. The hover state on a button. The drop shadow on a draggable element.

In an NLX product, the equivalent is making the user's *language space* discoverable. What can they ask? What phrasing works? What patterns produce good responses?

**The design pattern:** Surfacing language patterns in three places:
1. **Onboarding** — show 5-7 example prompts, organized by use case, that the user can tap to try
2. **Empty states** — when the user starts a new session, suggest patterns relevant to where they are
3. **In-conversation** — after a response, suggest 2-3 follow-up questions the user might ask next ("Would you like me to: explain this further / show the source / find related cases?")

**The anti-pattern:** Hiding the language space. Users discover what works through trial and error, with most early attempts producing unsatisfying responses. Adoption craters before users learn how to use the product.

### Four NLX Design Patterns That Work

Beyond the inversions, four specific patterns earn their place in any NLX product. Use these consistently:

#### Pattern 1: Confirmation by Restatement

When the user makes a high-stakes request, the AI restates it in its own words before acting. Not "are you sure?" — restatement.

**Example:**
> User: "Cancel my Bain meeting"
> AI: "Cancelling your 3pm Bain meeting today. The attendees will be notified. Want me to suggest a reschedule?"

The restatement does three things: confirms understanding, surfaces side effects, gives the user a moment to abort. It feels natural, not interrogative.

**When to use:** Any action that is destructive, irreversible, or expensive (sending an email, scheduling a meeting, deleting data, executing a transaction).

**When NOT to use:** Routine retrieval and answer tasks. Restating "let me look up the weather for you" before answering is friction.

#### Pattern 2: Progressive Disclosure via Follow-Up

Don't dump the full answer in turn 1. Give the headline, offer to expand.

**Example:**
> User: "What are the risks in this contract?"
> AI: "I found three significant risks: indemnification scope, IP ownership ambiguity, and termination terms. Want me to walk through them in order, or focus on one?"

The user gets the structure first. They can drill in where they need to. The AI doesn't waste tokens generating depth the user won't read.

**When to use:** Complex answers with multiple dimensions. Answers where the user's next question depends on which part of the answer matters.

**When NOT to use:** Simple, single-fact answers. "What time is my next meeting?" doesn't need progressive disclosure — just answer.

#### Pattern 3: Structured-Output Chips Inside Conversation

When the AI's response includes structured options or actions, present them as inline chips the user can tap — embedded in the conversational flow.

**Example:**
> AI: "I can summarize this contract in three ways. Tap one or tell me what you need."
> [📄 1-paragraph summary] [⚖️ Risk-focused] [💼 Negotiation-ready]

The chips are visual affordances inside the language interface. They preserve the conversational flow while giving the user a tactile shortcut for common follow-ups.

**When to use:** When the AI's response naturally branches into 3-5 follow-up paths and the user shouldn't have to type them.

**When NOT to use:** When the answer is open-ended. Forcing chips on every response makes the product feel like a glorified menu.

#### Pattern 4: Fallback to GUI When Conversation Fails

NLX is powerful but not universal. When the user's intent is precise and structured (filling a form, scheduling at a specific time, configuring settings), language is *worse* than GUI.

The pattern: detect when conversation is failing, offer a GUI fallback.

**Example:**
> User: "Set up a recurring meeting every other Tuesday at 2pm except holidays"
> AI: "That's a complex pattern — let me show you the scheduling form so you can verify each detail. [Open scheduling form]"

The AI recognizes that natural language is high-friction for this task and routes the user to a GUI affordance. The user appreciates the honesty more than they would appreciate a forced conversational walk-through.

**When to use:** When the task has 4+ structured parameters, when the cost of mis-parsing is high (financial transactions, scheduling, data entry), or when the user has visibly given up trying to express something in words.

**When NOT to use:** As a default. NLX should be the primary mode. GUI fallback is the safety net, not the floor.

### The NLX-First Design Checklist

Before shipping an NLX product:

- [ ] Onboarding shows example prompts organized by use case (not a blank text box)
- [ ] Empty states suggest where to start
- [ ] Follow-up suggestions appear after responses, especially for complex queries
- [ ] High-stakes actions trigger confirmation-by-restatement before executing
- [ ] Errors stay in dialog voice — no system messages, no modals
- [ ] Validation happens via clarifying questions, not error states
- [ ] GUI fallback exists for tasks with 4+ structured parameters
- [ ] Language space discoverability is designed, not accidental

The Chennapragada lens: in NLX, every word the AI writes is a UI element. Designers who internalize this build products that feel natural. Designers who treat language as throwaway output build products that feel broken even when the model is great.

---

## KEY DIAGNOSTIC QUESTIONS

**Q1: Confidence Appropriateness**
Does your interface's stated confidence match users' actual accuracy experience?

> **How to actually measure this (not estimate it):**
>
> Take 100 representative outputs from your AI feature. For each output:
> 1. Record the confidence signal you displayed (or would display) — Level 1 assertion, Level 2 verbal, etc.
> 2. Have a domain expert rate the actual accuracy (correct / partially correct / wrong)
> 3. Plot: confidence signal on X-axis, actual accuracy on Y-axis
>
> **Diagnose the plot:**
> - Diagonal line = calibrated. Your confidence signal matches reality.
> - Above the diagonal = overconfident. You're displaying more certainty than the AI actually has. Users will learn to distrust after errors.
> - Below the diagonal = underconfident. You're underselling accurate outputs. Users ignore a feature that could help them.
>
> **Red flag:** If you've never run this audit, your confidence signals are guesses. Most teams discover they're overconfident at the edges (low-confidence outputs displayed as assertions) and underconfident in the mid-range.
>
> **Sharpen it:** Run this audit on 3 different user query types (simple, medium, complex). Calibration often looks fine on average but breaks on complex queries — which are exactly where users need the signal most.

---

**Q2: Failure Transparency**
When the AI fails, does the user know it failed? Or do they think it worked?

- Example: Search returned 0 results. User sees nothing. Assumes no answer exists. Actually: the AI searched incorrectly.
- Example: Recommendation system suggests an irrelevant item. User doesn't interact. You think the feature is bad. Actually: the confidence signal was wrong and the algorithm surfaced a low-confidence result as an assertion.

**The behavioral test:** Show 5 incorrect AI outputs to 10 users without telling them the outputs are wrong. Measure: how many of them catch the error? If fewer than 50% catch the error, your failure signaling is insufficient — users will over-trust in production.

---

**Q3: Trust Durability**
After the AI gives one wrong answer, does the user:
A) Give it a second chance
B) Distrust it for months
C) Use it only for low-stakes decisions from now on

**The answer depends on product type. These are not guidelines — they are benchmarks from shipped products:**

| Product type | Trust recovery after one visible error | Why |
|---|---|---|
| **Enterprise tools** (finance, legal, HR systems) | 3-6 months of reduced usage | High stakes + professional reputation at risk. "I trusted the AI and it made me look bad" = lasting distrust. |
| **Consumer tools** (email, search, writing) | Users often retry within the same session | Lower stakes. Users frame errors as "the AI got it wrong this time" not "the AI is broken." |
| **Internal tools** (ops, data, eng workflows) | 2-4 weeks of skepticism, then recovery | Professional context but lower external consequences. Error feels like a tool bug, not a betrayal. |
| **Medical/legal/regulated** | Never fully recovers without explanation | If the domain has safety implications, a visible error without explanation triggers permanent distrust — and sometimes a compliance event. |

**Measure this for your product:** After a visible error, what % of users return to the feature within 24 hours? Within 7 days? If 24-hour return rate drops >30% after a visible error, your error UX is compounding the trust damage.

**Recovery design:** The fastest trust recovery comes from explaining *what went wrong* (not hiding it) and showing *what you're doing about it*. "We detected this response was incorrect and are using it to improve. Here's what I should have said: [X]." This converts a trust-damaging event into a trust-building one.

---

**Q4: Modality Fit**
Is the modality (chat, inline, dedicated interface) appropriate for the confidence level and error cost?
- Low stakes + high confidence → Inline assertion. No explicit confidence signal needed.
- High stakes + low confidence → Dedicated decision interface with explicit reasoning.
- Medium stakes + medium confidence → What are you using? If it's inline, it's wrong.

---

## REALITY CHECK

Before you ship:
- Have you tested on a user who doesn't know this is AI? Do they understand the confidence signal intuitively?
- Have you watched someone use the feature *incorrectly* because the confidence signal was ambiguous?
- Have you measured: what % of wrong answers does the user actually notice? (If it's < 50%, your failure UX is insufficient.)
- Can you explain your confidence levels without saying "the AI told me"?
- Have you run the calibration audit (100 outputs, plot confidence vs. accuracy)?

---

## QUALITY GATE

Before you ship AI with uncertainty:
- [ ] Confidence thresholds defined for each UI pattern (assertion, signal, alternative, question back, abstain)
- [ ] Calibration audit completed: actual accuracy vs. stated confidence align within 10%
- [ ] Interface tested with users who are NOT AI-literate
- [ ] Wrong-answer experience designed explicitly and tested — not just the success path
- [ ] AI loading states show process steps, not a generic spinner (for waits > 2s)
- [ ] Error states name the AI's limitation, not the user's failure
- [ ] Trust recovery benchmarks checked against product type (enterprise vs. consumer vs. internal)
- [ ] Trigger defined: what accuracy % would require a redesign of the confidence UI?

---

## WHEN WRONG

**Users trust the AI too much:**
- AI says X. User takes action without verifying. AI was wrong. User blames you.
- Trigger: Confidence signal is too strong, or hidden when it should be visible.
- Recovery: Add visible feedback loops ("I was wrong here"). Move from assertion to verbal confidence signal.

**Users don't trust the AI enough:**
- AI is 85% accurate. Users use it only 20% of the time they should.
- Trigger: Confidence signal is too visible ("0.75" feels low) or too verbal ("possibly" implies doubt).
- Recovery: Hide the confidence score. Show social proof instead: "95% of users find this helpful."

**Users game the uncertainty:**
- They learn the AI's failure modes and work around them. System feels fragile.
- Trigger: You built on top of a probabilistic model without designing for probabilistic use.
- Recovery: Reframe AI as a tool, not an authority. "AI suggestion. You decide." Shift responsibility explicitly.

**Modality mismatch causes confusion:**
- Users don't know whether to trust inline suggestions, chat, or decision interfaces.
- Trigger: High-confidence inline and low-confidence chat mixed in the same product without clear separation.
- Recovery: Physically separate modalities. Different screens, different interaction patterns, different confidence signals.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6:
1. **The recommendation** — specific confidence pattern for this feature and confidence range
2. **The hypothesis** — "We believe [confidence pattern X] will [produce Y trust outcome] because [Z]. We'd know we're wrong if [trust recovery metric drops]."
3. **The key trade-off** — transparency vs. friction; certainty vs. trust durability
4. **The biggest risk** — and mitigation (usually: over-confidence in early stages, calibration drift as model improves)
5. **The next action** — [step] by [role] by [date]

---

## GENERATE THE DELIVERABLE

Use the output prompt from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 11.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary. The diagram should show:
- The Uncertainty Communication Ladder (Level 1-5) as a vertical scale with confidence ranges and example products
- The calibration plot concept (diagonal = calibrated, above/below = over/underconfident)
- The trust recovery timeline by product type (enterprise 3-6 months vs. consumer within session)

Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.
