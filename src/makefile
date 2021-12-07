all: compile run

compile:
	c++ main.cpp Schrodinger.cpp -o main.exe -std=c++11 -larmadillo

run: ./main.exe

clean: rm -f *.o *~
