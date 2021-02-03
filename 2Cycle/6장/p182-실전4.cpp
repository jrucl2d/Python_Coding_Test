#include <algorithm>
#include <iostream>
using namespace std;
int n, k, A[100010], B[100010];

bool comp(int a, int b) {
    return a > b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    sort(A, A + n);
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    sort(B, B + n, comp);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (k > 0 && A[i] < B[i]) {
            ans += B[i];
            k -= 1;
        } else
            ans += A[i];
    }
    cout << ans;

    return 0;
}