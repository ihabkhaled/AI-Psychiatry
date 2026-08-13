# Executive State Machine

States: idle → focused → drift_warning → attention_reset → strategy_reset → isolated → blocked → complete. Recovery escalates only when observable progress stalls and each level narrows the search space. Block or complete are terminal.

