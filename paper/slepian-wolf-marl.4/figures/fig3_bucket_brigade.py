"""fig3_bucket_brigade.py

Bucket Brigade environment topology: 10 houses arranged in a ring,
4 agents at indicative positions, with one observation window highlighted.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyArrowPatch

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
})

K = 10                # houses
N = 4                 # agents
R_house = 4.0         # ring radius
house_size = 0.55     # house square half-width
agent_radius = 0.35
obs_radius_houses = 2  # window radius (each side)

# Indicative state: a couple of houses on fire
fire_idx = {2, 6}
ruined_idx = {7}
agent_positions = [0, 3, 5, 8]  # house indices each agent occupies

fig, ax = plt.subplots(figsize=(5.0, 5.0))
ax.set_xlim(-R_house - 1.5, R_house + 1.5)
ax.set_ylim(-R_house - 1.5, R_house + 1.5)
ax.set_aspect("equal")
ax.axis("off")

# Compute house centers
angles = np.linspace(np.pi / 2, np.pi / 2 - 2 * np.pi, K, endpoint=False)
house_centers = np.array([(R_house * np.cos(a), R_house * np.sin(a)) for a in angles])

# Highlight one agent's observation window (agent 0 at house 0, radius 2)
agent_focus = 0
home = agent_positions[agent_focus]
window = {(home + d) % K for d in range(-obs_radius_houses, obs_radius_houses + 1)}

# Draw window as faint sector behind houses
for idx in window:
    a = angles[idx]
    a_deg = np.degrees(a)
    wedge = Wedge((0, 0), R_house + 0.9, a_deg - 360 / K / 2, a_deg + 360 / K / 2,
                  width=1.8, facecolor="#FFF3E0", edgecolor="none", alpha=0.7, zorder=0)
    ax.add_patch(wedge)

# Draw houses
for idx, (x, y) in enumerate(house_centers):
    if idx in ruined_idx:
        face = "#9E9E9E"
        edge = "#424242"
        label = "X"
    elif idx in fire_idx:
        face = "#FFCDD2"
        edge = "#C62828"
        label = ""
    else:
        face = "#E8F5E9"
        edge = "#1B5E20"
        label = ""
    # House body (square)
    sq = plt.Rectangle((x - house_size, y - house_size),
                       2 * house_size, 2 * house_size,
                       facecolor=face, edgecolor=edge, linewidth=1.2, zorder=2)
    ax.add_patch(sq)
    # Roof (triangle)
    triangle = plt.Polygon([(x - house_size, y + house_size),
                            (x + house_size, y + house_size),
                            (x, y + house_size + 0.45)],
                           facecolor=face, edgecolor=edge, linewidth=1.2, zorder=2)
    ax.add_patch(triangle)
    # Fire glyph
    if idx in fire_idx:
        ax.text(x, y, "♦", fontsize=10, color="#B71C1C",
                ha="center", va="center", zorder=3)
    if idx in ruined_idx:
        ax.text(x, y, label, fontsize=10, color="#FFFFFF", weight="bold",
                ha="center", va="center", zorder=3)
    # House index
    ax.text(x, y - house_size - 0.5, str(idx), fontsize=7, color="#555",
            ha="center", va="top")

# Draw agents (small filled circles offset toward center)
for k, idx in enumerate(agent_positions):
    a = angles[idx]
    ax_pos = (R_house - 1.2) * np.cos(a)
    ay_pos = (R_house - 1.2) * np.sin(a)
    color = "#1565C0" if k == agent_focus else "#37474F"
    ax.add_patch(Circle((ax_pos, ay_pos), agent_radius, facecolor=color,
                        edgecolor="black", linewidth=0.7, zorder=4))
    ax.text(ax_pos, ay_pos, str(k + 1), fontsize=7, color="white",
            ha="center", va="center", zorder=5, weight="bold")

# Indicate fire-spread between adjacent burning houses
for fi in fire_idx:
    for nbr in [(fi - 1) % K, (fi + 1) % K]:
        if nbr in (fire_idx | ruined_idx):
            continue
        x0, y0 = house_centers[fi]
        x1, y1 = house_centers[nbr]
        # arrow slightly outside the ring
        arr = FancyArrowPatch((x0, y0), (x1, y1),
                              arrowstyle="->", mutation_scale=8,
                              color="#FF6F00", linewidth=1.0,
                              connectionstyle="arc3,rad=0.25", zorder=1, alpha=0.6)
        ax.add_patch(arr)

# Legend
legend_items = [
    plt.Rectangle((0, 0), 1, 1, facecolor="#E8F5E9", edgecolor="#1B5E20"),
    plt.Rectangle((0, 0), 1, 1, facecolor="#FFCDD2", edgecolor="#C62828"),
    plt.Rectangle((0, 0), 1, 1, facecolor="#9E9E9E", edgecolor="#424242"),
    plt.Rectangle((0, 0), 1, 1, facecolor="#FFF3E0", edgecolor="#FB8C00"),
    plt.Line2D([0], [0], marker="o", color="w",
               markerfacecolor="#1565C0", markersize=8),
]
ax.legend(legend_items,
          ["Safe house", "Burning", "Ruined", "Agent 1 obs window (r=2)", "Agent"],
          loc="upper left", bbox_to_anchor=(-0.05, -0.02), ncol=3,
          fontsize=7, frameon=False, columnspacing=0.6, handlelength=1.5)

ax.set_title(r"Bucket Brigade: $K{=}10$ houses, $N{=}4$ agents, ring topology"
             "\nAction set: {work_here, work_left, work_right, rest}",
             fontsize=9, pad=6)

fig.savefig("fig3_bucket_brigade.pdf")
fig.savefig("fig3_bucket_brigade.png")
print("Saved fig3_bucket_brigade.{pdf,png}")
