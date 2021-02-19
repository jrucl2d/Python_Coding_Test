#include <iostream>
#include <queue>
#define INF 1e9
using namespace std;

typedef pair<int, int> pii;

int t, n, arr[130][130], dist[130][130];

class Info{
public:
    int dist;
    pii pos;
    Info() {};
    Info(int d, pii a){
        dist = d;
        pos.first = a.first;
        pos.second = a.second;
    }
};

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

struct compare {
    bool operator() (Info& a, Info& b){
        return a.dist < b.dist;
    }
};

int dijkstra(){
    priority_queue<Info, vector<Info>, compare> pq;
    pq.push(Info(arr[0][0], {0, 0}));
    dist[0][0] = arr[0][0];
    while(!pq.empty()){
        Info now = pq.top();
        pq.pop();
        if(dist[now.pos.first][now.pos.second] < now.dist){
            continue;
        }
        for(int i = 0 ; i < 4; i++){
            int nx = now.pos.first + dx[i];
            int ny = now.pos.second + dy[i];
            if(nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
            int cost = now.dist + arr[nx][ny];
            if(dist[nx][ny] > cost){
                dist[nx][ny] = cost;
                pq.push(Info(cost, {nx, ny}));
            }
        }
    }
    return dist[n - 1][n - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    while(t--){
        cin >> n;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> arr[i][j];
                dist[i][j] = INF;
            }
        }
        cout << dijkstra() << "\n";
    }
    return 0;
}