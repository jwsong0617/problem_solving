import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
board = [[None]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
directions = [(1,0), (0,1), (-1,0), (0,-1)]
for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().rstrip().split()))
Q = deque()
areas = []
def bfs(i, j):
    if(board[i][j]==0 or visited[i][j]==1):
        pass
    else:
        area = 1
        Q.append((i,j))
        visited[i][j] = 1
        while(len(Q) != 0):
            cur = Q.popleft()
            for d in directions:
                nx = cur[0] + d[0]
                ny = cur[1] + d[1]
                if(nx<0 or nx>=N or ny<0 or ny>=M):
                    continue
                if(board[nx][ny] == 0 or (visited[nx][ny]==1)):
                    continue
                visited[nx][ny] = 1
                Q.append((nx,ny))
                area += 1
        if(area != 0):
            areas.append(area)
for i in range(N):
    for j in range(M):
        bfs(i, j)
print(len(areas))
if(len(areas)==0):
    print(0)
else:
    print(max(areas))