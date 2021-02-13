#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

class Info {
   public:
    string name;
    int kor;
    int eng;
    int math;
    Info(){};
    Info(string a, int b, int c, int d) {
        name = a;
        kor = b;
        eng = c;
        math = d;
    }
};

int n;
Info info[100010];

bool comp(Info a, Info b) {
    if (a.kor == b.kor) {
        if (a.eng == b.eng) {
            if (a.math == b.math) {
                return a.name < b.name;
            }
            return a.math > b.math;
        }
        return a.eng < b.eng;
    }
    return a.kor > b.kor;
}

int main() {
    ios::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    string t1;
    int t2, t3, t4;
    for (int i = 0; i < n; i++) {
        cin >> t1 >> t2 >> t3 >> t4;
        info[i] = Info(t1, t2, t3, t4);
    }
    sort(info, info + n, comp);
    for (int i = 0; i < n; i++) {
        cout << info[i].name << "\n";
    }
    return 0;
}