# Understanding autonomy as an action contract

**Business lens:** decide which work to delegate, which decisions to retain, and what oversight costs. Autonomy can reduce waiting and expand useful work, but can also add cost or amplify errors. There is no universal equation in which trust-recovery cost equals latency gain.

**Technical lens:** enforce who can perform an action on which resource, under which conditions, with what evidence and recovery behavior. Model confidence can inform a tested routing rule; it does not grant permission. The contract belongs to the combination of system, action, user, and context.

## Start with consequences, not available access

Suppose an incorrect database write could require $50,000 and two days to remediate. Those illustrative consequences justify examining the write's scope, validation, recovery, and approval needs. They do not mechanically prescribe one approval design. Do not grant authority simply because the credential permits it.

Reading a file does not reverse a disclosure. A development database restore may lose intervening work. A production rollback may restore software while leaving customer effects. Deleting one backup may or may not be irreversible, depending on other recoverable copies. Name the effect and available recovery precisely.

Scope matters too: one operation can affect a person, a batch can affect thousands, and a cross-system action can trigger further work. Copying a permission contract to more agents or users changes aggregate exposure and coordination needs. Reassess the expanded deployment.

## Calibrate evidence rather than trusting a confidence sentence

“I am 92% confident” is a model output, not a certificate that its training history showed 91% accuracy. Define the prediction, score, task population, and evaluation set. Compare estimated probabilities with observed outcomes, including sample uncertainty and changes in conditions. Calibration is a property of groups of predictions, not proof about one answer.

If predictions scored around 92% are correct only 60% of the time on representative data, they are overconfident in that setting. Recalibrate, restrict their use, or require stronger evidence. **Lowering the acceptance threshold would generally allow more predictions through; it is not the automatic correction for overconfidence.** Choose a decision threshold against error consequences and review cost after validating the score.

An underconfident score also needs calibration rather than an arbitrary threshold change. A calibrated system can still be too inaccurate for the action, and rare severe errors can be hidden by high average accuracy.

## Choose an initial mode and change it deliberately

Sandbox evaluation, shadow operation, supervised execution, sampling, and exception-based handling are possible stages. Their order, duration, and necessity depend on the work. The source's 0–20, 20–100, 100–500, and 500+ decision bands and its weeks 1–2 through 7+ schedule were illustrative; they are not validated graduation requirements.

Likewise, 95% accuracy over 50 cases or 98% over 100 cases does not automatically authorize consequential execution. Check coverage, severe failures, correlated errors, detection, and recovery. A critical failure may justify stopping the affected action; do not use a fixed “drop two levels” rule regardless of cause.

Acceptance rate measures acceptance. It is not correctness, sufficient review, or an optimal 70–85% trust target. A person can rightly accept 95% of good suggestions or reject most unsuitable ones. Investigate the result and the review process.

## Make the experience understandable

Users should understand the scope they delegate, relevant actions taken, and how to intervene. Ask a concrete approval question when approval is needed; proceed on already-authorized routine work. Explain the evidence and rationale for a result without claiming access to an infallible internal reasoning record.

“Override” can change future behavior or some current state. It cannot retroactively unsend an email. Similarly, a user's correction does not automatically retrain the model; state how feedback affects this run, stored preferences, policy, or a later training process.

## Illustrative pitfalls

- **Delivery dispatch:** a workflow that works in ordinary conditions may need different controls during demand or supply disruption. The original named Uber/COVID pricing story was not sourced sufficiently to establish that causal account.
- **Medical analysis:** 99% test accuracy can conceal selection, prevalence, subgroup, or deployment differences. It does not independently justify removing qualified oversight.
- **Driving systems:** performance in one location need not transfer to different roads or weather. The original California-to-Arizona story is a generic distribution-shift illustration, not a verified named deployment incident.
- **Message moderation:** an unexpected deletion can damage trust even if recovery is possible. State the moderation policy, available appeal, and restoration limits. The source's Slack-bot case is illustrative.

These examples motivate checking detection, consequence, exposure, recovery, and user expectations. They do not establish that all read access is safe or all deletion must be prohibited.

## Conceptual lineage

Control theory offers feedback and stability concepts; decision theory connects uncertain outcomes with costs; organizational research examines delegation and accountability; AI evaluation examines calibration, distribution shift, and specification gaming. These are conceptual connections, not proof that a particular historical author prescribed this seven-level taxonomy. Goodhart-style metric failure is a risk of poorly chosen incentives, not a guarantee that any accuracy metric causes deceptive behavior.

Use the [main skill](SKILL.md) to create the action-level map and choose a supervision contract.
