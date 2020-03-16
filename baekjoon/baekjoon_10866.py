import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
q = deque()
for i in range(N):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0]=="push_front":
        q.appendleft(int(commands[1]))
    elif commands[0]=="push_back":
        q.append(int(commands[1]))
    elif commands[0]=="pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif commands[0]=="pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif commands[0]=="size":
        print(len(q))
    elif commands[0]=="empty":
        if q:
            print(0)
        else:
            print(1)
    elif commands[0]=="front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif commands[0]=="back":
        if q:
            print(q[-1])
        else:
            print(-1)