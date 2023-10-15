#include "utils.hpp"

#include <iostream>

void print_array(const int* a, int n) {
    std::cout << "[";
    for (int i = 0; i < n; i++) {
        std::cout << a[i] << ", ";
    }
    std::cout << "]" << std::endl; 
}

bool is_sorted(int *a, int n) {
    for (int i = 0; i < n - 1; i++) {
        if (a[i+1] < a[i]) {
            return false;
        }
    }
    return true;
}