---
name: rtp-readme-storytelling
description: >
  Write READMEs and public-facing technical descriptions with Morgan Housel-level
  storytelling — narrative-first, no feature specs, frame-of-reference openings, before/after
  contrasts, and "why" before "what". A README is the first 30 seconds of a conversation
  with someone who doesn't care yet; this skill makes them care before they understand.
  Use when writing or rewriting a project README, a GitHub repo description, a launch
  announcement, or any first-touch technical narrative. Triggers on "readme", "GitHub
  readme", "repo description", "storytelling readme", "narrative-first writeup", "rewrite
  this readme", "make this readme better", "README hook".
version: 1.0
author: Ravi Teja Palanki
---

# README Storytelling — Narrative-First Technical Writing

Write READMEs and public-facing technical descriptions that make people care before they understand.

## CORE PHILOSOPHY

A README is not a feature spec with a title. It's the first 30 seconds of a conversation with someone who doesn't care yet — and your job is to make them care.

Three principles:

1. **Open with a frame of reference, not a feature count.** "66 skills, 3 layers, 5 plugins" means nothing to a stranger. "The best PMs don't have better answers — they have better questions, and they ask them in the right order" makes them lean in.

2. **Tell the story of why before the story of what.** The frustration, the pattern you kept seeing, the moment you realized the existing tools weren't enough — that's what earns the reader's attention. The technical architecture comes after they already care.

3. **Show the difference, don't describe the features.** A before/after comparison — "without this" vs "with this" — does more work than three paragraphs of capability description.

---

## STRUCTURE

### The Hook (first 3 lines after the hero image)
- A frame of reference the reader already agrees with
- No statistics, no product names, no "introducing..."
- Reads like the opening of a Morgan Housel essay — a truth about the domain that the reader recognizes

### The Bridge (1 sentence)
- Connects the hook to the author's intent
- "I wanted to build a system that thinks like that."
- Short. Declarative. No hedging.

### The Origin Story (1-2 paragraphs)
- The frustration or pattern that motivated the work
- Specific enough to feel real — name the failure mode you kept seeing
- This is where lived experience shows: "I'd been shipping Gen AI products" not "teams often ship"
- End with the architectural insight that solved the frustration

### The Architecture (bulk of README)
- Explain each layer through what it DOES, not what it IS
- Skill names never appear as raw technical labels — describe what the skill asks or produces
- Use the reader's language: "the skill that asks 'who pays the cost if you're wrong?'" not "`rtp-falsification`"
- Color-code layers with emoji dots (🟣 🔵 🟢) for visual scanning

### The Comparison (mandatory)
- Before/after block showing output without the system vs with it
- The "without" should sound like every generic AI output the reader has seen
- The "with" should be specific enough to feel like real work product
- Bold the punchline: **"The difference isn't polish. It's that the thinking happened in the right order."**

### The Compounding Story
- This is the "moat" section — what makes the system improve over time
- Use the blockquote callout for the key insight
- End with the strongest single line: **"The system doesn't just run — it learns from running."**

### About Me
- Lead with concrete experience: years, scale, verticals, what you shipped
- Then the archetype/identity — but grounded in specific behavior, not abstract labels
- The bridger description works because it names what happens in the room, not a personality trait
- Close with: "This isn't a side project. It's how I actually work."

---

## ANTI-PATTERNS

- **Never open with a feature count.** "66 skills, 3 layers" is a spec, not a story.
- **Never use "leveraging" or "harnessing" or "empowering."** Say what it does.
- **Never list technical labels without explaining what they do in human terms.**
- **Never describe yourself passively.** "I've shipped" not "I've worked with teams that ship." "I sit in the room with engineers" not "I've been in environments where engineers..."
- **Never use "game-changing," "revolutionary," "cutting-edge."** The work speaks.
- **Never force a rule of three.** Use whatever number is actually right.
- **Never end with a generic positive conclusion.** End with a specific, declarative statement about what this means.

---

## FORMATTING TRICKS FOR VISUAL EMPHASIS

- **Bold + italic for key insight phrases:** ***ways of thinking***
- **Blockquote + italic for section openers** that set emotional tone
- **Bold the punchline sentence** in any comparison or conclusion
- **Emoji color dots** (🟣 🔵 🟢 🟠 🔴) to create visual layers in lists
- **Arrow chains** in protocol descriptions: gather context → choose depth → quality gate
- **Sub tags** for the footer: `<sub>Built with Claude · April 2026</sub>`
- Keep headers as **## level** — never go deeper than ### in a README. Depth comes from prose, not heading hierarchy.

---

## VOICE

Write like Morgan Housel explains finance — with frames of reference that sting the heart before they inform the mind. Vary sentence rhythm. Short declarative sentences after long flowing ones. Let some structural messiness in — perfect structure feels algorithmic.

Have opinions. "A framework that doesn't know its limits is more dangerous than having no framework at all" is an opinion. It's also true. Don't hedge it.

---

## QUALITY GATE

Before shipping, read the README aloud. If any sentence sounds like it came from a product launch blog post, rewrite it. If any paragraph could apply to any project by changing the proper nouns, it's too generic. If the About Me section could describe any experienced PM, it hasn't earned its place.

The test: would someone who reads this think "I want to talk to this person" — not "I understand this product"?
