# Numerical Templates — Complete Change Log

This document records every change made to the numerical templates, domain by domain and template by template. It covers three waves of work:

1. **The careful A–E redesign** — done one domain at a time, removing synthetic-difficulty L3 templates and replacing them with genuinely hard ones.
2. **The F–S sweep** — the same fix applied across the remaining domains, with capped domains (L, R) and unchanged domains (Q, S) identified.
3. **The renumbering** — trailing template numbers replaced with a globally unique 1–113 index, prefixes preserved.

**The governing principle throughout:** difficulty must be intrinsic to the computation-tree structure. A constraint that does not bind, or that is checked in one trivial line after the real work, is *synthetic* and does not make a template L3. The strip test: remove the constraint; if what remains is already L2 and the constraint never binds, the template was synthetic.

Legend: ⟳ = added, reclassified, or moved during the redesign. ✗ = removed. Current IDs use the final 1–113 numbering.

---

## Domain A — Ratios & Proportions
**Before:** 6 templates (2 L1, 2 L2, 2 L3) · **After:** 7 templates (2 L1, 2 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_RP_L1_001 | kept | Compute part from ratio and total | unchanged |
| NUM_RP_L1_002 | kept | Ratio scaling from a known part | unchanged |
| NUM_RP_L2_003 | kept | Chain ratios A:B and B:C | unchanged |
| NUM_RP_L2_004 | kept | Split total into 3+ parts | unchanged |
| — | ✗ removed | Allocation under cap/floor | Synthetic: once the ratio is computed, checking a cap is trivial. The constraint added a line, not cognitive load. |
| — | ✗ removed | Adjust one component and decide feasibility | Synthetic: adjustment is a simple step; the feasibility check is decorative. |
| NUM_RP_L3_005 | ⟳ added | Ratio change over time | Genuine L3: two ratio states linked by a fixed change require simultaneous equations. |
| NUM_RP_L3_006 | ⟳ added | Investment ratio with mid-period change | Genuine L3: time-weighting makes the effective ratio differ from the stated one. This is also the template that exposed the clean-answer bug (₹57,000 not divisible by capital-month weights). |
| NUM_RP_L3_007 | ⟳ added | Reverse ratio with replacement | Genuine L3: work backwards from a final ratio to an unknown removed amount. |

---

## Domain B — Percentages & Growth
**Before:** 6 templates (2 L1, 2 L2, 2 L3) · **After:** 7 templates (2 L1, 2 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_PC_L1_008 | kept | Percent of a number | unchanged |
| NUM_PC_L1_009 | kept | Percent change | unchanged |
| NUM_PC_L2_010 | kept | Reverse percentage | unchanged |
| NUM_PC_L2_011 | kept | Weighted percentage across groups | unchanged |
| — | ✗ removed | Two-lever trade-off (price × volume) | Synthetic: two multiplications and a comparison; no genuine insight. |
| — | ✗ removed | Multi-step growth planning with target | Synthetic: compound growth with a yes/no check bolted on. |
| NUM_PC_L3_012 | ⟳ added | Successive percentage changes | Genuine L3: changes compound on a running base; the additive answer is the trap. |
| NUM_PC_L3_013 | ⟳ added | Reverse-engineer original from multi-variable outcome | Genuine L3: two unknowns resolved backwards from an absolute margin. |
| NUM_PC_L3_014 | ⟳ added | Successive discounts and profit | Genuine L3: markup then two multiplicative discounts, profit measured on cost. |

---

## Domain C — Profit / Loss / Discount
**Before:** 6 templates (2 L1, 2 L2, 2 L3) · **After:** 7 templates (2 L1, 3 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_PL_L1_015 | kept | Profit or loss percentage | unchanged |
| NUM_PL_L1_016 | kept | Discount price | unchanged |
| NUM_PL_L2_017 | kept | Markup then discount | unchanged |
| NUM_PL_L2_018 | kept | Compare two offers | unchanged |
| NUM_PL_L2_019 | ⟳ added (L2) | Same selling price, one profit one loss | Kept at L2, not L3: the trick is well-known once seen; execution is two CP calculations and a comparison. You explicitly judged this an L2. |
| — | ✗ removed | Meet margin under cost increase and discount cap | Synthetic: new CP in one step, min SP in one formula, cap checked in one line. |
| — | ✗ removed | Optimize discount for revenue and margin targets | Synthetic: longer arithmetic, not harder reasoning. |
| NUM_PL_L3_020 | ⟳ added | Chain of transactions | Genuine L3: work backwards through two successive margins; adding margins is the trap. |
| NUM_PL_L3_021 | ⟳ added | False weight with markup | Genuine L3: two gain sources compound multiplicatively; most solvers count one. |

---

## Domain D — Averages & Weighted Mean
**Before:** 5 templates (1 L1, 2 L2, 2 L3) · **After:** 7 templates (1 L1, 3 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_AV_L1_022 | kept | Simple average | unchanged |
| NUM_AV_L2_023 | kept | Weighted average | unchanged |
| NUM_AV_L2_024 | kept | Replace one item | unchanged |
| NUM_AV_L2_025 | ⟳ added (L2) | Reverse average (missing value) | Stripped version of the old synthetic "hit target average with minimum bounds" L3; the bound was decorative, so the remainder lands at L2. |
| NUM_AV_L2_026 | ⟳ added (L2) | Reverse weighted average | Stripped version of the old "adjust subgroup mean" L3; you decided it sits at the L2/L3 boundary and placed it in L2 to balance counts. |
| — | ✗ removed | Hit target average with minimum bounds | Synthetic: stripped of the bound, reduces to a reverse average already near AV_021. |
| — | ✗ removed | Adjust subgroup mean to hit overall average | Synthetic: the bound check added nothing; the core is reverse weighted average. |
| NUM_AV_L3_027 | ⟳ added | Overlapping subgroups | Genuine L3: track three subgroup totals simultaneously; averaging the averages is the trap. |
| NUM_AV_L3_028 | ⟳ added | Average shift (batting average) | Genuine L3: must use totals; subtracting averages directly is the trap. |
| NUM_AV_L3_029 | ⟳ added | Unknown group size | Genuine L3: the group size is the unknown; set up and solve an equation. |

---

## Domain E — Mixtures & Allegations
**Before:** 5 templates (1 L1, 2 L2, 2 L3) · **After:** 7 templates (1 L1, 3 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_MA_L1_030 | kept | Final concentration after mixing | unchanged |
| NUM_MA_L2_031 | kept | Allegation ratio | unchanged |
| NUM_MA_L2_032 | kept | One-step replacement | unchanged |
| NUM_MA_L2_033 | ⟳ added (L2) | Multi-step replacement | Stripped version of the old synthetic "multi-step replacement feasibility" L3; repeated formula application lands at L2. |
| — | ✗ removed | Multi-step replacement feasibility | Synthetic: applying c×(1−f)^n repeatedly is an L2 extension, not L3. |
| — | ✗ removed | Choose plan meeting concentration and cost targets | Synthetic: the cost check and concentration check are independent; redundant with the stripped version. |
| NUM_MA_L3_034 | ⟳ added | Three sources, equal amounts | Genuine L3: convert ratios to fractions and combine under equal-weight mixing. |
| NUM_MA_L3_035 | ⟳ added | Add pure substance | Genuine L3: adding pure substance changes numerator and denominator together. |
| NUM_MA_L3_036 | ⟳ added | Reverse mixture | Genuine L3: two unknowns, two equations (volume and concentration). |

---

## Domain F — Simple & Compound Interest
**Before:** 6 templates · **After:** 7 templates (2 L1, 3 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_SI_L1_037 | kept | Simple interest | unchanged |
| NUM_CI_L1_038 | kept | Compound interest | unchanged |
| NUM_SI_L2_039 | kept | Simple interest with an unknown | unchanged |
| NUM_CI_L2_040 | kept | Compound interest with frequency | unchanged |
| NUM_CI_L2_041 | ⟳ moved to L2 | Compare two plans | Stripped from the old synthetic "compare plans by deadline" L3; two CI computations and a comparison are L2. |
| NUM_SI_L3_042 | ⟳ added | Doubling / tripling time | Genuine L3: derive the rate from a doubling, reuse for another multiple. |
| NUM_CI_L3_043 | ⟳ added | CI − SI difference | Genuine L3: use the closed form difference = P(R/100)² to solve backwards. |

---

## Domain G — Time & Work
**Before:** 6 templates · **After:** 7 templates (1 L1, 3 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_TW_L1_044 | kept | Single worker | unchanged |
| NUM_TW_L2_045 | kept | Two workers combined | unchanged |
| NUM_TW_L2_046 | kept | Start/stop times | unchanged |
| NUM_TW_L2_047 | ⟳ moved to L2 | Efficiency multiplier | Reclassified from L3: a single modifier on a rate plus a division, with no binding constraint, is L2. |
| NUM_TW_L3_048 | kept | Multi-phase with a binding cap | Genuine L3 (cap can actually bind). |
| NUM_TW_L3_049 | kept | Feasibility under availability | Genuine L3 (availability windows interact with rates). |
| NUM_TW_L3_050 | ⟳ added | Three-equation rate system | Genuine L3: solve a system from pairwise rates; averaging the pair-times is the trap. |

---

## Domain H — Time–Speed–Distance
**Before:** 6 templates · **After:** 6 templates (1 L1, 2 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_TSD_L1_051 | kept | Basic motion | unchanged |
| NUM_TSD_L2_052 | kept | Relative speed | unchanged |
| NUM_TSD_L2_053 | kept | Train crossing | unchanged |
| NUM_TSD_L3_054 | kept | Multi-segment routing | Genuine L3 (deadline can bind). |
| — | ✗ removed | Feasibility with two independent caps | Synthetic: the time cap and the fuel/distance cap don't interact; two independent checks. |
| NUM_TSD_L3_055 | kept | Optimize speed for arrival window | Genuine L3 (a real min–max band). |
| NUM_TSD_L3_056 | ⟳ added | Boats and streams system | Genuine L3: two equations, two unknowns (still-water and stream speed). Replaces the removed feasibility template. |

---

## Domain I — Pipes / Tanks / Flow
**Before:** 6 templates · **After:** 6 templates (1 L1, 3 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_PT_L1_057 | kept | One inlet one outlet | unchanged |
| NUM_PT_L2_058 | kept | Multiple inlets and outlets | unchanged |
| NUM_PT_L2_059 | kept | Two-phase fill | unchanged |
| NUM_PT_L2_060 | ⟳ moved to L2 | Three-phase fill | Stripped from the old synthetic three-phase-with-capacity L3; the capacity bound didn't bind, so phase tracking is L2. |
| NUM_PT_L3_061 | ⟳ added | Proportional-rate pipes | Genuine L3: set rates as r, 2r, 4r and solve. |
| NUM_PT_L3_062 | kept | Optimize schedule | Genuine L3 (cost/time trade-off where the cap eliminates the naive cheapest option). |

---

## Domain J — Permutations & Combinations
**Before:** 4 templates · **After:** 6 templates (1 L1, 3 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_PN_L1_063 | kept | Basic nPr / nCr | unchanged |
| NUM_PN_L2_064 | kept | Choose permutation vs combination | unchanged |
| NUM_PN_L2_065 | kept | Restricted arrangements | unchanged |
| NUM_PN_L2_066 | ⟳ moved to L2 | Multi-constraint counting (gap method) | Reclassified from L3: mechanical once the gap method is known; relative to genuine combinatorics this is L2. |
| NUM_PN_L3_067 | ⟳ added | Divisibility arrangement | Genuine L3: select digit sets meeting a divisibility rule, then permute. |
| NUM_PN_L3_068 | ⟳ added | Circular with restriction | Genuine L3: (n−1)! base adjusted for a together/apart rule. |

Note: this domain was under-built (only 4 templates). The additions both strengthen it and raise its genuine ceiling.

---

## Domain K — Probability
**Before:** 4 templates · **After:** 6 templates (1 L1, 2 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_PR_L1_069 | kept | Basic probability | unchanged |
| NUM_PR_L2_070 | kept | Complement / at-least-one | unchanged |
| NUM_PR_L2_071 | kept | Sequential draws | unchanged |
| NUM_PR_L3_072 | kept | Expected-value decision | Genuine L3. |
| NUM_PR_L3_073 | ⟳ added | Conditional / Bayes | Genuine L3: posterior from base rates and conditionals; ignoring base rates is the trap. Filled a gap (no conditional probability existed). |
| NUM_PR_L3_074 | ⟳ added | Conditional on an event | Genuine L3: restrict the sample space, then compute within it. |

---

## Domain L — Number Series & Patterns — CAPPED AT L2
**Before:** 4 templates · **After:** 4 templates (1 L1, 3 L2, no L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_NS_L1_075 | kept | AP / GP next term | unchanged |
| NUM_NS_L2_076 | kept | Mixed-operations series | unchanged |
| NUM_NS_L2_077 | kept | Alternating two-rule series | unchanged |
| NUM_NS_L2_078 | ⟳ moved to L2 | Rule identification | Reclassified from L3: choosing a rule from options is *easier*, since options can be tested. |

**Decision:** this domain has no genuine L3. Pattern recognition resolves in a single insight; it is not multi-step computation. Do not synthesize an L3 here.

---

## Domain M — Divisibility / HCF / LCM
**Before:** 5 templates · **After:** 5 templates (1 L1, 2 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_DV_L1_079 | kept | Divisibility check | unchanged |
| NUM_DV_L2_080 | kept | Apply LCM / HCF | unchanged |
| NUM_DV_L2_081 | kept | Prime factorization reasoning | unchanged |
| — | ✗ merged | Two near-identical "find number in range" L3s | The old find-in-range and optimize-min/max L3s were essentially the same LCM-then-filter problem; merged. |
| NUM_DV_L3_082 | ⟳ added | HCF–LCM product relation | Genuine L3: use the non-obvious product = HCF × LCM. |
| NUM_DV_L3_083 | ⟳ added | Common-remainder problem | Genuine L3: LCM plus a fixed offset, smallest in range. |

---

## Domain N — Remainders / Modular
**Before:** 5 templates · **After:** 5 templates (1 L1, 1 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_RM_L1_084 | kept | Simple remainder | unchanged |
| NUM_RM_L2_085 | kept | Remainder cycles | unchanged |
| NUM_RM_L3_086 | kept | CRT-style candidate | Genuine L3. |
| NUM_RM_L3_087 | ⟳ added | Large-power remainder | Genuine L3: reduce a large exponent via the cycle mod m. Filled a gap. |
| NUM_RM_L3_088 | ⟳ added | Last two digits | Genuine L3: cycle mod 100, longer than the mod-10 cycle. |

---

## Domain O — Mensuration 2D
**Before:** 5 templates · **After:** 5 templates (1 L1, 2 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_MS2_L1_089 | kept | Area / perimeter | unchanged |
| NUM_MS2_L2_090 | kept | Composite / missing dimension | unchanged |
| NUM_MS2_L2_091 | ⟳ moved to L2 | Cost with wastage | Stripped from the old synthetic "cost with wastage and budget" L3; the budget check was decorative. |
| NUM_MS2_L3_092 | ⟳ added | Path around a rectangle | Genuine L3: outer-minus-inner area with the dimension adjusted on both sides. |
| NUM_MS2_L3_093 | ⟳ added | Wire reshaped | Genuine L3: same perimeter, two shapes, compare areas. |

---

## Domain P — Mensuration 3D
**Before:** 5 templates · **After:** 5 templates (1 L1, 2 L2, 2 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_MS3_L1_094 | kept | Volume / surface area | unchanged |
| NUM_MS3_L2_095 | kept | Hollow / composite | unchanged |
| NUM_MS3_L2_096 | ⟳ moved to L2 | Capacity with efficiency | Stripped from the old synthetic "capacity with efficiency feasibility" L3; one modifier and a comparison is L2. |
| NUM_MS3_L3_097 | ⟳ added | Melting and recasting | Genuine L3: volume conservation, ratio of cubes. |
| NUM_MS3_L3_098 | ⟳ added | Painted cube | Genuine L3: spatial classification of unit cubes by painted-face count. |

---

## Domain Q — Data Interpretation — UNCHANGED (already well-built)
**Before:** 6 templates · **After:** 6 templates (1 L1, 2 L2, 3 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_DI_L1_099 | kept | Read and compute | unchanged |
| NUM_DI_L2_100 | kept | Multi-step derived metric | unchanged |
| NUM_DI_L2_101 | kept | Infer missing value | unchanged |
| NUM_DI_L3_102 | kept | Decision under constraint | Genuine L3. |
| NUM_DI_L3_103 | kept | Sensitivity analysis | Genuine L3. |
| NUM_DI_L3_104 | kept | Feasibility to hit a KPI | Genuine L3. |

**Decision:** this domain was already built around genuine binding constraints; no synthetic templates found. Left as-is.

---

## Domain R — Estimation & Approximation — CAPPED AT L2
**Before:** 3 templates (1 had a synthetic L3) · **After:** 3 templates (1 L1, 2 L2, no L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_EST_L1_105 | kept | Rounding | unchanged |
| NUM_EST_L2_106 | kept | Bounds-based choice | unchanged |
| NUM_EST_L2_107 | kept | Approximate product or ratio | unchanged |
| — | ✗ removed | Robust decision across scenarios | Synthetic: the scenario framing didn't add genuine multi-step reasoning. |

**Decision:** estimation's genuine skill is bounding and approximating — L1/L2 work. No genuine L3.

---

## Domain S — Resource Allocation & Constraints — UNCHANGED (already L3-heavy)
**Before:** 6 templates · **After:** 6 templates (2 L2, 4 L3)

| Current ID | Status | Template | Note |
|---|---|---|---|
| NUM_AL_L2_108 | kept | Budget with min/max bounds | unchanged |
| NUM_AL_L2_109 | kept | Capacity split | unchanged |
| NUM_AL_L3_110 | kept | Multi-constraint feasibility (subset) | Genuine L3. Disambiguated from 112: this asks for a feasible subset. |
| NUM_AL_L3_111 | kept | Trade-off analysis | Genuine L3. |
| NUM_AL_L3_112 | kept | Pick valid option | Genuine L3. Disambiguated from 110: single-option selection from a table. |
| NUM_AL_L3_113 | kept | Lever analysis | Genuine L3. Flagged as a candidate to scrutinize — its tree is genuine but shallow (concept-mapping more than computation). |

**Decision:** already structured around genuine binding constraints. Left as-is, with the 110/112 overlap clarified by note rather than change.

---

## Summary Across All Domains

| Domain | Before | After | Net | Synthetic L3s removed | Genuine L3s added |
|---|---|---|---|---|---|
| A Ratios | 6 | 7 | +1 | 2 | 3 |
| B Percentages | 6 | 7 | +1 | 2 | 3 |
| C Profit/Loss | 6 | 7 | +1 | 2 | 2 (+1 new L2) |
| D Averages | 5 | 7 | +2 | 2 | 3 (+2 stripped to L2) |
| E Mixtures | 5 | 7 | +2 | 2 | 3 (+1 stripped to L2) |
| F Interest | 6 | 7 | +1 | 1 | 2 |
| G Time & Work | 6 | 7 | +1 | 0 (1 moved to L2) | 1 |
| H TSD | 6 | 6 | 0 | 1 | 1 |
| I Pipes | 6 | 6 | 0 | 0 (1 moved to L2) | 1 |
| J P&C | 4 | 6 | +2 | 0 (1 moved to L2) | 2 |
| K Probability | 4 | 6 | +2 | 0 | 2 |
| L Number Series | 4 | 4 | 0 | capped at L2 | 0 |
| M Divisibility | 5 | 5 | 0 | merged 2→1 | 2 |
| N Remainders | 5 | 5 | 0 | 0 | 2 |
| O Mensuration 2D | 5 | 5 | 0 | 0 (1 moved to L2) | 2 |
| P Mensuration 3D | 5 | 5 | 0 | 0 (1 moved to L2) | 2 |
| Q Data Interpretation | 6 | 6 | 0 | 0 (unchanged) | 0 |
| R Estimation | 3 | 3 | 0 | 1, capped at L2 | 0 |
| S Resource Allocation | 6 | 6 | 0 | 0 (unchanged) | 0 |
| **Total** | **104** | **113** | **+9** | | |

## Two domains capped below L3
**L (Number Series)** and **R (Estimation)** — neither reaches genuine multi-step L3. Do not force an L3 by bolting on a constraint or an options framing.

## Two domains left unchanged because already well-built
**Q (Data Interpretation)** and **S (Resource Allocation)** — both already structured around genuine binding constraints.

## The renumbering
After the redesign, trailing template numbers carried collisions (e.g. an L2 and an L3 sharing a number). All IDs were renumbered to a globally unique 1–113 index in document order, with domain and level prefixes preserved. See `template_id_renumber_map.md` for the full old→new table.

## Note on the two failure modes the redesign targets
1. **Synthetic difficulty** — a non-binding constraint inflating an L2 into a fake L3. Removed wherever found; caught by the strip test.
2. **Dirty answers** — parameters chosen to look plausible rather than divide cleanly (the ₹57,000 investment bug). Addressed by the clean-answer rule in the contract. Note: this is a *generation-time* guarantee that must be enforced by validation code; the rule being written down does not enforce it, as the domain A generation collisions demonstrated.
