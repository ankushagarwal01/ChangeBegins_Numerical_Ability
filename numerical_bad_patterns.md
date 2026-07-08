# Numerical Bad Patterns

One section per template ID. The prompt-builder injects a template's section into
its FOCUSED CONTRACT at build time (only where a section exists). Terse
`failure → guard` lines, then descriptive distractor rules.

Guards that require checking all four options (uniqueness, distinctness, key-matches-
explanation) are enforced by `question_validator.py` in the pipeline, not by the LLM.
These entries cover DESIGN-level failures only. Pure arithmetic errors are handled by
the recompute layer, not here.

---

## NUM_AL_L3_091

Bad patterns (failure → guard):
- Two subsets both feasible, one keyed → exactly one of the four may pass all constraints, else regenerate.
- Nothing binds; obvious pick already wins → naive single-metric pick must fail ≥1 constraint.
- Primary-trap distractor is actually feasible → it must break exactly one constraint, strictly.

Distractors (each defined by the constraint it breaks):
- Correct: the unique subset that satisfies every constraint — budget/time, count cap, and per-item value floor — simultaneously.
- IGNORED_CONSTRAINT (primary): clears the headline limit (fits budget/time) but breaks one non-obvious constraint — includes a below-floor item or exceeds the count cap.
- PARTIAL_COMPUTATION: wins on a single metric while ignoring another — highest total value but over budget, or most items but under the value floor.
- ARITHMETIC_SLIP / CLOSE_NUMERIC: misses one constraint by a small margin (one unit over budget, one item just under the floor), landing within ~5–10% of the correct total.

---

## NUM_AL_L3_093

This asks to pick the single valid **option** from a table (vs 091 which asks for a feasible subset). Failure seen in the bank: multiple suppliers satisfied every stated requirement, so several options were equally correct.

Bad patterns (failure → guard):
- Multiple options satisfy all requirements → exactly one option may satisfy all stated requirements; if the item is "which qualifies", tighten a requirement until only one passes, else regenerate.
- No requirement is binding → each wrong option must violate at least one specific requirement; verify which one before accepting.

Distractors (each defined by the requirement it fails):
- Correct: the only option meeting every requirement — cost ceiling, minimum-order, and lead-time — at once.
- IGNORED_CONSTRAINT (primary): beats the headline number (cheapest, or fastest) but violates another requirement (order minimum or lead time).
- PARTIAL_COMPUTATION: best on one attribute read in isolation, fails a second.
- CLOSE_NUMERIC: fails one requirement by a small margin.

---

## NUM_CI_L1_137

Failure seen: options "$662" and "$662.00" were both present — numerically identical, so two correct answers.

Bad patterns (failure → guard):
- Two options equal in value, differ only in formatting → all four options must be distinct by numeric value, not just by string; enforced by the validator.
- Distractor coincides with the correct value after rounding → round all options to the same precision and confirm four distinct values.

Distractors (compound-interest compute):
- Correct: CI = P(1+r/100)^t − P, to the stated precision.
- WRONG_METHOD: simple interest instead of compound (P·r·t/100).
- SCALE_ERROR: reports the amount A instead of the interest A − P.
- CLOSE_NUMERIC: off by one compounding period (t±1) or a small rounding gap — but must remain a distinct value.

---

## NUM_RM_L3_069

Failure seen: "find a number in 1–100 with remainder 3 mod 5 and 2 mod 7" had three valid answers (23, 58, 93) because the range spans more than one LCM(5,7)=35 period, so multiple options were correct.

Bad patterns (failure → guard):
- Range spans more than one modular period → the stated range must contain exactly one solution: bound it to a single LCM period (here ≤35 wide), or ask for "the smallest such number", else multiple options are correct.
- More than one listed option satisfies the congruences → verify exactly one option satisfies all stated congruences; enforced by the validator.

Distractors (CRT-style):
- Correct: the unique value in-range satisfying all congruences (or the smallest, if phrased that way).
- IGNORED_CONSTRAINT (primary): satisfies one congruence but not the other.
- REVERSE_DIRECTION: swaps the remainders between the divisors.
- CLOSE_NUMERIC: the correct value ± one divisor, satisfying neither fully.
