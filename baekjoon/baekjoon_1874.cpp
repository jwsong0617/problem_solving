#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<int> s;
    queue<int> q;
    queue<string> ops;
    int N;
    int num;
    int pop_count=0;
    cin >> N;
    for (int i=0;i<N;i++){
        cin >> num;
        q.push(num);
    }
    for (int i=1;i<2*N+1;i++){
        if(!s.empty()) {
            if(s.top()==q.front()){
                q.pop();
                s.pop();
                pop_count++;
                ops.push("-");
            } else if(q.front() < i-pop_count){
                cout << "NO";
                return 0;
            } else{
                s.push(i-pop_count);
                ops.push("+");
            }
        } else {
            if(q.empty()){
                break;
            } else {
                s.push(i-pop_count);
                ops.push("+");
            }
        }
    }
    for (int i=0; i<2*N; i++) {
        if(ops.empty()){
            return 0;
        } else {
            cout << ops.front() << "\n";
            ops.pop();
        }
    }
}