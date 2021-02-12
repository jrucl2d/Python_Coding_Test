#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Virus {
   public:
    int x;
    int y;
    int num;
    int time;
    Virus() {}
    Virus(int x, int y, int num, int time) {
        this->x = x;
        this->y = y;
        this->num = num;
        this->time = time;
    }
};
bool comp(Virus a, Virus b) {
    return a.num < b.num;
}

int n, k, arr[210][210], s, x, y;
queue<Virus> q;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

int bfs() {
    while (!q.empty()) {
        Virus now = q.front();
        q.pop();
        if (now.time == s) {
            break;
        }
        for (int d = 0; d < 4; d++) {
            int nx = now.x + dx[d];
            int ny = now.y + dy[d];
            if (nx >= 1 && ny >= 1 && nx <= n && ny <= n) {
                if (arr[nx][ny] == 0) {
                    arr[nx][ny] = now.num;
                    q.push(Virus(nx, ny, now.num, now.time + 1));
                }
            }
        }
    }
    return arr[x][y];
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k;
    vector<Virus> tmp;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 0) continue;
            tmp.push_back(Virus(i, j, arr[i][j], 0));
        }
    }
    sort(tmp.begin(), tmp.end(), comp);
    for (int i = 0; i < tmp.size(); i++) {
        q.push(tmp[i]);
    }

    cin >> s >> x >> y;
    cout << bfs();

    return 0;
}