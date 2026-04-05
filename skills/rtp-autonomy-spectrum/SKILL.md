---
name: rtp-autonomy-spectrum
version: 3.0.0
author: RTP (Ravi Teja Palanki)
plugin: rtp-agent-design
updated: April 5, 2026 (v3.0: comprehensive product intelligence map, model-agnostic design pattern, Descript exemplar)
description: >
  Choose the right level of AI autonomy for every interaction — from autocomplete to
  multi-agent systems. Use when someone says "let's build an agent", when designing any
  AI product, when evaluating competitors, or when deciding how much control to give AI.
  The core question: who decides what happens next — the code or the model? This skill
  gives you the 7-level spectrum to answer that for every feature, not just the product.
  Do NOT use for: evaluating model quality (use eval-framework), testing outputs
  (use stress-test), or incident response (use safety-by-design).
imports:
  - determinism-compass
  - tool-architecture
frameworks:
  - name: "The Agent Spectrum"
    source: "AI Fluent — Ravi Teja Palanki (2026)"
    canonical: "../../frameworks/governance/autonomy-ladder.md"
  - name: "Four-Friction Model"
    source: "Telang, Hydari, Iqbal — HBR (2026)"
    canonical: "../../frameworks/governance/four-friction-model.md"
  - name: "Autonomy Ladder (Sema4.ai adaptation)"
    source: "Sema4.ai Research (2025)"
---

# Autonomy Spectrum
**Place every AI interaction at exactly the level it deserves — not the highest.**

> "Autonomy is a design decision, not a capability decision. Target the right level — not the highest." — RTP, The Agent Spectrum (2026)

---

## DEPTH DECISION

**Go deep if:** You're designing a new AI product, building multi-agent systems, shipping to production with real consequences, or implementing progressive trust escalation.

**Skim to The Seven Levels if:** You need a quick classification of where your product sits, or evaluating a competitor.

**Skip if:** Pure advisory systems (read-only, no actions), regulatory approval already in place, or the AI takes zero actions.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md):
1. Ask the Grounding Questions (Section 1) — at minimum: Who is the customer? What problem? What are we saying YES to and NO to?
2. Route depth: Executive Summary or Comprehensive Analysis?
3. Identify output format: Document, presentation, spreadsheet, or inline?

Then proceed with the skill-specific analysis below.

---

## THE TRAP

**You reverse-engineer autonomy from capability:** "The model CAN do X, so let's let it do X." This is backwards. Start with the consequence of failure: "If the AI does X wrong, what's the damage? Who absorbs it? Can we undo it?"

The trap is most seductive when:
- A competitor ships a "fully autonomous" feature and your team wants to match it
- The demo is impressive and leadership says "make it do everything"
- The model keeps getting better, so you keep raising autonomy without raising governance
- Someone says "just let the AI handle it" to avoid building proper UX
- The model is expensive to run, so teams assume higher autonomy = cost savings (wrong; it increases operational cost)

**The deeper trap:** Treating autonomy as a single number for your whole product. GitHub Copilot isn't "Level 4" — it's Level 1 (autocomplete), Level 3 (chat), and Level 6 (Workspace) simultaneously. The PM question is never "what level is our product?" It's "what level is each interaction? What would go wrong if the AI failed here? And who decides whether that's acceptable?"

---

## THE SEVEN LEVELS — The Agent Spectrum

Every AI system sits somewhere on this spectrum. The dividing line between Levels 1-4 and Levels 5-7 is the structural shift: below the line, **code controls the workflow**. Above the line, **the model controls the workflow**. Everything changes at that boundary — cost, failure modes, monitoring requirements, user expectations.

### Level 1: AI Feature — Code, Always

**Identity:** Predetermined responses. Enhances a single action. No LLM reasoning required.
**Who decides:** Entirely the code. The AI generates a prediction at a pre-determined moment. The user accepts or ignores.

**2026 Examples:**
- **Gmail Smart Compose** — Predicts your next few words as you type. Press Tab to accept. You never interact with the AI directly.
- **Grammarly inline corrections** — Underlines errors, suggests fixes. You click to accept or ignore.
- **Spotify Discover Weekly** — AI curates a playlist. You listen or skip. No conversation, no planning.

**Cost:** <$0.01 per interaction. Runs on lightweight models or embeddings.
**What breaks:** Awkward or inappropriate suggestions. Low stakes — user always reviews.
**Governance need:** Minimal. Logging optional. No kill switch needed.

You wouldn't call Smart Compose an "agent." But you'd be surprised how many products at this level get marketed as one.

---

### Level 2: Chatbot — Code, via Decision Trees

**Identity:** Branching logic. Routes queries via scripted paths. LLM optional — may use one for natural language understanding, but the flow is coded.
**Who decides:** The code. Chatbots follow decision trees, match intents, or retrieve from a knowledge base. Off-script → handoff to human.

**2026 Examples:**
- **Most customer support bots** — "I can help with orders, returns, or shipping. Which one?"
- **Supabase AI assistant** — Scoped to documentation and database queries. Structured, bounded, reliable. Answers what it knows, admits what it doesn't.
- **Bank FAQ chatbots** — Route to the right article or policy. Don't make decisions.

**Cost:** $0.01–0.03 per interaction.
**What breaks:** "I'm sorry, I don't understand. Would you like to speak to a representative?" That's the chatbot hitting the edge of its decision tree.
**Governance need:** Low. Content review of knowledge base. No action-level monitoring needed.

---

### Level 3: AI Assistant — Human Directs, AI Responds

**Identity:** Conversational AI. Understands context, handles multi-turn dialogue, generates original content. But fundamentally reactive — it does what you ask, then waits.
**Who decides:** You. The assistant responds to your direction. You decide what to ask, when, and what to do with the answer. Close the tab and nothing happens.

**2026 Examples:**
- **ChatGPT (basic mode)** — You ask, it answers. Draft an email, summarize a report, explain a concept. Each interaction: you prompt, it responds.
- **Perplexity (search mode)** — You ask a question, it searches, synthesizes, cites sources. But YOU initiated, YOU direct follow-ups, YOU decide what to do with the answer.
- **Claude.ai (conversational)** — Rich multi-turn dialogue with artifacts, but always user-directed.

**Cost:** $0.01–0.05 per interaction. Higher for long conversations.
**What breaks:** Hallucinations. Confidently wrong answers. But consequences limited because humans review everything.
**Governance need:** Moderate. Content safety filters. Citation accuracy for search assistants.

**Key difference from chatbot:** A chatbot says "I can help with A, B, or C." An assistant says "tell me what you need" and handles a much wider range. But both are reactive — both wait for you to drive.

---

### Level 4: Copilot — Human Decides, AI Suggests

**Identity:** Side-by-side partner embedded in your workflow. Sees your work context, makes proactive suggestions. You remain in control — it suggests, you decide.
**Who decides:** You — but the AI is more active than an assistant. It sees your context and offers help without being asked. The critical word is *suggests*. It doesn't act without approval.

**2026 Examples:**
- **GitHub Copilot (autocomplete)** — Reads your file, your function names, your comments. Suggests next lines. You press Tab or keep typing. Never writes a file, never commits code.
- **Cursor Tab** — Same pattern in a dedicated AI editor. Context-aware suggestions, but always human-approved.
- **Notion AI (inline)** — Helps you write, summarize, or brainstorm within a page. Suggests, you edit.

**Cost:** $0.01–0.10 per interaction. Higher when processing large context.
**What breaks:** Suggestions that look right but contain bugs. The risk is subtler — because the suggestion *seems* good, humans may accept without scrutinizing. This is where judgment atrophy begins.
**Governance need:** Moderate. Quality monitoring. Track acceptance rate (too high = rubber-stamping).

**Why "Copilot" was a brilliant brand name:** It manages expectations. A copilot assists the pilot — the pilot remains in command. When products branded as "copilots" start adding agent features, the branding creates confusion.

---

### ⚡ THE STRUCTURAL SHIFT — Code Control vs Model Control

**LEVELS 1-4 (BELOW): CODE CONTROLS THE WORKFLOW**
- What happens: You write rules that say "when X happens, do Y." The AI generates predictions/suggestions, but the rules decide what actually happens.
- Who approves actions: Humans. Every real consequence requires human decision.
- If the AI fails: You see it immediately. A wrong suggestion looks like a wrong suggestion. Humans can reject it.
- Governance: Moderate. You're checking outputs, not monitoring decisions.
- Cost failure: Expensive to prevent, but bounded in scope.

**VISUAL ANALOGY:** Like a co-pilot who makes suggestions but the pilot always has hands on the wheel. If the co-pilot suggests something dangerous, the pilot can ignore it immediately.

---

**LEVELS 5-7 (ABOVE): THE MODEL CONTROLS THE WORKFLOW**
- What happens: You tell the AI "achieve this goal" and it decides what to do, in what order, using which tools, without asking permission.
- Who approves actions: The AI, subject to guardrails you set up in advance.
- If the AI fails: You might not know for hours. A multi-step plan can compound errors. By the time humans notice, the damage may have cascaded.
- Governance: Very high. You're no longer checking outputs — you're monitoring decisions, trying to catch problems before they propagate.
- Cost failure: Can be catastrophic if the wrong decision gets automated at scale.

**VISUAL ANALOGY:** Like hiring a new team member who has a job description and authority limits, but then works independently. You don't approve every email they send or every decision they make. You've hired them, set expectations, and now trust the system to catch problems.

**EVERYTHING CHANGES AT THIS LINE:**
- **Cost**: Jumps 10-100x because you need 24/7 monitoring, rollback systems, and kill switches.
- **Failure mode**: Shifts from "wrong suggestion" (human catches it) to "wrong action taken" (cascades before anyone notices).
- **Monitoring**: Shifts from "check outputs" (sampled review) to "watch decisions" (real-time alerting, pattern detection).
- **User expectation**: Shifts from "it helps me work" to "it works for me while I oversee it."
- **Liability**: Shifts from "the human chose to accept bad advice" to "the AI made a decision we need to explain and potentially reverse."

**This is the line most teams underestimate.** Crossing it isn't a feature upgrade — it's an architecture change. It requires different infrastructure, different monitoring, different organizational structure.

---

### Level 5: Agent — AI Decides, Within Boundaries

**Identity:** Bounded autonomy. Receives a goal, plans multi-step execution, uses tools, makes decisions. Operates within defined guardrails.
**Who decides:** The AI controls the workflow. You set the goal and boundaries. The agent decides what to do, in what order, using which tools.

**2026 Examples:**
- **Claude Cowork** — You give it a task ("create a project plan", "research this topic", "organize these files"). It plans, uses tools (file system, browser, search), executes multi-step work within your workspace boundaries. You see what it does and can intervene.
- **Notion AI 3.0** — Tell it "Create a project launch plan, break into tasks, assign to team." Works autonomously for up to 20 minutes — creating pages, analyzing workspace, drafting documents. You set the destination, it drove.
- **Harvey AI** — Legal analysis within structured boundaries. Reads case law, identifies relevant precedents, drafts analysis. Operates within legal domain guardrails. Lawyers review output, but the analysis path was AI-decided.
- **Perplexity Deep Research** — You ask a complex research question. It plans a multi-step search strategy, reads dozens of sources, synthesizes findings, and presents a structured report. The research strategy was the model's decision.

**Cost:** $0.10–0.50 per interaction. Multiple LLM calls (5-20), substantial context processing.
**What breaks:** Misinterprets your goal. Takes unexpected actions (assigns task to wrong person, creates document with incorrect data). Because it operated autonomously, you may not catch errors until someone else does.
**Governance need:** High. Four-friction audit required (Identity, Context, Control, Accountability). Kill switch accessible. Action logging mandatory. Human review of high-stakes outputs.

---

### Level 6: Autonomous Agent — AI Decides, Humans Monitor

**Identity:** Self-directed worker. Operates independently on complex, extended tasks. Handles not just individual tasks but ongoing responsibilities. Adapts approach based on results.
**Who decides:** The AI, with guardrails. Humans set up constraints and monitor outcomes — but don't approve individual actions. This is delegation, not collaboration.

**2026 Examples:**
- **Claude Code** — Give it a GitHub issue or feature request. It reads the entire codebase, creates a plan, writes code across multiple files, runs tests, iterates when tests fail, commits changes. The entire sequence happens without human involvement. You review the PR at the end.
- **Devin 2.0 (Cognition)** — End-to-end software engineering. Takes a task, researches, plans, codes, tests, debugs, and produces a PR. Operates over hours, not minutes.
- **OpenAI Codex (async mode)** — Receives coding tasks asynchronously, works in a sandboxed environment, produces results. Humans check outputs periodically, not per-action.
- **Replit Agent** — Builds entire applications from natural language descriptions. Creates file structure, writes code, configures deployment. Autonomous creation within the Replit environment.

**Cost:** $0.50–$50+ per task. Long reasoning chains, multiple tool calls, potential retries.
**What breaks:** Error-compounding math bites hardest here. A 20-step task at 95% per-step accuracy has only 36% chance of being completely correct. Autonomous agents can confidently complete a task with a fundamental flaw. The risk isn't loud failure — it's quiet failure. Claude Code is known to mark features "complete" without proper testing.
**Governance need:** Very high. Comprehensive audit trails. Deterministic validation layers. Consequence magnitude mapped per task type. Regular human checkpoint reviews. Context anxiety monitoring (agents make hasty decisions as context fills).

---

### Level 7: Multi-Agent System — Distributed AI Decisions

**Identity:** Agent orchestra. Multiple specialized agents coordinate, delegate, hand off work, and may negotiate with each other. No single agent controls the whole process.
**Who decides:** Distributed. A supervisor agent may coordinate, but each agent makes autonomous decisions within its domain.

**2026 Examples:**
- **OpenAI Codex App (multi-agent)** — Multiple coding agents can be assigned parallel tasks from the same codebase. Each works independently, and results are coordinated.
- **Salesforce Agentforce** — Service Agent resolves complaint → triggers Marketing Agent for retention offer → notifies Sales Agent to flag account. Cross-domain coordination.
- **Microsoft AutoGen** — Research framework where multiple agents conduct research, debate findings, synthesize conclusions.
- **Enterprise AI workflows** — Claims processing: Intake Agent (reads documents) → Verification Agent (checks policy) → Decision Agent (approves/denies) → Communication Agent (drafts response). Each agent specialized, coordinated by orchestrator.

**Cost:** $1–$20,000+ per workflow. Multiply single-agent cost by agent count, plus coordination overhead.
**What breaks:** Everything that goes wrong with a single agent, multiplied, plus new failure modes: miscommunication between agents, conflicting actions, cascading errors where one agent's mistake becomes another agent's input. Second-order prompt injection (Agent A passes malicious data to Agent B). This is the frontier — powerful in demos, fragile in production.
**Governance need:** Maximum. Network segmentation between agents. Independent audit per agent. Cascade failure detection. Kill switch per agent AND for the system. Human oversight of inter-agent handoffs.

---

## THE SPECTRUM AT A GLANCE

| Level | Type | Who Decides? | 2026 Product Example | Cost per Interaction | Governance Need |
|:---:|:---|:---|:---|:---:|:---:|
| 1 | AI Feature | Code, always | Gmail Smart Compose | <$0.01 | Minimal |
| 2 | Chatbot | Code, via decision trees | Supabase AI, support bots | $0.01–0.03 | Low |
| 3 | AI Assistant | Human directs, AI responds | Perplexity search, ChatGPT | $0.01–0.05 | Moderate |
| 4 | Copilot | Human decides, AI suggests | GitHub Copilot, Cursor | $0.01–0.10 | Moderate |
| — | **⚡ STRUCTURAL SHIFT** | **Code controls ↑ / Model controls ↓** | | | |
| 5 | Agent | AI decides, within boundaries | Claude Cowork, Harvey AI | $0.10–0.50 | High |
| 6 | Autonomous Agent | AI decides, humans monitor | Claude Code, Devin 2.0 | $0.50–$50+ | Very High |
| 7 | Multi-Agent System | Distributed AI decisions | Codex App, Agentforce | $1–$20,000+ | Maximum |

**The pattern:** As you move up, three things happen simultaneously — flexibility increases, cost increases, predictability decreases. That's the fundamental tradeoff.

---

## THE PRODUCT INTELLIGENCE MAP — Who's Actually Shipping What in 2026

Most products don't sit at a single level. They span multiple levels simultaneously — each interaction designed at the autonomy level it deserves. This is the critical PM insight. Every winning product in 2026 is multi-level by design.

For each product below: **what does the AI decide?** What does the **human decide?** What **actions** does the system take? Where does each **capability** sit on the spectrum?

---

### 🔵 DEVELOPER TOOLS

**GitHub Copilot (Microsoft) — The Multi-Level Blueprint**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Tab Autocomplete | 1 | Accept/reject suggestion | Predict next code tokens | Inserts code at cursor |
| Copilot Chat | 3 | What to ask, whether to apply | Understand codebase, generate explanation/code | Displays answer in chat panel |
| Copilot Workspace (Issue→PR) | 6 | Approve final PR, set issue scope | Plan implementation, write code across files, run tests, iterate on failures | Creates branch, commits code, opens PR |

**PM lesson:** Three completely different autonomy contracts in one product. Users understand the boundaries because the UI makes each mode explicit. Tab = passive. Chat = reactive. Workspace = delegated.

**Cursor — Progressive Autonomy in the Editor**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Inline predictions (Tab) | 1 | Accept/ignore | Predict next code from context | Inserts at cursor |
| Cmd+K inline edit | 4 | Describe change, approve diff | Generate code transformation | Shows diff, applies on approval |
| Composer (multi-file) | 5 | Describe feature, review plan | Plan across files, determine which files to change | Edits multiple files per plan |
| Agent mode | 5-6 | Define goal, set boundaries | Research codebase, plan steps, execute, debug | Reads files, writes code, runs terminal commands, iterates |

**PM lesson:** The L1→L4 transition is smooth (same editing paradigm). L4→L6 requires explicit trust-building — Cursor introduced Agent mode as a beta toggle, not a default. Early adopters = power users. Mainstream adoption requires proven reliability.

**Lovable.dev — From Prompt to Deployed App**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Visual Edits (click-to-modify) | 3 | Click element, describe change | Generate CSS/component update | Modifies UI in real-time |
| Plan Mode (collaborative) | 4 | Describe intent, iterate | Suggest architecture, debug approach | Proposes code, waits for approval |
| Agent Mode (autonomous build) | 5-6 | Define app concept, set stack | Explore codebase, plan structure, write React/TypeScript/Tailwind, connect Supabase, deploy preview | Creates full-stack app autonomously |

**PM lesson:** $6.6B valuation, $200M ARR. Enterprise customers (Klarna, Uber). Lovable succeeds because Visual Edits (L3) anchors trust — users see changes immediately. Agent Mode (L5-6) is the growth engine but Plan Mode (L4) bridges the gap. Users who start in Visual Edits graduate to Agent Mode after building confidence.

**Claude Code (Anthropic) — Fully Autonomous Engineering**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Single-file edit | 5 | Describe change, approve | Understand codebase context, generate edit | Modifies file |
| Issue-to-PR (full) | 6 | Assign issue, review final PR | Read entire codebase, plan implementation, write code, run tests, iterate on failures, commit | Creates files, runs tests, commits, opens PR |
| Parallel tasks (Codex) | 7 | Assign multiple tasks | Each agent independently plans, codes, tests | Multiple PRs from parallel agents |

---

### 🟢 KNOWLEDGE & RESEARCH

**ChatGPT (OpenAI) — Six Tools, Six Autonomy Levels**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Basic chat | 3 | Ask question, evaluate answer | Generate response from knowledge | Displays text/code/images |
| Web Search | 3 | Trigger search or AI auto-triggers | Choose search queries, synthesize results | Searches web, cites sources |
| Canvas (document editor) | 4 | Direct edits, approve suggestions | Suggest structure, rewrites, code improvements | Opens side-by-side editor |
| Deep Research | 5 | Define research question | Plan multi-step search strategy, read 100+ sources, synthesize 5-30 min report | Produces analyst-grade research document |
| Agent Mode (formerly Operator) | 5-6 | Define task, set boundaries | Navigate websites, fill forms, reason through multi-step workflows | Browses web, takes actions on websites, completes tasks |
| Image Generation (DALL-E) | 3 | Describe image, iterate | Interpret prompt, generate visual | Creates image |

**PM lesson:** ChatGPT's Tools dropdown is a masterclass in progressive disclosure. Users choose their autonomy level explicitly. Most stay in L3 chat. Deep Research (L5) and Agent Mode (L5-6) are clearly positioned as "more powerful, takes longer, costs more." The UI communicates autonomy boundaries without technical jargon.

**Perplexity — Search to Agent Spectrum**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Quick Search | 3 | Ask question | Search, synthesize, cite | Displays answer with sources |
| Model Council | 3-4 | Ask question, compare outputs | Multiple models (GPT-5, Claude 4.6, Gemini) generate independent answers | Shows side-by-side model responses |
| Perplexity Computer (screen vision) | 4 | Show screen, ask question | Analyze visible UI, suggest actions in context | Proposes actions based on what it sees |
| Deep Research | 5 | Define complex research question | Plan multi-step research, read 50+ sources, synthesize structured report | Produces comprehensive research document |
| Comet Browser (mobile agent) | 5 | Define task within browser | Navigate web pages, extract information, complete workflows | Takes actions within Chromium browser |
| Spaces (collaborative research) | 4-5 | Define research direction, iterate | Explore research threads, maintain context across sessions | Builds persistent research workspace |

**PM lesson:** Perplexity's Model Council is a Level 3-4 innovation that gives users *choice without autonomy*. Instead of trusting one model, users see how GPT-5, Claude, and Gemini each answer — then decide for themselves. This is governance through transparency. Users who discovered they preferred Claude for code and Gemini for visual tasks are more informed customers.

**NotebookLM (Google) — Intentional Level 3-4 Focus**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Source Q&A | 3 | Upload sources, ask questions | Reason over uploaded material, cite specific passages | Answers grounded in your documents only |
| Audio Overview (podcast) | 3-4 | Select sources, choose format (deep dive/brief/critique/debate) | Generate conversational podcast script from sources, synthesize themes | Creates 15-min audio discussion |
| Interactive Mode | 4 | Interrupt audio, ask follow-up | Pause discussion, answer question from sources, resume flow | Real-time Q&A within podcast |
| Studio (flashcards/quizzes/mind maps) | 3 | Select output type | Generate study materials from sources | Creates flashcards, quizzes, slide decks, infographics |

**PM lesson:** NotebookLM is deliberately kept at Level 3-4. The product is "help you understand complex material" — not "automate your learning." Going to Level 5 (autonomous research beyond your sources) would violate the core value proposition: everything is grounded in YOUR documents. This is focus as competitive advantage.

---

### 🟡 CREATIVE & CONTENT

**Descript Underlord — The Model-Agnostic Design Pattern ⭐**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Transcript-based editing | 3 | Edit transcript text, AI syncs video | Maintain video-transcript sync | Cuts/rearranges video to match text edits |
| Auto-captions/filler word removal | 2 | Approve generated captions, accept/reject edits | Detect filler words, generate captions | Marks filler words, generates subtitle track |
| Underlord AI Co-Editor | 4-5 | Describe editing intent ("make this punchier"), choose AI model, approve plan | Plan multi-step edit sequence, explain reasoning, self-correct | Proposes edits, executes approved changes |
| Model Picker | — | Select which model powers Underlord (Claude, GPT, Gemini) | Each model handles different parts of the agent | Swaps underlying model without changing UX |

**⭐ WHY DESCRIPT IS THE EXEMPLAR: Designing for Model Version**

Descript built something most AI products haven't: **a product that automatically gets better when models improve — without any product redesign.**

Here's why this matters:

1. **Model-agnostic infrastructure:** Underlord's LLM layer is provider/model agnostic. Different models handle different parts of the agent. When Anthropic releases a better Claude, or OpenAI ships a better GPT, Descript swaps the model and the product improves. No feature rewrite. No UX change. No migration.

2. **Model Picker gives users control:** Users choose which model powers their editing. Claude Sonnet 4.6 for precise multi-step workflows. Gemini 3.1 Pro for complex creative tasks. GPT-5.4 for general editing. The user picks based on their task — not locked into one vendor.

3. **The evaluation challenge is the moat:** Video editing is subjective. "Better" depends on the final project, not individual tool calls. Descript invested heavily in evaluation infrastructure to compare models across real editing workflows — this evaluation capability is harder to copy than the product features.

4. **20% cost reduction through model intelligence:** Underlord v2 uses 20% fewer AI credits per full video edit because better models = fewer retries = lower cost. The product literally gets cheaper to run as models improve.

**The design principle:** Don't build your product around a specific model's capabilities. Build it around the TASK the user wants to accomplish, with a model-agnostic layer underneath. When models improve, your product improves. When a model vendor has an outage, you swap to another. This is resilience + automatic improvement.

**Gamma — Focused L3-4 Creative Tool**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Generate deck from prompt/outline | 4 | Provide topic/outline, select template | Generate slide content, choose layout, select images | Creates full presentation |
| Agent 3.0 (research + generate) | 5 | Define topic, review output | Research web, refine content, restyle entire deck through conversation | Produces research-backed presentation |
| Design feedback | 3-4 | Ask "make this more executive" | Analyze design, suggest improvements | Modifies styling/layout |
| Generate API (programmatic) | 5 | Define template + data source | Generate content at scale from API calls | Batch-creates presentations |

**PM lesson:** 70M users, $100M ARR, $2.1B valuation. Gamma's L3-4 anchor (generate deck, you edit) is where most users live. Agent 3.0 (L5) is the power feature for paying users. Intentional cap: board presentations are high-stakes. Users need to review every slide. The speed gain from L6 automation isn't worth the risk of one bad slide in front of the board.

**ElevenLabs — Three Pillars, Three Autonomy Ranges**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Text-to-Speech (ElevenCreative) | 2-3 | Input text, select voice, adjust parameters | Generate speech with emotion/intonation | Produces audio file |
| AI Dubbing (29 languages) | 4 | Select source video + target languages, review output | Analyze speakers, preserve voice characteristics, translate, lip-sync | Produces dubbed video maintaining original voice identity |
| Voice Cloning | 3 | Provide audio samples, approve clone quality | Learn voice characteristics from samples | Creates reusable voice profile |
| ElevenAgents (conversational AI) | 5 | Define agent persona, set conversation boundaries | Handle multi-turn voice conversations with emotional intelligence, turn-taking | Autonomous voice conversations with callers |
| Expressive Mode (v3 Conversational) | 5 | Set emotional parameters | Context-aware emotional speech synthesis + intelligent turn-taking | Real-time emotionally responsive voice agent |

**PM lesson:** $11B valuation, $500M raise Feb 2026. ElevenLabs shows autonomy tiering within a media domain: Text-to-Speech (L2-3) is the anchor. Dubbing (L4) requires human review of each language. ElevenAgents (L5) is where real autonomy lives — voice agents handling live phone calls. The jump from "generate audio file" to "conduct live conversation" is the L4→L5 boundary in action.

**Higgsfield — Model-Agnostic Video Infrastructure**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Text/image-to-video generation | 3-4 | Describe scene, select model (Kling 3.0, Veo 3.1, Sora 2) | Interpret prompt, generate video | Produces video clip |
| Cinema Studio (camera controls) | 4 | Set camera body, lens type, focal length, movements | Execute physical camera simulation with real optical physics | Generates cinematically controlled video |
| Character consistency (cross-scene) | 4-5 | Define character, set consistency constraints | Maintain character identity across multiple generations | Produces consistent character across scenes |
| Batch production (enterprise) | 5 | Define campaign brief, set brand guidelines | Generate multiple videos at scale within brand constraints | Produces batch of brand-consistent videos |

**PM lesson:** 15M users, $200M revenue in 9 months. Higgsfield, like Descript, is model-agnostic — integrating Kling, Veo, Sora, and FLUX in one platform. Users pick the best model for each task. This is the same design pattern as Descript's Model Picker: build for the task, not the model. When Sora 3 ships, Higgsfield adds it without product redesign.

---

### 🔴 PRODUCTIVITY & ENTERPRISE

**Microsoft 365 Copilot — Same Brand, Different Products, Different Levels**

| Product Variant | Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---|:---:|:---|:---|:---|
| **Copilot in Word** | Draft/summarize/rewrite | 3-4 | Describe what to write, review output | Generate content from prompt + document context | Inserts/modifies text in document |
| **Copilot in Excel** | Formula suggestions, data analysis | 3-4 | Ask question about data | Analyze spreadsheet, generate formulas/charts | Creates formulas, pivots, visualizations |
| **Copilot Researcher** | In-depth research reports | 5 | Define research topic | Search organizational + web data, synthesize multi-source report | Produces analyst-grade research document |
| **Copilot Researcher — Critique mode** | Verified research | 5+ | Define topic, choose Critique | One AI writes report, second AI independently checks accuracy/completeness/source quality | Produces research with independent verification layer |
| **Copilot Researcher — Council mode** | Multi-perspective research | 5-7 | Define topic, choose Council | Two models (GPT + Claude) each produce full report; third AI compares, shows agreements/disagreements | Produces multi-model comparative analysis |

**PM lesson:** Microsoft's "Copilot" brand spans L3-4 (Word/Excel helper) to L5+ (Researcher producing verified multi-model reports). Copilot Researcher's Council mode — where GPT and Claude independently analyze the same question and a third AI compares them — is the most sophisticated autonomy architecture in enterprise productivity. It's Level 5 individual agents coordinated into a Level 7 pattern. The brand "Copilot" now stretches from autocomplete to multi-agent research.

**Notion AI — From Add-On to Core Architecture**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| @ai inline (write/summarize/brainstorm) | 3 | Describe what to generate | Generate content from page context | Inserts text into page |
| Automate (workflow builder) | 2-3 | Define trigger conditions | Generate automation script | Executes automation when triggered |
| Built-in Agents (triage, meeting prep) | 5 | Enable agent, set parameters | Autonomous multi-step work: read databases, categorize, create pages, assign tasks | Modifies workspace autonomously for up to 20 min |
| Custom Agents (Feb 2026) | 5-6 | Define agent job description + triggers/schedule | Run autonomously 24/7 on schedule, triage with >95% accuracy, resolve 25%+ of tickets independently | Takes actions in workspace without human prompting |

**⭐ THE ADD-ON → CORE TRANSFORMATION:** Notion didn't add AI as a sidebar feature. They rebuilt the product from the ground up in Notion 3.0 (Sep 2025). AI isn't an add-on at $10/user — it's built into Business ($20/user) and Enterprise plans as a core capability. This is the difference between "AI-enhanced product" and "AI-native product." The Custom Agents feature (21,000+ built in beta) shows what happens when you integrate AI into the product's data model rather than bolt it onto the UI.

**Enterprise proof:** Remote's IT Ops saved 20 hours/week. Custom Agents triage with >95% accuracy and resolve 25%+ of tickets autonomously. That's L5-6 in production, at enterprise scale.

**Clay — AI-Native CRM Intelligence**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Data enrichment (150+ providers) | 3-4 | Define enrichment criteria, select providers | Waterfall across providers to find best data match | Enriches CRM records |
| AI web research (gap filling) | 4-5 | Define what data to find | Research web to fill gaps not in standard databases | Adds non-standard data to records |
| Claygent (MCP-connected agent) | 5 | Define agent workflow, connect to Salesforce/Gong/Google Docs | Autonomous multi-source enrichment with business context | Pulls data from multiple enterprise systems |
| Versioned AI agents (reusable across workflows) | 5-6 | Build agent, version it, deploy across workbooks | Execute enrichment workflows at scale with consistency | Processes millions of records autonomously |
| ChatGPT integration (account research) | 4 | Define research parameters | Conduct account/contact research, draft personalized emails | Produces enriched records + drafted outreach |

**PM lesson:** Clay shows AI at every level of a sales/marketing workflow. The anchor is L3-4 enrichment (structured, predictable). Claygent (L5) crosses the structural shift — it connects to Salesforce, Gong, Google Docs via MCP and makes autonomous enrichment decisions. The versioned agent system (L5-6) means you build once, deploy at scale, and the agent processes millions of records without per-record human approval.

**Wispr Flow — Deliberate Level 2-3 Focus**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Real-time transcription | 2 | Speak; dictation is always-on | Convert speech to text (97.2% accuracy) | Inserts text into any app |
| Auto-editing (filler removal, punctuation) | 2 | Enable/disable auto-edit preferences | Remove filler words, add punctuation, format based on context | Cleans transcription in real-time |
| Command Mode (voice editing) | 3 | Select text, speak command ("summarize this", "make formal") | Interpret voice command, transform text | Modifies selected text per voice instruction |
| Whisper Mode (discreet) | 2 | Activate whisper mode in shared spaces | Detect low-volume speech, maintain accuracy | Transcribes quiet speech |

**PM lesson:** Wispr Flow is HIPAA-ready, SOC 2 Type II compliant, 100+ languages, Hinglish support. $0 governance overhead because everything stays at L2-3. No autonomous actions, no multi-step reasoning, no decisions made by AI. This is deliberately boring, deliberately reliable. They chose "work perfectly in one narrow task" over "do many things with higher autonomy." The result: trusted in healthcare, legal, and enterprise — domains where L5+ products struggle to get compliance approval.

**Google Antigravity — Agentic IDE for PMs and Developers**

| Capability | Level | Human Decision | AI Decision | Action Taken |
|:---|:---:|:---|:---|:---|
| Chat (explain/debug) | 3 | Ask question about code/project | Analyze context, generate explanation | Displays answer |
| Editor view (focused work) | 4 | Describe edits needed | Suggest code changes with explanation | Shows diff for approval |
| Planning mode (complex tasks) | 5 | Define multi-step project goal | Break into steps, plan execution order | Creates structured plan, executes with approval |
| Agent Manager (parallel agents) | 6-7 | Assign multiple tasks, monitor dashboard | Multiple agents independently plan, code, debug, test | Parallel autonomous execution across tasks |

**PM lesson:** Antigravity saves PMs 10-20 hours/week by automating document creation, research analysis, meeting notes. But the key innovation is the Agent Manager — a centralized dashboard to monitor and control multiple parallel agents. This is L6-7 infrastructure: you don't approve each agent's actions, you monitor patterns across all agents simultaneously. The governance model is "air traffic control," not "co-pilot."

---

### THREE DESIGN PATTERNS EVERY PM MUST KNOW

**Pattern 1: Model-Agnostic Architecture (Descript, Higgsfield, Perplexity)**

Build for the TASK, not the MODEL. Descript's Underlord uses a mix of models (Claude, GPT, Gemini) — each handling different parts of the agent. Higgsfield integrates Kling, Veo, Sora, FLUX. Perplexity's Model Council shows users how different models answer the same question.

**Why this matters:** When the next model generation ships (GPT-6, Claude 5, Gemini 4), model-agnostic products improve automatically. Model-locked products need a feature rewrite. Descript already saw 20% cost reduction just from swapping to better models.

**The PM decision:** If your product's value depends on a specific model's quirks, you're building on sand. If it depends on the task being accomplished regardless of which model powers it, you're building on rock.

**Pattern 2: AI-as-Core vs AI-as-Add-On (Notion 3.0 vs the old Notion AI)**

Notion didn't sprinkle AI features onto an existing product. They rebuilt the entire architecture so AI is part of the data model, the workflow engine, and the collaboration layer. AI isn't a $10/month add-on anymore — it's a fundamental capability in Business/Enterprise plans.

**Why this matters:** Add-on AI = "nice to have, turn off if budget tight." Core AI = "the product doesn't work without it." Notion's Custom Agents (21,000+ built) only work because AI has access to the full workspace data model. An add-on couldn't do that.

**The PM decision:** Are you adding AI features to an existing product (faster time-to-market, lower risk, easier to kill) or rebuilding with AI at the core (slower, more expensive, but fundamentally more capable)? Both are valid — but they lead to very different autonomy ceilings.

**Pattern 3: Progressive Disclosure of Autonomy (ChatGPT, Cursor, Lovable)**

ChatGPT's Tools dropdown lets users explicitly choose: chat (L3), search (L3), canvas (L4), deep research (L5), agent mode (L5-6). Cursor starts with inline suggestions (L1), graduates to Cmd+K (L4), offers Agent mode as opt-in (L5-6). Lovable starts with Visual Edits (L3), bridges through Plan Mode (L4), then offers Agent Mode (L5-6).

**Why this matters:** Users build trust at each level before progressing. Nobody starts at L6. The products that tried (Rabbit R1, Humane AI Pin) failed because they demanded L5-6 trust from users who had zero L3 experience with the tool.

**The PM decision:** Design your autonomy roadmap. Start users at L3. Let them succeed there. Offer L4 as a natural next step. Only surface L5+ to users who've demonstrated they understand the tool and its boundaries.

---

## MAPPING YOUR PRODUCT — The Exercise

For each interaction in your product, fill this table:

| Interaction | Current Level | Human Decision | AI Decision | Actions Taken | Consequence if Wrong | Target Level |
|:---|:---:|:---|:---|:---|:---|:---:|
| [e.g., FAQ answers] | 2 | Which FAQ to consult | Route to correct article | Display answer | User gets wrong article (low) | 2 |
| [e.g., Returns processing] | 3 | Whether to approve return | Categorize reason, check policy, suggest resolution | Proposes action to agent | Wrong categorization (medium) | 5 |
| [e.g., Billing disputes] | 3 | All decisions | Draft response only | Displays draft | Bad draft (low — human reviews) | 3 |

**The target isn't "make everything an agent."** It's a deliberate mix. FAQ stays at L2 (cheap, reliable). Returns move to L5 (complex, high-volume, bounded consequence). Billing disputes stay at L3 (high stakes, needs human judgment).

---

## IMPLEMENTATION — Consequence Magnitude & Control Design

Once you've chosen the level for each interaction, design the operational controls based on **what could go wrong and how bad it is if it does.**

### Action Classification by Consequence Magnitude

| Category | Consequence | Examples | Control Requirement |
|:---|:---|:---|:---|
| **Reversible, low-magnitude** | Easily undone; cost <$1 if wrong; user notices immediately | Read files, fetch data, generate suggestions | Agent can act freely; logging optional |
| **Reversible, medium-magnitude** | Can be undone; cost $1-100 if wrong; user notices within hours | Modify in staging, create draft, reorganize files | Agent acts with mandatory logging; human audits within 24h |
| **Reversible, high-magnitude** | Undoable but costly; cost $100-10k if wrong; harm cascades | Database modification, send email to 100 people | Requires explicit human approval before action |
| **Irreversible, medium-magnitude** | Cannot be undone; cost >$10k; harm is permanent | Delete production files, post public comment, legal signature | Agent cannot access. Period. No exceptions. |
| **Irreversible, high-magnitude** | Cannot be undone; cost >$100k; legal/reputational consequence | Execute financial transfer, modify patient medical record, change legal document | Hardened against agent access entirely. Audit every human who can access. |

**The discipline:** Map every action your agent might take into this table. If it's irreversible and >$10k, the agent never sees it. Full stop.

### Leash Length — Progressive Autonomy Model

The "leash" defines how much the agent can do without human intervention. Design leash length based on demonstrated performance, domain, and consequence magnitude.

| Mode | Autonomy Model | When to Use |
|:---|:---|:---|
| **Supervised** (leash = 0) | Human reviews and approves EVERY decision | Learning phase; high-magnitude consequences; new domain; team lacks confidence |
| **Spot-check** (leash = task) | Agent executes task independently; humans audit random sample post-execution | Reversible actions; team has calibrated confidence; consequences are bounded |
| **Exception-based** (leash = domain) | Agent acts freely within domain; escalates only on low confidence (below 70%) or pattern anomaly | High-accuracy domain (healthcare triage, known legal precedent); failure costs are predictable; infrastructure exists to catch exceptions |
| **Autonomous** (leash = unlimited) | Agent decides and executes; humans monitor dashboards for anomalies | >99% accuracy track record; consequence magnitude <$10; or read-only operations; AND user explicitly consented to this level |

### Progressive Trust Escalation

Don't start at the leash length you want. Earn it through performance:

1. **Start in Supervised mode** (human approves every decision)
2. **After 10 correct decisions:** Move to Spot-check (50% of decisions audited)
3. **After 50 correct decisions:** Move to Exception-based (human reviews only anomalies)
4. **After 100 correct decisions:** Consider Autonomous IF consequence magnitude is low

**Rules:**
- Any error → reset streak. Start back 50% of the way (not to zero, to prevent burnout, but clearly regress).
- Never auto-raise autonomy beyond domain boundary (agent trained on insurance claims shouldn't auto-escalate to healthcare claims).
- Set explicit re-audit schedule: every 30 days, human re-certifies whether performance still justifies leash length.
- Expose performance to user: "Your AI assistant has made 247 decisions. 246 were correct (99.6%). Last error: [date]. Recommending exception-based leash for next 30 days." Transparency prevents surprise autonomy escalation.

### Context Anxiety Principle — Quality Degrades With Context Filling

As the agent's context window fills (more files to read, longer conversation history, more constraints), decision quality degrades **nonlinearly**. It doesn't stay stable until 100% and then crash. It degrades earlier.

| Context Utilization | Recommendation |
|:---|:---|
| 0-40% | Full autonomy at current leash level |
| 40-60% | Drop autonomy by 1 level (e.g., Autonomous → Exception-based) |
| 60-80% | Advisor-only mode (recommend, never execute; wait for human decision) |
| 80%+ | Read-only mode; agent cannot propose actions |

**Operational detail:** Set automated alerts. When Claude Code hits 65% context utilization, it should automatically shift to advisor mode and prompt the user: "I'm approaching context limits. I can see the problem but want your go-ahead before making changes. Here's my plan: [X]. Approve to proceed?"

### Rollback Architecture — Design Undo Before You Deploy

For every action the agent might take, define rollback capability BEFORE you deploy:

| Consequence Magnitude | Rollback Window | Mechanism | Example |
|:---|:---|:---|:---|
| Reversible, low | Immediate (5 min) | Built-in undo | Revert file, Cmd+Z, API delete |
| Reversible, medium | 24 hours | Backup + restore | Database transaction rollback, version control revert |
| Reversible, high | 7 days | Full audit trail + selective restore | Restore from daily snapshot, manual review of what to restore |
| Irreversible, medium+ | N/A | Not allowed | Never grant agent access |

**The rule:** Never grant agent autonomy to actions where rollback window = N/A. If you can't undo it in 24 hours, the agent doesn't have access.

---

## QUALITY GATE

Before shipping any AI feature, answer these:

- [ ] Every interaction type is classified by level (not the whole product as one number)
- [ ] Actions classified by consequence magnitude, not by capability
- [ ] Leash length matches demonstrated performance track record
- [ ] Confidence thresholds tied to empirical error rates, not intuition
- [ ] Kill switch accessible, tested, and documented
- [ ] Users can see and understand the autonomy level + how it was earned
- [ ] Audit trail is queryable by (agent, action, outcome, consequence magnitude, approved-by, timestamp)
- [ ] Context anxiety thresholds set and monitored (alert at 60%)
- [ ] Rollback mechanisms designed and tested per action class
- [ ] Escalation from Supervised → Spot-check → Exception-based → Autonomous based on track record

## WHEN WRONG

This skill gives bad advice when:

1. **Pure advisory domain** (read-only, zero consequence). Skip governance overhead — just let the agent analyze.
2. **Error distribution is non-stationary.** Confidence doesn't predict accuracy. Run eval-framework first.
3. **Users are intolerant of wait time.** Async approval breaks UX. Reduce consequence magnitude instead of adding gates.
4. **The team conflates "we want Level 6" with "we need Level 6."** Capability ≠ appropriateness. Most products need Level 3-4 with good UX.
5. **Regulatory environment mandates specific controls.** Use safety-by-design for compliance-first design.

---

## VOCABULARY BRIDGE

When your **engineer** says: *"Deterministic workflow or agentic loop?"* → They're asking: Level 2-4, or Level 5+?

When your **designer** says: *"What happens when AI does something unexpected?"* → They've identified the Level 4→5 UX challenge.

When your **data scientist** says: *"We need eval frameworks before shipping"* → At Level 5+, you can't just test outputs — you test the decisions the agent makes along the way.

When your **board member** says: *"Where are we on AI agents?"* → Don't say "we're building agents." Say: "We're at Level 2-3 today. Moving returns to Level 5 this quarter, exploring Level 5 for proactive outreach in Q3. Here's the investment."

---

## THE HARDWARE LESSON + THE SOFTWARE LESSON

**Hardware failure pattern:** Rabbit R1 and Humane AI Pin both promised Level 5-6 autonomy in a new form factor. Both failed. They asked users to adopt a new device AND trust new autonomy simultaneously. Compare: AirPods launched as great earbuds first, then added Siri (Level 1), then smarter features over time. Don't change two things at once.

**Software success pattern:** Every winning product in 2026 embeds AI into tools you already use. Notion AI lives in Notion. Copilot lives in VS Code. Wispr Flow works in every app. Descript's Underlord lives in your video editing workflow. The product that succeeds isn't the one with the highest autonomy — it's the one that meets users where they already work.

**The Descript principle:** Build your AI layer model-agnostic. When models improve, your product improves automatically. Descript didn't just add AI to video editing — they built infrastructure that lets them swap models, add new providers, and let users choose. The product gets better without a single feature redesign.

**PM principle:** Don't ask users to change their workflow AND increase AI autonomy AND learn a new tool at the same time. Change one thing at a time. Earn trust at each level before progressing.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 3.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create an Agent Spectrum visual. This diagram should show all 7 levels, the structural shift line, 2026 product examples, and the cost-governance tradeoff.

---

## REFERENCES

- **The Agent Spectrum** — AI Fluent, Ravi Teja Palanki (2026). The canonical framework.
- **Four-Friction Model** — Telang, Hydari, Iqbal (HBR 2026). Identity, Context, Control, Accountability.
- **Six Operational Principles for Agent Onboarding** — Joseph Fuller (Harvard Business School, 2026).
- **Autonomy Ladder** — Adapted from Sema4.ai Research (2025). Levels 0-5 for organizational deployment.
- **SAE Automation Levels (0-5)** — The self-driving industry's shared vocabulary. Analogous framework.
- **Context Anxiety Principle** — Anthropic Research (March 2026). Quality degrades at 50-60% context.

---

*Source: AI Fluent — The Agent Spectrum — Ravi Teja Palanki (2026)*
*Skill version: 3.0.0 | Plugin: rtp-agent-design | Last updated: April 5, 2026*
*v3.0: Product Intelligence Map with 15+ products, model-agnostic design pattern (Descript exemplar), three design patterns, precise capability/human/AI/action mapping per product*
