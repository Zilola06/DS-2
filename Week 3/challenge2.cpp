#include <iostream>
using namespace std;

int binarySearch(int a[], int lo, int hi, int key) {
    //base case: empty range
    if (lo > hi) {
        return -1;
    }

    int mid = lo + (hi - lo) / 2;

    //key found
    if (a[mid] == key) {
        return mid;
    }

    //search left half
    if (key < a[mid]) {
        return binarySearch(a, lo, mid - 1, key);
    }

    //search right half
    return binarySearch(a, mid + 1, hi, key);
}

int main() {
    int a[] = {2, 5, 8, 12, 16, 23, 38, 45};
    int n = sizeof(a) / sizeof(a[0]);

    int key = 23;

    int result = binarySearch(a, 0, n - 1, key);

    cout << "index: " << result << endl;

    return 0;
}
