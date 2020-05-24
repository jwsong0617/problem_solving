N = int(input())
used_col = [0]*N
used_diag1 = [0]*2*N
used_diag2 = [0]*2*N
answer = 0
def f(x):
    if(x==N):
        global answer
        answer+=1
        return
    for y in range(N):
        if(used_col[y] == 1 or used_diag1[x+y] == 1 or used_diag2[x-y+N-1] == 1):
            continue
        used_col[y] = 1
        used_diag1[x+y] = 1
        used_diag2[x-y+N-1] = 1
        f(x+1)
        used_col[y] = 0
        used_diag1[x+y] = 0
        used_diag2[x-y+N-1] = 0
f(0)
print(answer)