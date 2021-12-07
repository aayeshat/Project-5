#include "schrodinger.hpp"

using namespace arma;
using namespace std;

int main(int argc, char const *argv[])
{

    double h = 0.005; // step size in x|y direction
    int M = 1.0 / h + 1.0;
    double T = 0.008; // total time
    double dt = 2.5e-5;
    double N = T / dt; // number of time steps

    int n_slits = 2; // slits 0, 1, 2 or 3

    double wall_thickness = 0.02;
    double wall_x_pos = 0.5;
    double slit_size = 0.05;       // slit aperture (opening in the y-direction)
    double slit_separation = 0.05; // length of the wall piece separating the slits

    double v0 = 1;
    cx_double r = cx_double(0.0, dt / (2 * h * h)); // constant

    double x_c = 0.25;
    double y_c = 0.5;
    double sigma_x = 0.05;
    double sigma_y = 0.2;
    double p_x = 200;
    double p_y = 0;

    Schrodinger schrodinger(M, h, dt);
    schrodinger.init(r, v0, n_slits, slit_size, slit_separation, wall_thickness, wall_x_pos);
    cx_vec u = schrodinger.initialize_internal_state(x_c, y_c, sigma_x, sigma_y, p_x, p_y);

    cx_cube u_cube = schrodinger.simulate(u, N);
    u_cube.save("../out/data.txt");
    return 0;
}
