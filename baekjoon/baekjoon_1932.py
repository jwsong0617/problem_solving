from sys import stdin
def rl():
    return map(int, stdin.readline().strip().split(' '))
N = int(input())
arr = [None]*N
cum = [None]*N
for i in range(N):
    arr[i] = list(rl())
cum[0] = arr[0]
for i in range(1, N):
    temp = [None]*(i+1)
    temp[0] = cum[i-1][0]+arr[i][0]
    for j in range(1, i):
        temp[j] = max(cum[i-1][j-1], cum[i-1][j]) + arr[i][j]
    temp[-1] = cum[i-1][-1]+arr[i][-1]
    cum[i] = temp
print(max(cum[-1]))