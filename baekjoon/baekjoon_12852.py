N = int(input())
arr = [None]*(N+1)
pre = [None]*(N+1)
arr[1], pre[1] = 0, 1
for i in range(2, N+1):
    arr[i] = arr[i-1]+1
    pre[i] = i-1
    if i%2 == 0 and arr[i] > arr[i//2]+1:
        arr[i] = arr[i//2] + 1
        pre[i] = i//2
    if i%3 == 0 and arr[i] > arr[i//3]+1:
        arr[i] = arr[i//3] + 1
        pre[i] = i//3
print(arr[N])
cur = N
while(True):
    print(cur, end=' ')
    if cur == 1:
        break
    cur = pre[cur]