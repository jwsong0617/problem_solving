from collections import deque
from sys import stdin
def rl():
    return list(stdin.readline().strip().split(' '))
N = int(input())
dq = deque()
for i in range(N):
    cmd = rl()
    if len(cmd) == 2:
        dq.append(int(cmd[1]))
    else:
        cmd = cmd[0]
        if cmd == 'pop':
            if len(dq) == 0:
                print('-1')
            else:
                print(dq.popleft())
        elif cmd == 'size':
            print(len(dq))
        elif cmd == 'empty':
            if len(dq) == 0:
                print('1')
            else:
                print('0')
        elif cmd == 'front':
            if len(dq) == 0:
                print('-1')
            else:
                print(dq[0])
        elif cmd == 'back':
            if len(dq) == 0:
                print('-1')
            else:
                print(dq[-1])