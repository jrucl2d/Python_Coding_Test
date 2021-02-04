#include <iostream>

using namespace std;
int n, arr[110], dp[110];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    dp[0] = arr[0];
    dp[1] = max(arr[0], arr[1]);
    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 1]);
    }
    cout << dp[n - 1];

    return 0;
}