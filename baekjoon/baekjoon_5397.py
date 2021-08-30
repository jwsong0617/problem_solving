from queue import deque


L = int(input())
for i in range(L):
    left = deque()
    right = deque()
    logs = list(input().strip())
    for log in logs:
        if log == '<':
            if len(left) != 0:
                right.appendleft(left.pop())
        elif log == '>':
            if len(right) != 0:
                left.append(right.popleft())
        elif log == '-':
            if len(left) != 0:
                left.pop()
        else:
            left.append(log)
    print(''.join(left) + ''.join(right))