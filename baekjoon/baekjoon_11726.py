N = int(input())
D = [-1]*N
if(N==1):
    print(1%10007)
else:
    D[0] = 1
    D[1] = 2
    for i in range(2,N):
        D[i] = D[i-1]+D[i-2]
    print(D[N-1]%10007)