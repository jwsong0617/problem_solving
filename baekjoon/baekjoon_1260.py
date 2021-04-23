import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().strip().split())
edges = {}
for i in range(M):
    s, e = map(int, sys.stdin.readline().strip().split())
    if edges.get(s):
        edges[s].append(e)
    else:
        edges[s] = [e]
    if edges.get(e):
        edges[e].append(s)
    else:
        edges[e] = [s]


def bfs(start_point):
    queue = deque()
    visited = [0] * (N + 1)
    answer = []
    queue.append(start_point)
    while len(queue) != 0:
        cur_point = queue.popleft()
        if visited[cur_point] == 1:
            continue
        else:
            answer.append(str(cur_point))
            visited[cur_point] = 1
            dests = edges.get(cur_point)
            if dests:
                dests.sort()
                for dest in dests:
                    queue.append(dest)
            else:
                continue
    print(' '.join(answer))


def dfs(start_point):
    queue = deque()
    visited = [0] * (N + 1)
    answer = []
    queue.append(start_point)
    while len(queue) != 0:
        cur_point = queue.popleft()
        if visited[cur_point] == 1:
            continue
        else:
            answer.append(str(cur_point))
            visited[cur_point] = 1
            dests = edges.get(cur_point)
            if dests:
                dests.sort(reverse=True)
                for dest in dests:
                    queue.appendleft(dest)
            else:
                continue
    print(' '.join(answer))


dfs(V)
bfs(V)
