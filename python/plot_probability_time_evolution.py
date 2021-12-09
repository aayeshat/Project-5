import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyarma as pa

h = 0.005
M = int(1.0/h + 1.0)
T = 0.002
dt = 2.5e-5
N = int(T/dt)

U_cube_T = pa.cx_cube()
U_cube_T.load("../out/T_0002.bin")
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

        p_0[i, j] = (np.conj(U_cube[i, j, 0])*U_cube[i, j, 0]).real
        p_0001[i, j] = (np.conj(U_cube[i, j, int(N/2)])*U_cube[i, j, int(N/2)]).real
        p_0002[i, j] = (np.conj(U_cube[i, j, N-1])*U_cube[i, j, N-1]).real


fig = plt.figure(figsize = (8,6))

p = [p_0, p_0001, p_0002]
p_title = ["$p_0$", "$p_{0001}$", "$p_{0002}$"]

U_Re = [U_0_Re, U_0001_Re, U_0002_Re]
U_Re_title = ["Re($U_0$)", "Re($U_{0001}$)", "Re($U_{0002}$)"]

U_Im = [U_0_Im, U_0001_Im, U_0002_Im]
U_Im_title = ["Im($U_0$)", "Im($U_{0001}$)", "Im($U_{0002}$)"]

slice = 0.8
x = np.linspace(0+h, 1-h, M-2)
#print(len(p_0002[int(x*(M-2)), :]))

plt.imshow(p_0)
plt.show()
plt.imshow(p_0001)
plt.show()
plt.imshow(p_0002)
plt.show()
plt.imshow(U_0002_Im)
plt.show()
plt.imshow(U_0002_Re)
plt.show()

plt.plot(x, p_0[:,int(slice*(M-2))], label = "t = 0.0")
plt.plot(x, p_0001[:,int(slice*(M-2))], label = "t = 0.001")
plt.plot(x, p_0002[:,int(slice*(M-2))], label = "t = 0.002")
plt.legend()
plt.show()
# #plt.savefig("../out/plot_probability_time_evolution.pdf")


plt.plot(x, U_0_Im[:,int(slice*(M-2))], label = "t = 0.0")
plt.plot(x, U_0001_Im[:,int(slice*(M-2))], label = "t = 0.001")
plt.plot(x, U_0002_Im[int(slice*(M-2)), :], label = "t = 0.002")
plt.show()

plt.plot(x, U_0_Re[:,int(slice*(M-2))], label = "t = 0.0")
plt.plot(x, U_0001_Re[:,int(slice*(M-2))], label = "t = 0.001")
plt.plot(x, U_0002_Re[:,int(slice*(M-2))], label = "t = 0.002")
plt.show()
