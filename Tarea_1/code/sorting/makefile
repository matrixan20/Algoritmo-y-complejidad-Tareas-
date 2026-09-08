CXX = g++
CXXFLAGS = -std=c++17 -Wall -O3
EJECUTABLE = sorting
SCRIPT_PYTHON = scripts/Automatizacion_sort.py

all: $(EJECUTABLE)

$(EJECUTABLE): sorting.cpp
	$(CXX) $(CXXFLAGS) sorting.cpp -o $(EJECUTABLE)

run: $(EJECUTABLE)
	python3 $(SCRIPT_PYTHON)

clean:
	rm -f $(EJECUTABLE)