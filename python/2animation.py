import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyarma as pa
import matplotlib.animation as animation

h = 0.005
M = int(1.0/h + 1.0);
T = 0.008
dt = 2.5e-5
N = int(T/dt)

plt.rcParams.update({'figure.max_open_warning': 0})

U_cube_T = pa.cx_cube()
#U_cube_T.load("../out/data/T_0002.bin")
#U_cube_T.load("../out/data/data_slits_2_v0_1e10.bin")
U_cube_T.load("../out/data/data_slits_2_v0_0.bin")
#U_cube_T.load("../out/data/data_slits_0_v0_1e10.bin")
U_cube = np.transpose(U_cube_T)

x_points = np.arange(0, 1+h, h);
y_points = np.arange(0, 1+h, h);
x, y = np.meshgrid(x_points, y_points, sparse = True)

t_points = np.arange(0, 1+dt, dt)

p_data_list = []
for n in range(N):
    p_data = np.real(np.conj(U_cube[:, :, n])*U_cube[:, :, n])
    p_data_list.append(p_data)


fontsize = 14
t_min = t_points[0]
x_min, x_max = x_points[0], x_points[-1]
y_min, y_max = y_points[0], y_points[-1]

# Create figure
fig = plt.figure()
ax = plt.gca()

# Create a colour scale normalization according to the max z value in the first frame
norm = matplotlib.cm.colors.Normalize(vmin=0.0, vmax=np.max(p_data_list[0]))

# Plot the first frame
img = ax.imshow(p_data_list[0], extent=[x_min,x_max,y_min,y_max], cmap=plt.get_cmap("viridis"), norm=norm)

# Axis labels
plt.xlabel("x", fontsize=fontsize)
plt.ylabel("y", fontsize=fontsize)
plt.xticks(fontsize=fontsize)
plt.yticks(fontsize=fontsize)

# Add a colourbar
cbar = fig.colorbar(img, ax=ax)
cbar.set_label("p(x, y, t)", fontsize=fontsize)
cbar.ax.tick_params(labelsize=fontsize)

# Add a text element showing the time
time_txt = plt.text(0.95, 0.95, "t = {:.3e}".format(t_min), color="white",
horizontalalignment="right", verticalalignment="top", fontsize=fontsize)

# Function that takes care of updating the z data and other things for each frame
def animation(i):
    # Normalize the colour scale to the current frame?
    norm = matplotlib.cm.colors.Normalize(vmin=0.0, vmax=np.max(p_data_list[i]))
    img.set_norm(norm)

    # Update z data
    img.set_data(p_data_list[i])

    # Update the time label
    current_time = t_min + i * dt
    time_txt.set_text("t = {:.3e}".format(current_time))

    return img

    # Use matplotlib.animation.FuncAnimation to put it all together
anim = FuncAnimation(fig, animation, interval=1, frames=np.arange(0, len(p_data_list), 2), repeat=False, blit=0)

n_slits = 2
v0 = 0

anim.save('../out/plots/animation_slit' + str(n_slits) + '_v0_' + str(v0) + '.gif', writer="imagemagick", bitrate=-1, fps=30)

    # Run the animation!
plt.show()
