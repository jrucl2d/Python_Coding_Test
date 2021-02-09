#include <string>
#include <iostream>
#include <vector>
#define INF 1e9

using namespace std;

int get_min(int a, int b){
    return a < b ? a : b;
}

int solution(string s) {
    int answer = INF;
    int s_len = s.size();
    if(s_len == 1){
        return 1;
    }
    for(int unit = 1; unit <= s_len / 2; unit++){
        string done_string = "";
        string comp_string = "";
        int s_cnt = 1;
        for(int i = 0 ; i < unit; i++){
            comp_string += s[i];
        }
        int i = unit;
        for(; i < s_len; i+= unit){
            if(i + unit > s_len){
                break;
            }
            string the_string = "";
            for(int j = i; j < i + unit; j++){
                the_string += s[j];
            }
            //cout << comp_string << " " << the_string <<"\n";
            if(comp_string == the_string){
                s_cnt += 1;
            } else {
                if(s_cnt != 1){
                    string cnt_string = to_string(s_cnt);
                    done_string += cnt_string;
                }
                done_string += comp_string;
                //cout << done_string <<endl;
                comp_string = the_string;
                s_cnt = 1;
            }
        }
        if(s_cnt != 1){
            string cnt_string = to_string(s_cnt);
            done_string += cnt_string;
        }
        done_string += comp_string;
        for(int j = i; j < s_len; j++){
            done_string += s[j];
        }
        answer = get_min(answer, done_string.size());
        //cout << done_string << endl;
    }
    return answer;
}