#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    string a, b;
    cin >> a >> b;
    if (a.size() == b.size()) {
        int cnt = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] != b[i]) {
                cnt += 1;
            }
        }
        cout << cnt;
    } else {
        if (a.size() > b.size()) {
            string tmp = a;
            a = b;
            b = tmp;
        }
        int s = 0, cnt = 0;
        for (int i = 0; i < a.size(); i++) {
            for (int j = s; j < b.size(); j++) {
                if (a[i] == b[j]) {
                    s = j + 1;
                    cnt += 1;
                    break;
                }
            }
        }
        cout << b.size() - cnt;
    }

    return 0;
}