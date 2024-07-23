import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("plot-123.txt", skiprows=1)

E_total = data[:, 7]

Bx = data[:, 4]

fig, ax = plt.subplots()

ax.plot(Bx, E_total, lw=1, color="black")

ax.set_xlabel("$B_x$ (T)", fontsize=15)
ax.set_ylabel(R"$E_{total}$ (J)", fontsize=15)

plt.savefig("plot-1.png", dpi=300, bbox_inches="tight")
plt.close()
