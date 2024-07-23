import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("dispersion.txt", skiprows=1).T


# There is NxN pints in the data

kx = data[0]
ky = data[1]
energy = data[2]


fig, ax = plt.subplots(figsize=(6, 5))


ax.scatter(kx, ky, c=energy, cmap="twilight_shifted_r", s=0.5)

ax.set_aspect("equal")


ax.set_xlabel(R"$k_x$ ($\mathrm{\AA^{-1}}$)", fontsize=25)
ax.set_ylabel(R"$k_y$ ($\mathrm{\AA^{-1}}$)", fontsize=25)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlim(kx.min(), kx.max())
ax.set_ylim(ky.min(), ky.max())

plt.savefig("scatter-1.png", dpi=300, bbox_inches="tight")
plt.close()
