import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyarma as pa

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 16
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12
mpl.rcParams["legend.fontsize"] = 12
mpl.rcParams.update({'figure.autolayout': True})
#plt.rcParams["figure.figsize"] = (7, 4)
plt.rcParams["figure.figsize"] = (4, 6)

def add_inner_title(ax, title, loc, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke
    prop = dict(path_effects=[withStroke(foreground='w', linewidth=3)],
                size=plt.rcParams['legend.fontsize'])
    at = AnchoredText(title, loc=loc, prop=prop,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)
    ax.add_artist(at)
    return at


h = 0.005
M = int(1.0/h + 1.0)
T = 0.002
dt = 2.5e-5
N = int(T/dt)
slice = 0.8
y = np.linspace(0+h, 1-h, M-2)

U_cube1 = pa.cx_cube()
U_cube2 = pa.cx_cube()
U_cube3 = pa.cx_cube()

U_cube1.load("../out/data/data_slits_1_v0_1e10.bin")
U_cube2.load("../out/data/T_0002.bin")
U_cube3.load("../out/data/data_slits_3.bin")

U_cube_1 = np.transpose(U_cube1)
U_cube_2 = np.transpose(U_cube2)
U_cube_3 = np.transpose(U_cube3)

p1 = np.zeros((M-2, M-2))
p2 = np.zeros((M-2, M-2))
p3 = np.zeros((M-2, M-2))

for i in range(M-2):
    for j in range(M-2):
        p1[i, j] = (np.conj(U_cube_1[i, j, N-1]) * U_cube_1[i, j, N-1]).real
        p2[i, j] = (np.conj(U_cube_2[i, j, N-1]) * U_cube_2[i, j, N-1]).real
        p3[i, j] = (np.conj(U_cube_3[i, j, N-1]) * U_cube_3[i, j, N-1]).real


fig, ax = plt.subplots(nrows = 3, ncols = 1)
fig1 = ax[0].plot(y, p1[:,int(slice*(M-2))]/(sum(p1[:,int(slice*(M-2))])))
fig2 = ax[1].plot(y, p2[:,int(slice*(M-2))]/(sum(p2[:,int(slice*(M-2))])))
fig3 = ax[2].plot(y, p3[:,int(slice*(M-2))]/(sum(p3[:,int(slice*(M-2))])))

test_prob = np.trapz(abs(p1[:,int(slice*(M-2))]/(sum(p1[:,int(slice*(M-2))]))))
print(1-test_prob)
test2 = np.trapz(abs(p2[:,int(slice*(M-2))]/(sum(p2[:,int(slice*(M-2))]))))
print(1-test2)
test3 = np.trapz(abs(p3[:,int(slice*(M-2))]/(sum(p3[:,int(slice*(M-2))]))))
print(1-test3)

# for axs in ax.flat:
#     axs.set(xlabel="$y$", ylabel="$p(y | x = 0.8; t = 0.002)$")

ax[1].set_ylabel("$p(y | x = 0.8; t = 0.002)$")
ax[2].set_xlabel("$y$")

# Hide x labels and tick labels for top plots and y ticks for right plots.
for axs in ax.flat:
    axs.label_outer()

for fig, ax in zip(ax, ["(a)", "(b)", "(c)"]):
    t = add_inner_title(fig, ax, loc='upper left')
    t.patch.set_ec("none")
    t.patch.set_alpha(0.5)


# plt.savefig("../out/plots/probability3.pgf")
# plt.show()
