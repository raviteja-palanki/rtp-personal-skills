---
name: rtp-observability-stack
version: v1.0_latest
description: 'Choose and drive an AI observability platform without buying a data-model you cannot leave. Covers the decision most teams skip (what question is the telemetry answering?), instrumenting to the OpenInference/OTel standard so the vendor stays swappable, picking a backend on data gravity not features, and the traps that make trace tooling lie to you — index lag that hides your own fix, bulk exports that dump production PII to local disk, and "read-only" tools that write. Use when standing up observability, evaluating Arize AX vs Phoenix vs LangSmith, wiring the trace→eval→dataset→experiment loop, or auditing a setup before it touches regulated data. Pairs with: production-observability (what to monitor and why — read that first), eval-framework, eval-driven-development, gen-ai-experimentation. Triggers: "which observability tool", "Arize vs Phoenix", "LangSmith", "set up tracing", "instrument my agent", "OpenInference", "vendor lock-in on traces".'
imports:
  - production-observability
  - eval-framework
  - eval-driven-development
---

# Observability Stack

## DEPTH DECISION

**Quick pass (10 min)** — you already have a platform and just need the traps. Read THE SCENE, then REALITY CHECK.

**Full pass (60–90 min)** — you're choosing a platform, or auditing one before it sees production data. Run the whole PROCESS and fill the WHERE YOU ARE artifact.

Sibling boundary: `production-observability` answers *what to watch and why*. This skill answers *what to buy and how to drive it*. If you don't yet know which signals matter, read that one first — a platform won't tell you.

## THE TRAP

Teams treat the observability platform as a tooling choice. Reversible, cheap, argue about it later.

It isn't. The subscription is reversible. The instrumentation isn't. When you wire tracing into an agent, you touch every LLM call, every tool handler, every retriever. Do that against a vendor's proprietary SDK and the switching cost stops being a renewal negotiation and becomes a re-instrumentation project across your whole codebase. The bill is small. The exit is not.

### The deeper trap: the escape hatch is free and almost nobody takes it

There is an open standard underneath. **OpenTelemetry** carries the spans; **OpenInference** is the semantic convention that says what an LLM span looks like — `llm.input_messages`, `tool.name`, `retrieval.documents`, `session.id`. Instrument to the *standard* and the vendor becomes a backend you point at, not a decision you're married to.

This costs nothing at instrumentation time. It costs a rewrite afterward. That asymmetry is the whole reason this skill exists, and it's the one thing to get right in week one.

## KEY TERMS (plain language)

| Term | What it actually means |
|---|---|
| **Span** | One operation — an LLM call, a tool call, a retrieval. The atom. |
| **Trace** | A tree of spans sharing an ID. One user request, end to end. |
| **Session** | Several traces sharing a conversation ID. A multi-turn chat. |
| **OpenInference** | The open convention for what fields an LLM span carries. Your portability layer. |
| **OTLP** | The wire protocol spans travel over. Vendor-neutral. |
| **Data gravity** | Once traces live somewhere, evals, datasets and experiments accrete around them. That mass — not features — is what actually locks you in. |

## WHAT THIS SKILL CONSUMES & PRODUCES

**Consumes:** the decision the telemetry is meant to change · your deployment constraints (regulated data? air-gapped? who can see prompts?) · the existing framework, if any.

**Produces:** a backend choice with the reasoning written down · an instrumentation approach that survives changing your mind · a guardrail list before production data flows · the WHERE YOU ARE artifact below.

**Not this skill's job:** which metrics to alert on (`production-observability`), how to design the evals (`eval-framework`), or how to run the experiment (`gen-ai-experimentation`).

## THE SCENE: the afternoon you lose to a lie

You ship a prompt fix at 2pm. Reasonable next move: query the last hour of traces and confirm it worked.

Zero results.

So you assume the deploy broke ingestion. You roll back. You spend the afternoon reading exporter logs, checking API keys, adding print statements to the OTel pipeline. Nothing is wrong. The traces were there the entire time.

The reason is architectural, and no dashboard tells you: the store indexed by trace ID gets written on ingestion, but the **time-series index** that answers "show me the last hour" is built asynchronously behind it. Arize documents that lag at **6–12 hours** ◆ *(vendor-disclosed, in their own tooling docs — I have not measured it independently)*. A direct trace-ID lookup would have returned your fix in seconds. A time-range query was never going to.

The lesson generalizes past Arize. **Every trace platform has a fast path and a slow path, and the UI rarely tells you which one you're on.** Find out which is which on day one, or you will eventually debug a problem you don't have.

## THE PROCESS

### 1. NAME THE DECISION THE TELEMETRY CHANGES

Before evaluating anything, finish this sentence: *"When this is instrumented, I will be able to decide ______, which today I decide by guessing."*

If you can't finish it, you don't have an observability problem — you have a "we should probably have dashboards" instinct. Instrument anyway if you like, but know you're buying insurance, not answers, and size the spend accordingly.

**Why:** platform evaluations without a decision behind them collapse into feature-grid comparison, which every vendor wins.
**When this is wrong:** regulated deployments. If EU AI Act Art. 12 or NIST MAN-2.1 obliges you to keep event logs, the audit trail *is* the decision. Skip to step 3.

### 2. INSTRUMENT TO THE STANDARD, NOT THE VENDOR

Wire OpenTelemetry with OpenInference conventions. Point the OTLP exporter at whichever backend you're trying. Changing your mind later becomes an endpoint change instead of a refactor.

**Why:** it's the only decision in this list that's free now and expensive later.
**When this is wrong:** you need a vendor-specific capability that has no OTel expression, and you've confirmed it has no OTel expression rather than assuming. Rare. Verify before accepting it.

### 3. CHOOSE THE BACKEND ON DATA GRAVITY, NOT FEATURES

Three realistic shapes, and the honest reason to pick each:

| Option | Pick it when | The real cost |
|---|---|---|
| **Arize Phoenix** (open source, self-host) ◆ | Prompts or outputs can't leave your infrastructure. Regulated data, or enterprise review you'd rather not run. | You operate it. Storage, upgrades, retention are yours. |
| **Arize AX** (hosted) ◆ | You want the eval/dataset/experiment loop wired without building it, and sending trace content to a vendor is acceptable. | Trace content — including whatever PII sits in prompts — leaves your perimeter. That's a DPIA question, not a procurement one. |
| **LangSmith** ⚠ | Your app is already LangChain/LangGraph and you want the native fit. | Tightest to that ecosystem. Verify current OTel ingestion support before assuming portability — don't take my word or theirs. |

Same span shape underneath the Arize pair, so moving between them is an endpoint change if you followed step 2.

**Why:** features converge within two quarters. Where your traces live, and what accretes around them, doesn't.
**When this is wrong:** at genuinely small scale — under a few hundred traces a day — structured logs and a notebook beat all three. Adopt a platform when *reading the logs* is the bottleneck, not before.

### 4. WIRE THE LOOP, NOT JUST THE TRACES

Tracing alone gives you forensics. The compounding version is a loop: **trace → find the failures → make them a dataset → run experiments against it → keep the eval that catches the regression.**

If you land on the Arize toolchain, four of its thirteen skills carry that loop — `arize-instrumentation`, `arize-trace`, `arize-evaluator`, `arize-experiment`. The rest are situational; `arize-compliance-audit` matters only if you're facing an actual regulatory question, and it is guidance, not legal advice.

**Why:** teams that stop at traces re-debug the same failure class every month. The dataset is what makes a fix permanent.
**When this is wrong:** pre-product-market-fit, where the failure classes are still moving. Build the loop once failures repeat.

### 5. SET THE GUARDRAILS BEFORE PRODUCTION DATA FLOWS

Four defaults worth overriding, all verified first-hand by reading the Arize skill sources on 29 JUL 2026 ✅. Treat them as a template for auditing *any* trace tooling:

- **Exports auto-escalate.** A targeted export that hits its row limit re-runs unbounded without asking. Bulk production traces land unencrypted in your working directory. Decide where that directory is before you find out.
- **Spans carry PII by design.** `input.value`, `output.value`, `user.id`, and custom metadata like `user_email` are the point of tracing. Redact at the span processor, before the exporter fires — not after it's in the vendor's store.
- **"Read-only" tools write.** The trace skill also exposes bulk annotation — up to 1000 writes per request. Read the verbs, not the name.
- **Report paths default outside your control.** The compliance skill writes to `/tmp` by default, and a compliance report is a map of exactly where your secrets and PII live. Redirect it explicitly.

**Why:** each of these is a default someone chose for convenience, and every one of them is wrong for regulated data.
**When this is wrong:** never, for production. For a scratch project, ignore all four and move fast.

## DIAGNOSTIC QUESTIONS

1. If you switched vendors tomorrow, how many files change? (More than the exporter config means step 2 didn't happen.)
2. Which query path is fast, and which lags? Can you name the lag in hours?
3. What's in `input.value` on your highest-volume span, and would you be comfortable reading it aloud in a compliance review?
4. When a trace shows a failure, what's the path from there to a test that prevents it? How many manual steps?
5. Who can see production prompts today, and did anyone approve that?

## REALITY CHECK

**The five-minute audit.** Export one trace. Open the JSON. Look at `input.value` and `output.value` with the eyes of your DPO. Most teams discover they've been shipping customer PII to a vendor for months and nobody explicitly decided to.

**The claim that ages fastest.** Anything in this skill about a specific vendor's features. Re-verify before citing — this was written 29 JUL 2026 against tooling that ships to main continuously.

**Honest limits.** I verified the Arize skill sources directly ✅ and read their license and file contents. I have *not* independently measured the index lag, benchmarked any platform, run Phoenix, or tested LangSmith's current OTel support — those are marked ◆ vendor-disclosed and ⚠ unverified above, and should stay that way until someone measures them.

## WHERE YOU ARE — OUTPUT

```markdown
# Observability Stack: [Product]

## The decision this telemetry changes
[One sentence. If it's empty, say so — that's a finding.]

## Instrumentation
Standard: [OpenInference/OTel | vendor SDK — and why]
Files touched if we switch vendors: [count]

## Backend
Choice: [Phoenix | Arize AX | LangSmith | logs, not yet]
Chosen because: [data gravity / residency / ecosystem — not features]
Trace content leaves our perimeter: [yes/no] · Approved by: [name or NOT ASKED]

## Query paths
Fast path: [trace-ID lookup] · Lag: [none]
Slow path: [time-range] · Lag: [hours] · Source: [measured | vendor-disclosed]

## The loop
trace → [ ] dataset → [ ] experiment → [ ] regression eval
Broken at: [step]

## Guardrails
[ ] Export directory chosen deliberately
[ ] PII redacted at span processor, pre-export
[ ] Write-capable tools inventoried
[ ] Report/output paths redirected in-perimeter

## OPEN: decision-needed
[Anything above needing a human call — residency, DPIA, budget]
```

## QUALITY GATE

- Every vendor claim carries a tier: ✅ verified · ◆ vendor-disclosed · ⚠ unverified. No blending.
- The backend choice names a reason that isn't a feature.
- Someone has actually opened a raw span and read it.
- The output states what wasn't checked.

## WHEN WRONG

**You'll know this skill misled you if:** you followed the standard-first advice, then hit a genuine capability that has no OTel expression and had to instrument twice. That's the real cost of the recommendation, and it's a bet, not a certainty — the bet is that portability is worth more than the marginal feature, which holds for most enterprise teams and fails for teams doing something unusual enough that the vendor is the only one who's built it.

**Falsification condition:** if OpenInference adoption stalls and the vendors diverge into proprietary span shapes, step 2 stops buying portability and becomes ceremony. Watch for that.

## TRADE-OFF LEDGER

| We chose | We gave up | Because |
|---|---|---|
| Standard-first instrumentation | Some vendor-native ergonomics | The exit stays cheap |
| Data gravity as the deciding axis | Feature-grid rigor | Features converge; stored data doesn't |
| Guardrails before production data | A faster first week | Every default here is tuned for convenience, not regulated data |
| Naming vendor claims by tier | Cleaner-looking prose | A confident wrong number is the failure this corpus exists to prevent |

## CONCLUSION

The platform question feels like the decision. It isn't. The decision is whether your traces are written in a shape someone else owns.

Get that right and the vendor becomes an endpoint — swap it in an afternoon when the pricing or the roadmap turns. Get it wrong and you'll discover the real cost the first time you want to leave, which is exactly when you have the least appetite for a refactor.

**Monday move:** export one trace from whatever you're running today, open the JSON, and answer two things — how many files change if you switch vendors, and would you read `input.value` aloud in a compliance review. Both answers are findings.

## VISUAL SUMMARY

Invoke `excalidraw-svg` for: (1) the lock-in asymmetry — vendor-SDK instrumentation against OpenInference/OTel, with the switch cost drawn on each path (one endpoint config versus every call site); (2) the fast-path/slow-path split — primary trace store answering trace-ID lookups instantly, time-series index lagging behind it, and which question routes to which; (3) the compounding loop — trace → dataset → experiment → regression eval — drawn as a cycle with the usual break point marked between trace and dataset.
