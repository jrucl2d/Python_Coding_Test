#include <iostream>

using namespace std;

int g, p, arr[100010], parent[100010];

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

    cin >> g >> p;
    for (int i = 1; i <= g; i++) {
        parent[i] = i;
    }
    for (int i = 1; i <= p; i++) {
        cin >> arr[i];
    }

    int ans = 0;
    for (int i = 1; i <= p; i++) {
        int the_p = find_p(arr[i]);
        if (the_p == 0) {
            break;
        }
        union_p(the_p, the_p - 1);
        ans += 1;
    }
    cout << ans;
    return 0;
}