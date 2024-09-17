#include <stdio.h>

int main() {
    int arr[] = { 1, 2, 3, 4, 5 };
    int* ptr = arr;

    for (int i = 0; i < 5; i++) {
        printf("Element %d: %d\n", i, *ptr);
        ptr++;
    }

    return 0;
}
