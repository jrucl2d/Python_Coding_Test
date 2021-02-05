#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Info {
   public:
    int from;
    int to;
    int cost;
    Info(){};
    Info(int f, int t, int c) {
        from = f;
        to = t;
        cost = c;
    }
};

bool comp(Info a, Info b) {
    return a.cost < b.cost;
}

int n, m, parent[100010], the_max = 0;
vector<Info> adj;
vector<int> ans;

int find_p(int a) {
    if (parent[a] != a) {
        parent[a] = find_p(parent[a]);
    }
    return parent[a];
}
void union_p(int a, int b) {
    a = find_p(a);
    b = find_p(b);
    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    int t1, t2, t3;
    for (int i = 0; i < m; i++) {
        cin >> t1 >> t2 >> t3;
        adj.push_back({t1, t2, t3});
    }
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    sort(adj.begin(), adj.end(), comp);

    // kruskal
    for (int i = 0; i < m; i++) {
        int cost = adj[i].cost;
        int from = adj[i].from;
        int to = adj[i].to;
        if (find_p(from) != find_p(to)) {
            // if no cycle
            union_p(from, to);
            ans.push_back(cost);
            the_max = max(the_max, cost);
        }
    }
    int res = 0;
    for (int i = 0; i < ans.size(); i++) {
        res += ans[i];
    }
    cout << res - the_max;

    return 0;
}