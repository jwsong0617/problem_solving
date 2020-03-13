#-*- coding:utf-8 -*-
# baekjoon_1267
import sys
import math
N = int(sys.stdin.readline().rstrip())
y_total = 0
m_total = 0
for time in map(int, sys.stdin.readline().rstrip().split()):
    y_total += (int(time / 30)+1) * 10
    m_total += (int(time / 60)+1) * 15
if y_total > m_total:
    print('M', m_total)
elif y_total == m_total:
    print('Y M', y_total)
else:
    print('Y', y_total)
