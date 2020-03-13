#-*- coding:utf-8 -*-
# baekjoon_1267
import sys
import string
from collections import Counter
S = sys.stdin.readline().rstrip()
Cs = Counter(S)
results = []
for char in string.ascii_lowercase:
    if(char in Cs.keys()):
        results.append(str(Cs[char]))
    else:
        results.append('0')
print(' '.join(results))
