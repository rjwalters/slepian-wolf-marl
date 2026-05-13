"""fig2_policy_encoder_pipeline.py

Block diagram: random-variable flow through the multi-agent system.
Highlights that the environment is an evaluator, not a Shannon decoder.
"""

import sys
sys.path.insert(0, "/Users/rwalters/GitHub/sphere/docs/templates")

from patent_figures import PatentFigure

fig = PatentFigure(
    "Policies as distributed encoders of the latent optimal action distribution",
    width=11, height=6.5, palette="color",
)

# State / nature
state = fig.block(6, 42, 14, 16,
                  "Nature\n" r"$S \sim \rho$",
                  fill="neutral")

# Observation functions (split into per-agent slices)
obs1 = fig.block(28, 62, 14, 10,
                 r"$\Omega_1$" "\n" r"$O_1 = \Omega_1(S)$",
                 fill="signal")
obs2 = fig.block(28, 42, 14, 10,
                 r"$\Omega_2$" "\n" r"$O_2 = \Omega_2(S)$",
                 fill="signal")
obs3 = fig.block(28, 22, 14, 10,
                 r"$\Omega_N$" "\n" r"$O_N = \Omega_N(S)$",
                 fill="signal")
fig.text(35, 36, r"$\vdots$", fontsize=14)

# Policies / encoders
pol1 = fig.block(50, 62, 16, 10,
                 r"Encoder $\pi_1$" "\n" r"$A_1 \sim \pi_1(\cdot|O_1)$",
                 fill="digital")
pol2 = fig.block(50, 42, 16, 10,
                 r"Encoder $\pi_2$" "\n" r"$A_2 \sim \pi_2(\cdot|O_2)$",
                 fill="digital")
pol3 = fig.block(50, 22, 16, 10,
                 r"Encoder $\pi_N$" "\n" r"$A_N \sim \pi_N(\cdot|O_N)$",
                 fill="digital")
fig.text(58, 36, r"$\vdots$", fontsize=14)

# Environment as evaluator
env = fig.block(74, 36, 18, 22,
                "Environment\n(evaluator)\n" r"$R = R(S, A)$",
                fill="alert")

# Latent optimal distribution (off to the side, dashed connection)
opt = fig.block(50, 4, 16, 10,
                "Latent optimal\n" r"$A^* \sim \mathcal{Z}(\cdot|S)$",
                fill="control")

# Arrows: nature -> observation functions
fig.arrow(state, obs1, style="data")
fig.arrow(state, obs2, style="data")
fig.arrow(state, obs3, style="data")

# Observation -> policy
fig.arrow(obs1, pol1, style="data")
fig.arrow(obs2, pol2, style="data")
fig.arrow(obs3, pol3, style="data")

# Policy -> environment (joint action)
fig.arrow(pol1, env, style="data")
fig.arrow(pol2, env, style="data")
fig.arrow(pol3, env, style="data")

# Environment -> learning signal (routed around / below to policies)
# Use route_right_down_left for each: feedback path
fig.route_right_down_left(env, pol1, style="cal", x_offset=4)
fig.route_right_down_left(env, pol2, style="cal", x_offset=4)
fig.route_right_down_left(env, pol3, style="cal", x_offset=4)

# Label one of the feedback arrows
fig.text(96, 36, "reward /\ngradient", fontsize=7, color="#C62828")

# State -> latent optimal (reference, dashed via "clock" style)
fig.arrow(state, opt, style="clock")

# Annotation: encoders share no information at inference (lower than title)
fig.text(58, 73,
         "Encoders share no information at inference",
         fontsize=8, color="#1565C0")

# Annotation: environment is evaluator
fig.text(83, 64,
         "Environment evaluates joint $A$;\n"
         "not a Shannon decoder.",
         fontsize=7.5, color="#C62828", ha="center")

# Annotation: latent optimal is a reference
fig.text(58, 1,
         r"$\mathcal{Z}$ is a conceptual reference (centralized teacher);"
         "\nused only for entropy estimation, not at runtime.",
         fontsize=7.5, color="#7B1FA2", ha="center")

fig.save("fig2_policy_encoder_pipeline.pdf")
fig.save("fig2_policy_encoder_pipeline.png")
print("Saved fig2_policy_encoder_pipeline.{pdf,png}")
