import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("dispersion.txt", skiprows=1).T


# There is NxN pints in the data

kx = data[0]
ky = data[1]
energy = data[2]


limit = 0.2
# Filter an array
energy = energy[kx > -limit]
ky = ky[kx > -limit]
kx = kx[kx > -limit]

energy = energy[kx < limit]
ky = ky[kx < limit]
kx = kx[kx < limit]

energy = energy[ky > -limit]
kx = kx[ky > -limit]
ky = ky[ky > -limit]

energy = energy[ky < limit]
kx = kx[ky < limit]
ky = ky[ky < limit]

fig, ax = plt.subplots(figsize=(6, 5))


ax.scatter(kx, ky, c=energy, cmap="twilight_shifted_r", s=4)

ax.set_aspect("equal")


ax.set_xlabel(R"$k_x$ ($\mathrm{\AA^{-1}}$)", fontsize=25)
ax.set_ylabel(R"$k_y$ ($\mathrm{\AA^{-1}}$)", fontsize=25)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlim(kx.min(), kx.max())
ax.set_ylim(ky.min(), ky.max())

plt.savefig("scatter-2.png", dpi=300, bbox_inches="tight")
plt.close()
