from sys import stdin
from math import ceil


def rl():
    a, b = map(int, stdin.readline().strip().split(' '))
    return a, b


N, K = rl()
rooms = [[0]*6 for _ in range(2)]
for i in range(N):
    s, y  = rl()
    rooms[s][y-1] += 1
print(sum([sum([ceil(e/K) for e in room]) for room in rooms]))