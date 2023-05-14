/**
 * @author      : szcz (szcz@$HOSTNAME)
 * @file        : primes
 * @created     : Sunday Dec 04, 2022 15:35:17 GMT
 */
 #define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; })

 #define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _b : _a; })
#include <stdio.h>
#include <stdlib.h>

int sieve(int** ret, int N) {
    int M = (N+1)/2 + 1;
    int c = 0;
    int* arr = malloc(sizeof(int) * M);
    for (size_t i =0; i < M; i++) {
        arr[i] = 1;
    }
    for (size_t i = 1; i < M; i++) {
        for (size_t j = 3*i + 1; j < min(M, 2*i*i + 2*i + 1); j += 2*i + 1) {
            arr[j] = 0;
        }
    }
    for (size_t i = 1; i < M; i++) {
        if (arr[i]) c++;
    }
    *ret = (int*) malloc(sizeof(int) * c);
    size_t k = 0;
    for (size_t i = 1; i < M; i++) {
        if (arr[i]) (*ret)[k++] = 2*i + 1;
    }
    free(arr);
    return c;
}

int lower_bound(int* arr, int n, int x) {
    int lo, hi, mid;
    lo = 0;
    hi = n;
    while (lo < hi) {
        mid = lo + (hi - lo)/2;
        if (arr[mid] >= x) {
            hi = mid;
        }
        else {
            lo = mid + 1;
        }
    }
    return lo;
}

int upper_bound(int* arr, int n, int x) {
    int lo, hi, mid;
    lo = 0;
    hi = n;
    while (lo < hi) {
        mid = lo + (hi - lo)/2;
        if (arr[mid] <= x) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
    }
    return lo;
}

long long int euler_totient(int m, int* primes, int n) {
    /*
     * Finds the number of factors of `n` using primes from `primes` array.
    */
    int a = n;
    int div2 = 0;
    while (a % 2 == 0) {
        div2++;
        a /= 2;
    }
    long long int num, den;
    num = den = 1;
    if (div2 > 0) den *= 2;
    int r = -1;
    while (a > 1) {
        int k = lower_bound(primes, m, a);
        if (k == m) k--;
        while (k >= 0) {
            if (a % primes[k] == 0) {
                if (r != k) {
                    num *= primes[k]-1;
                    den *= primes[k]; r = k;
                }
                a /= primes[k];
            }
            else {
                k--;
            }
        }
    }
    return (num * n) / den;
}

