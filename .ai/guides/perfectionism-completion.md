# Perfectionism and Completion Avoidance

## Engineering behavior

Perfectionism becomes an agent failure mode when a correct, complete, verified solution is delayed for elegance, speculative edge cases, optional refactors, subjective style, or marginal optimization. Completion avoidance is its terminal form: all Definition of Done items are satisfied, yet the agent keeps finding one more thing.

## Observable signals

- Working systems are redesigned without a correctness, security, or explicit requirement.
- Local changes expand into repository cleanup.
- Style preferences block delivery after required quality gates pass.
- Hypothetical edge cases multiply without evidence or acceptance impact.
- The remaining required-item count is zero but investigation broadens.
- The agent replaces a valid solution because another might be marginally cleaner.
- Final review becomes a fresh repository-wide audit.

## Prevention

Define a finite minimum Definition of Done before implementation. Separate mandatory quality from optional refinement. Use refactor, architecture, and optimization gates: proceed only for requested behavior, correctness, security, measured performance, regression prevention, or necessary maintainability of changed code.

## Intervention

1. Freeze new improvements and audits.
2. Enumerate each Definition of Done condition with current proof.
3. Classify every remaining concern as blocker, required, optional, or unrelated.
4. Fix blockers and required defects only.
5. Record optional findings without implementation.
6. Run only the final mandatory gate whose proof is absent or invalidated.
7. Report delivered behavior, relevant verification, and deferred findings.
8. Stop; do not append another improvement cycle.

Near completion, scope-expansion tolerance becomes zero and verification focus becomes narrow. I can make it cleaner is not a requirement. Sunk cost does not justify continued refinement.

## Recovery levels

Use scope guard for optional improvements. Use verification controller when reassurance drives more testing. Use critic controller when reviewers invent requirements. Use completion gate as soon as all finite conditions are true.

## Example

A bug fix passes its regression test, related integration suite, lint, and required build. Renaming unrelated helpers or redesigning the module may be attractive, but it is optional. Record it if useful, report proof, and finish.

## Common mistakes

Delivery-first does not mean skipping required security or regression checks. Conversely, quality does not mean theoretical perfection. A full audit at finalization violates bounded completion unless the repository explicitly requires it.

## Stop condition

Stop immediately when the requested outcome, explicit requirements, relevant tests, mandatory gates, and absence of known blocking regression are proven.
