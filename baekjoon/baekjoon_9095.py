# D[N] = D[N-3] + D[N-2] + D[N-1]
T = int(input())
arr = [None]*12
arr[1] = 1
arr[2] = 2
arr[3] = 4
arr[4] = 7
arr[7] = 44
arr[10] = 274
for t in range(T):
    n = int(input())
    if arr[n] != None:
        print(arr[n])
    else:
        for i in range(4, n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        print(arr[n])