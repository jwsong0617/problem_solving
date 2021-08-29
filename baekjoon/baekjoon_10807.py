from collections import Counter
from sys import stdin


N = int(input())
c = Counter(list(map(int, stdin.readline().strip().split(' '))))
v = int(input())
print(c[v])