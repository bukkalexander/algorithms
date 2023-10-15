#include "utils.hpp"

#include <iostream>

void sort(int* a, int i_start, int i_end);

void merge(int* a, int i_start, int i_mid, int i_end);

void merge_sort(int* a, int n) {
    
    sort(a, 0, n-1);
}

void sort(int* a, int i_start, int i_end) {
    // base case

    std::cout << "sorting " << i_start << " " << i_end << std::endl;
    if (i_start == i_end) {
        return;
    }
    
    // divide
    // calculate the middle element index i_mid
    // i_start + (i_end - i_start) / 2 = (2*i_start + i_end - i_start) / 2 = (i_start + i_end) / 2
    int i_mid = (i_start + i_end) / 2;
    std::cout << "dividing " << i_mid << std::endl;
    // conquer
    // recursively sort each sub array a[i_start:i_mid], a[i_mid+1:i_end]
    sort(a, i_start, i_mid);
    sort(a, i_mid + 1, i_end);
    

    // combine (merge)
    merge(a, i_start, i_mid, i_end);
    std::cout << "combine" << "a[" << i_start << ":" << i_mid << "] and a[" << i_mid + 1 << ":" << i_end << "]" << std::endl;
}

void merge(int* a, int i_start, int i_mid, int i_end) {
    // merge the already sorted sub arrays a[i_start:i_mid] and a[i_mid+1:i_end]
    // into a single sorted array a[i_start:i_end]

    int n = i_end - i_start + 1;
    int i_b = 0;
    int *b = new int[n];

    int i_left_start = i_start;
    int i_left_end = i_mid;
    int i_left_out = i_left_end + 1;

    int i_right_start = i_mid + 1;
    int i_right_end = i_end;
    int i_right_out = i_right_end + 1;
    
    int i_left = i_left_start;
    int i_right = i_right_start;

    while (i_b < n && i_left < i_left_out && i_right < i_right_out) {
        if (a[i_left] < a[i_right]) {
            b[i_b] = a[i_left];
            i_left++;
        } else {
            b[i_b] = a[i_right];
            i_right++;
        }
        i_b++;
    }

    while (i_left < i_left_out) {
        b[i_b] = a[i_left];
        i_left++;
        i_b++;
    }

    while (i_right < i_right_out) {
        b[i_b] = a[i_right];
        i_right++;
        i_b++;
    }

    // copy the sorted array b into a[i_start:i_end]
    for (int i = 0; i < n; i++) {
        a[i_start+i] = b[i];
    }

    delete[] b;
    std::cout << "hej"<< std::endl;

}

int main() {
    int n = 6;
    int a[] = {5, 2, 7, 1, 3, -6};


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