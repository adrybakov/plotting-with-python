import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("plot-123.txt", skiprows=1)

Bx = data[:, 4]

Energies = data[:, 7:]

fig, ax = plt.subplots()

Energy_names = ["E_total", "E_Zeeman", "E_exch", "E_anis", "E_demag"]

for i in range(5):

    ax.plot(Bx, Energies[:, i], lw=1, label=Energy_names[i])

ax.legend()

ax.set_xlabel("$B_x$ (T)", fontsize=15)
ax.set_ylabel("Energy (J)", fontsize=15)

plt.savefig("plot-3.png", dpi=300, bbox_inches="tight")
plt.close()
