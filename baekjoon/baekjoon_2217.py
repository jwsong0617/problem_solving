import sys
N = int(sys.stdin.readline().strip())
ropes = []
max_weight = 0
for i in range(N):
    ropes.append(int(sys.stdin.readline().strip()))
for i, rope in enumerate(sorted(ropes)):
    if rope*(N-i) > max_weight:
        max_weight = rope*(N-i)
print(max_weight)