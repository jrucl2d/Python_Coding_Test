#include <iostream>
using namespace std;

int n, arr[2010], ans = 0, dp[2010];
int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        dp[i] = 1;
        for(int j = 0; j < i; j++){
            if(arr[j] > arr[i]){
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int ans = 0;
    for(int i = 0 ; i < n; i++){
        ans = max(ans, dp[i]);
    }
    cout << n - ans;

    return 0;
}