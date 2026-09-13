---
name: rtp-interview-skill
version: v1.0.1_latest
description: 'Prepare Ravi for senior and Director-level AI PM interviews across technical depth, AI system design, product sense, leadership, strategy, and hiring-manager rounds. Run a mock, review an answer, explain a concept, prepare for a company, diagnose a previous loop, or help Ravi evaluate the employer. Use the connected AI-PM library for depth and verified personal records for experience. Keep real work, authored analysis, and hypothetical approaches distinct. Review answers for a clear direction, technical understanding, relevant evidence, useful nuance, concise delivery, and honest uncertainty. Includes concept explanations, practice questions, illustrative answers, a shared rubric, and targeted coaching drills. Pairs with the orchestrator for routing, falsification for a loop pre-mortem, stakeholder communications for executive discussions, and the resume builder for application materials.'
---
# AI PM interview preparation

Help Ravi explain sound product judgment clearly and defend it under follow-up questions. Use the library to recover the reasoning; use verified experience to establish what he personally did. Preparation should uncover knowledge gaps as well as improve retrieval and delivery.

## Start with the task and the evidence

Identify the requested mode, role, round, and available time from the conversation. Ask only for missing details that change the preparation. A general mock can begin without a company name. This skill specializes in AI PM interviews; adapt its general communication principles for other roles without assuming the same technical emphasis.

Keep three kinds of answer distinct:

- **Experience:** what Ravi actually built, led, decided, or observed. Verify his role, dates, scope, collaborators, outcomes, and numbers from his records or his account.
- **Proposed approach:** what he would do in a case or design exercise. Say “I would”; explain assumptions and how he would test them. A hypothetical question does not require a past deployment.
- **Knowledge:** an explanation supported by technical sources or his analysis. Writing a playbook demonstrates analysis; it does not establish that he deployed the system it describes.

Never invent projects, failures, metrics, ownership, or first-person anecdotes. Keep confidential examples at an appropriate level of detail. Do not introduce personal health, family, age, financial, immigration, or relationship details into interview answers. If Ravi explicitly requests help discussing a career gap or another sensitive topic, help him choose the minimum disclosure he wants to make.

For current prices, capabilities, company policies, and interview arrangements, verify the relevant primary source. Historical interview reports are practice leads, not promises about a current loop. Unsupported statistics need verification or removal; making them vague does not make them true.

## Choose the round and retrieve the right depth

| Round | Preparation focus | Connected skills |
|---|---|---|
| Technical depth | Explain the mechanism and its limits | `rtp-agent-harness`, `rtp-invisible-stack`, `rtp-context-spec`, `rtp-eval-framework`, `rtp-prompt-craft` |
| AI system design | Define the task, system, permissions, failure paths, and evaluation | `rtp-ai-prd`, `rtp-autonomy-spectrum`, `rtp-agent-spec`, `rtp-failure-modes`, `rtp-tool-architecture`, `rtp-determinism-compass` |
| Product sense | Choose a valuable problem and reject weak solutions | `rtp-problem-ai-fit`, `rtp-jtbd-analysis`, `rtp-opportunity-solution-tree`, `rtp-first-principles`, `rtp-ai-product-taste` |
| Behavioral and leadership | Explain personal decisions, collaboration, consequences, and learning | Verified experience; `rtp-adoption-launch`, `rtp-needs-guard`, `rtp-problem-type` |
| Strategy and case | Defend a bet, its economics, and conditions for changing course | `rtp-strategy-canvas`, `rtp-moat-finder`, `rtp-cost-model`, `rtp-token-economics`, `rtp-build-or-buy`, `rtp-falsification` |
| Hiring manager and executive | Connect judgment, execution, and accountable ownership | `rtp-stakeholder-communications`, `rtp-trust-under-fog`, `rtp-dual-lens` |
| Evaluating the employer | Assess the role, operating conditions, and mutual fit | Questions below; `rtp-responsible-ai-program`, `rtp-cost-model` |

Retrieve only the relevant skill and depth. Answer in ordinary language rather than reciting internal skill names. Naming a useful framework is fine when it helps the interviewer; name-dropping does not replace reasoning.

Two practice lenses help tune depth: an **engineering interviewer** probes how the system works; a **product interviewer** probes what that mechanism changes about a decision. Real interviewers blend both. Infer the emphasis from the role, recruiter guidance, and follow-up questions rather than the company logo alone.

## Use one shared set of six criteria

The original five principles plus honest uncertainty form the rubric used throughout this skill:

1. **Clear direction.** Answer the question early. If a missing constraint changes the answer, clarify it or give a conditional recommendation with the deciding condition.
2. **Technical depth.** Use accurate terms and explain the mechanism as far as the question requires. Plain language is welcome; jargon is not a scoring requirement.
3. **Relevant evidence.** For an experience question, distinguish Ravi’s contribution from the team’s and connect it to an observed result. For a hypothetical or definition, use sound reasoning; mark personal experience not applicable when appropriate.
4. **Useful nuance.** Name the trade-off, boundary, or failure condition that matters to this decision. Do not append a generic caveat to every simple answer.
5. **Concise delivery.** Give enough detail to answer, then leave room for follow-up. Length depends on the question and the agreed format.
6. **Honest uncertainty.** Separate what is known, inferred, proposed, and unknown. Explain how a material uncertainty would be resolved. Correct a mistake directly.

“I have not implemented that component; my understanding is…” is stronger evidence of calibration than pretending. It still identifies a preparation gap if that component is central to the role or to a claimed responsibility. An incorrect answer alone does not prove deliberate bluffing, and this practice rubric cannot predict an employer’s hiring decision.

Use [the grading rubric](references/grading-rubric.md) for consistent feedback and [the concept guide](references/concepts.md) to repair understanding.

## Ground personal answers in the right records

Paths below are relative to the Claude workspace. Locate their current equivalents if this skill is used elsewhere; do not pretend unavailable files were read.

**Experience records:** start with relevant material in `5_My Resume/`, project records, and Ravi’s account. Confirm any Honeywell tenure and scope, Perplexity AI Fellow title and year, and other career details before using them. Do not translate total career experience into years of AI deployment or a fellowship into employment.

**Argument and spoken delivery:** use the current approved playbooks under:

`1_Projects/1_my-personal-website/1_My Series-MD-FILES/Important playbooks/`

- `playbook-harness. engg/final playbook/How-I-Explain-Harness-Engineering-Interview-Definitive-Draft-6.md` provides the 30-second, 90-second, and five-minute answer shapes and the outcome, owner, or test discipline.
- `playbook-harness. engg/final playbook/The-Harness-Engineering-Playbook-Definitive-Draft-6.md` supplies the contracts, ownership verbs, failure shapes, decisions, and economics behind harness answers.
- `Frontier playbook/The-Frontier-Companies-Playbook-Draft-6-Combined.md` supports company-strategy preparation. Locate the current `AI_Playbook.md` for breadth when needed.

Prefer the approved `final playbook/` material over superseded `Version_1/` drafts. These named Draft 6 files are the checked starting points for this revision; verify a later approved successor before switching.

**Drills and research:** `1_Projects/0_interview-prep/` holds question banks and company preparation; `3_Research/08_career/` holds collected guides. Relevant `Ravi_` analyses in `3_Research/01_agentic-stack/`, `02_harness-engineering/`, and `03_ai-evals/` supply intellectual depth. Their authorship does not prove operational ownership. Count the live skill inventory if its size matters; do not repeat a frozen library count.

For leadership stories, consider the **Bridger** pattern where the experience supports it: understand partners’ constraints, translate across engineering, design, and finance, challenge assumptions, and integrate a workable decision. Use the pattern to reveal real collaboration, not to force every story into one template.

## Run the requested mode

### Mock

Use [the question bank](references/question-bank.md). State the round and practice emphasis, then ask one question at a time. Follow the answer one level deeper at its most consequential gap before giving feedback. Ask for application after a definition, a limitation after a tool choice, mechanism after vague architecture, or a product consequence after technical detail.

Five questions is a useful default, adjustable to the time available. At the end, review the six criteria, identify the most important improvement, and revise the weakest answer using verified experience or an explicitly hypothetical approach. Do not let an average conceal a material error; do not fail a session merely because one optional dimension was unused.

### Grade an answer

Check the mechanism and evidence first. Give a short, specific assessment under the applicable criteria, explain the largest gap, and offer a corrected version. Preserve Ravi’s meaning and ownership. If an experience detail is missing, flag it rather than inventing it to make the rewrite sound stronger. Use practice labels, not claims of a guaranteed “A+” interview result.

### Coach or explain an answer

Use [the coaching playbook](references/coaching-playbook.md) to match a gap to one drill. When Ravi asks for a model answer directly, answer directly and use [illustrative answers](references/model-answers.md) as reasoning examples. Do not turn every explanation into a mock or quiz.

### Prepare for a company

Read the role and available recruiter guidance, then consult current company sources. Map confirmed rounds separately from likely preparation topics. Select relevant skills, real stories, and the question most likely to reveal a substantive gap. Treat the historical company bank as a starting point, not inside knowledge of current hiring criteria.

### Run a loop pre-mortem or retrospective

For a pre-mortem, imagine a disappointing result and identify a plausible, actionable reason: unclear ownership, an unsupported number, weak technical depth, no relevant learning story, or a mismatch in answer depth. Look for evidence before choosing the drill. No need to manufacture discomfort or a flaw if preparation is sound.

After a real loop, separate remembered questions, actual feedback, and hypotheses about the decision. Interview outcomes have multiple causes; do not present an inferred rejection reason as fact.

### Help Ravi evaluate the employer

Choose questions that reveal the conditions of this role:

- Who can stop a harmful model or deployment, how is that authority exercised, and how are conflicts with delivery goals resolved?
- What did you ship recently that did not work, and how was the concern raised and handled?
- How do you detect that an AI feature is getting worse, and who responds?
- How do the economics change at ten times current usage, and which assumptions remain untested?
- Which decisions would this role own, influence, or escalate?

Ask natural follow-ups and record evidence. An unclear answer is a reason to investigate, not proof of ineffective governance or poor culture. Reporting lines alone do not establish stop authority. Choose a few useful questions; there is no quota of uncomfortable questions or basis for inferring character from a candidate’s question count.

## Improve delivery without scripting a persona

Practice aloud when useful, with Ravi’s preferred recording or dictation method. Prepare a 30-second direction, a 90-second explanation, and a five-minute deeper version of important stories. These are practice lengths, not universal interview limits; time actual speech rather than converting a fixed word count into seconds.

Lead with the answer, explain the decisive mechanism, add relevant evidence, and state the important trade-off. Vary that shape when the question calls for a definition, story, or design. Check whether the interviewer wants more depth. Do not rehearse away the specific details and uncertainty that make a real story credible.

Watch seven recurring problems: invented detail; overstated platform ownership; activity presented as a proven outcome; claims of an unblemished record; AI designs without meaningful failure handling; depth mismatched to the question; and unsupported statistics. These are diagnostic prompts, not automatic rejection rules. Verified ticket resolution can be an outcome. Fixed acceptance criteria are useful; pair them with appropriate evaluation, permissions, fallback, drift monitoring, and ownership. A numerical confidence threshold is not mandatory for every product, and human review alone does not establish safety or an audit trail.

## Finish the session

Check that the answer addresses the question, its mechanism is defensible, its ownership and numbers are supported, and uncertainty is clear. For leadership preparation, include a relevant setback or changed decision when the record supports one. For a full loop, prepare useful questions for the employer.

Return the requested answer or practice assessment, the single next improvement, and any unresolved fact that matters. Store only useful practice notes in the authorized workspace. Preserve the distinction between rehearsed, fact-checked, and independently evaluated; this skill’s examples and rubric are coaching aids.

## Attribution and maintenance

The five original principles, interviewer lenses, and follow-up practice draw on Aakash Gupta and Prasad Reddy’s [AI PM technical interview guide](https://www.news.aakashg.com/p/ai-pm-technical-interview), published July 22, 2026. The full-loop map, local skill routing, explicit uncertainty criterion, source discipline, pre-mortem, and employer evaluation extend that approach. Do not infer that the source opposes acknowledging uncertainty.

Editorial revision: September 13, 2026. All five companions use the same six criteria. Research qualifications and technical corrections are collected in the concept guide; company reports remain historical practice context.
