#include <algorithm>
#include <iostream>

using namespace std;
int n, arr[100010];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    int ans = 0;
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        cnt += 1;
        if (arr[i] <= cnt) {
            ans += 1;
            cnt = 0;
        }
    }
    cout << ans;

    return 0;
}