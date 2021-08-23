import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B, C = list(map(int, sys.stdin.readline().strip().split()))
supervisors = 0
for i in range(N):
    remainder = A[i] - B
    supervisors += 1
    if remainder <= 0:
        continue
    else:
        if remainder % C == 0:
            supervisors += remainder // C
        else:
            supervisors += (remainder // C) + 1
print(supervisors)
