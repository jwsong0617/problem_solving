#-*- coding:utf-8 -*-
# baekjoon_2309
# heights = [20, 7, 23, 19, 10, 15, 25, 8, 13]
import sys
from itertools import combinations
heights = []
for line in range(9):
    heights+=list(map(int, sys.stdin.readline().split()))
combs = list(combinations(heights, 7))
for comb in combs:
    if sum(comb)==100:
        comb = sorted(comb)
        for element in comb:
            print(element)
        break