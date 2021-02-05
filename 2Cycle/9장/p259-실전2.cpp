#include <iostream>

#define INF 1e9
using namespace std;

int n, m, x, k, arr[110][110];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            arr[i][j] = i == j ? 0 : INF;
        }
    }

    int t1, t2;
    for (int i = 0; i < m; i++) {
        cin >> t1 >> t2;
        arr[t1][t2] = 1;
        arr[t2][t1] = 1;
    }
    cin >> x >> k;

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
            }
        }
    }
    if (arr[1][k] == INF || arr[k][x] == INF) {
        cout << -1;
    } else {
        cout << arr[1][k] + arr[k][x];
    }

    return 0;
}