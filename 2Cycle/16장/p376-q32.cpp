#include <iostream>

using namespace std;

int n, arr[510][510], dp[510][510];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> arr[i][j];
        }
    }
    dp[0][0] = arr[0][0];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (i == j) {
                dp[i][j] = arr[i][j] + dp[i - 1][j - 1];
            } else if (j == 0) {
                dp[i][j] = arr[i][j] + dp[i - 1][j];
            } else {
                int the_max = max(dp[i - 1][j - 1], dp[i - 1][j]);
                dp[i][j] = arr[i][j] + the_max;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, dp[n - 1][i]);
    }
    cout << ans;
    return 0;
}