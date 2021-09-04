from sys import stdin
from collections import deque
R, C = map(int, stdin.readline().strip().split(' '))
board = [0]*R
f_queue, j_queue = deque(), deque()
f_visited = [[0]*C for _ in range(R)]
j_visited = [[0]*C for _ in range(R)]

for i in range(R):
    board[i] = list(input())
for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            f_queue.append((i, j))
        elif board[i][j] == 'J':
            j_queue.append((i, j))
dirs = ((0,1), (1,0), (0,-1), (-1,0))

while len(f_queue) != 0:
    sr, sc = f_queue.popleft()
    for dr, dc in dirs:
        nr = sr + dr
        nc = sc + dc
        if 0 <= nr < R and 0 <= nc < C:
            if f_visited[nr][nc] == 0 and board[nr][nc] != '#':
                f_visited[nr][nc] = f_visited[sr][sc] + 1
                f_queue.append((nr, nc))

end_flag = False
while len(j_queue) != 0:
    sr, sc = j_queue.popleft()
    for dr, dc in dirs:
        nr = sr + dr
        nc = sc + dc
        if 0 <= nr < R and 0 <= nc < C:            
            if j_visited[nr][nc] == 0 and board[nr][nc] != '#':
                if j_visited[sr][sc] + 1 < f_visited[nr][nc] or f_visited[nr][nc] == 0:
                    j_visited[nr][nc] = j_visited[sr][sc] + 1
                    j_queue.append((nr, nc))
        else:
            print(j_visited[sr][sc]+1)
            end_flag = True
            break
    if end_flag:
        break
if not end_flag:
    print('IMPOSSIBLE')