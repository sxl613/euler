// https://mathworld.wolfram.com/PartitionFunctionP.html
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef long double ld;
ll MOD = 1000000;
ll Px [10000000] = { 0 };

llu modulo( ll value, ll m) {
    int mod = value % (ll)m;
    if (mod < 0) {
        mod += m;
    }
    return mod;
}

ll Pn (ll n) {
  if (n < 0) return 0;
  if (Px[n] > 0) {
    return modulo(Px[n], MOD);
  }
  ll ans = 0;
  ll bound = (ll) sqrt(n);
  for (ll k = 1; k <= bound; k++) {
    ll n1 = n - k * (3 * k - 1) / 2;
    ll n2 = n - k * (3 * k + 1) / 2;
    ll Pn1 = Pn(n1);
    ll Pn2 = Pn(n2);
    ll s = Pn1 + Pn2;
    if (k % 2 == 1) {
      ans += s;
    }
    else
    {
      ans -= s;
    }
  }
  Px[n] = modulo(ans, MOD);
  return Px[n];
}

int solve() {
  int n;
  cin >> n;
  ll ans = 0;
  for (int i = 1; i <= n; i++) {
    ans = Pn(i);
    if (ans == 0) {
      cout << "P(" << i << ") = " << ans << endl;
      return 0;
    }
  }
  return 0;
}

int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  Px[0] = 1;
  solve();
}
