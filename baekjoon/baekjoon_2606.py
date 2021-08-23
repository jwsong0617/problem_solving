import sys
from collections import deque
N = int(input())
M = int(input())
queue = deque()
connections = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, d = map(int, sys.stdin.readline().strip().split())
    connections[s][d] = 1
    connections[d][s] = 1


def bfs(starting_point):
    got_virus = 0
    visited = [0] * (N+1)
    queue.append(starting_point)
    visited[starting_point] = 1
    while len(queue) != 0:
        dest_pos = []
        dests = connections[queue.popleft()]
        for idx, dest in enumerate(dests):
            if dest == 0:
                continue
            dest_pos.append(idx)
        for pos in dest_pos:
            if visited[pos] == 1:
                continue
            queue.append(pos)
            visited[pos] = 1
            got_virus += 1
    return got_virus


if N == 0 or M == 0:
    print(0)
else:
    print(bfs(1))
