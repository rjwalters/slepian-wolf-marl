# Literature Review — Slepian-Wolf MARL (v3)

## Status

This v3 review accompanies the paper's v3 bibliography (~52 entries — v2 + MIR3 + MADPO). The bibliography positions the work relative to the four nearest lines of recent literature (Section 2.7 "Closest Prior Work") plus two 2024 extensions, and to the classical theory we draw on conceptually.

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

## Issues Addressed from v2 Review

- **Abstract enumeration**: now lists all 5 predictions consistent with body.
- **$R_{\pi_i}$ definition**: now defined in Section 3.4 as $I(A_i^*; A_i \mid S)$.
- **Theorem A.3 / E.4 / E.5 downgrades**: now Conjectures with $A_i^*$ notation.
- **Notation drift in Appendix A/C/D/E**: $\mathcal{Z}_i$ inside entropies/MI replaced with $A_i^*$; $\mathcal{Z}_i$ retained only as the distribution.
- **Definition A.14**: now conditional MI, consistent with Section 6's algorithm.
- **Numbering collisions**: Propositions renumbered P.1–P.5 with their own counter; Definitions, Conjectures, Lemmas, Heuristics, Scaling Hypotheses, Proxies keep their existing prefixed labels.
- **MIR3, MADPO citations**: added in Closest Work subsection.
- **$H$ symbol clash**: Bucket Brigade uses $K=10$ houses now.
- **Aspirational language**: "should show phase transitions" → "is conjectured to show".

## Remaining Gaps (for v4 if needed)

- 2024+ work on offline / meta MARL with IT objectives (UNICORN-style frameworks).
- Connections to in-context-learning + emergent communication in foundation-model agents.
- Sequential rate--distortion with side information — flagged as formal home in Discussion, no direct derivation in this paper.
