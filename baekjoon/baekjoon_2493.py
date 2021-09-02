from sys import stdin
N = int(input())
towers = list(map(int, stdin.readline().strip().split(' ')))
stk = [(towers[0], 1)]
answer = ['0']
for idx, t in enumerate(towers[1:]):
    while len(stk) != 0:
        if stk[-1][0] > t:
            answer.append(str(stk[-1][1]))
            break
        else:
            stk.pop()        
    if len(stk) == 0:
       answer.append('0')
    stk.append((t, str(idx+2)))
print(' '.join(answer))