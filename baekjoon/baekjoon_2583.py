import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().rstrip().split())
board = [[0]*N for _ in range(M)] # M: row num, N: col num, board[M][N]
visited = [[0]*N for _ in range(M)]
directions = ((1,0), (0,1), (-1,0), (0, -1))
areas = []
Q = deque()
for _ in range(K):
    x0, y0, x1, y1 = map(int, sys.stdin.readline().rstrip().split())
    for y in range(y0, y1):
        for x in range(x0, x1):
            board[y][x] = -1
def bfs(i, j): # y,x
    if(board[i][j]==-1 or visited[i][j]==1):
        pass
    else:
        area = 1
        Q.append((i,j))
        visited[i][j] = 1
        while(len(Q)!=0):
            cur = Q.popleft()
            for d in directions:
                y = cur[0]+d[0]
                x = cur[1]+d[1]
                if(x<0 or y<0 or x>=N or y>=M):
                    continue
                if(board[y][x]==-1 or visited[y][x]==1):
                    continue
                Q.append((y,x))
                visited[y][x] = 1
                area+=1
        if(area != 0):
            areas.append(area)
for i in range(M):
    for j in range(N):
        bfs(i, j)
print(len(areas))
for area in sorted(areas):
    print(area, end=' ')