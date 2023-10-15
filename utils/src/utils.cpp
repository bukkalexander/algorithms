#include "utils.hpp"

#include <iostream>

void print_array(const int* a, int n) {
    std::cout << "[";
    for (int i = 0; i < n; i++) {
        std::cout << a[i] << ", ";
    }
    std::cout << "]" << std::endl; 
}