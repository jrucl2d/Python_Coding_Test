#include <iostream>
#include <queue>
#include <vector>

using namespace std;
typedef pair<int, int> pii;
int n, l, r, arr[51][51];
bool visited[51][51];
queue<pii> q;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

bool bfs() {
    // init
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            visited[i][j] = false;
        }
    }
    vector<pii> now_visiting;
    int move_cnt = 0;

    // brute-force
    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            if (visited[a][b]) continue;
            // check in
            visited[a][b] = true;
            q.push({a, b});                  // for bfs
            now_visiting.push_back({a, b});  // for calculating new value

            // while q is not empty
            while (!q.empty()) {
                pii now = q.front();
                q.pop();
                for (int i = 0; i < 4; i++) {
                    int nx = now.first + dx[i];
                    int ny = now.second + dy[i];
                    if (nx >= 0 && ny >= 0 && nx < n && ny < n && visited[nx][ny] == false) {
                        if (abs(arr[now.first][now.second] - arr[nx][ny]) >= l && abs(arr[now.first][now.second] - arr[nx][ny]) <= r) {
                            move_cnt += 1;  // union count
                            visited[nx][ny] = true;
                            q.push({nx, ny});
                            now_visiting.push_back({nx, ny});
                        }
                    }
                }
            }
            // calculate new value
            int inner_sum = 0;
            for (int i = 0; i < now_visiting.size(); i++) {
                int na = now_visiting[i].first;
                int nb = now_visiting[i].second;
                inner_sum += arr[na][nb];
            }
            int new_val = inner_sum / now_visiting.size();

            // set new value
            while (now_visiting.size() > 0) {
                int na = now_visiting.back().first;
                int nb = now_visiting.back().second;
                arr[na][nb] = new_val;
                now_visiting.pop_back();
            }
        }
    }
    if (move_cnt == 0) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> l >> r;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    int ans = 0;
    while (true) {
        if (bfs() == false) break;
        ans += 1;
    }
    cout << ans;

    return 0;
}