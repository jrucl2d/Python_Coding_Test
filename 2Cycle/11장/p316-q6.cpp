#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
priority_queue<pii> pq;

int solution(vector<int> food_times, ll k) {
    ll first_sum = 0;
    for(int i = 0 ; i < food_times.size(); i++){
        first_sum += food_times[i];
        pq.push({-food_times[i], i + 1});
    }
    if(first_sum <= k){
        return -1;
    }
    ll food_cnt = food_times.size();
    ll before = 0;
    ll the_sum = 0;
    while(true){
        int now_time = -pq.top().first;
        if(the_sum + (now_time - before) * food_cnt <= k){
            the_sum += (now_time - before) * food_cnt;
            pq.pop();
            food_cnt -= 1;
            before = now_time;
        } else {
            vector<ll> tmp;
            while(!pq.empty()){
                tmp.push_back(pq.top().second);
                pq.pop();
            }
            sort(tmp.begin(), tmp.end());
            return tmp[(k - the_sum) % food_cnt];
        }
    }
}