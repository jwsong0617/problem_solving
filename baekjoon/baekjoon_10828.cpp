#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    string op;
    int num;
    stack <int> S;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> op;
        if (op == "push") {
            cin >> num;
            S.push(num);
        }
        else if (op == "pop") {
            if (S.size() == 0) {
                cout << -1 << "\n";
            }
            else {
                cout << S.top() << "\n";
                S.pop();
            }
        }
        else if (op == "size") {
            cout << S.size() << "\n";
        }
        else if (op == "empty") {
            if (S.size() == 0) {
                cout << 1 << "\n";
            }
            else {
                cout << 0 << "\n";
            }
        }
        else if (op == "top") {
            if (S.size() == 0) {
                cout << -1 << "\n";
            }
            else {
                cout << S.top() << "\n";
            }
        }
        
    }
}