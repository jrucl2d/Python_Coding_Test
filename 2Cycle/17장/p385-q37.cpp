#include <iostream>
#include <vector>
#define INF 1e9
using namespace std;

int n, m, arr[110][110];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    int t1, t2, t3;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            arr[i][j] = INF;
            if(i == j) arr[i][j] = 0;
        }
    }
    for(int i = 0 ; i < m; i++){
        cin >> t1 >> t2 >> t3;
        arr[t1][t2] = min(arr[t1][t2], t3);
    }
    for(int k = 1; k <= n; k++){
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
            }
        }
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            int show = arr[i][j] == INF ? 0 : arr[i][j];
            cout << show << " ";
        }
        cout << "\n";
    }
    return 0;
}