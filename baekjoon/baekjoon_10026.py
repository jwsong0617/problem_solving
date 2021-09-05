# start: 12:45
# end: 13:11
from sys import stdin
from collections import deque
N = int(stdin.readline().strip())
board_rgb = [[0]*N for _ in range(N)]
board_rb = [[0]*N for _ in range(N)]
for i in range(N):
    temp_input = list(stdin.readline().strip())
    for j in range(N):
        element = temp_input[j]
        board_rgb[i][j] = element
        if element == 'G':
            board_rb[i][j] = 'R'
        else:
            board_rb[i][j] = element
dirs = ((1,0), (0,1), (-1, 0), (0, -1))

visited = [[0]*N for _ in range(N)]
area = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] != 0:
            continue
        q = deque()
        q.append((r,c))
        visited[r][c] = 1
        while q:
            sr, sc = q.popleft()
            for dr, dc in dirs:
                nr = sr + dr
                nc = sc + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] == 0 and board_rgb[sr][sc] == board_rgb[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
        area += 1
answers = [str(area)]

visited = [[0]*N for _ in range(N)]
area = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] != 0:
            continue
        q = deque()
        q.append((r,c))
        visited[r][c] = 1
        while q:
            sr, sc = q.popleft()
            for dr, dc in dirs:
                nr = sr + dr
                nc = sc + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] == 0 and board_rb[sr][sc] == board_rb[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
        area += 1
answers.append(str(area))
print(' '.join(answers))