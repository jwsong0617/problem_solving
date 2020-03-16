#include <bits/stdc++.h>
using namespace std;
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    int num;
    stack<int> s;
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> num;
        if(num==0){
            s.pop();
        }else{
            s.push(num);
        }
    }
    int sum=0;
    while(!s.empty()){
        // cout << s.top() << "\n";
        sum += s.top();
        s.pop();
    }
    cout << sum;
}