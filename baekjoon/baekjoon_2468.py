from sys import stdin
from collections import deque
N = int(input())
board = [0]*N
min_h = 101
max_h = 0
for i in range(N):
    board[i] = list(map(int, stdin.readline().strip().split(' ')))
    max_h = max(max_h, max(board[i]))
    min_h = min(min_h, min(board[i]))
dirs = ((0,1),(1,0),(0,-1),(-1,0))
result = 1
drown = [[0]*N for _ in range(N)]
for drown_h in range(min_h, max_h):
    area = 0
    q = deque()
    visited = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 1 or drown[y][x] == 1:
                continue
            if board[y][x] <= drown_h:
                drown[y][x] = 1
                continue
            q.appendleft((y,x))
            visited[y][x] = 1
            while len(q) != 0:
                sy, sx = q.popleft()
                for dy, dx in dirs:
                    ny = sy + dy
                    nx = sx + dx
                    if nx >= N or ny >= N or nx < 0 or ny < 0:
                        continue
                    if visited[ny][nx] == 1 or drown[ny][nx] == 1:
                        continue
                    if board[ny][nx] <= drown_h:
                        drown[ny][nx] = 1
                        continue
                    q.appendleft((ny,nx))
                    visited[ny][nx] = 1
            area += 1
    result = max(result, area)
print(result)