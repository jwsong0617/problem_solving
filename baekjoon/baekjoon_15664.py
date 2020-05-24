import sys
N, M = map(int,sys.stdin.readline().rstrip().split())
candidates = list(map(int,sys.stdin.readline().rstrip().split()))
candidates.sort()
arr = [0]*M
used = [0]*N
printed = set()
def f(arr, used, k):
    if(k==M):
        answer = list(map(str, arr))
        if(' '.join(answer) not in printed):
            print(' '.join(answer))
            printed.add(' '.join(answer))
        else:
            pass
        return
    for i in range(len(candidates)):
        if(used[i] == 0):
            if(k>0):
                if(arr[k-1] > candidates[i]):
                    continue
            arr[k] = candidates[i]
            used[i] = 1
            f(arr, used, k+1)
            used[i] = 0
f(arr, used, 0)