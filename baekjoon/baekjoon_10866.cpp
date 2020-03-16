#include <bits/stdc++.h>
using namespace std;
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    string command;
    deque<int> dq;
    int X;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> command;
        if (command == "push_front") {
            cin >> X;
            dq.push_front(X);
        } else if (command == "push_back") {
            cin >> X;
            dq.push_back(X);
        } else if (command == "pop_front") {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        } else if (command == "pop_back") {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        } else if (command == "size") {
            cout << dq.size() << "\n";
        } else if (command == "empty") {
            if (dq.empty()) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        } else if (command == "front") {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.front() << "\n";
            }
        } else if (command == "back") {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.back() << "\n";
            }
        }
    }
}