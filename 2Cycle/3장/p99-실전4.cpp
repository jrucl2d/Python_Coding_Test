#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    cin >> n >> k;

    int ans = 0;
    while (n != 1) {
        if (n % k == 0)
            n /= k;
        else
            n -= 1;
        ans += 1;
    }
    cout << ans;
    return 0;
}