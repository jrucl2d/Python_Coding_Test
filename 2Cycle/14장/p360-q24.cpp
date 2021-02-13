#include <algorithm>
#include <iostream>

using namespace std;

int n, arr[200010];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    if (n % 2 == 0) {
        cout << arr[n / 2 - 1];
    } else {
        cout << arr[n / 2];
    }

    return 0;
}