#include <iostream>

using namespace std;
typedef pair<int, int> pii;

int n, dp[16];
pii arr[16];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    int t1, t2;
    for (int i = 1; i <= n; i++) {
        cin >> t1 >> t2;
        arr[i].first = t1;
        arr[i].second = t2;
    }
    for (int i = 1; i <= n; i++) {
        if (i + arr[i].first <= n + 1) {
            dp[i] = max(arr[i].second, dp[i]);
        }
        for (int j = i + arr[i].first; j <= n; j++) {
            if (j + arr[j].first <= n + 1) {
                dp[j] = max(dp[j], dp[i] + arr[j].second);
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        ans = max(ans, dp[i]);
    }
    cout << ans;
    return 0;
}