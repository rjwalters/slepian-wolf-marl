<!-- moved to be colocated with the paper -->
# Review: Appendix A — Mathematical Details

Audience: 1st–2nd year grad students (ML + basic info theory). Goal: make definitions precise, align units/variables, and calibrate theorem status (theorem vs proposition vs conjecture) so claims are rigorous yet accessible.

## Summary
- Content spans: A.3 policy-encoding framework, A.4 distributed learning bounds (necessity/sufficiency), A.5 sample complexity, A.6 network capacity, A.7 specialization, A.8 communication value, A.9 convergence, A.10 extensions (continuous, non‑stationary), and A.11 summary.
- Key formal items: Definition A.12 and Theorem A.1–A.10 (see `src/research/papers/2024-slepian-wolf-marl.tsx:3826`, `:3837`, `:3843`, `:3863`, `:3891`, `:3910`, `:3969`, `:3995`, `:4035`, `:4052`).

## Rigor and Consistency
- Random variables vs distributions: Entropies/MI should be defined over random variables (e.g., actions), not distribution‑valued symbols 𝒁_i. Use A_i* for teacher/optimal action and A_i for learned action.
- Base distribution ρ(S): State explicitly the distribution over states for all expectations (stationary under π, behavior policy, or oracle). Keep it consistent across results.
- Units: Conditional entropy H(·) and MI are in bits. Capacity proxies like |θ| are dimensionless counts; avoid equating them directly without a mediating description‑length notion.

## Critical Issues
1) Definition A.12 / Information rate (lines `:3837–:3843`)
- Current: R_{π_i} = I(𝒁_i; π_i) = E_s[D_KL(𝒁_i(·|s) || π_i(·|Ω_i(s)))]. The RHS is a KL fidelity term, not mutual information between random variables; the LHS uses distribution symbols inside MI.
- Fix:
  - Information view (recommended): Define random variables S, O_i = Ω_i(S), A_i* ~ 𝒁_i(·|S), A_i ~ π_i(·|O_i). Set R_{π_i} := I(A_i*; A_i | S). Units: bits.
  - Fidelity view (alternative): Define F_{π_i} := E_{S,O_i}[D_KL(𝒁_i(·|S) || π_i(·|O_i))]. Do not call this “information rate”.

2) Necessity/Sufficiency bounds (A.4; lines `:3863–:3896`)
- Theorem A.2 (“lower bound on information rate”) and A.3 (“achievability”) need clear assumptions. For A.2, a Fano‑style argument can connect action mismatch probability to H(A_i*|A_{−i}*). For A.3, achievability requires finite state/action spaces, infinite data, universal approximation, and optimal optimization.
- Action: List assumptions before each statement; consider demoting “Theorem” → “Proposition/Conjecture” if proofs remain sketches.

3) Sample complexity (A.5; lines `:3910–:3920`)
- Current derivation uses a coupon‑collector‑style step; not standard for policy learning and likely overstates 2^H dependence.
- Action: Frame as a scaling hypothesis and/or derive PAC‑style bounds with covering numbers/VC/Rademacher or PAC‑Bayes. Include capacity/complexity terms explicitly and state the distributional assumptions.

4) Capacity (A.6; lines `:3969–:3980`)
- “Effective capacity” ≈ α·b·|θ| is heuristic. Without a formal coding argument or MDL/PAC‑Bayes link, Theorem A.5/A.6 should be labeled as heuristic guidelines.
- Action: Replace with description‑length proxies (compressed weight bits), PAC‑Bayes KL from prior to posterior, or effective dimension. If α·b·|θ| is kept, mark as “Empirical Proxy” not a theorem.

5) Specialization and redundancy (A.7; lines `:3995–:4014`)
- Penalizing I(π_i; π_j) at the action level can suppress necessary synchrony. Prefer conditional MI (I(π_i;π_j | S) or | A_i*) or representation‑level redundancy I(Ž_i; Ž_j). Clarify which variable level is penalized.

6) Communication value (A.8; lines `:4035–:4040`)
- Formalize with a message variable M and define Δ_i := H(A_i*|O_i) − H(A_i*|O_i, M). A principled threshold compares Σ_i Δ_i against channel cost. Cite Wyner–Ziv (lossy with side information) for analogy.

7) Convergence (A.9; lines `:4052–:4064`)
- Convergence of InfoMARL requires standard assumptions (smoothness/Lipschitz of objectives, unbiased stochastic gradients or bounded bias for MI surrogates, step‑size schedule, stable critics). If proofs are outlines, mark the result as “Sketch” or move to supplementary.

## Suggested Edits (by subsection)
- A.3 Policy Encoding
  - Add a “Random Variables at a Glance” box: S, O_i, A_i*, A_i, Ž_i (representation). Use these across A.3–A.8.
  - Replace H(𝒁_i) with H(A_i*), and H(𝒁_i|𝒁_{−i}) with H(A_i*|A_{−i}*).

- A.4 Bounds
  - A.2 Necessity: State conditions; use Fano’s inequality to relate action misclassification to conditional entropy.
  - A.3 Achievability: Restrict to finite state/action, i.i.d. episodes, universal function classes, and infinite data; otherwise present as conjecture.

- A.5 Sample Complexity
  - Provide PAC‑style bound template: m_i = O((ComplexityTerm + log(1/δ))/ε²), and argue ComplexityTerm grows with H(A_i*|A_{−i}*) for specified classes.

- A.6 Capacity
  - Reframe “Theorem A.6 (Minimum Viable Capacity)” as “Heuristic Capacity Guideline”; add alternate proxies and note their empirical estimation.

- A.7 Redundancy
  - Switch to representation‑level redundancy or conditional MI; add caution for synchronized behaviors.

- A.8 Communication
  - Introduce M and define Δ_i formally; relate to side‑information bounds; specify message budget/cost model.

- A.9 Convergence
  - List assumptions (L‑smoothness, bounded variance, Robbins‑Monro step sizes) and cite standard convergence results for stochastic optimization; treat MI surrogates carefully.

## Optional Rewrite Snippets
- Corrected definition (A.12 replacement):
  - “Let S ~ ρ, O_i = Ω_i(S), A_i* ~ 𝒁_i(·|S), A_i ~ π_i(·|O_i). Define the policy information rate R_{π_i} := I(A_i*; A_i | S). Alternatively, define a policy fidelity F_{π_i} := E_{S,O_i}[D_KL(𝒁_i(·|S) || π_i(·|O_i))], which is not an information quantity but a useful surrogate.”
- Necessity statement (A.2):
  - “Under finite state/action spaces and a fixed ρ(S), any policy achieving ε‑suboptimality implies, for each i, either I(A_i*; A_i | S) ≥ H(A_i*|A_{−i}*) − δ(ε) or a contradiction via Fano’s inequality; δ(ε) → 0 as ε → 0.”
- Capacity guideline (A.6):
  - “We hypothesize the knee occurs when a capacity proxy (e.g., weight description length) matches H(A_i*|A_{−i}*). We estimate both sides and observe phase transitions accordingly.”

## Notation and Style Checklist
- Define S, O_i, A_i*, A_i, Ž_i once and reuse.
- Use MI/entropy only on random variables; keep bits units explicit.
- Specify ρ(S) and conditioning context for every expectation.
- Label heuristic results as “Guideline” or “Conjecture” if proofs are sketches.

## Line‑Level Notes
- A.3 definitions and MI/KL: `src/research/papers/2024-slepian-wolf-marl.tsx:3826`, `:3837–:3843`
- A.4 necessity/sufficiency: `src/research/papers/2024-slepian-wolf-marl.tsx:3863`, `:3891`
- A.5 sample complexity: `src/research/papers/2024-slepian-wolf-marl.tsx:3910–:3920`
- A.6 capacity: `src/research/papers/2024-slepian-wolf-marl.tsx:3969–:3980`
- A.7 redundancy/specialization: `src/research/papers/2024-slepian-wolf-marl.tsx:3995–:4014`
- A.8 communication threshold: `src/research/papers/2024-slepian-wolf-marl.tsx:4035–:4040`
- A.9 convergence: `src/research/papers/2024-slepian-wolf-marl.tsx:4052–:4064`
