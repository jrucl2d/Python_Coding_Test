#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#define INF 1e9

using namespace std;
int n, m, k, x, dist[300010];
vector<int> adj[1000010];

void bfs() {
    queue<int> q;
    q.push(x);
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        for (int i = 0; i < adj[now].size(); i++) {
            int next = adj[now][i];
            if (dist[next] > dist[now] + 1) {
                q.push(next);
                dist[next] = dist[now] + 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m >> k >> x;
    for (int i = 0; i <= n; i++) {
        dist[i] = INF;
    }
    dist[x] = 0;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    bfs();
    vector<int> ans;

    for (int i = 1; i <= n; i++) {
        if (dist[i] == k) {
            ans.push_back(i);
        }
    }
    if (ans.size() == 0) {
        cout << -1;
        return 0;
    }
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}
