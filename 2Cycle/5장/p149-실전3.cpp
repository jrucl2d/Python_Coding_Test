#include <iostream>
#include <string>
using namespace std;

int n, m, ans = 0;
char arr[1010][1010];

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, -1, 0, 1};

void dfs(int y, int x) {
    // 체크인
    arr[y][x] = '1';

    // 갈 수 있으면 간다.
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny >= 0 && nx >= 0 && ny < n && nx < m && arr[ny][nx] == '0') {
            dfs(ny, nx);
        }
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    string tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        for (int j = 0; j < m; j++) {
            arr[i][j] = tmp[j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == '0') {
                ans += 1;
                dfs(i, j);
            }
        }
    }
    cout << ans;

    return 0;
}