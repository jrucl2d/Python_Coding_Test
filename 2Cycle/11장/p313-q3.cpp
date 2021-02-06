#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    cin >> s;
    int now = s[0];
    int cnt[2] = {0, 0};
    cnt[now - '0'] += 1;
    for (int i = 1; i < s.size(); i++) {
        if (now != s[i]) {
            now = s[i];
            cnt[now - '0'] += 1;
        }
    }
    cout << min(cnt[0], cnt[1]);
    return 0;
}