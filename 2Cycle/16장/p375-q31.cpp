#include <iostream>

using namespace std;

int n, m, t, arr[30][30], dp[30][30];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    while (t--) {
        for (int i = 0; i < 30; i++) {
            for (int j = 0; j < 30; j++) {
                dp[i][j] = 0;
            }
        }
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> arr[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            dp[i][0] = arr[i][0];
        }
        for (int j = 0; j < m - 1; j++) {
            for (int i = 0; i < n; i++) {
                if (i - 1 >= 0) {
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j]);
                }
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j]);
                if (i + 1 < n) {
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i + 1][j]);
                }
                dp[i][j + 1] += arr[i][j + 1];
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(dp[i][m - 1], ans);
        }
        cout << ans << "\n";
    }
    return 0;
}
