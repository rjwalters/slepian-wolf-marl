# Literature Review — Slepian-Wolf MARL (v2)

## Status

This v2 review accompanies the paper's v2 bibliography (~50 entries). It positions the work relative to the four nearest lines of recent literature (now explicitly engaged in Section 2.7 "Closest Prior Work") and to the classical theory we draw on conceptually.

## Positioning

We treat the Slepian-Wolf theorem as a **conceptual lens** for multi-agent reinforcement learning, not as a theorem we apply. Their setting (lossless block coding of i.i.d. sources, joint decoder, asymptotic block length) is incompatible with ours (lossy policies, sequential non-i.i.d. data, environment-as-evaluator rather than decoder). The lens motivates the choice of $H(A_i^* \mid A_{-i}^*)$ as the central quantity, the predictions in Section 5, and the conditional-MI regularizer in Section 6. It does not give us free theorems; the conjectures in Section 4 and Appendix A are stated and tested on their own footing.

## Closest Prior Work (engaged in Section 2.7)

### MARL with information-theoretic regularization for role/specialization emergence

- **ROMA** (Wang et al., ICML 2020) — stochastic role embeddings via identifiability + specialization regularizers; closest in spirit to our Prediction 3 (specialization).
- **RODE** (Wang et al., ICLR 2021) — role-based action-space decomposition.
- **PMIC** (Li et al., ICML 2022) — *contradicts* naive MI minimization between agents' behaviors; demonstrates that selective MI control (maximize for good, minimize for bad collaboration) is needed. We take this as evidence that our redundancy penalty must condition on task signal.

### MARL communication and information bottleneck

- **IMAC** (Wang et al., ICML 2020) — information bottleneck for limited-bandwidth multi-agent communication; closest to our Prediction 4 (communication threshold).
- **DIAL / CommNet / TarMAC** (Foerster 2016; Sukhbaatar 2016; Das 2019) — learned communication baselines for our P4 experiments.
- **EMC** (Eccles et al., NeurIPS 2019) — biases for emergent communication.

### Information bottleneck and IT representation learning

- **Conditional Entropy Bottleneck** (Fischer, Entropy 2020) — formal home for our conditional-MI penalty $I(\hat{Z}_i; \hat{Z}_j \mid R)$.
- **Variational IB** (Alemi et al., ICLR 2017) — implementation backbone for the compression term $I(\hat{Z}_i; O_i)$.
- **Deterministic IB** (Strouse & Schwab, 2017), **Barlow Twins** (Zbontar et al., 2021).

### Rate-distortion / bounded rationality in RL

- **Ortega & Braun (2013)**, **Genewein et al. (2015)** — bounded rationality as information-processing cost. Connects to our use of a Boltzmann optimal-action distribution.
- **Grau-Moya et al. (2018)** — IT in two-player games.

### Empowerment / intrinsic motivation

- **Klyubin et al. (2005)**, **Mohamed & Rezende (2015)**, **DIAYN** (Eysenbach et al., 2018) — adjacent but conceptually distinct (action-state MI vs. policy-fidelity).

### MARL methods (CTDE / baselines for Section 7)

- **VDN, QMIX, MADDPG, COMA** (Sunehag 2018; Rashid 2018; Lowe 2017; Foerster 2018).
- **PPO** (Schulman et al., 2017) — independent-learner baseline.
- **MAVEN** (Mahajan et al., 2019) — variational MI for exploration in MARL.
- **Social Influence** (Jaques et al., ICML 2019) — MI-driven multi-agent objective.

### Dec-POMDPs / team theory (for hardness context)

- **Bernstein et al. (2002)** — NEXP-completeness of optimal Dec-POMDP.
- **Oliehoek & Amato (2016)** — comprehensive treatment.
- **Marschak & Radner (1972)** — team theory.
- **Witsenhausen (1968)** — nonlinear-beats-linear counterexample.

### Distributed source coding (theoretical roots)

- **Slepian & Wolf (1973)** — original distributed lossless coding theorem.
- **Wyner & Ziv (1976)** — lossy source coding with side information.
- **Cover & Thomas (2006)**, **Berger (1971)**, **Csiszár & Körner (2011)** — textbook treatments.

### Distinct namespace overlap

- **"Coding for Distributed Multi-Agent Reinforcement Learning"** (Wang et al., 2021, arXiv:2101.02308) — title-collision with this paper. Addresses straggler coding in distributed gradient computation, *not* the policy-as-encoder analogy. We cite to disambiguate.

## Issues Addressed from v1 Review

- **Bibliography expansion**: v1 had 12 entries; v2 has ~50, covering all inline citations.
- **ROMA / RODE / PMIC / IMAC engagement**: now in Section 2.7 with 2–4 sentences each.
- **PMIC counterexample**: now drives the design choice to condition the redundancy penalty on task signal.
- **Conditional entropy bottleneck**: now cited as formal home for $I(\hat{Z}_i;\hat{Z}_j\mid R)$.
- **Coding-for-DMARL disambiguation**: explicit citation and one-line distinguish.

## Remaining Gaps (for v3 if needed)

- Recent (2023–2025) work on offline / meta MARL with IT objectives (e.g., UNICORN-style frameworks).
- Robust MARL via MI regularization (Bo An et al., 2025) — relevant to the conjecture's robustness implications.
- Connections to in-context-learning + emergent communication in foundation-model agents.
