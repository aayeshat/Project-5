#include "schrodinger.hpp"

Schrodinger::Schrodinger(int M_in, double h_in, double dt_in){
    M = M_in;
    h = h_in;
    dt = dt_in;

    length = (M - 2) * (M - 2);

    A = sp_cx_mat(length, length);
    B = sp_cx_mat(length, length);

    a = cx_vec(length, fill::zeros);
    b = cx_vec(length, fill::zeros);
}

void Schrodinger::init(cx_double r, double v0, int n_slits, double slit_height, double slit_separation, double wall_thickness, double wall_x_pos){
    mat V = potential(v0, n_slits, slit_height, slit_separation, wall_thickness, wall_x_pos);
    vector(V, r);
    matrix(r);
}

// Function returning the potential matrix V(x,y) as a barrier with a variable number of slits configured by the argument n_slits

mat Schrodinger::potential(double v0, int n_slits, double slit_height, double slit_separation, double wall_thickness, double wall_x_pos){

    int wall_x_index = wall_x_pos / h;
    int wall_dx_index = wall_thickness / h;

    int slit_dy_index = slit_height / h;
    int slit_sep_index = slit_separation / h;

    double top_slit_y = 1.0 / 2.0 - n_slits / 2.0 * slit_height - (n_slits - 1.0) / 2.0 * slit_separation;
    int top_slit_index = top_slit_y * 1.0 / h;

    mat V = mat(M, M, fill::zeros);

    for (int i = wall_x_index; i < (wall_dx_index + wall_x_index); ++i){
        //
        V.submat(i, 0, i, M - 1).fill(v0);

        for (int j = 0; j < n_slits; ++j){
            int slit_top = top_slit_index + j * slit_dy_index + j * slit_sep_index;
            int slit_bottom = slit_top + slit_dy_index - 1;

            V.submat(i, slit_top, i, slit_bottom).fill(0);
        }
    }

    return V;
}

// Filling diagonal a- and b- vectors with elements solving the Schrodinger equation

void Schrodinger::vector(mat V, cx_double r){
    for (int j = 1; j <= M - 2; ++j){
        for (int i = 1; i <= M - 2; ++i){
            int k = get_k(i, j);
            a(k) = 1.0 + 4.0 * r + complex<double>(0, 1.0) * dt / 2.0 * V(i, j);
            b(k) = 1.0 - 4.0 * r - complex<double>(0, 1.0) * dt / 2.0 * V(i, j);
        }
    }
}

//Function to vectorize matrix U to vectors u

cx_vec Schrodinger::u_mat_to_vec(cx_mat u){
  cx_vec u_vec((M - 2) * (M - 2), fill::zeros);
  int col_len = M - 2;
  for (int i = 0; i < M - 2; ++i)
  {
    u_vec.subvec(col_len * i, col_len * (i + 1) - 1) = u.col(i);
  }
  return u_vec;
}

// Function to translate indices (i,j) of U matrix to an index k for u-vector

int Schrodinger::get_k(int i, int j){
    return (i - 1) + (j - 1) * (M - 2);
}

// Filling matrices A and B with diagonal and off-diagonal elements

void Schrodinger::matrix(cx_double r){

    A.diag(0) = a;
    B.diag(0) = b;

    A.diag(1).fill(-r);
    A.diag(-1).fill(-r);

    B.diag(1).fill(r);
    B.diag(-1).fill(r);

    A.diag(M - 2).fill(-r);
    A.diag(-(M - 2)).fill(-r);

    B.diag(M - 2).fill(r);
    B.diag(-(M - 2)).fill(r);

    for (int j = 0; j < length; ++j){
        if ((j + 1) % (M - 2) == 0 && j != (length - 1))
        {
            A(j, j + 1) = 0;
            A(j + 1, j) = 0;

            B(j, j + 1) = 0;
            B(j + 1, j) = 0;
        }
    }
}

//Function to initialize the internal state with a Gaussian wavepacket.
//The function returns normalized internal u-vectors

cx_vec Schrodinger::initialize_internal_state(double x_c, double y_c, double sigma_x, double sigma_y, double p_x, double p_y){
    mat x(M - 2, M - 2, fill::zeros);
    mat y(M - 2, M - 2, fill::zeros);

    for (int j{0}; j < M - 2; ++j){
        y.row(j) = trans(linspace(h, 1 - h, M - 2));
    }

    for (int i{0}; i < M - 2; ++i){
        x.col(i) = linspace(h, 1 - h, M - 2);
    }

    complex<double> i_imag(0, 1.0);
    cx_mat u_mat = exp(-(x - x_c) % (x - x_c) / (2 * sigma_x * sigma_x) - (y - y_c) % (y - y_c) / (2 * sigma_y * sigma_y) + i_imag * p_x * (x - x_c) + i_imag * p_y * (y - y_c));

    cx_vec u_vec = u_mat_to_vec(u_mat);
    cx_vec u_vec_conj = conj(u_vec);

    double norm_const = sqrt(sum(u_vec % u_vec_conj).real());

    return u_vec / norm_const;
}

//Function to solve the Crank-Nicolson matrix equations to evolve the system in time, i.e. find u for the next time step 

cx_cube Schrodinger::crank_nicolson(cx_vec u, int N){
    cx_vec b = cx_vec(u.size());
    cx_cube U_cube = cx_cube(M - 2, M - 2, N);

    cout << "Total time steps: " << N << endl;

    for (int n = 0; n < N; n++){
        cout << "Step: " << n << endl;
        b = B * u;
        u = spsolve(A, b);

        for (int i = 0; i < (M - 2); i++){
            for (int j = 0; j < (M - 2); j++){
                U_cube(i, j, n) = u(i + j * (M - 2));
            }
        }
    }


    return U_cube;
}
