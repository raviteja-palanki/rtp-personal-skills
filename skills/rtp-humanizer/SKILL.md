---
name: rtp-humanizer
description: >
  Identifies and removes signs of AI-generated text using Wikipedia's AI Cleanup patterns.
  Use when writing emails, articles, README content, or any text that must read as genuinely
  human-written. Applies 24 pattern checks covering inflated significance, AI vocabulary,
  hedging, filler, and chatbot artifacts.
---

# Humanizer — Remove AI Writing Patterns

A writing tool that identifies and removes signs of AI-generated text, making it sound more natural and human-written. Based on Wikipedia's "Signs of AI writing" guide, maintained by WikiProject AI Cleanup, which catalogues observations from thousands of instances of AI-generated text.

## Why This Exists

Large language models produce text by predicting the most statistically likely next token. The result tends toward the average — the phrasing that works in the widest variety of cases. This is why AI writing sounds generic: it literally is the generic version of everything.

The Humanizer detects 24 specific patterns that betray AI-generated text and rewrites them to sound like an actual person wrote them. It also addresses "soulless" writing — text that is technically clean but lacks any human voice or personality.

## The 24 Patterns

The patterns fall into five categories. Each pattern includes what to look for and how to fix it.

### Content Patterns (1–6)

**1. Significance Inflation.** AI text inflates the importance of everything. Words like "pivotal moment," "enduring testament," "evolving landscape," and "indelible mark" are red flags. The fix is to state facts plainly. Instead of "marking a pivotal moment in the evolution of regional statistics," write "was established in 1989 to collect regional statistics."

**2. Notability Name-Dropping.** LLMs dump lists of media outlets to prove something matters. Instead of "cited in NYT, BBC, FT, and The Hindu," pick one and provide context: "In a 2024 NYT interview, she argued that..."

**3. Superficial -ing Analyses.** Participle phrases like "highlighting," "showcasing," "reflecting," and "symbolizing" get tacked onto sentences to create an illusion of depth. Remove them or replace with sourced claims.

**4. Promotional Language.** Words like "nestled," "breathtaking," "vibrant," "groundbreaking," and "must-visit" turn factual writing into ad copy. Replace with neutral descriptions.

**5. Vague Attributions.** "Experts believe," "Industry reports suggest," and "Some critics argue" attribute opinions to nobody in particular. Name specific sources or remove the claim.

**6. Formulaic Challenges Sections.** "Despite challenges... continues to thrive" is a template LLMs apply to everything. Replace with specific facts about actual challenges.

### Language and Grammar Patterns (7–12)

**7. AI Vocabulary.** Certain words appear at dramatically higher frequency in post-2023 AI text: "Additionally," "delve," "foster," "underscore," "intricate," "pivotal," "landscape" (used abstractly), "testament," "showcase," and "vibrant." Replace with simpler, more common alternatives.

**8. Copula Avoidance.** LLMs avoid "is" and "has" in favor of elaborate substitutes: "serves as," "stands as," "features," "boasts." Just use "is" and "has."

**9. Negative Parallelisms.** "It's not just X, it's Y" and "Not only... but also..." are overused by AI. State the point directly.

**10. Rule of Three.** LLMs force ideas into groups of three ("innovation, inspiration, and insights") to sound comprehensive. Use whatever number of items is actually appropriate.

**11. Synonym Cycling.** Repetition-penalty algorithms cause LLMs to cycle through synonyms: "the protagonist... the main character... the central figure... the hero." Just repeat the clearest term.

**12. False Ranges.** "From X to Y" constructions where X and Y aren't on a meaningful spectrum. List topics directly instead.

### Style Patterns (13–18)

**13. Em Dash Overuse.** LLMs use em dashes far more than human writers. Replace most with commas or periods.

**14. Boldface Overuse.** AI mechanically bolds terms, especially acronyms and key phrases. Remove unnecessary bold formatting.

**15. Inline-Header Lists.** Bullet points starting with a bolded label and colon ("**Performance:** Performance has been enhanced..."). Convert to prose.

**16. Title Case Headings.** AI capitalizes every major word in headings. Use sentence case instead.

**17. Emojis.** AI decorates bullet points and headings with emojis. Remove them from professional text.

**18. Curly Quotes.** ChatGPT outputs curly quotation marks instead of straight ones. Replace with straight quotes.

### Communication Patterns (19–21)

**19. Chatbot Artifacts.** Phrases like "I hope this helps!", "Certainly!", "Let me know if you'd like me to expand," and "Great question!" are conversational chatbot artifacts that get pasted into documents. Remove entirely.

**20. Knowledge-Cutoff Disclaimers.** "While specific details are limited based on available sources" and "as of my last training update" are AI disclaimers that don't belong in finished text. Find real sources or remove.

**21. Sycophantic Tone.** "Great question! You're absolutely right!" is people-pleasing filler. Respond to the substance directly.

### Filler and Hedging (22–24)

**22. Filler Phrases.** "In order to" becomes "To." "Due to the fact that" becomes "Because." "At this point in time" becomes "Now." "It is important to note that" gets deleted — just state the thing.

**23. Excessive Hedging.** "It could potentially possibly be argued that" becomes "may." Say what you mean.

**24. Generic Positive Conclusions.** "The future looks bright" and "Exciting times lie ahead" are vacuous. Replace with specific plans, numbers, or facts.

## The Humanization Process

The process has two phases. The first is mechanical: identify and fix the 24 patterns above. The second is harder and more important — adding voice and personality.

### Phase 1: Pattern Removal

Scan the text for all 24 patterns. Rewrite each instance while preserving the core meaning and matching the intended tone. Use simple constructions where appropriate. Replace vague claims with specifics.

### Phase 2: Adding Soul

Sterile, voiceless writing is just as obviously AI as text full of "delve" and "tapestry." Good writing has a human behind it. Signs of soulless writing include every sentence being the same length, no opinions or reactions, no acknowledgment of uncertainty, no first-person perspective, no humor, and reading like a press release.

To add voice: have opinions and react to facts rather than just reporting them. Vary sentence rhythm — short punchy sentences followed by longer ones. Acknowledge complexity and mixed feelings. Use first person when it fits. Let some structural messiness in, because perfect structure feels algorithmic. Be specific about feelings rather than generic ("there's something unsettling about agents churning away at 3am" beats "this is concerning").

### Phase 3: Anti-AI Audit

After rewriting, ask: "What makes this so obviously AI generated?" Identify any remaining tells, then revise to eliminate them. This second pass catches patterns that survive the first rewrite — the rhythm can still be too tidy, or the structure too balanced, even after individual patterns are fixed.

## Full Example

### Before (AI-sounding)

> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools — nestled at the intersection of research and practice — are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale.

### After (Humanized)

> AI coding assistants can make you faster at the boring parts. Not everything. Definitely not architecture.
>
> They're great at boilerplate: config files, test scaffolding, repetitive refactors. They're also great at sounding right while being wrong. I've accepted suggestions that compiled, passed lint, and still missed the point because I stopped paying attention.
>
> People I talk to tend to land in two camps. Some use it like autocomplete for chores and review every line. Others disable it after it keeps suggesting patterns they don't want. Both feel reasonable.

### What changed

Chatbot artifacts removed ("Great question!", "I hope this helps!"). Significance inflation removed ("testament," "pivotal moment," "evolving landscape"). Promotional language removed ("groundbreaking," "nestled"). AI vocabulary replaced ("Additionally," "showcase," "foster"). Copula avoidance fixed ("serves as" became "is"). Negative parallelism removed ("It's not just X; it's Y"). Rule-of-three patterns broken. Voice and personality added throughout.

## Reference

Based on the Wikipedia article "Signs of AI writing," maintained by WikiProject AI Cleanup. The patterns documented there come from analysis of thousands of instances of AI-generated text observed on Wikipedia.

The key insight is this: LLMs predict the statistically most likely next token. The output gravitates toward the most generic phrasing that works across the widest range of contexts. Recognizing this tendency is the first step to fixing it.

## Version History

- 2.1.1 — Fixed pattern 18 example (curly quotes vs straight quotes)
- 2.1.0 — Added before/after examples for all 24 patterns
- 2.0.0 — Complete rewrite based on raw Wikipedia article content
- 1.0.0 — Initial release

## License

MIT
