# Trust Ladder: match reliance and authority to the task

The framework helps people delegate useful work while retaining the checks and control the situation needs. It is informed by research on automation use, misuse, and disuse, and by practical delegation and organizational design. Parasuraman and Riley’s 1997 work is part of that lineage; the original attribution of a specific “proposal authority” theory to Saaty was not supported. Delegation can include execution as well as proposals, depending on actual authorization.

Netflix-style autonomy with context is an analogy, not evidence that a particular AI ladder is effective. The useful question is concrete: **what may this system do, under which conditions, and what would a person need to understand or intervene?**

## Three dimensions, not one score

System reliability, user belief, and permission can differ. A technically capable tool may reasonably receive narrow authority. A trusted tool may perform poorly in a new domain. A user may understand the limits and still lack the practical right to change an outcome.

Use task-specific trust states as conversation prompts. Maintain actual permissions through explicit rules and enforcement. Do not implement a state machine that promotes a user because thirty days elapsed or demotes them because they accepted too many good suggestions. High confidence, frequent use, and a click on “I understand” do not establish permission for unspecified future actions.

Calibration concerns warranted belief; appropriate reliance concerns the decision. The same calibrated probability can support different choices when the consequences or alternatives differ. A user need not reject a fixed fraction to demonstrate thoughtfulness.

## Worked examples

### Calendar assistant

Separate finding times, drafting invitations, sending invitations, changing attendees, and canceling existing commitments. These actions have different effects and can receive different permissions. A draft is not a sent invitation. A cancellation may be technically reversible while still disrupting other people.

Start with the authorization and evidence available. A user might delegate routine scheduling within defined hours and participants while retaining approval for external or conflicting meetings. A confidence threshold alone cannot authorize sending. If a veto period exists, state whether sending is delayed until it ends; an invitation already received cannot be erased from recipients’ experience. Review actual mistakes and recovery, with a cadence fitted to exposure rather than a universal weekly check-in.

### Expense assistance

Separate reading a receipt, extracting fields, categorizing, submitting, approving, and paying. Validate amounts and currency against suitable records. A routine submission below an agreed limit may be delegated if the policy and controls allow it; the original $500 limit was an example, not a standard. Some submissions can be corrected, while disbursed funds or compliance effects may be harder to remedy.

Maintain relevant evidence and exception handling. “Trusted user” does not justify handling all expenses with only an annual audit. Conversely, no recent manual review is not proof of harmful reliance if automated controls and appropriate sampling are working. Assess the errors and consequences the review is meant to catch.

### Document editing and communication

Separate proposing edits, applying edits, approving a draft, publishing, and sending. Version history can restore text; it cannot retract what readers already saw. Posting inside an organization can still expose sensitive information or create commitments. Use channel, audience, content, and actual authorization rather than treating internal publication as automatically low risk.

A user can delegate routine revisions and maintain review for a public article. Respect prior authorization without requiring repeated permission for the same bounded work. If evidence shows inaccurate publication, restrict the affected path and improve review; do not infer that the user stopped thinking merely because they made few edits.

## Confidence and evidence

For a proposed meeting time, show the relevant availability and constraints. Do not invent “96% best time” unless a defined, validated prediction supports it. For an email or financial recommendation, show the facts needed to assess the action, its consequences, and uncertainty. More source links or a detailed rationale need not mean stronger evidence.

A correct confidence display describes an event and its calibration population. It does not dictate how often a user must accept. Complement probabilities and false-positive rates are different concepts. Use `confidence-tuner` for measurement and display design.

## Detect problems through outcomes

Click speed, edits, rejections, and explanations opened can help locate a problem, but cannot establish attention on their own. Inspect whether the person accepts harmful errors, catches them in time, or changes correct advice into worse outcomes. Compare the combined workflow against realistic alternatives and measure the burden of review.

Use safe learning exercises or appropriately sampled operational cases to evaluate competence. Do not plant consequential live mistakes, fabricate uncertainty, or increase friction to achieve a target rejection rate. Sometimes a better interface solves the issue; sometimes a deterministic check, narrower permission, qualified reviewer, or non-AI approach is needed.

## Repair and boundaries

After a failure, acknowledge known facts, contain harm, offer usable control and remedy, and demonstrate relevant improvement. Do not fabricate a cause, historical confidence, or a fix’s success rate. Support teams can be essential to this process. More approval screens without an effective check do not repair trust.

Requirements vary by action and jurisdiction. HIPAA governs specific health-information relationships and activities; it does not require a human approval for every medical decision. Use the actual applicable clinical, professional, legal, and organizational requirements.

Maintain separate assessments where trust is domain-specific. Reassess when capability, permission, stakes, or user needs change. A successful outcome may involve more delegation, a narrower scope, or a permanent assisted workflow. The ladder’s purpose is useful, justified reliance—not graduation to full autonomy.

Use [SKILL.md](SKILL.md) for the process and [trust-evidence.md](references/trust-evidence.md) for the research boundaries.
