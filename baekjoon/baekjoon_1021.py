from collections import deque
import sys
N, input_size = map(int, sys.stdin.readline().split())
inputs = map(int, sys.stdin.readline().split())
dq2 = deque(range(1, N+1))
dq3 = deque(range(1, N+1))
op_2_num = 0
op_3_num = 0
total_op_num = 0
for num in inputs:
    while(dq2[0]!=num):
        dq2.append(dq2.popleft())
        op_2_num+=1
    while(dq3[0]!=num):
        dq3.appendleft(dq3.pop())
        op_3_num+=1
    if(op_2_num<=op_3_num):
        dq2.popleft()
        dq3 = dq2.copy()
        total_op_num+=op_2_num
        op_2_num = 0
        op_3_num = 0
    else:
        dq3.popleft()
        dq2 = dq3.copy()
        total_op_num+=op_3_num
        op_2_num = 0
        op_3_num = 0
print(total_op_num)