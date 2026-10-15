"""Rigorous upper bound on theta_1* + theta_2* for the BPV k=2 system (python-flint arb).
G2(u) = (1+u)e^{-u}, G3(u) = (u^2+2u+2)e^{-u}; z = G2(u) in (0,1]; H(z) = 2 - G3(G2^{-1}(z)), decreasing in z.
(1) theta_2* is the unique root of T(theta) = int_0^inf u e^{-u}/(1/theta - 2 + G3(u)) du = 1 (T increasing).
(2) z_2' = H(z_2) - 1/theta_2*, z_1' = H(z_1) - r* f(t), f = 2 - G3(u_2) in [0,2] increasing in u_2;
    z_j(0)=1 and z_j -> 0 as t -> 1. Sub-solution barriers phi_2 (with 1/theta_lo) and phi_1 (with r_lo and an
    upper envelope of f) staying positive at t=1 prove r* > r_lo."""
import math, json, sys
from fractions import Fraction as Fr
import flint
from flint import arb, acb
flint.ctx.prec = 200
def exact(q):
    if isinstance(q, bool) or not isinstance(q, (str, int, Fr)):
        raise ValueError("exact rational string, integer or Fraction required")
    return Fr(q)
def positive_integer(n, name):
    if type(n) is not int or n <= 0: raise ValueError(name + " must be a positive integer")
def theta_value(q):
    q = exact(q)
    if not 0 < q < Fr(1, 2): raise ValueError("theta must lie in (0,1/2)")
    return q
def A(q): q = exact(q); return arb(q.numerator) / arb(q.denominator)
G2 = lambda u: (1 + u) * (-u).exp()
G3 = lambda u: (u * u + 2 * u + 2) * (-u).exp()

def T_enclosure(theta, U=60):
    theta_value(theta); positive_integer(U, "U")
    th = A(theta)
    f = lambda u, _: u * (-u).exp() / (1 / th - 2 + (u * u + 2 * u + 2) * (-u).exp())
    I = acb.integral(f, 0, U).real
    tail_hi = (arb(U) + 1) * (-arb(U)).exp() / (1 / th - 2)
    return I, I + tail_hi            # T in [I, I + tail]

def u_lower(z):   # rational u with G2(u) >= z certified  => u <= G2^{-1}(z)
    if not (arb(z) > 0 and arb(z) <= 1): raise ValueError("inverse argument must be certified in (0,1]")
    zf = float(z.mid()) if isinstance(z, arb) else float(z)
    if zf >= 1: return Fr(0)
    lo, hi = 0.0, 100.0
    for _ in range(80):
        m = (lo + hi) / 2
        if (1 + m) * math.exp(-m) > zf: lo = m
        else: hi = m
    u = Fr(lo).limit_denominator(10**12) - Fr(1, 10**9)
    u = max(u, Fr(0))
    for _ in range(1000):
        if G2(A(u)) >= z: return u
        u -= Fr(1, 10**8)
    raise RuntimeError("could not certify lower inverse proposal")

def u_upper(z):   # rational u with G2(u) <= z certified  => u >= G2^{-1}(z)
    if not (arb(z) > 0 and arb(z) <= 1): raise ValueError("inverse argument must be certified in (0,1]")
    zf = float(z.mid()) if isinstance(z, arb) else float(z)
    lo, hi = 0.0, 200.0
    for _ in range(80):
        m = (lo + hi) / 2
        if (1 + m) * math.exp(-m) > zf: lo = m
        else: hi = m
    u = Fr(hi).limit_denominator(10**12) + Fr(1, 10**9)
    for _ in range(1000):
        if G2(A(u)) <= z: return u
        u += Fr(1, 10**8)
    raise RuntimeError("could not certify upper inverse proposal")

def barrier(theta_lo, r_lo, N):
    positive_integer(N, "N"); theta_value(theta_lo)
    if exact(r_lo) <= 0: raise ValueError("r_lo must be positive")
    h = A(Fr(1, N)); K2 = 1 / A(theta_lo); rr = A(r_lo)
    phi2 = [arb(1)]; dead2 = None
    for i in range(N):                                  # phi_2: slope = min(0, lower H(phi2_i) - 1/theta_lo)
        p = phi2[-1]
        if not (p > 0): phi2.append(arb(-1)); dead2 = dead2 or i; continue
        Hlo = 2 - G3(A(u_lower(p))).upper()             # lower bound of H(p)
        s = Hlo - K2
        s_lo = s.lower()                                 # exact lower endpoint; any slope <= it is valid
        s = s_lo if s_lo < 0 else arb(0)
        phi2.append((p + s * h).lower())
    phi1 = [arb(1)]
    for i in range(N):                                  # phi_1 with K(t) <= r_lo * fbar(t_{i+1})
        p = phi1[-1]
        if not (p > 0): return phi2, phi1, False
        q = phi2[i + 1]
        fbar = arb(2) if not (q > 0) else (2 - G3(A(u_upper(q))).lower()).upper()
        Hlo = 2 - G3(A(u_lower(p))).upper()
        s = Hlo - rr * fbar
        s_lo = s.lower()                                 # exact lower endpoint; any slope <= it is valid
        s = s_lo if s_lo < 0 else arb(0)
        phi1.append((p + s * h).lower())
    return phi2, phi1, bool(phi1[-1] > 0)

if __name__ == "__main__":
    th_lo, th_hi, r_lo, N = Fr("0.48300"), Fr("0.48302"), Fr("1.37"), int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    positive_integer(N, "N")
    Tlo = T_enclosure(th_lo); Thi = T_enclosure(th_hi)
    ok_theta = bool(Tlo[1] < 1) and bool(Thi[0] > 1)
    phi2, phi1, ok_r = barrier(th_lo, r_lo, N)
    bound = A(th_hi) * (1 + 1 / A(r_lo))
    out = {"T(theta_lo)_upper": Tlo[1].str(10), "T(theta_hi)_lower": Thi[0].str(10), "theta2_bracket_certified": ok_theta,
           "barrier_steps": N, "phi2_at_1": phi2[-1].str(8), "phi1_at_1": phi1[-1].str(8), "r_star_gt_r_lo_certified": ok_r,
           "sum_theta_upper_bound": bound.str(10), "sum_theta_lt_0.8365": bool(bound < A("0.8365")) and ok_theta and ok_r,
           "sum_theta_lt_0.835590": bool(bound < A("0.835590")) and ok_theta and ok_r,
           "theta_lo": str(th_lo), "theta_hi": str(th_hi), "r_lo": str(r_lo), "flint": flint.__version__, "prec": flint.ctx.prec}
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["sum_theta_lt_0.835590"] else 1)
