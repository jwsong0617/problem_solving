import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0]*M
def f(arr, k):
    if(k==M):
        a = list(map(str, arr))
        b = ' '.join(a)
        print(b)
        return
    for i in range(0, N):
        arr[k] = i+1
        f(arr, k+1)
f(arr, 0)