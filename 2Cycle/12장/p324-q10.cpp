#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> before_task(int n, int m, vector<vector<int>> lock){
    int nn = n + 2 * m - 2;
    vector<vector<int>> nlock;
    vector<int> tmp;
    for(int i = 0 ; i < nn; i++){
        tmp.push_back(0);
    }
    nlock.push_back(tmp);
    for(int i = 0 ; i < nn; i++){
        nlock.push_back(tmp);
    }
    for(int i = 0 ; i < n; i++){
        for(int j = 0 ; j < n; j++){
            nlock[i + m - 1][j + m - 1] = lock[i][j];
        }
    }
    
    return nlock;
}
vector<vector<int>> rotate(int m, vector<vector<int>> k){
    vector<vector<int>> ret;
    vector<int> tmp;
    for(int i = 0;i < m; i++){
        tmp.push_back(0);
    }
    for(int i = 0; i < m ; i++){
        ret.push_back(tmp);
    }
    for(int r = 0; r < m ; r++){
        for(int c = 0; c < m; c++){
            ret[c][m - 1 - r] = k[r][c];
        }
    }
    return ret;
}
bool check(vector<vector<int>> lock, int n, int m) {
    for(int i = m - 1; i < m - 1 + n; i++){
        for(int j = m - 1; j < m - 1 + n; j++){
            if(lock[i][j] != 1){
                return false;
            }
        }
    }
    return true;
}
vector<vector<int>> deep_copy(vector<vector<int>> l){
    vector<vector<int>> tmp;
    for(int i = 0 ; i < l.size(); i++){
        vector<int> itmp;
        for(int j = 0 ; j < l.size(); j++){
            itmp.push_back(l[i][j]);
        }
        tmp.push_back(itmp);
    }
    return tmp;
}
bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    int n = lock.size(), m = key.size();
    lock = before_task(n, m, lock);
    int nn = n + 2 * m - 2;

    for(int r = 0 ; r < 4; r++){
        for(int si = 0; si < nn - m + 1; si++){
            for(int sj = 0 ; sj < nn - m + 1; sj++){
                vector<vector<int>> nlock = deep_copy(lock);
                for(int i = si; i < si + m; i++){
                    for(int j = sj; j < sj + m; j++){
                        nlock[i][j] += key[i - si][j - sj];
                    }
                }

                if(check(nlock, n, m)){
                    return true;
                }
            }
        }
        key = rotate(m, key);
    }
    return false;
}