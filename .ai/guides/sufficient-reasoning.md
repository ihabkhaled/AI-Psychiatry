# Sufficient Reasoning and Evidence Floors

Sufficient reasoning is enough understanding and proof to decide, implement, verify, and deliver safely—then stop. It rejects both immediate guessing and unlimited analysis.

## Observable signals

Reasoning is below the floor when the user requirement, affected subsystem, relevant dependency, existing pattern, acceptance condition, failure path, required test, or security/data implication is critically unknown. Evidence is below the floor when code requirements lack implementation proof, behavior requirements lack runtime proof, integrations lack integration proof, security requirements lack relevant validation, or migrations lack schema/data verification.

Reasoning exceeds the useful ceiling when those facts are known, the decision is ready, required proof exists, and more investigation repeats the same evidence or explores optional possibilities.

## Intervention

Before a major decision, record the decision, minimum required evidence, available evidence, critical unknowns, and readiness. Before non-trivial implementation, answer: what exists, what changes, why, what could break, and how it will be proven. Before a debugging change, record a short hypothesis, evidence, and expected result; trivial syntax repairs are exempt.

Apply evidence by requirement class. Run at least one required first verification. Add negative validation when meaningful failure states exist: explicit invalid inputs, authorization, dependency failure, boundary conditions, security-sensitive paths, data-loss risks, and likely regressions. Do not invent every imaginable edge case.

Maintain a compact completion evidence matrix. Inspection and confidence cannot replace executed proof. A slow or expensive test may motivate a targeted development test, but required final quality gates remain required unless a higher-priority instruction explicitly changes them.

## Recovery

If evidence is insufficient, investigate or verify only the missing critical row. If a critic surfaces a correctness, security, data-loss, requirement, or regression finding after its budget, keep the finding and use a controlled override. If evidence is sufficient, stop reviewing and deliver.

## Stop condition

Stop reasoning when critical uncertainty is resolved, decision-ready evidence exists, and further investigation is unlikely to change the decision. Stop work when every mandatory evidence row is current and all required findings are resolved.
