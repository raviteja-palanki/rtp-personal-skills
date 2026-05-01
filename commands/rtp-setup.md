---
description: Bootstrap the full RTP ecosystem on a fresh Claude Code account — install rtp-personal-skills + companion plugins (superpowers, compound-engineering, pm-skills, anthropic-skills, dev tools)
---

# /rtp-setup — Bootstrap the Full RTP Ecosystem

You are running on a Claude Code account where Ravi Teja Palanki's complete operating system needs to be installed. The user just invoked `/rtp-setup` to absorb the full ecosystem in one shot.

## What this command does

1. Confirms `rtp-personal-skills` is installed (the foundation)
2. Prints the marketplace `add` commands the user needs to run
3. Prints the `/plugin install` commands tier by tier
4. Verifies setup at the end by reading `rtp-personal-skills:rtp-aipm-orchestrator` tier map

## Output to the user

Print this verbatim, then wait for them to run the commands and tell you they're done:

---

**Bootstrapping the full RTP ecosystem.**

This installs `rtp-personal-skills` (already done if you can see this) plus four companion tiers documented in `COMPANION-PLUGINS.md`.

Run these blocks in order. After each block, confirm "done" before continuing.

### Step 1 — Verify Tier 1 (RTP skills)

```
/plugin marketplace add github:raviteja-palanki/rtp-personal-skills
/plugin install rtp-personal-skills@rtp-personal-skills
```

If `/plugin list` already shows `rtp-personal-skills@rtp-personal-skills`, skip this step.

### Step 2 — Tier 2: Process and engineering rigor

```
/plugin marketplace add github:obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
/plugin install episodic-memory@superpowers-marketplace
/plugin install claude-session-driver@superpowers-marketplace
/plugin install elements-of-style@superpowers-marketplace
/plugin install superpowers-developing-for-claude-code@superpowers-marketplace
/plugin install superpowers-lab@superpowers-marketplace
/plugin install compound-engineering@compound-engineering-plugin
/plugin install coding-tutor@compound-engineering-plugin
```

(If `compound-engineering-plugin` marketplace isn't already registered, find its source URL via the Claude Code plugin registry and run `/plugin marketplace add <url>` first.)

### Step 3 — Tier 3: PM execution (pm-skills, 8 plugins)

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

### Step 4 — Tier 4: Anthropic skills (file formats)

```
/plugin install anthropic-skills@claude-plugins-official
```

### Step 5 — Tier 5: Development tools (install only what you'll use)

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

### Step 6 — Restart Claude Code, then verify

After install, restart Claude Code so all plugins activate. Then:

```
"Run a tier check — invoke rtp-aipm-orchestrator and have it list installed plugins by tier, flagging any gaps from the RTP ecosystem map."
```

The orchestrator will read its `FULL ECOSYSTEM AWARENESS` section in `rtp-personal-skills:rtp-aipm-orchestrator/SKILL.md` and report what's complete vs missing.

---

## After the user reports done

When the user says "done" or shows you `/plugin list` output:

1. Compare their installed plugins against `companion-plugins.json` at the repo root
2. Confirm Tier 1 + Tier 2 are fully installed (these are the load-bearing tiers)
3. Note any optional Tier 3-5 plugins they skipped — that's fine, but flag what capabilities they're missing
4. Suggest invoking the orchestrator for a real task to confirm the ecosystem works end to end

## If something fails

If a marketplace add fails (URL not found, etc.), the user should:
1. Check Claude Code's official plugin registry for the current source URL
2. Update `companion-plugins.json` and `COMPANION-PLUGINS.md` with the correct URL
3. Commit + push so the next account doesn't hit the same issue

The whole point of this manifest is that it stays accurate. Stale URLs are the #1 way the bootstrap rots over time.
