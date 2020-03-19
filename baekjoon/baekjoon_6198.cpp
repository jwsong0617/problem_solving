//monotone stack
#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    int num;
    long long total=0;
    cin >> N;
    stack<int> stk;
    for (int i=0; i<N; i++) {
        cin >> num;
        while(!stk.empty() && stk.top()<=num){
            stk.pop();
        }
        total+=stk.size();
        stk.push(num);
    }
    cout << total;
}