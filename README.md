# Slepian-Wolf MARL

**Distributed Compression of Latent Game Structure: A Slepian-Wolf Perspective on Multi-Agent Learning**

Robot teams in jammed communication zones. Distributed sensors that can't flood the network. These systems must coordinate without talking to each other. This paper proposes viewing multi-agent reinforcement learning (MARL) through the lens of distributed source coding: each agent's policy acts as a lossy encoder, the environment as a joint decoder.

The framework is inspired by the Slepian-Wolf theorem (1973), which showed that two parties with correlated data can compress just as efficiently without coordination as with it. Our setting differs (sequential, lossy, not i.i.d.), but the core insight transfers: each agent only needs to encode what teammates cannot infer from their own observations.

The paper is **READY** (v4, 33/40 review score). The current draft is live at [rjwalters.info](https://rjwalters.info/research/2024-slepian-wolf-marl). The experimental testbed (Bucket Brigade) is under active development in the companion repo [`bucket-brigade`](https://github.com/rjwalters/bucket-brigade).

## Predictions

- Policy capacity should scale with **conditional entropy** — the uncertainty that remains after accounting for teammates' information.
- Agents should **specialize** to avoid redundant encoding.
- Explicit communication helps only when local uncertainty exceeds what behavior reveals.
- Decentralized training can match centralized performance when policies coordinate via correlated observations rather than messages.

## Repository Layout

```
paper/                          # LaTeX paper, versioned via the pub workflow
  slepian-wolf-marl.N/          # Draft version N
    paper.tex
    paper.pdf
    figures/
    literature.md
  slepian-wolf-marl.N.review/   # Review (read-only sibling)
    review.md
reviews-archive/                # Initial section-level reviews (pre-pub workflow)
```

## Related Work

- [`bucket-brigade`](https://github.com/rjwalters/bucket-brigade) — the experimental testbed implementing the paper's Section 7 protocol; under active development.
- ["Ordering Is Not Invariant"](https://github.com/rjwalters/latent-space-symmetries) — empirical evidence on functional vs. structural equivariance in transformer representations.
- [Group-MoE](https://github.com/rjwalters/group-moe) — architectural follow-up giving models algebraic fixed-function units.

## Workflow

Publication work follows the `pub` skill (see `.claude/skills/pub/SKILL.md`):

```
EMPTY --> DRAFTED --> REVIEWED --> REVISED --> ... --> READY
```

The paper is currently at **READY** (v4). Run `/pub-review` to score a new version or `/pub-revise` to incorporate new experimental findings into the next revision.
