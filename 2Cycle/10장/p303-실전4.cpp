#include <iostream>
#include <queue>
#include <vector>

using namespace std;
int n, time[510], indegree[510];
vector<int> pre[510];

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        int the_time;
        cin >> the_time;
        time[i] = the_time;
        int tmp;
        while (true) {
            cin >> tmp;
            if (tmp == -1) break;
            pre[tmp].push_back(i);
            indegree[i] += 1;
        }
    }

    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    int res_time[510];
    for (int i = 1; i <= n; i++) {
        res_time[i] = time[i];
    }
    while (!q.empty()) {
        int now = q.front();
        q.pop();

        for (int i = 0; i < pre[now].size(); i++) {
            int next = pre[now][i];
            indegree[next] -= 1;
            if (indegree[next] == 0) {
                q.push(next);
            }
            res_time[next] = max(res_time[next], res_time[now] + time[next]);
        }
    }
    for (int i = 1; i <= n; i++) {
        cout << res_time[i] << "\n";
    }

    return 0;
}