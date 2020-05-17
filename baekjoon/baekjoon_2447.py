N = int(input())
answer = [[' ']*N for _ in range(N)]
def recursion(k, x, y):
    if(k==1):
        answer[x][y] = '*'
        return
    div = k//3
    for i in range(3):
        for j in range(3):
            if(i==1 and j==1):
                pass
            else:
                recursion(div, x+(i*div), y+(j*div))
recursion(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(answer[i][j], end='')
    print()