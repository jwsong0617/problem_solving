import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0]*M
def f(arr, k):
    if(k==M):
        a = [a+1 for a in arr]
        a = list(map(str, a))
        b = ' '.join(a)
        print(b)
        return
    st = 0
    if(k!=0):
        st = arr[k-1]
    for i in range(st, N):
        arr[k] = i
        f(arr, k+1)
f(arr, 0)