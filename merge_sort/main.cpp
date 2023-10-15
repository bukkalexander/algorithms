#include "utils.hpp"

#include <iostream>

void merge_sort(int* a, int i_start, int i_end);

void merge(int* a, int i_start, int i_mid, int i_end);

void merge_sort(int* a, int i_start, int i_end) {
    // base case
    std::cout << "sorting " << i_start << " " << i_end << std::endl;
    if (i_start == i_end) {
        return;
    }
    
    // divide
    // calculate the middle element index i_mid
    // i_start + (i_end - i_start) / 2 = (2*i_start + i_end - i_start) / 2 = (i_start + i_end) / 2
    int i_mid = (i_start + i_end) / 2; // floor
    std::cout << "dividing " << i_mid << std::endl;

    // conquer
    // recursively sort each sub array a[i_start:i_mid], a[i_mid+1:i_end]
    merge_sort(a, i_start, i_mid);
    merge_sort(a, i_mid + 1, i_end);
    

    // combine (merge)
    merge(a, i_start, i_mid, i_end);
    std::cout << "merge a[" << i_start << ":" << i_mid << "] and a[" << i_mid + 1 << ":" << i_end << "]" << std::endl;
}

void merge(int* a, int i_start, int i_mid, int i_end) {
    // merge the already sorted sub arrays a[i_start:i_mid] and a[i_mid+1:i_end]
    // into a single sorted array a[i_start:i_end]
    
    int n_left = i_mid - i_start + 1;
    int n_right = i_end - i_mid;

    int *left = new int[n_left];
    int *right = new int[n_right];

    for (int i = 0; i < n_left; i++) {
        left[i] = a[i_start + i];
    }

    for (int i = 0; i < n_right; i++) {
        right[i] = a[i_mid + 1 + i];
    }

    int i_left = 0;
    int i_right = 0;
    int i_a = i_start;
    while (i_left < n_left && i_right < n_right) {
        if (left[i_left] < right[i_right]) {
            a[i_a] = left[i_left];
            i_left++;
        } else {
            a[i_a] = right[i_right];
            i_right++;
        }
        i_a++;
    }

    while (i_left < n_left) {
        a[i_a] = left[i_left];
        i_left++;
        i_a++;
    }

    while (i_right < n_right) {
        a[i_a] = right[i_right];
        i_right++;
        i_a++;
    }
    
    delete[] left;
    delete[] right;

}

int main() {
    int n = 6;
    int a[] = {5, 0, 5, -1, 3, -6};

    std::cout << "================================================" << std::endl;
    
    std::cout << "a = ";
    print_array(a, n);

    std::cout << "Sorting..." << std::endl;
    merge_sort(a, 0, n-1);
    std::cout << "a = ";
    print_array(a, n);

    bool is_a_sorted = is_sorted(a, n);
    std::cout << "is_a_sorted=";
    if (is_a_sorted) {
        std::cout << "true";
    } else {
        std::cout << "false";
    }
    std::cout << std::endl;
    std::cout << "================================================" << std::endl;
    return 0;
}