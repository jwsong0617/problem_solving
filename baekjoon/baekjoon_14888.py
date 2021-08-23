import sys
N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
ops = list(map(int, sys.stdin.readline().strip().split()))

max_value = -1000000000
min_value = 1000000000


def check_op(value, op_idx, cur_idx):
    global nums
    if op_idx == 0:
        value += nums[cur_idx+1]
    elif op_idx == 1:
        value -= nums[cur_idx+1]
    elif op_idx == 2:
        value *= nums[cur_idx+1]
    elif op_idx == 3:
        if value < 0:
            value = -(-value//nums[cur_idx+1])
        else:
            value = value // nums[cur_idx+1]
    return value


def func(value, cur_ops, cur_idx):
    global max_value
    global min_value
    if cur_idx == N-1:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
        return 0
    else:
        for i in range(4):
            if cur_ops[i] == 0:
                continue
            else:
                cur_ops[i] -= 1
                new_value = check_op(value, i, cur_idx)
                cur_idx += 1
                func(new_value, cur_ops, cur_idx)
                cur_idx -= 1
                cur_ops[i] += 1
        return -1


_ = func(nums[0], ops, 0)
print(max_value)
print(min_value)
