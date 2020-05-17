import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
board = [0]*N
visited = [[0]*N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int,sys.stdin.readline().rstrip()))
Q = deque()
areas = []
directions = ((0,1), (1,0), (0,-1), (-1,0))
def bfs(y, x):
    Q.append((y, x))
    visited[y][x] = 1
    area = 1
    while(len(Q) != 0):
        cur = Q.popleft()
        for d in directions:
            sy = cur[0]+d[0]
            sx = cur[1]+d[1]
            if(sy<0 or sx<0 or sy>=N or sx>=N):
                continue
            if(visited[sy][sx]==1 or board[sy][sx]==0):
                continue
            Q.append((sy,sx))
            visited[sy][sx] = 1
            area+=1
    areas.append(area)
for i in range(N):
    for j in range(N):
        if(board[i][j] == 1 and visited[i][j] == 0):
            bfs(i, j)
print(len(areas))
for i in sorted(areas):
    print(i)