# Relationship scenarios and domain choices

These are design prompts, not prescribed stages. Select by the actual task, evidence, authority, and user needs. Days of use do not establish competence. The former Level 0–4 permissions conflicted with the library’s shared autonomy taxonomy; use explicit permission modes instead.

## Eleven relationship scenarios

| Scenario | Candidate behavior | What the user needs | Evidence to collect |
|---|---|---|---|
| New user, scope unclear | Suggest or prepare; obtain missing authorization before effects. | Task, access, relevant alternatives, limitations. | Comprehension and task success, not approval volume alone. |
| New user, bounded task understood | Recommend; execute only within current authorized bounds. | Preview and actual recovery limits. | Correct and harmful acceptance; decision burden. |
| Building evidence with review | Keep relevant review while evaluating outcomes. | Accurate reports of errors and changes. | What review catches, misses, and unnecessarily changes. |
| Building evidence on low-consequence tasks | Delegate appropriate routine work. | Clear scope and correction path. | Errors, useful corrections, actual time saved. |
| Established use, monitoring calibration | Maintain justified delegation and test remaining risks. | Real uncertainty and material changes. | Representative evaluated cases or safe training exercises; no fabricated live doubt. |
| Established use with recoverable effects | Execute defined action classes if authorized and adequately controlled. | Whether recovery is actual undo, delayed execution, or compensation. | Recovery success, residual harm, and unexpected effects. |
| Evidence of harmful reliance | Contain the relevant exposure and redesign review or controls. | Specific problem and reason for restriction. | Reduction in harmful acceptance and burden; no rejection quota. |
| Restoring delegated scope | Reassess tested action classes and current preferences. | Exact permissions being restored. | Outcome evidence and remaining gaps, not a waiver checkbox alone. |
| Immediate post-failure repair | Contain, explain known facts, and provide a usable alternative. | Actual status, owner, remedy, and next update. | Harm addressed, repair effectiveness, user understanding. |
| Gradual post-failure return | Restore only justified scope; a narrower permanent mode is valid. | What changed, why, and how to revoke or appeal. | Performance by action class and conditions for further change. |
| Enterprise deployment | Apply scoped authorization, oversight, and evidence requirements across modes. | Roles, policy, action history, and limits of recovery. | Ability to establish material facts and maintain controls. |

The original navigation mentioned twelve rows but supplied eleven. These eleven preserve the intended scenarios without adding an invented stage. The earlier first-week, first-month, six-month, two-stage-reset, and threefold early-failure rules are not validated timing standards.

## Domain considerations

| Domain | Useful starting design | What governs further delegation |
|---|---|---|
| Creative tools | Drafts or previews with usable version history. | Publication, authorship, sensitive content, and actual recovery. |
| Consumer email and writing | Separate drafting from sending or publishing. | Recipient, content, authorization, privacy, and irreversible exposure. |
| Enterprise search and analysis | Evidence-linked responses and known limitations. | Source access, current context, decision consequences, verification options. |
| Finance, audit, forecasting, or transactions | Separate information, recommendation, approval, and execution. | Specific activity, professional duties, funds at risk, identity and transaction limits. |
| Healthcare support | A defined clinical or informational role with appropriate expertise. | Intended use, clinical evidence, applicable requirements, workflow, and patient consequences. |
| Legal research or review | Verifiable sources, jurisdiction, date, and unresolved issues. | Actual service, professional requirements, confidential data, and decision authority. |
| Customer support | Distinguish drafting, responding, routing, refunds, and account changes. | Complexity, policy, identity, customer impact, and effective escalation. |
| Internal developer tools | Bound repository, environment, credentials, and execution permissions. | Test evidence, production access, dependencies, and recovery. |
| Code review or suggestions | Show findings and evidence without assuming every flag is correct. | Vulnerability severity, patch effects, false alarms, and release rights. |

No sector has a universal healthy rejection range or a safe maximum autonomy level after six months. False positives are not inherently worse than false negatives in all creative products, and enterprise consequences are not always greater than consumer consequences.

## Event and rate design

Record a privacy-appropriate item ID, task, system configuration, permission mode, presentation time, and the valid confidence measure if available. Capture user events separately from actual effects: accepted, edited, rejected, regenerated, deferred, or no observed response, then queued, executed, failed, canceled, or outcome uncertain where relevant.

Choose either mutually exclusive final dispositions or explicitly multi-event analysis. Do not count one regeneration, edit, and later acceptance as three separate presented outputs unless the unit of analysis defines them that way.

- Acceptance rate can be accepted items / eligible presented items, with unresolved items reported separately.
- Rejection and regeneration rates should be separate unless there is a specific reason to combine them.
- Edit rate indicates change, not necessarily correction of an error.
- Undo rate concerns actions for which undo was actually available. Include whether it succeeded.
- Approval rate uses decisions actually presented for approval; it is not the fraction of all system actions that were authorized.

Pair these behavioral rates with labeled quality and consequences. For binary correctness, harmful acceptance among incorrect recommendations and correct acceptance among appropriate correct recommendations are distinct rates. The evaluation rubric must account for valid preferences, abstention, and multiple acceptable outcomes. A low error base rate affects what can be inferred from small samples.
