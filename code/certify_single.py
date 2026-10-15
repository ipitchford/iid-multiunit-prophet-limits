"""Rigorous certification (python-flint arb ball arithmetic) that an explicit piecewise-constant quantile
policy for the Poissonised i.i.d. k-selection prophet problem guarantees ratio >= c, i.e.
   W(x) >= c * P_k(x)  for all x >= 0,
W(x) = int_0^1 sum_j pi_j(t) min(x, a_j(t)) dt (j = slots left), P_k(x) = k - e^{-x} sum_{r<k} (k-r) x^r / r!.
Input JSON: {"k": int, "T": int, "a": [[str fraction] * T] * k (row j-1 = j slots left), "c": str fraction}.
Method: per time interval of length h=1/T the state chain has constant generator Q; exp of the augmented
matrix [[Q^T?..]] gives both pi at the interval end and int pi over the interval exactly (as balls).
W is piecewise linear in x with breakpoints at the a-values; on each piece g = W - c P_k is convex
(P_k'' = -x^{k-1} e^{-x}/(k-1)! <= 0); tangent-line lower bounds at subinterval endpoints certify g >= 0."""
import hashlib, json, sys
from fractions import Fraction as Fr
import flint
from flint import arb, arb_mat
flint.ctx.prec = 256

def exact(q):
    if isinstance(q, bool) or not isinstance(q, (str, int, Fr)):
        raise ValueError("exact rational string, integer or Fraction required")
    return Fr(q)
def A(fr): fr = exact(fr); return arb(fr.numerator) / arb(fr.denominator)
def validate(spec, N):
    for name, value in [("N", N), ("k", spec["k"]), ("T", spec["T"])]:
        if type(value) is not int or value <= 0: raise ValueError(name + " must be a positive integer")
    a = spec["a"]
    if not (isinstance(a, list) and len(a) == spec["k"] and all(isinstance(r, list) and len(r) == spec["T"] for r in a)):
        raise ValueError("need k rows of T thresholds")
    if not all(exact(q) >= 0 for r in a for q in r): raise ValueError("thresholds must be nonnegative")
    if not (0 < exact(spec["c"]) < 1): raise ValueError("c must lie in (0,1)")

def interval_integrals(k, T, a):
    h = A(Fr(1, T)); n = k + 1
    pi = [arb(0)] * n; pi[k] = arb(1)                 # index = slots left
    I = [[arb(0)] * T for _ in range(n)]
    for c in range(T):
        # forward equation d pi/dt = M pi, M[j][j] = -a_j, M[j-1][j] = +a_j  (j>=1)
        M = [[arb(0)] * n for _ in range(n)]
        for j in range(1, n):
            r = A(a[j - 1][c]); M[j][j] -= r; M[j - 1][j] += r
        # augmented [[M, I],[0, 0]] * h ; exp gives [[e^{Mh}, int_0^h e^{Ms} ds],[0, I]]
        Aug = [[arb(0)] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            for j in range(n): Aug[i][j] = M[i][j] * h
            Aug[i][n + i] = h
        E = arb_mat(Aug).exp()
        newpi = [sum((E[i, j] * pi[j] for j in range(n)), arb(0)) for i in range(n)]
        for i in range(n):
            I[i][c] = sum((E[i, n + j] * pi[j] for j in range(n)), arb(0))
        pi = newpi
    return I, pi

def Pk(x, k):
    s = arb(0); term = arb(1); fact = arb(1)
    for r in range(k):
        if r > 0: term = term * x / r
        s += (k - r) * term
    return k - (-x).exp() * s

def dPk(x, k):
    s = arb(0); term = arb(1)
    for r in range(k):
        if r > 0: term = term * x / r
        s += term
    return (-x).exp() * s

def certify(spec, N=400):
    validate(spec, N)
    k, T, a, c = spec["k"], spec["T"], spec["a"], A(spec["c"])
    I, pend = interval_integrals(k, T, a)
    terms = [(Fr(a[j - 1][cc]), I[j][cc]) for j in range(1, k + 1) for cc in range(T)]   # (breakpoint, weight)
    bps = sorted(set(b for b, _ in terms))
    report = {"pieces": [], "ok": True}
    Winf = sum((w * A(b) for b, w in terms), arb(0))
    tail = Winf - c * k
    report["W_inf_minus_ck"] = tail.str(5); report["ok"] &= bool(tail > 0)
    beta0 = sum((w for _, w in terms), arb(0))
    d0 = beta0 - c
    report["g_prime_0"] = d0.str(5); report["ok"] &= bool(d0 > 0)
    pts = [Fr(0)] + bps
    for i in range(1, len(pts) - 1):
        l, u = pts[i], pts[i + 1]
        alpha = sum((w * A(b) for b, w in terms if b <= l), arb(0))
        beta = sum((w for b, w in terms if b >= u), arb(0))
        worst = None
        for s in range(N):
            xa = A(l + (u - l) * Fr(s, N)); xb = A(l + (u - l) * Fr(s + 1, N))
            ga = alpha + beta * xa - c * Pk(xa, k); gb = alpha + beta * xb - c * Pk(xb, k)
            da = beta - c * dPk(xa, k); db = beta - c * dPk(xb, k)
            lbL = ga + (da * (xb - xa) if not (da >= 0) else arb(0))
            lbR = gb - (db * (xb - xa) if not (db <= 0) else arb(0))
            lb = lbL if lbL.lower() > lbR.lower() else lbR
            if worst is None or lb.lower() < worst.lower(): worst = lb
        report["pieces"].append({"l": str(l), "u": str(u), "min_lower_bound": worst.lower().str(6)})
        report["ok"] &= bool(worst > 0)
    return report

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1])); rep = certify(spec, int(sys.argv[2]) if len(sys.argv) > 2 else 400)
    rep.update({"flint_version": flint.__version__, "prec_bits": flint.ctx.prec, "c": spec["c"], "k": spec["k"], "T": spec["T"], "input": sys.argv[1].split("/")[-1], "input_sha256": hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()})
    print(json.dumps(rep, indent=1))
    sys.exit(0 if rep["ok"] else 1)
