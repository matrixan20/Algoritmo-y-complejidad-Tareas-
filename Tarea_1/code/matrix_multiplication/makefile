CXX = g++
CXXFLAGS = -std=c++17 -Wall -O3
EJECUTABLE = matrix_multiplication
SCRIPT_PYTHON = scripts/Automatizacion_matriz.py

all: $(EJECUTABLE)

$(EJECUTABLE): matrix_multiplication.cpp
	$(CXX) $(CXXFLAGS) matrix_multiplication.cpp -o $(EJECUTABLE)

run: $(EJECUTABLE)
	python3 $(SCRIPT_PYTHON)

clean:
	rm -f $(EJECUTABLE)