#include <iostream>
#include <queue>
#include <string>
using namespace std;
typedef pair<int, int> pii;

int n, m, arr[210][210], visited[210][210];
queue<pii> q;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void bfs() {
    q.push({0, 0});
    visited[0][0] = true;

    while (!q.empty()) {
        pii now = q.front();
        q.pop();
        int before_val = visited[now.first][now.second];

        for (int i = 0; i < 4; i++) {
            int nx = now.first + dx[i];
            int ny = now.second + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < m && arr[nx][ny] == 1 && visited[nx][ny] == 0) {
                q.push({nx, ny});
                visited[nx][ny] = before_val + 1;
            }
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
            arr[i][j] = tmp[j] - '0';
        }
    }
    bfs();
    cout << visited[n - 1][m - 1];

    return 0;
}