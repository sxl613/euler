#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef long double ld;

ll Pn (int n, map<ll , ll>& d) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  if (d[n] != 0) return d[n];
  ll ans = 0;
  for (int i = 1; i <= n; i++) {
    ans += ((i % 2 == 1) ? 1 : -1) * (Pn(n - (i*(3*i-1))/2, d) + Pn(n - (i*(3*i+1)/2), d));
  }
  d[n] = ans;
  return ans;
}

int solve() {
  int n;
  cin >> n;
  map<ll, ll> d;
  cout << "P(" << n << ") = " << Pn((ll)n, d) << endl;
  return 0;
}

int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  solve();
  }
