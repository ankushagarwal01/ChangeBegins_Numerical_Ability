# LLM-Ready Numerical Reasoning Template Contracts: Domains A–S

Use this file directly as generation guidance for numerical reasoning questions. The LLM's job is to instantiate the selected template, not to invent the difficulty.

For every generation request, first select or receive a `template_id`. Then obey the corresponding contract exactly.

The organizing idea for this domain is the **computation tree**. Every numerical question decomposes into a tree of typed nodes. The difficulty of a question is a property of its tree structure, not of how large the numbers are or how long the wording is. A template's level is fixed by the shape of tree it requires.

---

## The Computation Tree

Every question is built from five node types:

| Node | Meaning |
| --- | --- |
| `LEAF` | A raw given value taken directly from the problem statement. No computation. |
| `OPERATION` | A pure arithmetic combination of two or more inputs (`+`, `−`, `×`, `÷`, exponent, `mod`). Requires no domain knowledge to recall. |
| `FORMULA` | A domain formula applied to inputs (e.g. `SI = P·R·T/100`, `V = πr²h`, allegation rule). Requires recalling the formula. |
| `MODIFIER` | A node that scales or transforms an intermediate value before it can be used (efficiency factor, time-weighting, applying a percentage change to a running total). |
| `CONSTRAINT` | A node that resolves a comparison, cap, floor, feasibility check, or optimization (`min`, `max`, shortfall, "is it feasible?", "which option wins?"). |

The tree flows upward: leaves at the bottom, the answer at the root.

### Difficulty is determined by tree shape

| Level | Tree signature |
| --- | --- |
| L1 | Depth 1–2. A single `FORMULA` or `OPERATION` applied to leaves. No `MODIFIER`, no `CONSTRAINT`. |
| L2 | Depth 2–3. At least one `OPERATION` that combines two sub-results, or a short chain of dependent operations. No `CONSTRAINT` at the root. May contain a single `MODIFIER` only where the template explicitly allows it. |
| L3 | Depth 3+. The hard part is intrinsic: either a `CONSTRAINT` node at the root that genuinely changes the answer (feasibility, optimization, comparison), OR a structure requiring two interacting sub-computations held simultaneously (simultaneous equations, two-state reasoning, working backwards from a final state). |

### The synthetic-difficulty prohibition

A `CONSTRAINT` node only counts toward L3 if removing it would change the answer or the reasoning required. A constraint that is always satisfied, or that is checked in one trivial line after the real work is done, is **synthetic** and does not raise the level.

Test: strip the constraint. If what remains is already an L2 problem and the constraint never binds, the question is a disguised L2. Do not generate it as L3. Genuine L3 difficulty comes from one of:

- a feasibility or optimization decision where the binding constraint is not obvious in advance,
- simultaneous reasoning across two states or two unknowns,
- working backwards from a final condition,
- a structural trap where the naive method gives a specific wrong answer.

---

## Global Generation Rules

### The LLM Must Preserve

- `template_id`
- `domain`
- `difficulty_level`
- the required computation-tree node types (`tree_signature`)
- answer mode
- number of correct answers
- the parameter bounds and the **clean-answer constraints**
- validator expectations

### The LLM May Vary

- names, labels, objects, currency context, and non-essential surface dressing
- order of options
- natural-language wording
- the specific numeric values, **within the allowed bounds and subject to the clean-answer rule**

### The LLM Must Not Do

- Do not raise difficulty by using bigger numbers, more decimals, or longer wording. Difficulty is fixed by the tree.
- Do not add a constraint that does not bind, then call the result L3.
- Do not introduce information that requires outside knowledge (real interest rates, real distances, real prices).
- Do not produce a question whose answer is not one of the options.
- Do not produce two options with the same value.
- Do not use a node type outside the template's `tree_signature`.
- Do not let the explanation rely on a fact not stated in the question.

---

## The Clean-Answer Rule (mandatory)

Numerical questions fail most often because the parameters were chosen to *look* plausible, not to *divide cleanly*. The investment-ratio failure (a ₹57,000 profit that is not divisible by the capital-month weights) is the canonical example.

**Generate parameters by working backwards from the answer, not forwards from plausible-looking inputs.**

The required order:

1. Fix the structural parameters (ratios, rates, weights, counts).
2. Compute the divisor or denominator the final step will use (sum of ratio parts, sum of capital-months, LCM, total weight).
3. Choose the remaining free parameter (the total, the profit, the budget) to be an exact multiple of that divisor, so every share, every intermediate, and the final answer are integers (or terminate cleanly to the stated precision).
4. Solve the question fully yourself.
5. Confirm the computed answer is exactly equal to the value you place in the correct option.

If a clean answer cannot be produced within the stated bounds, change the structural parameters — never ship a question with a non-terminating or mismatched answer.

---

## Required Output Format

Return every generated item in this structure:

```json
{
  "template_id": "",
  "domain": "",
  "difficulty_level": "",
  "tree_signature": [],
  "answer_mode": "",
  "parameters": {},
  "question": "",
  "options": { "A": "", "B": "", "C": "", "D": "" },
  "correct_option": "",
  "correct_answer": "",
  "computation_tree": "",
  "explanation": "",
  "option_rationales": { "A": "", "B": "", "C": "", "D": "" },
  "validation_notes": {
    "answer_recomputed_matches_option": true,
    "exactly_one_correct": true,
    "all_options_distinct": true,
    "answer_type_sane": true,
    "difficulty_source": ""
  }
}
```

`computation_tree` must show the actual node sequence with the chosen values, e.g. `LEAF(P=3000)+LEAF(R=10)+LEAF(T=3)→FORMULA(SI=900)`.

---

## Answer Modes

| Mode | Use |
| --- | --- |
| `VALUE` | A single numeric answer (the most common). |
| `FEASIBILITY` | A yes/no decision plus the supporting figure ("Yes, ₹3,600 ≥ requirement"). |
| `COMPARISON` | Identify which option/plan/item wins. |
| `RANGE` | A valid range (min–max). |
| `RATIO` | A ratio in lowest terms. |

If the question is not naturally multiple choice, still provide four options.

---

## Option and Distractor Design Rules

Every wrong option must represent a meaningful mistake a test-taker could actually make. No random or impossible distractors.

- Exactly one correct option.
- Three wrong options from **three different error types**.
- All four options similar in magnitude, format, and plausibility.
- No option may equal the correct value.
- The correct option must not be the only one with a different sign, format, or level of precision (that gives the answer away).
- Do not use `none of the above`, `cannot be determined`, or `data insufficient` unless the answer mode explicitly permits it.
- `option_rationales` must explain, for every option, why it is correct or exactly what mistake produces it.

### Numerical distractor taxonomy

| Distractor Type | Meaning |
| --- | --- |
| `ARITHMETIC_SLIP` | Right method, one small calculation error. |
| `WRONG_METHOD` | Wrong formula or wrong approach (e.g. simple interest where compound is required). |
| `SCALE_ERROR` | ×100 / ÷100 mistake, ratio inverted, unit not converted. |
| `PARTIAL_COMPUTATION` | Stops one step early; reports an intermediate as the final answer. |
| `ADDITIVE_PERCENT` | Treats successive percentages/discounts as additive instead of multiplicative. |
| `SUBGROUP_AVERAGE` | Averages averages instead of weighting by counts/totals. |
| `REVERSE_DIRECTION` | Solves for the wrong unknown, or inverts before/after, profit/loss, up/down stream. |
| `IGNORED_CONSTRAINT` | Ignores the cap/floor/feasibility condition that determines the answer. |
| `CLOSE_NUMERIC` | A near value (for L3, at least two distractors within ~5–10% of the correct answer). |

At least one wrong option must encode the **most common misconception** for that template (named in the contract's "primary trap" field). At least two wrong options must be plausible to a student who partially understood the question.

---

## Final Self-Check Before Returning Any Generated Question

Before returning, silently verify:

1. The selected `template_id` is obeyed.
2. The `tree_signature` used matches the template exactly — no extra or missing node types.
3. The difficulty source is structural, not synthetic — stripping any constraint would change the answer.
4. The parameters obey the clean-answer rule; the answer terminates cleanly.
5. You solved the question yourself and the result **exactly equals** the value in `correct_option`.
6. Exactly one option is correct; all four options are distinct.
7. The answer type is sane (a count is a positive integer; a probability is in [0,1]; a percentage is reasonable; a distance is positive).
8. Each wrong option is a distinct, named mistake, and one encodes the primary trap.
9. The explanation proves the answer from the question alone.
10. No forbidden pattern appears.

If any check fails, regenerate before returning.

---
# Domain A: Ratios & Proportions

## Domain Purpose
Test whether the student can split quantities by ratio, find an unknown from a ratio relationship, and reason across two ratio states.

## Domain Tree Operators
`FORMULA(part = total × a/(a+b))`, ratio equalization `OPERATION`, time-weighting `MODIFIER`, two-state simultaneous `OPERATION`.

## Domain-Wide Rules
- The sum of ratio parts must divide the total exactly (clean-answer rule).
- For two-state problems, choose the unknown so all quantities are positive integers.
- Primary traps: averaging ratios, using the original ratio when it has changed, adding to one part only.

---

## NUM_RP_L1_001: Compute part from A:B and total
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { a_b: 2-9, total: divisible by (a+b), total_max: 500 }
primary_trap: SCALE_ERROR (use wrong part of ratio)
```
Contract: Give a ratio A:B and a total; ask for one part. Single formula `total × a/(a+b)`.
Forbidden: any constraint; non-integer answer.
Validator: answer integer; `total` divisible by `(a+b)`; one distractor uses the other part.
Example: "Cement:sand = 3:5, total 240 kg. Cement?" → 90.

## NUM_RP_L1_002: Ratio scaling and comparison
```yaml
difficulty_level: L1
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
allowed_values: { a_b: 2-9, known_part: divisible by its ratio component }
primary_trap: REVERSE_DIRECTION (scale the wrong way)
```
Contract: Give the ratio and one actual quantity (not the total); find the other quantity.
Forbidden: giving the total; non-integer answer.
Validator: scale factor is exact; distractor inverts the ratio.
Example: "Boys:girls = 4:3, 28 boys. Girls?" → 21.

## NUM_RP_L2_003: Chain ratios A:B and B:C
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { parts: 2-12, B_requires_LCM: true }
primary_trap: WRONG_METHOD (multiply ratios without equalizing B)
```
Contract: Two linked ratios; equalize the common term, then find an actual value.
Forbidden: B values already equal (removes the step).
Validator: B equalized via LCM; answer integer.
Example: "A:B=2:3, B:C=4:5, C=60. A?" → 32.

## NUM_RP_L2_004: Split total into 3+ parts
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { parts: 3 parts summing ≤20, total: divisible by part-sum, total: 100-2000 }
primary_trap: PARTIAL_COMPUTATION (find unit value, forget to multiply)
```
Contract: Three-part ratio, split a total, ask one share.
Validator: total divisible by part-sum; shares sum to total.
Example: "₹720 in 2:3:4, B's share?" → 240.

## NUM_RP_L3_005: Ratio change over time
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { ratio_parts: 2-6, time_gap: 3-10, answer: positive integer }
difficulty_source: two ratio states linked by a fixed change → simultaneous equations
primary_trap: REVERSE_DIRECTION (apply change to only one term)
```
Contract: A ratio now, a different ratio after a fixed change; solve for a current value. Set 3x/5x style unknowns, build one equation from each state, solve.
Forbidden: a change that makes the equation degenerate; non-integer solution.
Validator: both states used; unique positive integer solution; recompute matches option.
Example: "Ages 3:5 now, 3:4 in 6 years. A's age?" → 6.

## NUM_RP_L3_006: Investment ratio with mid-period change
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { initial_parts: 1-5, change_month: 3/4/6, multiplier: 2 or 3, profit: divisible by total capital-months }
difficulty_source: time-weighted (capital-month) ratio differs from stated ratio
primary_trap: WRONG_METHOD (split profit by the stated ratio, ignoring time)
```
Contract: Partners invest by ratio; one changes capital partway; split year-end profit. Compute capital-months per partner, derive effective ratio, split profit.
Clean-answer: profit MUST be a multiple of the sum of capital-months (this is the step the canonical bug missed).
Validator: capital-months computed; profit divisible by their sum; every share integer; recompute matches option.
Example: ratio 2:3:5, A doubles after 6 months → weights 36:36:60 (sum 132); choose profit = ₹66,000 → A = ₹18,000.

## NUM_RP_L3_007: Reverse ratio with replacement
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { initial_ratio: {3:1,4:1,5:1,3:2}, total_volume: 20-60, removed: positive integer }
difficulty_source: work backwards from final ratio for unknown removed amount
primary_trap: PARTIAL_COMPUTATION (remove from one component only)
```
Contract: Known initial ratio and total; some mixture removed and replaced with water; known final ratio; find amount removed. Removal scales both components; set equation from final ratio.
Validator: removal proportional to both parts; integer answer; recompute matches.
Example: "30 L, milk:water 4:1, becomes 2:3, how much removed?" → 15.

---

# Domain B: Percentages & Growth

## Domain Purpose
Test percentage computation, reverse percentage, and multi-variable / successive-change reasoning.

## Domain-Wide Rules
- Successive changes apply to the running value, never the original.
- Reverse problems must yield an integer original.
- Primary traps: additive treatment of successive percentages; applying change to original base each time.

---

## NUM_PC_L1_007: Percent of a number
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { base: 100-1000, p: {5,10,15,20,25,30}, result: integer }
primary_trap: SCALE_ERROR
```
Contract: `base × p/100`. Example: 15% of 480 → 72.

## NUM_PC_L1_008: Percent change
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { original: 50-500, new: 60-600, change: whole-number % }
primary_trap: SCALE_ERROR (divide by new instead of original)
```
Contract: `(new−original)/original × 100`. Example: 200→250 → 25%.

## NUM_PC_L2_009: Reverse percentage
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
allowed_values: { result: 100-2000, p: {10,15,20,25}, original: integer }
primary_trap: WRONG_METHOD (subtract p% of the result instead of dividing)
```
Contract: original = result / (1 ± p/100). Example: after +20% it is 960 → 800.

## NUM_PC_L2_010: Weighted percentage across groups
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { p: 10-50, n: 10-100, result: ≤1 decimal }
primary_trap: SUBGROUP_AVERAGE (average the two percentages)
```
Contract: weight each percentage by its group size. Example: 70%×40 + 80%×60 → 76%.

## NUM_PC_L3_011: Successive percentage changes
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { changes: 2-3 from ±{10,15,20,25,30}, net: non-trivial }
difficulty_source: multiplicative chaining on a running base
primary_trap: ADDITIVE_PERCENT
```
Contract: apply each change to the running value from base 100; report net % from original.
Validator: not simply additive; at least one distractor is the additive answer.
Example: +20, −20, +25 → net +20%.

## NUM_PC_L3_012: Reverse-engineer original from multi-variable outcome
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { turnout: {70,75,80,85}, gap%: {10,12,15,20}, margin: divisible by gap% }
difficulty_source: two unknowns resolved sequentially backwards from a margin
primary_trap: PARTIAL_COMPUTATION (stop at votes cast, forget turnout step)
```
Contract: percentages of percentages with a known absolute margin; work back to the base.
Clean-answer: margin divisible by the gap percentage; turnout divides the result evenly.
Example: 80% turnout, A 55% vs B 40%, margin 3600 → 30,000 registered.

## NUM_PC_L3_013: Successive discounts and profit
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { markup: {30,35,40,45,50}, discounts: two of {10,12,15,20}, result: non-zero }
difficulty_source: markup then two multiplicative discounts, profit measured on cost
primary_trap: ADDITIVE_PERCENT (sum the two discounts)
```
Contract: mark up cost, apply two successive discounts to running price, compute profit/loss on cost.
Example: +40% markup, −10% then −15% → +7.1% profit.

---

# Domain C: Profit / Loss / Discount

## Domain Purpose
Cost-price relationships, discounting, and multi-party or weighted transactions.

## Domain-Wide Rules
- Profit/loss always measured on cost price unless stated.
- Chain transactions resolve backwards.
- Primary traps: measuring profit on the wrong base; assuming equal-SP gains and losses cancel.

---

## NUM_PL_L1_013: Profit or loss percentage
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { CP: 100-500, SP: 80-700, result: whole % }
primary_trap: SCALE_ERROR (measure on SP)
```
`(SP−CP)/CP × 100`. Example: 400→500 → 25%.

## NUM_PL_L1_014: Discount price
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { MRP: 100-1000, d: {5,10,15,20,25}, SP: integer }
primary_trap: ARITHMETIC_SLIP
```
`MRP × (1 − d/100)`. Example: ₹600 − 15% → ₹510.

## NUM_PL_L2_015: Markup then discount
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { CP: 200-800, markup: {20,25,30,40,50}, discount: {10,15,20} }
primary_trap: ADDITIVE_PERCENT
```
MRP from markup, SP from discount, profit on CP. Example: 500, +40%, −25% → +5%.

## NUM_PL_L2_016: Compare two offers
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: COMPARISON
allowed_values: { both effective prices integer }
primary_trap: PARTIAL_COMPUTATION (compare headline numbers not effective prices)
```
Two parallel formula branches feeding a comparison. Example: ₹1000−20% vs ₹1100−30% → B cheaper.

## NUM_PL_L2_017: Same selling price, one profit one loss
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { SP equal, ±p%: {10,20} }
primary_trap: WRONG_METHOD (assume net zero)
```
Two items at equal SP, +p% and −p%; the CPs differ so there is a net loss. Example: ₹1200 each, ±20% → loss ₹100.

## NUM_PL_L3_017: Chain of transactions
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { margins: ±{15,20,25}, final_price: divides cleanly back }
difficulty_source: work backwards through two successive margins
primary_trap: ADDITIVE_PERCENT (combine the two margins directly)
```
A→B→C with stated margins and C's price; find A's cost. Divide back through each margin.
Clean-answer: final price chosen so each back-division is exact.
Example: +20% then +15%, C pays ₹2760 → A paid ₹2000.

## NUM_PL_L3_018: False weight with markup
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { false_weight: {800,900}g per 1kg, markup: {5,10} }
difficulty_source: two gain sources compounding multiplicatively
primary_trap: PARTIAL_COMPUTATION (count only one gain source)
```
Combine weight gain (1000/false − 1) with markup multiplicatively. Example: 900 g + 10% → 22.2%.

---

# Domain D: Averages & Weighted Mean

## Domain Purpose
Means, weighted means, and problems that require reasoning with totals rather than averages.

## Domain-Wide Rules
- Always convert averages to totals before manipulating.
- Primary traps: averaging averages; subtracting averages directly.

---

## NUM_AV_L1_019: Simple average
```yaml
difficulty_level: L1
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { 3-5 values 10-100, result clean }
primary_trap: ARITHMETIC_SLIP
```
Sum then divide. Example: 45,60,75,80 → 65.

## NUM_AV_L2_020: Weighted average
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { 2-3 value-weight pairs, result ≤1 decimal }
primary_trap: SUBGROUP_AVERAGE
```
Weight by counts. Example: 70(w3),80(w2) → 74.

## NUM_AV_L2_021: Replace one item
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { avg 30-80, n 4-10 }
primary_trap: PARTIAL_COMPUTATION
```
Adjust the total, recompute the average. Example: avg 60 of 5, replace 40 by 80 → 68.

## NUM_AV_L2_022: Reverse average (missing value)
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { target avg 50-90, n 4-6 }
primary_trap: REVERSE_DIRECTION
```
Required total minus current total. Example: 55,60,70,65; need avg 65 over 5 → 75.

## NUM_AV_L2_023: Reverse weighted average
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { group avgs 40-90, target between them }
primary_trap: SUBGROUP_AVERAGE
```
Given two group averages and a target overall, find the required subgroup change. Example: A(4)@60, B(6)@80, target 72 → already 72, change 0.

## NUM_AV_L3_022: Overlapping subgroups
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: track three subgroup totals simultaneously
primary_trap: SUBGROUP_AVERAGE
```
Overall average plus two overlapping subgroup averages; find the remaining group's average via totals. Example: 8 nums avg 20, first-3 avg 15, last-3 avg 25 → middle-2 avg 20.

## NUM_AV_L3_023: Batting average drop
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: must use totals; subtracting averages fails
primary_trap: WRONG_METHOD (subtract the averages)
```
Average before and after extra innings; find the average over the new innings. Example: 48 after 20, 45 after 25 → 33 in the 5.

## NUM_AV_L3_024: Unknown group size
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { group size chosen so n is a positive integer }
difficulty_source: group size is the unknown; set up and solve an equation
primary_trap: SUBGROUP_AVERAGE
```
Overall average, two subgroup averages, one subgroup size known; solve for the other size.
Clean-answer: choose averages and known size so the unknown count is an integer.
Example: all @600, mgrs @800 (12), non-mgrs @550 → 48 non-managers.

---

# Domain E: Mixtures & Allegations

## Domain Purpose
Concentration mixing, replacement, and reverse / multi-source mixture problems.

## Domain-Wide Rules
- Replacement multiplies concentration by (1−fraction) each step.
- Adding a pure substance changes numerator and denominator together.
- Primary traps: mishandling the equal-amounts condition; wrong equation when adding pure substance.

---

## NUM_MA_L1_024: Final concentration
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { c: {20..80}%, q: multiples of 10, result integer % }
primary_trap: SUBGROUP_AVERAGE (average the two concentrations)
```
`(c1q1+c2q2)/(q1+q2)`. Example: 40L@60% + 60L@40% → 48%.

## NUM_MA_L2_025: Allegation ratio
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA]
answer_mode: RATIO
allowed_values: { c1 < target < c2, ratio small integers }
primary_trap: REVERSE_DIRECTION (invert the allegation)
```
`(c2−target):(target−c1)`. Example: 20% & 60% → 40% → 1:1.

## NUM_MA_L2_026: One-step replacement
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, FORMULA]
answer_mode: VALUE
allowed_values: { volume 50-200, drain fraction simple }
primary_trap: PARTIAL_COMPUTATION
```
Remove fraction, refill, recompute. Example: 100L@80%, remove 25 → 60%.

## NUM_MA_L2_027: Multi-step replacement
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { initial c {60,70,80}, drain {1/4,1/5}, steps 2-4 }
primary_trap: WRONG_METHOD (subtract fraction each step instead of multiplying)
```
`c × (1−f)^n`. Example: 80%, drain 1/4, 2 steps → 45%.

## NUM_MA_L3_027: Three sources, equal amounts
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: convert ratios to fractions and combine under equal-weight mixing
primary_trap: WRONG_METHOD (average the ratios as written)
```
Equal amounts of solutions with given component fractions; find resulting fraction. Average the fractions, not the ratios.
Clean-answer: choose fractions whose average terminates.

## NUM_MA_L3_028: Add pure substance
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { volume, start %, target %, answer integer L }
difficulty_source: pure addition changes numerator and denominator together
primary_trap: WRONG_METHOD (treat denominator as fixed)
```
`(start_amount + x)/(volume + x) = target`; solve for x. Example: 40L@30%, target 50% → add 16 L.

## NUM_MA_L3_029: Reverse mixture
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: two unknowns, two equations (volume + concentration)
primary_trap: PARTIAL_COMPUTATION (one equation only)
```
Known final volume and concentration from two known-strength solutions; find how much of each. Example: 60L@40% from 25% and 70% → 40 L of the 25%.

---
# Domain F: Simple & Compound Interest

## Domain Purpose
Interest computation and the structural problems that interest enables (doubling time, CI−SI difference).

## Domain-Wide Rules
- SI is linear; CI is multiplicative. Keep the distinction sharp — it is the main trap.
- Primary traps: using SI where CI is required; treating doubling as a fixed add-on.

---

## NUM_SI_L1_029: Simple interest
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { P: 500-5000 (×500), R: {5,8,10,12,15}, T: 1-5, SI integer }
primary_trap: SCALE_ERROR
```
`P·R·T/100`. Example: 2000,10%,3 → 600.

## NUM_CI_L1_031: Compound interest
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { P: 1000-5000, R: {5,8,10}, T: 2-3, A integer }
primary_trap: WRONG_METHOD (compute SI)
```
`A=P(1+R/100)^T`, CI=A−P. Example: 1000,10%,2 → 210.

## NUM_SI_L2_030: SI with unknown
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { unknown integer }
primary_trap: REVERSE_DIRECTION
```
Rearrange SI for P, R, or T. Example: SI 900, 10%, 3y → P 3000.

## NUM_CI_L2_032: CI with frequency
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { n: {2,4}, A integer }
primary_trap: SCALE_ERROR (forget to divide R by n)
```
Adjust rate and periods for frequency. Example: 4000,10% half-yearly,1y → CI 410.

## NUM_CI_L2_033: Compare two plans
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: COMPARISON
allowed_values: { both amounts integer }
primary_trap: PARTIAL_COMPUTATION (compare principals not final amounts)
```
Two parallel CI computations, compare. (Stripped from the old synthetic L3.)

## NUM_SI_L3_034: Doubling / tripling time
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: derive rate from doubling, reuse for a different multiple
primary_trap: WRONG_METHOD (treat tripling time as 1.5× doubling time additively without the SI logic)
```
A sum doubles in T years at SI → interest equals principal in T → rate known → solve for the time to reach another multiple. Example: doubles in 8y → triples in 16y.

## NUM_CI_L3_035: CI − SI difference
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { 2-year difference, R: {5,10}, P integer }
difficulty_source: use difference = P(R/100)² to solve backwards
primary_trap: WRONG_METHOD (compute CI and SI separately and subtract with an error)
```
For 2 years, CI−SI = P(R/100)². Given the difference and rate, find P. Example: diff 100 at 10% → P 10,000.

---

# Domain G: Time & Work

## Domain Purpose
Work rates, combined work, efficiency, multi-phase scheduling, and three-equation rate systems.

## Domain-Wide Rules
- Work = rate × time; rates add.
- Primary traps: averaging days instead of adding rates; mishandling phase boundaries.

---

## NUM_TW_L1_034: Single worker
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { days 4-20, integer answer }
primary_trap: REVERSE_DIRECTION
```
Rate 1/days, apply to a time or fraction. Example: 15 days, 5 days → 1/3.

## NUM_TW_L2_035: Two workers combined
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { TA,TB 4-24, clean combined time }
primary_trap: WRONG_METHOD (average the days)
```
Add rates, invert. Example: 10 & 15 → 6 days.

## NUM_TW_L2_036: Start/stop times
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { clean phase boundaries }
primary_trap: PARTIAL_COMPUTATION
```
One works alone then joined; account for work per phase. Example: A 12, B 8, A alone 4 days first → 7.2 total.

## NUM_TW_L2_037: Efficiency multiplier
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, MODIFIER, OPERATION]
answer_mode: VALUE
allowed_values: { eff {0.5,0.75,1.25,1.5}, clean answer }
primary_trap: SCALE_ERROR (multiply time by efficiency instead of dividing)
```
Effective rate = base × efficiency; time = work / effective. (Moved down from L3 — a single modifier, no binding constraint.) Example: 20 days @75% → 26.67.

## NUM_TW_L3_038: Multi-phase with cap
```yaml
difficulty_level: L3
tree_signature: [LEAF, FORMULA, OPERATION, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: FEASIBILITY
difficulty_source: work tracked across phases against a binding day cap
primary_trap: IGNORED_CONSTRAINT
```
Phased work with different teams; decide if it completes within a cap that can actually bind.
Validator: the cap must be capable of being exceeded by a plausible wrong method.

## NUM_TW_L3_039: Feasibility under availability
```yaml
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: FEASIBILITY
difficulty_source: availability windows reduce effective contribution; feasibility genuinely uncertain
primary_trap: IGNORED_CONSTRAINT
```
Workers with limited availability or reduced efficiency; decide if the deadline is met.

## NUM_TW_L3_040: Three-equation rate system
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { pair-times chosen so individual rates are clean }
difficulty_source: solve a 3-equation system from pairwise rates
primary_trap: WRONG_METHOD (average the three pair-times)
```
A+B, B+C, A+C times given; find all-three time or one worker alone. Sum the pairs = 2(A+B+C).
Clean-answer: choose pair-times so the combined and individual rates invert to clean numbers.

---

# Domain H: Time–Speed–Distance

## Domain Purpose
Motion, relative speed, train crossing, routing, arrival windows, and boats-and-streams systems.

## Domain-Wide Rules
- Convert units before combining (km/h ↔ m/s).
- Primary traps: forgetting length in crossing; adding when subtracting relative speeds; reporting path length not net.

---

## NUM_TSD_L1_040: Basic motion
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { S 20-100, T 1-6, D integer }
primary_trap: REVERSE_DIRECTION
```
D=S×T. Example: 60,3 → 180.

## NUM_TSD_L2_041: Relative speed
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { integer meeting time }
primary_trap: WRONG_METHOD (add when same direction / subtract when opposite)
```
Relative speed then time. Example: 60 & 40 opposite, 400 km → 4 h.

## NUM_TSD_L2_042: Train crossing
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { lengths combine; speed in m/s }
primary_trap: PARTIAL_COMPUTATION (omit platform/object length)
```
Total distance = sum of lengths. Example: 200 m train @72 km/h, 100 m platform → 15 s.

## NUM_TSD_L3_043: Multi-segment routing
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION, CONSTRAINT]
answer_mode: FEASIBILITY
difficulty_source: sum segment times plus stop against a deadline that can bind
primary_trap: IGNORED_CONSTRAINT
```
Two segments at different speeds plus a stop; decide if within deadline.

## NUM_TSD_L3_045: Optimize speed for arrival window
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, CONSTRAINT]
answer_mode: RANGE
difficulty_source: compute both bounds of a feasible speed band
primary_trap: REVERSE_DIRECTION (swap min/max bound)
```
Arrive within a window → min and max speed; check against a vehicle cap. Example: 240 km in 3–4 h → 60–80 km/h.

## NUM_TSD_L3_046: Boats and streams system
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { two trips chosen so upstream/downstream rates are clean }
difficulty_source: two equations, two unknowns (still-water and stream speed)
primary_trap: WRONG_METHOD (average the trip speeds)
```
Two up/down trips with times; separate into 1/u and 1/d, solve, recover still-water and stream speeds.
Clean-answer: pick distances and times so u and d are integers.

---

# Domain I: Pipes / Tanks / Flow

## Domain Purpose
Fill/empty rates, multi-pipe combinations, phased fills, proportional-rate pipes, and schedule optimization.

## Domain-Wide Rules
- Net rate = inflows − outflows.
- Primary traps: sign errors on the drain; mishandling phase boundaries.

---

## NUM_PT_L1_046: One inlet one outlet
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { Tf<Te, integer fill time }
primary_trap: SCALE_ERROR (add rates instead of subtracting)
```
Net = 1/Tf − 1/Te. Example: 6 & 9 → 18 h.

## NUM_PT_L2_047: Multiple inlets/outlets
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { rates yield clean fill time }
primary_trap: WRONG_METHOD
```
Combine all rates. Example: 4,6 in; 8 out → 24/7 h.

## NUM_PT_L2_048: Two-phase fill
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { clean phase volumes }
primary_trap: PARTIAL_COMPUTATION
```
Fill alone, then a drain opens. Example: 8 h fill, 3 h alone, drain 12 h → 18 h total.

## NUM_PT_L2_049: Three-phase fill
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { clean phase volumes }
primary_trap: PARTIAL_COMPUTATION
```
Extension of two-phase to a third phase. (Stripped from the old synthetic L3 — no binding capacity.)

## NUM_PT_L3_050: Proportional-rate pipes
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { combined time chosen so r is a clean fraction }
difficulty_source: set rates as r, 2r, 4r and solve
primary_trap: WRONG_METHOD (divide combined time by 3)
```
Each pipe a fixed multiple of the previous; together fill in T; find the slowest alone. Example: r,2r,4r together 4 h → slowest 28 h.

## NUM_PT_L3_051: Optimize schedule
```yaml
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: cost/time trade-off where the cheapest option within the cap is non-obvious
primary_trap: IGNORED_CONSTRAINT (pick the cheapest ignoring the time cap)
```
Pipe combinations with per-hour costs and a time cap; minimize cost subject to the cap. The cap must eliminate the naively-cheapest option.

---

# Domain J: Permutations & Combinations

## Domain Purpose
Counting arrangements and selections, including restricted, circular, and divisibility-constrained counts.

## Domain-Wide Rules
- State clearly whether order matters.
- Primary traps: P vs C confusion; treating restricted items wrongly; circular off-by-one.

---

## NUM_PN_L1_050: Basic nPr/nCr
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { n 4-8, r 2-4, result ≤5040 }
primary_trap: WRONG_METHOD (P vs C)
```
Single formula. Example: arrange 4 → 24.

## NUM_PN_L2_051: Choose P vs C
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, FORMULA]
answer_mode: VALUE
allowed_values: { clear ordered/unordered cue }
primary_trap: WRONG_METHOD
```
Decide order relevance, then apply. Example: committee of 3 from 6 → 20.

## NUM_PN_L2_052: Restricted arrangements
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, FORMULA, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { group size 2-3, answer ≤10000 }
primary_trap: PARTIAL_COMPUTATION (forget internal arrangements)
```
Glue group as a unit, multiply by internal arrangements. Example: 5 in a row, A&B together → 48.

## NUM_PN_L2_053: Multi-constraint counting (gap method)
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { small n }
primary_trap: WRONG_METHOD
```
No-two-adjacent via the gap method, or total-minus-together. (Moved down from L3 — mechanical once known.) Example: 3M 3W no two men adjacent → 144.

## NUM_PN_L3_054: Divisibility arrangement
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: select digit-sets meeting a divisibility property, then permute
primary_trap: PARTIAL_COMPUTATION (count permutations without filtering by the property)
```
Form k-digit numbers from a digit pool divisible by 3 or 5; select valid digit-sets, then arrange.

## NUM_PN_L3_055: Circular with restriction
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: circular base count (n−1)! adjusted for a together/apart restriction
primary_trap: WRONG_METHOD (use linear n! base)
```
Round-table arrangement with a not-adjacent or together rule. Example: 6 round a table, two never adjacent → 72.

---

# Domain K: Probability

## Domain Purpose
Event probability, complement, sequential draws, expected-value decisions, and conditional / Bayes reasoning.

## Domain-Wide Rules
- Probabilities lie in [0,1]; answers usually simple fractions.
- Primary traps: forgetting to update after no-replacement; ignoring base rates in Bayes.

---

## NUM_PR_L1_054: Basic probability
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { simple fraction }
primary_trap: SCALE_ERROR
```
favorable/total. Example: 4 red of 10 → 2/5.

## NUM_PR_L2_055: Complement / at-least-one
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { simple fraction }
primary_trap: WRONG_METHOD (sum individual probabilities)
```
1 − P(none). Example: 4 tosses, at least one head → 15/16.

## NUM_PR_L2_056: Sequential draws
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { simple fraction }
primary_trap: PARTIAL_COMPUTATION (forget to update the bag)
```
With/without replacement; update between draws. Example: 3R 5B, first red second blue → 15/56.

## NUM_PR_L3_057: Expected-value decision
```yaml
difficulty_level: L3
tree_signature: [LEAF, FORMULA, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: compute EV net of cost, compare options
primary_trap: IGNORED_CONSTRAINT (ignore the entry cost)
```
EV with payoffs/probabilities minus cost; decide which option or whether to play.

## NUM_PR_L3_058: Conditional / Bayes
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: posterior from total probability and base rates
primary_trap: WRONG_METHOD (use the defect rate directly, ignore base rates)
```
Sources with base rates and conditional rates; given the event, find the source posterior. Example: machines 50/30/20%, defects 2/3/5%, given defective → P(A)=0.345.

## NUM_PR_L3_059: Conditional on event
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: restrict the sample space, then compute within it
primary_trap: PARTIAL_COMPUTATION (use the full sample space)
```
Condition on a stated event (sum ≥ 9), compute a probability within the restricted space.

---
# Domain L: Number Series & Patterns — capped at L2

## Domain Purpose
Infer the rule governing an ordered sequence and extend it.

## Domain note on level ceiling
Pattern recognition resolves in a single insight; it is not multi-step computation. This domain **does not have a genuine L3**. A "choose the rule from options" framing is easier, not harder, because options can be tested. Do not generate L3 series questions.

## Domain-Wide Rules
- The intended rule must be nameable and fit every visible term.
- Values usually within −100 to 300.
- Primary traps: using only the first two transitions; applying the change in the wrong direction.

---

## NUM_NS_L1_058: AP/GP next term
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { AP d 2-6, GP r 2-3, next ≤500 }
primary_trap: WRONG_METHOD (AP vs GP)
```
Single constant step or ratio. Example: 3,6,12,24 → 48.

## NUM_NS_L2_059: Mixed-operations series
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { position-dependent or composed step }
primary_trap: PARTIAL_REASONING (use only the first two transitions)
```
Step depends on position or repeats a two-op transform. Example: 2,4,12,48,240 (×2,×3,×4,×5) → 1440.

## NUM_NS_L2_060: Alternating two-rule series
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { two interleaved subsequences }
primary_trap: WRONG_METHOD (treat as one rule)
```
Split odd/even positions into two rules. Example: 2,5,4,10,8,20 → 16.

## NUM_NS_L2_061: Rule identification
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION]
answer_mode: COMPARISON
allowed_values: { exactly one rule fits all terms }
primary_trap: PARTIAL_REASONING
```
Four candidate rules; exactly one fits every term; pick it and the next term. (Moved down from L3.) Example: 1,2,5,10,17,26 → n²+1, next 37.

---

# Domain M: Divisibility / HCF / LCM

## Domain Purpose
Number properties, HCF/LCM relations, and constrained number-finding.

## Domain-Wide Rules
- Use the HCF×LCM = product relation where relevant.
- Primary traps: confusing HCF and LCM; off-by-remainder errors.

---

## NUM_DV_L1_062: Divisibility check
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { n 50-500, d common divisor }
primary_trap: ARITHMETIC_SLIP
```
Apply a divisibility rule. Example: 432 by 9 → yes.

## NUM_DV_L2_063: Apply LCM/HCF
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA]
answer_mode: VALUE
allowed_values: { numbers 6-60 }
primary_trap: WRONG_METHOD (HCF vs LCM)
```
Factorize then compute. Example: LCM(12,18,24) → 72.

## NUM_DV_L2_064: Prime factorization reasoning
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { n 50-300 }
primary_trap: PARTIAL_COMPUTATION
```
Derive a property (factor count, sum of primes) from the factorization. Example: factors of 360 → 24.

## NUM_DV_L3_065: HCF–LCM product relation
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { other number integer }
difficulty_source: use product = HCF × LCM, a non-obvious relation
primary_trap: WRONG_METHOD (add or average instead)
```
Given HCF, LCM and one number, find the other. Example: HCF 12, LCM 432, one is 48 → 108.

## NUM_DV_L3_066: Common-remainder problem
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: VALUE
difficulty_source: LCM plus offset, smallest in range
primary_trap: PARTIAL_COMPUTATION (forget to add the remainder)
```
Smallest number leaving a fixed remainder under several divisors. Example: remainder 6 under 12,15,20,35 → LCM 420 + 6 = 426.

---

# Domain N: Remainders / Modular

## Domain Purpose
Modular arithmetic, remainder cycles, CRT-style constraint solving, and large-power remainders.

## Domain-Wide Rules
- Large powers reduce via the cycle length.
- Primary traps: not reducing the exponent mod the cycle; wrong cycle length.

---

## NUM_RM_L1_067: Simple remainder
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { n 10-200, d 3-12 }
primary_trap: ARITHMETIC_SLIP
```
n mod d. Example: 47 mod 8 → 7.

## NUM_RM_L2_068: Remainder cycles
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { base {2,3,7,8}, exponent 10-50 }
primary_trap: SCALE_ERROR (wrong cycle length)
```
Units digit via the cycle. Example: 7^45 → 7.

## NUM_RM_L3_069: CRT-style candidate
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: VALUE
allowed_values: { coprime moduli, unique solution < range }
difficulty_source: intersect two modular constraints
primary_trap: PARTIAL_COMPUTATION (satisfy one congruence only)
```
Find N meeting two congruences in a range. Example: N≡2(3), N≡3(5), <100 → 38.

## NUM_RM_L3_070: Large-power remainder
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: reduce a large exponent via the cycle mod m
primary_trap: WRONG_METHOD (compute the power directly)
```
Remainder of base^big mod m. Example: 2^100 mod 7 → cycle length 3, 100 mod 3 = 1 → 2.

## NUM_RM_L3_071: Last two digits
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: cycle mod 100 (longer cycle than mod 10)
primary_trap: SCALE_ERROR (use the mod-10 cycle)
```
Last two digits of base^big. Example: 7^81 → cycle 4 mod 100, → 07.

---

# Domain O: Mensuration 2D

## Domain Purpose
Area, perimeter, composite shapes, and genuine spatial reasoning (paths, reshaping).

## Domain-Wide Rules
- π = 22/7 unless stated; integer answers preferred.
- Primary traps: wrong outer dimension for a path; assuming same perimeter gives same area.

---

## NUM_MS2_L1_071: Area/perimeter
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { circle r 3-14, rectangle 4-20 }
primary_trap: WRONG_METHOD (area vs perimeter)
```
Single formula. Example: circle r 7 → 154.

## NUM_MS2_L2_072: Composite / missing dimension
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { integer result }
primary_trap: PARTIAL_COMPUTATION
```
Two shapes combined or one dimension solved first. Example: L-shape 12×8 minus 4×3 → 84.

## NUM_MS2_L2_073: Cost with wastage
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
allowed_values: { wastage {10,15,20}% }
primary_trap: SCALE_ERROR (apply wastage to net not gross)
```
Gross area = net/(1−wastage); cost. (Stripped from synthetic L3.) Example: 100 m² @₹300, 20% wastage → ₹37,500.

## NUM_MS2_L3_074: Path around a rectangle
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: outer-minus-inner area with correct dimension adjustment
primary_trap: SCALE_ERROR (add width once instead of twice)
```
Uniform-width path inside/outside a rectangle. Example: 2 m path outside 20×15 → 156 m².

## NUM_MS2_L3_075: Wire reshaped
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: same perimeter, two shapes, compare areas
primary_trap: WRONG_METHOD (assume equal area)
```
Wire bent into circle then square; compare areas. Example: 88 cm → circle 616, square 484, diff 132.

---

# Domain P: Mensuration 3D

## Domain Purpose
Volume, surface area, hollow solids, and conservation/spatial reasoning (melting, painted cubes).

## Domain-Wide Rules
- π = 22/7 unless stated.
- Primary traps: forgetting cube/recasting volume conservation; miscounting painted faces.

---

## NUM_MS3_L1_075: Volume/surface area
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
allowed_values: { cube 4-15, cylinder r 3-10 }
primary_trap: WRONG_METHOD
```
Single formula. Example: cube edge 6 → 216.

## NUM_MS3_L2_076: Hollow / composite
```yaml
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: VALUE
allowed_values: { integer result }
primary_trap: PARTIAL_COMPUTATION
```
Outer minus inner. Example: hollow cylinder r6/r4 h14 → 880.

## NUM_MS3_L2_077: Capacity with efficiency
```yaml
difficulty_level: L2
tree_signature: [LEAF, MODIFIER]
answer_mode: VALUE
allowed_values: { eff {60,70,75,80}% }
primary_trap: SCALE_ERROR
```
Effective output = rate × efficiency × time. (Stripped from synthetic L3.) Example: 600 L/h @75%, 8 h → 3,600 L.

## NUM_MS3_L3_078: Melting and recasting
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: volume conservation, ratio of cubes
primary_trap: WRONG_METHOD (use radius ratio not volume ratio)
```
One solid melted into many; count by volume. Example: sphere r6 → spheres r1 → 216.

## NUM_MS3_L3_079: Painted cube
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
difficulty_source: spatial classification of small cubes by painted-face count
primary_trap: WRONG_METHOD (confuse edge/face/corner cubes)
```
Painted cube cut into unit cubes; count those with k painted faces. Example: 4-cube, exactly 2 faces → 24.

---

# Domain Q: Data Interpretation — well-built, unchanged

## Domain Purpose
Read structured data, compute derived metrics, and make decisions / feasibility judgments from it.

## Domain-Wide Rules
- All data needed must be in the table; no outside knowledge.
- Primary traps: reading the wrong cell; ignoring a constraint in decision problems.

---

## NUM_DI_L1_079: Read and compute
```yaml
difficulty_level: L1
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
primary_trap: ARITHMETIC_SLIP
```
One read plus one operation. Example: sum four quarters → 200.

## NUM_DI_L2_080: Multi-step derived metric
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
primary_trap: PARTIAL_COMPUTATION
```
Per-row metric then aggregate/compare. Example: revenue = price×qty, compare → B by 2,000.

## NUM_DI_L2_081: Infer missing value
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
primary_trap: ARITHMETIC_SLIP
```
Total minus known. Example: missing department → 100.

## NUM_DI_L3_082: Decision under constraint
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: filter options against several binding constraints
primary_trap: IGNORED_CONSTRAINT
```
Score options, eliminate by constraints, pick the survivor(s).

## NUM_DI_L3_083: Sensitivity analysis
```yaml
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: recompute a subset after a change and detect a ranking shift
primary_trap: PARTIAL_COMPUTATION
```
Change one metric, re-rank, decide if the order changes.

## NUM_DI_L3_084: Feasibility to hit KPI
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: FEASIBILITY
difficulty_source: project growth and test against a target that can genuinely fail
primary_trap: IGNORED_CONSTRAINT
```
Project at max growth and compare to a target. Example: 42 @6% for 3 months → 50.02 ≥ 50 feasible.

---

# Domain R: Estimation & Approximation — capped at L2

## Domain Purpose
Rounding, bounding, and approximate comparison.

## Domain note on level ceiling
Estimation's genuine skill is bounding and approximating — L1/L2 work. The old "robust decision across scenarios" L3 was synthetic. **No genuine L3**; do not generate one.

## Domain-Wide Rules
- Approximations must be defensible to the stated precision.
- Primary traps: rounding the wrong direction; over-precise false answers.

---

## NUM_EST_L1_085: Rounding
```yaml
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
primary_trap: REVERSE_DIRECTION
```
Round to a stated place. Example: 347 to nearest 100 → 300.

## NUM_EST_L2_086: Bounds-based choice
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: COMPARISON
primary_trap: PARTIAL_COMPUTATION (evaluate at one bound only)
```
Evaluate options at both bounds, identify the crossover. Example: fixed ₹90 vs cost+5% over ₹80–100 → B cheaper below ₹85.71.

## NUM_EST_L2_087: Approximate ratio / product
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
primary_trap: SCALE_ERROR
```
Approximate a ratio or product. Example: 198×51 ≈ 10,000.

---

# Domain S: Resource Allocation & Constraints — L3-heavy, unchanged

## Domain Purpose
Budget/capacity allocation and multi-constraint optimization, feasibility, and trade-off decisions.

## Domain-Wide Rules
- All constraints must be stated; the binding one should not be obvious in advance.
- Primary traps: satisfying capacity but ignoring another constraint; picking the naive optimum.

---

## NUM_AL_L2_089: Budget with min/max bounds
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, MODIFIER]
answer_mode: VALUE
allowed_values: { integer allocation }
primary_trap: PARTIAL_COMPUTATION
```
Assign minimums, distribute the remainder. Example: ₹100K, 3 depts min ₹20K → ₹33,333 each.

## NUM_AL_L2_090: Capacity split
```yaml
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
primary_trap: PARTIAL_COMPUTATION
```
Split by priority or proportion. Example: 500/day, A 300 B 250 by proportion → A 272.

## NUM_AL_L3_091: Multi-constraint feasibility
```yaml
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: several constraints, only one combination satisfies all; binding constraint not obvious
primary_trap: IGNORED_CONSTRAINT
```
Pick the combination meeting budget/ROI/size constraints simultaneously.
Note: keep distinct from L3_093 — this asks for a feasible *combination/subset*, 093 asks to pick a single valid *option* from a table.

## NUM_AL_L3_092: Trade-off analysis
```yaml
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: weighted scoring across two competing metrics
primary_trap: PARTIAL_COMPUTATION (use one metric only)
```
Weighted score of two options on two metrics; pick the winner.

## NUM_AL_L3_093: Pick valid option
```yaml
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: filter four concrete options against three constraints; exactly one survives
primary_trap: IGNORED_CONSTRAINT
```
Each option has several attributes; eliminate by each constraint; exactly one valid.
Note: distinct from L3_091 — this is single-option selection from a table, not subset feasibility.

## NUM_AL_L3_094: Lever analysis
```yaml
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: COMPARISON
difficulty_source: compute each lever's impact on the target, pick the strongest
primary_trap: WRONG_METHOD (confuse a margin lever with a revenue lever)
```
Several levers each affecting one metric; identify which most improves the target. Example: +10% price beats +5% volume beats a cost cut for revenue.

---

# Closing Notes

## Domains capped below L3
- **L (Number Series)** and **R (Estimation)** have no genuine L3. Do not synthesize one by bolting on a constraint or an options-framing.

## Domains left unchanged because already well-built
- **Q (Data Interpretation)** and **S (Resource Allocation)** were already structured around genuine binding constraints.

## The two failure modes this contract is designed to prevent
1. **Synthetic difficulty** — a non-binding constraint inflating an L2 into a fake L3. Caught by the strip test in the global rules.
2. **Dirty answers** — parameters chosen to look plausible rather than divide cleanly, producing an answer that matches no option. Caught by the clean-answer rule (generate the divisor first, choose the free parameter as a multiple of it) and by the mandatory recompute-and-match self-check.

Together with the computational validation tier (recompute the answer from the tree, confirm option uniqueness and answer-type sanity in code before any LLM judgement), these rules keep generated questions both correctly levelled and correctly answered.
