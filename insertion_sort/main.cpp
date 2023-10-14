#include <iostream>

void insertion_sort(int* a, int n)
{
    int j;
    for (int i = 1; i < n; i++) {
        int key = a[i];
        j = i - 1;
        while (j > -1 && a[j] > key) {
            a[j + 1] = a[j];
            j--; 
        }
        a[j + 1] = key;
    }
}


void print_array(const int* a, int n) {
    std::cout << "[";
    for (int i = 0; i < n; i++) {
        std::cout << a[i] << ", ";
    }
    std::cout << "]" << std::endl; 
}

int main() {
    int n = 5;
    int a[] = {5, 2, 7, 1, 3};


    std::cout << "================================================" << std::endl;
    
    std::cout << "a = ";
    print_array(a, n);

    std::cout << "Sorting..." << std::endl;
    insertion_sort(a, n);
    std::cout << "a = ";
    print_array(a, n);

    std::cout << "================================================" << std::endl;
    return 0;
}