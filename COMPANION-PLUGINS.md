# Companion Plugins — The Full RTP Ecosystem

`rtp-personal-skills` is the **first plugin** to install on a fresh Claude Code account. But the orchestrator (`rtp-aipm-orchestrator`) is designed to command an entire ecosystem — not just RTP's own skills. To unlock its full power, install the companion plugins below.

This manifest exists so a new Claude account inheriting Ravi's work can rebuild the full operating system in a few commands, not by archaeology.

---

## TL;DR — The five tiers

| Tier | Owner | What it covers | Install priority |
|---|---|---|---|
| **1** | RTP (this plugin) | AI PM strategy, content + visual output in Ravi's voice, governance, design systems | Already installed |
| **2** | superpowers + compound-engineering | TDD discipline, systematic debugging, code review, brainstorming, plan execution | High |
| **3** | pm-skills | Textbook PM frameworks (Lean Canvas, OKRs, RICE, JTBD, Porter's, GTM, cohort analysis, A/B stats) | Medium |
| **4** | anthropic-skills | File formats (pdf, pptx, xlsx, docx), web artifacts, brand guidelines, scheduled tasks | Medium |
| **5** | dev tools | github, linear, supabase, commit-commands, episodic-memory, elements-of-style | As needed |

The orchestrator's tier map (in `skills/rtp-aipm-orchestrator/SKILL.md` → "FULL ECOSYSTEM AWARENESS" section) tells it which tier to reach for on any given task. Without these plugins installed, the orchestrator falls back to RTP-only — still useful, but missing 60% of its addressable surface.

---

## Tier 1 — RTP skills (this plugin, already installed)

```
/plugin marketplace add github:raviteja-palanki/rtp-personal-skills
/plugin install rtp-personal-skills@rtp-personal-skills
```

After install, every RTP skill is addressable as `rtp-personal-skills:rtp-{name}` (e.g., `rtp-personal-skills:rtp-first-principles`, `rtp-personal-skills:rtp-ai-prd`).

**80 skills + 10 slash commands.** Full list in `README.md`.

---

## Tier 2 — Process and engineering rigor

The discipline layer. When the work is actual engineering — code, tests, debugging, code review — these own the workflow.

### superpowers

Test-driven development, systematic debugging, brainstorming (rigor mode), writing plans, executing plans, finishing development branches, dispatching parallel agents, verification before completion, receiving code review, requesting code review.

```
/plugin marketplace add github:obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

Companion superpowers plugins (same marketplace):
```
/plugin install episodic-memory@superpowers-marketplace
/plugin install claude-session-driver@superpowers-marketplace
/plugin install elements-of-style@superpowers-marketplace
/plugin install superpowers-developing-for-claude-code@superpowers-marketplace
/plugin install superpowers-lab@superpowers-marketplace
```

### compound-engineering

Frontend design, agent-native architecture, dhh-rails-style code review, every-style-editor, agent-browser, document review, skill creation, brainstorming (compound mode), plan deepening, gemini imagegen.

```
/plugin install compound-engineering@compound-engineering-plugin
/plugin install coding-tutor@compound-engineering-plugin
```

(Marketplace `compound-engineering-plugin` is typically pre-registered with Claude Code; if not, ask the future Claude account where to add it.)

---

## Tier 3 — PM execution (pm-skills marketplace, 8 plugins)

Textbook PM frameworks. Use when an AI-specific RTP version doesn't apply or when Ravi explicitly wants the canonical framework.

```
/plugin install pm-product-discovery@pm-skills
/plugin install pm-product-strategy@pm-skills
/plugin install pm-execution@pm-skills
/plugin install pm-market-research@pm-skills
/plugin install pm-data-analytics@pm-skills
/plugin install pm-go-to-market@pm-skills
/plugin install pm-toolkit@pm-skills
/plugin install pm-marketing-growth@pm-skills
```

What each covers:

| Plugin | Frameworks |
|---|---|
| pm-product-discovery | Discovery cycles, OST, JTBD, interview synthesis, metrics dashboards |
| pm-product-strategy | Lean Canvas, Business Model Canvas, Porter's Five Forces, SWOT, PESTLE, Ansoff Matrix |
| pm-execution | PRDs, sprint planning, OKRs, retros, user stories, pre-mortems, test scenarios |
| pm-market-research | Competitive analysis, customer journey, market sizing, segmentation, personas |
| pm-data-analytics | A/B testing, cohort analysis, SQL queries, statistical analysis |
| pm-go-to-market | GTM strategy, ICP, beachhead segment, growth loops, battlecards |
| pm-toolkit | Resume review, NDAs, privacy policies, grammar checks |
| pm-marketing-growth | Marketing ideas, value props, positioning, North Star metrics, product names |

**RTP wins for AI-specific PM work** (`rtp-strategy-canvas` over generic strategy canvas). **pm-skills wins for everything else PM** — the textbook frameworks are sharper there.

---

## Tier 4 — File formats and Anthropic skills

Whenever the task touches a specific file format or Anthropic-built capability.

```
/plugin install anthropic-skills@claude-plugins-official
```

What this brings:
- `anthropic-skills:pdf` — read, fill, merge, split, manipulate PDF files
- `anthropic-skills:pptx` — create and edit PowerPoint presentations
- `anthropic-skills:xlsx` — create and edit Excel spreadsheets
- `anthropic-skills:docx` — create and edit Word documents
- `anthropic-skills:web-artifacts-builder` — multi-component HTML artifacts
- `anthropic-skills:brand-guidelines` — Anthropic's official brand colors and typography
- `anthropic-skills:skill-creator` — create new skills, modify existing ones
- `anthropic-skills:schedule` — scheduled tasks
- `anthropic-skills:consolidate-memory` — reflective pass over memory files
- `anthropic-skills:setup-cowork` — guided Cowork setup

**Layer with Tier 1 design DNA** when output is visual: `rtp-personal-branding` for typography + 4-color identity, then `anthropic-skills:pptx` or `anthropic-skills:docx` for the file format.

---

## Tier 5 — Development tools

Wrap operations the orchestrator should hand off rather than reinvent.

```
/plugin install github@claude-plugins-official
/plugin install linear@claude-plugins-official
/plugin install supabase@claude-plugins-official
/plugin install commit-commands@claude-plugins-official
/plugin install ralph-loop@claude-plugins-official
/plugin install skill-creator@claude-plugins-official
/plugin install claude-md-management@claude-plugins-official
/plugin install frontend-design@claude-plugins-official
```

Use when the task obviously hits that tool. The orchestrator's job is to know what's installed and pick the right one — never reinvent what's already wrapped.

---

## One-shot bootstrap on a fresh account

The slash command `/rtp-setup` (defined in `commands/rtp-setup.md`) prints this entire install sequence so a future Claude account runs it once and absorbs the full ecosystem.

```
/rtp-setup
```

After install, restart Claude Code, then ask the orchestrator to verify:

> "Run a tier check — list all installed plugins by tier and flag anything missing from the RTP ecosystem."

The orchestrator (loaded from `rtp-aipm-orchestrator`) will read the tier map in its SKILL.md and report which tiers are complete vs. partial.

---

## How the orchestrator uses these tiers

The orchestrator commands all installed plugins as expert agents, not just RTP's own skills. It picks the right tier per task:

- *"Brainstorm a new product idea"* → `superpowers:brainstorming` first (rigor), then layer `rtp-thinking-skills` for voice
- *"Write an AI PRD"* → `rtp-personal-skills:rtp-ai-prd` (purpose-built, RTP wins)
- *"Write a non-AI backlog story"* → `pm-execution:write-stories` (textbook, pm-skills wins)
- *"Debug failing tests"* → `superpowers:systematic-debugging` + `superpowers:test-driven-development`
- *"Build a slide deck"* → `rtp-personal-skills:rtp-frontend-slides` for HTML mechanics + `rtp-personal-skills:rtp-personal-branding` for design DNA
- *"Create a Word doc"* → `anthropic-skills:docx` for the file + `rtp-personal-skills:rtp-personal-branding` for visual style
- *"Search past conversations"* → `episodic-memory:search-conversations`
- *"Run a competitive analysis"* → `pm-market-research:competitive-analysis` for the framework + `rtp-personal-skills:rtp-thinking-skills` for the structural insight

The principle: **never refuse, never narrow.** If a plugin solves the problem better than RTP's purpose-built skill, reach for it. If after honest scanning no plugin fits, say so plainly.

---

## When companion plugins are missing

Without companion plugins installed, the orchestrator falls back to RTP-only mode. It still works — RTP covers AI PM strategy, content, design, and governance end-to-end — but you'll miss:

- **Engineering discipline** (TDD, debugging workflows, code review rigor) — superpowers/compound-engineering
- **Textbook PM frameworks** (Lean Canvas, RICE, OKRs, JTBD canonical) — pm-skills
- **File format generation** (real .pptx, .docx, .xlsx, .pdf) — anthropic-skills
- **Operational tools** (GitHub, Linear, Supabase) — claude-plugins-official

If a task hits a missing tier, the orchestrator will say: *"This needs `[plugin]` — install it via `/rtp-setup` or skip the framework and use a generic approach."* Better to know the gap than fake the answer.

---

## Updating this manifest

This file is the source of truth for the companion plugin ecosystem. When Ravi adds a new marketplace or plugin to his daily workflow, update:

1. **This file** (COMPANION-PLUGINS.md) — human-readable tier map
2. **companion-plugins.json** — machine-readable manifest (keeps `/rtp-setup` accurate)
3. **rtp-aipm-orchestrator/SKILL.md** — "FULL ECOSYSTEM AWARENESS" section
4. **commands/rtp-setup.md** — the install commands the slash command emits

Keep these four in sync. The whole point of the manifest is that a fresh Claude account inherits the working setup, not a stale one.
