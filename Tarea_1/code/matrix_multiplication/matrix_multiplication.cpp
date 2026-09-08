#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include "algorithms/strassen.cpp"
#include "algorithms/naive.cpp"

using namespace std;

// Función para leer una matriz desde un archivo de texto número por número
vector<vector<int>> leer_matriz(string ruta, int n) {
    ifstream archivo(ruta);
    vector<vector<int>> matriz(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            archivo >> matriz[i][j];
        }
    }
    return matriz;
}

// Función para guardar una matriz en el archivo "_out.txt"
void guardar_matriz(string ruta, const vector<vector<int>>& matriz, int n) {
    ofstream archivo(ruta);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            archivo << matriz[i][j] << " ";
        }
        archivo << "\n";
    }
}

int main(int argc, char* argv[]) {
    // Ahora pedimos 7 argumentos exactos (igual que los manda Python)
    if (argc < 7) {
        cerr << "Uso: ./matrix_multiplication <input1> <input2> <output> <tiempo> <algoritmo> <tamaño>" << endl;
        return 1;
    }

    string ruta_ini1 = argv[1];
    string ruta_ini2 = argv[2];
    string ruta_salida = argv[3];
    string ruta_tiempo = argv[4];
    string algoritmo = argv[5];
    int tamaño = stoi(argv[6]);

    // 1. Leer matrices usando la función (Todo es vector<vector<int>>)
    vector<vector<int>> A = leer_matriz(ruta_ini1, tamaño);
    vector<vector<int>> B = leer_matriz(ruta_ini2, tamaño);
    vector<vector<int>> Salida;

    // 2. Medir tiempo y ejecutar el algoritmo correspondiente
    auto start = chrono::high_resolution_clock::now();
    
    if (algoritmo == "strassen") {
        // Llamamos a tu función adaptada de Strassen
        Salida = ConvertToSquareMat(A, B, tamaño, tamaño, tamaño, tamaño);
    } else if (algoritmo == "naive") {
        // Llamamos a tu algoritmo Naive actualizado
        Salida = matrixMult(A, B, tamaño);
    } else {
        cerr << "Algoritmo desconocido: " << algoritmo << endl;
        return 1;
    }
    
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();

    // 3. Guardar matriz resultante en su txt
    guardar_matriz(ruta_salida, Salida, tamaño);

    // 4. Guardar tiempo en el CSV para los gráficos
    ofstream archivo_tiempo(ruta_tiempo);
    if (archivo_tiempo.is_open()) {
        archivo_tiempo << duration << "\n";
        archivo_tiempo.close();
    } else {
        cerr << "No se pudo abrir el archivo de tiempo: " << ruta_tiempo << endl;
    }

    return 0;
}