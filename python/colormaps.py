import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyarma as pa

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 16
mpl.rcParams["xtick.labelsize"] = 10
mpl.rcParams["ytick.labelsize"] = 10
mpl.rcParams["legend.fontsize"] = 12
#mpl.rcParams.update({'figure.autolayout': True})
plt.rcParams["figure.figsize"] = (6.9, 3)


h = 0.005
M = int(1.0/h + 1.0)
T = 0.002
dt = 2.5e-5
N = int(T/dt)

n_slits = "_2_slits"

U_cube_T = pa.cx_cube()
U_cube_T.load("../out/data/t_0002.bin")
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

slice = 0.8
y = np.linspace(0+h, 1-h, M-2)

#Colormap for p

fig, ax = plt.subplots(nrows = 1, ncols = 3)
im1 = ax[0].imshow(p_0, extent=[0,1,0,1])
im2 = ax[1].imshow(p_0001, extent=[0,1,0,1])
im3 = ax[2].imshow(p_0002, extent=[0,1,0,1])
ax[1].set_xlabel("$x_i$")
ax[0].set_ylabel("$y_j$")
ax[1].axes.yaxis.set_ticklabels([])
ax[2].axes.yaxis.set_ticklabels([])
#fig.subplots_adjust(right=0.85, top = 0.87, wspace = 0.3)
#cbar_ax = fig.add_axes([0.88, 0.27, 0.03, 0.45])

cbar = fig.colorbar(im1, ax = ax[0], location = 'top')
cbar2 = fig.colorbar(im2, ax = ax[1], location = 'top')
cbar3 = fig.colorbar(im3, ax = ax[2], location = 'top')
cbar.formatter.set_powerlimits((0, 0))
cbar2.formatter.set_powerlimits((0, 0))
cbar3.formatter.set_powerlimits((0, 0))
cbar.set_label('$p^n_{ij}$',size=12)
cbar2.set_label('$p^n_{ij}$',size=12)
cbar3.set_label('$p^n_{ij}$',size=12)


for fig, ax in zip(ax, ["(a) t = 0", "(b) t = 0.001 ", "(c) t = 0.002"]):
    t = add_inner_title(fig, ax, loc='upper left')
    t.patch.set_ec("none")
    t.patch.set_alpha(0.5)

plt.savefig("../out/plots/colormap_p" + n_slits + ".pdf")
plt.savefig("../out/plots/colormap_p" + n_slits + ".pgf")
plt.show()

#Colormap for Re(Uij)

fig, ax = plt.subplots(nrows = 1, ncols = 3)
im1 = ax[0].imshow(U_0_Re, extent=[0,1,0,1])
im2 = ax[1].imshow(U_0001_Re, extent=[0,1,0,1])
im3 = ax[2].imshow(U_0002_Re, extent=[0,1,0,1])
ax[1].set_xlabel("$x_i$")
ax[0].set_ylabel("$y_j$")
ax[1].axes.yaxis.set_ticklabels([])
ax[2].axes.yaxis.set_ticklabels([])
#fig.subplots_adjust(right=0.85, top = 0.87, wspace = 0.3)
#cbar_ax = fig.add_axes([0.88, 0.27, 0.03, 0.45])

cbar = fig.colorbar(im1, ax = ax[0], location = 'top')
cbar2 = fig.colorbar(im2, ax = ax[1], location = 'top')
cbar3 = fig.colorbar(im3, ax = ax[2], location = 'top')
cbar.formatter.set_powerlimits((0, 0))
cbar2.formatter.set_powerlimits((0, 0))
cbar3.formatter.set_powerlimits((0, 0))
cbar.set_label('$Re(u_{ij})$',size=12)
cbar2.set_label('$Re(u_{ij})$',size=12)
cbar3.set_label('$Re(u_{ij})$',size=12)


for fig, ax in zip(ax, ["(a) t = 0", "(b) t = 0.001 ", "(c) t = 0.002"]):
    t = add_inner_title(fig, ax, loc='upper left')
    t.patch.set_ec("none")
    t.patch.set_alpha(0.5)

plt.savefig("../out/plots/colormap_Re_u" + n_slits + ".pdf")
plt.savefig("../out/plots/colormap_Re_u" + n_slits + ".pgf")
plt.show()

#Colormap for Im(Uij)

fig, ax = plt.subplots(nrows = 1, ncols = 3)
im1 = ax[0].imshow(U_0_Im, extent=[0,1,0,1])
im2 = ax[1].imshow(U_0001_Im, extent=[0,1,0,1])
im3 = ax[2].imshow(U_0002_Im, extent=[0,1,0,1])
ax[1].set_xlabel("$x_i$")
ax[0].set_ylabel("$y_j$")
ax[1].axes.yaxis.set_ticklabels([])
ax[2].axes.yaxis.set_ticklabels([])
#fig.subplots_adjust(right=0.85, top = 0.87, wspace = 0.3)
#cbar_ax = fig.add_axes([0.88, 0.27, 0.03, 0.45])

cbar = fig.colorbar(im1, ax = ax[0], location = 'top')
cbar2 = fig.colorbar(im2, ax = ax[1], location = 'top')
cbar3 = fig.colorbar(im3, ax = ax[2], location = 'top')
cbar.formatter.set_powerlimits((0, 0))
cbar2.formatter.set_powerlimits((0, 0))
cbar3.formatter.set_powerlimits((0, 0))
cbar.set_label('$Im(u_{ij})$',size=12)
cbar2.set_label('$Im(u_{ij})$',size=12)
cbar3.set_label('$Im(u_{ij})$',size=12)


for fig, ax in zip(ax, ["(a) t = 0", "(b) t = 0.001 ", "(c) t = 0.002"]):
    t = add_inner_title(fig, ax, loc='upper left')
    t.patch.set_ec("none")
    t.patch.set_alpha(0.5)

plt.savefig("../out/plots/colormap_Im_u" + n_slits + ".pdf")
plt.savefig("../out/plots/colormap_Im_u" + n_slits + ".pgf")
plt.show()


# plt.figure()
# plt.imshow(p_0)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.colorbar()
# plt.show()
# # plt.savefig("../out/plots/colormap_p_t0" + n_slits + ".pdf")
# #
# plt.figure()
# plt.imshow(p_0001)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.colorbar()
# plt.show()
# # plt.savefig("../out/plots/colormap_p_t0001" + n_slits + ".pdf")
# #
# plt.figure()
# plt.imshow(p_0002)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.colorbar()
# plt.show()
# plt.savefig("../out/plots/colormap_p_t0002" + n_slits + ".pdf")

# plt.figure()
# plt.imshow(U_0_Re)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("../out/plots/colormap_U_t0_Re" + n_slits + ".pdf")
#
# plt.figure()
# plt.imshow(U_0001_Re)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("../out/plots/colormap_U_t0001_Re" + n_slits + ".pdf")
#
# plt.figure()
# plt.imshow(U_0002_Re)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("../out/plots/colormap_U_t0002_Re" + n_slits + ".pdf")
#
# plt.figure()
# plt.imshow(U_0_Im)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("../out/plots/colormap_U_t0_Im" + n_slits + ".pdf")
#
# plt.figure()
# plt.imshow(U_0001_Im)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("../out/plots/colormap_U_t0001_Im" + n_slits + ".pdf")
#
# plt.figure()
# plt.imshow(U_0002_Im)
# #plt.title("Colormap ")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("../out/plots/colormap_U_t0002_Im" + n_slits + ".pdf")
