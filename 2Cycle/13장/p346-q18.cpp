#include <string>
#include <vector>

using namespace std;

bool is_balanced(string s) {
    int left = 0, right = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(')
            left += 1;
        else
            right += 1;
    }
    if (left == right) return true;
    return false;
}
bool is_right(string s) {
    vector<char> stack;
    if (s[0] == ')') return false;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            stack.push_back('(');
        } else if (s[i] == ')') {
            if (stack.back() == '(') {
                stack.pop_back();
            } else {
                return false;
            }
        }
    }
    if (stack.size() == 0)
        return true;
    return false;
}

string solution(string p) {
    string answer = "";
    if (is_right(p)) return p;

    if (p == "") return "";
    string u = "", v = "";
    int i = 0;
    for (; i < p.size(); i++) {
        u += p[i];
        if (is_balanced(u)) {
            i += 1;
            break;
        }
    }
    for (; i < p.size(); i++) {
        v += p[i];
    }
    if (is_right(u)) {
        answer += u;
        answer += solution(v);
    } else {
        answer += '(';
        answer += solution(v);
        answer += ')';
        for (int i = 1; i < u.size() - 1; i++) {
            answer += (u[i] == '(' ? ')' : '(');
        }
    }
    return answer;
}