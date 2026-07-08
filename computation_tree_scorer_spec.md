# Computation-Tree Difficulty Scorer — Specification

**Purpose.** Turn a question's computation structure into a numeric difficulty score and an L1/L2/L3 level, so the generation pipeline can *verify* that a produced question actually matches the level its template intended. This is the quantitative companion to the qualitative framework in `numerical_template_contracts_v2.md`.

**Status note (read this first).** The original scorer implementation (the Mensuration-3D proof of concept) was lost to an environment reset. This specification is reconstructed from the worked-example scores recorded across the project. The *model* and the *strip test* below are faithful and reproduce the clean two- and three-layer examples exactly. The one piece that cannot be pinned with certainty is the leaf-layer counting constant for deep trees — the historical examples are themselves inconsistent about whether raw leaves are counted individually or folded into a flat base. Where an exact historical replica matters, reconcile this constant against the original implementation if it is ever recovered. The strip test — which is what actually drives the synthetic-vs-genuine decision — does not depend on that constant.

---

## The model

A question's computation is a tree of typed nodes arranged in depth layers.

Node types:

- **LEAF** — a raw given value; no computation.
- **OPERATION** — arithmetic on two or more values.
- **FORMULA** — a domain formula applied to inputs.
- **MODIFIER** — scales or transforms an intermediate value (efficiency factor, percentage adjustment, time-weighting).
- **CONSTRAINT** — resolves a comparison, cap, floor, feasibility, or optimization decision.

The tree is written in arrow notation, where each arrow advances one depth:

```
LEAF(a)+LEAF(b)+LEAF(c) -> FORMULA(...) -> MODIFIER(...) -> CONSTRAINT(...)
```

Depth starts at 1 for the leaf/input layer.

## The score

```
score = sum over each depth d of ( nodes_at_depth_d x d )  +  L3_BASE
```

`L3_BASE = 3` when the tree has intrinsic L3 structure, and `0` otherwise. Mechanically, a tree is L3-structured when it contains at least one CONSTRAINT node, **or** two or more MODIFIER nodes (two interacting sub-computations held simultaneously). This `+3` is the constant that appears in every L3 worked example, written there as the `(4x1+3)` head of the expression.

## Level bands

| Level | Score |
|---|---|
| L1 | ≤ 4 |
| L2 | 5 – 12 |
| L3 | ≥ 13 |

These bands are read off from where the project's worked examples fall.

---

## The strip test (the important part)

A high score is only *genuine* difficulty if the structure that produces it is doing real cognitive work. The recurring failure mode is a **synthetic** CONSTRAINT: a cap or feasibility check bolted onto the end of an otherwise-complete computation, which inflates the tree score (a CONSTRAINT sits deep, so it contributes heavily) without adding any reasoning a human would actually have to do.

The strip test detects this:

1. Score the tree as written.
2. Remove the trailing CONSTRAINT node and score again.
3. If the level **does not change**, the constraint was not solely responsible for the L3 status.
4. If the level **drops** (e.g. L3 → L2), the L3 status rested on that tail constraint — flag it for review.

**A crucial limit.** The strip test flags *candidates*, it does not deliver the verdict. Tree shape alone cannot tell whether a constraint binds — that is a semantic question ("does removing the constraint change the answer or the reasoning?"), which a structural scorer cannot answer. A genuinely hard template whose difficulty lives in interacting modifiers will *also* flag on strip, because removing its constraint drops the mechanical score too. So the tool narrows the field to the templates worth examining; the final synthetic-vs-genuine call is the human strip-test judgment, applied exactly as it was for TW_038 (cap never binds → synthetic) versus TW_039 (availability windows interact → genuine) below.

A CONSTRAINT earns its L3 status only if removing it changes the answer or the reasoning. This is the operational form of the synthetic-difficulty prohibition in the main contract — and it is verified by a human, with the scorer surfacing which templates to check.

---

## Worked calibration

The model reproduces the clean examples exactly:

| Template (example) | Tree shape | Score | Level |
|---|---|---|---|
| Chain ratios | 2 compute nodes over 2 depths | 3 | L2 |
| Split into 3+ parts | formula + operation | 4 | L2 |
| Markup then discount | 3 chained operations | 6 | L2 |
| One-step replacement | operation + formula | 5 | L2 |
| Remainder cycles | formula + 2 operations | 7 | L2 |
| Allocation under cap | leaves + modifier + **binding** constraint | 13 | L3 |
| Multi-step replacement | leaves + modifier + constraint | 13 | L3 |
| Decision under constraint | leaves + modifier + constraint | 14 | L3 |
| Lever analysis | leaves + 3 interacting modifiers + constraint | 25 | L3 |

## Applied result — the two Time & Work L3 templates

| Template | As written | Strip constraint | Verdict |
|---|---|---|---|
| Multi-phase with a cap (TW_038) | L3 | drops to L2 | **synthetic** — the day-cap never binds; reclassify to L2 or remove |
| Feasibility under availability (TW_039) | L3 | stays high on intrinsic structure | **genuine** — difficulty is in the interacting availability windows |

The score for TW_038 collapses when the cap is removed because the cap was the only thing pushing it over the L3 threshold; the phased-rate computation underneath is L2 work. TW_039's difficulty comes from the interacting sub-computations, not from a tail comparison, so stripping does not rescue it into being easy — it is genuinely hard.

---

## Integration notes (for the n8n pipeline)

- The scorer consumes the tree-expression string the item-writer already emits, so it slots in as a verification node between the LLM generation step and the database write.
- On each generated item: parse the tree, compute the score and level, and compare against the template's declared level. Flag mismatches for review rather than silently accepting them.
- Run the strip test at *template design* time, not per item — it is a property of the template's structure, not of individual parameter draws.
- The level bands and the `+3` constant are the two tunable numbers; hold them fixed once reconciled against the original implementation so scores stay comparable across runs.
