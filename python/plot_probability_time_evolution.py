import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyarma as pa

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 16
mpl.rcParams["xtick.labelsize"] = 14
mpl.rcParams["ytick.labelsize"] = 14
mpl.rcParams["legend.fontsize"] = 12
mpl.rcParams.update({'figure.autolayout': True})

h = 0.005
M = int(1.0/h + 1.0)
T = 0.002
dt = 2.5e-5
N = int(T/dt)

n_slits = "_3_slits"

U_cube_T = pa.cx_cube()
U_cube_T.load("../out/data/data_slits_3.bin")
#U_cube_T.load("../out/data/data_slits_1.bin")
#U_cube_T.load("../out/data/T_0002.bin")
U_cube = np.transpose(U_cube_T)

U_0_Re = np.zeros((M-2, M-2))
U_0001_Re = np.zeros((M-2, M-2))
U_0002_Re = np.zeros((M-2, M-2))

U_0_Im = np.zeros((M-2, M-2))
U_0001_Im = np.zeros((M-2, M-2))
U_0002_Im = np.zeros((M-2, M-2))

p_0 = np.zeros((M-2, M-2))
p_0001 = np.zeros((M-2, M-2))
p_0002 = np.zeros((M-2, M-2))

for i in range(M-2):
    for j in range(M-2):
        U_0_Re[i, j] = U_cube[i, j, 0].real
        U_0001_Re[i, j] = U_cube[i, j, int(N/2)].real
        U_0002_Re[i, j] = U_cube[i, j, N-1].real

        U_0_Im[i, j] = U_cube[i, j, 0].imag
        U_0001_Im[i, j] = U_cube[i, j, int(N/2)].imag
        U_0002_Im[i, j] = U_cube[i, j, N-1].imag

        p_0[i, j] = (np.conj(U_cube[i, j, 0]) * U_cube[i, j, 0]).real
        p_0001[i, j] = (np.conj(U_cube[i, j, int(N/2)]) * U_cube[i, j, int(N/2)]).real
        p_0002[i, j] = (np.conj(U_cube[i, j, N-1]) * U_cube[i, j, N-1]).real


slice = 0.8
y = np.linspace(0+h, 1-h, M-2)

# Time evolution

plt.figure()
plt.plot(y, p_0002[:,int(slice*(M-2))]/(sum(p_0002[:,int(slice*(M-2))])))
plt.xlabel("$y$")
plt.ylabel("$p(y | x = 0.8; t = 0.002)$")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.savefig("../out/plots/time_evolution_p" + n_slits + ".pdf")
plt.savefig("../out/plots/time_evolution_p" + n_slits + ".pgf")
plt.show()
