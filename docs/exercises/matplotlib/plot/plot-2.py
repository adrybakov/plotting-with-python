import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("plot-123.txt", skiprows=1)

Bx = data[:, 4]

mx = data[:, 1]
my = data[:, 2]
mz = data[:, 3]

fig, ax = plt.subplots()

ax.plot(Bx, mx, lw=1, color="tab:red", label="$m_x$")
ax.plot(Bx, my, lw=1, color="tab:green", label="$m_y$")
ax.plot(Bx, mz, lw=1, color="tab:blue", label="$m_z$")

ax.legend(loc="lower right", frameon=False, fontsize=20)

ax.set_xlabel("$B_x$ (T)", fontsize=15)
ax.set_ylabel("Unitless magnetization", fontsize=15)

plt.savefig("plot-2.png", dpi=300, bbox_inches="tight")
plt.close()
