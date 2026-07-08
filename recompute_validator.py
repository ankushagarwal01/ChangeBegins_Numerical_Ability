"""
Recompute validator: the second pipeline gate after question_validator.py.
Given an item + its parameters + the template's solver, recomputes the answer in
code and rejects the item if the marked answer disagrees.

Registry maps template_id -> solver fn. Extend as solvers are written; a template
with no solver yet returns ('NO_SOLVER', None) so the pipeline can route it to
manual review rather than silently passing.
"""
import template_solvers as S
from fractions import Fraction

REGISTRY = {
  'NUM_CI_L2_138': S.solve_ci_compound,
  'NUM_CI_L1_137': S.solve_ci_compound,
  'NUM_CI_L2_113': S.solve_compare_si_ci,
  'NUM_MA_L2_109': S.solve_replacement,
  'NUM_MA_L3_110': S.solve_mix_two_ratios_equal,
  'NUM_MA_L3_111': S.solve_add_pure,
  'NUM_MA_L3_112': S.solve_alligation_volume,
  'NUM_PC_L3_098': S.solve_successive_pct,
  'NUM_PN_L3_122': S.solve_count_divisible_by_5,
  'NUM_PN_L3_123': S.solve_circular_adjacent,
  'NUM_PR_L3_124': S.solve_bayes,
  'NUM_RM_L1_067': S.solve_mod,
  'NUM_RM_L3_129': S.solve_mod_pow,
  'NUM_RM_L3_069': S.solve_crt_in_range,
  'NUM_PT_L2_047': S.solve_pipe_net,
}

def recompute_check(template_id, params, marked_answer, tol=0.05):
    """Return (status, computed). status in PASS / FAIL_MISMATCH / NO_SOLVER."""
    fn = REGISTRY.get(template_id)
    if fn is None:
        return ('NO_SOLVER', None)
    computed = fn(params)
    # normalise for comparison
    def val(x):
        if isinstance(x, tuple): return x
        try: return float(Fraction(x)) if not isinstance(x,(int,float)) else float(x)
        except Exception: return x
    c, m = val(computed), val(marked_answer)
    if isinstance(c, tuple) or isinstance(m, tuple):
        ok = c == m
    elif isinstance(c, float) and isinstance(m, float):
        ok = abs(c-m) <= tol
    else:
        ok = c == m
    return ('PASS' if ok else 'FAIL_MISMATCH', computed)

if __name__ == "__main__":
    # Demonstrate: feed each failing item its params + the WRONG marked answer,
    # confirm the recompute gate FAILS it (i.e. would have caught the bug).
    cases = [
      ('NUM_CI_L2_138', dict(P=8000,rate=12,years=2,freq=2), 2119.04),
      ('NUM_MA_L2_109', dict(c0=80,f=Fraction(1,4),n=3), 42.1875),
      ('NUM_MA_L3_111', dict(V=120,c0=25,ct=40), 40.0),
      ('NUM_PN_L3_123', dict(n=8), 8640),
      ('NUM_RM_L1_067', dict(a=247,n=13), 13),
      ('NUM_PT_L2_047', dict(rates=[12,8,-5],capacity=300), 15.0),
    ]
    print("Recompute gate on the originally-marked (wrong) answers:")
    for tid, params, wrong in cases:
        status, computed = recompute_check(tid, params, wrong)
        print(f"  {tid:<16} marked={wrong:<10} computed={str(computed):<10} -> {status}")
