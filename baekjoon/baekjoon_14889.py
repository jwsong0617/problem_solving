# SOL 1
import sys
from itertools import permutations, combinations

N = int(sys.stdin.readline().strip())
tables = [0]*N
members = list(range(N))
synergies_set = set()
synergies_dict = {}
diffs = []
for i in range(N):
    tables[i] = list(map(int, sys.stdin.readline().strip().split()))
combs = list(combinations(members, N//2))
for comb in combs:
    start_members = comb
    link_members = list(set(members) - set(comb))
    start_synergies = list(permutations(start_members, 2))
    start_synergy = 0
    for s in start_synergies:
        s_tup = (s[0], s[1])
        if s_tup in synergies_set:
            start_synergy += synergies_dict[s_tup]
        else:
            synergies_set.add(s_tup)
            start_synergy += tables[s[0]][s[1]]
            synergies_dict[s_tup] = tables[s[0]][s[1]]
    link_synergies = list(permutations(link_members, 2))
    link_synergy = 0
    for l in link_synergies:
        l_tup = (l[0], l[1])
        if l_tup in synergies_set:
            link_synergy += synergies_dict[l_tup]
        else:
            synergies_set.add(l_tup)
            link_synergy += tables[l[0]][l[1]]
            synergies_dict[l_tup] = tables[l[0]][l[1]]
    diffs.append(abs(start_synergy - link_synergy))
print(min(diffs))

# SOL 2 - DFS(https://chldkato.tistory.com/155)

# import sys
#
#
# def dfs(idx, cnt):
#     global ans
#     if cnt == n // 2:
#         start, link = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if select[i] and select[j]:
#                     start += a[i][j]
#                 elif not select[i] and not select[j]:
#                     link += a[i][j]
#         ans = min(ans, abs(start - link))
#
#     for i in range(idx, n):
#         if select[i]:
#             continue
#         select[i] = 1
#         dfs(i + 1, cnt + 1)
#         select[i] = 0
#
#
# n = int(sys.stdin.readline())
# a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#
# select = [0 for _ in range(n)]
# ans = sys.maxsize
# dfs(0, 0)
# print(ans)