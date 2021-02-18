#include <iostream>

using namespace std;

int n;
bool ugly[10000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    ugly[1] = true;
    for(int i = 1; i <= 1000; i++){
        if(ugly[i]){
            ugly[i * 2] = true;
            ugly[i * 3] = true;
            ugly[i * 5] = true;
        }
    }
    int cnt = 0;
    int i = 1;
    for(; i <= 1000; i++){
        if(ugly[i]){
            cnt += 1;
            if(cnt == n) break;
        }
    }
    cout << i;
    return 0;
}