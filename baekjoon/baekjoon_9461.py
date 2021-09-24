T = int(input())
arr = [None]*101
arr[0:6] = [0,1,1,1,2,2]
for t in range(T):
    N = int(input())
    if arr[N] != None:
        print(arr[N])
    else:
        for i in range(6, N+1):
            if arr[i] != None:
                continue
            else:
                arr[i] = arr[i-1] + arr[i-5]
        print(arr[N])