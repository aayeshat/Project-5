# Project-5

## Simulating the two-dimensional time-dependent Schrödinger equation

We have used the Crank-Nicolson method to solve the time-dependent Schödinger equation in two dimensions, as slit diffraction experiments. We use a Gaussian wavepacket that is passed through a potential barrier, where the number og slits can be varied in main.cpp. In the folder data/plots, we have an animation clearly showing the simulation. 

-------

schrodinger.cpp contains all functions used. Vary the different parameters and call functions in main.cpp.

-------

## Compile & run
g++ main.cpp schrodinger.cpp -larmadillo && ./a.out

## Compile & run MacOs

add compiler flag std=c++11 -larmadillo

------

Installation of the Armadillo library is needed.

