#include <algorithm>
#include <iostream>
using namespace std;

int n, m, arr[1000010], first_max = -11, ans = -1;

int get_sum(int cut) {
    int ret = 0;
    for (int i = 0; i < n; i++) {
        ret += arr[i] - cut > 0 ? arr[i] - cut : 0;
    }
    return ret;
}

void b_search(int left, int right, int val) {
    if (left <= right) {
        int mid = (left + right) / 2;
        int the_sum = get_sum(mid);
        if (the_sum >= val) {
            ans = max(ans, mid);
            b_search(mid + 1, right, val);
        } else {
            b_search(left, mid - 1, val);
        }
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        first_max = max(first_max, arr[i]);
    }
    sort(arr, arr + n);
    b_search(0, first_max, m);
    cout << ans;

    return 0;
}