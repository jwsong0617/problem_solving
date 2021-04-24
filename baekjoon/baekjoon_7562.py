import sys
from collections import deque
N = int(input())
dirs = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
for i in range(N):
    queue = deque()
    l = int(input())
    sx, sy = map(int, sys.stdin.readline().strip().split())  # 출발지
    fx, fy = map(int, sys.stdin.readline().strip().split())  # 최종 목적지
    board = [[0] * l for _ in range(l)]
    queue.append((sx, sy))
    board[sx][sy] = 1
    while len(queue) != 0:
        x, y = queue.popleft()
        if x == fx and y == fy:
            print(board[x][y]-1)
            break
        for d in dirs:
            dx = x + d[0]
            dy = y + d[1]
            if dx >= l or dy >= l or dx < 0 or dy < 0:
                continue
            if board[dx][dy] != 0:
                continue
            queue.append((dx, dy))
            board[dx][dy] = board[x][y] + 1
