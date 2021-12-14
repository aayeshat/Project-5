# Project-5

## Simulating the two-dimensional time-dependent Schrödinger equation

The project5 folder contains source code containing all cpp, python python codes to generate plots and animation. Thw aim in this project is to study the behavoiur of a quantum particle in a box by using the normalizes schrodiner equation. To do so, a series of experiments (the single-, double- and triple-slit) are performed using this simulations. 

The main.cpp is set in such a way that it has all the arguments forgaussian wave packet and parameters to set up experiment either single slit or more slits for example slit sizes slit separation etc. It also stimulate and call functions fron schrodinger.cpp in which  all the necessary code is implemented for this project.

## Compiling 
g++ main.cpp schrodinger.cpp -larmadillo
