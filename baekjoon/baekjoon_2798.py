import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))
combs = list(combinations(cards, 3))
for i, comb in enumerate(combs):
    s = sum(comb)
    s = M - s
    combs[i] = s
minimum = M
for i, comb in enumerate(combs):
    if comb < 0:
        continue
    else:
        if comb < minimum:
            minimum = comb
print(M-minimum)
