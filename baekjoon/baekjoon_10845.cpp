#include <bits/stdc++.h>

using namespace std;
int main(void) {
    ios::sync_with_stdio;
    cin.tie(0);
    int N;
    string command;
    queue<int> Q;
    int X;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> command;
        if (command == "push") {
            cin >> X;
            Q.push(X);
        } else if (command == "pop") {
            if (Q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << Q.front() << "\n";
                Q.pop();
            }
        } else if (command == "size") {
            cout << Q.size() << "\n";
        } else if (command == "empty") {
            if (Q.empty()) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        } else if (command == "front") {
            if (Q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << Q.front() << "\n";
            }
        } else if (command == "back") {
            if (Q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << Q.back() << "\n";
            }
        }
    }
}