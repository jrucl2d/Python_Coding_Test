#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, arr[1010];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    int target = 1;
    for (int i = 0; i < n; i++) {
        if (target < arr[i]) {
            break;
        }
        target += arr[i];
    }
    cout << target;

    return 0;
}