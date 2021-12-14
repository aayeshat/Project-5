#include "schrodinger.hpp"

using namespace arma;
using namespace std;

int main(int argc, char const *argv[])
{

    double h = 0.005; // Step-size
    int M = 1.0 / h + 1.0;
    double T = 0.008;   // Total time
    double dt = 2.5e-5; // Time steps
    double N = T / dt;  // Number of time steps

    int n_slits = 2; // Number of slits; there can be 0 - 3 slits

    double wall_thickness = 0.02;
    double wall_x_pos = 0.5;
    double slit_size = 0.05;
    double slit_separation = 0.05;

    double v0 = 1e10;
    cx_double r = cx_double(0.0, dt / (2 * h * h)); // idt/d^2h in Crank-Nicolson scheme

    //Arguments for wavepacket
    double x_c = 0.25;
    double y_c = 0.5;
    double sigma_x = 0.05;
    double sigma_y = 0.1;
    double p_x = 200;
    double p_y = 0;

    Schrodinger schrodinger(M, h, dt);
    schrodinger.init(r, v0, n_slits, slit_size, slit_separation, wall_thickness, wall_x_pos);
    cx_vec u = schrodinger.initialize_internal_state(x_c, y_c, sigma_x, sigma_y, p_x, p_y);

    cx_cube u_cube = schrodinger.crank_nicolson(u, N);

    // "0" or "1e10"
    string v0_string = "1e10";

    //u_cube.save("../out/data/data_slits_" + to_string(n_slits) + "_v0_" + v0_string + ".bin");
    //u_cube.save("../out/data/data_slits_" + to_string(n_slits) + ".bin");

    return 0;
}
