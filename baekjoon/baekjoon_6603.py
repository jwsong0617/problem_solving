from sys import stdin
# # method 1 - using combination function
# from itertools import combinations
# while(True):
#     t = list(map(int, stdin.readline().strip().split(' ')))
#     n = t[0]
#     t = t[1:]
#     if n == 0:
#         break
#     combs = combinations(t, 6)
#     for c in combs:
#         c = map(str, c)
#         print(' '.join(c))
#     print()

# method 2 - using backtracking
def lotto(x, cnt):
    global n
    global t
    if cnt == 6:
        for i in range(n):
            if select[i]:
                print(t[i], end=' ')
        print()
        return

    for i in range(x, n):
        select[i] = 1
        lotto(i+1, cnt+1)
        select[i] = 0

while(True):
    t = list(map(int, stdin.readline().strip().split(' ')))
    n = t[0]
    if n == 0:
        break
    t = t[1:]
    select = [0 for _ in range(n)]
    lotto(0, 0)
    print()