#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    cin >> s;
    vector<char> ch;
    int num = 0;

    for (int i = 0; i < s.size(); i++) {
        int now = s[i] - '0';
        if (now >= 0 && now <= 9) {
            num += now;
        } else {
            ch.push_back(s[i]);
        }
    }
    sort(ch.begin(), ch.end());
    for (int i = 0; i < ch.size(); i++) {
        cout << ch[i];
    }
    cout << num;

    return 0;
}