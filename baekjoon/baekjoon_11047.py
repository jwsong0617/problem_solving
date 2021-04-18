import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = [0]*N
for i in range(N):
    coins[i] = int(sys.stdin.readline())
# print(N, K)
# print(coins)

cnt = 0
for idx in range(len(coins)-1, -1, -1):
    if K // coins[idx] == 0:
        continue
    else:
        cnt += K // coins[idx]
        K = K % coins[idx]
print(cnt)
