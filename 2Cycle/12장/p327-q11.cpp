#include <deque>
#include <iostream>
#define APPLE 1
#define BODY 2
using namespace std;

class Info {
   public:
    int time;
    char dir;
    Info(){};
};

int n, k, l, arr[110][110], time = 0;
Info info[110];
int info_index = 0;
deque<pair<int, int>> body;

// up, left, down, right
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
int now_dir = 3;           // first right dir
int now_x = 1, now_y = 1;  // now pos

void input() {
    cin >> n >> k;
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        arr[a][b] = APPLE;
    }
    cin >> l;
    for (int i = 0; i < l; i++) {
        int a;
        char c;
        cin >> a >> c;
        info[i].time = a;
        info[i].dir = c;
    }
}

void turn_left() {
    now_dir = now_dir + 1 == 4 ? 0 : now_dir + 1;
}
void turn_right() {
    now_dir = now_dir - 1 == -1 ? 3 : now_dir - 1;
}
bool check_end(int x, int y) {
    if (x == 0 || y == 0 || x == n + 1 || y == n + 1) {
        return true;
    }
    if (arr[x][y] == BODY) {
        return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    input();
    body.push_back({1, 1});
    while (true) {
        time += 1;
        int nx = now_x + dx[now_dir], ny = now_y + dy[now_dir];
        if (check_end(nx, ny)) {
            cout << time;
            break;
        }
        // apple
        if (arr[nx][ny] == APPLE) {
            arr[nx][ny] = BODY;
            body.push_back({nx, ny});
        }

        // noraml
        else if (arr[nx][ny] == 0) {
            int del_x = body.front().first, del_y = body.front().second;
            arr[del_x][del_y] = 0;
            arr[nx][ny] = BODY;
            body.push_back({nx, ny});
            body.pop_front();
        }

        now_x = nx, now_y = ny;

        // dir turn
        if (info[info_index].time == time) {
            char turn_dir = info[info_index].dir;
            info_index += 1;
            if (turn_dir == 'L') {
                turn_left();
            } else {
                turn_right();
            }
        }
    }

    return 0;
}