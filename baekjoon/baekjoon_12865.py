import sys
N, K = map(int, sys.stdin.readline().strip().split())
things = [[0,0]]
for i in range(N):
    things.append(list(map(int, sys.stdin.readline().strip().split())))
bags = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = things[i][0]
        value = things[i][1]
        if j < weight:
            bags[i][j] = bags[i - 1][j]
        else:
            bags[i][j] = max(value + bags[i - 1][j - weight], bags[i - 1][j])
print(bags[N][K])