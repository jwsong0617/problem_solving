import sys
N, M = map(int,sys.stdin.readline().rstrip().split())
candidates = list(map(int,sys.stdin.readline().rstrip().split()))
candidates.sort()
arr = [0]*M
printed = set()
def f(arr, k):
    if(k==M):
        answer = list(map(str, arr))
        if(' '.join(answer) not in printed):
            print(' '.join(answer))
            printed.add(' '.join(answer))
        else:
            pass
        return
    for i in range(len(candidates)):
        if(k>0):
            if(arr[k-1] > candidates[i]):
                continue
        arr[k] = candidates[i]
        f(arr, k+1)
f(arr, 0)