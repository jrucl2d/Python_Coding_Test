#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    cin >> s;
    int ans = 0;
    for (int i = 0; i < s.size(); i++) {
        int now = s[i] - '0';
        if (now == 0 || ans == 0 || now == 1 || ans == 1) {
            ans += now;
        } else {
            ans *= now;
        }
    }
    cout << ans;
    return 0;
}