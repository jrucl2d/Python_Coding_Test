#include <iostream>

using namespace std;

class Info {
   public:
    int a;
    int b;
    int dir;
    Info() {
        a = 1;
        b = 1;
        dir = 0;
    }
};

int n, m, arr[52][52], ans = 1;
Info info;

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

void Input() {
    cin >> n >> m;
    int t1, t2, t3;
    cin >> t1 >> t2 >> t3;
    info.a = t1;
    info.b = t2;
    info.dir = t3;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }
    arr[t1][t2] = 2;  // 시작점
}
int turn_left(int dir) {
    return dir - 1 == -1 ? 3 : dir - 1;
}
bool can_go(int a, int b) {
    if (a < 0 || b < 0 || a >= n || b >= m) return false;
    if (arr[a][b] == 1 || arr[a][b] == 2) return false;
    return true;
}

void sol() {
    int turn_cnt = 0;
    while (true) {
        int now_dir = turn_left(info.dir);  // 왼쪽 방향
        int ny = info.a + dy[now_dir];
        int nx = info.b + dx[now_dir];
        if (turn_cnt == 4) {
            int back_dir = turn_left(turn_left(info.dir));
            ny = info.a + dy[back_dir];
            nx = info.b + dx[back_dir];
            if (arr[ny][nx] == 1) break;
            info.a = ny;
            info.b = nx;
            turn_cnt = 0;
            continue;
        }
        info.dir = now_dir;
        if (can_go(ny, nx)) {
            info.a = ny;
            info.b = nx;
            arr[ny][nx] = 2;
            ans += 1;
            turn_cnt = 0;
        } else {
            turn_cnt += 1;
        }
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    Input();
    sol();
    cout << ans;

    return 0;
}