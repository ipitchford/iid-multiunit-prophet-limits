"""Double oracle for the continuum k-unit i.i.d. prophet game (pilot, floating point).
Adversary: layer measure nu >= 0 on a grid xs with sum nu P_k = 1 (profile v(s) = nu((s, inf))).
Decider: mixtures of quantile policies A (k x T thresholds, j = units left). Payoff sum_x nu_x W^A(x).
LP over nu against the current policy set gives t (= mixture guarantee on the grid, by LP duality);
the continuum DP best response to nu gives V_nu(0) >= game value (upper estimate). Iterate."""
import numpy as np, sys
from scipy.special import gammainc
from scipy.optimize import linprog
from scipy.linalg import expm

def Pk(x, k): return sum(gammainc(i + 1, x) for i in range(k))

def W_of_x(A, k, xs, sub=12):
    T = A.shape[1]; h = 1.0 / T
    gx, gw = np.polynomial.legendre.leggauss(sub); tn = 0.5 * h * (gx + 1); tw = 0.5 * h * gw
    pi = np.zeros(k + 1); pi[k] = 1.0; Wx = np.zeros(len(xs))
    for c in range(T):
        a = A[:, c]; Q = np.zeros((k + 1, k + 1))
        for j in range(1, k + 1): Q[j, j] -= a[j - 1]; Q[j - 1, j] += a[j - 1]
        m = np.minimum(xs[:, None], a[None, :])
        for tt, ww in zip(tn, tw): Wx += ww * (m @ (expm(Q * tt) @ pi)[1:])
        pi = expm(Q * h) @ pi
    return Wx

def best_response(nu, xs, k, T, steps):
    """Continuum DP for v(s) = sum_{x_j >= s} nu_j on (x_{j-1}, x_j]; returns V_k(0) and averaged optimal thresholds."""
    v = np.cumsum(nu[::-1])[::-1]; e = np.concatenate([[0.0], xs]); ds = np.diff(e)
    Psi = lambda tau: np.sum(ds * np.maximum(v - tau, 0.0))
    def thr(tau):                                   # sup{s : v(s) > tau}
        idx = np.nonzero(v > tau)[0]
        return xs[idx[-1]] if len(idx) else 0.0
    V = np.zeros(k + 1); hu = 1.0 / steps
    # integrate in u = 1 - t from 0 to 1; record thresholds at t = 1 - u
    rec = np.zeros((k, steps))
    def F(V):
        d = np.zeros(k + 1)
        for j in range(1, k + 1): d[j] = Psi(V[j] - V[j - 1])
        return d
    for i in range(steps):
        for j in range(1, k + 1): rec[j - 1, steps - 1 - i] = thr(V[j] - V[j - 1])
        k1 = F(V); k2 = F(V + 0.5 * hu * k1); k3 = F(V + 0.5 * hu * k2); k4 = F(V + hu * k3)
        V = V + hu / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    A = rec.reshape(k, T, steps // T).mean(axis=2)
    return V[k], A

def run(k, J=220, T=64, steps=2048, iters=int(sys.argv[2]) if len(sys.argv) > 2 else 60, xmin=1e-7, xmax=2e3):
    xs = np.geomspace(xmin, xmax, J); P = Pk(xs, k)
    pols = [np.full((k, T), a) for a in (0.3, 1.0, 3.0)]; Ws = [W_of_x(A, k, xs) for A in pols]
    best_up = 9
    for it in range(iters):
        Wm = np.array(Ws)                            # (n_pol, J)
        n = len(Ws)
        c = np.zeros(J + 1); c[-1] = 1.0
        A_ub = np.hstack([Wm, -np.ones((n, 1))]); b_ub = np.zeros(n)
        A_eq = np.concatenate([P, [0.0]])[None, :]; b_eq = [1.0]
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * J + [(None, None)], method="highs")
        t = res.x[-1]; nu = res.x[:J]; mu = -res.ineqlin.marginals; mu = mu / mu.sum()
        Wmix = mu @ Wm; low_grid = np.min(Wmix / P)
        up, Anew = best_response(nu, xs, k, T, steps); best_up = min(best_up, up)
        print(f"it {it:2d}: LP t={t:.6f}  mixture grid-guarantee={low_grid:.6f}  BR V_nu(0)={up:.6f}  best upper={best_up:.6f}  |pol|={n}", flush=True)
        if up - t < 2e-6: break
        pols.append(Anew); Ws.append(W_of_x(Anew, k, xs))
    np.savez(f"do_k{k}.npz", xs=xs, nu=nu, mu=mu, pols=np.array(pols), t=t, up=best_up)
    return t, best_up

if __name__ == "__main__":
    k = int(sys.argv[1]); print(run(k))
