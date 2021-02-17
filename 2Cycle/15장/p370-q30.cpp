#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    vector<vector<string> > nwords(10001);
    vector<vector<string> > nrwords(10001);
    for (int i = 0; i < words.size(); i++) {
        nwords[words[i].size()].push_back(words[i]);
        string tmp = words[i];

        reverse(tmp.begin(), tmp.end());
        nrwords[words[i].size()].push_back(tmp);
    }
    for (int i = 0; i < 10001; i++) {
        sort(nwords[i].begin(), nwords[i].end());
        sort(nrwords[i].begin(), nrwords[i].end());
    }
    for (int i = 0; i < queries.size(); i++) {
        string now = queries[i];
        string now2 = now;
        int start, end;
        if (now[0] == '?') {
            replace(now.begin(), now.end(), '?', 'a');
            replace(now2.begin(), now2.end(), '?', 'z');
            reverse(now.begin(), now.end());
            reverse(now2.begin(), now2.end());
            start = lower_bound(nrwords[now.size()].begin(), nrwords[now.size()].end(), now) - nrwords[now.size()].begin();
            end = upper_bound(nrwords[now2.size()].begin(), nrwords[now2.size()].end(), now2) - nrwords[now2.size()].begin();
        } else {
            replace(now.begin(), now.end(), '?', 'a');
            replace(now2.begin(), now2.end(), '?', 'z');
            start = lower_bound(nwords[now.size()].begin(), nwords[now.size()].end(), now) - nwords[now.size()].begin();
            end = upper_bound(nwords[now2.size()].begin(), nwords[now2.size()].end(), now2) - nwords[now2.size()].begin();
        }
        answer.push_back(end - start);
    }

    return answer;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string w[6] = {"frodo",
                   "front",
                   "frost",
                   "frozen",
                   "frame",
                   "kakao"};
    vector<string> words;
    string q[5] = {
        "fro??",
        "????o",
        "fr???",
        "fro???",
        "pro?"};
    vector<string> querys;
    for (int i = 0; i < 6; i++) {
        words.push_back(w[i]);
    }
    for (int i = 0; i < 5; i++) {
        querys.push_back(q[i]);
    }
    vector<int> the_res = solution(words, querys);
    for (int i = 0; i < the_res.size(); i++) {
        cout << the_res[i] << " ";
    }

    return 0;
}