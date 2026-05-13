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

The initial draft is published on [rjwalters.info](https://rjwalters.info/research/2024-slepian-wolf-marl) and was authored before this repo existed. Initial section-by-section reviews live in `reviews-archive/`. Going forward, paper revisions use the `pub` workflow (see `.claude/skills/pub/SKILL.md`):

```
EMPTY --> DRAFTED --> REVIEWED --> REVISED --> ... --> READY
```

Next step: run `/pub-draft` to produce `paper/slepian-wolf-marl.1/` as the first formally-versioned draft, incorporating the existing site content and the archived section reviews.

## Related Work (in this research program)

- ["Ordering Is Not Invariant"](https://github.com/rjwalters/latent-space-symmetries) — functional vs. structural equivariance in language model representations
- [Group-MoE](https://github.com/rjwalters/group-moe) — architectural follow-up enabling selective algebraic structure

## Conventions

- Papers live in `paper/` with immutable version history (see `.claude/skills/pub/SKILL.md`)
- Publication pipeline: `/pub-draft` → `/pub-review` → `/pub-revise` → `/pub-audit` → `/pub-website`
- Archived pre-workflow reviews in `reviews-archive/`
