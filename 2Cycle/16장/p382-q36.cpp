#include <iostream>
#include <string>
using namespace std;

int dp[5001][5001];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    string a, b;
    cin >> a >> b;
    for(int i = 1; i <= b.size(); i++){
        dp[0][i] = i;
    }
    for(int i = 1; i <= a.size(); i++){
        dp[i][0] = i;
    }
    for(int i = 1; i <= a.size(); i++){
        for(int j = 1; j <= b.size(); j++){
            if(a[i - 1] == b[j - 1]){
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = min(min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]) + 1;
            }
        }
    }
    cout << dp[a.size()][b.size()];

    return 0;
}