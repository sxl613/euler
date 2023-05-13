/**
 * @author      : szcz (szcz@$HOSTNAME)
 * @file        : euler69
 * @created     : Sunday Dec 04, 2022 15:46:32 GMT
 */

#include <stdio.h>
#include <stdlib.h>
#include "primes.h"

int is_perm(unsigned long long int a, unsigned long long int b) {
    int x[10] = { 0 };
    int y[10] = { 0 };

    while (a) {
        x[a % 10]++;
        a /= 10;
    }
    while (b) {
        y[b % 10]++;
        b /= 10;
    }
    for (size_t i = 0; i < 9; i++) {
        if (x[i] != y[i]) return 0;
    }
    return 1;
}

int main(void) {
    int n; int* ret;
    int r = fscanf(stdin, "%d", &n);
    if (r <= 0) exit(1);
    int m = sieve(&ret, n + 1);
    double ratio = 0.0; double min = 100.0;
    long long int ans = 0; long long int min_nf = 0;
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            unsigned long long int x = ret[j] * ret[i];
            unsigned long long int nf = (ret[i] - 1) * (ret[j] - 1);
            ratio = (double) x / nf;
            if (is_perm(x, nf)) {
                if (ratio < min && x < 10000000) {
                    min = ratio;
                    ans = x;
                    min_nf = nf;
                }
         }
        }
    }
    
    printf("minimum: %lld <-> %lld\n", ans, min_nf);
    free(ret);
    return 0;
}

