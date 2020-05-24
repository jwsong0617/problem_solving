import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
candidates = list(map(int, sys.stdin.readline().rstrip().split()))
candidates.sort()
arr = [0]*M
def f(arr, k):
    if(k==M):
        answer = list(map(str, arr))
        print(' '.join(answer))
        return
    for i in range(len(candidates)):
        arr[k] = candidates[i]
        f(arr, k+1)
f(arr, 0)