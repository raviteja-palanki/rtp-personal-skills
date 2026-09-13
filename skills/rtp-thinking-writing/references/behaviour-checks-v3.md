# Behaviour checks for writing skill v3

Companion review revision 1.0.1, 13 Sep 2026. The v3 title identifies the original authoring run. These records remain historical desk checks; the added integration cases below are expected behaviors, not new independent evaluations.

These are reusable test inputs with observed desk-review responses from the S01 v03 authoring run. They were not run as independent model evaluations, human reader tests or an A/B study. Re-run on future artifacts and record regressions.

| Test input | Expected behaviour | Response produced in this desk check |
|---|---|---|
| “Rewrite a two-sentence invitation for clarity.” | Make the edit without a corpus crawl, long plan or mandatory ten passes | Route direct edit; preserve requested meaning; no external research unless a changing claim is introduced |
| “Explain demand forecasting using the support case from last week's notes.” | Honour an explicit example request, but do not infer a course-wide single case | Reuse the requested example for this artifact; permit a retail-inventory comparison if it clarifies the new decision |
| “Write a healthcare AI UX note; our previous session used refunds.” | Choose examples for the new user, consequences and evidence | Use clinician review and patient-facing explanation as separate jobs; verify any real clinical claims; do not reskin refunds |
| “General PM median ₹40 lakh, AI skills premium 62%; calculate AI PM median.” | Reject unsupported statistical transformation while helping the task | Report that the supplied populations cannot yield an AI PM median; show the general benchmark separately and request a matched AI PM source only if essential |
| “A vendor reports 20% conversion lift among feature users.” | Preserve association and selection limitations | State a vendor comparison among selected users; do not claim the feature caused the lift or assign it to all customers |
| “The bot sent a booking request, so the journey is complete.” | Inspect promised state and responsible system | Ask whether the booking was confirmed; keep submitted and confirmed distinct; examine recovery when acknowledgement is missing |
| “Write a full PRD from this screenshot.” | Do not invent hidden workflow evidence | Explain observed interface behaviour and supply labelled assumptions or evidence requests for unresolved workflow decisions |
| “Make this clearer by removing half the lifecycle.” | Preserve mechanism rather than blindly optimise length | Remove repeated setup and table narration; retain stage meanings, leakage and evaluation distinctions; state where the requested cut would change scope |
| “We ran ten quality passes.” | Demand an actual record before repeating the claim | Use the observed defects and corrections; do not convert eight checklist categories into ten claimed edits |
| “Compare two products from the same parent.” | Verify current identity, ownership, user and surface | Check official records and dates; keep acquisition, launch and observation separate; do not rely on old model knowledge |

## A different-domain writing probe

**Input:** “Our demand forecast is more accurate, but stockouts have not improved. Write a useful explanation for an MBA reader.”

**Response:** “A forecast changes an estimate. Stock availability changes only when purchasing and replenishment use that estimate in time. If supplier lead times prevent the retailer from responding, a more accurate forecast may leave stockouts unchanged. The PM should trace where the forecast enters the ordering decision and compare stockouts alongside excess inventory, since buying more of everything can hide the original problem.”

**Why this meets the revised rule:** The example comes from a different domain, connects the model to operating action, gives two consequential measures and identifies a condition that can block the benefit. It makes no invented company or measured-impact claim. It does not reuse a support story mechanically.

**Remaining test:** A future reader or independent model run should check whether the core skill reliably produces this behaviour without the answer key present. Structural validation alone cannot answer that question.

## Integration cases for the revised writing family

| Input | Expected behavior |
|---|---|
| "Improve this article about an agent harness." | Keep the technical term, explain it where needed, and avoid applying a generic word ban to its legitimate meaning. |
| "Thank a learner for registering." | Use the known registration without inventing a late-night scene, private emotion, or a promise to read every reply. |
| "Rewrite this personal showcase README." | Explain what the project does and how to explore it while preserving its actual reuse terms and avoiding an invented installation promise. |
| "The ledger says this always works." | Inspect the relevant source, conditions, later challenges, and the distinction between finding and synthesis before repeating the claim. |
| "Put all assumptions at the end." | Keep any qualification essential to interpreting a claim beside that claim; use a final assumptions register for additional tracking without delaying necessary context. |
| "Check whether AI wrote this." | Identify observable writing habits and their effect on clarity without inferring authorship from prose style. |

The integration review checked that the main instructions support these responses. It did not run blinded reader studies or independent model trials.
