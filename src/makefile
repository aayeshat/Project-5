all: compile run

compile:
	c++ main.cpp solver.cpp -o main.o -std=c++11 -larmadillo

run: ./main.o

clean: rm -f *.o *~