#include <stdio.h>
#include <math.h>


int main() {
    for (int n = 1; n <= 30; n++) {
        float x = pow(0.1, n);
        printf("n = %2d | %.20e\n", n, x);
    }
    return 0;
}