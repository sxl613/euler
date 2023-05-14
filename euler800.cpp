#include <cmath>
#include <functional>
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

vector<int> sieve(int m) {
  int n = (int)m / 2;
  vector<int> primes;
  vector<char> isPrime(n + 1, true);
  primes.push_back(2);

  for (long long i = 1; i <= n; i++) {
    if (isPrime[i]) {
      primes.push_back((int)(2 * i + 1));
      for (long long j = 2 * i * i + 2 * i; j <= n; j += 2 * i + 1) {
        isPrime[j] = false;
      }
    }
  }
  return primes;
}

int lower_bound(const vector<int> &arr, long long x) {
  long long lo, hi, mid;
  lo = 0;
  hi = (int)arr.size();
  while (lo < hi) {
    mid = lo + (hi - lo) / 2;
    if (arr[mid] >= x) {
      hi = mid;
    } else {
      lo = mid + 1;
    }
  }
  return (int)lo;
}

int upper_bound(const vector<int> &arr, long long x) {
  long long lo, hi, mid;
  lo = 0;
  hi = (int)arr.size();
  while (lo < hi) {
    mid = lo + (hi - lo) / 2;
    if (arr[mid] <= x) {
      lo = mid + 1;
    } else {
      hi = mid;
    }
  }
  return (int)lo;
}

int lower_bound(long long a, long long b, std::function<double(long long)> f) {
  long long m;
  while (a < b) {
    m = (b - a) / 2 + a;
    if (f(m) >= 0) {
      b = m;
    } else {
      a = m + 1;
    }
  }
  return (int)a;
}

int upper_bound(long long a, long long b, std::function<double(long long)> f) {
  long long m;
  while (a < b) {
    m = (b - a) / 2 + a;
    if (f(m) <= 0) {
      a = m + 1;
    } else {
      b = m;
    }
  }
  return (int)a;
}

int count_primes(long long a, long long b, const vector<int> &primes) {
  int i = lower_bound(primes, a);
  int j = upper_bound(primes, b);
  return j - i;
}

long long hybrid(int a, int b, const vector<int> &primes) {
  double lim = log((double)a) * b;
  long long ans = 0;
  for (auto &p : primes) {
    double logp = log((double)p);
    double llim = ((double)lim) / logp;
    long long ullim = (long long)floor(llim);
    int k = upper_bound(p + 1, ullim,
                        [=](long long v) { return (double)(logp * (double)v) + log(v) * p - lim; });
    int count = count_primes(p + 1, k-1, primes);
    ans += count;
    if (count == 0)
      break;
  }
  return ans;
}

int main() {
  vector<int> primes = sieve(3e7);
  cout << hybrid(800, 1, primes) << endl;
  cout << hybrid(800, 800, primes) << endl;
  cout << hybrid(800800, 800800, primes) << endl;
  return 0;
}