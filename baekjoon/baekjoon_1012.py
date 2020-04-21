import sys
from collections import deque

def dfs(y, x):
    worm = 1
    Q.append((y, x))
    visited[y][x] = 1
    while(len(Q)!=0):
        cur = Q.popleft()
        for d in directions:
            nx = cur[1]+d[1]
            ny = cur[0]+d[0]
            if(ny<0 or nx<0 or ny>=N or nx>=M):
                continue
            if(board[ny][nx]==0 or visited[ny][nx]==1):
                continue
            Q.append((ny,nx))
            visited[ny][nx] = 1
            worm+=1
    if(worm!=0):
        worms.append(worm)

T = int(input())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split()) # N: row length(y), M: column length(x)
    board = [[0]*M for _ in range(N)] # board[N][M]
    visited = [[0]*M for _ in range(N)]
    Q = deque()
    worms = []
    directions = ((1,0), (0,1), (-1,0), (0,-1))
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        board[y][x] = 1
    for y in range(N):
        for x in range(M):
            if(board[y][x] != 0 and visited[y][x] == 0):
                dfs(y,x)
    print(len(worms))