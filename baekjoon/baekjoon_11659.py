import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cum_sum = [0]*(len(arr)+1)
cum_sum[1] = arr[0]
for i in range(2, len(arr)+1):
    cum_sum[i] = cum_sum[i-1]+arr[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(cum_sum[j] - cum_sum[i-1])
