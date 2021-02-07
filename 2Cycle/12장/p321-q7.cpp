#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    cin >> s;
    int left = 0, right = 0, mid = s.size() / 2;
    for (int i = 0; i < s.size(); i++) {
        if (i < mid) {
            left += (s[i] - '0');
        } else {
            right += (s[i] - '0');
        }
    }
    string ans = left == right ? "LUCKY" : "READY";
    cout << ans;
    return 0;
}