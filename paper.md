<div class="center">

Version 0.1.0-candidate\
Reserved DOI:
[10.5281/zenodo.23404235](https://doi.org/10.5281/zenodo.23404235)

</div>

# Introduction

Let $`X_1,\ldots,X_n`$ be independent with common known law $`F`$ on
$`[0,\infty)`$ and $`0<\mathbb E X_1<\infty`$. A decision maker sees the
observations sequentially and may irrevocably accept at most $`k`$ of
them. For $`n\ge k`$, let $`\mathrm{DP}_{n,k}(F)`$ be the optimal
expected accepted sum, and let $`\mathrm{PR}_{n,k}(F)`$ be the expected
sum of the $`k`$ largest observations. We study
``` math
\gamma_{n,k}=\inf_F\frac{\mathrm{DP}_{n,k}(F)}{\mathrm{PR}_{n,k}(F)}.
```
The infimum permits a different law at each horizon. Consequently,
existence of a limit for each fixed law does not establish convergence
of $`\gamma_{n,k}`$.

The main analytic result,
Theorem <a href="#thm:general-k-game" data-reference-type="ref"
data-reference="thm:general-k-game">2</a>, proves convergence for every
fixed $`k`$ and identifies the limit with a continuum game. The compact
strategy variable is the cumulative acceptance function, not a bounded
set of thresholds or a compact family of observation laws. Lower
transfer is uniform over laws for each fixed finite policy mixture.
Upper transfer constructs a horizon-dependent finite-support law from
each fixed step profile. Compactness and explicit origin and tail
estimates connect these two directions. These arguments do not
interchange a limit with an infimum over all laws.

#### Relation to earlier formulations.

For $`k=1`$, the asymptotic constant and its optimal-policy
interpretation are classical (Hill and Kertz 1982; Kertz 1986; Correa et
al. 2021). Jiang, Ma and Zhang (Jiang et al. 2026, Definition 4.1,
Eq. (25), Theorem 4.2) give a finite-horizon semi-infinite linear
programme for arbitrary $`k,n`$ using state occupancy and cumulative
type coverage; their Proposition 4.8 controls quantile discretization at
fixed $`n`$. Our cumulative acceptance formulation is closely related to
that framework. Their Lemma 2.11 and Appendix C also supply the relevant
threshold-recovery precedent. We record an explicit continuous-time
occupancy formula, not a new purification principle.

Brustle, Perez-Salazar and Verdugo (Brustle et al. 2026, Theorems 1–2)
give an exact finite-horizon quantile formulation and an asymptotic
lower bound
``` math
\gamma_{n,k}\ge\left(1-\frac{24k\log^2n}{n}\right)
                  \sum_{j=1}^k\theta_j^\star
```
for sufficiently large $`n`$. This is a lower bound on a liminf, not an
identification of the optimal limit. Molina, Gast, Loiseau and
Perchet (Molina et al. 2025, Proposition 5.4, Eq. (5.7)) analyze a
related boundary-value construction; with equal selection and benchmark
budgets it yields the same kind of lower bound. Their fixed-horizon
finite-support reduction (Proposition 5.5) is distinct from convergence
as the horizon grows. The asymptotic tightness question is also
discussed in (Brüstle 2025).

Quantile-kernel minimax and finite-horizon implementation are
substantive methodological precedents in Loiseau et al. (Loiseau et al.
2026, sec. 3, Appendix C.4). Their principal model uses a single static
threshold and a different endpoint topology. Here the controls depend on
time and remaining budget, the benchmark is the top-$`k`$ sum, and
compactness is imposed on cumulative coverage; both endpoint estimates
are proved explicitly. Other quantile and restricted-policy formulations
include (Perez-Salazar et al. 2026; Goldenshluger et al. 2026), and
related online-selection analyses include (Perez-Salazar and Verdugo
2024). Kong and Murthy (Kong and Murthy 2026) study fixed-law
extreme-value asymptotics, which do not justify moving the infimum over
laws through the limit. Cruz-Ossa, Perez-Salazar and Verdugo (Cruz-Ossa
et al. 2026) study single-threshold competition complexity with a
potentially different observation budget. Neither comparison supplies
the unrestricted adaptive limit proved here. A bounded source comparison
found no earlier theorem with precisely this fixed-budget worst-case
limit and characterization; this is not an exhaustive priority claim.

#### Certified two-unit consequence.

The analytic theorem also makes finite continuum certificates sufficient
for asymptotic bounds. The following numerical consequence uses the
explicit witnesses and rigorous arithmetic described in
Section <a href="#sec:certificates" data-reference-type="ref"
data-reference="sec:certificates">3</a>.

<div id="thm:main" class="theorem">

**Theorem 1** (computer-assisted numerical bounds). *The limit
$`\gamma_2^*=\lim_{n\to\infty}\gamma_{n,2}`$ exists, and
``` math
0.83695\le\gamma_2^*\le0.8372914<0.83730.
```
Moreover
``` math
\theta_1^\star+\theta_2^\star
 <\frac{5723787}{6850000}<0.835590,\qquad
 \gamma_2^*-(\theta_1^\star+\theta_2^\star)
 >\frac{18641}{13700000}.
```*

</div>

Thus the nonlinear-system value is not the asymptotic optimum for two
units. This does not settle a claim about $`\inf_n\gamma_{n,2}`$, or
show where a particular restricted dual construction loses value. The
strengthened certified bracket has width $`0.0003414`$; rounding the
upper endpoint outward to $`0.83730`$ gives width $`0.00035`$. Numerical
single-horizon bounds in (Jiang et al. 2026; Brustle et al. 2026) and
fixed-law numerical asymptotics in (Kong and Murthy 2026) are useful
comparisons, but are not substitutes for this asymptotic certificate.

# A continuum characterization for every fixed number of selections

Fix an integer $`k\ge1`$. For $`n\ge k`$, let $`\gamma_{n,k}`$ be the
infimum, over laws $`F`$ on $`[0,\infty)`$ with
$`0<\mathbb E_F X<\infty`$, of the optimal expected reward from at most
$`k`$ online selections divided by the expected sum of the $`k`$ largest
of $`n`$ independent observations. The restriction $`n\ge k`$ is
immaterial for the limit; for smaller horizons one may define the
benchmark using the largest $`\min(k,n)`$ observations. Set
``` math
P_k(x)=\mathbb E\min\{\mathrm{Pois}(x),k\}
       =\int_0^x\Pr(\mathrm{Pois}(s)\le k-1)\,ds.
```
Then $`P_k(0)=0`$, $`P_k'(0)=1`$, $`P_k(\infty)=k`$, and
``` math
P_k''(x)=-e^{-x}\frac{x^{k-1}}{(k-1)!}\le0,
 \qquad 0<P_k(x)\le\min\{x,k\}\quad(x>0).
```
In particular $`P_k(x)/x\to1`$ as $`x\downarrow0`$, including when
$`k=1`$.

A nonnegative bounded measurable threshold vector $`a=(a_1,\ldots,a_k)`$
accepts an arrival of scaled tail quantile $`s`$ at time $`t`$ with
$`j`$ slots remaining when $`s\le a_j(t)`$. Use column state
probabilities indexed by $`0,\ldots,k`$, initially $`\pi(0)=e_k`$, with
generator
``` math
Q_{j-1,j}(t)=a_j(t),\qquad Q_{j,j}(t)=-a_j(t)\quad(j\ge1),
 \qquad Q_{\cdot,0}=0.
```
The state equation is $`\pi'=Q\pi`$. Define
``` math
W^a(x)=\int_0^1\sum_{j=1}^k\pi_j^a(t)\min\{x,a_j(t)\}\,dt.
```
An equal-mesh threshold is constant on each interval of some finite
equal partition of $`[0,1]`$. Let $`\mathcal C_k`$ be the pointwise
closure on $`(0,\infty)`$ of the convex hull of their functions $`W^a`$.

A profile $`v`$ is a nonzero nonnegative nonincreasing step function of
finite height, supported in $`(0,S]`$ for some finite $`S`$. Write
$`M_v=\int_0^S v(s)\,ds`$, let $`v_1`$ be its maximum height, and put
``` math
\Psi_v(z)=\int_0^S(v(s)-z)^+\,ds\quad(z\in\mathbb R).
```
Let $`V_0^v=0`$ and define $`V_j^v`$, $`1\le j\le k`$, by
``` math
\begin{equation}
\label{eq:general-k-values}
 (V_j^v)'(t)=-\Psi_v(V_j^v(t)-V_{j-1}^v(t)),
 \qquad V_j^v(1)=0.
\end{equation}
```

<div id="thm:general-k-game" class="theorem">

**Theorem 2**. *For every fixed integer $`k\ge1`$, the limit of
$`\gamma_{n,k}`$ exists and
``` math
\lim_{n\to\infty}\gamma_{n,k}
 =\inf_{v}\frac{V_k^v(0)}{\int v\,dP_k}
 =\max_{W\in\mathcal C_k}\inf_{x>0}\frac{W(x)}{P_k(x)}.
```
The infimum is over the profiles just defined. The maximum is attained
in $`\mathcal C_k`$; no attainment by a bounded threshold policy or by a
profile is asserted. This statement does not identify the limit with
$`\inf_n\gamma_{n,k}`$ or give a rate uniform in $`k`$.*

</div>

## Finite-horizon lower transfer

For $`n\ge k`$ and $`0\le x\le n`$, define
``` math
P_{n,k}(x)=\int_0^x\Pr(\mathrm{Bin}(n-1,s/n)\le k-1)\,ds.
```
Summing the beta integrals for ranks $`0,\ldots,k-1`$ gives
``` math
\begin{equation}
\label{eq:general-k-finite-tail}
 P_{n,k}(n)=n\sum_{r=0}^{k-1}\binom{n-1}{r}
 \int_0^1q^r(1-q)^{n-1-r}\,dq=k.
\end{equation}
```
Let $`a`$ have $`T`$ time pieces and threshold bound $`A`$. For
$`n\ge\max\{k,2A\}`$, at step $`i`$ use $`t_i=(i-1)/n`$ and accept iff
$`nU_i\le a_j(t_i)`$ with $`j\ge1`$ slots remaining. With $`p_{j,i}`$
the pre-step state probabilities, set
``` math
W_n^a(x)=\frac1n\sum_{i=1}^n\sum_{j=1}^k
 p_{j,i}\min\{x,a_j(t_i)\}.
```
For a finite mixture write $`\overline W_n`$ and $`\overline W`$ for the
weighted cumulative payoffs, and put
``` math
g_n=\inf_{0<x\le n}\overline W_n(x)/P_{n,k}(x).
```

<div id="lem:general-k-lower-transfer" class="lemma">

**Lemma 3**. *Every such mixture guarantees
$`\mathrm{DP}_{n,k}(F)\ge g_n\mathrm{PR}_{n,k}(F)`$ for every admissible
$`F`$, and
``` math
\liminf_{n\to\infty}g_n\ge
 c:=\inf_{x>0}\frac{\overline W(x)}{P_k(x)}.
```
For a single policy, writing
``` math
D=e(4A^2+4AT)+2A+2T,\qquad \delta_n=D/n,
```
one has $`|W_n^a(x)-W^a(x)|\le\delta_n x`$ and
``` math
\begin{equation}
\label{eq:general-k-benchmark-error}
 |P_{n,k}(x)-P_k(x)|\le\frac{x^3/3+x^2/2}{n}.
\end{equation}
```
For a fixed finite mixture use the maxima of its component bounds.*

</div>

<div class="proof">

*Proof.* Let $`\psi(q)=\inf\{z:F(z)\ge1-q\}`$ and realize
$`X_i=\psi(U_i)`$ with independent uniform $`U_i`$. Observed atoms are
handled by drawing the conditional quantile using fresh randomness; this
gives admissible randomized decisions and the stated iid joint
realization. Put $`v_n(s)=\psi(s/n)`$. The pre-step state is independent
of $`U_i`$, so the policy reward is $`\int_0^n v_n\,dW_n^a`$. An item at
quantile $`q`$ is among the top $`k`$ precisely when at most $`k-1`$
other uniform quantiles are smaller. Thus
$`\mathrm{PR}_{n,k}(F)=\int_0^n v_n\,dP_{n,k}`$. Ties among observed
values are harmless. Every strict level set of nonincreasing $`v_n`$ is
an initial interval; Tonelli’s layer-cake identity therefore turns
$`\overline W_n\ge g_nP_{n,k}`$ into the claimed reward inequality.
Finite mean makes both rewards finite. Mixtures are selected before
arrivals, and the same argument applies to their weighted payoffs.

In the induced $`\ell_1`$ matrix norm, $`\|Q(t)\|\le2A`$, independent of
the number of states. The discrete kernel is $`K_i=I+Q(t_i)/n`$. If
there is no threshold breakpoint inside its cell, its exact continuous
propagator $`E_i`$ satisfies
``` math
\|E_i-K_i\|\le(2A/n)^2e^{2A/n}.
```
At most $`T-1`$ cells contain a breakpoint; on these the bound
$`4Ae^{2A/n}/n`$ suffices. All propagators are stochastic and hence
contractive in $`\ell_1`$. Telescoping gives
``` math
\max_i\|p_{\cdot,i}-\pi(t_i)\|_1
 \le e(4A^2+4AT)/n.
```
Within a cell $`\|\pi(t)-\pi(t_i)\|_1\le2A(t-t_i)`$. The integrand
entries $`\min\{x,a_j\}`$ are bounded by $`x`$; separating the
breakpoint cells in the Riemann sum gives the displayed $`\delta_nx`$
bound.

For completeness, $`d_{\rm TV}(\mathrm{Bern}(p),\mathrm{Pois}(p))
=p(1-e^{-p})\le p^2`$ for $`0\le p\le1`$. Coupling independent summands
and then Poisson variables differing in mean by $`s/n`$ gives
``` math
d_{\rm TV}(\mathrm{Bin}(n-1,s/n),\mathrm{Pois}(s))
 \le(s^2+s)/n.
```
Apply this to the event $`\{0,\ldots,k-1\}`$ and integrate to obtain
<a href="#eq:general-k-benchmark-error" data-reference-type="eqref"
data-reference="eq:general-k-benchmark-error">[eq:general-k-benchmark-error]</a>.
Mixture errors are convex combinations of the component errors.

If $`c=0`$, nonnegativity of $`g_n`$ proves the conclusion directly,
including the case $`A=0`$. Suppose $`c>0`$, so $`A>0`$, and set
$`\kappa=P_k(A)/A>0`$. For sufficiently large $`n`$,
$`c-\delta_n/\kappa>0`$. Concavity gives $`P_k(x)\ge\kappa x`$ on
$`(0,A]`$, and hence
``` math
\frac{\overline W_n(x)}{P_{n,k}(x)}
 \ge\frac{c-\delta_n/\kappa}
 {1+(A^2/3+A/2)/(\kappa n)}.
```
The positive numerator justifies replacing the denominator by its upper
bound. For $`A\le x\le n`$, the numerator is constant and
$`P_{n,k}(x)\le k`$. Since $`\overline W(A)=\overline W(\infty)\ge kc`$,
``` math
\frac{\overline W_n(x)}{P_{n,k}(x)}\ge c-\delta_nA/k.
```
Both lower bounds tend to $`c`$. ◻

</div>

## Verification and quantitative upper transfer

<div id="lem:general-k-verification" class="lemma">

**Lemma 4**. *The system
<a href="#eq:general-k-values" data-reference-type="eqref"
data-reference="eq:general-k-values">[eq:general-k-values]</a> has a
unique solution and $`V_j\ge V_{j-1}\ge0`$ for all $`1\le j\le k`$. For
uniformly bounded Borel acceptance sets $`\mathcal A_j(t)`$ with jointly
Borel sets $`\{(t,s):s\in\mathcal A_j(t)\}`$, the associated continuum
policy reward is at most $`V_k(0)`$. Equality holds for
``` math
\mathcal A_j^*(t)=\{s:v(s)>V_j(t)-V_{j-1}(t)\}.
```
If $`\Phi_0=0`$ and continuous piecewise absolutely continuous functions
$`\Phi_j`$ satisfy $`\Phi_j(1)\ge0`$ and
$`\Phi_j'\le-\Psi_v(\Phi_j-\Phi_{j-1})`$ almost everywhere, then
$`V_j\le\Phi_j`$ for every $`j`$.*

</div>

<div class="proof">

*Proof.* The function $`\Psi_v`$ is nonnegative, nonincreasing and
globally $`S`$-Lipschitz on $`\mathbb R`$, so the finite-dimensional
vector field is globally Lipschitz and the terminal solution exists
uniquely. First $`V_1\ge0`$. Inductively let $`D_j=V_j-V_{j-1}`$ and
suppose $`D_{j-1}\ge0`$. On an interval where $`D_j<0`$,
``` math
D_j'=\Psi_v(D_{j-1})-\Psi_v(D_j)\le0.
```
Such a negative interval cannot return to the terminal value
$`D_j(1)=0`$, proving $`D_j\ge0`$.

Write $`b_j=|\mathcal A_j|`$, $`r_j=\int_{\mathcal A_j}v`$, and
$`\Delta_j=V_j-V_{j-1}\ge0`$. Then
$`\Psi_v(\Delta_j)\ge r_j-b_j\Delta_j`$, even if acceptance extends
beyond the support of $`v`$. For the corresponding state law,
``` math
\frac{d}{dt}\sum_{j=0}^k\pi_jV_j
 =\sum_{j=1}^k\pi_j[-\Psi_v(\Delta_j)-b_j\Delta_j]
 \le-\sum_{j=1}^k\pi_jr_j.
```
Integration from 0 to 1 gives $`J\le V_k(0)`$. For the displayed
maximizing sets, $`\Psi_v(\Delta_j)=r_j-b_j\Delta_j`$, giving equality.
These sets are bounded by $`S`$, Borel, and initial intervals up to
irrelevant endpoints, hence are bounded measurable quantile thresholds.

For the final assertion, proceed by induction in $`j`$. If
$`V_{j-1}\le\Phi_{j-1}`$ then $`V_j'\ge-\Psi_v(V_j-\Phi_{j-1})`$. On a
positive component of $`V_j-\Phi_j`$, its derivative is nonnegative by
monotonicity of $`\Psi_v`$, so it cannot return to its nonpositive
terminal value. Thus that positive component cannot exist. ◻

</div>

<div id="prop:general-k-upper-transfer" class="proposition">

**Proposition 5**. *Let $`v=v_m`$ on $`(e_{m-1},e_m]`$, with $`e_M=S`$
and $`v=0`$ beyond $`S`$. For $`n\ge\max\{k,2S\}`$, let $`F_n`$ put mass
$`(e_m-e_{m-1})/n`$ at $`v_m`$ and the remaining mass at zero. Then
``` math
\mathrm{DP}_{n,k}(F_n)
 \le V_k(0)+\frac{(2eS^2+S)M_v}{n},
```
``` math
\mathrm{PR}_{n,k}(F_n)
 \ge\int v\,dP_k-\frac{v_1(S^3/3+S^2/2)}n.
```
Consequently $`\limsup_n\gamma_{n,k}\le V_k(0)/\int v\,dP_k`$.*

</div>

<div class="proof">

*Proof.* Backward induction gives a deterministic optimal finite-horizon
policy whose decisions depend on time, remaining slots and current
value. It may reject zero without loss. In quantile coordinates its
acceptance sets $`\mathcal A_{i,j}`$ lie in $`(0,S]`$. Put
$`\alpha_{i,j}=\int_{\mathcal A_{i,j}}v\le M_v`$; its reward is
$`n^{-1}\sum_{i,j}p_{j,i}\alpha_{i,j}`$.

Use the same sets constantly on the corresponding continuum cells. Their
generators have norm at most $`2S`$, so
``` math
\|E_i-K_i\|\le2eS^2/n^2,
 \quad \max_i\|p_{\cdot,i}-\pi(t_i)\|_1\le2eS^2/n,
 \quad \|\pi(t)-\pi(t_i)\|_1\le2S(t-t_i).
```
Multiplying by the reward-vector bound $`M_v`$ and summing cells gives
``` math
n^{-1}\sum_{i,j}p_{j,i}\alpha_{i,j}
 \le\int_0^1\sum_j\pi_j(t)\alpha_j(t)\,dt
       +(2eS^2+S)M_v/n.
```
The integral is at most $`V_k(0)`$ by
Lemma <a href="#lem:general-k-verification" data-reference-type="ref"
data-reference="lem:general-k-verification">4</a>. The prophet identity
and layer cake, using
<a href="#eq:general-k-benchmark-error" data-reference-type="eqref"
data-reference="eq:general-k-benchmark-error">[eq:general-k-benchmark-error]</a>
on $`[0,S]`$, give the denominator bound. Its limit is positive because
$`v`$ is nonzero. Divide for sufficiently large $`n`$ and use
$`\gamma_{n,k}\le\mathrm{DP}_{n,k}(F_n)/\mathrm{PR}_{n,k}(F_n)`$. ◻

</div>

For numerical certification at any fixed $`k`$, the verification lemma
permits a conservative backward grid construction, computed in
increasing state order at each time step:
``` math
\Phi_j(t_i)\ge\Phi_j(t_{i+1})
 +h\Psi_v\bigl(\Phi_j(t_{i+1})-\Phi_{j-1}(t_i)\bigr),
 \qquad \Phi_j(1)=0,
```
with upward rounding. Increments are nonnegative. Linear interpolation
satisfies $`\Phi_j(t)-\Phi_{j-1}(t)\ge
\Phi_j(t_{i+1})-\Phi_{j-1}(t_i)`$, which proves the required slope
inequality. This is a valid general scheme, not a new numerical witness.

## Compact minimax and control of both boundaries

<div class="proof">

*Proof of
Theorem <a href="#thm:general-k-game" data-reference-type="ref"
data-reference="thm:general-k-game">2</a>.* Let $`c`$ denote the infimum
over profiles in the theorem. The upper transfer gives
$`\limsup_n\gamma_{n,k}\le c`$. Clearly $`c\ge0`$; also $`c\le1`$, since
for $`v=\mathbf1_{(0,x]}`$ both the optimal reward and prophet reward
are $`P_k(x)`$, obtained by taking up to $`k`$ positive Poisson
arrivals.

Let $`\mathcal K_k`$ be the set of nondecreasing concave functions
$`W:(0,\infty)\to[0,k]`$ with $`W(x)\le x`$. Every $`W^a`$ lies in it:
its slope is at most $`\int_0^1\sum_{j\ge1}\pi_j\le1`$, and its limit at
infinity is the expected number of acceptances, at most $`k`$. The
defining inequalities of $`\mathcal K_k`$ are closed finite-evaluation
conditions. Thus it is a convex closed subset of the compact product
$`[0,k]^{(0,\infty)}`$, and $`\mathcal C_k`$ is compact and convex.
Every member extends by $`W(0)=0`$ and is $`1`$-Lipschitz: for
$`0<x<y`$, concavity gives
``` math
0\le\frac{W(y)-W(x)}{y-x}\le\frac{W(x)}x\le1.
```

For each profile, the optimal bounded measurable thresholds from
Lemma <a href="#lem:general-k-verification" data-reference-type="ref"
data-reference="lem:general-k-verification">4</a> can be approximated in
$`L^1`$ by equal-mesh thresholds with values in $`[0,S]`$. Indeed the
cell averages converge in $`L^1`$. For
$`\|a-b\|_{L^1}=\int_0^1\sum_{j=1}^k|a_j-b_j|`$, stochastic contraction
and Duhamel’s formula give
``` math
\sup_t\|\pi^a(t)-\pi^b(t)\|_1\le2\|a-b\|_{L^1}.
```
The reward integrals differ by at most $`v_1|a_j-b_j|`$ in state $`j`$,
so
``` math
|J_v(a)-J_v(b)|\le(2M_v+v_1)\|a-b\|_{L^1}.
```
Consequently the supremum of the profile reward over equal-mesh policies
is $`V_k^v(0)`$.

Write profiles as $`v_\nu(s)=\nu((s,\infty))`$, where $`\nu`$ is a
nonzero finitely supported positive measure on $`(0,\infty)`$. Fubini
gives $`J_{v_\nu}(a)=\int W^a\,d\nu`$ and
$`\int v_\nu\,dP_k=\int P_k\,d\nu`$. Values at profile endpoints affect
none of these expressions or the ODE. Homogeneity of
<a href="#eq:general-k-values" data-reference-type="eqref"
data-reference="eq:general-k-values">[eq:general-k-values]</a> permits
normalization $`\int P_k\,d\nu=1`$; let $`\mathcal N_k`$ be this convex
set of normalized finite measures. Finite evaluation makes
$`W\mapsto\int W\,d\nu`$ continuous and affine. It has the same supremum
over the generating policies as over their convex hull and closure, so
compactness gives
``` math
\max_{W\in\mathcal C_k}\int W\,d\nu=V_k^{v_\nu}(0),
 \qquad c=\inf_{\nu\in\mathcal N_k}V_k^{v_\nu}(0).
```

We give the compact minimax argument explicitly. For each $`x>0`$ set
$`H_x=\{W\in\mathcal C_k:W(x)\ge cP_k(x)\}`$. If a finite subfamily
indexed by $`x_1,\ldots,x_m`$ had empty intersection, the compact convex
set of vectors
``` math
\left\{\left(\frac{W(x_\ell)}{P_k(x_\ell)}\right)_{\ell=1}^m:
                    W\in\mathcal C_k\right\}
```
would be disjoint from $`[c,\infty)^m`$. Strict finite-dimensional
separation supplies nonnegative weights $`\lambda_\ell`$ with
$`\sum_\ell\lambda_\ell=1`$ such that
``` math
\max_{W\in\mathcal C_k}\sum_\ell
 \lambda_\ell\frac{W(x_\ell)}{P_k(x_\ell)}<c.
```
The separating weights are nonnegative because the upper orthant is
unbounded in each positive coordinate direction. But
$`\nu=\sum_\ell\lambda_\ell\delta_{x_\ell}/P_k(x_\ell)`$ lies in
$`\mathcal N_k`$, contradicting the definition of $`c`$ and the
preceding payoff equality. The closed sets $`H_x`$ therefore have the
finite-intersection property, and compactness supplies
$`W^*\in\mathcal C_k`$ with $`W^*\ge cP_k`$ everywhere. Conversely, for
every $`W\in\mathcal C_k`$ and $`\nu\in\mathcal N_k`$,
``` math
\inf_{x>0}\frac{W(x)}{P_k(x)}
 \le\int W\,d\nu\le V_k^{v_\nu}(0).
```
Taking the infimum over $`\nu`$ proves the minimax equality and
attainment in $`\mathcal C_k`$ without requiring $`\mathcal N_k`$
compact.

If $`c=0`$, nonnegativity and the upper transfer already prove limit
existence. Suppose $`c>0`$ and choose $`0<\varepsilon<\min\{c,1/2\}`$.
Choose $`0<\delta<1<L`$ with
``` math
P_k(\delta)/\delta\ge1-\varepsilon,
 \qquad P_k(L)\ge k(1-\varepsilon).
```
Pointwise closure and the common $`1`$-Lipschitz bound give a finite
convex combination $`W`$ of equal-mesh policy payoffs with
``` math
\sup_{x\in[\delta,L]}|W(x)-W^*(x)|\le\varepsilon P_k(\delta).
```
To see this directly, approximate at finitely many sufficiently fine
grid points, then apply the Lipschitz bounds between them. Thus
$`W/P_k\ge c-\varepsilon`$ on $`[\delta,L]`$. At the lower boundary,
concavity and $`P_k(x)\le x`$ give, for $`0<x<\delta`$,
``` math
\frac{W(x)}{P_k(x)}\ge\frac{W(\delta)}\delta
 \ge(c-\varepsilon)(1-\varepsilon).
```
At the upper boundary, monotonicity and $`P_k(x)\le k`$ give, for
$`x>L`$,
``` math
\frac{W(x)}{P_k(x)}\ge\frac{W(L)}k
 \ge(c-\varepsilon)\frac{P_k(L)}k
 \ge(c-\varepsilon)(1-\varepsilon).
```
The fixed finite mixture representing $`W`$ is eligible for
Lemma <a href="#lem:general-k-lower-transfer" data-reference-type="ref"
data-reference="lem:general-k-lower-transfer">3</a>; hence
``` math
\liminf_n\gamma_{n,k}\ge(c-\varepsilon)(1-\varepsilon).
```
Let $`\varepsilon\downarrow0`$ and combine with the upper transfer. The
order of choices is $`k`$, then $`\varepsilon`$, then the finite
mixture, then sufficiently large $`n`$. No joint uniform convergence
over all distributions or policies has been assumed. ◻

</div>

## Occupancy-weighted domination of finite mixtures

The following constructive consequence is naturally expressed in the
state occupancy and acceptance flow framework of Jiang, Ma and
Zhang (Jiang et al. 2026). We do not claim a novel purification
principle. It clarifies the role of mixtures as computational
representations.

<div id="prop:general-k-occupancy-domination" class="proposition">

**Proposition 6**. *Every finite mixture of bounded measurable quantile
policies is dominated, simultaneously for all $`x>0`$, by one bounded
measurable time- and state-dependent quantile policy. The corresponding
statement holds at each finite horizon for feasible quantile
thresholds.*

</div>

<div class="proof">

*Proof.* Let the mixture weights be $`\mu_r`$, thresholds $`a_{r,j}`$
and state probabilities $`\pi_{r,j}`$. Put
``` math
p_j(t)=\sum_r\mu_r\pi_{r,j}(t),\qquad
 b_j(t)=
 \begin{cases}
 \displaystyle\frac{\sum_r\mu_r\pi_{r,j}(t)a_{r,j}(t)}{p_j(t)},
       &p_j(t)>0,\\
 0,&p_j(t)=0.
 \end{cases}
```
These are measurable thresholds bounded by the maximum component
threshold. If $`p_j=0`$ all the nonnegative weighted occupancy terms
vanish, so $`p_jb_j=\sum_r\mu_r\pi_{r,j}a_{r,j}`$ in all cases. Writing
$`p_{k+1}b_{k+1}=0`$ and $`b_0=0`$, the averaged state equations are
``` math
p_j'=p_{j+1}b_{j+1}-p_jb_j\quad(0\le j\le k),
 \qquad p(0)=e_k.
```
Uniqueness for this bounded measurable linear system identifies $`p`$
with the state probabilities of policy $`b`$. Concavity of
$`u\mapsto\min\{x,u\}`$ gives
``` math
p_j(t)\min\{x,b_j(t)\}
 \ge\sum_r\mu_r\pi_{r,j}(t)\min\{x,a_{r,j}(t)\}.
```
Summing and integrating proves $`W^b\ge\sum_r\mu_rW^{a_r}`$. At a finite
horizon define $`b_{j,i}`$ by the same weighted formula using pre-step
state probabilities. The acceptance flows agree, so the state
probabilities agree by induction. The same concavity inequality proves
domination of $`W_n`$ and hence, by layer cake, reward domination for
every admissible law. ◻

</div>

The dominating continuum thresholds need not retain an equal mesh. The
proposition implies equality of the game value with the *supremum*
guarantee over bounded measurable deterministic quantile thresholds,
because each approximating finite mixture can be dominated. Conversely,
every bounded measurable threshold payoff belongs to $`\mathcal C_k`$:
approximate its thresholds in $`L^1`$ by equal-mesh cell averages and
apply the reward-continuity estimate above to each indicator profile
$`v=\mathbf1_{(0,x]}`$. This gives pointwise convergence of the
cumulative payoffs. The maximum over $`\mathcal C_k`$ therefore also
bounds the deterministic supremum from above. This does not prove
attainment of that supremum, nor remove the separate quantile
randomization needed for atoms in $`F`$. The analytic results of this
section provide no numerical bracket or nonlinear-system separation for
$`k\ge3`$; such conclusions require their own witnesses and
certificates.

# Certified two-unit bounds

In this section $`k=2`$, $`P=P_2=2-e^{-x}(2+x)`$, and $`V_j=V_j^v`$.
Thus $`P''(x)=-xe^{-x}\le0`$. Write $`\bar W`$ for the weighted
cumulative acceptance function of a finite mixture. The next two
propositions certify particular rational inputs; they do not certify the
search procedure or its optimality.

<div id="prop:lowcert" class="proposition">

**Proposition 7** (computer-assisted). *For the explicit mixture of
$`36`$ rational quantile policies with $`T=64`$ in the data file
`mix_fine.json` (rational weights summing to $`1`$),
$`\bar W(x)\ge 0.83695\,P(x)`$ for all $`x\ge0`$.*

</div>

<div class="proof">

*Proof (certificate).* On each time piece the chain of each policy has a
constant generator $`M`$; both $`\pi`$ at the end of the piece and
$`\int\pi\,dt`$ over the piece are read off from
$`\exp\bigl(h\begin{smallmatrix}M & I\\ 0&0\end{smallmatrix}\bigr)`$,
$`h=1/64`$, computed as a rigorous ball. This gives
$`\bar W(x)=\sum_bw_b\min\{x,b\}`$ over the $`1319`$ distinct positive
thresholds $`b`$, with certified weights $`w_b`$. So $`\bar W`$ is
piecewise linear and $`g=\bar W-0.83695P`$ is convex on every linear
piece.

- First piece: $`g(0)=0`$ and
  $`g'(0)=\sum_bw_b-0.83695>4.04\times10^{-6}>0`$.

- Tail: beyond the largest threshold,
  $`g\ge\bar W(\infty)-2(0.83695)>2.57\times10^{-5}>0`$, since $`P<2`$.

- Each remaining piece is split into $`40`$ subintervals, on which the
  tangent lines of $`g`$ at the endpoints give valid lower bounds. The
  smallest certified bound exceeds $`2.95\times10^{-8}`$, on
  $`[0.00558303,0.00751685]`$ (exact decimal endpoints).

All computations use python-flint 0.9.0 (Arb) at $`256`$ bits (Johansson
2017). ◻

</div>

<div id="prop:upcert" class="proposition">

**Proposition 8** (computer-assisted). *For the explicit rational
measure with $`41`$ layer atoms $`\nu`$ of the data file
`inst_do450.json`, the profile $`v=\nu((\cdot,\infty))`$ satisfies
$`V_2(0)/\int v\,dP\le0.8372914`$.*

</div>

<div class="proof">

*Proof (certificate).* On the grid $`t_i=i/N`$, $`N=80000`$, put
$`\Phi_{j}(1)=0`$ and, backwards,
``` math
\Phi_1(t_i)=\Phi_1(t_{i+1})+N^{-1}\Psi\bigl(\Phi_1(t_{i+1})\bigr),\qquad
\Phi_2(t_i)=\Phi_2(t_{i+1})+N^{-1}\Psi\bigl(\Phi_2(t_{i+1})-\Phi_1(t_i)\bigr),
```
rounded up, and interpolate linearly. Both are nonincreasing. On
$`[t_i,t_{i+1}]`$ we have $`\Phi_1\ge\Phi_1(t_{i+1})`$ and
$`\Phi_2-\Phi_1\ge\Phi_2(t_{i+1})-\Phi_1(t_i)`$, so, $`\Psi`$ being
nonincreasing, the slope conditions of
Lemma <a href="#lem:general-k-verification" data-reference-type="ref"
data-reference="lem:general-k-verification">4</a> hold. The benchmark is
$`\int v\,dP=\sum_j\nu_jP(x_j)`$. In ball arithmetic at $`200`$ bits,
$`\Phi_2(0)\le0.8372913936`$ and $`\int v\,dP\ge0.9999999999`$. ◻

</div>

# An upper bound for the nonlinear-system value

The system of (Brustle et al. 2026) reads, on $`[0,1)`$ with
$`y_j(0)=1`$ and $`y_j(t)\to0`$ as $`t\uparrow1`$,
$`\Gamma_\ell(x)=\int_x^\infty s^{\ell-1}e^{-s}\,ds`$,
``` math
\bigl(\Gamma_2(-\ln y_2)\bigr)' = 2 - \tfrac{1}{\theta_2} - \Gamma_3(-\ln y_2),\qquad
\bigl(\Gamma_2(-\ln y_1)\bigr)' = 2 - \Gamma_3(-\ln y_1) - \tfrac{\theta_2}{\theta_1}\bigl(2 - \Gamma_3(-\ln y_2)\bigr).
```
Write $`u_j=-\ln y_j`$ and
$`z_j=\Gamma_2(u_j)=(1+u_j)e^{-u_j}\in(0,1]`$. Also put
$`\Gamma_3(u)=(u^2+2u+2)e^{-u}`$ and
$`H(z)=2-\Gamma_3(\Gamma_2^{-1}(z))`$. Since
$`dH/dz=-\Gamma_2^{-1}(z)\le 0`$, $`H`$ is nonincreasing, and the system
reads $`z_2'=H(z_2)-1/\theta_2`$, $`z_1'=H(z_1)-r\,f(t)`$ with
$`r=\theta_2/\theta_1`$ and $`f=2-\Gamma_3(u_2)\in[0,2]`$.

<div id="lem:theta2" class="lemma">

**Lemma 9**. *Any solution has $`\theta_2<1/2`$ and
$`\mathcal T(\theta_2)=1`$, where
$`\mathcal T(\theta)=\int_0^\infty ue^{-u}\,du/(1/\theta-2+\Gamma_3(u))`$.
The function $`\mathcal T`$ is increasing, and
$`\mathcal T(0.48300)\le 0.99990<1<1.00009\le\mathcal T(0.48302)`$, so
$`\theta_2^\star\in(0.48300,0.48302)`$.*

</div>

<div class="proof">

*Proof.* If $`\theta_2\ge 1/2`$, then $`z_2'\ge -\Gamma_3(u_2)`$. Since
$`\Gamma_3(u)=(1+u)\Gamma_2(u)+e^{-u}\le(2+u)\Gamma_2(u)`$, and
$`u_2\le 2\ln(1/z_2)`$ once $`u_2\ge 3`$, this gives
$`z_2'\ge -C z_2\ln(1/z_2)`$ near $`0`$, so $`z_2`$ cannot reach $`0`$
in finite time; the integral also diverges at $`\theta=1/2`$. For
$`\theta_2<1/2`$, $`z_2`$ is strictly decreasing and its hitting time of
$`0`$ is $`\mathcal T(\theta_2)=1`$. The enclosures use rigorous Arb
quadrature on $`[0,60]`$ with the tail over $`[60,\infty)`$ bounded by
$`61e^{-60}/(1/\theta-2)`$. ◻

</div>

<div id="prop:theta" class="proposition">

**Proposition 10** (computer-assisted). *For any solution,
$`r=\theta_2/\theta_1>1.37`$. Consequently
$`\theta_1^\star+\theta_2^\star<0.48302\,(1+1/1.37)<0.835590`$.*

</div>

<div class="proof">

*Proof.* Since $`H`$ is nonincreasing, a continuous piecewise-linear
$`\phi`$ with $`\phi(0)\le z(0)`$ and $`\phi'\le H(\phi)-K(t)`$ almost
everywhere is a lower barrier for any solution of
$`z'=H(z)-\tilde K(t)`$ with $`\tilde K\le K`$: where $`\phi>z>0`$,
$`(\phi-z)'\le H(\phi)-H(z)\le 0`$. Both barriers start at
$`\phi_j(0)=1=z_j(0)`$ and live on a grid of step $`1/2000`$. While
$`\phi_2(t_i)`$ is certified positive, $`\phi_2`$ has slope
$`\min\{0,\underline H(\phi_2(t_i))-K\}`$ on $`[t_i,t_{i+1}]`$, with
$`K=1/0.48300\ge 1/\theta_2^\star`$ and a certified lower bound
$`\underline H`$ evaluated only at certified points of $`(0,1]`$; once
$`\phi_2`$ is not certified positive the construction stops, since
$`z_2\ge0`$ holds trivially (the certificate records this with the
sentinel value $`-1`$). This gives $`z_2\ge\phi_2^+`$ on $`[0,1)`$.
Because $`z_2`$ is decreasing and $`f=2-\Gamma_3(u_2)`$ is a decreasing
function of $`z_2`$,
$`f\le\bar f_i:=2-\Gamma_3(\overline u(\phi_2(t_{i+1})))`$ on
$`[t_i,t_{i+1}]`$ while $`\phi_2(t_{i+1})`$ is certified positive, where
$`\overline u(z)\ge\Gamma_2^{-1}(z)`$ is a certified rational upper
bound, and $`\bar f_i=2`$ afterwards. If $`r\le 1.37`$, the barrier
$`\phi_1`$ built with $`K=1.37\bar f_i`$ satisfies
$`z_1\ge\phi_1\ge0.0105>0`$ on $`[0,1)`$, contradicting $`z_1(t)\to 0`$.
Finally $`\theta_1^\star+\theta_2^\star=\theta_2^\star(1+1/r^\star)`$. ◻

</div>

<div class="proof">

*Proof of Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>.* Existence follows from
Theorem <a href="#thm:general-k-game" data-reference-type="ref"
data-reference="thm:general-k-game">2</a> with $`k=2`$.
Proposition <a href="#prop:lowcert" data-reference-type="ref"
data-reference="prop:lowcert">7</a> and
Lemma <a href="#lem:general-k-lower-transfer" data-reference-type="ref"
data-reference="lem:general-k-lower-transfer">3</a> give the lower
bound. Proposition <a href="#prop:upcert" data-reference-type="ref"
data-reference="prop:upcert">8</a> and
Proposition <a href="#prop:general-k-upper-transfer" data-reference-type="ref"
data-reference="prop:general-k-upper-transfer">5</a> give the upper
bound, since $`0.8372914<0.83730`$.
Proposition <a href="#prop:theta" data-reference-type="ref"
data-reference="prop:theta">10</a> gives
$`\theta_1^\star+\theta_2^\star<0.48302(1+1/1.37)=5723787/6850000`$.
Finally, exact rational subtraction gives
``` math
\frac{83695}{100000}-\frac{5723787}{6850000}
 =\frac{18641}{13700000}>0.
```
 ◻

</div>

# Discussion and scope

#### What the separation establishes.

The cumulative formulation permits a certified construction above the
nonlinear-system value. It does not determine why that particular value
falls short. The loss may lie in the dual restriction used in (Brustle
et al. 2026), in the feasible construction chosen within that
restriction, or in both. In particular, we do not establish
suboptimality of the entire restricted pointwise programme or necessity
of a nonzero dual variable $`\eta`$. The finite-horizon
linear-programming characterisation and the lower-bound theorem of
(Brustle et al. 2026) remain unaffected.

#### Computation versus proof.

A floating-point double-oracle search used a $`320`$-point quantile
grid, $`64`$ time pieces and $`450`$ iterations. The reported grid value
$`0.837050`$ and profile estimate $`0.837281`$ are discovery
diagnostics, not certified continuum bounds. Restricting the adversary
to a grid can overstate a policy’s off-grid guarantee. Only the explicit
ball-arithmetic inequalities in
Propositions <a href="#prop:lowcert" data-reference-type="ref"
data-reference="prop:lowcert">7</a>,
<a href="#prop:upcert" data-reference-type="ref"
data-reference="prop:upcert">8</a> and
<a href="#prop:theta" data-reference-type="ref"
data-reference="prop:theta">10</a>, combined with the analytic
transfers, justify Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>. No numerical interval for $`k\ge3`$ is
established here.

Mixtures are convenient finite representations for search and
certification.
Proposition <a href="#prop:general-k-occupancy-domination" data-reference-type="ref"
data-reference="prop:general-k-occupancy-domination">6</a> shows that a
bounded measurable deterministic quantile policy can dominate each
finite mixture. Therefore the better certificate from the $`36`$-policy
mixture than from the illustrative $`24`$-piece policy in
Appendix <a href="#app:policy" data-reference-type="ref"
data-reference="app:policy">6</a> is not evidence that mixing is
intrinsically superior. The recovered threshold need not retain the
original time mesh; attainment of the optimal value by one bounded
threshold policy remains unproved.

#### Remaining questions.

Theorem <a href="#thm:general-k-game" data-reference-type="ref"
data-reference="thm:general-k-game">2</a> concerns each fixed $`k`$, not
a budget growing with $`n`$. Its maximum is attained in a compact
closure, not necessarily by a single implementable optimizer. It proves
neither equality of the limit with the all-horizon infimum nor an exact
numerical constant. Quantitative transfer bounds depend on the chosen
profile or policy, and are not a uniform convergence rate over the
entire continuum game. Sharper certificates for larger budgets and a
characterization of extremizers are separate problems.

#### Reproducibility and provenance.

The accompanying repository contains the rational policy mixture, layer
measure, illustrative policy, certificate programs and replay
documentation. Threshold-array row $`j`$, counted from $`1`$, contains
the threshold for $`j`$ remaining slots. A layer atom $`(x,w)`$
specifies a jump of height $`w`$ in the profile; it is not an atom of an
observation distribution. The upper transfer specifies the actual
horizon-dependent observation law.

The analytic proof covers every fixed budget. Numerical replay covers
only the supplied finite $`k=2`$ witnesses and the implemented
arithmetic checks; it is not a formal verification of the manuscript, a
proof of global numerical optimality, or an independent human peer
review. The revision separates historical search outputs from
certificate evidence and does not treat unsupported older numerical
upper estimates as results. Automated research assistance was used in
proof development, revision and internal checking. The supplied review
is advisory evidence, not an external publication endorsement.

#### Declarations.

The study uses mathematical constructions and no human-participant or
personal data; ethics approval is not applicable. Data and code are
prepared for the public repository
<https://github.com/ipitchford/iid-multiunit-prophet-limits>, with the
versioned archive assigned the reserved DOI above. These identifiers do
not by themselves assert that public release has completed. Authorship
is anonymous. No claim about undisclosed funding or competing interests
is made.

# An illustrative two-unit threshold policy

<div id="prop:det" class="proposition">

**Proposition 11** (computer-assisted). *For the rational deterministic
policy of Table <a href="#tab:policy" data-reference-type="ref"
data-reference="tab:policy">1</a> ($`T=24`$), $`W(x)\ge0.8365\,P(x)`$
for all $`x\ge0`$.*

</div>

<div class="proof">

*Certificate.* As for
Proposition <a href="#prop:lowcert" data-reference-type="ref"
data-reference="prop:lowcert">7</a> with a single policy:
$`g'(0)>1.85\times10^{-5}>0`$, the tail margin exceeds $`0.0028`$, and
the smallest certified lower bound over the $`47`$ remaining pieces
($`400`$ subintervals each) exceeds $`3.2\times10^{-5}`$. These are
conservative lower bounds, not equalities obtained by rounding displayed
decimals. ◻

</div>

<div id="tab:policy">

| time piece        | $`a_2`$ (two slots) | $`a_1`$ (one slot) |
|:------------------|:-------------------:|:------------------:|
| $`[0/24,1/24)`$   |      $`1.170`$      |     $`0.184`$      |
| $`[1/24,2/24)`$   |      $`1.303`$      |     $`0.123`$      |
| $`[2/24,3/24)`$   |      $`1.433`$      |     $`0.125`$      |
| $`[3/24,4/24)`$   |      $`1.643`$      |     $`0.158`$      |
| $`[4/24,5/24)`$   |      $`1.781`$      |     $`0.252`$      |
| $`[5/24,6/24)`$   |      $`1.911`$      |     $`0.306`$      |
| $`[6/24,7/24)`$   |      $`2.130`$      |     $`0.370`$      |
| $`[7/24,8/24)`$   |      $`2.272`$      |     $`0.439`$      |
| $`[8/24,9/24)`$   |      $`2.413`$      |     $`0.507`$      |
| $`[9/24,10/24)`$  |      $`2.650`$      |     $`0.581`$      |
| $`[10/24,11/24)`$ |      $`2.801`$      |     $`0.652`$      |
| $`[11/24,12/24)`$ |      $`2.952`$      |     $`0.733`$      |
| $`[12/24,13/24)`$ |      $`3.224`$      |     $`0.809`$      |
| $`[13/24,14/24)`$ |      $`3.374`$      |     $`0.889`$      |
| $`[14/24,15/24)`$ |      $`3.662`$      |     $`0.977`$      |
| $`[15/24,16/24)`$ |      $`3.883`$      |     $`1.072`$      |
| $`[16/24,17/24)`$ |      $`4.086`$      |     $`1.547`$      |
| $`[17/24,18/24)`$ |      $`4.483`$      |     $`2.040`$      |
| $`[18/24,19/24)`$ |      $`4.723`$      |     $`2.540`$      |
| $`[19/24,20/24)`$ |      $`5.297`$      |     $`3.068`$      |
| $`[20/24,21/24)`$ |      $`5.620`$      |     $`3.593`$      |
| $`[21/24,22/24)`$ |      $`6.009`$      |     $`4.234`$      |
| $`[22/24,23/24)`$ |      $`8.273`$      |     $`5.010`$      |
| $`[23/24,24/24)`$ |     $`10.602`$      |     $`6.587`$      |

The certified policy ($`k=2`$, $`T=24`$). On each time piece the policy
accepts an arrival with scaled tail quantile $`s\le a_2`$ when two slots
remain, and $`s\le a_1`$ when one remains. All values are exact
decimals.

</div>

<div class="thebibliography">

99 J. Brustle, S. Perez-Salazar, V. Verdugo. Splitting guarantees for
prophet inequalities via nonlinear systems. *Math. Oper. Res.* 51(2)
(2026) 877–904 (online 17 April 2025), doi:10.1287/moor.2024.0413;
arXiv:2406.17767v2. J. Brüstle. *Optimisation for prophet inequalities*.
PhD thesis, London School of Economics (2025),
doi:10.21953/lse.00004808. E. Cruz-Ossa, S. Perez-Salazar, V. Verdugo.
Competition versus complexity in multiple-selection prophet
inequalities. arXiv:2602.20398 (2026). J. Correa, P. Foncea, R. Hoeksma,
T. Oosterwijk, T. Vredeveld. Posted price mechanisms and optimal
threshold strategies for random arrivals. *Math. Oper. Res.* 46 (2021)
1452–1478. K. Fan. Minimax theorems. *Proc. Natl. Acad. Sci. USA* 39
(1953) 42–47. A. Goldenshluger, Y. Malinovsky, A. Zeevi. Optimal
single-threshold stopping rules and sharp prophet inequalities.
*J. Appl. Probab.* (2026), First View, 1–28 (online 27 July 2026),
doi:10.1017/jpr.2026.10117; arXiv:2404.12949. T. P. Hill, R. P. Kertz.
Comparisons of stop rule and supremum expectations of i.i.d. random
variables. *Ann. Probab.* 10 (1982) 336–345. R. P. Kertz. Stop rule and
supremum expectations of i.i.d. random variables: a complete comparison
by conjugate duality. *J. Multivariate Anal.* 19 (1986) 88–112.
J. Jiang, W. Ma, J. Zhang. Tightness without counterexamples: a new
approach and new results for prophet inequalities. *Proc. EC* 2023;
*Math. Oper. Res.* 51(2) (2026) 956–987 (online 2025),
doi:10.1287/moor.2023.0221; arXiv:2205.00588v5. F. Johansson. Arb:
efficient arbitrary-precision midpoint-radius interval arithmetic. *IEEE
Trans. Comput.* 66 (2017) 1281–1292. J. Kong, K. Murthy. Multiunit
i.i.d. prophet inequalities via extreme value asymptotics.
arXiv:2602.18756v2 (2026). S. Perez-Salazar, M. Singh, A. Toriello. The
IID prophet inequality with limited flexibility. *Math. Oper. Res.*
51(1) (2026) 218–254 (online 2025), doi:10.1287/moor.2022.0345;
arXiv:2210.05634. S. Perez-Salazar, V. Verdugo. Optimal guarantees for
online selection over time. arXiv:2408.11224 (2024). L. Le Cam. An
approximation theorem for the Poisson binomial distribution. *Pacific
J. Math.* 10 (1960) 1181–1197. P. Loiseau, M. Molina, V. Perchet,
S. Perez-Salazar, V. Verdugo. Kernel methods for refined prophet
inequalities. arXiv:2608.08662. M. Molina, N. Gast, P. Loiseau,
V. Perchet. Prophet inequalities: competing with the top $`\ell`$ items
is easy. *Proc. SODA* (2025) 1270–1307, doi:10.1137/1.9781611978322.38;
arXiv:2408.07616v2.

</div>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-BPV" class="csl-entry">

Brustle, Johannes, Sebastian Perez-Salazar, and Victor Verdugo. 2026.
“Splitting Guarantees for Prophet Inequalities via Nonlinear Systems.”
*Mathematics of Operations Research* 51 (2): 877–904.
<https://doi.org/10.1287/moor.2024.0413>.

</div>

<div id="ref-Brustle26" class="csl-entry">

Brüstle, Johannes. 2025. “Optimisation for Prophet Inequalities.” PhD
thesis, London School of Economics; Political Science.
<https://doi.org/10.21953/lse.00004808>.

</div>

<div id="ref-CFHOV21" class="csl-entry">

Correa, José, Patricio Foncea, Ruben Hoeksma, Tim Oosterwijk, and Tjark
Vredeveld. 2021. “Posted Price Mechanisms and Optimal Threshold
Strategies for Random Arrivals.” *Mathematics of Operations Research*
46: 1452–78.

</div>

<div id="ref-CPV26" class="csl-entry">

Cruz-Ossa, Eugenio, Sebastian Perez-Salazar, and Victor Verdugo. 2026.
*Competition Versus Complexity in Multiple-Selection Prophet
Inequalities*.

</div>

<div id="ref-GMZ" class="csl-entry">

Goldenshluger, Alexander, Yaakov Malinovsky, and Assaf Zeevi. 2026.
“Optimal Single-Threshold Stopping Rules and Sharp Prophet
Inequalities.” *Journal of Applied Probability*, 1–28.
<https://doi.org/10.1017/jpr.2026.10117>.

</div>

<div id="ref-HK82" class="csl-entry">

Hill, Theodore P., and Robert P. Kertz. 1982. “Comparisons of Stop Rule
and Supremum Expectations of i.i.d. Random Variables.” *Annals of
Probability* 10: 336–45.

</div>

<div id="ref-JMZ" class="csl-entry">

Jiang, Jiashuo, Will Ma, and Jiawei Zhang. 2026. “Tightness Without
Counterexamples: A New Approach and New Results for Prophet
Inequalities.” *Mathematics of Operations Research* 51 (2): 956–87.
<https://doi.org/10.1287/moor.2023.0221>.

</div>

<div id="ref-Johansson" class="csl-entry">

Johansson, Fredrik. 2017. “Arb: Efficient Arbitrary-Precision
Midpoint-Radius Interval Arithmetic.” *IEEE Transactions on Computers*
66: 1281–92.

</div>

<div id="ref-Kertz86" class="csl-entry">

Kertz, Robert P. 1986. “Stop Rule and Supremum Expectations of i.i.d.
Random Variables: A Complete Comparison by Conjugate Duality.” *Journal
of Multivariate Analysis* 19: 88–112.

</div>

<div id="ref-KM26" class="csl-entry">

Kong, Jieming, and Karthyek Murthy. 2026. *Multiunit i.i.d. Prophet
Inequalities via Extreme Value Asymptotics*.
<https://arxiv.org/abs/2602.18756v2>.

</div>

<div id="ref-LMPPV" class="csl-entry">

Loiseau, Patrick, Mathieu Molina, Vianney Perchet, Sebastian
Perez-Salazar, and Victor Verdugo. 2026. *Kernel Methods for Refined
Prophet Inequalities*.

</div>

<div id="ref-MGLP" class="csl-entry">

Molina, Mathieu, Nicolas Gast, Patrick Loiseau, and Vianney Perchet.
2025. “Prophet Inequalities: Competing with the Top $`\ell`$ Items Is
Easy.” *Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete
Algorithms (SODA)*, 1270–307.
<https://doi.org/10.1137/1.9781611978322.38>.

</div>

<div id="ref-PST" class="csl-entry">

Perez-Salazar, Sebastian, Mohit Singh, and Alejandro Toriello. 2026.
“The I.I.D. Prophet Inequality with Limited Flexibility.” *Mathematics
of Operations Research* 51 (1): 218–54.
<https://doi.org/10.1287/moor.2022.0345>.

</div>

<div id="ref-PSV" class="csl-entry">

Perez-Salazar, Sebastian, and Victor Verdugo. 2024. *Optimal Guarantees
for Online Selection over Time*.

</div>

</div>
