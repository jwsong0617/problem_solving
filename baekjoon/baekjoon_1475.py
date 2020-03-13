#-*- coding:utf-8 -*-
# baekjoon_1475
import sys
from math import ceil
room_num = map(int, sys.stdin.readline().rstrip())
digits = [0]*10
max_values = []
for num in room_num:
    digits[num] += 1
for idx, digit in enumerate(digits):
    if digit == max(digits):
        if(idx == 6 or idx == 9):
            max_values.append(ceil((digits[6]+digits[9]) / 2))
        else:
            max_values.append(digit)
print(max(max_values))
