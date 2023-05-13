/**
 * @author      : szcz (szcz@$HOSTNAME)
 * @file        : euler69
 * @created     : Sunday Dec 04, 2022 15:46:32 GMT
 */

#include <stdio.h>
#include <stdlib.h>
#include "primes.h"

int main(void) {
    int n; int* ret;
    int r = fscanf(stdin, "%d", &n);
    if (r <= 0) exit(1);
    int m = sieve(&ret, n);
    double rf, rr;
    rf = rr = 0.0;
    int maxx = 0;
    for (int x = 1; x < ret[m-1]; x++) {
        long long int nf = euler_totient(m, ret, x);
        printf("%d: %lld\n", x, nf);
        if (nf == 0) continue;
        rr = (double) x / nf;
        if (rr > rf) {
            rf = rr;
            maxx = x;
        }
    }
    printf("max ratio: %f, for %d (1 <= x <= %d)\n", rf, maxx, ret[m-1]);
    free(ret);
    return 0;
}

