#include <algorithm>
#include <vector>
#include <chrono>
#include <fstream>
#include <iostream>

using namespace std;

std::vector<int> sortArray(std::vector<int>& arr) {
    std::sort(arr.begin(), arr.end());  // std::sort de la STL
    return arr;
}
