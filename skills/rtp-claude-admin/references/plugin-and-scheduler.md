# Plugin and scheduler maintenance

Companion revision 1.0.1, 13 Sep 2026. Use for the requested maintenance scope. A read-only audit, package build, remote release, installed refresh, and schedule change are separate actions; preserve authorization already given for each.

## Plugin audit

1. **Identify the candidate.** The personal plugin repository is `rtp-personal-skills-repo/` under the Claude library. Inspect its active branch, remote, manifests, working-tree changes, and intended output. Preserve unrelated and uncommitted work.
2. **Run the installed validator.** Where available, run `claude plugin validate .` from the repository. Inspect the actual target, errors, warnings, and validator version. A schema check is useful diagnostic evidence; it does not prove that every skill behaves correctly or that a Desktop cache contains this candidate.
3. **Check library-specific invariants.** Parse each header, preserve its fields, enforce the user's 1,000-character description maximum, validate the current name/folder mapping, resolve imports, and verify referenced resources. A clear description should say when the skill applies, but the literal phrase "use when" is not a universal parser requirement.
4. **Distinguish host schemas.** Claude Code supports additional frontmatter fields, and other Claude surfaces can impose different rules. The library deliberately retains version and dependency metadata. Do not strip `license`, `framework_source`, invocation controls, or other established fields through a blanket allowlist. Diagnose a real compatibility error against the intended host and resolve the smallest necessary change while preserving the user's required header structure.
5. **Quote YAML safely.** Descriptions containing colons or other YAML-sensitive text need correct quoting or a block scalar. Validate the parsed value rather than replacing punctuation by guesswork.
6. **Inspect plugin locations in context.** Search manifests within the relevant installation and project scope. The personal repository has a canonical manifest, but vendor plugins, authorized separate projects, caches, and worktrees can legitimately have their own. Classify an apparent duplicate before moving it. Do not archive every other manifest found on the computer.
7. **Check bundle contents.** Compare the artifact manifest, skill versions, names, references, scripts, and assets with the final candidate. File modification time or ZIP timestamps alone do not establish freshness. Keep a release record with version, source revision, and content checksum when useful.

Current primary guidance: [Claude Code skills](https://code.claude.com/docs/en/skills) and [plugin validation reference](https://code.claude.com/docs/en/plugins-reference#plugin-validate), checked 13 Sep 2026. Their schema details depend on host and version. Recheck before making a compatibility migration.

## Release and installed state

The canonical bundle convention is `rtp-personal-skills-vX.Y.Z-DDMMMYYYY.plugin`, with the current root `rtp-personal-skills.plugin` and previous releases recorded under the established plugin archive. Use the repository's verified release process so artifacts and manifests agree. Avoid extra unlabeled or Finder-copy bundles that leave the current build ambiguous.

Before running `scripts/plugin-release.sh`, inspect its actual behavior and current options. The September review found incidental operations that need repair or a scoped alternative: lock deletion, broad staging, credential-in-URL fallback, marketplace hard reset, backup deletion, and incomplete error handling. Do not assume a `--check` flag has no side effects.

Stage only changes in the authorized release. Preserve active locks and concurrent work. Keep credentials out of command text, remote URLs, logs, and user-visible output. Use authenticated tooling without printing tokens. Stop the affected release step on failure and retain recovery copies until the final state is verified.

For remote publishing, use the intended branch and remote rather than assuming remote HEAD is the release branch. Local uncommitted files can differ even when commit IDs match. A different installed version can also be intentional, so compare the expected release state rather than requiring every location to match throughout development.

Prefer the host's supported plugin update mechanism. If a marketplace checkout needs repair, inspect its branch and local changes first. Do not use an unconditional hard reset or delete a cache containing unpreserved work. An authorized refresh of a clean, disposable cache can proceed with a verified source and recovery path.

After an authorized release or refresh, verify the state actually reached:

| Layer | Evidence to record |
|---|---|
| Canonical skill library | Revised files and required resources |
| Local repository | Intended changes, validation, version, and source revision |
| Bundle | Artifact path, manifest version, contents, and checksum |
| Remote release | Actual pushed revision or published artifact, when authorized |
| Marketplace and installed plugin | Expected version and relevant loaded files, with any restart requirement |

Report an inaccessible or unverified layer explicitly. A successful push is not proof that the running app loaded the new files, and a newer checkout does not necessarily replace the active installed cache.

## Scheduler maintenance

The intended task is `governance-health-check`, weekly on Sunday at 09:00 in the configured local timezone. Its job is to run the current governance checker, review the judgment-based findings, and record the actual result. Preserve its configured notification preference and scope.

For Claude Code Desktop, the prompt is normally stored at `~/.claude/scheduled-tasks/<task-name>/SKILL.md`, or under the configured Claude directory. The schedule, working folder, model, and enabled state are managed by the scheduler rather than inferred from that prompt file. Use the tools or UI available in the current host to inspect the actual task and recent runs.

The [Desktop scheduling documentation](https://code.claude.com/docs/en/desktop-scheduled-tasks), checked 13 Sep 2026, describes local execution and a catch-up policy that looks for missed runs in the last seven days, then starts one for the most recent missed time. A prompt can therefore run later than its nominal hour. Confirm the actual host and current behavior; Claude Desktop, cloud routines, and other assistants' schedulers are different systems.

Do not infer that a missing task file means the schedule was deleted, or that a present file means it is active. When access is unavailable, report that limit. When repairing an authorized schedule, preserve its existing fields unless the user requested a change, avoid duplicates, and verify the saved schedule and relevant execution evidence.

The governance health entry uses the established `DD MMM YYYY` heading pattern that the local heartbeat checker parses. Record a completed full or partial run honestly, including failures and skips. Creating a healthy-looking log entry without running the checks defeats the backstop.

## Historical lessons retained

The earlier admin skill recorded missed manual checks, a disappeared schedule, stale plugin caches, and duplicate upload bundles. Their reusable lesson is to verify each layer against its intended behavior. The historical counts and dates explain why the procedure exists; they do not establish that those problems are happening now.
