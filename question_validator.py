"""
Question validator for the ChangeBegins numerical bank.
Structural checks requiring no template knowledge. Conservative: only flags what
it can establish with confidence, to avoid false positives.
"""
import json, re
from fractions import Fraction

CUR = '$£₹'

def is_pure_number(s):
    """True if the option is essentially just a numeric value / ratio / currency /
    percentage, not a sentence."""
    t = s.strip()
    # allow leading currency, digits, commas, dot, %, ratio a:b, fraction a/b, 'approx'
    t2 = re.sub(r'(?i)\bapprox(imately)?\b', '', t).strip()
    return bool(re.fullmatch(r'[\$£₹]?\s*-?\d[\d,]*\.?\d*\s*%?', t2)) or \
           bool(re.fullmatch(r'-?\d+\s*[:/]\s*\d+', t2))

def num_value(s):
    t = re.sub(r'[,\s%'+CUR+r']', '', s)
    m = re.fullmatch(r'(-?\d+)[:/](\d+)', t)
    if m:
        try: return round(float(Fraction(int(m.group(1)), int(m.group(2)))),4)
        except ZeroDivisionError: return None
    m = re.fullmatch(r'-?\d+\.?\d*', t)
    return round(float(m.group()),4) if m else None

def norm_text(s):
    return re.sub(r'\s+',' ', s.strip().lower())

def option_key(s):
    if is_pure_number(s):
        v = num_value(s)
        if v is not None:
            return ('num', v)
    return ('txt', norm_text(s))

def last_value_in(expl):
    """The final numeric value the explanation lands on."""
    if not expl: return None
    nums = re.findall(r'-?\d[\d,]*\.?\d*\s*/\s*\d+|-?\d[\d,]*\.?\d*', expl)
    if not nums: return None
    return num_value(nums[-1])

def validate(q):
    issues=[]
    opts=q['options']

    # duplicate options — only collapse pure-numbers by value; sentences by exact norm text
    seen={}
    for o in opts:
        k=option_key(o['text'])
        if k in seen:
            issues.append(("DUPLICATE_OPTIONS", f"{seen[k]} & {o['label']} both = {o['text']!r}"))
        else:
            seen[k]=o['label']

    ncorrect=sum(1 for o in opts if o.get('is_correct'))
    if ncorrect!=1:
        issues.append(("BAD_CORRECT_COUNT", f"{ncorrect} flagged correct"))

    # key matches explanation — ONLY for pure-number keyed options (sentence answers
    # can't be reduced to one trailing number reliably)
    keyed=next((o for o in opts if o.get('is_correct')),None)
    if keyed and is_pure_number(keyed['text']):
        kv=num_value(keyed['text']); ev=last_value_in(q.get('correct_answer_explanation',''))
        if kv is not None and ev is not None and abs(kv-ev)>0.01:
            alt=next((o['label'] for o in opts
                      if is_pure_number(o['text']) and num_value(o['text']) is not None
                      and abs(num_value(o['text'])-ev)<0.01), None)
            issues.append(("KEY_EXPLANATION_MISMATCH",
                f"expl lands {ev}, keyed {keyed['label']}={kv}"+(f", matches {alt}" if alt else ", matches none")))
    return issues

if __name__=="__main__":
    data=json.load(open('/mnt/user-data/uploads/restructured_questions.json'))
    from collections import Counter
    tally=Counter(); caught=0
    for q in data:
        iss=validate(q)
        if iss: caught+=1
        for t,_ in iss: tally[t]+=1
    print("=== structural catches ===")
    for t,c in tally.most_common(): print(f"  {c:>3}  {t}")
    print(f"\ncaught structurally: {caught}/49 | pure-compute (need recompute): {49-caught}")

# ---------------------------------------------------------------------------
# Pipeline usage:
#   from question_validator import validate
#   issues = validate(question_dict)   # -> list of (TAG, message); empty = passes structural checks
#
# Checks performed (no template knowledge needed):
#   DUPLICATE_OPTIONS        two options equal (pure numbers compared by value)
#   BAD_CORRECT_COUNT        not exactly one option flagged correct
#   KEY_EXPLANATION_MISMATCH keyed numeric answer != value the explanation derives
#
# NOT covered (needs the clean-answer / recompute layer, i.e. actually solving the
# item from its parameters): pure arithmetic errors where the explanation itself
# contains the wrong math. Those require template-specific solvers, not structural
# checks. Run this validator as a first gate; route anything it passes to the
# recompute validator before accepting.
