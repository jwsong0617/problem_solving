# from itertools import combinations
from sys import stdin
answer = 0
N = int(input())
cs = list(map(int, stdin.readline().strip().split(' ')))
# with open('temp.txt', 'r') as f:
#     cs = f.read()
# cs = list(map(int, cs.strip().split(' ')))
x = int(input())

# # method 1: unsing combination -> timeout
# cs = filter(lambda e: e < x, cs)
# for p in combinations(cs, 2):
#     if sum(p) == x:
#         answer+=1
# print(answer)

# method 2: sort & two pointer
cs.sort()
l = 0
r = N-1
while l < r:
    tmp = cs[l] + cs[r]
    if tmp > x:
        r -= 1
    elif tmp < x:
        l += 1
    elif tmp == x:
        answer+=1
        l += 1
        r -= 1
print(answer)