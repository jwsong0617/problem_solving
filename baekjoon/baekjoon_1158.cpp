// baekjoon_1158
#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, K;
    cin >> N >> K;
    list<int> L;
    vector<int> V;
    for (int i=1; i<=N; i++) {
        L.push_back(i);
    }
    auto cursor = L.begin();
    while (N--) {
        for (int i=0; i<K-1; i++) {
            if (*cursor == L.back()) {
                cursor = L.begin();
            }
            else {
                cursor++;
            }
        }
        V.push_back(*cursor);
        if(*cursor == L.back()) {
            L.erase(cursor);
            cursor = L.begin();
        }
        else {
            cursor = L.erase(cursor);
        }
    }
    cout << "<" << V[0];
    for (int i = 1; i < V.size(); i++) {
        cout << ", " << V[i];
    }
    cout << ">";
}

// 1 2 3 4 5 6 7
// 1 4
// 3 6 2 7 5 1 4