# Slepian-Wolf MARL

## Project Overview

Distributed compression view of multi-agent reinforcement learning: each agent's policy is a lossy encoder of a latent optimal action distribution, with the environment acting as a joint decoder. Inspired by the Slepian-Wolf theorem on distributed source coding, this framework yields testable predictions about sample complexity, network capacity requirements, and the emergence of specialized roles.

## Key Idea

Standard MARL theory treats coordination without communication as a coordination problem. We treat it as a **compression problem**: agents need not exchange messages if their observations are sufficiently correlated that each can infer what the others will do. Policy capacity should scale with conditional entropy (uncertainty given teammate behavior), not with absolute environment entropy.

This reframes several MARL phenomena:
- **Why decentralized training works**: agents implicitly perform distributed source coding
- **When communication helps**: only when local uncertainty exceeds what behavior reveals
- **Why specialization emerges**: identical policies are redundant encoding under any non-trivial joint distribution

## Status

**READY** — v4 is live at [rjwalters.info](https://rjwalters.info/research/2024-slepian-wolf-marl) (review score 33/40; no critical or important issues). The paper went through four pub-workflow iterations (v1–v4) before reaching READY. Archived pre-workflow section reviews live in `reviews-archive/`.

The companion experimental testbed ([`bucket-brigade`](https://github.com/rjwalters/bucket-brigade)) is under active development and implements the Section 7 protocol. Experimental results there may warrant a v5 revision when they mature.

The pub workflow pipeline:
```
EMPTY --> DRAFTED --> REVIEWED --> REVISED --> ... --> READY
```

## Related Work (in this research program)

- [`bucket-brigade`](https://github.com/rjwalters/bucket-brigade) — experimental testbed for the paper's predictions (P1–P5); Rust-backed, 14 scenarios, active RL/Nash/evolution experiments
- ["Ordering Is Not Invariant"](https://github.com/rjwalters/latent-space-symmetries) — functional vs. structural equivariance in language model representations
- [Group-MoE](https://github.com/rjwalters/group-moe) — architectural follow-up enabling selective algebraic structure

## Paper 2 (slepian-wolf-marl-2)

Follow-on empirical paper. Thesis: conditional entropy of the heterogeneous Nash equilibrium predicts cooperation difficulty across Bucket Brigade scenarios. Standard trainers fail in high-entropy scenarios; asymmetry-aware training closes the gap.

- Draft skeleton: `paper/slepian-wolf-marl-2.1/`
- Experiments run in `../bucket-brigade`
- Detailed TODO: `TODO.md`

Key open work: run `HeterogeneousDoubleOracle` across all 14 scenarios, compute $H(A_i^*|A_{-i}^*)$ per scenario, extend tier-1 sweep, characterize and test asymmetry-aware training.

## Conventions

- Papers live in `paper/` with immutable version history (see `.claude/skills/pub/SKILL.md`)
- Thread naming: `slepian-wolf-marl.N` for Paper 1, `slepian-wolf-marl-2.N` for Paper 2
- Publication pipeline: `/pub-draft` → `/pub-review` → `/pub-revise` → `/pub-audit` → `/pub-website`
- Archived pre-workflow reviews in `reviews-archive/`
