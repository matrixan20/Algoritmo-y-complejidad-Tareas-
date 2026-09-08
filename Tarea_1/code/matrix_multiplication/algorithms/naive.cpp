// Codigo sacado de los PPT de la clase
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> matrixMult(vector<vector<int>>& M1, vector<vector<int>>& M2, int n) {
    // Se crea la matriz C de n x n llena de ceros
    vector<vector<int>> C(n, vector<int>(n, 0));
        
    // Cálculo de cada casilla C[i][j]
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                C[i][j] += M1[i][k] * M2[k][j];
            }
        }
    }
    return C;
}