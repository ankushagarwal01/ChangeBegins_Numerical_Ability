# Numerical Templates — Pending Changes (to apply together at the end)

Nothing here is executed yet. This is the running list of changes to effect in one
coordinated pass. Kept durable in outputs because /home/claude does not survive a
session reset.

---

## 1. Architecture (locked)

- **Bad patterns live in one keyed file**, `numerical_bad_patterns.md`, one section per
  template ID (same pattern as the prompts JSON). The contract stays untouched.
- **The prompt-builder injects** each template's bad-patterns section into its FOCUSED
  CONTRACT at build time, only where an entry exists, then reruns once to regenerate all
  prompts.
- **Hard guards also become validator checks.** Guards that require computing over all four
  options (e.g. "exactly one subset feasible") can't be done by the LLM mid-generation —
  they become fields in the prompt's `validation_notes` block and are enforced by the
  pipeline's validation node.

### Bad-patterns format (locked)

```
# Bad Patterns — <ID>

Bad patterns (failure → guard):
- <terse failure> → <executable guard>.

Distractors (each defined by the constraint it breaks):
- Correct: <what the right answer is>.
- <PRIMARY_TRAP>: <what it does / breaks>.
- <type>: <what it does / breaks>.
- <type>: <what it does / breaks>.
```

Terse `failure → guard` bad-pattern lines; descriptive distractor lines.

---

## 2. Prompt edits (pending)

- **Remove the synthetic-difficulty guard from all 113 prompts.** Two boilerplate lines:
  - global "LLM Must Not Do": *"Do not add a constraint that does not bind, then call the result L3."*
  - each template's Forbidden block: *"a constraint set with no binding constraint (synthetic)."*
  - Reason: this is a template-design/validation check (strip test / tree scorer), not an
    item-generation rule. The LLM can't act on it — structure is fixed upstream.
  - **Keep** the "more than one valid subset unless intended" line — that IS a legitimate
    generation-time concern (depends on the parameters drawn).

---

## 3. Template 91 — NUM_AL_L3_091 (pending)

Kept as **feasibility** (not converted to optimization — that would need a domain-wide
consistency pass across the allocation L3s: 092 trade-off, 093 pick-valid-option, 094 lever).
The guards handle the multiple-correct-answer bug without converting.

Finalized bad-patterns entry:

```
# Bad Patterns — NUM_AL_L3_091

Bad patterns (failure → guard):
- Two subsets both feasible, one keyed → exactly one of the four may pass all constraints, else regenerate.
- Nothing binds; obvious pick already wins → naive single-metric pick must fail ≥1 constraint.
- Primary-trap distractor is actually feasible → it must break exactly one constraint, strictly.

Distractors (each defined by the constraint it breaks):
- Correct: the unique subset that satisfies every constraint — budget/time, count cap, and per-item value floor — simultaneously.
- IGNORED_CONSTRAINT (primary): clears the headline limit (fits budget/time) but breaks one non-obvious constraint — includes a below-floor item or exceeds the count cap.
- PARTIAL_COMPUTATION: wins on a single metric while ignoring another — highest total value but over budget, or most items but under the value floor.
- ARITHMETIC_SLIP / CLOSE_NUMERIC: misses one constraint by a small margin (one unit over budget, one item just under the floor), landing within ~5–10% of the correct total.
```

- 91's "exactly one subset feasible" guard should also become a `validation_notes` field
  (e.g. `exactly_one_subset_feasible: true`) at build time.

---

## Suggested working approach

- Batch remaining templates **by domain**, not ID order — templates in a domain share
  failure modes (allocation L3s share the feasibility/uniqueness issue; multi-step percent
  templates share additive-vs-multiplicative), so the reasoning is reusable.

---

## Separate workstream — 4-domain source reconciliation (do NOT tangle with the above)

From reconciling the two given source files (markdown vs DB export). Only 4 domains differ:
CI, PT, TSD, TW. The other 14 verified identical (IDs, levels, descriptions; structure
spot-checked on A, D, M).

- **CI:** (1) plain CI-compute is L1 (DB wrongly L2) → level change → new 95+ number.
  (2) CI-with-frequency exists only in markdown → keep → new 95+ number.
  (3) compare-plans — already handled earlier, no action.
  (4) DB-only choose-rate-to-hit-target — drop.
- **TW:** (1) combined-work (035) is L2 (DB wrongly L1) → level change → new 95+ number.
  (2) 036/037 swapped between sources; 037 already handled → 036 needs renumbering → new 95+.
  (3) 038 "feasibility with caps" — synthetic (cap never binds; scorer 20→12 on strip) →
      reclassify to L2 or remove.
  (4) 039 — genuine L3 either way (feasibility-under-availability or optimize-allocation);
      which version to keep still pending.
- **PT (parked):** 046 matches; DB's 047 record is internally inconsistent (description
  "net rate" vs envelope "2-phase"); markdown has a two-phase L2 the DB may not represent;
  L3 numbering disagrees (md 049/050 vs DB 048/049). Needs fresh-eyes resolution.
- **TSD (parked):** genuine content shuffle, not a clean level shift. 040 matches; 044 likely
  matches; 041/042/043/045 differ in concept and/or level. No decisions made.

When applying any ID changes: single simultaneous regex replace over full ID tokens —
never chained .replace() (it corrupted domains B/C/D twice before).

---

## 4. Evidence from the flagged-questions batch (restructured_questions.json, 49 items / 39 templates)

Ran a structural validator over all 49. The failures split three ways, and this
changes the fix strategy — most are NOT template-design problems.

### A. Structural — caught now by `question_validator.py` (14 questions, 13 templates)
Duplicate options, or keyed answer disagreeing with its own explanation.
Templates: AV_020, AV_106, CI_137, DI_079, EST_086, MA_025, MA_109, MS2_131,
PC_098, PN_123, RM_069, RP_003, RP_095.
FIX: run the validator as the first pipeline gate. No per-template work needed.

### B. Design / multiple-correct — need bad-patterns uniqueness guard (4 templates)
AL_091, AL_093, CI_137, RM_069. (137 and 069 also caught structurally.)
FIX: bad-patterns entries written in `numerical_bad_patterns.md`.
- AL_093: several options satisfied all requirements — need exactly one qualifying.
- RM_069: range spanned >1 LCM period → 23/58/93 all valid — bound to one period.

### C. Pure compute errors — need a recompute / clean-answer layer (24 templates)
AL_092, AL_094, CI_113, CI_138, DI_084, MA_110, MA_111, MA_112, MS2_133, MS3_076,
PL_016, PL_101, PL_102, PN_122, PR_057, PR_124, PT_047, PT_049, RM_067, RM_129,
RP_096, RP_097, TW_036, TW_039.
The marked answer is arithmetically wrong and the explanation ITSELF contains the
wrong math — so a structural check can't catch them. These need the item actually
solved from its parameters and the answer recomputed.
FIX: this is the Option-B clean-answer parameter generator + a recompute validator
(the upstream code the prompts already assume exists). Biggest remaining build; it
is what actually clears the bulk of the 49. NOT fixable by bad-patterns text.

### Deliverables added this session
- `question_validator.py` — structural gate (duplicate / correct-count / key-vs-explanation).
- `numerical_bad_patterns.md` — keyed bad-patterns file; entries for AL_091, AL_093, CI_137, RM_069.

### Key takeaway
Bad-patterns files fix design flaws (≈4 templates here). The dominant failure (24
templates) is generation-time arithmetic, fixed only by the clean-answer/recompute
layer. Prioritise building that layer over writing 39 bad-patterns files.

---

## 5. IMPLEMENTED THIS SESSION (moved from pending to done)

### Recompute / clean-answer layer — BUILT (the fix for the 24 compute errors)
- `template_solvers.py` — 15+ deterministic solvers, each with solve() (recompute
  verifier) and the computation for gen_params() (clean-answer generator). Every solver
  VERIFIED to reproduce the correct answer stated in the flag reasons (not the wrong
  marked one). Covers: CI compound, SI-vs-CI compare, mixture replacement, two-ratio mix,
  add-pure, alligation, successive %, count-divisible, circular-adjacent, Bayes, mod,
  mod-pow, CRT-in-range, pipe-net.
- `recompute_validator.py` — the second pipeline gate. REGISTRY maps template_id -> solver.
  recompute_check() recomputes and returns PASS / FAIL_MISMATCH / NO_SOLVER. Demonstrated
  to FAIL every originally-marked wrong answer (i.e. would have caught all these bugs).
  Templates with no solver yet return NO_SOLVER -> route to manual review, never silent pass.

### Prompt edit — APPLIED
- Synthetic-difficulty guard REMOVED from all 113 prompts (verified: neither guard string
  remains; all 113 prompts intact). This check now lives only at template-validation
  (strip test / tree scorer), not item generation.

### Pipeline order (now concrete)
1. Generate item (LLM renders wording around pipeline-injected clean params).
2. `question_validator.py` — structural gate (distinct options, one correct, key==explanation).
3. `recompute_validator.py` — recompute answer in code; reject on mismatch.
4. Accept only if both pass. NO_SOLVER items go to manual review.

## STILL PENDING
- Write solvers for the remaining pure-compute templates not yet covered (AL_092 weighted
  score, AL_094 lever, DI_084 growth-feasibility, MS2_133 area-diff, MS3_076 hollow-volume,
  PL_016/101/102 profit-loss, PL/PR_057 EV, RP_096/097 ratio-word, TW_036/039). Same pattern.
- Wire the bad-patterns injection into the prompt-builder (build step), plus the validator
  fields into validation_notes.
- The 4-domain source reconciliation (CI/TW decided; PT/TSD parked) — unchanged, separate.

---

## 6. FINAL DELIVERABLE COMPLETE — prompts restructured to answer-injection

`numerical_generation_prompts.json` (113 prompts) is the deliverable and is now
restructured so the LLM RENDERS rather than COMPUTES. This is the root fix for the
24 compute errors: the model can no longer key a wrong answer because it no longer
derives one.

Every prompt now:
- Header states the correct answer is injected; the LLM must not recompute.
- Carries an INJECTED block: `parameters`, `correct_answer`, `worked_steps`
  (filled by the pipeline per item — the `<<PIPELINE: ...>>` tokens are the fill points).
- "Render, Do Not Compute" instruction replaces the old "compute and verify" one.
- metadata.correct_answer references the injected value; validation_notes swapped to
  `used_injected_answer / did_not_recompute / all_options_distinct_by_value / primary_trap_present`.
- Distractors must be distinct BY VALUE (not display string).
- Bad-patterns injected for the 4 templates that had design entries.

### The generation flow the prompts now assume
1. Pipeline runs the template's SOLVER (`template_solvers.py`) → clean params + correct answer + worked steps.
2. Pipeline injects those into the prompt's INJECTED block.
3. LLM renders wording + builds distractors around the fixed answer.
4. `question_validator.py` (structural) then `recompute_validator.py` (safety net) gate the result.

### IMPORTANT — ID mismatch found
The flagged-question batch used some IDs that DON'T match the deliverable's prompt keys.
Confirmed case: flagged `NUM_CI_L1_137` == prompt `NUM_CI_L1_031` (plain CI compute).
The "137/138" numbers came from a different/newer numbering than the prompts use.
Before mapping any further flagged fixes onto prompts, reconcile the flagged-batch IDs
against the prompt keys — do not assume the flagged ID is the prompt key.

### Still pending (unchanged)
- Solvers for the remaining ~dozen compute templates (pattern established in template_solvers.py).
- The solver/param generator must run in n8n to fill the INJECTED tokens.
- 4-domain source reconciliation (PT/TSD parked).
