#include "solver.hpp"

Solver::Solver(int M_in, double h_in, int dt_in, double r_in)
{
    M = M_in;
    h = h_in;
    dt = dt_in;
    r = r_in;

    build_vectors();
    build_matrixs();

    U = cx_mat(M - 2, M - 2, fill::randu);
}

void Solver::build_vectors()
{
    a = cx_vec((M - 2) * (M - 2));
    b = cx_vec((M - 2) * (M - 2));

    cx_mat V = cx_mat((M - 2), (M - 2), fill::ones);
    cx_vec v = V.as_col();
    complex<double> i(0.0, 1.0);

    for (int k = 0; k < pow(M - 2, 2); k++)
    {
        a(k) = 1 + 4 * r + i * dt / 2.0 * v(k);
        b(k) = 1 - 4 * r - i * dt / 2.0 * v(k);
    }
}

void Solver::build_matrixs()
{
    A = sp_cx_mat((M - 2) * (M - 2), (M - 2) * (M - 2));
    B = cx_mat((M - 2) * (M - 2), (M - 2) * (M - 2), fill::zeros);

    for (int i = 0; i < (M - 2) * (M - 2); i++)
    {
        A(i, i) = a(i);
        B(i, i) = b(i);
    }
    for (int i = 0; i < (M - 2) * (M - 2) - (M - 2); i++)
    {
        A(i, i + (M - 2)) = -r;
        A(i + (M - 2), i) = -r;
        B(i, i + (M - 2)) = r;
        B(i + (M - 2), i) = r;
    }
    for (int i = 0; i < (M - 2) * (M - 2) - 1; i++)
    {
        A(i, i + 1) = -r;
        A(i + 1, i) = -r;
        B(i, i + 1) = r;
        B(i + 1, i) = r;
        for (int j = 1; j < (M - 2) * (M - 2) - 1; j++)
        {
            if (i == j * (M - 2) - 1)
            {
                A(i, i + 1) = 0;
                A(i + 1, i) = 0;
                B(i, i + 1) = 0;
                B(i + 1, i) = 0;
            }
        }
    }
}

void Solver::solve()
{
    cx_vec u = U.as_col();
    cx_vec b = cx_vec(u.size());

    for (int k = 0; k < u.size(); k++)
    {
        cx_double B_tot = 0;
        for (int s = 0; s < u.size(); s++)
        {
            B_tot += B.col(k)(s);
        }
        b(k) = B_tot * u(k);
    }
}