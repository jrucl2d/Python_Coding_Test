#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef pair<double, int> pdi;

bool comp(pdi a, pdi b) {
    if (a.first == b.first) {
        return a.second < b.second;
    }
    return a.first > b.first;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pdi> tmp;
    int num = stages.size();
    int count[510] = {
        0,
    };
    for (int i = 0; i < num; i++) {
        count[stages[i]] += 1;
    }
    int cnt = num;
    for (int i = 1; i <= N; i++) {
        double first;
        if (count[i] != 0)
            first = double(count[i]) / cnt;
        else
            first = 0;
        tmp.push_back({first, i});
        cnt -= count[i];
    }
    sort(tmp.begin(), tmp.end(), comp);
    for (int i = 0; i < tmp.size(); i++) {
        answer.push_back(tmp[i].second);
    }
    return answer;
}