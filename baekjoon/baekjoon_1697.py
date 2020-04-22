import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())
MAX = 100001
board = [0] * MAX
visited = [0] * MAX
Q = deque()
board[K] = 1
def bfs(i, t):
    def bfs_lambda(pos, elapsed):
        if(pos >= MAX or pos < 0):
            return False
        if(visited[pos] == 1):
            return False
        if(board[pos]):
            print(elapsed+1)
            return True
        Q.append((pos,elapsed+1))
        visited[pos] = 1
    if(board[i]):
        print(0)
    Q.append((i,t))
    visited[i] = 1
    while(len(Q) != 0):
        cur, t = Q.popleft()
        dir_0 = cur*2
        dir_1 = cur+1
        dir_2 = cur-1
        v_0 = bfs_lambda(dir_0, t)
        if(v_0):
            return
        v_1 = bfs_lambda(dir_1, t)
        if(v_1):
            return
        v_2 = bfs_lambda(dir_2, t)
        if(v_2):
            return
bfs(N, 0)