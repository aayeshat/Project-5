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
cout << u << endl;
cx_vec U_col = cx_vec(pow(M-2, 2));
cout << U_col << endl;

cx_vec ncols(u.n_cols);
cout << ncols << endl;

cx_vec u_vec = vectorise(u);
cout << u_vec << endl;

return 0;
}


int k(int i,int j){
  return i + n*j
  }

}


// for (i = 0; i <= M - 2; i++){
//   for (j = 0; j <= M - 2; j++){
//   U_col[i] += u.col(i,j);
// }
// }
