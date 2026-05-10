---
name: rtp-gen-ai-experimentation
description: 'Use when planning gen-AI experiments, structuring pilots vs A/B tests, or validating productivity gains before scaling. Design and run organisational experiments to validate gen AI before scaling. Covers the Productivity J-Curve, how to structure experiments vs pilots vs A/B tests, causal vs correlational insights, ecosystem experimentation, and how to build an internal experimentation capability. Triggers: ''gen AI experiment'', ''AI pilot design'', ''productivity J-curve'', ''organisational experiment'', ''test AI before scaling'', ''AI adoption testing'''
---
# Gen AI Experimentation

## DEPTH DECISION

**Go deep if:** You are deciding whether to scale a gen AI tool, designing a structured test to validate AI impact before a broad rollout, or building your organisation's internal experimentation capability.

**Skim to the experiment design checklist if:** You have a clear hypothesis and just need to structure the test correctly.

**Skip if:** You've already validated the use case with rigorous data and are in scale-up mode — switch to eval-driven-development for ongoing quality.

## GROUNDING (Before Starting)

Follow the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md).

---

## THE TRAP

Most organisations call something an "experiment" when it is actually a pilot. That distinction is not semantic — it determines whether you learn anything you can act on.

A pilot answers the question: "Can our best users make this tool work?" An organisational experiment answers the question: "Will this tool improve performance for our actual workforce, under real conditions, at scale?"

The gap between those two questions is where AI rollouts die. A successful pilot creates enthusiasm. A successful experiment creates evidence. Enthusiasm is not enough to justify a £2M deployment.

| | Pilot | A/B Test | Organisational Experiment |
|---|---|---|---|
| Participants | Handpicked enthusiasts | Random sample from digital channel | Random assignment or staggered rollout across the organisation |
| Hypothesis | Absent ("let's try it") | Narrow feature variant | Explicit and testable, covering workflow and human impact |
| Control group | None | Yes, for the feature variant | Yes — essential |
| What you learn | "Our best users liked it" | Which variant performs better on one metric | Causal impact on real-world performance, adoption, and satisfaction |
| Scaling decision basis | Enthusiasm and anecdotes | Statistical lift on one metric | Effect sizes, segment breakdowns, cost at scale |
| What it misses | Almost everything | Coordination, workflow, culture effects | Nothing designed to be missed |

A/B tests are a step forward from pilots but still fall short for gen AI — they capture feature-level signal, not the broader effects on how teams coordinate, how workflows shift, and how different employee segments experience the change.

---

## The Productivity J-Curve

> **Attribution:** This concept was developed by the research team (Berndt, Englmaier, Sadun, Tamayo, von Hesler) in their HBR analysis of gen AI adoption, drawing on economic history research by Paul David on electricity adoption. Published HBR, January–February 2026.

Organisations adopting gen AI almost always experience an **initial dip in productivity before sustained gains**. This is the Productivity J-Curve — and it is not a failure signal. It is a structural consequence of how general-purpose technologies get absorbed.

```
Performance
    │
    │                                          ╱╱╱ Sustained gains
    │                                       ╱╱╱
    │                                    ╱╱╱
    │         ───────────────────────╱╱╱
    │         ↑ Adoption             ↑ Inflection point
    │      ╲╱  J-Curve dip
    │
    └──────────────────────────────────────────── Time
         Months 1-6           Months 9-18+
```

**Why the dip happens:**
- Learning curves: people are slower while adjusting to a new tool
- Workflow disruption: existing processes don't fit the new capability
- Integration costs: connecting AI to existing systems takes time and energy
- Complementary investments needed: training, process redesign, data infrastructure

**What the dip is NOT:**
- Evidence the technology doesn't work
- A reason to abandon the initiative
- A management failure

**The McKinsey 2025 data point:** Despite rapid gen AI adoption, more than 80% of firms reported gen AI had no significant impact on earnings yet. This is the J-Curve at scale — most organisations are in the dip, not yet through it.

**The strategic implication:** Don't judge gen AI ROI at month 3. Build the complementary investments (training, workflow redesign, process integration) in parallel with technology adoption, not after.

---

## What Makes a Good Organisational Experiment

A rigorous organisational experiment has five structural requirements:

### 1. A Clear, Testable Hypothesis

Not: "We want to see if Copilot helps our team."

Yes: "We believe gen AI coding assistants will reduce task completion time for junior engineers by 20-30%, with smaller effects for senior engineers, because the tool provides the most value where knowledge gaps are largest."

The hypothesis forces you to define: What changes? For whom? By how much? Why?

### 2. A Control Group (Essential)

Without a control group, you cannot distinguish the effect of the tool from the effect of time, the effect of the early adopters being more motivated, or a market trend that affected everyone.

**Methods:**
- **Random assignment:** Half the team gets the tool, half doesn't. Gold standard.
- **Staggered rollout:** Roll out to different groups over time, creating natural control groups. Works when randomisation is impractical.
- **Lab in the field:** A controlled environment where interactions with the new technology can be observed (P&G's hackathon model is an example).

### 3. Metrics Defined Before the Experiment Starts

Define metrics before you see results, or you'll find the metric that makes the tool look good.

Measure at three levels:
- **Behavior changes:** Time to complete specific tasks, frequency of tool use, types of queries
- **Attitude changes:** Job satisfaction, confidence, reported stress levels
- **Productivity outcomes:** Output quantity, quality scores, customer metrics

### 4. Duration Long Enough to Capture Real Effects

Short experiments capture the novelty effect, not the genuine productivity change. Gen AI adoption often requires 4-12 weeks of integration before the full effect shows. Run experiments for long enough to capture both the initial disruption and the stabilisation.

### 5. Granular Analysis by User Segment

Gen AI's effectiveness is highly context-dependent. What works brilliantly for one group may fail for another. Always segment results by:
- Experience level (junior vs senior)
- Role type (generalist vs specialist)
- Task type (creative vs analytical)
- Workflow integration (solo vs collaborative)

**Why this matters:** Evidence from customer service AI shows large benefits for less-experienced workers but nearly undetectable effects for experienced workers. If you only measure the average, you'll miss both the groups where it's transformative and the groups where it's a distraction.

---

## Proven Results from Gen AI Experiments (Attribution Reference)

Use these as benchmarks when setting hypotheses and evaluating your own results.

| Experiment | Conducted By | Finding |
|---|---|---|
| AI coding assistant (GitHub Copilot, Google) | GitHub & Google (controlled trials) | 21–55% faster task completion; higher completion rates; improved job satisfaction |
| Customer service AI (Fortune 500) | Fortune 500 company (staggered rollout, 5,000+ agents) | 14% overall productivity gain; 34% for less-experienced agents; higher customer sentiment; improved retention |
| P&G Innovation Hackathon | P&G + Raffaella Sadun (Harvard) | AI solo users performed as well as non-AI teams; both AI groups better at blending technical and commercial ideas |
| Microsoft Copilot across 7,000 employees | Microsoft + academics (66 firms) | 1.3–3.6 fewer hours/week on email; faster document drafting; no change in meeting behavior; training + change management critical to adoption |
| Siemens shop floor AI assistant | Siemens (Erlangen factory, 2024) | Reduced time to find information; workers felt more secure in jobs (not less); enabled workers to handle more-complex problems independently |

---

## Ecosystem Experimentation

The most sophisticated organisations run experiments not just internally but across their ecosystems — testing with customers, partners, and suppliers to generate insights at scale.

**Why this matters for product companies:** If your product includes gen AI features, ecosystem experimentation tells you which use cases genuinely matter for your customers, what implementation challenges they face, and how to design for adoption — not just capability.

**The Grab example:** Collaborating with academic researchers to study gen AI impact on 1 million+ entrepreneurs across 6 countries, with precision on which tasks AI helps most and how different business types actually use it.

**How to design ecosystem experiments:**
1. Partner with customers who have enough volume to generate statistically meaningful results
2. Bring in academic researchers to ensure experimental rigour (access to experimental expertise without hiring it full-time)
3. Design the experiment to answer product questions, not just validate the technology
4. Share findings with partner customers — the relationship creates mutual value

---

## The Five Capabilities You Need to Experiment Well

1. **Customer understanding:** Every experiment must start from a specific, high-impact customer problem — not a technology looking for a use case. Distinguish between strategic differentiators and "nice to haves." Channel resources into high-impact experiments only.

2. **Usable prototypes:** Early prototypes people can actually use in real conditions. Not demos. Not simulations. Tools users put into their actual workflow.

3. **Learning mindset:** Cross-functional teams working in short sprints, bringing customers in from the start, treating results — including failures — as learning inputs to the next iteration.

4. **Experimental expertise:** The ability to design clean experiments, determine appropriate sample sizes, analyse results correctly, and communicate findings in plain language. Some companies hire this capability; others partner with academic researchers.

5. **Partnership capabilities:** Active relationships with suppliers, customers, industry experts, and academics who can provide domain expertise, distribution at scale, and experimental credibility.

---

## Responsible AI Checkpoint

> **This step is mandatory.** Any gen AI experiment involves deploying AI on real people — employees or customers. Before running an experiment:
>
> - Has the AI Use Case Risk Assessment been completed? (From `responsible-ai-program` skill)
> - Who is accountable at the project level if the AI causes harm during the experiment?
> - Has informed consent been addressed for participants?
> - Are the experiment's data collection practices compliant with privacy requirements?
> - If the experiment reveals bias or harm, who stops it and how fast?
>
> Experiments are not exempt from responsible AI requirements. Running an unethical experiment "in the name of learning" is not a defence.

---

## The Ship/Don't Scale Decision

A successful experiment does not automatically mean you should scale. Before scaling, evaluate:

| Question | What you're assessing |
|---|---|
| Is the effect real or a false positive? | Was the result a fluke in a small sample? Do you have enough statistical power? |
| Will it generalise? | Did you test on motivated early adopters? Will results hold for a broader, more diverse group? |
| Are the success ingredients replicable? | Is the success dependent on one exceptional manager, one specific workflow, or one tool configuration? Can you replicate those conditions? |
| What are the unintended consequences at scale? | What happens when 10x more people use this? Does it strain infrastructure, create new dependencies, or change team dynamics in unexpected ways? |
| Is the cost sustainable at scale? | Gen AI adoption requires non-trivial investments. Does the cost model work at 100x? |

*Framework derived from John A. List's "The Voltage Effect," applied to gen AI by the HBR research team.*

---

## OUTPUT FORMAT

```
## Gen AI Experiment Design: [Tool/Feature]

Hypothesis:
"We believe [gen AI capability] will [measurable outcome] for [specific user segment]
because [mechanism]. We'd know we're wrong if [counter-signal] within [timeframe]."

Experiment Design:
- Control group: [how selected]
- Treatment group: [who gets the tool]
- Duration: [X weeks]
- Metrics: [behavior / attitude / productivity]
- Segmentation plan: [how results broken down]

Responsible AI Pre-Check:
- Risk assessment completed: [YES/NO]
- Project-level accountability assigned: [name/role]
- Privacy/consent addressed: [YES/NO]
- Harm stop protocol: [who, how fast]

Success Criteria:
- Minimum effect to justify scaling: [specific threshold]
- What would make us stop the experiment early: [criteria]

Scaling Decision Framework:
| Question | Assessment |
|----------|-----------|
| Real effect (not false positive)? | |
| Generalisable beyond early adopters? | |
| Success ingredients replicable? | |
| Unintended consequences checked? | |
| Cost sustainable at 10x? | |
```

---

## WHEN WRONG

- **Use case lacks genuine ROI:** Experimenting with AI when the problem doesn't justify the investment. Experimentation has cost. Focus on high-impact use cases.
- **Organisation not ready for honest results:** If negative results will be ignored or buried, experiments are pointless. They only work in organisations that will act on what they learn, including stopping.
- **Experiment runs too short:** Results from a 2-week experiment capture novelty effects, not real productivity change. Extend the timeline.
- **No control group:** Without a control group, you have an expensive anecdote, not evidence.

---

## TRADE-OFF LEDGER

Complete the Trade-Off Ledger from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 5.

## CONCLUSION

Follow the Conclusion Protocol from the [Universal Skill Protocol](../../UNIVERSAL-SKILL-PROTOCOL.md), Section 6.

---

## VISUAL SUMMARY

After completing the primary output, invoke the **excalidraw-svg** skill to create a single Excalidraw SVG visual summary — ideally visualising the Productivity J-Curve and the experiment design structure. Follow the Visual Summary Protocol in `excalidraw-svg/references/visual-summary-protocol.md`.

---

*Version 1.0 — 5 APR 2026*
*Framework Source: Harvard Business Review, Berndt, Englmaier, Sadun, Tamayo & von Hesler, "A Systematic Approach to Experimenting with Gen AI", January–February 2026*
*Part of: AI PM Skills / eval-and-quality layer*
