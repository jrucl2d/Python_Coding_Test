#include <iostream>

using namespace std;
int n, arr[1000010];

int b_find(int a, int b) {
    if (a <= b) {
        int mid = (a + b) / 2;
        if (arr[mid] == mid) {
            return mid;
        } else if (arr[mid] < mid) {
            return b_find(mid + 1, b);
        } else {
            return b_find(a, mid - 1);
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int cnt = 0;
    int ans = b_find(0, n - 1);
    if (ans != -1) {
        cout << ans << " ";
    } else {
        cout << -1;
    }

    return 0;
}