---
name: rtp-readme-storytelling
description: 'Write or revise a README, GitHub project introduction, or public technical description that connects the project to a recognizable problem. Explain why it exists, what it does, how it works, and what the reader can do next. Preserve the narrative approach, concrete examples, and personal voice while making practical information easy to find. Use verified project facts and genuine author experience; distinguish illustrative comparisons from measured results and documented learning processes from automatic improvement. Adapt the structure for a reusable tool, a personal showcase, or a documentation repository. Pair with rtp-thinking-writing for clarity, evidence, and voice.'
version: v1.0.1_latest
---

# README storytelling

Help a new reader understand why the project matters, what it actually does, and whether it is relevant to them. Use a clear narrative to connect the problem, the design, and a concrete result. Keep the practical information easy to find.

Use `rtp-thinking-writing` for the shared writing standard. The original reference to Morgan Housel describes an editorial aspiration: familiar situations, clear reasoning, specific observations, and natural rhythm. Develop the project's own story rather than borrowing a signature passage or inventing an emotional origin.

## 1. Understand the project before writing its story

Read the existing README, relevant source or architecture, usage guidance, and license. Establish the intended reader and whether the repository is a reusable tool, public showcase, research artifact, or internal documentation. A public repository does not automatically grant permission to reuse its contents.

Check what exists now, what is proposed, and what has actually been tested. Verify counts, commands, supported environments, file paths, ownership, and any claimed results. Do not infer the project's capabilities from its name or an old diagram. For a revision, preserve working installation or usage steps, important limitations, links, and licensing information unless a verified change requires updating them.

Identify the central problem in the reader's terms. An inventory such as "90 skills" can orient a visitor when its purpose is explained, but a count alone does not explain value. A useful opening states what the project does and the decision or difficulty it addresses.

## 2. Build the narrative around useful questions

Use the following sequence as a starting point. Move quick-start or essential scope information earlier when that helps the visitor. A short project description may need only a few of these parts.

| Part | Purpose |
|---|---|
| Opening | Establish a recognizable problem and explain the project's purpose within the first few lines |
| Bridge | Connect that problem to the design choice or the author's intention |
| Origin | When relevant, describe the real frustration or observation that prompted the work |
| Getting started or exploring | Show the next useful step for this repository's intended audience |
| Architecture | Explain components through what they take in, decide, and produce |
| Example or comparison | Demonstrate the practical difference with a representative case |
| Improvement over time | Explain the actual learning, maintenance, or feedback process, if one exists |
| Author and project context | Provide relevant, verified experience and responsibilities |
| Help, contribution, and license | State or link the project's actual expectations where applicable |

### Open with a point the reader can recognize

A direct explanation, concrete problem, short story, or verified number can work. A hero image is optional. Do not require a slogan, ban the product name, or delay what the repository does until the reader has finished an origin story.

The bridge can be a simple sentence connecting the problem and approach. Use first person only when writing for the author and the intent is supported. "I wanted to make those decisions easier to review" is appropriate only if that is the author's stated intent.

### Tell the origin honestly

One or two paragraphs often suffice. Name the recurring difficulty, why the existing approach was insufficient, and the design insight that followed. Include lived experience only when supplied or verified. Do not replace "worked with a team" with "shipped" if that inflates the author's role. Some repositories need no personal origin story.

### Explain architecture in both human and practical terms

Describe what each layer or component does, then include its real identifier and a useful link when the reader needs to locate or invoke it. For example, explain that a falsification skill identifies evidence that would overturn a recommendation, then name `rtp-falsification`. Human descriptions and exact labels serve different needs and can appear together.

Show the sequence or dependencies when they affect use. Distinguish automatic behavior from user-triggered actions, supported parallel work from a universal promise, and generated artifacts from validated outcomes. Put detailed reference material in linked documents where that keeps the introduction readable.

### Show a fair example

Include a before-and-after comparison or worked example when it helps explain the project. Label constructed outputs as illustrative. For an observed comparison, record the input, relevant configuration, versions, and conditions, including material differences in available information.

Do not invent a weak baseline or imply that a curated example is an experiment. Explain the specific difference: perhaps the revised output names assumptions, identifies a decision owner, or records what evidence would change the recommendation. Avoid a mandatory punchline such as "the thinking happened in the right order" unless the example establishes it.

### Describe improvement as a real process

If the system improves through use, explain what is captured, who reviews it, how accepted changes enter the project, and what is versioned or tested. Distinguish stored feedback from adopted changes and demonstrated improvement. A system does not automatically learn merely because a README says it compounds. If no learning loop exists, describe maintenance or omit the claim.

A concise callout can highlight the mechanism. Claims of a moat or defensible advantage require evidence and conditions; they are not required for an appealing project introduction.

### Ground the author section in relevant facts

Use verified experience, scope, domain, and contributions before abstract identity labels. Show what the author does rather than assigning a flattering archetype. An author can be a thoughtful practitioner without claiming sole ownership of team results. Include "this is how I work" only when the author has established that the project is actually used that way.

## 3. Make the README usable and readable

For a reusable tool, provide or link the necessary prerequisites, setup, a first useful example, limitations, and help. For a personal showcase, explain how to explore the material and its reuse terms instead of inventing an installation promise. Keep claims consistent with the repository's license and current documentation.

Use ordinary verbs and concrete nouns. Explain technical labels rather than removing them. Replace hype with the specific capability or result. Retain a meaningful opinion when supported, and qualify it where the conditions matter. "A framework without limits is always worse than no framework" is an argument to examine, not an established fact.

Use a clear heading hierarchy, usually a project title followed by second-level sections and occasional third-level subsections. Greater depth can be valid when genuinely needed; a separate reference often reads better. Use bold or a blockquote for an important sentence sparingly. Avoid layering bold, italics, color, and callouts on every paragraph.

Diagrams, before-and-after tables, and short arrow sequences can explain architecture. Include meaningful image descriptions. Use text labels alongside any color coding; decorative emoji are not required. A small HTML footer can work when the renderer supports it, but its tool attribution and date must be accurate rather than copied from an old template.

Use working relative links for files inside the repository and verified external links where needed. Check heading anchors after renaming sections. Keep essential information available as text rather than only in a hero image.

## 4. Review before delivery

Read the opening, example, practical instructions, and ending as a newcomer would. Check whether each paragraph identifies something specific about this project. Retain clear reusable language where it serves ordinary documentation; not every sentence needs an original flourish.

Review natural rhythm aloud when available or silently otherwise. Do not add deliberate disorder to make the writing seem human. Check links and claims, and verify commands when feasible and within the task's authorized scope. Report untested commands as untested rather than implying successful execution.

The finished README should let the reader explain the purpose, find a concrete example, understand the important limits, and take the intended next step. Interest in the author is a possible benefit, not a substitute for understanding the project. Deliver the revised file and a concise note about material changes or incomplete checks. Publishing follows the user's authorization for the task.

Reference checked 13 Sep 2026: [GitHub's guidance on repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) covers purpose, usefulness, getting started, help, maintainers, and relative links. It supports these practical documentation needs without prescribing one narrative style.

**Revision 1.0.1, 13 Sep 2026.** Preserves the narrative opening, bridge, origin, functional architecture, example, improvement story, author context, and visual emphasis. Clarifies factual limits, actual repository use, and practical information a visitor needs.
