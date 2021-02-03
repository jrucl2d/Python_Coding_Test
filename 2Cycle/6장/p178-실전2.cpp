#include <algorithm>
#include <iostream>
using namespace std;
int n, arr[510];

bool comp(int a, int b) {
    return a > b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n, comp);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}