#include <iostream>

using namespace std;

int n, m, parent[510];

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
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    int tmp;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> tmp;
            if (tmp == 1) {
                union_p(i, j);
            }
        }
    }
    int the_parent = 0;
    for (int i = 0; i < m; i++) {
        cin >> tmp;
        if (i == 0) {
            the_parent = parent[tmp];
        } else {
            if (the_parent != parent[tmp]) {
                cout << "NO";
                return 0;
            }
        }
    }
    cout << "YES";

    return 0;
}