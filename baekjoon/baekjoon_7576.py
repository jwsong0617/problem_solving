import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split()) # M: col num(x), N: row num(y)
board = [0] * N
dist = [[-1]*M for _ in range(N)]
for y in range(N):
    board[y] = list(map(int, sys.stdin.readline().rstrip().split()))
Q = deque()
dirs = ((1,0), (0,1), (-1,0), (0,-1))

def check_done(lst):
    for ls in lst:
        if 0 in ls:
            return False
    return True

def bfs():
    while(len(Q) != 0):
        cur = Q.popleft()
        for d in dirs:
            sy = cur[0]+d[0]
            sx = cur[1]+d[1]
            if(sy <0 or sy >= N or sx <0 or sx >=M):
                continue
            if(board[sy][sx] == -1):
                continue
            if(dist[sy][sx] != -1):
                continue
            Q.append((sy, sx))
            dist[sy][sx] = dist[cur[0]][cur[1]]+1
            board[sy][sx] = 1
    if(check_done(board)):
        return max(map(max, *dist))
    else:
        return -1
    return 0
for y in range(N):
    for x in range(M):
        if((board[y][x] == -1) or (board[y][x] == 0)):
            continue
        Q.append((y,x))
        dist[y][x] = 0
result = bfs()
print(result)