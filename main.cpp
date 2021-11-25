#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <complex>
#include <cmath>

using namespace arma;

int k(int i,int j);

int main(){
int i, j;
int M = 5;
cx_mat u = cx_mat(M-2, M-2, fill::randu);
cx_vec U_col = cx_vec(pow(M-2, 2));
cx_vec u_vec = vectorise(u);

cx_vec a = cx_vec(9);
cx_vec b = cx_vec(9);


return 0;
}


int k(int i,int j){
  return i + n*j
}
