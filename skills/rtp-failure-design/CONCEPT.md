# Failure Design — Concept Guide

## FIRST PRINCIPLES

In traditional software, errors are exceptions. The system is designed to work correctly, and error handling catches the rare cases where it doesn't. In AI products, errors are not exceptions. They are a statistical certainty. A model with 95% accuracy will be wrong on 1 in 20 responses. That's not an edge case — that's a design parameter.

The atomic insight: **in AI products, the experience of the AI being wrong IS the product, as much as the experience of it being right.** Users don't judge AI products by peak performance. They judge them by how the product handles the inevitable wrong answer.

## DUAL DEFINITION

**Business definition:** Failure design is the practice of creating user experiences for when AI outputs are incorrect, uncertain, or inappropriate — ensuring that these moments build trust rather than destroy it, by giving users transparency, control, and recovery paths.

**Technical definition:** The specification of fallback behaviors, confidence thresholds, correction interfaces, and graceful degradation paths for every non-deterministic output in the system — including refusal logic, human escalation triggers, and feedback capture mechanisms.

**The Happy Path Monopoly.** Product demos show success. Design reviews focus on ideal flow. User stories describe winning scenarios. The PM writes one line about failures — "show error message" — and moves on. This is designing a car with no seatbelts because you plan to only drive in good weather. It's incomplete product design.

**The Blame-Shift Pattern.** When AI fails, the response matters more than the failure itself. "I'm sorry, I didn't understand that. Could you try again?" shifts the burden to the user — they asked wrong. Trust erodes not because the AI was wrong, but because it avoided responsibility. Compare: "I'm not confident in this answer. Here's what I found, but verify before acting on it." Same failure, opposite trust impact. One erodes trust; one deepens it.

**The Confidence Theater.** Displaying confidence percentages without actionable meaning. "87% confidence" is noise. What does the user do with it? Confidence must translate to action: "I'm confident about this — no verification needed" vs "I found something relevant — you should review it" vs "I'm too uncertain — ask a human." Actionable trust language beats false precision.

**The Invisible Degradation.** A correction path exists, but the user doesn't know when to use it. The AI serves a plausible-sounding wrong answer with no signal that verification is needed. The user acts on it and discovers the mistake hours or days later. High-stakes failures need explicit uncertainty signals before the user commits to acting on the output.

## INTELLECTUAL LINEAGE

- **Anthropic's approach to model limitations** — Claude's design philosophy of being transparent about uncertainty and refusing when appropriate. The product embodiment of failure design.
- **Don Norman** — *The Design of Everyday Things.* On designing for human error. Applied to AI: designing for AI error is equally important.
- **Jared Spool** — "The best error message is the one that never shows up." Applied to AI: the best failure design makes the failure feel like a normal part of the interaction, not a break in experience.
- **Ravi's Agent Spectrum** — Progressive autonomy levels explicitly define what the AI does when it's uncertain at each level, from "suggest and explain" to "act and report."

## REAL-WORLD EXAMPLES

**Example 1: Claude's refusal design.**
When Claude encounters an uncertain or out-of-scope request, it refuses explicitly rather than guessing. "I'm not certain about this" beats "I think..." when the stakes are high. This is a product decision that trades short-term task completion for long-term trust. The failure mode (refusal) is designed as carefully as the success mode (generation). Users prefer "I don't know" to a confident-sounding wrong answer.

**Example 2: Autocomplete failure design.**
Gmail's Smart Compose offers suggestions. When wrong, the user keeps typing and the suggestion vanishes — zero friction recovery. Consequence magnitude is tiny (a momentary visual distraction). Correction path is the normal path (typing). This works because it's low-stakes. High-stakes suggestions need higher-friction confirmation.

**Example 3: Medical AI diagnostic failure.**
An AI tool flags potential conditions. Wrong classification = unnecessary procedures or missed diagnoses. Failure design: AI presents findings as "areas for physician review" not "diagnoses." All flags require human confirmation before any action. High confidence (>95%) still requires review, but routes to routine intake. Low confidence (<80%) routes to specialist review. The failure path is engineered as carefully as the detection path.

**Example 4: Credit limit increase recommendation.**
An AI recommends increasing a customer's credit limit. Wrong decision = customer financial distress or write-off. Failure design: AI generates recommendation with confidence and reasoning. Above 90% confidence, show in customer dashboard for them to accept. Below 80%, don't show at all. 80-90%, queue for underwriter review. The human decision is the product; the AI's job is to surface candidates and highlight uncertainty.

## FURTHER READING

- Don Norman, *The Design of Everyday Things* — Designing for error as a feature
- Anthropic, "Claude's Character" — Transparency and refusal as design choices
- Jared Spool, "Design for Failure" — Error prevention vs error recovery
- Kat Holmes, *Mismatch* — Inclusive design principles applied to AI error handling
