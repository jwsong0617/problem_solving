from itertools import combinations
import sys
N, S = map(int, sys.stdin.readline().rstrip().split())
candidates = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
for i in range(1, N+1):
    cs = combinations(candidates, i)
    for c in cs:
        if(sum(c) == S):
        # if(sum(c) == S and len(c) != 0):
            # print(c)
            answer+=1
print(answer)