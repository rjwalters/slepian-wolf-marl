# Literature Review — Slepian-Wolf MARL 2

## Headline finding from the search

**The structural claim is established prior art; the predictive claim is novel.**

The core structural claim of this paper — that symmetric self-play algorithms
cannot reach asymmetric Nash equilibria — has direct, recent, formal precedent
in **Emmons et al. (ICML 2022)**: in common-payoff games, every local optimum
of a symmetric strategy profile is a global Nash equilibrium, *and* mixed local
optima are unstable under joint asymmetric deviations. The game-theoretic
existence result that symmetric games can have *only* asymmetric NE is older
still (Fey 2012).

This reshapes Paper 2's contribution:
- **Not novel:** the structural failure mode itself
- **Novel:** using $\tilde{H}_i := H(A_i^*|A_{-i}^*)$ computed from a
  heterogeneous Nash as a *quantitative scenario-difficulty predictor*; the
  empirical phase-diagram demonstration; possibly the explicit
  `HeterogeneousDoubleOracle` algorithm itself.

Paper 2 should be positioned as: *Emmons gave us the qualitative failure mode;
we give a forecastable scenario-difficulty metric grounded in the heterogeneous
Nash's information structure.*

## Inherited from companion paper

Full v4 bibliography (53 entries) at `paper/slepian-wolf-marl.4/paper.tex`.
Key inherited citations:
- Slepian & Wolf (1973), Wyner & Ziv (1976)
- ROMA, RODE, PMIC, IMAC, MIR3, MADPO, Graph-IB
- Cover & Thomas; Miller-Madow
- Schulman et al. PPO; Rashid et al. QMIX; Lowe et al. MADDPG; Foerster et al. COMA

---

## Area 1: Symmetric self-play vs. asymmetric Nash — PRIOR ART EXISTS

**`emmons2022symmetric`** — Emmons, S., Oesterheld, C., Critch, A., Conitzer,
V., & Russell, S. (2022). For Learning in Symmetric Teams, Local Optima are
Global Nash Equilibria. *ICML 2022, PMLR 162: 5924–5943* (spotlight).
arXiv:2207.03470. **Direct precedent for this paper's structural claim.**
Proves any locally optimal symmetric strategy profile in a common-payoff game
is a global Nash equilibrium, and that mixed local optima are unstable under
joint, asymmetric deviations. Must be cited prominently; Paper 2 builds the
*quantitative* extension of this *qualitative* result.

**`fey2012symmetric`** — Fey, M. (2012). Symmetric games with only asymmetric
equilibria. *Games and Economic Behavior*, 75(1), 424–427. The canonical
existence proof that symmetric games can fail to admit any symmetric Nash
equilibrium. Establishes the structural premise that Paper 2's
`asymmetric_only` cells empirically instantiate.

**`xefteris2023continuous`** — Xefteris, D., et al. (2023). Symmetric games
with only asymmetric equilibria: continuous payoff functions. *Economic Theory
Bulletin*, 11(1). Extends Fey (2012) to continuous payoffs — closes the gap
that this is a discrete-game artifact.

**`harsanyi1988general`** — Harsanyi, J.C. & Selten, R. (1988). *A General
Theory of Equilibrium Selection in Games*. MIT Press. Classical equilibrium
selection: in symmetric games, advocates the symmetric NE. Cite as the
methodological convention symmetric self-play implicitly implements — which
becomes the failure mode in `asymmetric_only` cells.

**`duersch2014zerosum`** — Duersch, P., Oechssler, J., & Schipper, B.M.
(2014). Symmetric zero-sum games with only asymmetric equilibria. *Games and
Economic Behavior*. Companion result for zero-sum; useful if reviewers want
completeness across payoff regimes.

## Area 2: Double Oracle — canonical and relevant variants

**`mcmahan2003planning`** — McMahan, H.B., Gordon, G.J., & Blum, A. (2003).
Planning in the Presence of Cost Functions Controlled by an Adversary
(Double Oracle). *ICML 2003*. Canonical origin.

**`lanctot2017unified`** — Lanctot, M., Zambaldi, V., Gruslys, A., Lazaridou,
A., Tuyls, K., Pérolat, J., Silver, D., & Graepel, T. (2017). A Unified
Game-Theoretic Approach to Multiagent Reinforcement Learning (PSRO).
*NeurIPS 2017*. arXiv:1711.00832. The standard generalization to deep MARL.
Cite as the lineage for `HeterogeneousDoubleOracle`.

**`mcaleer2021xdo`** — McAleer, S., Lanier, J., Fox, R., & Baldi, P. (2021).
XDO: A Double Oracle Algorithm for Extensive-Form Games. *NeurIPS 2021*.
arXiv:2103.06426. Extension to extensive-form with convergence guarantees;
relevant for any DO theory discussion.

**Note on heterogeneous variants:** No published DO variant explicitly
enforces per-position heterogeneous best response. PSRO is agnostic but
inherits the symmetric-policy-class constraint when run with shared parameters.
This makes `HeterogeneousDoubleOracle` a candidate algorithmic contribution
(though the paper's main contribution is the predictive index, not the solver).

## Area 3: Free-riding in cooperative MARL (2020+)

**`liu2023lazy`** — Liu, B., Pu, Z., Pan, Y., Yi, J., Liang, Y., & Zhang, D.
(2023). Lazy Agents: A New Perspective on Solving Sparse Reward Problem in
Multi-agent Reinforcement Learning. *ICML 2023, PMLR 202*. Current
formalization of the lazy/free-riding phenomenon under sparse rewards;
proposes causal-effect intrinsic rewards. Direct comparator for any
asymmetry-aware training method.

**`ivanov2023mediated`** — Ivanov, D., et al. (2023). Mediated Multi-Agent
Reinforcement Learning. arXiv:2306.08419. Trains a mediator alongside agents
to maximize social welfare under cooperation-incentive constraints — the
mechanism-design route to escaping free-riding. Complements the
training-side methods.

**`vanderheiden2022transfer`** — Van Der Heiden, T., Weiss, C., Nagaraja, N.S.,
Gavves, E., Salzmann, T., & van Hoof, H. (2022). Reliably Re-Acting to
Partner's Actions with the Social Intrinsic Motivation of Transfer
Empowerment. *Artificial Life 2022* / arXiv:2203.03355. Intrinsic-motivation
method targeting under-reaction failures; relevant comparator.

**`pmic` (inherited)** — PMIC (Li et al. 2022) already in companion paper.
Worth re-citing here for the specific claim that naïve MI maximization can
entrench free-riding.

## Area 4: Heterogeneous-agent / role-conditioned MARL

**`bettini2023hetgppo`** — Bettini, M., Shankar, A., & Prorok, A. (2023).
Heterogeneous Multi-Robot Reinforcement Learning (HetGPPO). *AAMAS 2023*.
arXiv:2301.07137. Empirically demonstrates that homogeneous methods fail
under strong heterogeneous requirements and HetGPPO succeeds. **Existence
proof in the literature that the failure mode Paper 2 predicts is
observable in practice.** Should be cited alongside Emmons (2022) as the
empirical complement.

**`zhong2024harl`** — Zhong, Y., Kuba, J.G., Hu, S., Ji, J., & Yang, Y.
(2024). Heterogeneous-Agent Reinforcement Learning (HARL/HAPPO/HATRPO).
*JMLR* 25, paper 23-0488. arXiv:2304.09870. Provably-correct, parameter-
sharing-free trust region method with monotonic improvement guarantees.
HAPPO is a natural baseline for asymmetry-aware training.

**`christianos2021selective`** — Christianos, F., Papoudakis, G., Rahman,
A., & Albrecht, S.V. (2021). Scaling Multi-Agent Reinforcement Learning with
Selective Parameter Sharing (SePS). *ICML 2021, PMLR 139*. Intermediate
between full and zero sharing; position Paper 2's approach against this.

**`christianos2020seac`** — Christianos, F., Schäfer, L., & Albrecht, S.V.
(2020). Shared Experience Actor-Critic (SEAC). *NeurIPS 2020*. Canonical
non-fully-shared MARL.

**`li2024kaleidoscope`** — Li, X., et al. (2024). Kaleidoscope: Learnable
Masks for Heterogeneous Multi-agent Reinforcement Learning. *NeurIPS 2024*.
arXiv:2410.08540. Most recent (2024) adaptive partial-parameter-sharing —
current SOTA for the homogeneous-heterogeneous tradeoff Paper 2 formalizes.

## Area 5: Correlated equilibria and information structure

**`aumann1974subjectivity`** — Aumann, R.J. (1974). Subjectivity and
Correlation in Randomized Strategies. *J.\ Math.\ Economics*, 1(1), 67–96.
Original correlated equilibrium paper. **Key relevance:** allowing privately
observed signals expands the equilibrium set beyond Nash; a CE is a NE of an
augmented game with a correlation signal. Directly parallel to Paper 1's
conditional-entropy framing: information about teammate actions changes the
equilibrium structure.

**`marris2021ce`** — Marris, L., Muller, P., Lanctot, M., Tuyls, K., &
Graepel, T. (2021). Multi-Agent Training beyond Zero-Sum with Correlated
Equilibrium Meta-Solvers. *ICML 2021*. Replaces the NE meta-solver in PSRO
with a CE meta-solver; shows CE outperforms NE in cooperative-ish MARL.
**Most direct prior work supporting the conditional-entropy framing in deep
MARL.** Cite as the strongest evidence that conditional/correlated structure
matters for MARL practice.

**`hart2000simple`** — Hart, S. & Mas-Colell, A. (2000). A Simple Adaptive
Procedure Leading to Correlated Equilibrium. *Econometrica*, 68(5),
1127–1150. Regret-matching → CE; pair with Foster-Vohra.

**`foster1997calibrated`** — Foster, D.P. & Vohra, R.V. (1997). Calibrated
Learning and Correlated Equilibrium. *Games and Economic Behavior*, 21(1–2),
40–55. Foundational learning-to-CE result.

---

## Open questions still to resolve

1. **`HeterogeneousDoubleOracle` algorithmic novelty.** Worth one more
   targeted search for "per-position best response" + "double oracle" in 2024–
   2026 venues before claiming algorithmic novelty in the paper.
2. **`anvil_pub.1` workshop paper positioning.** When the bucket-brigade
   companion paper drafts its related work, ensure overlap with Paper 2's
   related work is intentional (cite each other; don't duplicate the framing).
3. **Strategic risk aversion (arXiv:2602.21515).** Cited in the search; worth
   a closer read — it argues a non-Nash solution concept escapes free-riding.
   Could be either a baseline or a competing framing.
