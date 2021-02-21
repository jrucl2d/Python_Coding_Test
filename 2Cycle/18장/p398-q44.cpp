#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
class Info{
public:
    int x, y, z;
    Info(){};
    Info(int a, int b, int c) {
        x = a, y = b, z = c;
    }
};

int n;
vector<Info> adj; // dist, a, b
int parent[100010];
pii x[100010];
pii y[100010];
pii z[100010];

int find_p(int a){
    if(parent[a] != a){
        parent[a] = find_p(parent[a]);
    }
    return parent[a];
}
void union_p(int a, int b){
    a = find_p(a);
    b = find_p(b);
    if(a < b){
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}
bool comp(Info a, Info b){
    return a.x < b.x;
}
bool comp2(pii a, pii b){
    return a.first < b.first;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++){
        parent[i] = i;
    }
    int t1, t2, t3;
    for(int i = 0; i < n; i++) {
        cin >> t1 >> t2 >> t3;
        x[i].first = t1, x[i].second = i;
        y[i].first = t2, y[i].second = i;
        z[i].first = t3, z[i].second = i;
    }
    sort(x, x + n, comp2);
    sort(y, y + n, comp2);
    sort(z, z + n, comp2);
    for(int i = 0 ; i < n - 1 ; i++){
        adj.push_back(Info(abs(x[i].first - x[i + 1].first), x[i].second, x[i + 1].second));
        adj.push_back(Info(abs(y[i].first - y[i + 1].first), y[i].second, y[i + 1].second));
        adj.push_back(Info(abs(z[i].first - z[i + 1].first), z[i].second, z[i + 1].second));
    }

    sort(adj.begin(), adj.end(), comp);
    ll ans = 0;
    for(int i = 0; i < adj.size(); i++){
        int a = adj[i].y, b = adj[i].z;
        int pa = find_p(a), pb = find_p(b);
        if(pa == pb) continue;
        union_p(a, b);
        ans += adj[i].x;
    }
    cout << ans;
    return 0;
}