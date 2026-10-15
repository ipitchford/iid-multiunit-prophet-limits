# Reproduce the numerical certificates

The analytic fixed-k theorem is not a finite test. Read its complete proof in [paper.tex](paper.tex). This route checks the four k=2 certificates and input/semantic regressions only.

## Environment

Use Python 3.11 or later and **python-flint 0.9.0**. The recorded draft replay used Python 3.11.14 on macOS arm64. No NumPy, SciPy or mpmath is needed for certificate replay. Use an isolated environment, not an active unrelated research environment. Example setup, if dependency installation is wanted:

```sh
python3 -m venv /absolute/path/to/new-replay-venv
/absolute/path/to/new-replay-venv/bin/python -m pip install python-flint==0.9.0
```

The installation step may access the network; the replay itself does not. Alternatively use an existing compatible environment. The dependency's own licence applies; it is not vendored or relicensed here.

## Clean execution

Extract the eventual frozen archive into a new directory, enter its root, and choose a **new** output directory whose parent exists:

```sh
/absolute/path/to/replay-venv/bin/python -B code/replay.py /absolute/path/to/new-results
```

Or set `PYTHON` to that interpreter and run `bash code/reproduce.sh /absolute/path/to/new-results`. The wrapper no longer overwrites shipped logs or invokes an environment manager. The runner refuses an existing output directory, executes serially with bytecode disabled and one OpenMP/OpenBLAS thread, and records UTC receipt times plus monotonic elapsed seconds. Those clocks are computational wall time, not active human effort. A crash or timeout leaves partial evidence, not a pass.

Runs in each mode (`-B`, then `-O -B`):

1. `code/cert_lower_mix.py data/mix_fine.json 40`
2. `code/cert_upper2.py data/inst_do450.json 80000`
3. `code/theta_cert.py 2000`
4. `code/certify_single.py data/policy_k2_T24.json 400`
5. `code/test_certifiers.py`

The runner checks exits **and** output fields against the exact declared c, k, T, policy/atom counts and barrier steps. It checks source/data hashes before and after execution, retains stdout/stderr separately, and writes portable relative commands plus hashes in `summary.json`. Inspect failures rather than editing a receipt. The final exit is zero only when all checked runs pass and their source/data inputs are unchanged.

The 110-check regression suite includes invalid step counts, boolean dimensions, malformed shapes, NaN/nonfinite values, invalid rational/domain inputs, zero mixture weight, and excessive substantive claims. Its comparisons use explicit exceptions rather than Python assertions. A negative control failing to certify a proposed bound is not automatically a certified lower bound on the actual optimum.

## Expected substantive results

Mixture: c=0.83695; 36 policies; 64 pieces; positive initial slope, positive tail and positive convex-piece tangent bounds. Upper profile: 41 layer atoms; 80000-step barrier below 0.8372914. Theta: certified theta bracket, positive phi1 endpoint and sum below 0.835590. Deterministic illustration: c=0.8365, 24 pieces. Detailed ball enclosures, not rounded displays in prose, govern the comparisons.

The mixture c=0.83696 and deterministic c=0.8366 controls fail for those witnesses; they do not exclude a different better policy. Upper claim 0.83 fails against this enclosure; that is not an independent lower certificate on its true value. Theta's phi2=-1 sentinel records a stopped barrier and uses a trivial zero-state bound thereafter, as explained in the proof.

## Optional search provenance

`double_oracle.py` and `double_oracle2.py` are optional floating-point exploration scripts requiring NumPy and SciPy. They write `.npz` files in the working directory and may be expensive. They are not invoked by replay, are not needed to validate the frozen rational witnesses, and do not yield rigorous upper or lower guarantees by themselves. No broad search regeneration or optimization cost is included in recorded replay times.
