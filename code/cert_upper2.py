"""Certified UPPER bound on the continuum two-unit i.i.d. prophet ratio R(v) = V_2(0) / int v dP_2 for an explicit
step profile given by a layer measure: points 0 < x_1 < ... < x_M with weights nu_j > 0, v(s) = sum_{x_j >= s} nu_j,
i.e. level v_m = sum_{j >= m} nu_j on (x_{m-1}, x_m] (x_0 = 0) and v = 0 beyond x_M.  python-flint arb.
Continuum DP (t in [0,1]): V_0 = 0, V_j(1) = 0, V_j' = -Psi(V_j - V_{j-1}), Psi(tau) = sum_m (x_m - x_{m-1}) (v_m - tau)^+.
Backward barriers (Delta = 1/N): Phi_1 = Phi_1' + Delta Psi(Phi_1'), Phi_2 = Phi_2' + Delta Psi(Phi_2' - Phi_1)  (primes:
values at t_{i+1}; Phi_1 at t_i), rounded up.  Then V_1 <= Phi_1 and V_2 <= Phi_2 (Lemma: comparison, Psi nonincreasing).
Benchmark: int v dP_2 = sum_j nu_j P_2(x_j), P_2(x) = E min(Pois(x), 2) = 2 - e^{-x} (2 + x)."""
import hashlib, json, sys
from fractions import Fraction as Fr
import flint
from flint import arb
flint.ctx.prec = 200
def exact(q):
    if isinstance(q, bool) or not isinstance(q, (str, int, Fr)):
        raise ValueError("exact rational string, integer or Fraction required")
    return Fr(q)
def A(q):
    f = exact(q); return arb(f.numerator) / arb(f.denominator)

def validate(spec):
    if not isinstance(spec["x"], list) or not isinstance(spec["nu"], list): raise ValueError("x and nu must be lists")
    x = [exact(q) for q in spec["x"]]; nu = [exact(q) for q in spec["nu"]]
    if not (len(x) == len(nu) and len(x) >= 1): raise ValueError("need matching x and nu")
    if not (x[0] > 0 and all(x[i] < x[i + 1] for i in range(len(x) - 1))): raise ValueError("x must be positive and strictly increasing")
    if not all(w > 0 for w in nu): raise ValueError("nu must be positive")
    if not (0 < exact(spec.get("claim", "0.8372914")) < 1): raise ValueError("claim must lie in (0,1)")

def certify(spec, N):
    if type(N) is not int or N <= 0: raise ValueError("N must be a positive integer")
    validate(spec)
    x = [A(q) for q in spec["x"]]; nu = [A(q) for q in spec["nu"]]; M = len(x)
    v = [sum(nu[j:], arb(0)) for j in range(M)]                       # levels v_m on (x_{m-1}, x_m]
    ds = [x[0]] + [x[m] - x[m - 1] for m in range(1, M)]
    def Psi(tau):
        F = arb(0)
        for m in range(M):
            d = v[m] - tau
            if d > 0: F += ds[m] * d
            elif not (d <= 0): F += ds[m] * arb(d.upper())            # straddling ball: upper endpoint (valid upper bound)
        return F
    D = arb(1) / N; P1 = arb(0); P2 = arb(0)
    for i in range(N - 1, -1, -1):
        P1n = arb((P1 + D * Psi(P1)).upper())                          # Phi_1 at t_i
        P2 = arb((P2 + D * Psi(P2 - P1n)).upper())                     # uses Phi_2(t_{i+1}) and Phi_1(t_i)
        P1 = P1n
    B = sum((nu[j] * (2 - (-x[j]).exp() * (2 + x[j])) for j in range(M)), arb(0))
    R = P2 / B
    return {"V2_0_upper": P2.str(12), "V1_0_upper": P1.str(12), "benchmark": B.str(12), "ratio_upper": arb(R.upper()).str(10),
            "claimed_upper": spec.get("claim", "0.8372914"), "below_claim": bool(R < A(spec.get("claim", "0.8372914"))), "steps": N, "M": M}

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1])); out = certify(spec, int(sys.argv[2]) if len(sys.argv) > 2 else 40000)
    out.update({"flint": flint.__version__, "prec": flint.ctx.prec, "input": sys.argv[1].split("/")[-1],
                "input_sha256": hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()})
    print(json.dumps(out, indent=1)); sys.exit(0 if out["below_claim"] else 1)
