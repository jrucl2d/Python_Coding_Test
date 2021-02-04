#include <algorithm>
#include <iostream>
using namespace std;

int n, m, arr[1000010];

int b_search(int left, int right, int val) {
    if (left > right) {
        return -1;
    }
    int mid = (left + right) / 2;
    if (arr[mid] == val) {
        return mid;
    } else if (arr[mid] < val) {
        return b_search(mid + 1, right, val);
    } else {
        return b_search(left, mid - 1, val);
    }
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    cin >> m;
    int finding;
    for (int i = 0; i < m; i++) {
        cin >> finding;
        int is_there = b_search(0, n - 1, finding);
        if (is_there != -1)
            cout << "yes ";
        else
            cout << "no ";
    }

    return 0;
}