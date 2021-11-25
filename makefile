all: compile run

compile:
	c++ main.cpp -o main.exe -std=c++11 -larmadillo

run: ./main.exe
