import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("dispersion.txt", skiprows=1).T


# There is NxN pints in the data
N = int(np.sqrt(data.shape[1]))
data = data.reshape((data.shape[0], N, N))

kx = data[0]
ky = data[1]
energy = data[2]

fig, ax = plt.subplots(figsize=(6, 5))


ax.imshow(
    energy,
    cmap="twilight_shifted_r",
    origin="lower",
    extent=[np.amin(kx), np.amax(kx), np.amin(ky), np.amax(ky)],
)

ax.set_aspect("equal")


ax.set_xlabel(R"$k_x$ ($\mathrm{\AA^{-1}}$)", fontsize=25)
ax.set_ylabel(R"$k_y$ ($\mathrm{\AA^{-1}}$)", fontsize=25)

ax.set_xticks([])
ax.set_yticks([])

plt.savefig("imshow-1.png", dpi=300, bbox_inches="tight")
plt.close()
