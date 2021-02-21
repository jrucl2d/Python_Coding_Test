#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int t, n, m, arr[510];
vector<int> indegree[510];
int ind_cnt[510];
priority_queue<int> pq;

void remove_b_from_a(int a, int b){
    for(int j = 0; j < indegree[a].size(); j++){
        if(indegree[a][j] == b){
            indegree[a][j] = -1;
            ind_cnt[a] -= 1;
            return;
        }
    }
}
void print() {
    for(int i = 1; i <= n; i++){
        cout << i << "일 때"<<endl;
        for(int j = 0; j < indegree[i].size(); j++){
            cout << indegree[i][j] <<" ";
        }
        cout << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> t;
    while(t--){
        cin >> n;
        for(int i = 1; i <= n; i++){
            indegree[i].clear();
        }
        for(int i = 1; i <= n; i++){
            cin >> arr[i];
            ind_cnt[i] = 0;
        }
        for(int i = 1; i <= n; i++){
            for(int j = i + 1; j <= n; j++){
                indegree[arr[j]].push_back(arr[i]);
                ind_cnt[arr[j]] += 1;
            }
        }
        cin >> m;
        int a, b;
        for(int i = 0; i < m; i++){
            cin >> a >> b;
            // if a has b
            bool a_has_b = false;
            for(int j = 0; j < indegree[a].size(); j++){
                if(indegree[a][j] == b){
                    a_has_b = true;
                    indegree[a][j] = -1;
                    indegree[b].push_back(a);
                    ind_cnt[a] -= 1;
                    ind_cnt[b] += 1;
                    break;
                }
            }
            if(a_has_b) continue;
            remove_b_from_a(b, a);
            indegree[a].push_back(b);
            ind_cnt[a] += 1;
        }
        int tmp_cnt = 0;
        for(int i = 1; i <= n; i++){
            if(ind_cnt[i] == n - 1){
                pq.push(i);
                tmp_cnt += 1;
            }
        }
        if(tmp_cnt > 1){
            cout << "?\n";
            continue;
        }
        vector<int> ans;
        bool question_mark = false;
        while(!pq.empty()){
            int now = pq.top(); pq.pop();
            ans.push_back(now);
            int inner_tmp_cnt = 0;
            for(int i = 0; i < indegree[now].size(); i++){
                int next = indegree[now][i];
                indegree[next].push_back(now);
                ind_cnt[next] += 1;
                if(ind_cnt[next] == n - 1){
                    pq.push(next);
                    inner_tmp_cnt += 1;
                }
            }
            if(inner_tmp_cnt > 1){
                cout << "?\n";
                question_mark = true;
                break;
            }
        }
        if(question_mark) continue;
        if(ans.size() != n) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        for(int i = ans.size() - 1; i >= 0; i--){
            cout << ans[i] <<" ";
        }
        cout << "\n";
    }
    return 0;
}