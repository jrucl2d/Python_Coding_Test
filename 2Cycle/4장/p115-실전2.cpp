#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    string now;
    cin >> now;
    int col = now[0] - 'a';
    int row = now[1] - '0' - 1;
    int ans = 0;

    // 왼쪽
    if (col - 2 >= 0) {
        if (row - 1 >= 0) ans += 1;
        if (row + 1 < 8) ans += 1;
    }
    // 오른쪽
    if (col + 2 < 8) {
        if (row - 1 >= 0) ans += 1;
        if (row + 1 < 8) ans += 1;
    }
    // 위쪽
    if (row - 2 >= 0) {
        if (col - 1 >= 0) ans += 1;
        if (col + 1 < 8) ans += 1;
    }
    // 아래쪽
    if (row + 2 < 8) {
        if (col - 1 >= 0) ans += 1;
        if (col + 1 < 8) ans += 1;
    }
    cout << ans;

    return 0;
}