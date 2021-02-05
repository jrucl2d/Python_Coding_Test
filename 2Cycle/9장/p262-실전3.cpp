#include <iostream>
#include <queue>
#include <vector>
#define INF 1e9
using namespace std;
typedef pair<int, int> pii;

int n, m, c, dist[30010];
vector<pii> adj[30010];

void dijikstra() {
    for (int i = 0; i < 30010; i++) {
        dist[i] = INF;
    }
    priority_queue<pii> pq;
    dist[c] = 0;
    pq.push({0, c});
    while (!pq.empty()) {
        int now_cost = pq.top().first;
        int now_pos = pq.top().second;
        pq.pop();
        // 이미 지난번에 최저 cost를 찾은 경우에는 넘긴다.
        // 매 반복마다 최저 cost를 무조건 하나씩 찾기 때문에 이미 지난 것은 무쓸모.
        if (dist[now_pos] < now_cost) continue;

        for (int i = 0; i < adj[now_pos].size(); i++) {
            int next_pos = adj[now_pos][i].first;
            int next_cost = adj[now_pos][i].second;
            if (dist[now_pos] + next_cost < dist[next_pos]) {
                dist[next_pos] = dist[now_pos] + next_cost;
                pq.push({dist[next_pos], next_pos});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m >> c;
    int x, y, z;
    for (int i = 0; i < m; i++) {
        cin >> x >> y >> z;
        adj[x].push_back({y, z});  // x에서 y로 가는 데 걸리는 시간 z
    }
    int ans = 0, cnt = 0;
    dijikstra();
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INF || i == c) continue;
        cnt += 1;
        ans = max(ans, dist[i]);
    }
    cout << cnt << " " << ans;
    return 0;
}