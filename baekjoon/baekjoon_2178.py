import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
board = [[None]*M for _ in range(N)]
dists = [[-1]*M for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().rstrip()))
directions = [(1,0), (0,1), (-1,0), (0,-1)]
Q = deque()
def bfs(i, j, dist):
    Q.append((i, j, dist))
    dists[i][j] = dist
    while(len(Q) != 0):
        cur = Q.popleft()
        for d in directions:
            nx = cur[0]+d[0]
            ny = cur[1]+d[1]
            if(nx<0 or nx>=N or ny<0 or ny>=M):
                continue
            if(dists[nx][ny]!=-1 or (board[nx][ny]==0)):
                continue
            dists[nx][ny] = cur[2]+1
            Q.append((nx, ny, cur[2]+1))
bfs(0, 0, 1)
print(dists[N-1][M-1])