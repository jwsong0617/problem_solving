#include <bits/stdc++.h>
using namespace std;
int main(void){
    queue<int> q;
    int N, num;
    cin >> N;
    for (int i=1; i<=N; i++){
        q.push(i);
    }
    while(!q.empty()){
        if(q.size()==1){
            cout << q.back();
            return 0;
        }
        q.pop();
        q.push(q.front());
        q.pop();
    }
}
