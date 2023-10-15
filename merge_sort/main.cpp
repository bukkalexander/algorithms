#include "utils.hpp"

#include <iostream>

void merge_sort(int* a, int n)
{
}

int main() {
    int n = 5;
    int a[] = {5, 2, 7, 1, 3};


    std::cout << "================================================" << std::endl;
    
    std::cout << "a = ";
    print_array(a, n);

    std::cout << "Sorting..." << std::endl;
    merge_sort(a, n);
    std::cout << "a = ";
    print_array(a, n);

    std::cout << "================================================" << std::endl;
    return 0;
}