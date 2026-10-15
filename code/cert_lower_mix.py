"""Rigorous certification (python-flint arb) that a finite MIXTURE of piecewise-constant quantile policies for the
Poissonised i.i.d. k-selection prophet problem guarantees ratio >= c:  Wbar(x) = sum_i w_i W_i(x) >= c P_k(x) for all x >= 0.
W_i(x) = int_0^1 sum_j pi^i_j(t) min(x, a^i_j(t)) dt (j = slots left); P_k(x) = E min(Pois(x), k).
Input JSON: {"k": int, "T": int, "c": str, "policies": [{"w": str, "a": [[str]*T]*k}, ...]}, weights positive summing to 1.
Per policy and time piece, exp of the augmented generator gives pi at the piece end and int pi over the piece (balls).
Wbar is piecewise linear with breakpoints at the positive thresholds; g = Wbar - c P_k is convex on each piece (P_k concave);
tangent-line lower bounds on N subintervals per piece certify g >= 0; first piece via g(0)=0, g'(0)>0; tail via Wbar(inf) > c k."""
import hashlib, json, sys
from fractions import Fraction as Fr
import flint
from flint import arb, arb_mat
flint.ctx.prec = 256

def exact(q):
    if isinstance(q, bool) or not isinstance(q, (str, int, Fr)):
        raise ValueError("exact rational string, integer or Fraction required")
    return Fr(q)

def positive_integer(n, name):
    if type(n) is not int or n <= 0: raise ValueError(name + " must be a positive integer")

def A(fr): fr = exact(fr); return arb(fr.numerator) / arb(fr.denominator)

def validate(spec):
    k, T, pols = spec["k"], spec["T"], spec["policies"]
    positive_integer(k, "k"); positive_integer(T, "T")
    if not isinstance(pols, list) or not pols: raise ValueError("policies must be a nonempty list")
    ws = [exact(p["w"]) for p in pols]
    if not (all(w > 0 for w in ws) and sum(ws) == 1): raise ValueError("weights must be positive and sum to exactly 1")
    for p in pols:
        if not (isinstance(p["a"], list) and len(p["a"]) == k and all(isinstance(r, list) and len(r) == T for r in p["a"])): raise ValueError("each policy needs k rows of T thresholds")
        if not all(exact(q) >= 0 for r in p["a"] for q in r): raise ValueError("thresholds must be nonnegative")
    if not (0 < exact(spec["c"]) < 1): raise ValueError("c must lie in (0,1)")

def interval_integrals(k, T, a):
    h = A(Fr(1, T)); n = k + 1
    pi = [arb(0)] * n; pi[k] = arb(1)
    I = [[arb(0)] * T for _ in range(n)]
    for c in range(T):
        M = [[arb(0)] * n for _ in range(n)]
        for j in range(1, n):
            r = A(a[j - 1][c]); M[j][j] -= r; M[j - 1][j] += r
        Aug = [[arb(0)] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            for j in range(n): Aug[i][j] = M[i][j] * h
            Aug[i][n + i] = h
        E = arb_mat(Aug).exp()
        newpi = [sum((E[i, j] * pi[j] for j in range(n)), arb(0)) for i in range(n)]
        for i in range(n): I[i][c] = sum((E[i, n + j] * pi[j] for j in range(n)), arb(0))
        pi = newpi
    return I

def Pk(x, k):
    s = arb(0); term = arb(1)
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

def certify(spec, N=40):
    positive_integer(N, "N")
    validate(spec)
    k, T, c = spec["k"], spec["T"], A(spec["c"])
    agg = {}                                                    # breakpoint (Fraction > 0) -> total weight (arb)
    for p in spec["policies"]:
        w = A(p["w"]); I = interval_integrals(k, T, p["a"])
        for j in range(1, k + 1):
            for cc in range(T):
                b = Fr(p["a"][j - 1][cc])
                if b > 0: agg[b] = agg.get(b, arb(0)) + w * I[j][cc]
    bps = sorted(agg)                                           # Fractions: exact ordering
    wts = [agg[b] for b in bps]
    # prefix sums: alpha(l) = sum_{b <= l} w b ; beta(u) = sum_{b >= u} w
    alpha_pref = [arb(0)]
    for b, w in zip(bps, wts): alpha_pref.append(alpha_pref[-1] + w * A(b))
    beta_suf = [arb(0)] * (len(bps) + 1)
    for i in range(len(bps) - 1, -1, -1): beta_suf[i] = beta_suf[i + 1] + wts[i]
    rep = {"ok": True, "pieces": len(bps) - 1, "breakpoints": len(bps)}
    tail = alpha_pref[-1] - c * k; rep["W_inf_minus_ck"] = tail.str(6); rep["ok"] &= bool(tail > 0)
    d0 = beta_suf[0] - c; rep["g_prime_0"] = d0.str(6); rep["ok"] &= bool(d0 > 0)   # slope of Wbar at 0 is total weight; P_k'(0) = 1
    worst_all = None; worst_at = None
    for i in range(len(bps) - 1):
        l, u = bps[i], bps[i + 1]
        alpha = alpha_pref[i + 1]; beta = beta_suf[i + 1]        # on [l,u]: Wbar = sum_{b<=l} w b + x sum_{b>=u} w
        for s in range(N):
            xa = A(l + (u - l) * Fr(s, N)); xb = A(l + (u - l) * Fr(s + 1, N))
            ga = alpha + beta * xa - c * Pk(xa, k); gb = alpha + beta * xb - c * Pk(xb, k)
            da = beta - c * dPk(xa, k); db = beta - c * dPk(xb, k)
            lbL = ga + (da * (xb - xa) if not (da >= 0) else arb(0))
            lbR = gb - (db * (xb - xa) if not (db <= 0) else arb(0))
            lb = lbL if lbL.lower() > lbR.lower() else lbR
            if worst_all is None or lb.lower() < worst_all.lower(): worst_all, worst_at = lb, (str(l), str(u))
            if not (lb > 0): rep["ok"] = False
    rep["min_piece_lower_bound"] = worst_all.lower().str(6) if worst_all is not None else None
    rep["min_piece"] = worst_at
    return rep

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1])); rep = certify(spec, int(sys.argv[2]) if len(sys.argv) > 2 else 40)
    rep.update({"flint": flint.__version__, "prec": flint.ctx.prec, "c": spec["c"], "k": spec["k"], "T": spec["T"],
                "n_policies": len(spec["policies"]), "input": sys.argv[1].split("/")[-1],
                "input_sha256": hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()})
    print(json.dumps(rep, indent=1)); sys.exit(0 if rep["ok"] else 1)
