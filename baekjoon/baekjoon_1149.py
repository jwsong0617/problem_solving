import sys
N = int(input())
S = [-1]*N
for i in range(N):
    S[i] = list(map(int, sys.stdin.readline().rstrip().split()))
D = [[0]*3 for _ in range(N)]
D[0] = S[0]
for i in range(1, N):
    D[i][0] = min(D[i-1][1], D[i-1][2])+S[i][0]
    D[i][1] = min(D[i-1][0], D[i-1][2])+S[i][1]
    D[i][2] = min(D[i-1][0], D[i-1][1])+S[i][2]
print(min(D[N-1]))
