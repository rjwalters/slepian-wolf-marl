<!-- moved to be colocated with the paper -->
# Global Review and Summary — “Distributed Compression of Latent Game Structure: A Slepian–Wolf Perspective on Multi‑Agent Learning”

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: deliver a clear, rigorous, and reproducible research guide for the Bucket Brigade program while remaining accessible and honest about scope.

## Big Wins
- Cohesive conceptual lens: policies as lossy encoders; environment evaluates joint actions. Strong throughline from intro to experiments.
- Actionable predictions and an environment (Bucket Brigade) designed to measure information quantities alongside performance.
- Practical algorithms and diagnostics that can guide engineering decisions.

## Cross‑Cutting Issues (to resolve globally)
- Notation (distributions vs random variables): Use random variables consistently for information quantities: S (state), O_i = Ω_i(S), A_i* (teacher/optimal action), A_i (learned action). Replace H(𝒁_i) with H(A_i*), H(𝒁_i|𝒁_{−i}) with H(A_i*|A_{−i}*), and R_{π_i} with I(A_i*; A_i | S). Key references to fix: `src/research/papers/2024-slepian-wolf-marl.tsx:3839`, `:5414`, `:5616`.
- R_{π_i} definition: Do one of the following everywhere:
  - MI view (preferred): R_{π_i} := I(A_i*; A_i | S) (bits), or
  - Rename to F_{π_i} for KL fidelity if using E[ D_KL(𝒁_i(·|S) || π_i(·|O_i)) ]. Avoid mixing MI and KL. Fix at: `src/research/papers/2024-slepian-wolf-marl.tsx:3839`, `:1816`.
- Units and base distribution: State ρ(S) (stationary under teacher or a fixed behavior policy) wherever expectations/entropies appear; keep bits (log base 2) consistent.
- Capacity proxy: α·b·|θ| is heuristic; present as “capacity proxy” and pair with additional proxies (weight compression bits, PAC‑Bayes KL, pruned parameter count). Adjust language in predictions (5.1) and A.6. References: `:1440–1510`, `:3969–3980`.
- “Joint decoder” metaphor: Outside analogy boxes, prefer “environment evaluates joint actions.” References: abstract and intro `:57`, `:140`.
- Discrete vs continuous: Scope core results/metrics to discrete actions; defer continuous to Appendix A.10 and D with explicit differential entropy notes.
- Estimation and statistics: Add CIs everywhere information metrics are reported; prefer plug‑in with Miller–Madow (discrete) and bootstrap CIs; keep neural MI bounds offline and labeled as lower bounds.
- Redundancy penalty and measurement: Penalizing I(π_i;π_j) at action level can harm synchrony; prefer representation‑level redundancy (e.g., CCA/HSIC on Ẑ_i) or conditional MI I(π_i;π_j | S). Update Algorithmic Framework and metrics. References: `:1816`, `:1700–1760`, `:5414`.
- Communication threshold: Introduce message RV M and define Δ_i := H(A_i*|O_i) − H(A_i*|O_i, M); relate benefit to cost; clarify role of A_{−i}*. References: `:1666–1720`, A.8 `:4035–4040`.
- Claims calibration: “If and only if” (strong conjecture), “state‑of‑the‑art,” “provably impossible,” and phase‑transition “theorem” should be softened or clearly scoped; proofs moved to propositions/sketches as needed. References: `:1078`, `:3011`, `:3029`, Appendix E `:6165–6230`.

## Prioritized Edits
- P0 (must fix before broad release)
  - Unify information notation (A_i*, A_i, ρ(S)), redefine/rename R_{π_i}; sweep fixes across Abstract/Intro/Policies/Conjecture/Appendix A/D. Key lines: `:3839`, `:5414`, `:5616`.
  - Reframe capacity as heuristic; add capacity proxies and CIs in Implications (5.1) and Experiments (7.x). Lines: `:1440–1510`, `:2542`.
  - Standardize measurement/logging and add CIs to all information metrics; reflect in Appendix C/D and Section 7. Lines: `:5458`, `:5630–5680`.
  - Replace “joint decoder” wording outside analogy boxes. Lines: `:57`, `:140`.

- P1 (high value)
  - Move strong form conjecture to “idealized” box; lead with approximate plain‑language form; add “Units & Estimation” callout. Lines: `:1078`, `:1034`.
  - Adjust redundancy penalty to representation‑level or conditional; add caution about synchrony. Lines: `:1816`, `:1700–1760`.
  - Clarify Discrete vs Continuous scope; mark continuous as future work; add unit conversion (nats→bits) notes in D.2.2. Lines: `:5250`, `:5686–5740`.

- P2 (polish)
  - Tighten Abstract to ~180 words; move examples to Intro.
  - Shorten Discussion AGI outlook; separate “evidence” vs “speculation.” Lines: `:3339–3445`, `:3530–3538`.
  - Convert Theorem labels to Proposition/Heuristic where proofs are sketches (A.4, A.6, E.2).

## Unified Definitions & Notation
- Random variables: S, O_i = Ω_i(S), A_i* ~ 𝒁_i(·|S), A_i ~ π_i(·|O_i), optional Ẑ_i = encoder(O_i).
- Information quantities:
  - H(A_i*), H(A_i*|A_{−i}*), I(A_i*; A_i | S), I(Ẑ_i; Ẑ_j), etc.
- Distribution: Explicitly state ρ(S) for every expectation; default to stationary under π* for teacher‑based metrics.

## Measurement & Reporting Standard
- Logging schema (per time step): (t, S_t hash/features, O_i^t, A_i^{*,t}, A_i^t, R_i^t).
- Estimators: discrete plug‑in + Miller–Madow; bootstrap CIs (by episode). Continuous: KSG/KDE with unit conversion.
- Reporting: Always show mean ± 95% CI across ≥20 seeds for metrics and phase diagrams. Annotate ρ(S) and estimator choices.

## Experimental Protocol Standard
- Capacity: sweep width/depth/quantization; plot performance vs multiple capacity proxies (|θ|, compression bits, PAC‑Bayes KL, pruned params); mark conditional entropy threshold with CI.
- Sample complexity: measure episodes to ε for multiple ε; fit scaling; compare linear‑in‑H vs alternatives.
- Specialization: use representation‑level redundancy (CCA/HSIC) and role entropy; ablate λ_red; test synchrony tasks.
- Communication: define M, estimate Δ_i, sweep bandwidth/noise; compare implicit vs explicit channels.
- Symmetry: report permutation invariance “in expectation” across seeds; probe robustness to small asymmetries.

## Writing & Presentation Guidance
- Plain‑language boxes: high‑level conjecture; “Units & Estimation” quick reference; “What to remember” after core concepts.
- Move strong theoretical claims to clearly labeled idealized/heuristic boxes with assumptions.
- Keep equations where they add clarity; place derivations in appendices.

## Appendix Actions
- Appendix A: Replace MI/KL mix (R_{π_i}) with chosen path; relabel heuristic “theorems”; add RV/ρ(S) box.
- Appendix B: Fix entropy estimator to use A_i* (teacher) not random actions; clarify MI usage (offline vs loss surrogates); seed and determinism.
- Appendix C: Add oracle computation methods; seeding/determinism; scenario configs + schema; logging schema; clarify discrete scope.
- Appendix D: Add Dirichlet smoothing and conditional‑Y guards; unit conversion notes; CI column in tables.
- Appendix E: Restate linear‑Gaussian result with log‑det covariances and assumptions; relabel phase‑transition argument as heuristic; improve sensitivity methods.

## Proposed Timeline
- Week 1: P0 changes (notation, capacity language, measurement/CI, wording fixes). Update Abstract/Intro/Policies/Conjecture/Implications/Appendix A/C/D.
- Week 2: P1 edits (redundancy objective/metrics, discrete vs continuous scope, D.2.2 unit notes). Update Algorithmic Framework, Experiments, Appendix B.
- Week 3: P2 polish (Abstract, Discussion/Conclusion tone, label heuristics) and finalize figures with CI overlays.

## One‑Paragraph Abstract (Broader Audience)
Multi‑agent systems often need to coordinate without reliable communication. We show how an information‑theoretic lens helps design such systems: treat each agent’s policy as compressing just the task‑relevant information that others can’t infer, and size policies to match that “conditional information.” This view yields practical rules of thumb—where performance “turns on,” why agents specialize, and when adding a communication channel helps—and it suggests concrete metrics to measure in our Bucket Brigade environment. We standardize how to estimate these quantities with uncertainty, report results across random seeds, and connect them to network design. The result is a clear, testable guide for building scalable, cooperative multi‑agent systems.

---

Key source anchors to revisit: `src/research/papers/2024-slepian-wolf-marl.tsx:57`, `:140`, `:1816`, `:3839`, `:5414`, `:5616`, `:1440–1510`, `:2542`, `:1666–1720`, `:3011`, `:3029`, `:6165–6230`.
