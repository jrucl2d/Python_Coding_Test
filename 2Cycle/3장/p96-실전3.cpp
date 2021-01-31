#include <iostream>
#define INF 987654321
using namespace std;

int n, m, ans = -1;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int the_min = INF, tmp;
        for (int j = 0; j < m; j++) {
            cin >> tmp;
            the_min = min(the_min, tmp);
        }
        ans = max(ans, the_min);
    }
    cout << ans;

    return 0;
}