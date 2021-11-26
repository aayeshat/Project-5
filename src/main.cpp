#include "solver.hpp"

using namespace arma;
using namespace std;

int main(int argc, char const *argv[])
{
    int M = 5;
    double h = 0.1;
    double dt = 0.1;
    int T = 100;
    double r = 2;

    Solver solver(M, h, dt, r);
    solver.solve();

    solver.A.print();
    cout << "----" << endl;
    solver.B.print();

    cx_vec u_next = spsolve(solver.A, solver.b);

    cout << u_next << endl;

    return 0;
}
