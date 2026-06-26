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
| L2 | Depth 2–3. At least one `OPERATION` combining two sub-results, or a short chain of dependent operations. No `CONSTRAINT` at the root. May contain a single `MODIFIER` only where the template explicitly allows it. |
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

At least one wrong option must encode the **most common misconception** for that template (named in the contract's `primary_trap`). At least two wrong options must be plausible to a student who partially understood the question.

---

# Domain A: Ratios & Proportions

## Domain Purpose

Test whether the student can split a quantity by a given ratio, recover an unknown quantity from a ratio relationship, and reason across two ratio states that are linked by a change.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `RATIO_SPLIT` | Divide a total into parts according to a ratio |
| `RATIO_SCALE` | Scale from one known part to another using the ratio |
| `RATIO_CHAIN` | Combine A:B and B:C by equalizing the common term |
| `TIME_WEIGHTING` | Weight each share by the duration it was held |
| `TWO_STATE_SOLVE` | Build equations from a before-state and an after-state and solve simultaneously |
| `REVERSE_FROM_FINAL` | Work backwards from a final ratio to an unknown change |

## Domain-Wide Rules

- The sum of the ratio parts must divide the total exactly; never ship a non-integer share.
- For two-state and replacement problems, choose the free parameter so the unknown is a positive integer.
- Ratios in answers are always reduced to lowest terms.
- Difficulty must come from the relationship between states, not from larger numbers.
- Do not state the total when the template is a scaling template, and do not state a part when the template is a splitting template; the missing piece is what makes the question.

## Domain Option Rules

Ratio distractors must come from plausible ratio mistakes:

- `SCALE_ERROR`: use the wrong part of the ratio, or invert it.
- `REVERSE_DIRECTION`: scale from the wrong known quantity.
- `WRONG_METHOD`: multiply two ratios without equalizing the common term.
- `PARTIAL_COMPUTATION`: find the unit value but forget to multiply back to the asked share.
- `ARITHMETIC_SLIP`: correct setup, one calculation error.

For two-state templates, at least one distractor must be the value obtained by applying the change to only one side, and at least one must be the answer from using the original ratio after it has changed.

---

## NUM_RP_L1_001: Compute Part From Ratio and Total

```yaml
domain: Ratios & Proportions
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - RATIO_SPLIT
allowed_values:
    ratio_parts: 2-9
    total: divisible by (a+b)
    total_max: 500
primary_trap: SCALE_ERROR
```

### Contract

Generate a question that gives a two-term ratio and a total, and asks for one of the two parts. The answer is a single application of `part = total × a/(a+b)`.

### Allowed Variations

- either part may be the one asked for
- any everyday splitting context (mixtures, money split, group composition)
- the ratio may be presented as `a:b` or in words

### Forbidden

- any cap, floor, or feasibility condition
- a total not divisible by the sum of parts
- a non-integer answer
- giving one of the parts instead of the total

### Validator Must Check

- the total is divisible by `(a+b)`
- the computed part is an integer and equals the correct option
- exactly one distractor uses the other part of the ratio
- no distractor equals the correct value

### Example Skeleton

```text
Cement and sand are mixed in the ratio 3:5. The total mixture is 240 kg.
Question: How much cement is there?
Answer: 90
```

---

## NUM_RP_L1_002: Ratio Scaling From a Known Part

```yaml
domain: Ratios & Proportions
difficulty_level: L1
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
required_operators:
    - RATIO_SCALE
allowed_values:
    ratio_parts: 2-9
    known_part: divisible by its ratio component
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question that gives a ratio and one actual quantity (not the total), and asks for the other quantity. The student finds the scale factor from the known part and applies it to the other.

### Allowed Variations

- either side may be the known quantity
- comparison contexts (boys/girls, two investments, two lengths)

### Forbidden

- giving the total
- a non-integer scale factor
- a non-integer answer

### Validator Must Check

- the known part is divisible by its ratio component so the scale factor is exact
- the answer is an integer and equals the correct option
- one distractor inverts the ratio direction

### Example Skeleton

```text
The ratio of boys to girls in a class is 4:3. There are 28 boys.
Question: How many girls are there?
Answer: 21
```

---

## NUM_RP_L2_003: Chain Two Ratios

```yaml
domain: Ratios & Proportions
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - RATIO_CHAIN
    - RATIO_SCALE
allowed_values:
    parts: 2-12
    common_term_requires_LCM: true
primary_trap: WRONG_METHOD
```

### Contract

Generate two linked ratios `A:B` and `B:C` where the common term B has different values. The student must equalize B, derive `A:C`, and then find an actual value from a given quantity.

### Allowed Variations

- ask for A given C, or C given A
- three-entity contexts (three quantities, three people)

### Forbidden

- B already equal in both ratios (removes the equalization step)
- a non-integer final answer
- more than three linked entities

### Validator Must Check

- the common term is equalized via its LCM before deriving A:C
- the final answer is an integer and equals the correct option
- one distractor multiplies the ratios directly without equalizing

### Example Skeleton

```text
A:B = 2:3 and B:C = 4:5. C = 60.
Question: What is A?
Answer: 32
```

---

## NUM_RP_L2_004: Split Total Into Three or More Parts

```yaml
domain: Ratios & Proportions
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - RATIO_SPLIT
allowed_values:
    parts: 3 parts summing to ≤ 20
    total: divisible by part-sum, 100-2000
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a three-part (or more) ratio and a total, and ask for one specified share. The student computes the unit value, then the asked share.

### Allowed Variations

- ask for the largest, smallest, or a named share
- 3 or 4 parts

### Forbidden

- a total not divisible by the part-sum
- a non-integer share
- asking for the total (that is L1)

### Validator Must Check

- total divisible by the sum of parts
- all shares are integers and sum to the total
- one distractor reports the unit value instead of the asked share

### Example Skeleton

```text
₹720 is divided among A, B and C in the ratio 2:3:4.
Question: How much does B get?
Answer: 240
```

---

## NUM_RP_L3_005: Ratio Change Over Time

```yaml
domain: Ratios & Proportions
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - TWO_STATE_SOLVE
allowed_values:
    ratio_parts: 2-6
    time_gap: 3-10
    answer: positive integer
difficulty_source: two ratio states linked by a fixed change require simultaneous equations
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question with a ratio now and a different ratio after a fixed change applied to both quantities (e.g. years added to two ages). The student sets the current quantities as multiples of the present ratio, writes one equation from the future state, and solves.

### Allowed Variations

- ages, populations, or any two quantities changing by the same added amount
- ask for either current quantity or their sum
- the change may be an increase or a decrease

### Forbidden

- a change applied to only one quantity (that is not this template)
- parameters giving a non-integer or negative solution
- a degenerate pair of ratios that makes the equation trivial

### Validator Must Check

- both ratio states appear in the computation
- the solution is a unique positive integer
- the recomputed answer equals the correct option
- one distractor applies the change to only one side; one uses the original ratio after the change

### Example Skeleton

```text
A's age to B's age is 3:5. In 6 years the ratio will be 3:4.
Question: What is A's current age?
Answer: 6
```

---

## NUM_RP_L3_006: Investment Ratio With Mid-Period Change

```yaml
domain: Ratios & Proportions
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - TIME_WEIGHTING
    - RATIO_SPLIT
allowed_values:
    initial_parts: 1-5
    change_month: 3, 4, or 6
    multiplier: 2 or 3
    profit: divisible by total capital-months
difficulty_source: time-weighted (capital-month) ratio differs from the stated ratio
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where partners invest by a stated ratio, one partner changes their capital partway through the year, and a year-end profit is split. The student computes capital-months for each partner, derives the effective ratio, and splits the profit.

### Allowed Variations

- two or three partners
- the change may be a doubling, tripling, or partial withdrawal
- ask for any partner's share

### Forbidden

- profit not divisible by the sum of capital-months (this is the canonical clean-answer failure)
- a non-integer share
- a change time that does not divide the year cleanly into the stated months

### Validator Must Check

- capital-months are computed per partner
- the profit is an exact multiple of the sum of capital-months
- every share is an integer and the recomputed asked share equals the correct option
- one distractor splits the profit by the stated ratio, ignoring time

### Example Skeleton

```text
A, B and C invest in the ratio 2:3:5. After 6 months A doubles his investment.
The year-end profit is ₹66,000.
Question: What is A's share?
Answer: ₹18,000   (weights 36:36:60, sum 132; 66000 × 36/132)
```

---

## NUM_RP_L3_007: Reverse Ratio With Replacement

```yaml
domain: Ratios & Proportions
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - REVERSE_FROM_FINAL
allowed_values:
    initial_ratio: {3:1, 4:1, 5:1, 3:2}
    total_volume: 20-60
    removed: positive integer
difficulty_source: solve backwards from a final ratio for an unknown removed amount
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question with a known initial ratio in a known total volume, where some mixture is removed and replaced with one component (usually water), producing a known final ratio. The student lets the removed amount be unknown, notes that removal reduces both components proportionally, and solves from the final-ratio condition.

### Allowed Variations

- milk/water, acid/water, or any two-component mixture
- removal-and-replace with water, or with one pure component

### Forbidden

- removal that affects only one component
- parameters giving a non-integer removed amount
- a final ratio not achievable from the initial one

### Validator Must Check

- the removed amount reduces both components in the original proportion
- the equation is built from the final-ratio condition
- the answer is a positive integer equal to the correct option
- one distractor removes the unknown from one component only

### Example Skeleton

```text
A 30-litre vessel contains milk and water in the ratio 4:1. Some mixture is removed
and replaced with water, making the ratio 2:3.
Question: How much mixture was removed?
Answer: 15
```

---

# Domain B: Percentages & Growth

## Domain Purpose

Test percentage computation, reverse percentage, and reasoning about successive or multi-variable percentage changes where the naive additive approach fails.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `PERCENT_OF` | Compute a percentage of a base |
| `PERCENT_CHANGE` | Compute the percentage change between two values |
| `REVERSE_PERCENT` | Recover the original from a changed value |
| `WEIGHTED_PERCENT` | Combine percentages weighted by group size |
| `SUCCESSIVE_CHANGE` | Apply changes to a running value, not the original |
| `MULTI_VARIABLE_BACKSOLVE` | Recover a base from percentages-of-percentages and an absolute figure |

## Domain-Wide Rules

- Successive changes always apply to the running value, never repeatedly to the original.
- Reverse problems must yield an integer original within the stated bounds.
- Percentages combine multiplicatively, not additively.
- Difficulty comes from chaining and back-solving, not from larger bases.

## Domain Option Rules

Percentage distractors must come from the classic percentage errors:

- `ADDITIVE_PERCENT`: sum successive changes instead of compounding them.
- `SCALE_ERROR`: divide by the new value instead of the original, or misplace a decimal.
- `WRONG_METHOD`: subtract a percentage of the result instead of dividing in reverse problems.
- `SUBGROUP_AVERAGE`: average two percentages instead of weighting them.
- `PARTIAL_COMPUTATION`: stop at an intermediate base in a back-solve.

For successive-change templates, at least one distractor must be the additive answer. For back-solve templates, at least one distractor must be the intermediate value reached before the final division.

---

## NUM_PC_L1_007: Percent of a Number

```yaml
domain: Percentages & Growth
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - PERCENT_OF
allowed_values:
    base: 100-1000
    p: {5, 10, 15, 20, 25, 30}
    result: integer
primary_trap: SCALE_ERROR
```

### Contract

Generate a question asking for a simple percentage of a base. The answer is `base × p/100`.

### Allowed Variations

- any context with a quantity and a percentage (discount amount, tax amount, share)
- the percentage may be stated in words or symbol

### Forbidden

- a percentage producing a non-integer result
- any second step or change
- reverse phrasing

### Validator Must Check

- the result is an integer equal to the correct option
- one distractor misplaces a decimal (×10 or ÷10 of the answer)

### Example Skeleton

```text
What is 15% of 480?
Answer: 72
```

---

## NUM_PC_L1_008: Percent Change

```yaml
domain: Percentages & Growth
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - PERCENT_CHANGE
allowed_values:
    original: 50-500
    new: 60-600
    change: whole-number %
primary_trap: SCALE_ERROR
```

### Contract

Generate a question giving an original and a new value, asking for the percentage increase or decrease. The answer is `(new − original)/original × 100`.

### Allowed Variations

- increase or decrease
- price, salary, population, score contexts

### Forbidden

- a change that is not a whole-number percentage
- dividing by the new value as the intended method

### Validator Must Check

- the change is a whole-number percentage equal to the correct option
- one distractor divides by the new value instead of the original

### Example Skeleton

```text
A price rose from ₹200 to ₹250.
Question: What is the percentage increase?
Answer: 25%
```

---

## NUM_PC_L2_009: Reverse Percentage

```yaml
domain: Percentages & Growth
difficulty_level: L2
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
required_operators:
    - REVERSE_PERCENT
allowed_values:
    result: 100-2000
    p: {10, 15, 20, 25}
    original: integer
primary_trap: WRONG_METHOD
```

### Contract

Generate a question giving a value after a percentage change and asking for the original. The student divides by `(1 ± p/100)`.

### Allowed Variations

- after an increase or after a discount
- price, population, salary contexts

### Forbidden

- an original that is not an integer
- a result that equals the original (no change)

### Validator Must Check

- the original is an integer equal to the correct option
- one distractor subtracts `p%` of the result instead of dividing

### Example Skeleton

```text
After a 20% increase, a value is 960.
Question: What was the original value?
Answer: 800
```

---

## NUM_PC_L2_010: Weighted Percentage Across Groups

```yaml
domain: Percentages & Growth
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - WEIGHTED_PERCENT
allowed_values:
    p: 10-50
    n: 10-100
    result: at most 1 decimal place
primary_trap: SUBGROUP_AVERAGE
```

### Contract

Generate a question with two groups, each with a size and a percentage, asking for the combined percentage. The student weights each percentage by its group size.

### Allowed Variations

- two or three groups
- pass rates, quality rates, attendance contexts

### Forbidden

- equal group sizes (this collapses to a simple average and removes the trap)
- a result needing more than one decimal place

### Validator Must Check

- the combined value is weighted by group size and equals the correct option
- one distractor is the plain average of the two percentages

### Example Skeleton

```text
Group A has 40 students averaging 70%. Group B has 60 students averaging 80%.
Question: What is the overall average?
Answer: 76%
```

---

## NUM_PC_L3_011: Successive Percentage Changes

```yaml
domain: Percentages & Growth
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - SUCCESSIVE_CHANGE
allowed_values:
    changes: 2-3 from ±{10, 15, 20, 25, 30}
    net: non-trivial (not zero, not a round additive value)
difficulty_source: changes compound on a running base, not the original
primary_trap: ADDITIVE_PERCENT
```

### Contract

Generate a question applying two or three successive percentage changes and asking for the net single percentage change from the original. The student applies each change to the running value from a base of 100.

### Allowed Variations

- any mix of increases and decreases
- price, value, population contexts

### Forbidden

- changes that happen to sum to the multiplicative answer (removes the trap)
- a net change that is a round additive number

### Validator Must Check

- changes are applied to the running value, not the original
- the net change equals the correct option
- one distractor is the additive sum of the changes

### Example Skeleton

```text
A price is increased by 20%, then decreased by 20%, then increased by 25%.
Question: What is the net single percentage change from the original?
Answer: +20%
```

---

## NUM_PC_L3_012: Reverse-Engineer Original From a Multi-Variable Outcome

```yaml
domain: Percentages & Growth
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - MULTI_VARIABLE_BACKSOLVE
allowed_values:
    turnout: {70, 75, 80, 85}
    gap_percent: {10, 12, 15, 20}
    margin: divisible by gap_percent
difficulty_source: two unknowns resolved sequentially backwards from an absolute margin
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where percentages are taken of percentages and a single absolute figure (a margin, a count) is given. The student works backwards: from the margin to the intermediate total, then from that to the base.

### Allowed Variations

- elections, surveys, attendance with valid/invalid or abstaining portions
- ask for the base (registered total, membership)

### Forbidden

- a margin not divisible by the percentage gap (clean-answer failure)
- a turnout that does not divide the intermediate evenly

### Validator Must Check

- the margin yields an integer intermediate total
- the intermediate yields an integer base equal to the correct option
- one distractor stops at the intermediate total

### Example Skeleton

```text
80% of registered voters voted. Candidate A got 55%, B got 40%, the rest were invalid.
A won by 3,600 votes.
Question: How many voters were registered?
Answer: 30,000
```

---

## NUM_PC_L3_013: Successive Discounts and Profit

```yaml
domain: Percentages & Growth
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - SUCCESSIVE_CHANGE
allowed_values:
    markup: {30, 35, 40, 45, 50}
    discounts: two of {10, 12, 15, 20}
    result: non-zero profit or loss
difficulty_source: markup then two multiplicative discounts, profit measured on cost
primary_trap: ADDITIVE_PERCENT
```

### Contract

Generate a question where a cost is marked up, then two successive discounts are applied to the running price, and the student must find the resulting profit or loss percentage on cost.

### Allowed Variations

- profit or loss outcome
- retail, wholesale contexts

### Forbidden

- discounts that sum to a clean equivalent (removes the trap)
- an exact 0% result
- measuring profit on the marked price instead of cost

### Validator Must Check

- discounts are applied successively to the running price
- profit/loss is measured on cost and equals the correct option
- one distractor treats the two discounts as additive

### Example Skeleton

```text
A shopkeeper marks goods 40% above cost, then gives successive discounts of 10% and 15%.
Question: What is the profit or loss percentage?
Answer: +7.1% profit
```

---

# Domain C: Profit / Loss / Discount

## Domain Purpose

Test cost-price relationships, discounting, and multi-party or weighted transactions where profit must be measured against the correct base.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `PROFIT_LOSS_PERCENT` | Compute profit/loss percentage on cost |
| `DISCOUNT_APPLY` | Apply a discount to a marked price |
| `MARKUP_DISCOUNT_STACK` | Mark up then discount, measure profit on cost |
| `OFFER_COMPARE` | Compute effective prices of two offers and compare |
| `EQUAL_SP_PAIR` | Two items at equal selling price, opposite percentage outcomes |
| `TRANSACTION_CHAIN` | Resolve a chain of sales backwards to an original cost |
| `FALSE_WEIGHT` | Combine a weight-based gain with a price markup |

## Domain-Wide Rules

- Profit and loss are measured on cost price unless explicitly stated otherwise.
- Chain transactions resolve backwards from the last known price.
- Equal selling prices with opposite percentages never net to zero, because the cost bases differ.
- Difficulty comes from the base of measurement and the direction of resolution.

## Domain Option Rules

Profit/loss distractors must come from base and direction errors:

- `SCALE_ERROR`: measure profit on selling price instead of cost.
- `ADDITIVE_PERCENT`: combine markup and discount, or two margins, additively.
- `WRONG_METHOD`: assume equal-SP opposite percentages cancel.
- `PARTIAL_COMPUTATION`: count only one gain source in a false-weight problem.
- `REVERSE_DIRECTION`: resolve a transaction chain forwards instead of backwards.

For the equal-SP template, one distractor must be "no profit/loss." For the chain template, one distractor must combine the two margins directly.

---

## NUM_PL_L1_013: Profit or Loss Percentage

```yaml
domain: Profit / Loss / Discount
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - PROFIT_LOSS_PERCENT
allowed_values:
    CP: 100-500
    SP: 80-700
    result: whole-number %
primary_trap: SCALE_ERROR
```

### Contract

Generate a question giving cost and selling price, asking for profit or loss percentage on cost.

### Allowed Variations

- profit or loss
- any buy/sell context

### Forbidden

- a result that is not a whole-number percentage
- measuring on selling price as the intended method

### Validator Must Check

- the percentage is measured on cost and equals the correct option
- one distractor measures on selling price

### Example Skeleton

```text
A trader buys for ₹400 and sells for ₹500.
Question: What is the profit percentage?
Answer: 25%
```

---

## NUM_PL_L1_014: Discount Price

```yaml
domain: Profit / Loss / Discount
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - DISCOUNT_APPLY
allowed_values:
    MRP: 100-1000
    d: {5, 10, 15, 20, 25}
    SP: integer
primary_trap: ARITHMETIC_SLIP
```

### Contract

Generate a question giving a marked price and a single discount, asking for the selling price.

### Allowed Variations

- any retail context
- discount stated as a percentage

### Forbidden

- a non-integer selling price
- a second discount

### Validator Must Check

- the selling price is an integer equal to the correct option
- one distractor subtracts the discount percentage as an absolute amount

### Example Skeleton

```text
The marked price of a shirt is ₹600 and a 15% discount is offered.
Question: What is the selling price?
Answer: ₹510
```

---

## NUM_PL_L2_015: Markup Then Discount

```yaml
domain: Profit / Loss / Discount
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - MARKUP_DISCOUNT_STACK
allowed_values:
    CP: 200-800
    markup: {20, 25, 30, 40, 50}
    discount: {10, 15, 20}
primary_trap: ADDITIVE_PERCENT
```

### Contract

Generate a question where a cost is marked up to a marked price, a discount is applied to reach a selling price, and the profit percentage on cost is asked.

### Allowed Variations

- profit or small loss
- retail contexts

### Forbidden

- markup and discount that net to a round additive figure
- measuring profit on the marked price

### Validator Must Check

- marked price then selling price computed in order
- profit measured on cost equals the correct option
- one distractor treats markup minus discount as the profit

### Example Skeleton

```text
A jacket costs ₹500, is marked up 40%, then given a 25% discount.
Question: What is the profit percentage?
Answer: 5%
```

---

## NUM_PL_L2_016: Compare Two Offers

```yaml
domain: Profit / Loss / Discount
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: COMPARISON
required_operators:
    - OFFER_COMPARE
allowed_values:
    both effective prices integer
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate two purchase offers with different structures (different base price and discount, or a bundle deal) and ask which is cheaper. The student computes both effective prices and compares.

### Allowed Variations

- percentage discount vs bundle offer
- two different discount structures

### Forbidden

- offers where the headline number alone gives the answer
- a tie unless explicitly intended

### Validator Must Check

- both effective prices are computed and compared
- the cheaper offer is identified correctly
- one distractor compares headline prices without computing effective prices

### Example Skeleton

```text
Offer A: ₹1,000 with a 20% discount. Offer B: ₹1,100 with a 30% discount.
Question: Which is cheaper?
Answer: Offer B at ₹770
```

---

## NUM_PL_L2_017: Same Selling Price, One Profit One Loss

```yaml
domain: Profit / Loss / Discount
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - EQUAL_SP_PAIR
allowed_values:
    SP: equal for both items
    percent: ±{10, 20}
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where two items are sold at the same selling price, one at a profit and one at an equal-magnitude loss, and ask for the net result. The cost bases differ, so there is always a net loss.

### Allowed Variations

- any pair of items
- 10% or 20% magnitude

### Forbidden

- different selling prices
- presenting the answer as no net loss

### Validator Must Check

- both cost prices are computed from the common selling price
- the net result equals the correct option (always a loss)
- one distractor is "no profit or loss"

### Example Skeleton

```text
Two items are sold at ₹1,200 each — one at a 20% profit, one at a 20% loss.
Question: What is the net result?
Answer: Loss of ₹100
```

---

## NUM_PL_L3_017: Chain of Transactions

```yaml
domain: Profit / Loss / Discount
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - TRANSACTION_CHAIN
allowed_values:
    margins: ±{15, 20, 25}
    final_price: divides cleanly back through each margin
difficulty_source: work backwards through two successive margins
primary_trap: ADDITIVE_PERCENT
```

### Contract

Generate a question with a chain of sales (A to B to C) at stated margins, with the final buyer's price known, asking for the original cost. The student divides back through each margin.

### Allowed Variations

- two or three links
- mix of profit and loss margins

### Forbidden

- a final price that does not divide cleanly back to an integer original
- combining the margins directly as the intended method

### Validator Must Check

- each back-division is exact
- the original cost is an integer equal to the correct option
- one distractor combines the two margins additively

### Example Skeleton

```text
A sells to B at 20% profit. B sells to C at 15% profit. C pays ₹2,760.
Question: What did A pay originally?
Answer: ₹2,000
```

---

## NUM_PL_L3_018: False Weight With Markup

```yaml
domain: Profit / Loss / Discount
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - FALSE_WEIGHT
allowed_values:
    false_weight: {800, 900} g per 1000 g
    markup: {5, 10}
difficulty_source: two gain sources compound multiplicatively
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where a trader uses a false weight and also marks up the price, asking for the actual profit percentage. The student combines the weight gain `(1000/false − 1)` with the markup multiplicatively.

### Allowed Variations

- different false weights and markups
- grocery, fabric, metal contexts

### Forbidden

- counting only one source of gain
- a false weight that gives a non-terminating gain

### Validator Must Check

- the weight gain and markup are combined multiplicatively
- the actual profit equals the correct option
- one distractor counts only the markup, one only the weight gain

### Example Skeleton

```text
A trader uses a 900 g weight instead of 1 kg and marks up the price by 10%.
Question: What is the actual profit percentage?
Answer: 22.2%
```

---

# Domain D: Averages & Weighted Mean

## Domain Purpose

Test means, weighted means, and problems that can only be solved by reasoning with totals rather than averages.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `SIMPLE_MEAN` | Average of a set of values |
| `WEIGHTED_MEAN` | Average weighted by counts |
| `ITEM_REPLACE` | Recompute an average after replacing a value |
| `REVERSE_MEAN` | Find a missing value given the target average |
| `OVERLAP_SUBGROUP` | Track multiple subgroup totals within a whole |
| `AVERAGE_SHIFT` | Use totals to find a subgroup average from a change in overall average |
| `UNKNOWN_GROUP_SIZE` | Solve for a group size from a combined average |

## Domain-Wide Rules

- Convert every average to a total before manipulating it.
- Never average two averages unless the groups are equal in size.
- Difficulty comes from working with totals where the average is misleading.

## Domain Option Rules

Average distractors must come from total/average confusion:

- `SUBGROUP_AVERAGE`: average the averages.
- `WRONG_METHOD`: subtract averages directly instead of using totals.
- `PARTIAL_COMPUTATION`: forget to include or exclude a value when adjusting the total.
- `REVERSE_DIRECTION`: solve for the wrong quantity.

For the batting-average and unknown-group templates, one distractor must come from manipulating averages directly rather than totals.

---

## NUM_AV_L1_019: Simple Average

```yaml
domain: Averages & Weighted Mean
difficulty_level: L1
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - SIMPLE_MEAN
allowed_values:
    count: 3-5 values
    values: 10-100
    result: clean
primary_trap: ARITHMETIC_SLIP
```

### Contract

Generate a question asking for the average of a small set of values, or for a missing value given the average.

### Allowed Variations

- average of given values, or one missing value given the average

### Forbidden

- weights
- a non-terminating result

### Validator Must Check

- the sum and division are correct and the result equals the correct option

### Example Skeleton

```text
Find the average of 45, 60, 75 and 80.
Answer: 65
```

---

## NUM_AV_L2_020: Weighted Average

```yaml
domain: Averages & Weighted Mean
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - WEIGHTED_MEAN
allowed_values:
    pairs: 2-3 value-weight pairs
    result: at most 1 decimal
primary_trap: SUBGROUP_AVERAGE
```

### Contract

Generate a question with values and unequal weights, asking for the weighted average.

### Allowed Variations

- scores with credit weights, prices with quantities

### Forbidden

- equal weights (removes the trap)
- a result needing more than one decimal

### Validator Must Check

- weights are applied and the result equals the correct option
- one distractor is the unweighted average

### Example Skeleton

```text
A student scores 70 in Maths (weight 3) and 80 in English (weight 2).
Question: What is the weighted average?
Answer: 74
```

---

## NUM_AV_L2_021: Replace One Item

```yaml
domain: Averages & Weighted Mean
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - ITEM_REPLACE
allowed_values:
    avg: 30-80
    n: 4-10
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where one value in a set is replaced (or removed) and the new average is asked. The student adjusts the total.

### Allowed Variations

- replace a value, or remove a value

### Forbidden

- a non-integer new average unless intended
- forgetting to adjust the count when removing

### Validator Must Check

- the total is adjusted correctly and the new average equals the correct option

### Example Skeleton

```text
The average of 5 numbers is 60. The number 40 is replaced by 80.
Question: What is the new average?
Answer: 68
```

---

## NUM_AV_L2_022: Reverse Average (Missing Value)

```yaml
domain: Averages & Weighted Mean
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - REVERSE_MEAN
allowed_values:
    target_avg: 50-90
    n: 4-6
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question giving several values and a target average over a larger count, asking for the value needed to reach the target. The student computes required total minus current total.

### Allowed Variations

- one more value to reach a target, test scores or measurements

### Forbidden

- a required value outside a sensible range
- a non-integer answer unless intended

### Validator Must Check

- required total minus current total equals the correct option
- one distractor is the target average itself

### Example Skeleton

```text
A student scored 55, 60, 70 and 65 in four tests.
Question: What score is needed in the fifth test to average 65?
Answer: 75
```

---

## NUM_AV_L2_023: Reverse Weighted Average

```yaml
domain: Averages & Weighted Mean
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - REVERSE_MEAN
    - WEIGHTED_MEAN
allowed_values:
    group_avgs: 40-90
    target: between the group averages
primary_trap: SUBGROUP_AVERAGE
```

### Contract

Generate a question giving two group averages and sizes and a target overall average, asking by how much one group's average must change. The student works from the required total.

### Allowed Variations

- raise or lower one group's average
- two groups of different sizes

### Forbidden

- a target outside the range of the two averages
- equal group sizes

### Validator Must Check

- the required change is computed from totals and equals the correct option
- one distractor averages the two group averages

### Example Skeleton

```text
Group X (5 people) averages 50. Group Y (5 people) averages 70.
Question: By how much must Group Y's average rise for the overall average to be 65?
Answer: 10
```

---

## NUM_AV_L3_022: Overlapping Subgroups

```yaml
domain: Averages & Weighted Mean
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - OVERLAP_SUBGROUP
difficulty_source: track three subgroup totals simultaneously within a whole
primary_trap: SUBGROUP_AVERAGE
```

### Contract

Generate a question giving the overall average and two overlapping subgroup averages, asking for the remaining group's average. The student works entirely with totals.

### Allowed Variations

- first-k and last-k subgroups within a sequence
- different group sizes

### Forbidden

- subgroups that do not leave a clean remaining group
- a non-integer remaining average unless intended

### Validator Must Check

- the overall total and subgroup totals are computed and the remaining average equals the correct option
- one distractor averages the subgroup averages

### Example Skeleton

```text
The average of 8 numbers is 20. The first 3 average 15 and the last 3 average 25.
Question: What is the average of the remaining 2?
Answer: 20
```

---

## NUM_AV_L3_023: Average Shift (Batting Average)

```yaml
domain: Averages & Weighted Mean
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - AVERAGE_SHIFT
difficulty_source: must use totals; subtracting averages gives the wrong answer
primary_trap: WRONG_METHOD
```

### Contract

Generate a question giving an average before and after some additional items, asking for the average over just the additional items. The student computes the two totals and subtracts.

### Allowed Variations

- average rising or falling
- innings, exams, monthly figures

### Forbidden

- subtracting the averages as the intended method
- parameters giving a non-integer subgroup average unless intended

### Validator Must Check

- totals before and after are computed and the subgroup average equals the correct option
- one distractor subtracts the two averages directly

### Example Skeleton

```text
A batsman's average after 20 innings is 48. After 5 more innings it drops to 45.
Question: What was the average in those 5 innings?
Answer: 33
```

---

## NUM_AV_L3_024: Unknown Group Size

```yaml
domain: Averages & Weighted Mean
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - UNKNOWN_GROUP_SIZE
allowed_values:
    sizes and averages chosen so the unknown count is a positive integer
difficulty_source: the group size is the unknown; set up and solve an equation
primary_trap: SUBGROUP_AVERAGE
```

### Contract

Generate a question giving an overall average, two subgroup averages, and one subgroup size, asking for the other subgroup size. The student sets the weighted-average equation equal to the overall average and solves for the unknown count.

### Allowed Variations

- managers/non-managers, boys/girls, two product lines

### Forbidden

- parameters giving a non-integer group size
- the overall average outside the range of the two subgroup averages

### Validator Must Check

- the equation is set up and solved for an integer group size equal to the correct option
- one distractor manipulates averages directly without solving for the count

### Example Skeleton

```text
The average salary of all employees is ₹600. Managers average ₹800 and non-managers ₹550.
There are 12 managers.
Question: How many non-managers are there?
Answer: 48
```

---

# Domain E: Mixtures & Allegations

## Domain Purpose

Test concentration mixing, replacement, and reverse or multi-source mixture problems.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `MIX_CONCENTRATION` | Combine two solutions into a final concentration |
| `ALLEGATION` | Find the mixing ratio for a target concentration |
| `SINGLE_REPLACE` | Remove a fraction and refill once |
| `MULTI_REPLACE` | Apply the replacement formula repeatedly |
| `EQUAL_MIX_FRACTION` | Combine equal amounts of several sources by fraction |
| `ADD_PURE` | Add a pure component to reach a target concentration |
| `REVERSE_MIX` | Recover source quantities from a known final mixture |

## Domain-Wide Rules

- Replacement multiplies the concentration by `(1 − fraction)` each step.
- Adding a pure substance changes the numerator and denominator together.
- Equal-amount mixing averages the component fractions.
- Difficulty comes from the structure of the change, not the size of the volumes.

## Domain Option Rules

Mixture distractors must come from concentration-handling errors:

- `SUBGROUP_AVERAGE`: average the concentrations without weighting by volume.
- `WRONG_METHOD`: subtract the fraction each step instead of multiplying; hold the denominator fixed when adding pure substance.
- `REVERSE_DIRECTION`: invert the allegation ratio.
- `PARTIAL_COMPUTATION`: set up only one of the two equations in a reverse mixture.

For the add-pure template, one distractor must hold the denominator fixed. For multi-step replacement, one distractor must subtract the fraction linearly.

---

## NUM_MA_L1_024: Final Concentration After Mixing

```yaml
domain: Mixtures & Allegations
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - MIX_CONCENTRATION
allowed_values:
    concentration: {20..80}%
    quantity: multiples of 10
    result: integer %
primary_trap: SUBGROUP_AVERAGE
```

### Contract

Generate a question mixing two solutions of known concentration and volume, asking for the final concentration.

### Allowed Variations

- acid, milk, alcohol contexts
- two solutions

### Forbidden

- equal volumes (collapses to a simple average)
- a non-integer result

### Validator Must Check

- the concentration is volume-weighted and equals the correct option
- one distractor averages the two concentrations

### Example Skeleton

```text
40 litres of 60% acid is mixed with 60 litres of 40% acid.
Question: What is the final concentration?
Answer: 48%
```

---

## NUM_MA_L2_025: Allegation Ratio

```yaml
domain: Mixtures & Allegations
difficulty_level: L2
tree_signature: [LEAF, FORMULA]
answer_mode: RATIO
required_operators:
    - ALLEGATION
allowed_values:
    c1 < target < c2
    ratio: small integers
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question asking in what ratio two solutions must be mixed to reach a target concentration. The student applies the allegation rule.

### Allowed Variations

- any two concentrations bracketing the target

### Forbidden

- a target outside the two concentrations
- a ratio that does not reduce to small integers

### Validator Must Check

- the ratio `(c2 − target):(target − c1)` is reduced and equals the correct option
- one distractor inverts the ratio

### Example Skeleton

```text
In what ratio must 20% and 60% solutions be mixed to get a 40% solution?
Answer: 1:1
```

---

## NUM_MA_L2_026: One-Step Replacement

```yaml
domain: Mixtures & Allegations
difficulty_level: L2
tree_signature: [LEAF, OPERATION, FORMULA]
answer_mode: VALUE
required_operators:
    - SINGLE_REPLACE
allowed_values:
    volume: 50-200
    drain_fraction: simple
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where a fraction of a solution is removed and replaced with water once, asking for the new concentration.

### Allowed Variations

- milk/water, concentrate/water

### Forbidden

- a non-terminating result
- multiple replacement steps

### Validator Must Check

- the remaining component is computed and the new concentration equals the correct option

### Example Skeleton

```text
A 100-litre tank has 80% milk. 25 litres is removed and replaced with water.
Question: What is the new concentration?
Answer: 60%
```

---

## NUM_MA_L2_027: Multi-Step Replacement

```yaml
domain: Mixtures & Allegations
difficulty_level: L2
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - MULTI_REPLACE
allowed_values:
    initial_c: {60, 70, 80}
    drain_fraction: {1/4, 1/5}
    steps: 2-4
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where a fixed fraction is removed and refilled with water several times, asking for the final concentration. The student applies `c × (1 − f)^n`.

### Allowed Variations

- 2 to 4 steps
- different drain fractions

### Forbidden

- a fraction or step count giving a non-terminating result
- a feasibility or cost condition (that would be synthetic)

### Validator Must Check

- the exponential replacement formula is applied and the result equals the correct option
- one distractor subtracts the fraction linearly each step

### Example Skeleton

```text
A tank has 80% acid. Each step, one quarter is drained and refilled with water. After 2 steps,
Question: what is the concentration?
Answer: 45%
```

---

## NUM_MA_L3_027: Three Sources, Equal Amounts

```yaml
domain: Mixtures & Allegations
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - EQUAL_MIX_FRACTION
difficulty_source: convert each ratio to a fraction and combine under equal-weight mixing
primary_trap: WRONG_METHOD
```

### Contract

Generate a question mixing equal amounts of two or three sources, each given as a component ratio, asking for the resulting fraction of one component. The student converts each ratio to a fraction and averages.

### Allowed Variations

- two or three alloys/solutions
- gold, copper, alcohol contexts

### Forbidden

- unequal amounts (that is a weighted mixture, a different shape)
- fractions whose average does not terminate to the stated precision

### Validator Must Check

- each ratio is converted to a fraction and the equal-weight average equals the correct option
- one distractor averages the ratios as written

### Example Skeleton

```text
Two alloys have copper fractions 3/5 and 5/8. Equal amounts are melted together.
Question: What fraction is copper?
Answer: 0.6125
```

---

## NUM_MA_L3_028: Add Pure Substance

```yaml
domain: Mixtures & Allegations
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - ADD_PURE
allowed_values:
    volume, start %, target %
    answer: integer litres
difficulty_source: adding a pure component changes numerator and denominator together
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where a quantity of a pure component is added to a solution to reach a target concentration, asking how much to add. The student solves `(start_amount + x)/(volume + x) = target`.

### Allowed Variations

- add pure acid, pure alcohol, pure water-removal framings

### Forbidden

- holding the denominator fixed as the intended method
- a non-integer amount to add

### Validator Must Check

- the equation updates both numerator and denominator and the answer equals the correct option
- one distractor holds the denominator fixed

### Example Skeleton

```text
A 40-litre solution is 30% acid.
Question: How much pure acid must be added to make it 50%?
Answer: 16 litres
```

---

## NUM_MA_L3_029: Reverse Mixture

```yaml
domain: Mixtures & Allegations
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - REVERSE_MIX
difficulty_source: two unknowns, two equations (total volume and concentration)
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question giving a final mixture's volume and concentration, formed from two solutions of known strength, asking how much of one source was used. The student sets up the volume and concentration equations and solves.

### Allowed Variations

- ask for either source quantity
- acid, alcohol contexts

### Forbidden

- parameters giving a non-integer source quantity
- using only one equation

### Validator Must Check

- both equations are used and the source quantity equals the correct option
- one distractor uses only the concentration equation

### Example Skeleton

```text
A 60-litre mixture is 40% alcohol, made by mixing a 25% solution with a 70% solution.
Question: How much of the 25% solution was used?
Answer: 40 litres
```

---

# Domain F: Simple & Compound Interest

## Domain Purpose

Test interest computation and the structural problems interest enables: solving for unknowns, comparing plans, doubling time, and the CI−SI difference.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `SIMPLE_INTEREST` | Compute SI = P·R·T/100 |
| `COMPOUND_INTEREST` | Compute A = P(1+R/100)^T, CI = A − P |
| `SI_UNKNOWN` | Rearrange the SI formula for P, R, or T |
| `CI_FREQUENCY` | Apply compounding more than once a year |
| `PLAN_COMPARE` | Compute two amounts and compare |
| `DOUBLING_TIME` | Use the rate implied by a doubling to find another multiple's time |
| `CI_SI_DIFFERENCE` | Use difference = P(R/100)² for two years |

## Domain-Wide Rules

- Simple interest is linear; compound interest is multiplicative. Keep the distinction sharp.
- Answers terminate cleanly; choose P, R, T so amounts are exact.
- Difficulty comes from the structural relation (doubling, difference), not from longer time periods.

## Domain Option Rules

Interest distractors must come from the SI/CI confusion and rate errors:

- `WRONG_METHOD`: use SI where CI is required, or vice versa.
- `SCALE_ERROR`: forget to divide the rate by the compounding frequency.
- `REVERSE_DIRECTION`: solve for the wrong variable.
- `ARITHMETIC_SLIP`: correct method, calculation error.

For the doubling and difference templates, one distractor must come from treating the relationship additively or computing SI and CI separately with an error.

---

## NUM_SI_L1_029: Simple Interest

```yaml
domain: Simple & Compound Interest
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - SIMPLE_INTEREST
allowed_values:
    P: 500-5000 in steps of 500
    R: {5, 8, 10, 12, 15}
    T: 1-5 years
    SI: integer
primary_trap: SCALE_ERROR
```

### Contract

Generate a question giving principal, rate and time, asking for simple interest (or the total amount).

### Allowed Variations

- ask for interest or total amount
- loan, deposit, investment contexts

### Forbidden

- compounding
- a non-integer interest

### Validator Must Check

- SI = P·R·T/100 is an integer equal to the correct option
- one distractor misplaces the ÷100

### Example Skeleton

```text
Find the simple interest on ₹2,000 at 10% per annum for 3 years.
Answer: ₹600
```

---

## NUM_CI_L1_031: Compound Interest

```yaml
domain: Simple & Compound Interest
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - COMPOUND_INTEREST
allowed_values:
    P: 1000-5000
    R: {5, 8, 10}
    T: 2-3 years
    A: integer
primary_trap: WRONG_METHOD
```

### Contract

Generate a question giving principal, rate and time, asking for compound interest over 2–3 years compounded annually.

### Allowed Variations

- ask for interest or amount
- 2 or 3 years

### Forbidden

- a non-integer amount
- compounding frequency other than annual (that is L2)

### Validator Must Check

- A = P(1+R/100)^T computed, CI = A − P equals the correct option
- one distractor computes simple interest

### Example Skeleton

```text
Find the compound interest on ₹1,000 at 10% per annum for 2 years.
Answer: ₹210
```

---

## NUM_SI_L2_030: Simple Interest With an Unknown

```yaml
domain: Simple & Compound Interest
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - SI_UNKNOWN
allowed_values:
    unknown: integer
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question giving the simple interest and two of P, R, T, asking for the third. The student rearranges the formula.

### Allowed Variations

- solve for principal, rate, or time

### Forbidden

- a non-integer unknown
- compounding

### Validator Must Check

- the rearranged formula gives an integer equal to the correct option
- one distractor solves for a different variable

### Example Skeleton

```text
The simple interest is ₹900 at 10% per annum over 3 years.
Question: What is the principal?
Answer: ₹3,000
```

---

## NUM_CI_L2_032: Compound Interest With Frequency

```yaml
domain: Simple & Compound Interest
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - CI_FREQUENCY
allowed_values:
    n: {2, 4}
    A: integer
primary_trap: SCALE_ERROR
```

### Contract

Generate a question with compounding more than once a year (half-yearly or quarterly), asking for the compound interest. The student adjusts the rate and the number of periods.

### Allowed Variations

- half-yearly or quarterly
- 1 or 2 years

### Forbidden

- a non-integer amount
- forgetting to adjust both rate and periods

### Validator Must Check

- rate divided by frequency and periods multiplied; CI equals the correct option
- one distractor forgets to divide the rate

### Example Skeleton

```text
Find the compound interest on ₹4,000 at 10% per annum compounded half-yearly for 1 year.
Answer: ₹410
```

---

## NUM_CI_L2_033: Compare Two Plans

```yaml
domain: Simple & Compound Interest
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: COMPARISON
required_operators:
    - PLAN_COMPARE
allowed_values:
    both amounts integer
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate two investment plans with different principals and rates, asking which yields more after a fixed time. The student computes both amounts and compares.

### Allowed Variations

- both compound, or one simple one compound
- ask which is larger and by how much

### Forbidden

- comparing principals instead of final amounts
- a tie unless intended

### Validator Must Check

- both final amounts computed and compared correctly
- one distractor compares the principals

### Example Skeleton

```text
Plan A: ₹10,000 at 8% compound interest. Plan B: ₹9,500 at 10% compound interest.
Question: Which yields more after 2 years?
Answer: Plan A
```

---

## NUM_SI_L3_034: Doubling / Tripling Time

```yaml
domain: Simple & Compound Interest
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - DOUBLING_TIME
difficulty_source: derive the rate from a doubling, then reuse it for a different multiple
primary_trap: WRONG_METHOD
```

### Contract

Generate a question stating that a sum doubles (or triples) in a given time at simple interest, asking the time to reach a different multiple. The student finds that doubling means interest equals principal over that time, derives the rate, and solves for the new time.

### Allowed Variations

- doubles then triples, triples then quintuples

### Forbidden

- compounding (the linear logic only holds for SI)
- parameters giving a non-integer time

### Validator Must Check

- the rate is derived from the stated multiple and reused
- the new time is an integer equal to the correct option
- one distractor scales the time by the multiple ratio directly

### Example Skeleton

```text
A sum doubles itself in 8 years at simple interest.
Question: In how many years will it triple?
Answer: 16
```

---

## NUM_CI_L3_035: CI − SI Difference

```yaml
domain: Simple & Compound Interest
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - CI_SI_DIFFERENCE
allowed_values:
    period: 2 years
    R: {5, 10}
    P: integer
difficulty_source: use the closed form difference = P(R/100)² to solve backwards
primary_trap: WRONG_METHOD
```

### Contract

Generate a question giving the difference between compound and simple interest over 2 years at a given rate, asking for the principal. The student uses difference = P(R/100)².

### Allowed Variations

- solve for principal, or for the difference given the principal

### Forbidden

- a period other than 2 years (the closed form changes)
- a non-integer principal

### Validator Must Check

- the closed-form relation is used and the principal equals the correct option
- one distractor computes CI and SI separately and subtracts with an error

### Example Skeleton

```text
The difference between compound and simple interest on a sum for 2 years at 10% is ₹100.
Question: Find the principal.
Answer: ₹10,000
```

---

# Domain G: Time & Work

## Domain Purpose

Test work-rate reasoning: single and combined workers, efficiency, multi-phase scheduling, and three-equation rate systems.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `SINGLE_RATE` | Rate of one worker as 1/time |
| `COMBINED_RATE` | Add rates of workers acting together |
| `PHASE_WORK` | Account for work done across start/stop phases |
| `EFFICIENCY_MODIFIER` | Scale a rate by an efficiency factor |
| `PHASE_FEASIBILITY` | Decide if phased work completes within a cap |
| `AVAILABILITY_FEASIBILITY` | Decide feasibility when workers have limited availability |
| `THREE_EQUATION_SYSTEM` | Solve pairwise-rate equations for individual or combined rates |

## Domain-Wide Rules

- Work equals rate times time; rates add, times do not.
- Choose times so combined rates invert to clean numbers.
- Difficulty comes from phase boundaries, binding caps, and systems, not from more workers.

## Domain Option Rules

Time-and-work distractors must come from rate-handling errors:

- `WRONG_METHOD`: average the days instead of adding the rates.
- `PARTIAL_COMPUTATION`: account for only one phase.
- `SCALE_ERROR`: multiply time by efficiency instead of dividing.
- `IGNORED_CONSTRAINT`: ignore the cap or availability window.

For the three-equation template, one distractor must average the three pairwise times.

---

## NUM_TW_L1_034: Single Worker

```yaml
domain: Time & Work
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - SINGLE_RATE
allowed_values:
    days: 4-20
    answer: integer or simple fraction
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question with one worker's completion time, asking for the fraction done in a given time or the time for a given fraction.

### Allowed Variations

- fraction completed, or time for a fraction

### Forbidden

- a second worker
- an awkward fraction

### Validator Must Check

- rate is 1/days and the result equals the correct option

### Example Skeleton

```text
A can complete a task in 15 days.
Question: What fraction is done in 5 days?
Answer: 1/3
```

---

## NUM_TW_L2_035: Two Workers Combined

```yaml
domain: Time & Work
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - COMBINED_RATE
allowed_values:
    times: 4-24
    combined time: integer or simple fraction
primary_trap: WRONG_METHOD
```

### Contract

Generate a question with two workers' individual times, asking how long they take together. The student adds rates and inverts.

### Allowed Variations

- two workers, taps, or machines

### Forbidden

- averaging the times as the intended method
- an awkward combined time

### Validator Must Check

- rates added and inverted; combined time equals the correct option
- one distractor averages the two times

### Example Skeleton

```text
A finishes a job in 10 days and B in 15 days.
Question: How long working together?
Answer: 6 days
```

---

## NUM_TW_L2_036: Start/Stop Times

```yaml
domain: Time & Work
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - PHASE_WORK
allowed_values:
    clean phase boundaries
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where one worker works alone for part of the job and another joins or leaves, asking for the total time. The student accounts for work done in each phase.

### Allowed Variations

- one joins partway, or one leaves partway

### Forbidden

- more than two phases (that approaches L3)
- ignoring the first phase's work

### Validator Must Check

- work per phase is accounted for and the total time equals the correct option

### Example Skeleton

```text
A works alone for 4 days, then B joins. A alone takes 12 days, B alone 8 days.
Question: What is the total time to finish?
Answer: 7.2 days
```

---

## NUM_TW_L2_037: Efficiency Multiplier

```yaml
domain: Time & Work
difficulty_level: L2
tree_signature: [LEAF, OPERATION, MODIFIER, OPERATION]
answer_mode: VALUE
required_operators:
    - EFFICIENCY_MODIFIER
allowed_values:
    efficiency: {0.5, 0.75, 1.25, 1.5}
    answer: clean
primary_trap: SCALE_ERROR
```

### Contract

Generate a question where a worker operates at a stated efficiency relative to normal, asking for the adjusted completion time. Effective rate = base rate × efficiency.

### Allowed Variations

- reduced or increased efficiency

### Forbidden

- a binding feasibility constraint (that would be L3)
- multiplying time by efficiency instead of dividing

### Validator Must Check

- the effective rate scales the base rate and the time equals the correct option
- one distractor multiplies time by efficiency

### Example Skeleton

```text
A can do a job in 20 days at full efficiency. Working at 75% efficiency,
Question: how long does it take?
Answer: 26.67 days
```

---

## NUM_TW_L3_038: Multi-Phase With a Binding Cap

```yaml
domain: Time & Work
difficulty_level: L3
tree_signature: [LEAF, FORMULA, OPERATION, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: FEASIBILITY
required_operators:
    - PHASE_WORK
    - PHASE_FEASIBILITY
difficulty_source: phased work tracked against a day cap that can genuinely be exceeded
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question with work split across phases using different teams, asking whether it finishes within a day cap. The cap must be able to bind under a plausible wrong method.

### Allowed Variations

- two or three phases with different teams

### Forbidden

- a cap that is never close to binding (synthetic)
- inconsistent phase definitions

### Validator Must Check

- work per phase computed, remaining work checked against the cap
- the feasibility answer equals the correct option
- one distractor ignores the cap

### Example Skeleton

```text
A (10 days), B (15 days), C (12 days). Phase 1: A+B work 3 days. Phase 2: B+C finish.
The cap is 9 total days.
Question: Do they finish in time?
Answer: Yes (about 6.3 days)
```

---

## NUM_TW_L3_039: Feasibility Under Availability

```yaml
domain: Time & Work
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: FEASIBILITY
required_operators:
    - AVAILABILITY_FEASIBILITY
    - EFFICIENCY_MODIFIER
difficulty_source: limited availability or reduced efficiency makes feasibility genuinely uncertain
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question where workers have limited availability windows or reduced efficiency, asking whether the deadline is met. The student computes effective work delivered against the requirement.

### Allowed Variations

- one worker leaves early, or works at reduced efficiency
- a deadline that may or may not be met

### Forbidden

- a deadline that is trivially met or missed
- inconsistent availability data

### Validator Must Check

- effective contribution computed against the requirement
- the feasibility answer equals the correct option
- one distractor uses full availability or full efficiency

### Example Skeleton

```text
A (12 days) and B (18 days) work together, but B works at 80% efficiency.
The deadline is 9 days.
Question: Is the job feasible?
Answer: Yes
```

---

## NUM_TW_L3_040: Three-Equation Rate System

```yaml
domain: Time & Work
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - THREE_EQUATION_SYSTEM
allowed_values:
    pair-times chosen so individual rates are clean
difficulty_source: solve a three-equation system from pairwise rates
primary_trap: WRONG_METHOD
```

### Contract

Generate a question giving the times for A+B, B+C and A+C, asking for the all-three time or one worker alone. The student adds the pairwise rates to get 2(A+B+C), then isolates.

### Allowed Variations

- ask for all-three time, or one individual time

### Forbidden

- pair-times that give non-clean individual rates
- averaging the pair-times as the intended method

### Validator Must Check

- pairwise rates summed and halved; the asked rate inverted to a clean time equal to the correct option
- one distractor averages the three pairwise times

### Example Skeleton

```text
A+B do a job in 12 days, B+C in 15 days, A+C in 20 days.
Question: How long for all three together?
Answer: 10 days
```

---

# Domain H: Time–Speed–Distance

## Domain Purpose

Test motion: basic relations, relative speed, train crossing, multi-segment routing, arrival windows, and boats-and-streams systems.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `BASIC_MOTION` | D = S × T |
| `RELATIVE_SPEED` | Combine speeds for meeting/overtaking |
| `TRAIN_CROSSING` | Add lengths to the distance covered |
| `SEGMENT_ROUTING` | Sum segment times plus stops |
| `ARRIVAL_WINDOW` | Compute the feasible speed band for an arrival window |
| `STREAM_SYSTEM` | Solve two trips for still-water and stream speed |

## Domain-Wide Rules

- Convert units (km/h ↔ m/s) before combining.
- Choose distances and speeds so times and speeds are clean.
- Difficulty comes from relative motion and back-solving, not from larger distances.

## Domain Option Rules

Motion distractors must come from speed and distance errors:

- `WRONG_METHOD`: add speeds when moving apart or subtract when approaching.
- `PARTIAL_COMPUTATION`: omit a train/platform length, or track one segment only.
- `REVERSE_DIRECTION`: swap the min and max bound of a speed window.
- `ARITHMETIC_SLIP`: correct setup, calculation error.

For the stream-system template, one distractor must average the two trip speeds.

---

## NUM_TSD_L1_040: Basic Motion

```yaml
domain: Time–Speed–Distance
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - BASIC_MOTION
allowed_values:
    S: 20-100
    T: 1-6
    D: integer
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question giving two of speed, distance, time and asking for the third.

### Allowed Variations

- solve for distance, speed, or time

### Forbidden

- a non-integer answer
- relative motion

### Validator Must Check

- D = S × T (rearranged as needed) equals the correct option

### Example Skeleton

```text
A car travels at 60 km/h for 3 hours.
Question: How far does it go?
Answer: 180 km
```

---

## NUM_TSD_L2_041: Relative Speed

```yaml
domain: Time–Speed–Distance
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - RELATIVE_SPEED
allowed_values:
    integer meeting/overtaking time
primary_trap: WRONG_METHOD
```

### Contract

Generate a question with two objects moving toward each other or in the same direction, asking when they meet or one overtakes the other.

### Allowed Variations

- approaching (subtract distance, add speeds) or same direction (subtract speeds)

### Forbidden

- a non-integer time
- ambiguous directions

### Validator Must Check

- relative speed combined correctly and the time equals the correct option
- one distractor uses the wrong sign for relative speed

### Example Skeleton

```text
Two trains move toward each other at 60 and 40 km/h, 400 km apart.
Question: When do they meet?
Answer: 4 hours
```

---

## NUM_TSD_L2_042: Train Crossing

```yaml
domain: Time–Speed–Distance
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - TRAIN_CROSSING
allowed_values:
    lengths combine; speed convertible to m/s cleanly
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where a train of given length crosses a platform, pole, or another train, asking for the crossing time. The student adds the relevant lengths to the distance.

### Allowed Variations

- pole (length zero), platform, or another train

### Forbidden

- omitting the train length
- a non-terminating time

### Validator Must Check

- total distance includes both lengths; the time equals the correct option
- one distractor omits the platform/object length

### Example Skeleton

```text
A 200 m train at 72 km/h crosses a 100 m platform.
Question: How long does the crossing take?
Answer: 15 s
```

---

## NUM_TSD_L3_043: Multi-Segment Routing

```yaml
domain: Time–Speed–Distance
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION, CONSTRAINT]
answer_mode: FEASIBILITY
required_operators:
    - SEGMENT_ROUTING
difficulty_source: sum segment times plus a stop and test against a deadline that can bind
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a journey with two segments at different speeds plus a stop, asking whether the total time meets a deadline that can genuinely fail.

### Allowed Variations

- two segments and one stop
- ask feasibility and the total time

### Forbidden

- a deadline that is trivially met
- inconsistent segment data

### Validator Must Check

- segment times and stop summed; feasibility equals the correct option
- one distractor omits the stop

### Example Skeleton

```text
120 km at 60 km/h, then 80 km at 40 km/h, plus a 30-minute stop. The deadline is 5 hours.
Question: Is it feasible?
Answer: Yes (4.5 hours)
```

---

## NUM_TSD_L3_045: Optimize Speed for an Arrival Window

```yaml
domain: Time–Speed–Distance
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, CONSTRAINT]
answer_mode: RANGE
required_operators:
    - ARRIVAL_WINDOW
difficulty_source: compute both bounds of a feasible speed band
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question where a distance must be covered within an arrival window, asking for the valid speed range, checked against a vehicle maximum.

### Allowed Variations

- a window of arrival times, a max vehicle speed

### Forbidden

- a window giving a non-clean speed bound
- swapping which bound corresponds to which time

### Validator Must Check

- min speed = distance/latest time, max speed = distance/earliest time, both within the cap
- the range equals the correct option
- one distractor swaps the bounds

### Example Skeleton

```text
A 240 km journey must finish between 3 and 4 hours; the vehicle's top speed is 90 km/h.
Question: What speed range is valid?
Answer: 60–80 km/h
```

---

## NUM_TSD_L3_046: Boats and Streams System

```yaml
domain: Time–Speed–Distance
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - STREAM_SYSTEM
allowed_values:
    two trips chosen so upstream/downstream rates are clean
difficulty_source: two equations, two unknowns (still-water and stream speed)
primary_trap: WRONG_METHOD
```

### Contract

Generate a question with two up/down trips and their times, asking for the still-water or stream speed. The student treats 1/upstream and 1/downstream as unknowns, solves, then recovers the speeds.

### Allowed Variations

- ask for still-water speed or stream speed

### Forbidden

- trips giving non-integer upstream/downstream speeds
- averaging the trip speeds as the intended method

### Validator Must Check

- the two-equation system is solved and the recovered speed equals the correct option
- one distractor averages the trip speeds

### Example Skeleton

```text
A boat goes 30 km upstream and 44 km downstream in 10 hours, and 40 km upstream and
55 km downstream in 13 hours.
Question: Find the boat's speed in still water.
Answer: 8 km/h
```

---

# Domain I: Pipes / Tanks / Flow

## Domain Purpose

Test fill/empty rates, multi-pipe combinations, phased fills, proportional-rate pipes, and schedule optimization.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `NET_RATE` | Combine inflow and outflow rates |
| `MULTI_PIPE` | Combine several inlets and outlets |
| `PHASE_FILL` | Track volume across fill phases |
| `PROPORTIONAL_RATES` | Pipes whose rates are fixed multiples of each other |
| `SCHEDULE_OPTIMIZE` | Minimize time or cost subject to a binding cap |

## Domain-Wide Rules

- Net rate equals inflows minus outflows.
- Choose rates so fill times are clean.
- Difficulty comes from phasing and binding caps, not from more pipes.

## Domain Option Rules

Pipe distractors must come from rate-combination errors:

- `SCALE_ERROR`: add the drain rate instead of subtracting.
- `WRONG_METHOD`: divide the combined time by the number of pipes.
- `PARTIAL_COMPUTATION`: track one phase only.
- `IGNORED_CONSTRAINT`: pick the cheapest option ignoring the time cap.

For the proportional-rate template, one distractor must divide the combined time by three.

---

## NUM_PT_L1_046: One Inlet One Outlet

```yaml
domain: Pipes / Tanks / Flow
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - NET_RATE
allowed_values:
    fill_time < empty_time
    integer fill time
primary_trap: SCALE_ERROR
```

### Contract

Generate a question with one fill pipe and one drain, both open, asking for the fill time. Net rate = 1/Tf − 1/Te.

### Allowed Variations

- fill and drain times

### Forbidden

- the drain faster than the fill (it never fills)
- a non-integer fill time

### Validator Must Check

- net rate subtracts the drain and the fill time equals the correct option
- one distractor adds the rates

### Example Skeleton

```text
A pipe fills a tank in 6 hours; another empties it in 9 hours. Both open.
Question: How long to fill?
Answer: 18 hours
```

---

## NUM_PT_L2_047: Multiple Inlets and Outlets

```yaml
domain: Pipes / Tanks / Flow
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - MULTI_PIPE
allowed_values:
    rates yield a clean fill time
primary_trap: WRONG_METHOD
```

### Contract

Generate a question with two or more inlets and one or more outlets, all open, asking for the fill time. The student sums all rates.

### Allowed Variations

- two inlets one outlet, or one inlet two outlets

### Forbidden

- a non-terminating fill time
- a phase structure (that is L2_048)

### Validator Must Check

- all rates combined and the fill time equals the correct option

### Example Skeleton

```text
Pipe A fills in 4 hours, pipe B in 6 hours, drain C empties in 8 hours. All open.
Question: How long to fill?
Answer: 24/7 hours
```

---

## NUM_PT_L2_048: Two-Phase Fill

```yaml
domain: Pipes / Tanks / Flow
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - PHASE_FILL
allowed_values:
    clean phase volumes
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where a pipe fills alone for a time, then a drain opens, asking for the total fill time. The student tracks the volume per phase.

### Allowed Variations

- fill alone then drain opens, or drain joins later

### Forbidden

- ignoring the first phase's volume
- a non-terminating time

### Validator Must Check

- volume after phase 1 and the phase-2 net rate computed; total time equals the correct option

### Example Skeleton

```text
A tank fills in 8 hours. The inlet runs alone for 3 hours, then a drain (12-hour empty rate) opens.
Question: What is the total fill time?
Answer: 18 hours
```

---

## NUM_PT_L2_049: Three-Phase Fill

```yaml
domain: Pipes / Tanks / Flow
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - PHASE_FILL
allowed_values:
    clean phase volumes
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question extending the two-phase fill to a third phase (a second pipe joins), asking for the total fill time. The student tracks volume across three phases.

### Allowed Variations

- a second inlet joins partway

### Forbidden

- a binding capacity constraint (that would be synthetic L3)
- a non-terminating time

### Validator Must Check

- volume tracked across all three phases; total time equals the correct option

### Example Skeleton

```text
Pipe A (5-hour fill) runs alone for 2 hours, then pipe B (10-hour fill) joins.
Question: What is the total fill time?
Answer: about 4.67 hours
```

---

## NUM_PT_L3_050: Proportional-Rate Pipes

```yaml
domain: Pipes / Tanks / Flow
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - PROPORTIONAL_RATES
allowed_values:
    combined time chosen so the base rate is a clean fraction
difficulty_source: rates set as r, 2r, 4r and solved from the combined time
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where each pipe fills a fixed multiple faster than the previous, and together they fill in a given time, asking how long the slowest takes alone. The student sets rates as r, 2r, 4r, sums them, and solves.

### Allowed Variations

- three pipes in a doubling progression

### Forbidden

- a combined time giving a non-clean base rate
- dividing the combined time by three as the intended method

### Validator Must Check

- the summed multiple of r equals the combined rate; the slowest time equals the correct option
- one distractor divides the combined time by three

### Example Skeleton

```text
Three pipes: the second fills twice as fast as the first, the third twice as fast as the second.
Together they fill a tank in 4 hours.
Question: How long does the first pipe alone take?
Answer: 28 hours
```

---

## NUM_PT_L3_051: Optimize Schedule

```yaml
domain: Pipes / Tanks / Flow
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - SCHEDULE_OPTIMIZE
difficulty_source: a cost/time trade-off where the cheapest option within the cap is not obvious
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question with pipe options that have per-hour costs and a time cap, asking which option minimizes cost while meeting the cap. The cap must eliminate the naively cheapest option.

### Allowed Variations

- single pipes vs combinations, with per-hour costs

### Forbidden

- a cap that does not eliminate any option (synthetic)
- a dominant option that wins on both time and cost

### Validator Must Check

- each option's time and cost computed against the cap; the cheapest feasible option equals the correct option
- one distractor picks the cheapest per-hour option ignoring the cap

### Example Skeleton

```text
Pipe A fills in 4 hours at ₹50/hour; pipe B in 6 hours at ₹30/hour. Options: A alone, B alone, or A+B.
The time cap is 5 hours. Minimize cost.
Answer: A+B at ₹192
```

---

# Domain J: Permutations & Combinations

## Domain Purpose

Test counting of arrangements and selections, including restricted, circular, and divisibility-constrained counts.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `BASIC_COUNT` | A single nPr or nCr |
| `ORDER_DECISION` | Decide whether order matters, then count |
| `RESTRICTED_ARRANGE` | Glue or separate items under a restriction |
| `GAP_METHOD` | Place items in gaps to enforce non-adjacency |
| `DIVISIBILITY_SELECT` | Select digit sets meeting a divisibility rule, then arrange |
| `CIRCULAR_ARRANGE` | Round-table counting with (n−1)! base |

## Domain-Wide Rules

- State clearly whether order matters.
- Keep counts small enough that the reasoning, not the arithmetic, is the work.
- Difficulty comes from the restriction structure, not from larger n.

## Domain Option Rules

Counting distractors must come from method confusion:

- `WRONG_METHOD`: use permutation where combination is needed, or a linear base for a circular problem.
- `PARTIAL_COMPUTATION`: forget the internal arrangements of a glued group, or skip the divisibility filter.
- `SCALE_ERROR`: off by a factorial factor.
- `ARITHMETIC_SLIP`: correct method, calculation error.

For the divisibility template, one distractor must count all arrangements without filtering. For the circular template, one distractor must use n! instead of (n−1)!.

---

## NUM_PN_L1_050: Basic nPr / nCr

```yaml
domain: Permutations & Combinations
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - BASIC_COUNT
allowed_values:
    n: 4-8
    r: 2-4
    result: ≤ 5040
primary_trap: WRONG_METHOD
```

### Contract

Generate a question requiring a single permutation or combination, with order clearly implied by the phrasing.

### Allowed Variations

- arrange n items, or choose r from n

### Forbidden

- ambiguous order
- a restriction (that is L2)

### Validator Must Check

- the correct formula (P or C) is applied and equals the correct option
- one distractor uses the other of P/C

### Example Skeleton

```text
In how many ways can 4 students be arranged in a row?
Answer: 24
```

---

## NUM_PN_L2_051: Choose Permutation vs Combination

```yaml
domain: Permutations & Combinations
difficulty_level: L2
tree_signature: [LEAF, OPERATION, FORMULA]
answer_mode: VALUE
required_operators:
    - ORDER_DECISION
allowed_values:
    clear ordered/unordered cue
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where the student must first decide whether order matters (committee vs ranked roles), then apply the right count.

### Allowed Variations

- committee (unordered) vs ranked roles (ordered)

### Forbidden

- phrasing that does not signal order clearly
- a restriction beyond order

### Validator Must Check

- the order decision is correct and the count equals the correct option
- one distractor uses the wrong one of P/C

### Example Skeleton

```text
A committee of 3 is formed from 6 people.
Question: In how many ways?
Answer: 20
```

---

## NUM_PN_L2_052: Restricted Arrangements

```yaml
domain: Permutations & Combinations
difficulty_level: L2
tree_signature: [LEAF, OPERATION, FORMULA, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - RESTRICTED_ARRANGE
allowed_values:
    group size: 2-3
    result: ≤ 10000
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where certain items must stay together, asking for the number of arrangements. The student glues the group as a unit and multiplies by internal arrangements.

### Allowed Variations

- two or three items must be together

### Forbidden

- forgetting the internal arrangements
- a not-together restriction (that is L2_053)

### Validator Must Check

- the glued-unit count is multiplied by internal arrangements; result equals the correct option
- one distractor omits the internal arrangements

### Example Skeleton

```text
5 people sit in a row; A and B must sit together.
Question: How many arrangements?
Answer: 48
```

---

## NUM_PN_L2_053: Multi-Constraint Counting (Gap Method)

```yaml
domain: Permutations & Combinations
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - GAP_METHOD
allowed_values:
    small n
primary_trap: WRONG_METHOD
```

### Contract

Generate a question requiring a no-two-adjacent arrangement (gap method) or a total-minus-together count. Mechanical once the method is known.

### Allowed Variations

- no two of one type adjacent, or a forbidden pair

### Forbidden

- more than one interacting restriction (that approaches L3)
- ambiguous adjacency

### Validator Must Check

- the gap method or complement is applied and equals the correct option

### Example Skeleton

```text
6 people, 3 men and 3 women, no two men adjacent.
Question: How many arrangements?
Answer: 144
```

---

## NUM_PN_L3_054: Divisibility Arrangement

```yaml
domain: Permutations & Combinations
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - DIVISIBILITY_SELECT
difficulty_source: select digit sets meeting a divisibility property, then permute them
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question forming k-digit numbers from a digit pool that must be divisible by 3 or 5, asking how many exist. The student identifies valid digit sets, then counts arrangements.

### Allowed Variations

- divisible by 3 (digit-sum rule) or by 5 (last-digit rule)

### Forbidden

- counting arrangements without the divisibility filter
- a pool so large the count becomes unwieldy

### Validator Must Check

- valid digit sets are identified and arranged; total equals the correct option
- one distractor counts all arrangements ignoring divisibility

### Example Skeleton

```text
How many 3-digit numbers from the digits 1–6 (no repetition) are divisible by 5?
Answer: 20
```

---

## NUM_PN_L3_055: Circular With Restriction

```yaml
domain: Permutations & Combinations
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - CIRCULAR_ARRANGE
difficulty_source: circular base count (n−1)! adjusted for a together/apart restriction
primary_trap: WRONG_METHOD
```

### Contract

Generate a round-table arrangement with a together or not-adjacent restriction, asking for the number of arrangements. The student uses the (n−1)! base and adjusts.

### Allowed Variations

- two people must sit together, or must not be adjacent

### Forbidden

- using a linear n! base
- ambiguous seating direction

### Validator Must Check

- the circular base is used and the restriction applied; result equals the correct option
- one distractor uses the linear base

### Example Skeleton

```text
6 people sit around a round table; two specific people must never be adjacent.
Question: How many arrangements?
Answer: 72
```

---

# Domain K: Probability

## Domain Purpose

Test event probability, complement, sequential draws, expected-value decisions, and conditional / Bayes reasoning.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `BASIC_PROB` | favorable / total |
| `COMPLEMENT` | 1 − P(none) for at-least-one |
| `SEQUENTIAL_DRAW` | Update probabilities across draws |
| `EXPECTED_VALUE` | Probability-weighted payoff, net of cost |
| `BAYES` | Posterior from base rates and conditionals |
| `CONDITIONAL_RESTRICT` | Restrict the sample space, then compute |

## Domain-Wide Rules

- Probabilities lie in [0,1]; answers are usually simple fractions.
- For no-replacement problems, update the pool between draws.
- Difficulty comes from conditioning and updating, not from larger sample spaces.

## Domain Option Rules

Probability distractors must come from conditioning errors:

- `WRONG_METHOD`: sum individual probabilities for at-least-one; use a raw rate in Bayes.
- `PARTIAL_COMPUTATION`: forget to update after a no-replacement draw; use the full sample space.
- `IGNORED_CONSTRAINT`: ignore the entry cost in expected value.
- `SCALE_ERROR`: invert favorable/total.

For Bayes, one distractor must use the conditional rate directly without base rates.

---

## NUM_PR_L1_054: Basic Probability

```yaml
domain: Probability
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - BASIC_PROB
allowed_values:
    simple fraction
primary_trap: SCALE_ERROR
```

### Contract

Generate a single-event probability from a clearly described sample space.

### Allowed Variations

- balls, dice, cards

### Forbidden

- conditioning or sequencing
- a non-reducible awkward fraction

### Validator Must Check

- favorable/total reduced and equals the correct option
- one distractor inverts the fraction

### Example Skeleton

```text
A bag has 4 red and 6 blue balls.
Question: What is the probability of drawing a red ball?
Answer: 2/5
```

---

## NUM_PR_L2_055: Complement / At-Least-One

```yaml
domain: Probability
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - COMPLEMENT
allowed_values:
    simple fraction
primary_trap: WRONG_METHOD
```

### Contract

Generate an at-least-one question solved via the complement 1 − P(none).

### Allowed Variations

- repeated tosses or trials

### Forbidden

- summing individual probabilities as the intended method
- an awkward fraction

### Validator Must Check

- 1 − P(none) computed and equals the correct option
- one distractor sums the individual probabilities

### Example Skeleton

```text
A coin is tossed 4 times.
Question: What is the probability of at least one head?
Answer: 15/16
```

---

## NUM_PR_L2_056: Sequential Draws

```yaml
domain: Probability
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - SEQUENTIAL_DRAW
allowed_values:
    simple fraction
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a two-draw question, with or without replacement, asking for a compound probability. The student updates the pool between draws if without replacement.

### Allowed Variations

- with or without replacement

### Forbidden

- forgetting to update without replacement
- an awkward fraction

### Validator Must Check

- the pool is updated correctly and the product equals the correct option
- one distractor does not update the pool

### Example Skeleton

```text
A bag has 3 red and 5 blue balls; two are drawn without replacement.
Question: P(first red, second blue)?
Answer: 15/56
```

---

## NUM_PR_L3_057: Expected-Value Decision

```yaml
domain: Probability
difficulty_level: L3
tree_signature: [LEAF, FORMULA, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - EXPECTED_VALUE
difficulty_source: compute expected value net of cost and decide between options
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question with probabilistic payoffs and a cost or an alternative, asking which choice has higher expected value or whether to play. The student computes EV net of cost.

### Allowed Variations

- a gamble vs a sure thing, or whether a paid game is worth playing

### Forbidden

- ignoring the cost as the intended method
- probabilities not summing to 1

### Validator Must Check

- EV computed net of cost and the decision equals the correct option
- one distractor ignores the entry cost

### Example Skeleton

```text
Option A: 60% chance of ₹1,000 profit, 40% chance of ₹500 loss. Option B: a guaranteed ₹200.
Question: Which has higher expected value?
Answer: Option A (EV ₹400)
```

---

## NUM_PR_L3_058: Conditional / Bayes

```yaml
domain: Probability
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - BAYES
difficulty_source: posterior from total probability and base rates
primary_trap: WRONG_METHOD
```

### Contract

Generate a question with sources having base rates and conditional rates, where an outcome is observed and the source posterior is asked. The student applies Bayes via total probability.

### Allowed Variations

- machines and defect rates, bags and draw colors

### Forbidden

- using the conditional rate directly as the answer
- base rates not summing to 1

### Validator Must Check

- the posterior is computed via total probability and equals the correct option
- one distractor uses the raw conditional rate ignoring base rates

### Example Skeleton

```text
Machines A, B, C make 50%, 30%, 20% of output with defect rates 2%, 3%, 5%.
A product is defective.
Question: What is the probability it came from A?
Answer: about 0.345
```

---

## NUM_PR_L3_059: Conditional on an Event

```yaml
domain: Probability
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - CONDITIONAL_RESTRICT
difficulty_source: restrict the sample space to the given event, then compute within it
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question conditioning on a stated event (e.g. the sum of two dice is at least 9), asking for a probability within the restricted space.

### Allowed Variations

- dice sums, card draws meeting a condition

### Forbidden

- using the full sample space
- an event with an empty or trivial restriction

### Validator Must Check

- the sample space is restricted to the event and the probability equals the correct option
- one distractor uses the full sample space

### Example Skeleton

```text
Two dice are rolled. Given the sum is at least 9,
Question: what is the probability both show the same number?
Answer: 3/10
```

---

# Domain L: Number Series & Patterns — capped at L2

## Domain Purpose

Infer the rule governing an ordered sequence and extend it.

## Domain note on level ceiling

Pattern recognition resolves in a single insight; it is not multi-step computation. **This domain has no genuine L3.** A "choose the rule from options" framing is easier, not harder, because options can be tested. Do not generate L3 series questions.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `CONSTANT_STEP` | Same add/subtract each step |
| `CONSTANT_RATIO` | Same multiply/divide each step |
| `POSITION_STEP` | Step depends on position |
| `COMPOSED_STEP` | A fixed two-operation transform repeated |
| `ALTERNATING_RULES` | Two interleaved subsequences |
| `RULE_VALIDATE` | Test candidate rules against all terms |

## Domain-Wide Rules

- The intended rule must be nameable and fit every visible term.
- Sequence values usually stay between −100 and 300.
- Difficulty comes from rule structure, not arithmetic burden.

## Domain Option Rules

Series distractors must come from rule mistakes:

- `PARTIAL_REASONING`: use only the first two transitions.
- `WRONG_METHOD`: multiply where the rule adds, or treat alternating as single-rule.
- `REVERSE_DIRECTION`: apply the change the wrong way.
- `ARITHMETIC_SLIP`: correct rule, calculation error.

---

## NUM_NS_L1_058: AP / GP Next Term

```yaml
domain: Number Series & Patterns
difficulty_level: L1
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - exactly one of: CONSTANT_STEP, CONSTANT_RATIO
allowed_values:
    AP_step: 2-6
    GP_ratio: 2-3
    next: ≤ 500
primary_trap: WRONG_METHOD
```

### Contract

Generate a sequence with a single constant step or constant ratio, asking for the next term.

### Allowed Variations

- arithmetic or geometric

### Forbidden

- mixed or position-dependent rules
- values outside the scale

### Validator Must Check

- the constant rule fits all terms and the next term equals the correct option
- one distractor uses the other rule type (AP vs GP)

### Example Skeleton

```text
Sequence: 3, 6, 12, 24, ?
Answer: 48
```

---

## NUM_NS_L2_059: Mixed-Operations Series

```yaml
domain: Number Series & Patterns
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - exactly one of: POSITION_STEP, COMPOSED_STEP
allowed_values:
    not explainable by a single L1 rule
primary_trap: PARTIAL_REASONING
```

### Contract

Generate a sequence whose step depends on position or repeats a fixed two-operation transform, asking for the next term.

### Allowed Variations

- increasing differences, or a ×then+ transform

### Forbidden

- a single L1 rule that explains everything
- multiple reasonable continuations

### Validator Must Check

- the declared rule fits every transition and the next term equals the correct option
- one distractor uses only the first two transitions

### Example Skeleton

```text
Sequence: 2, 4, 12, 48, 240, ?  (×2, ×3, ×4, ×5)
Answer: 1440
```

---

## NUM_NS_L2_060: Alternating Two-Rule Series

```yaml
domain: Number Series & Patterns
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - ALTERNATING_RULES
allowed_values:
    two interleaved subsequences
primary_trap: WRONG_METHOD
```

### Contract

Generate a sequence where odd and even positions follow two different simple rules, asking for the next term.

### Allowed Variations

- two interleaved arithmetic or geometric subsequences

### Forbidden

- more than two interleaved rules
- a single rule that fits everything

### Validator Must Check

- each subsequence follows its rule and the next term equals the correct option
- one distractor treats the sequence as a single rule

### Example Skeleton

```text
Sequence: 2, 5, 4, 10, 8, 20, ?  (odds ×2; evens ×2)
Answer: 16
```

---

## NUM_NS_L2_061: Rule Identification

```yaml
domain: Number Series & Patterns
difficulty_level: L2
tree_signature: [LEAF, OPERATION]
answer_mode: COMPARISON
required_operators:
    - RULE_VALIDATE
allowed_values:
    exactly one candidate rule fits all terms
primary_trap: PARTIAL_REASONING
```

### Contract

Generate a sequence with four candidate rules, exactly one of which fits every term, asking the student to identify it and give the next term.

### Allowed Variations

- arithmetic, geometric, or simple polynomial-style rules

### Forbidden

- two rules fitting all terms
- obviously unrelated candidate rules

### Validator Must Check

- exactly one rule fits all terms; the choice and next term equal the correct option
- each distractor rule fails at least one term

### Example Skeleton

```text
Sequence: 1, 2, 5, 10, 17, 26. Which rule fits, and what is the next term?
Answer: n² + 1, next 37
```

---

# Domain M: Divisibility / HCF / LCM

## Domain Purpose

Test number-property reasoning, HCF/LCM relations, and constrained number-finding.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `DIVISIBILITY_RULE` | Apply a divisibility test |
| `LCM_HCF_COMPUTE` | Compute LCM or HCF from factorizations |
| `FACTOR_PROPERTY` | Derive a property from prime factorization |
| `HCF_LCM_RELATION` | Use product = HCF × LCM |
| `COMMON_REMAINDER` | LCM plus a fixed offset |

## Domain-Wide Rules

- Use the HCF × LCM = product relation where relevant.
- Choose numbers so factorizations are clean.
- Difficulty comes from combining properties, not from larger numbers.

## Domain Option Rules

Number-property distractors must come from:

- `WRONG_METHOD`: confuse HCF and LCM, or add/average instead of using the product relation.
- `PARTIAL_COMPUTATION`: forget to add the remainder offset.
- `ARITHMETIC_SLIP`: factorization or multiplication error.

---

## NUM_DV_L1_062: Divisibility Check

```yaml
domain: Divisibility / HCF / LCM
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - DIVISIBILITY_RULE
allowed_values:
    n: 50-500
    divisor: common
primary_trap: ARITHMETIC_SLIP
```

### Contract

Generate a question asking whether a number is divisible by a given divisor, using a divisibility rule.

### Allowed Variations

- divisibility by 3, 4, 6, 8, 9, 11

### Forbidden

- a divisor needing factorization beyond a simple rule

### Validator Must Check

- the divisibility rule gives the correct yes/no equal to the correct option

### Example Skeleton

```text
Is 432 divisible by 9?
Answer: Yes
```

---

## NUM_DV_L2_063: Apply LCM / HCF

```yaml
domain: Divisibility / HCF / LCM
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA]
answer_mode: VALUE
required_operators:
    - LCM_HCF_COMPUTE
allowed_values:
    numbers: 6-60
primary_trap: WRONG_METHOD
```

### Contract

Generate a question asking for the LCM or HCF of two or three numbers via factorization.

### Allowed Variations

- LCM or HCF, two or three numbers

### Forbidden

- numbers with unwieldy factorizations

### Validator Must Check

- the factorization is correct and the result equals the correct option
- one distractor swaps HCF and LCM

### Example Skeleton

```text
Find the LCM of 12, 18 and 24.
Answer: 72
```

---

## NUM_DV_L2_064: Prime Factorization Reasoning

```yaml
domain: Divisibility / HCF / LCM
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - FACTOR_PROPERTY
allowed_values:
    n: 50-300
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question asking for a property derived from a prime factorization (number of factors, sum of distinct primes).

### Allowed Variations

- factor count, sum of distinct primes

### Forbidden

- a number whose factorization is unwieldy

### Validator Must Check

- the factorization-derived property equals the correct option

### Example Skeleton

```text
How many factors does 360 have?
Answer: 24
```

---

## NUM_DV_L3_065: HCF–LCM Product Relation

```yaml
domain: Divisibility / HCF / LCM
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - HCF_LCM_RELATION
allowed_values:
    other number integer
difficulty_source: use the non-obvious relation product = HCF × LCM
primary_trap: WRONG_METHOD
```

### Contract

Generate a question giving the HCF, the LCM, and one of two numbers, asking for the other. The student uses product = HCF × LCM.

### Allowed Variations

- solve for the other number

### Forbidden

- numbers where the other value is non-integer
- adding or averaging as the intended method

### Validator Must Check

- the product relation gives an integer equal to the correct option
- one distractor adds or averages HCF and LCM

### Example Skeleton

```text
The HCF of two numbers is 12 and their LCM is 432. One number is 48.
Question: Find the other.
Answer: 108
```

---

## NUM_DV_L3_066: Common-Remainder Problem

```yaml
domain: Divisibility / HCF / LCM
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: VALUE
required_operators:
    - COMMON_REMAINDER
difficulty_source: combine an LCM with a fixed offset and select the smallest in range
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question asking for the smallest number leaving a fixed remainder under several divisors. The student finds the LCM and adds the remainder.

### Allowed Variations

- a common remainder, or "leaves remainder r in each case"

### Forbidden

- forgetting to add the remainder
- divisors with an unwieldy LCM

### Validator Must Check

- LCM plus remainder equals the correct option
- one distractor reports the LCM without the offset

### Example Skeleton

```text
Find the smallest number that leaves remainder 6 when divided by 12, 15, 20 and 35.
Answer: 426
```

---

# Domain N: Remainders / Modular

## Domain Purpose

Test modular arithmetic, remainder cycles, CRT-style constraint solving, and large-power remainders.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `SIMPLE_MOD` | n mod d |
| `CYCLE_UNITS` | Units digit via a power cycle |
| `CRT_CANDIDATE` | Intersect two congruences |
| `LARGE_POWER_MOD` | Reduce a large exponent via the cycle mod m |
| `LAST_TWO_DIGITS` | Cycle mod 100 |

## Domain-Wide Rules

- Large powers reduce via the cycle length.
- Choose bases and moduli so cycles are short and clean.
- Difficulty comes from cycle reduction and intersection, not from larger exponents alone.

## Domain Option Rules

Modular distractors must come from:

- `WRONG_METHOD`: compute the power directly, or satisfy one congruence only.
- `SCALE_ERROR`: use the wrong cycle length (mod 10 instead of mod 100).
- `PARTIAL_COMPUTATION`: stop after one congruence.
- `ARITHMETIC_SLIP`: cycle index error.

---

## NUM_RM_L1_067: Simple Remainder

```yaml
domain: Remainders / Modular
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - SIMPLE_MOD
allowed_values:
    n: 10-200
    d: 3-12
primary_trap: ARITHMETIC_SLIP
```

### Contract

Generate a question asking for the remainder of one number divided by another.

### Allowed Variations

- any small divisor

### Forbidden

- powers or cycles

### Validator Must Check

- n mod d equals the correct option

### Example Skeleton

```text
What is the remainder when 47 is divided by 8?
Answer: 7
```

---

## NUM_RM_L2_068: Remainder Cycles

```yaml
domain: Remainders / Modular
difficulty_level: L2
tree_signature: [LEAF, FORMULA, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - CYCLE_UNITS
allowed_values:
    base: {2, 3, 7, 8}
    exponent: 10-50
primary_trap: SCALE_ERROR
```

### Contract

Generate a question asking for the units digit of a power, solved via the cyclic pattern of the last digit.

### Allowed Variations

- bases with a 4-cycle

### Forbidden

- computing the full power
- a base with no clean cycle

### Validator Must Check

- the cycle length and exponent reduction give the units digit equal to the correct option
- one distractor uses the wrong cycle length

### Example Skeleton

```text
What is the units digit of 7^45?
Answer: 7
```

---

## NUM_RM_L3_069: CRT-Style Candidate

```yaml
domain: Remainders / Modular
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: VALUE
required_operators:
    - CRT_CANDIDATE
allowed_values:
    coprime moduli; unique solution in range
difficulty_source: intersect two congruences to find the value in a range
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question giving two modular conditions and a range, asking which value satisfies both. The student intersects the two congruences.

### Allowed Variations

- two congruences with coprime moduli

### Forbidden

- satisfying only one congruence
- moduli giving multiple solutions in range

### Validator Must Check

- both congruences are satisfied by exactly one value equal to the correct option
- one distractor satisfies only one congruence

### Example Skeleton

```text
Find N < 100 where N ≡ 2 (mod 3) and N ≡ 3 (mod 5).
Answer: 38
```

---

## NUM_RM_L3_070: Large-Power Remainder

```yaml
domain: Remainders / Modular
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - LARGE_POWER_MOD
difficulty_source: reduce a large exponent via the cycle of the base mod m
primary_trap: WRONG_METHOD
```

### Contract

Generate a question asking for the remainder of a base raised to a large power, modulo m. The student finds the cycle of base^n mod m and reduces the exponent.

### Allowed Variations

- small modulus with a short cycle

### Forbidden

- attempting to compute the power directly
- a modulus with no clean cycle

### Validator Must Check

- the cycle is found and the exponent reduced; the remainder equals the correct option
- one distractor uses the wrong cycle length

### Example Skeleton

```text
What is the remainder when 2^100 is divided by 7?
Answer: 2
```

---

## NUM_RM_L3_071: Last Two Digits

```yaml
domain: Remainders / Modular
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - LAST_TWO_DIGITS
difficulty_source: cycle mod 100, which is longer than the mod-10 cycle
primary_trap: SCALE_ERROR
```

### Contract

Generate a question asking for the last two digits of a power, solved via the cycle mod 100.

### Allowed Variations

- bases with a manageable mod-100 cycle

### Forbidden

- using the mod-10 cycle
- a base with an unwieldy cycle

### Validator Must Check

- the mod-100 cycle is used and the last two digits equal the correct option
- one distractor uses the units-digit (mod-10) cycle

### Example Skeleton

```text
What are the last two digits of 7^81?
Answer: 07
```

---

# Domain O: Mensuration 2D

## Domain Purpose

Test area and perimeter computation, composite shapes, and genuine spatial reasoning (paths, reshaping).

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `BASIC_2D` | Area or perimeter of a single shape |
| `COMPOSITE_2D` | Combine or subtract shapes; solve a missing dimension |
| `WASTAGE_COST` | Apply wastage to area, then cost |
| `PATH_AREA` | Outer-minus-inner area for a uniform path |
| `WIRE_RESHAPE` | Same perimeter, compare areas of two shapes |

## Domain-Wide Rules

- Use π = 22/7 unless otherwise stated; prefer integer answers.
- Choose dimensions so areas and costs are clean.
- Difficulty comes from the dimensional reasoning, not from larger figures.

## Domain Option Rules

2D distractors must come from:

- `WRONG_METHOD`: area vs perimeter confusion; assume equal perimeter gives equal area.
- `SCALE_ERROR`: add a path width once instead of twice; apply wastage to net not gross.
- `PARTIAL_COMPUTATION`: subtract only one region in a composite.
- `ARITHMETIC_SLIP`: calculation error.

For the path template, one distractor must add the width once.

---

## NUM_MS2_L1_071: Area / Perimeter

```yaml
domain: Mensuration 2D
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - BASIC_2D
allowed_values:
    circle_r: 3-14
    rectangle: 4-20
primary_trap: WRONG_METHOD
```

### Contract

Generate a question asking for the area or perimeter of a single basic shape.

### Allowed Variations

- circle, rectangle, square, triangle

### Forbidden

- composite shapes
- a non-integer answer (choose r as a multiple of 7 for circles)

### Validator Must Check

- the correct formula is applied and equals the correct option
- one distractor swaps area and perimeter

### Example Skeleton

```text
A circle has radius 7 cm. Find its area. (π = 22/7)
Answer: 154 cm²
```

---

## NUM_MS2_L2_072: Composite / Missing Dimension

```yaml
domain: Mensuration 2D
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - COMPOSITE_2D
allowed_values:
    integer result
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question combining two shapes (or subtracting one), or solving a missing dimension from a perimeter, then computing area.

### Allowed Variations

- L-shape, shape with a cutout, dimension from perimeter

### Forbidden

- a non-integer result
- more than two component shapes

### Validator Must Check

- the composite area is computed correctly and equals the correct option

### Example Skeleton

```text
An L-shaped floor is 12 × 8 m with a 4 × 3 m cutout.
Question: Find the area.
Answer: 84 m²
```

---

## NUM_MS2_L2_073: Cost With Wastage

```yaml
domain: Mensuration 2D
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - WASTAGE_COST
allowed_values:
    wastage: {10, 15, 20}%
primary_trap: SCALE_ERROR
```

### Contract

Generate a question where material must cover an area with a wastage allowance, asking for the cost. Gross area = net / (1 − wastage).

### Allowed Variations

- tiling, painting, flooring

### Forbidden

- a feasibility or budget constraint (that would be synthetic L3)
- applying wastage to net instead of gross

### Validator Must Check

- gross area then cost computed; the cost equals the correct option
- one distractor applies wastage to the net area

### Example Skeleton

```text
A 100 m² floor is tiled at ₹300/m² with 20% wastage.
Question: What is the total cost?
Answer: ₹37,500
```

---

## NUM_MS2_L3_074: Path Around a Rectangle

```yaml
domain: Mensuration 2D
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - PATH_AREA
difficulty_source: outer-minus-inner area with the dimension adjusted on both sides
primary_trap: SCALE_ERROR
```

### Contract

Generate a question with a uniform-width path around (inside or outside) a rectangle, asking for the path area. The student computes outer and inner areas and subtracts.

### Allowed Variations

- path inside or outside
- a garden, field, or room

### Forbidden

- adding the width once instead of twice
- a non-integer result

### Validator Must Check

- both dimensions adjusted by twice the width; the path area equals the correct option
- one distractor adds the width once

### Example Skeleton

```text
A 2 m wide path runs around the outside of a 20 m × 15 m garden.
Question: What is the area of the path?
Answer: 156 m²
```

---

## NUM_MS2_L3_075: Wire Reshaped

```yaml
domain: Mensuration 2D
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - WIRE_RESHAPE
difficulty_source: same perimeter forms two shapes; compare their areas
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where a wire of fixed length is bent into one shape then reshaped into another, asking which has greater area and by how much.

### Allowed Variations

- circle vs square, square vs rectangle

### Forbidden

- assuming equal perimeter gives equal area
- a wire length giving non-clean dimensions

### Validator Must Check

- both areas computed from the shared perimeter; the difference equals the correct option
- one distractor assumes equal areas

### Example Skeleton

```text
An 88 cm wire is bent into a circle, then reshaped into a square. (π = 22/7)
Question: Which has greater area and by how much?
Answer: The circle, by 132 cm²
```

---

# Domain P: Mensuration 3D

## Domain Purpose

Test volume and surface area, hollow solids, and conservation / spatial reasoning (melting, painted cubes).

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `BASIC_3D` | Volume or surface area of a single solid |
| `HOLLOW_COMPOSITE` | Outer minus inner volume |
| `CAPACITY_EFFICIENCY` | Effective output = rate × efficiency × time |
| `MELT_RECAST` | Volume conservation across reshaping |
| `PAINTED_CUBE` | Classify unit cubes by painted-face count |

## Domain-Wide Rules

- Use π = 22/7 unless stated.
- Choose dimensions so volumes are clean.
- Difficulty comes from conservation and spatial classification, not from larger solids.

## Domain Option Rules

3D distractors must come from:

- `WRONG_METHOD`: use a radius ratio instead of a volume ratio in recasting; confuse edge/face/corner cubes.
- `SCALE_ERROR`: forget to cube a linear ratio.
- `PARTIAL_COMPUTATION`: subtract only part of a composite.
- `ARITHMETIC_SLIP`: calculation error.

For the painted-cube template, distractors must come from miscounting which cubes have k painted faces.

---

## NUM_MS3_L1_075: Volume / Surface Area

```yaml
domain: Mensuration 3D
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - BASIC_3D
allowed_values:
    cube_edge: 4-15
    cylinder_r: 3-10
primary_trap: WRONG_METHOD
```

### Contract

Generate a question asking for the volume or surface area of a single solid.

### Allowed Variations

- cube, cuboid, cylinder, sphere

### Forbidden

- composite solids
- a non-integer answer (choose r as a multiple of 7 for cylinders)

### Validator Must Check

- the correct formula is applied and equals the correct option

### Example Skeleton

```text
A cube has edge 6 cm.
Question: Find its volume.
Answer: 216 cm³
```

---

## NUM_MS3_L2_076: Hollow / Composite

```yaml
domain: Mensuration 3D
difficulty_level: L2
tree_signature: [LEAF, FORMULA, FORMULA, OPERATION]
answer_mode: VALUE
required_operators:
    - HOLLOW_COMPOSITE
allowed_values:
    integer result
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question with a hollow or composite solid, asking for the material volume (outer minus inner).

### Allowed Variations

- hollow cylinder, sphere inside a cube

### Forbidden

- a non-integer result
- more than two component solids

### Validator Must Check

- outer minus inner computed and equals the correct option

### Example Skeleton

```text
A hollow cylinder has outer radius 6 cm, inner radius 4 cm, height 14 cm. (π = 22/7)
Question: Find the volume of material.
Answer: 880 cm³
```

---

## NUM_MS3_L2_077: Capacity With Efficiency

```yaml
domain: Mensuration 3D
difficulty_level: L2
tree_signature: [LEAF, MODIFIER]
answer_mode: VALUE
required_operators:
    - CAPACITY_EFFICIENCY
allowed_values:
    efficiency: {60, 70, 75, 80}%
primary_trap: SCALE_ERROR
```

### Contract

Generate a question asking how much a pump or machine delivers given a rate, an efficiency, and a time. Effective output = rate × efficiency × time.

### Allowed Variations

- pumps, machines, production lines

### Forbidden

- a feasibility constraint (that would be synthetic L3)
- a non-integer output

### Validator Must Check

- the effective output equals the correct option
- one distractor omits the efficiency factor

### Example Skeleton

```text
A pump delivers 600 L/h at 75% efficiency.
Question: How much does it deliver in 8 hours?
Answer: 3,600 L
```

---

## NUM_MS3_L3_078: Melting and Recasting

```yaml
domain: Mensuration 3D
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - MELT_RECAST
difficulty_source: volume conservation, counting by the ratio of cubes
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where a solid is melted and recast into smaller identical solids, asking how many are formed. The student conserves volume.

### Allowed Variations

- sphere into small spheres, cylinder into spheres

### Forbidden

- using a linear (radius) ratio instead of a volume ratio
- dimensions giving a non-integer count

### Validator Must Check

- volume conserved and the count equals the correct option
- one distractor uses the radius ratio without cubing

### Example Skeleton

```text
A solid sphere of radius 6 cm is melted and recast into small spheres of radius 1 cm.
Question: How many small spheres are formed?
Answer: 216
```

---

## NUM_MS3_L3_079: Painted Cube

```yaml
domain: Mensuration 3D
difficulty_level: L3
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - PAINTED_CUBE
difficulty_source: spatial classification of unit cubes by painted-face count
primary_trap: WRONG_METHOD
```

### Contract

Generate a question where a painted cube is cut into unit cubes, asking how many have exactly k painted faces. The student classifies by position (corner, edge, face, interior).

### Allowed Variations

- exactly 0, 1, 2, or 3 painted faces

### Forbidden

- confusing edge and face cubes in the intended solution
- a cube size below 3 (degenerate)

### Validator Must Check

- the position classification gives the count equal to the correct option
- one distractor confuses two position categories

### Example Skeleton

```text
A 4 cm cube is painted on all faces and cut into 1 cm cubes.
Question: How many have exactly 2 faces painted?
Answer: 24
```

---

# Domain Q: Data Interpretation — well-built, unchanged

## Domain Purpose

Test reading structured data, computing derived metrics, and making decisions or feasibility judgments from it.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `READ_COMPUTE` | Read values and perform one operation |
| `DERIVED_METRIC` | Compute a per-row metric then aggregate or compare |
| `MISSING_VALUE` | Infer a missing entry from a total |
| `CONSTRAINT_DECISION` | Filter options against binding constraints |
| `SENSITIVITY` | Recompute after a change and detect a ranking shift |
| `KPI_FEASIBILITY` | Project growth and test against a target |

## Domain-Wide Rules

- All data needed must be in the table; no outside knowledge.
- Choose figures so derived metrics are clean.
- Difficulty in L3 comes from binding constraints and re-ranking, not from bigger tables.

## Domain Option Rules

DI distractors must come from:

- `ARITHMETIC_SLIP`: read the right cells, calculation error.
- `PARTIAL_COMPUTATION`: aggregate the wrong subset.
- `IGNORED_CONSTRAINT`: pick an option that violates a constraint.
- `WRONG_METHOD`: compare the wrong metric.

---

## NUM_DI_L1_079: Read and Compute

```yaml
domain: Data Interpretation
difficulty_level: L1
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
required_operators:
    - READ_COMPUTE
primary_trap: ARITHMETIC_SLIP
```

### Contract

Generate a question requiring one read plus one operation from a small table (sum, single share).

### Allowed Variations

- total of a row, one share of a total

### Forbidden

- multi-step derivation

### Validator Must Check

- the single operation equals the correct option

### Example Skeleton

```text
Quarterly sales: ₹40L, ₹55L, ₹60L, ₹45L.
Question: What is the total annual sales?
Answer: ₹200L
```

---

## NUM_DI_L2_080: Multi-Step Derived Metric

```yaml
domain: Data Interpretation
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - DERIVED_METRIC
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question requiring a per-row metric (price × quantity) then an aggregation or comparison.

### Allowed Variations

- compute revenue per item then compare, count rows meeting a threshold

### Forbidden

- ignoring a row that should be included

### Validator Must Check

- the derived metric and aggregation equal the correct option

### Example Skeleton

```text
Item A: 200 units at ₹50. Item B: 150 units at ₹80.
Question: Which has higher revenue, and by how much?
Answer: B by ₹2,000
```

---

## NUM_DI_L2_081: Infer Missing Value

```yaml
domain: Data Interpretation
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - MISSING_VALUE
primary_trap: ARITHMETIC_SLIP
```

### Contract

Generate a question giving a total and all-but-one entries, asking for the missing one.

### Allowed Variations

- missing department, missing row total

### Forbidden

- more than one missing value

### Validator Must Check

- total minus known equals the correct option

### Example Skeleton

```text
Five departments total ₹500L; four are ₹80L, ₹120L, ₹90L, ₹110L.
Question: Find the fifth.
Answer: ₹100L
```

---

## NUM_DI_L3_082: Decision Under Constraint

```yaml
domain: Data Interpretation
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - CONSTRAINT_DECISION
difficulty_source: filter options against several constraints where the survivor is not obvious
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question with several options described by multiple attributes and a set of constraints, asking which qualify. The student eliminates by each constraint.

### Allowed Variations

- suppliers, projects, plans with cost/time/quality attributes

### Forbidden

- a constraint set that eliminates nothing (synthetic)
- more than one survivor unless intended

### Validator Must Check

- each constraint is applied and the qualifying option(s) equal the correct option
- one distractor ignores a binding constraint

### Example Skeleton

```text
Four suppliers by price and delivery time. Constraints: price ≤ ₹50, delivery ≤ 6 days.
Question: Which qualify?
Answer: A and D
```

---

## NUM_DI_L3_083: Sensitivity Analysis

```yaml
domain: Data Interpretation
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - SENSITIVITY
difficulty_source: recompute after a change and detect whether the ranking shifts
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where one figure changes by a stated percentage, asking whether the ranking changes. The student recomputes and re-ranks.

### Allowed Variations

- a revenue drop, a performance rise

### Forbidden

- a change too small to ever affect ranking (trivial)
- ambiguous ranking ties unless intended

### Validator Must Check

- the changed figure is recomputed and the re-ranking equals the correct option
- one distractor recomputes but misreads the new rank

### Example Skeleton

```text
Products A ₹100L, B ₹80L, C ₹60L, D ₹40L. If A drops 20%,
Question: does the ranking change?
Answer: Yes, B ties/overtakes A
```

---

## NUM_DI_L3_084: Feasibility to Hit a KPI

```yaml
domain: Data Interpretation
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: FEASIBILITY
required_operators:
    - KPI_FEASIBILITY
difficulty_source: project at max growth and test against a target that can genuinely fail
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question giving a current figure, a target, a maximum growth rate, and a number of periods, asking whether the target is reachable. The student projects and compares.

### Allowed Variations

- revenue, output, subscriber targets

### Forbidden

- a target trivially met or missed
- compounding errors in the projection

### Validator Must Check

- the projection at max growth is computed and the feasibility equals the correct option
- one distractor uses linear growth instead of compounding

### Example Skeleton

```text
Current revenue ₹42L, target ₹50L, max monthly growth 6%, 3 months left.
Question: Is it feasible?
Answer: Yes (₹50.02L)
```

---

# Domain R: Estimation & Approximation — capped at L2

## Domain Purpose

Test rounding, bounding, and approximate comparison.

## Domain note on level ceiling

Estimation's genuine skill is bounding and approximating — L1/L2 work. The old "robust decision across scenarios" L3 was synthetic. **This domain has no genuine L3**; do not generate one.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `ROUND` | Round to a stated place |
| `BOUNDS_CHOICE` | Evaluate options at both bounds and find the crossover |
| `APPROX_PRODUCT` | Approximate a product or ratio |

## Domain-Wide Rules

- Approximations must be defensible to the stated precision.
- Difficulty comes from reasoning about bounds, not from harder arithmetic.

## Domain Option Rules

Estimation distractors must come from:

- `REVERSE_DIRECTION`: round the wrong way.
- `PARTIAL_COMPUTATION`: evaluate at one bound only.
- `SCALE_ERROR`: misplace a magnitude.
- `ARITHMETIC_SLIP`: approximation error.

---

## NUM_EST_L1_085: Rounding

```yaml
domain: Estimation & Approximation
difficulty_level: L1
tree_signature: [LEAF, FORMULA]
answer_mode: VALUE
required_operators:
    - ROUND
primary_trap: REVERSE_DIRECTION
```

### Contract

Generate a question asking to round a number to a stated place.

### Allowed Variations

- nearest 10, 100, or whole number

### Forbidden

- ambiguous rounding direction

### Validator Must Check

- the rounded value equals the correct option

### Example Skeleton

```text
Round 347 to the nearest 100.
Answer: 300
```

---

## NUM_EST_L2_086: Bounds-Based Choice

```yaml
domain: Estimation & Approximation
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: COMPARISON
required_operators:
    - BOUNDS_CHOICE
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question with two options whose costs depend on a quantity that varies over a range, asking where one becomes cheaper. The student evaluates at both bounds and finds the crossover.

### Allowed Variations

- fixed price vs variable price, with or without a fixed fee

### Forbidden

- evaluating at one bound only
- options that never cross

### Validator Must Check

- both bounds evaluated and the crossover equals the correct option
- one distractor evaluates at a single bound

### Example Skeleton

```text
Cost is between ₹80 and ₹100. Option A is a fixed ₹90; Option B is cost + 5%.
Question: Where is B cheaper than A?
Answer: Below about ₹85.71
```

---

## NUM_EST_L2_087: Approximate Product or Ratio

```yaml
domain: Estimation & Approximation
difficulty_level: L2
tree_signature: [LEAF, OPERATION]
answer_mode: VALUE
required_operators:
    - APPROX_PRODUCT
primary_trap: SCALE_ERROR
```

### Contract

Generate a question asking for an approximate product, ratio, or percentage, to a stated precision.

### Allowed Variations

- approximate a product or a ratio

### Forbidden

- demanding an exact answer
- a magnitude that is easy to misplace without the approximation being the point

### Validator Must Check

- the approximation to the stated precision equals the correct option

### Example Skeleton

```text
Estimate 198 × 51 to the nearest thousand.
Answer: 10,000
```

---

# Domain S: Resource Allocation & Constraints — L3-heavy, unchanged

## Domain Purpose

Test budget and capacity allocation and multi-constraint optimization, feasibility, and trade-off decisions.

## Domain Operators

| Operator | Meaning |
| --- | --- |
| `BOUNDED_ALLOCATE` | Assign minimums then distribute the remainder |
| `CAPACITY_SPLIT` | Split a capacity by priority or proportion |
| `SUBSET_FEASIBILITY` | Find the combination meeting all constraints |
| `WEIGHTED_TRADEOFF` | Score options on weighted competing metrics |
| `OPTION_FILTER` | Filter concrete options against constraints |
| `LEVER_IMPACT` | Compute each lever's impact on a target |

## Domain-Wide Rules

- All constraints must be stated; the binding one should not be obvious in advance.
- Choose figures so allocations are clean.
- Difficulty comes from constraint interaction, not from more options.

## Domain Option Rules

Allocation distractors must come from:

- `IGNORED_CONSTRAINT`: satisfy capacity but violate another constraint.
- `PARTIAL_COMPUTATION`: use one metric only in a trade-off.
- `WRONG_METHOD`: confuse a margin lever with a revenue lever.
- `ARITHMETIC_SLIP`: calculation error.

---

## NUM_AL_L2_089: Budget With Min/Max Bounds

```yaml
domain: Resource Allocation & Constraints
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION, MODIFIER]
answer_mode: VALUE
required_operators:
    - BOUNDED_ALLOCATE
allowed_values:
    integer allocation
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question where a budget is allocated across items with minimums, and the remainder is distributed equally, asking the amount each receives.

### Allowed Variations

- equal distribution of the remainder

### Forbidden

- a remainder that does not divide evenly
- a binding max that turns this into L3

### Validator Must Check

- minimums assigned and remainder distributed; the per-item amount equals the correct option

### Example Skeleton

```text
Budget ₹100,000. Three departments, each with a ₹20,000 minimum; the remainder is split equally.
Question: How much does each receive?
Answer: ₹33,333
```

---

## NUM_AL_L2_090: Capacity Split

```yaml
domain: Resource Allocation & Constraints
difficulty_level: L2
tree_signature: [LEAF, OPERATION, OPERATION]
answer_mode: VALUE
required_operators:
    - CAPACITY_SPLIT
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question splitting a capacity by priority or by proportion, asking how much one party receives.

### Allowed Variations

- priority allocation, or proportional split

### Forbidden

- a split that does not resolve cleanly

### Validator Must Check

- the split rule is applied and the amount equals the correct option

### Example Skeleton

```text
Production capacity is 500 units/day. Line A needs 300, Line B needs 250, split by proportion.
Question: How much does Line A get?
Answer: 272
```

---

## NUM_AL_L3_091: Multi-Constraint Feasibility (Subset)

```yaml
domain: Resource Allocation & Constraints
difficulty_level: L3
tree_signature: [LEAF, OPERATION, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - SUBSET_FEASIBILITY
difficulty_source: several constraints where only one combination satisfies all; the binding one is not obvious
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question asking which combination or subset of items meets budget, ROI, size, or value constraints simultaneously. The student tests combinations against all constraints.

Keep this template distinct from NUM_AL_L3_093: this asks for a feasible **combination/subset**; 093 asks to pick a single valid **option** from a table.

### Allowed Variations

- projects within a budget, tasks within a time limit

### Forbidden

- a constraint set with no binding constraint (synthetic)
- more than one valid subset unless intended

### Validator Must Check

- each constraint is applied to candidate subsets and the feasible one equals the correct option
- one distractor satisfies the obvious constraint but violates another

### Example Skeleton

```text
100 hours. Tasks A(30h, value 50), B(40h, value 70), C(50h, value 80), D(20h, value 40).
At most 3 tasks, each value ≥ 45.
Question: Which combination maximizes value within 100 hours?
Answer: B + C (90h, value 150)
```

---

## NUM_AL_L3_092: Trade-Off Analysis

```yaml
domain: Resource Allocation & Constraints
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - WEIGHTED_TRADEOFF
difficulty_source: weighted scoring across two competing metrics
primary_trap: PARTIAL_COMPUTATION
```

### Contract

Generate a question with two options scored on two competing metrics with stated weights, asking which wins. The student computes a weighted score for each.

### Allowed Variations

- speed vs cost, quality vs price

### Forbidden

- one option dominating on both metrics (no trade-off)
- using a single metric as the intended method

### Validator Must Check

- weighted scores computed for both and the winner equals the correct option
- one distractor uses one metric only

### Example Skeleton

```text
Option Fast: 5 days, ₹50,000. Option Cheap: 9 days, ₹30,000. Weights: time 60%, cost 40%.
Question: Which wins?
Answer: Fast
```

---

## NUM_AL_L3_093: Pick Valid Option

```yaml
domain: Resource Allocation & Constraints
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - OPTION_FILTER
difficulty_source: filter four concrete options against three constraints; exactly one survives
primary_trap: IGNORED_CONSTRAINT
```

### Contract

Generate a question with four options described by several attributes and three constraints, asking which is valid. Exactly one survives all constraints.

Keep this template distinct from NUM_AL_L3_091: this is single-option selection from a table, not subset feasibility.

### Allowed Variations

- vendors, plans, candidates with attribute triples

### Forbidden

- more than one valid option unless intended
- a constraint that eliminates nothing

### Validator Must Check

- each option checked against every constraint; exactly one valid, equal to the correct option
- each distractor violates exactly one named constraint

### Example Skeleton

```text
Four vendors by price, delivery, and rating. Constraints: price ≤ ₹45, delivery ≤ 5 days, rating ≥ 4.0.
Question: Which qualifies?
Answer: A and D
```

---

## NUM_AL_L3_094: Lever Analysis

```yaml
domain: Resource Allocation & Constraints
difficulty_level: L3
tree_signature: [LEAF, MODIFIER, OPERATION, CONSTRAINT]
answer_mode: COMPARISON
required_operators:
    - LEVER_IMPACT
difficulty_source: compute each lever's impact on the target and pick the strongest
primary_trap: WRONG_METHOD
```

### Contract

Generate a question with several levers, each affecting a metric differently, asking which most improves a stated target. The student computes each lever's impact.

### Allowed Variations

- price, volume, and cost levers on revenue or profit

### Forbidden

- confusing a margin lever with a revenue lever in the intended solution
- a lever that trivially dominates

### Validator Must Check

- each lever's impact on the target computed; the best equals the correct option
- one distractor confuses a margin effect with a revenue effect

### Example Skeleton

```text
Revenue ₹100L. Levers: A (+10% price → +10% revenue), B (+5% volume → +5% revenue),
C (cut cost 8% → margin only).
Question: Which lever most increases revenue?
Answer: Lever A
```

---

# Closing Notes

## Domains capped below L3

- **L (Number Series)** and **R (Estimation)** have no genuine L3. Do not synthesize one by bolting on a constraint or an options framing. A series question with answer choices is still L2; an estimation question across scenarios is still L2.

## Domains left unchanged because already well-built

- **Q (Data Interpretation)** and **S (Resource Allocation)** were already structured around genuine binding constraints, so their templates were kept as-is.

## A note on template IDs

Some template IDs collide across levels (for example, a level-2 and a level-3 template sharing a trailing number, or two templates reusing 022/023 within a domain). The IDs here are preserved to match the question bank. Renumber them to be globally unique before this drives the live pipeline.

## The two failure modes this contract is designed to prevent

1. **Synthetic difficulty** — a non-binding constraint inflating an L2 into a fake L3. Caught by the strip test in the global rules: remove the constraint, and if what remains is already L2 and the constraint never binds, the question is not L3.
2. **Dirty answers** — parameters chosen to look plausible rather than to divide cleanly, producing an answer that matches no option (the ₹57,000 investment failure). Caught by the clean-answer rule: fix the structural parameters, compute the divisor the final step uses, and choose the free parameter as an exact multiple of it; then recompute and confirm the answer equals the marked option.

Together with a computational validation tier — recompute the answer from the tree, confirm option uniqueness and answer-type sanity in code before any language-model judgement — these rules keep generated questions both correctly levelled and correctly answered.

## Final Self-Check Before Returning Any Generated Question

Before returning the final generated item, silently verify:

1. The selected `template_id` is obeyed.
2. The `tree_signature` used matches the template exactly — no extra or missing node types.
3. The difficulty source is structural, not synthetic — stripping any constraint would change the answer.
4. The parameters obey the clean-answer rule and the answer terminates cleanly.
5. You solved the question yourself and the result exactly equals the value in `correct_option`.
6. Exactly one option is correct and all four options are distinct.
7. The answer type is sane (a count is a positive integer, a probability lies in [0,1], a percentage is reasonable, a distance is positive).
8. Each wrong option is a distinct, named mistake, and one encodes the template's `primary_trap`.
9. The explanation proves the answer from the question alone.
10. No forbidden pattern appears.

If any check fails, regenerate the item before returning it.