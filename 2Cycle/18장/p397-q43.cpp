#include <algorithm>
#include <iostream>
using namespace std;

class Info {
   public:
    int cost, x, y;
    Info(){};
    Info(int a, int b, int c) {
        cost = a;
        x = b;
        y = c;
    }
};

int n, m, parent[200010];
Info info[200010];

bool comp(Info a, Info b) {
    return a.cost < b.cost;
}

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
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for (int i = 1; i < n; i++) {
        parent[i] = i;
    }
    int t1, t2, t3, outer_sum = 0;
    for (int i = 0; i < m; i++) {
        cin >> t1 >> t2 >> t3;
        outer_sum += t3;
        info[i] = Info(t3, t1, t2);
    }
    sort(info, info + n, comp);
    int inner_sum = 0;
    for (int i = 0; i < m; i++) {
        int xp = find_p(info[i].x);
        int yp = find_p(info[i].y);

        // cycle
        if (xp == yp) continue;
        union_p(info[i].x, info[i].y);
        inner_sum += info[i].cost;
    }
    cout << outer_sum - inner_sum;
    return 0;
}