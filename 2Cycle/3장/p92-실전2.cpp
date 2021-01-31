#include <algorithm>
#include <iostream>

using namespace std;

int n, m, k, arr[1010];
bool comp(int a, int b) {
    return a > b;
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n, comp);
    int ans = 0;

    // Greedy 풀이
    // for (int i = 1; i <= m; i++) {
    //     if (i % (k + 1) == 0) {
    //         ans += arr[1];
    //     } else {
    //         ans += arr[0];
    //     }
    // }

    // 수학적 접근 방식
    int group_cnt = m / (k + 1);
    int rest_cnt = m - (group_cnt * (k + 1));
    ans = group_cnt * (k * arr[0] + arr[1]) + rest_cnt * arr[0];

    cout << ans;
    return 0;
}