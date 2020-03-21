import sys
from collections import deque
brackets = sys.stdin.readline().strip()
dq = deque()
total_pieces = 0
last_bracket = None
for bracket in brackets:
    if(bracket==")"):
        if(dq[-1]=="(" and last_bracket == "("):  # laser
            dq.pop()
            total_pieces+=len(dq)
        elif(dq[-1]=="(" and last_bracket == ")"):
            dq.pop()
            total_pieces+=1
    else:
        dq.append(bracket)
    last_bracket = bracket
print(total_pieces)
