#-*- coding:utf-8 -*-
# baekjoon_15552
import sys
T = int(sys.stdin.readline().rstrip())
for line in range(T):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))
