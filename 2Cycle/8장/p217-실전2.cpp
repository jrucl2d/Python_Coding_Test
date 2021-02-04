#include <iostream>
#define INF 987654321
using namespace std;

int n, dp[30010];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        dp[i] = INF;
    }
    dp[n] = 0;
    for (int i = n; i > 1; i--) {
        if (i % 5 == 0) {
            dp[i / 5] = min(dp[i / 5], dp[i] + 1);
        }
        if (i % 3 == 0) {
            dp[i / 3] = min(dp[i / 3], dp[i] + 1);
        }
        if (i % 2 == 0) {
            dp[i / 2] = min(dp[i / 2], dp[i] + 1);
        }
        dp[i - 1] = min(dp[i - 1], dp[i] + 1);
    }
    cout << dp[1];

    return 0;
}