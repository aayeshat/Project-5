import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyarma as pa

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 14
mpl.rcParams["xtick.labelsize"] = 14
mpl.rcParams["ytick.labelsize"] = 14
mpl.rcParams["legend.fontsize"] = 14
mpl.rcParams.update({'figure.autolayout': True})
plt.rcParams["figure.figsize"] = (5, 4)

# 1 or 2
n_slits = 2

U_cube_0_arma = pa.cx_cube()
U_cube_0_arma.load("../out/data/data_slits_" + str(n_slits) + "_v0_0.bin")
U_cube_0 = np.transpose(U_cube_0_arma)

U_cube_10_arma = pa.cx_cube()
U_cube_10_arma.load("../out/data/data_slits_" + str(n_slits) + "_v0_1e10.bin")
U_cube_10 = np.transpose(U_cube_10_arma)

h = 0.005
M = int(1.0/h + 1.0)
T = 0.008
dt = 2.5e-5
N = int(T/dt)
t = np.linspace(0, T, N)
p_0_array = np.zeros(N)
p_10_array = np.zeros(N)

for n in range(N):
    p_0 = 0.0
    p_10 = 0.0
    for i in range(M-2):
        for j in range(M-2):
            p_0 += np.real(np.conj(U_cube_0[i, j, n])*U_cube_0[i, j, n])
            p_10 += np.real(np.conj(U_cube_10[i, j, n])*U_cube_10[i, j, n])
    p_0_array[n] = p_0
    p_10_array[n] = p_10

plt.plot(t, abs(1 - p_0_array), ".", label = "v0 = 0")
plt.plot(t, abs(1 - p_10_array), ".", label = "v0 = 1e10")

#plt.title("Deviation probability function of time")
plt.xlabel("Time")
plt.ylabel("|1 - $\sum_{i, j}\ p_{ij}$|")
plt.yscale("log")

plt.legend()
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plots/prob_deviation_nslit" + str(n_slits) + ".pdf")
plt.savefig("../out/plots/prob_deviation_nslit" + str(n_slits) + ".pgf")
plt.show()
