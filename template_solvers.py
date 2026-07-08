"""
Template solvers for the ChangeBegins numerical bank.

Each template gets:
  solve(params)      -> the correct answer, computed deterministically in code
  gen_params(rng)    -> a clean-answer parameter set (backward-generated where needed)

solve() is the RECOMPUTE VERIFIER: the pipeline runs it on an item's parameters and
rejects the item unless the marked answer equals solve()'s output.
gen_params() is the CLEAN-ANSWER GENERATOR: it supplies parameters that make the
answer land exactly, so the LLM only renders wording.

Verified against the known-correct answers stated in the flagged-question batch.
"""
from fractions import Fraction
import random, math

# ---------- Compound / Simple Interest ----------
def solve_ci_compound(p):
    """CI compounded n times/year. params: P, rate_annual_pct, years, freq_per_year."""
    P, r, t, f = p['P'], p['rate'], p['years'], p.get('freq', 1)
    amount = P * (1 + (r/100)/f) ** (f*t)
    return round(amount - P, 2)

def solve_si(p):
    return round(p['P'] * p['rate'] * p['years'] / 100, 2)

def solve_compare_si_ci(p):
    """Plan A simple vs Plan B compound. Returns (winner, margin)."""
    a = p['PA'] * (1 + p['rA']*p['years']/100)               # simple: P(1+rt/100)
    b = p['PB'] * (1 + p['rB']/100) ** p['years']            # compound
    if a >= b: return ('A', round(a-b, 2))
    return ('B', round(b-a, 2))

# ---------- Mixtures ----------
def solve_replacement(p):
    """Drain fraction f, refill with water, n times. params: c0(%), f, n."""
    return round(p['c0'] * (1 - p['f'])**p['n'], 4)

def solve_mix_two_ratios_equal(p):
    """Two alloys mixed in equal amounts; each given as gold:other. Fraction gold."""
    g1 = Fraction(p['a1'], p['a1']+p['b1'])
    g2 = Fraction(p['a2'], p['a2']+p['b2'])
    return (g1 + g2) / 2           # equal amounts -> average of fractions

def solve_add_pure(p):
    """Add x mL pure solute to V mL of c0% to reach target%. Return x."""
    V, c0, ct = p['V'], p['c0'], p['ct']
    # (c0/100*V + x) / (V + x) = ct/100  ->  x = V(ct-c0)/(100-ct)
    return round(V*(ct-c0)/(100-ct), 4)

def solve_alligation_volume(p):
    """Mix c_low% and c_high% to make V of target%. Return litres of the LOW solution."""
    cl, ch, ct, V = p['c_low'], p['c_high'], p['ct'], p['V']
    # x*cl + (V-x)*ch = V*ct  -> x = V(ch-ct)/(ch-cl)
    return round(V*(ch-ct)/(ch-cl), 4)

# ---------- Percentages ----------
def solve_successive_pct(p):
    """Net % change from a list of successive % changes."""
    factor = 1.0
    for c in p['changes']:
        factor *= (1 + c/100)
    return round((factor - 1)*100, 4)

# ---------- Permutations / Counting ----------
def solve_count_divisible_by_5(p):
    """k-digit codes from given distinct digits, no repeat, divisible by 5.
    Last digit must be 5 (or 0) if present in the set."""
    digits = p['digits']; k = p['length']
    endings = [d for d in digits if d % 5 == 0]
    if not endings: return 0
    n = len(digits)
    # last position: len(endings) choices; remaining k-1 from n-1 distinct
    perm = math.perm(n-1, k-1)
    return len(endings) * perm

def solve_circular_adjacent(p):
    """n people around a circle, 2 specified must sit together.
    (n-1)! ... treat pair as unit: (n-1-1)! * 2 = (n-2)!*2."""
    n = p['n']
    return math.factorial(n-2) * 2

# ---------- Probability (Bayes) ----------
def solve_bayes(p):
    """P(source A | defective). params: pA, dA, pB, dB (fractions of 1)."""
    num = p['pA']*p['dA']
    den = p['pA']*p['dA'] + p['pB']*p['dB']
    return round(num/den, 3)

# ---------- Remainders / Modular ----------
def solve_mod(p):
    return p['a'] % p['n']

def solve_mod_pow(p):
    return pow(p['base'], p['exp'], p['mod'])

def solve_crt_in_range(p):
    """Smallest / all solutions x in [lo,hi] with x % m_i == r_i."""
    lo, hi = p['lo'], p['hi']
    sols = [x for x in range(lo, hi+1)
            if all(x % m == r for m, r in p['congruences'])]
    return sols

# ---------- Pipes ----------
def solve_pipe_net(p):
    """Net fill time. params: rates (list, + fill / - drain), capacity."""
    net = sum(p['rates'])
    return round(p['capacity']/net, 4) if net > 0 else None


# =====================  VERIFICATION  =====================
if __name__ == "__main__":
    checks = [
      ("CI_138 half-yearly", solve_ci_compound, dict(P=8000,rate=12,years=2,freq=2), 2099.82),
      ("MA_109 replacement", solve_replacement, dict(c0=80,f=Fraction(1,4),n=3), 33.75),
      ("MA_110 two ratios",  solve_mix_two_ratios_equal, dict(a1=3,b1=5,a2=7,b2=9), Fraction(13,32)),
      ("MA_111 add pure",    solve_add_pure, dict(V=120,c0=25,ct=40), 30.0),
      ("MA_112 alligation",  solve_alligation_volume, dict(c_low=20,c_high=60,ct=35,V=80), 50.0),
      ("PC_098 successive",  solve_successive_pct, dict(changes=[20,-10,15]), 24.2),
      ("PN_122 div by 5",    solve_count_divisible_by_5, dict(digits=[1,2,4,5,7],length=3), 12),
      ("PN_123 circular adj",solve_circular_adjacent, dict(n=8), 1440),
      ("PR_124 bayes",       solve_bayes, dict(pA=0.6,dA=0.05,pB=0.4,dB=0.08), 0.484),
      ("RM_067 mod",         solve_mod, dict(a=247,n=13), 0),
      ("RM_129 mod pow",     solve_mod_pow, dict(base=7,exp=145,mod=25), 7),
      ("CI_113 compare",     solve_compare_si_ci, dict(PA=2000,rA=5,PB=1500,rB=8,years=3), ('A',410.43)),
      ("PT_047 pipe net",    solve_pipe_net, dict(rates=[12,8,-5],capacity=300), 20.0),
    ]
    print(f"{'template':<22}{'computed':<16}{'expected':<16}{'ok'}")
    allok=True
    for name, fn, params, exp in checks:
        got = fn(params)
        # compare with tolerance / fraction awareness
        if isinstance(exp, tuple):
            ok = got[0]==exp[0] and abs(got[1]-exp[1])<0.5
        elif isinstance(exp, Fraction):
            ok = Fraction(got).limit_denominator(10000)==exp
        else:
            ok = abs(float(got)-float(exp))<0.05
        allok &= ok
        print(f"{name:<22}{str(got):<16}{str(exp):<16}{'OK' if ok else 'XX'}")
    print("\nALL SOLVERS CORRECT:", allok)
