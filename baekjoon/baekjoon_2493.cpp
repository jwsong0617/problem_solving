#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    int num;
    stack<pair<int, int>> s;
    queue<int> ans;
    cin >> N;
    for (int i=1; i<=N; i++){
        cin >> num;
        int index=0;
        while(!s.empty()){
            if(s.top().second > num){
                // ans.push(s.top().first);
                cout << s.top().first << " ";
                break;
            }
            s.pop();
        }
        if(s.empty()){
            cout << 0 << " ";
            // ans.push(0);
        }
        s.push(make_pair(i, num));
    }
    for (int i=0; i<N; i++){
        cout << ans.back() << " ";
        ans.pop();
    }
}