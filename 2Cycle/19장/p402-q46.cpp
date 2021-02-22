#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9
using namespace std;
typedef pair<int, int> pii;
int n, arr[21][21];
int cnt = 0;

// shark info
int ssize = 2;
int ecnt = 0;
int sx = 0, sy = 0;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

vector<vector<int>> bfs(){
    vector<vector<int>> v(n, vector<int>(n, INF));
    queue<pair<pii, int>> q;

    int now_x = 0, now_y = 0, now_cnt = 0;
    q.push({{sx, sy}, 0});
    
    while(!q.empty()){
        pair<pii, int> now_inf = q.front(); q.pop();
        now_x = now_inf.first.first;
        now_y = now_inf.first.second;
        now_cnt = now_inf.second;
        if(v[now_x][now_y] != INF) continue;
        v[now_x][now_y] = min(v[now_x][now_y], now_cnt);
        for(int i = 0; i < 4; i ++){
            int nx = now_x + dx[i];
            int ny = now_y + dy[i];
            if(nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
            if(arr[nx][ny] > ssize) continue;
            q.push({{nx, ny}, now_cnt + 1});
        }
    }
    return v;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> arr[i][j];
            if(arr[i][j] == 9){
                sx = i, sy = j;
                arr[i][j] = 0;
            }
        }
    }       
    while(true){
        vector<vector<int>> dist = bfs();
        int shortest = INF;
        int rx = 0, ry = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){     
                if(dist[i][j] < shortest && arr[i][j] != 0 && arr[i][j] < ssize){
                    shortest = dist[i][j];
                    rx = i, ry = j;
                }
            }
        }
        if(shortest == INF) break;
        arr[rx][ry] = 0;
        sx = rx, sy = ry;
        ecnt += 1;
        if(ecnt == ssize){
            ecnt = 0;
            ssize += 1;
        }
        cnt += shortest;
    }
    cout << cnt;
    return 0;
}