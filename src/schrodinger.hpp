#ifndef SCHRODINGER_HPP
#define SCHRODINGER_HPP

#include <string>
#include <armadillo>
#include <iostream>
#include <iomanip>
#include <complex>

using namespace arma;
using namespace std;

class Schrodinger
{
public:
  int M;
  double h;
  double dt;
  int length;

  cx_vec a;
  cx_vec b;

  sp_cx_mat A;
  sp_cx_mat B;

  Schrodinger(int M_, double h_, double dt_);

  int get_k(int i, int j);

  void init(cx_double r, double v0, int n_slits, double slit_height, double slit_separation, double wall_thickness, double wall_x_pos);

  mat potential(double v0, int n_slits, double slit_height, double slit_separation, double wall_thickness, double wall_x_pos);

  void vector(mat V, cx_double r);

  void matrix(cx_double r);

  cx_vec u_mat_to_vec(const cx_mat &u) const
  {
    cx_vec u_vec((M - 2) * (M - 2), fill::zeros);
    int col_len = M - 2;
    for (int i = 0; i < M - 2; ++i)
    {
      u_vec.subvec(col_len * i, col_len * (i + 1) - 1) = u.col(i);
    }
    return u_vec;
  }

  cx_vec initialize_internal_state(double x_c, double y_c, double sigma_x, double sigma_y, double p_x, double p_y);

  cx_cube simulate(cx_vec u, int N);
};

#endif
