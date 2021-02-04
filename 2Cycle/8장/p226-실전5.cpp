#include <iostream>
#define INF 987654321
using namespace std;
int n, m, coins[110], dp[10010];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i <= m; i++) {
        dp[i] = INF;
    }
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
        dp[coins[i]] = 1;
    }
    for (int i = 1; i <= m; i++) {
        for (int j = 0; j < n; j++) {
            if (i - coins[j] <= 0 || dp[i - coins[j]] == INF) continue;
            dp[i] = min(dp[i], dp[i - coins[j]] + 1);
        }
    }
    int ans = dp[m] == INF ? -1 : dp[m];
    cout << ans;

    return 0;
}