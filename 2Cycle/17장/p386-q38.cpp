#include <iostream>
using namespace std;

int n, m, arr[501][501];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    int a, b;

    for(int i = 0; i < m; i++){
        cin >> a >> b;
        arr[a][b] = 1;
        arr[b][a] = 2;
    }
    for(int k = 1; k <= n; k++){
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(arr[i][k] == 1 && arr[k][j] == 1)
                    arr[i][j] = 1;
                else if (arr[i][k] == 2 && arr[k][j] == 2)
                    arr[i][j] = 2;
            }
        }
    }
    int cnt = 0;
    for(int i = 1; i <= n; i++){
        int inner_cnt = 0;
        for(int j = 1; j <= n; j++){
            if(arr[i][j] != 0) inner_cnt += 1;
        }
        if(inner_cnt == n - 1) cnt += 1;
    }
    cout << cnt;
    return 0;
}