"""
Computation-Tree Difficulty Scorer  (ChangeBegins numerical aptitude)
=====================================================================

Turns a question's computation-tree expression into a difficulty score and an
L1/L2/L3 level, and provides a strip test to distinguish genuine L3 difficulty
from synthetic (bolted-on-constraint) difficulty.

Companion spec: computation_tree_scorer_spec.md

TREE NOTATION
-------------
Arrow-separated layers; each "->" (or unicode arrow) advances one depth.
Nodes within a layer are joined with "+". Depth starts at 1.

    LEAF(a)+LEAF(b)+LEAF(c) -> FORMULA(...) -> MODIFIER(...) -> CONSTRAINT(...)

Node types recognised: LEAF, OPERATION (or OP), FORMULA, MODIFIER, CONSTRAINT.

SCORE
-----
    score = sum over depth d of (nodes_at_depth_d * d)  +  L3_BASE
    L3_BASE = 3 when the tree is L3-structured
              (>=1 CONSTRAINT, or >=2 MODIFIER nodes).

LEVEL BANDS:  L1 <= 4    |    L2 5..12    |    L3 >= 13

NOTE: the leaf-counting constant for very deep trees is convention-dependent and
should be reconciled against the original implementation if recovered. The strip
test does not depend on it and is the basis for the synthetic/genuine decision.
"""

import re

_NODE_RE = re.compile(r'\b(LEAF|OPERATION|OP|FORMULA|MODIFIER|CONSTRAINT)\b')

L1_MAX = 4
L2_MAX = 12


def parse_layers(expr: str):
    """Parse a tree expression into a list of layers; each layer is a list of
    node-type tokens (OP normalised to OPERATION)."""
    parts = re.split(r'->|\u2192', expr)
    layers = []
    for part in parts:
        toks = ['OPERATION' if t == 'OP' else t for t in _NODE_RE.findall(part)]
        if toks:
            layers.append(toks)
    return layers


def is_l3_structure(layers) -> bool:
    """A tree is L3-structured if it has a binding-capable CONSTRAINT or two or
    more MODIFIER nodes (interacting sub-computations)."""
    flat = [t for layer in layers for t in layer]
    return flat.count('CONSTRAINT') >= 1 or flat.count('MODIFIER') >= 2


def score(expr: str) -> int:
    """Difficulty score for a tree expression."""
    layers = parse_layers(expr)
    body = sum(len(layer) * (depth + 1) for depth, layer in enumerate(layers))
    return body + (3 if is_l3_structure(layers) else 0)


def level(expr_or_score) -> str:
    """L1/L2/L3 from either a tree expression or a numeric score."""
    s = expr_or_score if isinstance(expr_or_score, int) else score(expr_or_score)
    if s <= L1_MAX:
        return "L1"
    if s <= L2_MAX:
        return "L2"
    return "L3"


def strip_test(expr: str):
    """Score the tree with a trailing CONSTRAINT-only layer removed.
    Returns (stripped_score, stripped_level). If the level drops versus the
    original, the constraint was synthetic."""
    layers = parse_layers(expr)
    if layers and set(layers[-1]) == {'CONSTRAINT'}:
        layers = layers[:-1]
    body = sum(len(layer) * (depth + 1) for depth, layer in enumerate(layers))
    s = body + (3 if is_l3_structure(layers) else 0)
    return s, level(s)


def audit(expr: str) -> dict:
    """Full report for one tree.

    IMPORTANT: `review_candidate` is NOT a verdict of synthetic difficulty. Tree
    shape alone cannot tell whether a constraint binds. A dropped level on strip
    only means the L3 status rests on a single tail constraint -- which is worth
    a human check. The actual synthetic/genuine call requires answering "does
    removing the constraint change the answer?", which is semantic, not
    structural. Genuine L3 templates whose difficulty lives in interacting
    modifiers will also flag here and must be cleared by that human check."""
    s = score(expr)
    lv = level(s)
    ss, sl = strip_test(expr)
    review_candidate = (lv == "L3" and sl != "L3")
    return {
        "score": s,
        "level": lv,
        "stripped_score": ss,
        "stripped_level": sl,
        "review_candidate": review_candidate,
    }


if __name__ == "__main__":
    examples = {
        "TW_038 multi-phase with cap":
            "LEAF(10,15,12)+LEAF(3)+LEAF(cap) -> OP -> OP -> MODIFIER -> CONSTRAINT",
        "TW_039 feasibility under availability":
            "LEAF(10,15,20)+LEAF(deadline)+LEAF(avail) -> MODIFIER -> OP -> CONSTRAINT",
        "RP_L2_003 chain ratios (genuine L2)":
            "LEAF(2:3)+LEAF(4:5) -> OP -> OP",
        "MA_L3_027 multi-step replacement (genuine L3)":
            "LEAF(80%)+LEAF(1/4)+LEAF(2) -> MODIFIER -> MODIFIER -> CONSTRAINT",
    }
    for name, expr in examples.items():
        r = audit(expr)
        tag = "  <-- REVIEW (does the constraint bind?)" if r["review_candidate"] else ""
        print(f"{name:<45} score={r['score']:>3} {r['level']}  "
              f"strip->{r['stripped_score']:>3} {r['stripped_level']}{tag}")
