<!-- moved to be colocated with the paper -->
# Review: Abstract

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: guide Bucket Brigade research narrative while remaining accessible.

## Summary
- Frames MARL as distributed compression; policies as lossy encoders, environment as a joint decoder (src/research/papers/2024-slepian-wolf-marl.tsx:57).
- Cites Slepian–Wolf as the inspirational result; claims hinge on conditional information and predict capacity/sample complexity (src/research/papers/2024-slepian-wolf-marl.tsx:71).
- Positions the work as bridging information theory and MARL.

## Audience Fit
- Strength: Clear real‑world analogies (robots, sensors) and minimal equations.
- Risk: Terms like “joint decoder,” “lossy encoder,” and “conditional entropy” may require quick inline definitions; otherwise they will read as jargon.
- Scope: The abstract is long (multiple paragraphs). For a broader audience, aim for ~150–200 words focused on motivation, one key insight, and practical takeaways.

## Issues & Risks
- Joint decoder metaphor: Could confuse readers into thinking the environment reconstructs a source (it doesn’t). Consider rephrasing to “evaluates joint behavior” (src/research/papers/2024-slepian-wolf-marl.tsx:57).
- Overclaim around capacity prediction: “We can predict how large neural networks need to be …” reads strong without caveats; soften to “we hypothesize/predict and test” (src/research/papers/2024-slepian-wolf-marl.tsx:71).
- Slepian–Wolf scope: Emphasize the analogy, not direct application; explicitly say “lossy, sequential setting” differs from the theorem’s assumptions.
- Length and density: Five paragraphs is heavy for an abstract; consider compressing and moving secondary details (e.g., weather/sensor examples) into the Introduction.

## Suggestions
- Define once, briefly: “lossy encoder (compresses with some distortion)”; “conditional entropy (unpredictable information left after using teammates’ behavior).”
- Replace “joint decoder” with “joint evaluator” or “environment evaluates joint actions” to avoid reconstructive connotations.
- Add a one‑sentence statement about Bucket Brigade as the guiding empirical testbed to connect to the research program.
- End with concrete reader value: an intuition for when decentralized training can match centralized and how to size/regularize policies.

## Optional Rewrite (≈180 words)
Multi‑agent systems often must learn to coordinate without reliable communication—for example, robot teams in noisy environments or distributed sensors with limited bandwidth. We introduce an information‑theoretic perspective on this problem: treat each agent’s policy as a lossy encoder of task‑relevant strategic information, and view the environment’s reward as evaluating how well the agents’ encodings combine.

Inspired by results on distributed compression (Slepian–Wolf), our central intuition is that each agent needs to learn only the parts of the strategy that teammates cannot infer from their own experience—the “conditional” information. This lens yields practical predictions: when policies have enough effective capacity to capture their share of conditional information, decentralized learning can match centralized performance; agents naturally specialize to avoid redundancy; and explicit communication becomes useful when local uncertainty exceeds what can be inferred from others.

We outline empirical tests of these predictions in our Bucket Brigade project, a controllable multi‑agent environment designed to measure information‑theoretic quantities alongside performance. The result is a conceptual guide and set of tools for designing scalable coordination with minimal communication.

## Line‑Level Notes
- joint decoder wording: src/research/papers/2024-slepian-wolf-marl.tsx:57
- conditional entropy promise: src/research/papers/2024-slepian-wolf-marl.tsx:71
