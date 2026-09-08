#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include "algorithms/mergesort.cpp"
#include "algorithms/patiencesort.cpp"
#include "algorithms/quicksort.cpp"
#include "algorithms/sort.cpp"

using namespace std;

int main(int argc, char* argv[]) {
    if (argc < 5) {
        cerr << "Faltan argumentos. Uso: ./sorting <input_file> <output_file> <algorithm> <time_file>" << endl;
        return 1;
    }

    string ruta_ini = argv[1];
    string ruta_salida = argv[2];
    string ruta_tiempo = argv[3];
    string algoritmo = argv[4];

    ifstream archivo_entrada(ruta_ini);
    if (!archivo_entrada.is_open()) {
        cerr << "No se pudo abrir el archivo de entrada: " << ruta_ini << endl;
        return 1;
    }

    vector<int> array_original, array_ordenado;
    int numero;
    while (archivo_entrada >> numero) {
        array_original.push_back(numero);
    }
    archivo_entrada.close();

    array_ordenado = array_original;

    if (array_original.empty()) {
        cerr << "El archivo de entrada está vacío o no contiene números." << endl;
        return 1;
    }

    auto start = chrono::high_resolution_clock::now();

    if (algoritmo == "mergesort") {
        mergeSort(array_ordenado.data(), 0, array_ordenado.size() - 1);
    } else if (algoritmo == "patiencesort") {
        patienceSorting(array_ordenado);
    } else if (algoritmo == "quicksort") {
        quickSort(array_ordenado.data(), 0, array_ordenado.size() - 1);
    } else if (algoritmo == "sort") {
        sortArray(array_ordenado);
    } else {
        cerr << "Algoritmo desconocido: " << algoritmo << endl;
        return 1;
    }


    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();

    ofstream archivo_salida(ruta_salida);
    if (!archivo_salida.is_open()) {
        cerr << "No se pudo abrir el archivo de salida: " << ruta_salida << endl;
        return 1;
    }

    for (const auto& num : array_ordenado) {
        archivo_salida << num << " ";
    }
    archivo_salida.close();

    ofstream archivo_tiempo(ruta_tiempo);
    if (!archivo_tiempo.is_open()) {
        cerr << "No se pudo abrir el archivo de tiempo: " << ruta_tiempo << endl;
        return 1;
    }
    archivo_tiempo << duration << " microseconds" << endl;
    archivo_tiempo.close();
    
}