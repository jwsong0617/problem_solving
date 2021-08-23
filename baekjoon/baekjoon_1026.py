import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
A = sorted(A)
B = sorted(B, reverse=True)
answer = 0
for i in range(N):
    answer += A[i]*B[i]
print(answer)