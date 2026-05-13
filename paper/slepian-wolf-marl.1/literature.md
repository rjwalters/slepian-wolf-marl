# Literature Review — Slepian-Wolf MARL

## Status

**Skeleton only.** This v1 paper was ported as-is from the rjwalters.info TSX draft (Nov 2025). The TSX draft cited references inline as plain text rather than maintaining a literature review document. A proper literature review should be written during the `/pub-revise` pass that produces v2.

## Positioning

The paper applies a distributed source coding lens to multi-agent reinforcement learning. The core claim is that learned policies act as lossy encoders of a latent optimal action distribution, with the environment serving as a joint decoder. The framework is *inspired by* Slepian-Wolf rather than a direct application — the MARL setting is sequential, lossy, and non-i.i.d., so the original theorem does not literally apply.

## Areas to Survey in v2

### Information-theoretic MARL
- Wen et al. — information-theoretic regularization in MARL
- MAVEN — variational exploration via mutual information
- Foerster et al. — differentiable inter-agent communication
- Eccles et al. — biases for emergent communication

### Distributed source coding (theory)
- Slepian & Wolf (1973) — original distributed lossless coding theorem
- Wyner-Ziv (1976) — lossy source coding with side information
- Cover & Thomas — textbook treatment of distributed coding
- Berger — rate-distortion theory background

### MARL coordination
- CTDE (centralized training, decentralized execution) — VDN, QMIX, MADDPG
- Independent learners — IPPO, IQL
- Emergent communication / role specialization papers

### Connections to representation learning
- Information bottleneck (Tishby et al.)
- Mutual-information lower bounds (InfoNCE, MINE)
- Conditional entropy as a learning signal

## Known Issues from Archived Reviews

See `../reviews-archive/` for section-level reviews of the v1 draft (sourced from the pre-workflow rjwalters.info content). Major themes flagged for revision:

- Sharpen the conceptual gap between Slepian-Wolf (lossless, i.i.d.) and the MARL setting (lossy, sequential)
- Differentiate from prior information-theoretic MARL work
- Clarify which predictions are novel vs. corollaries of standard theory
- Tighten the algorithmic framework section — currently speculative
