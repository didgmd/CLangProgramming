#include <stdio.h>

double estimatePI(int n) {
    double pi = 0;
    int sign = 1;

    for (int i = 0; i < n; i++) {
        double term = 1.0 / (2 * i + 1);
        pi += sign * term;
        sign = -sign;
    }

    return 4 * pi;
}

int main() {
    int n = 10000;
    double result = estimatePI(n);
    printf("Estimated PI = %f\n", result);
    return 0;
}
