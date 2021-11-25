#ifndef SOLVER_HPP
#define SOLVER_HPP

#include <string>
#include <armadillo>
#include <iostream>
#include <iomanip>
#include <complex>

using namespace arma;
using namespace std;

class Solver
{
  //private:

public:
  int M;
  double r;
  double h;
  double dt;

  cx_mat U;
  cx_vec a;
  cx_vec b;

  sp_cx_mat A;
  cx_mat B;

  Solver(int M, double h, int dt, double r);

  void build_vectors();
  void build_matrixs();
  void solve();
};

#endif