# Series publishing and visual guidance

Companion to Deep Dive Writer, revision 1.1.1, 13 Sep 2026. Use this for Ravi's website series; check the active project's schema before changing metadata or navigation.

## Navigation comes from the current project

The earlier skill described four series locations: `1_Projects/2_agentic-stack/`, `1_Projects/3_harness-engineering-series/`, `1_Projects/4_ai-evals/`, and `1_Projects/7_AI PM OS/`. It recorded 35 Agentic Stack posts, 35 AI Evals posts, and 30 plus five bonus AI PM OS posts in May 2026. Those are historical planning counts, not current inventories or completion claims.

The old root `corpus-map.md` was found in `_archive/11_MAY_2026_root_cleanup/` during this revision. Locate the current series files, topic map, and tracker before using archived relationships. The website URL index is `1_Projects/1_my-personal-website/WEBSITE-URL-INDEX.md`. In September's local source, Why Your Agent Fails uses the `harness` series route and an `l1-t01-why-your-agent-fails` slug. A historic series label or episode number alone is insufficient to construct its destination.

For a legacy source consumed by the bracket-reference parser, preserve:

```text
[<Post Title> (<Series Name> <Post ID>)]
```

Use the actual title in the form the parser expects, the full series name, and the exact ID. Existing examples include `[The Context Stack (Agentic Stack L1-T03)]` and `[The Limits of Evaluation (AI Evals L3-T30)]`; resolve their current identities before reusing them. Prefer the canonical title over an automatic title-case conversion. Check how inline H1 formatting is normalized by the project rather than including or stripping markup by guesswork.

A current project may already use resolved Markdown links instead. Preserve that contract; do not replace working links with an old parser convention. Explain the relevant insight in the article, then link for further depth. A cross-reference should not require the reader to leave before they can understand the present argument.

## Spine metadata

Where the project uses this schema, retain its field names:

```yaml
spine:
  depends_on: [L1-T01, L1-T02]
  pairs_with: [L1-T05, L1-T09]
  builds_toward: [L2-T03, L3-T02]
```

These IDs illustrate the shape, not verified relationships for a particular article.

- `depends_on`: prerequisite ideas a reader needs.
- `pairs_with`: articles that complete the same loop or offer a useful complementary view.
- `builds_toward`: later concepts this article prepares the reader to understand.

Use actual relationships, allowing an empty field when valid. Two to four entries was an earlier navigation guideline, not a quota. Resolve ambiguous IDs across series using the project's supported convention; do not invent a namespace. Check missing destinations and unintended prerequisite cycles.

Retain a supported `cliffhanger` field if the article uses one. In the body, explain what this article resolved and why the next question follows, then name the next article. One or two connected paragraphs may be enough. For a final or standalone article, provide a complete ending and an appropriate related resource without inventing a next episode. Keep Builds on / Leads to navigation consistent with the same map.

## Two SVG briefs

The standard series uses concept and practice visuals. Place them where the reader needs them. The original authoring footer is:

```text
## SVG guidance — redesign notes for [post ID]

Concept SVG: [name]
Quick-scan message: [what the reader should understand]
Main visual element: [specific arrangement and annotations]
Exact display text: [approved labels and central sentence]
Redesign improvement: [what the current visual needs]

Practice SVG: [name]
Quick-scan message: [the practical insight]
Main visual element: [mechanism, contrast, or usable artifact]
Exact display text: [approved labels and central sentence]
Redesign improvement: [what the current visual needs]
```

Preserve this footer in a source workflow that expects it. In reader-facing output, use the established author-only handling or a companion brief. Check the actual rendering; an HTML comment can keep notes out of the visible page but is still public in source and must not contain confidential material.

Use the active Why Your Agent Fails visual system as a reference when it remains the series standard. Inspect the actual assets and design guidance rather than inferring colors or typography from the title. Keep prose-only edits separate from asset work unless asset changes are requested or necessary within scope.

Visual checks:

- One central concept, mechanism, or comparison is easy to recognize.
- Labels identify the actors, conditions, and quantities without requiring unexplained shorthand.
- Brief phrases and concrete nouns support scanning; necessary detail remains available in the article.
- Data retains units, periods, evidence labels, and important uncertainty.
- Color or a symbol is not the only way to communicate meaning.
- The reader can explain the intended point after viewing it; a three-second glance is a design aim, not a measured result unless tested.

## Framework vocabulary and attribution

The old skill called the following the "25 Ravi-invented frameworks." Preserve their place in the corpus, but verify each definition, origin, and canonical home. Inclusion in Ravi's writing does not establish that he invented a term or mathematical result; Pass^k and Time-to-First Value especially require accurate attribution.

CONTEXT framework; MHTE; Pass^k math; Agent Tax; Customer-Success Paradox; AI Agent Autonomy Rate; Magnifying Glass thesis; 8-or-9-words rule; Three Architecture Archetypes; Four Moat Archetypes; Three Loop Archetypes; Five Pricing Bands; Four Adoption Mechanics; Five Eval Limits; Five-Card Gate; CAPTURE; Context Spec; Language Test; Trap/Fix structure; 4-Stage Hill-Climb; Distribution Surface Map; Self-Optimisation Rounds; Time-to-First Value (TTFV); Harness Health Score; Five-Layer Governance Stack.

Link the relevant canonical article on first substantive use, explain the term briefly, and keep its conditions. A useful analogy, such as a chef's instructions, an exam packet, hotel concierge, F1 pit crew, or restaurant operations manual, should retain the relationship it teaches and its limit. Claims such as "the user's message is less than 1% of context" require a defined example or evidence; they are not universal facts to preserve verbatim.

## A verified cross-reference example

A runnable evaluation can guide repeated proposals, tests, and keep-or-discard decisions. Karpathy's [autoresearch repository](https://github.com/karpathy/autoresearch) describes that loop for bounded language-model training experiments, with human-maintained instructions and a fixed experiment budget. This is an example of the mechanism, not permission to run an unbounded optimization job or evidence of universal gains.

The earlier wording said the agent "shipped 93 automated commits" and produced a "53% rendering speedup" at Shopify. The [Liquid pull request](https://github.com/Shopify/liquid/pull/2056), opened March 11, 2026 and inspected September 13, was still open with 93 commits. It reported a 53% reduction in combined parse-and-render time on ThemeRunner, about 20% in rendering alone, and roughly 120 automated experiments. The method used Ruby 3.4 with YJIT, best-of-three benchmark runs, and disabled garbage collection during timing. This is a reported benchmark result in a proposed change, not verified production deployment. Recheck its status when writing about it.

Give the reader that bounded lesson before linking to the corpus article that develops it. Look up that article's current title and destination rather than preserving the old example reference uncritically.
