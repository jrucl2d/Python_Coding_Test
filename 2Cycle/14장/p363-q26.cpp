#include <iostream>
#include <queue>
using namespace std;

int n;
priority_queue<int> q;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    int tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        q.push(-tmp);
    }
    int ans = 0;
    while (true) {
        int first = -q.top();
        q.pop();
        if (q.empty()) {
            cout << ans;
            break;
        }
        int second = -q.top();
        q.pop();
        int the_sum = first + second;
        ans += the_sum;
        q.push(-the_sum);
    }
    return 0;
}