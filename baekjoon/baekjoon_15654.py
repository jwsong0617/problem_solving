import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
candidates = list(map(int, sys.stdin.readline().rstrip().split()))
candidates = sorted(candidates)
arr = [0]*M
used = [0]*N
def f(arr, used, k):
    if(k==M):
        a = list(map(str, arr))
        a = ' '.join(a)
        print(a)
        return
    for idx in range(len(candidates)):
        if(used[idx]==0):
            arr[k] = candidates[idx]
            used[idx] = 1
            f(arr, used, k+1)
            used[idx] = 0
f(arr, used, 0)