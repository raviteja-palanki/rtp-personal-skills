<p align="center">
  <img src="diagrams/01-think-judge-craft.svg" alt="Think, Judge, Craft: the three layers of the system" width="950"/>
</p>

# rtp-personal-skills

This is my product judgment, written down and version-controlled.

Most PMs carry their thinking in their head, and it leaves when they do. I spent three years externalizing mine: **90 skills** that encode how I make AI product decisions. When AI is the right answer and when rules are cheaper. How much autonomy an agent has earned. What a real moat is. What to check before anything ships. An **orchestrator** composes them the way I would, so the system does not just store my judgment. It applies it.

## What's inside

| | | |
|---|---|---|
| **Think** | 24 skills | Is this even an AI problem? What bias makes it feel obvious? What is the user really hiring it for? |
| **Judge** | 32 skills | Autonomy, moats, pricing, safety, evals. The calls that earn the right to ship. |
| **Craft** | 11 skills | AI-PRDs, agent specs, cost models, launch gates. Documents that arrive pre-tested. |
| **Plus** | 22 skills | Writing, research, design systems, presentations, admin. |
| **Orchestrator** | 1 | Reads the situation, composes the right skills, reviews the output. |

11 commands chain skills into a single decision. 6 workflows run multi-step work in one realistic sitting. 3 framework references sit behind them. Full detail: [ARCHITECTURE.md](ARCHITECTURE.md).

## How it works

The orchestrator spawns specialist workers, runs them in parallel, and reviews everything before you see one answer:

<p align="center">
  <img src="diagrams/02-orchestrator-workers.svg" alt="The orchestrator spawns specialist worker agents and reviews their output" width="950"/>
</p>

Here is what that produces. One request, end to end:

<p align="center">
  <img src="diagrams/03-pretested-prd.svg" alt="A request becoming a pre-tested PRD, stage by stage" width="950"/>
</p>

## Why it works

- **Every rule states the conditions under which it fails.** Advice that does not know its limits is more dangerous than no advice, so nothing here ships without its failure condition.
- **Every number is tagged by how solid it is:** ✅ audited · ◆ company-disclosed · ⚠ reported. A forecast is never called a fact.
- **Everything reads in plain language.** If a framework term appears, a legend explains it. A system only compounds if the next reader, human or AI, understands it on first pass.

## Who built it

**Ravi Teja Palanki** — Senior Technical PM at Honeywell · Perplexity AI Fellow 2025. 12+ years shipping enterprise products at Fortune 100 scale, now shipping Gen AI into production for safety-critical industrial environments, where a hallucination is not an inconvenience. It is a compliance incident.

[ravitejapalanki.com](https://ravitejapalanki.com) · [LinkedIn](https://www.linkedin.com/in/ravipalanki) · ravi.aifluentproduct@gmail.com

## The full map

<p align="center">
  <img src="diagrams/skill-map.svg" alt="The full map: all 90 skills, named" width="1000"/>
</p>

<sub>The map is generated from the skills actually in this repo by [`diagrams/build-skill-map.py`](diagrams/build-skill-map.py), so it cannot quietly drift from what ships.</sub>

---

<sub>This is my personal operating system. Public so the work is visible, not packaged for reuse. All Rights Reserved. · September 2026</sub>
