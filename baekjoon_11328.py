#-*- coding:utf-8 -*-
# baekjoon_11328
import sys
from collections import Counter
N = int(sys.stdin.readline())
for i in range(N):
    a, b = sys.stdin.readline().rstrip().split(' ')
    a_c = Counter(a)
    b_c = Counter(b)
    if(a_c == b_c):
        print("Possible")
    else:
        print("Impossible")
