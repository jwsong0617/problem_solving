import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
candidates = list(map(int, sys.stdin.readline().rstrip().split()))
candidates.sort()
arr = [0]*M
used = [0]*N
def f(arr, used, k):
    if(k==M):
        answer = list(map(str, arr))
        print(' '.join(answer))
        return
    if(used[k] == 1):
        return
    for i in range(N):
        if(k!=0):
            if(candidates[i] <=  arr[k-1]):
                continue
        arr[k] = candidates[i]
        used[k] = 1
        f(arr, used, k+1)
        used[k] = 0
f(arr, used, 0)
