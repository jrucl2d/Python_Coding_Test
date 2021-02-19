#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define INF 1e9
using namespace std;
typedef pair<int, int> pii;

int n, m, dist[20010];
vector<int> adj[20010];

bool comp(pii a, pii b){
    return a.first > b.first;
}

void dijk(int s){
    priority_queue<pii, vector<pii>> q;
    dist[s] = 0;
    q.push({0, s});
    while(!q.empty()){
        pii now_pii = q.top(); q.pop();
        int now_dist = -now_pii.first;
        int now_pos = now_pii.second;

        if(dist[now_pos] < now_dist) continue;

        for(int i = 0; i < adj[now_pos].size(); i++){
            int next = adj[now_pos][i];
            int cost = now_dist + 1;
            if(dist[next] > cost){
                dist[next] = cost;
                q.push({-cost, next});
            }
        }
    }
    vector<pii> before_ans;
    for(int i = 1; i <= n; i++){
        before_ans.push_back({dist[i], i});
    }
    sort(before_ans.begin(), before_ans.end(), comp);
    int d = before_ans[0].first;
    int num = INF;
    int cnt = 0;
    for(int i = 0; i < before_ans.size(); i++){
        if(before_ans[i].first == d){
            num = min(before_ans[i].second, num);
            cnt += 1;
        }
    }
    cout << num << " " << d << " " << cnt;
}

int main() {
    cin >> n >> m;
    int t1, t2;
    while(m--) {
        for(int i = 1; i <= n; i++){
            dist[i] = INF;
        }
        cin >> t1 >> t2;
        adj[t1].push_back(t2);
        adj[t2].push_back(t1);
    }
    dijk(1);
    return 0;
}