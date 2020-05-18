import sys
from collections import deque
N = int(input())
board = [[0]*N for _ in range(N)]
A = deque()
for i in range(N):
    board[i] = list(map(str, sys.stdin.readline().rstrip()))
def f(K, x, y):
    if K == 1:
        A.append(board[x][y])
        return
    check_all = []            
    for k in range(x, x+K):
        for l in range(y, y+K):
            check_all.append(board[k][l])
    if(all(t == '0' for t in check_all) and len(check_all) > 1):
        A.append('0')
        return
    elif(all(t == '1' for t in check_all) and len(check_all) > 1):
        A.append('1')
        return
    if(K > 1):
        A.append('(')
    div = K//2
    for i in range(2):
        for j in range(2):
            check_part = []
            for k in range(x+(div*i), x+(div*(i+1))):
                for l in range(y+(div*j), y+(div*(j+1))):
                    check_part.append(board[k][l])
            if(all(t == '0' for t in check_part) and len(check_part) > 1):
                A.append('0')
                continue
            elif(all(t == '1' for t in check_part) and len(check_part) > 1):
                A.append('1')
                continue
            else:
                f(div, x+(div*i), y+(div*j))
    A.append(')')
f(N, 0, 0)
print(''.join(A))