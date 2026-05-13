<!-- moved to be colocated with the paper -->
# Review: 8. Discussion

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: synthesize results without overclaiming, connect to adjacent areas responsibly, and give a clear research agenda for Bucket Brigade.

## Summary
- Broadens the lens to AI systems design, MoE, multimodal, federated learning; articulates design principles and real‑world analogies (start `src/research/papers/2024-slepian-wolf-marl.tsx:3015`).
- Covers limitations, challenging scenarios, and future directions; ends with a compelling “collective intelligence” vision (`:3330–3445`).

## Audience Fit
- Strengths: Engaging, aspirational narrative; concrete limitations section; practical design pseudo‑code.
- Risks: Several strong claims (e.g., “provably impossible,” “state‑of‑the‑art”) and AGI implications may read as overreach given current evidence; speculative cross‑domain links could distract core readers.
- Opportunity: Separate “evidence‑backed” vs “speculative outlook,” and ground cross‑domain extrapolations with caveats and citations or move them to a short “Outlook” box.

## Issues & Risks
- “Provably impossible” coordination (line `:3029`): Precise only under specific assumptions (bits‑based thresholds, fixed ρ(S), exact estimators). Recommend “information‑theoretically unlikely without sufficient capacity or bandwidth under our assumptions.”
- “State‑of‑the‑art performance” (lines `:3011`, `:3497–3512`): Needs named baselines, metrics, and CIs; consider “competitive performance” unless benchmark‑verified.
- LLM/MoE/federated parallels (around `:3120–3145`): Useful analogy, but label explicitly as analogy; avoid implying formal transfer without evidence.
- AGI/collective intelligence (lines `:3339–3445`, `:3530–3538`): Keep as Outlook; shorten and move to a sidebar to avoid overshadowing the research guidance.

## Suggestions (Structure)
- Add “What We Can Claim vs What We Hypothesize” callout with 4–6 bullets.
- Shorten the MoE/LLM extrapolations to a single paragraph with citations or move to Future Work.
- Keep “Limitations” early and explicit; cross‑reference earlier choices (MI vs KL, capacity proxies, ρ(S)).
- End with “Programmatic Next Steps” tied to Bucket Brigade (metrics to standardize, ablations to run, datasets to release).

## Wording Edits
- Replace absolutes with conditionals: “provably impossible” → “information‑theoretically infeasible under our assumptions.”
- “Bigger isn’t always better” → keep, but tie to measured knee points with error bars rather than general claim.
- Use “environment evaluates joint actions” instead of “joint decoder” unless inside analogy boxes.

## Optional Rewrite Snippet (opening + claims box)
This section steps back from experiments to reflect on what an information‑theoretic lens adds to multi‑agent learning. We highlight implications for system design, acknowledge limits, and sketch a research agenda.

What we can claim (based on evidence here)
- Observed knees in performance vs capacity near estimated conditional information thresholds in Bucket Brigade.
- Evidence of specialization under redundancy‑reducing regularization without hurting reward.
- A practical recipe to size and regularize policies using measurable information proxies.

What we hypothesize (needs broader validation)
- Generality of thresholds across domains and continuous control.
- Transfer of capacity rules to MoE/multimodal/federated settings.
- Collective‑intelligence benefits from specialized modules at scale.

## Line‑Level Notes
- Section start: `src/research/papers/2024-slepian-wolf-marl.tsx:3015`
- Strong claims: `:3011`, `:3029`, `:3497–3512`
- AGI/collective intelligence outlook: `:3339–3445`, `:3530–3538`
