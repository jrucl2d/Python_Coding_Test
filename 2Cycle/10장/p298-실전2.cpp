#include <iostream>

using namespace std;

int n, m, *parent;

int find_p(int a) {
    if (parent[a] != a) {
        parent[a] = find_p(parent[a]);
    }
    return parent[a];
}
void union_p(int a, int b) {
    a = find_p(a);
    b = find_p(b);
    if (a > b) {
        parent[a] = b;
    } else {
        parent[b] = a;
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    parent = new int[n];
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    int t1, t2, t3;
    for (int i = 0; i < m; i++) {
        cin >> t1 >> t2 >> t3;
        if (t1 == 0) {
            union_p(t2, t3);
        } else if (t1 == 1) {
            int a = find_p(t2);
            int b = find_p(t3);
            if (a == b) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        }
    }
    return 0;
}