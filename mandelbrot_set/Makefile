CXX= g++ -pthread
CXXFLAGS=  -Wall -Wextra -std=c++11 
SRC=main.c mandelbrot.cc
OBJ=$(SRC:.c=.o)


all: mandel

mandel:$(OBJ)
	$(CXX) -g -o mandel $(OBJ) $(CXXFLAGS)


#$(CXX) -o mandel $(OBJ) $(CXXFLAGS)
clean:
	rm -f *.o mandel
