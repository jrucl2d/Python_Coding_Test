#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m, ball[11], tmp;
    for (int i = 0; i < 11; i++) {
        ball[i] = 0;
    }
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        ball[tmp] += 1;
    }
    int ans = 0;

    for (int i = 1; i <= m; i++) {
        n -= ball[i];
        ans += ball[i] * n;
    }
    cout << ans;

    return 0;
}