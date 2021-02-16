#include <algorithm>
#include <iostream>

using namespace std;
int n, c, arr[200010];

int check_cnt(int num) {
    int s = arr[0];
    int cnt = 1;
    for (int i = 1; i < n; i++) {
        if (arr[i] >= s + num) {
            s = arr[i];
            cnt += 1;
        }
    }
    return cnt;
}

int sol() {
    int l = 1;
    int r = arr[n - 1] - arr[0];
    int mid;
    int ans;
    while (l <= r) {
        mid = (l + r) / 2;
        int the_cnt = check_cnt(mid);
        if (the_cnt < c) {
            r = mid - 1;
        } else {
            ans = mid;
            l = mid + 1;
        }
    }
    return ans;
}

int main() {
    cin >> n >> c;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    cout << sol();

    return 0;
}