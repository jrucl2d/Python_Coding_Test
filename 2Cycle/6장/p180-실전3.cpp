#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
typedef pair<string, int> psi;

int n;
psi arr[100010];

bool comp(psi a, psi b) {
    return a.second < b.second;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) {
        string tmp;
        int tmp2;
        cin >> tmp >> tmp2;
        arr[i] = {tmp, tmp2};
    }
    sort(arr, arr + n, comp);
    for (int i = 0; i < n; i++) {
        cout << arr[i].first << " ";
    }
    return 0;
}