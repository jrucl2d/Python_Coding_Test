#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int n, x;
vector<int> arr;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> x;
    int tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        arr.push_back(tmp);
    }
    int first = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
    int second = upper_bound(arr.begin(), arr.end(), x) - arr.begin();
    if (second - first != 0)
        cout << second - first;
    else
        cout << -1;
    return 0;
}