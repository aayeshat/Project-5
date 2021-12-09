#include "schrodinger.hpp"

using namespace arma;
using namespace std;

int main(int argc, char const *argv[])
{

    double h = 0.005; // step-size in x-y (a random guess not sure exact value)
    int M = 1.0 / h + 1.0;
    double T = 0.008;   // Total-time (overall T)
    double dt = 2.5e-5; //small time-steps
    double N = T / dt;  // No. of time steps totaltime/small time-step

    int n_slits = 2; // number of slits can be either 0(i think no slit), 1, 2(two slits separated by some length)

    double wall_thickness = 0.02;
    double wall_x_pos = 0.5;
    double slit_size = 0.05;       // size slit opening(length)
    double slit_separation = 0.05; // distance between slits or length separating slits

    double v0 = 1e10;
    cx_double r = cx_double(0.0, dt / (2 * h * h)); // a constt

    double x_c = 0.25;
    double y_c = 0.5;
    double sigma_x = 0.05;
    double sigma_y = 0.1;
    double p_x = 200;
    double p_y = 0;

    Schrodinger schrodinger(M, h, dt);
    schrodinger.init(r, v0, n_slits, slit_size, slit_separation, wall_thickness, wall_x_pos);
    cx_vec u = schrodinger.initialize_internal_state(x_c, y_c, sigma_x, sigma_y, p_x, p_y);

    cx_cube u_cube = schrodinger.simulate(u, N); // actually "stimulate" here is "CrankNicolson" did not used name

    //u_cube.save("../out/data_slits_" + to_string(n_slits) + "_v" + to_string((int)v0) + ".bin"); // save file
    u_cube.save("../out/T_0002.bin"); // save file

    return 0;
}
