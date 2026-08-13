# AI Agent Failure-Mode Catalog

This catalog uses engineering names. ADHD, OCD, and similar human terms may explain analogies but are not diagnoses of AI systems or people.

## Observable signals

Use observable state: objective changes, active items, nesting depth, retries, repeated commands or errors, critic rounds, context reloads, completed requirements, new evidence, and last progress. Do not store chain-of-thought.

| Failure mode | Symptoms and likely causes | Signals | Prevention | Recovery |
|---|---|---|---|---|
| Attention Drift | Novel findings displace required work; objective was not locked. | Work-item switching; optional branch active. | Lock objective; WIP one; classify discoveries. | Park branch; attention reset; resume parent. |
| Goal Drift | Agent silently redefines success. | Objective or DoD changes without authority. | Record objective and finite DoD. | Restore user outcome; ask if true conflict exists. |
| Scope Drift | Local task grows into cleanup or redesign. | Files, domains, and requirements increase. | Scope list and refactor gate. | Classify and park non-required work. |
| Context Drift | Irrelevant knowledge dominates active context. | Current evidence displaced by broad reading. | Layered context and load conditions. | Compress; reload only required sources. |
| Recursive Decomposition | Tasks open children that open more children. | Nesting depth above three. | Parent contract and depth budget. | Return to parent; close optional children. |
| Recursive Investigation | Each answer creates another prerequisite. | Reads and searches grow; decisions do not. | Bounded question and stop condition. | Isolate the minimum answer needed. |
| Compulsive Verification | Proven work is checked repeatedly for reassurance. | Equivalent passes without relevant change. | Define sufficient proof before testing. | Mark proof valid; stop verification. |
| Repetitive Validation | Different tools repeat the same assertion. | Same semantic test strategy. | Record what each command proves. | Reject equivalent rerun; choose missing proof only. |
| Analysis Paralysis | Reasoning blocks a reversible action. | Plans and hypotheses increase; execution stops. | Small evidence-producing experiments. | Pick one bounded action. |
| Retry Loop | Same strategy repeats after failure. | Attempt count reaches three. | Retry budget and novelty requirement. | Change hypothesis or layer, or block. |
| Tool Loop | Searches or commands repeat without information. | Same output or error; no new evidence. | State intended evidence before command. | Stop command; use different source. |
| Test/Fix Loop | Edits alternate with failures or reverts. | Acceptance progress flat across cycles. | Minimal reproduction and targeted test. | Freeze edits; isolate root cause. |
| Refactor Loop | Cleanup changes do not serve DoD. | Churn and reversions in unrelated code. | Refactor gate. | Restore smallest required change; defer cleanup. |
| Replan Loop | Whole plan regenerates after small discoveries. | More than two full replans without evidence. | Local plan updates. | Preserve valid plan; adjust one step. |
| Critic Loop | Reviewers repeatedly invent optional improvements. | More than two rounds; only style findings. | Critic contract and budget. | Classify optional findings; completion gate. |
| Context Reload Loop | Same architecture or files are reread. | Two reloads without source change. | Freshness metadata and compact context. | Use fresh stored facts; reload targeted source only. |
| Architecture Rabbit Hole | A local need becomes repository redesign. | Design scope exceeds acceptance condition. | Architecture redesign gate. | Demand evidence; return to local objective. |
| Premature Optimization | Performance work starts without measured need. | No benchmark or requirement. | Optimization gate. | Park optimization; restore required behavior. |
| Strategy Oscillation | Agent alternates A and B without new facts. | A to B to A to B pattern. | Decision criteria and evidence ledger. | Freeze both; select once by evidence. |
| Infinite Refinement | Correct output is polished indefinitely. | Optional edits near zero remaining DoD items. | Finite DoD and completion pressure. | Stop optional work; deliver proof. |
| Deadlock | No valid action due to missing authority or dependency. | Constraints block every bounded action. | Dependency clarity and early blocker checks. | Isolate; report blocker, evidence, needed input. |
| Livelock | Activity stays high while outcomes do not move. | Four stalled cycles; repeated failures. | Progress ledger and thresholds. | Strategy reset; reduce search space. |
| Evidence-Free Exploration | Speculation opens costly branches. | Hypotheses lack supporting source. | Evidence gate before expansion. | Park speculation; inspect authoritative source. |
| Hallucinated Repository Knowledge | Unobserved facts are stated confidently. | Missing path, output, or source. | Fact, inference, and unknown labels. | Say not confirmed; remove dependency. |
| Completion Avoidance | Agent continues after required proof exists. | DoD complete; one more thing appears. | Completion gate and termination rule. | Record optional follow-up; report and stop. |

## Intervention

Identify the dominant observable failure mode, not every possible label. Lock the objective, classify the active branch, and apply the smallest matching controller. If two modes coexist, resolve the higher-priority dependency first: evidence before speculation; depth before more delegation; strategy reset before another retry; completion before optional refinement. Record only evidence, state, decisions, and results.

## Stop condition

Stop the intervention when the triggering signal is below threshold, one productive next action exists, or a real external blocker is reported. Stop the overall task when the finite Definition of Done is proven.
