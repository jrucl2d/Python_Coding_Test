#include <iostream>
#include <vector>
using namespace std;
#define INF 1e9

int n, nums[110], max_ans = -INF, min_ans = INF;
char ops_char[4] = {'+', '-', '*', '/'};
vector<char> ops;
bool visited[12];

void dfs(int index, vector<char> inner_ops) {
    // 체크인
    visited[index] = true;
    inner_ops.push_back(ops[index]);

    // 종료 조건
    if (inner_ops.size() == n - 1) {
        int inner_sum = nums[0];
        for (int i = 0; i < n - 1; i++) {
            if (inner_ops[i] == '+') {
                inner_sum += nums[i + 1];
            } else if (inner_ops[i] == '-') {
                inner_sum -= nums[i + 1];
            } else if (inner_ops[i] == '*') {
                inner_sum *= nums[i + 1];
            } else {
                inner_sum /= nums[i + 1];
            }
        }
        max_ans = max(max_ans, inner_sum);
        min_ans = min(min_ans, inner_sum);
    }

    // 갈 수 있으면 간다
    for (int i = 0; i < n - 1; i++) {
        if (visited[i] == false) {
            dfs(i, inner_ops);
        }
    }

    // 체크 아웃
    visited[index] = false;
    inner_ops.pop_back();
}
int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    for (int i = 0; i < 4; i++) {
        int tmp;
        cin >> tmp;
        for (int j = 0; j < tmp; j++) {
            ops.push_back(ops_char[i]);
        }
    }
    for (int i = 0; i < n - 1; i++) {
        vector<char> inner_ops;

        dfs(i, inner_ops);
    }
    cout << max_ans << "\n"
         << min_ans;
    return 0;
}