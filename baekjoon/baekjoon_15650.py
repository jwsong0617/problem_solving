# sol 1
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0]*M
used = [0]*N
def f(arr, used, k):
    if(k == M):
        answer = [a+1 for a in arr]
        answer = list(map(str, answer))
        print(' '.join(answer))
        return
    st = 0
    if(k>0):
        st = arr[k-1]
    for i in range(st, N):
        if(used[i]==0):
            arr[k] = i
            used[i] = 1
            f(arr, used, k+1)
            used[i] = 0
f(arr, used, 0)
# sol 2
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0]*M
used = [0]*N
def f(arr, used, k):
    if(k == M):
        for idx in range(len(arr)-1):
            if(arr[idx] > arr[idx+1]):
                return
        answer = list(map(str, arr))
        print(' '.join(answer))
        return
    for i in range(1, N+1):
        if(used[i-1]==0):
            arr[k] = i
            used[i-1] = 1
            f(arr, used, k+1)
            used[i-1] = 0
f(arr, used, 0)