#include <stdio.h>

void modifyValue(int* num) {
    *num = *num * 2;
}

int main() {
    int value = 10;
    modifyValue(&value);
    printf("Modified value: %d\n", value);

    return 0;
}
