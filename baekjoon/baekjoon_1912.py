# Sol
import sys
N = int(input())
C = list(map(int, sys.stdin.readline().rstrip().split()))  # candidates
S = [-1]*N
S[0] = C[0]
for i in range(N):
    S[i] = max(0, S[i-1]) + C[i]
# print(S)
print(max(S))

# Wrong Solution - O(n^2)
import sys
N = int(input())
C = list(map(int, sys.stdin.readline().rstrip().split()))  # candidates
S = [-1]*N  # summations
A = []  # answers
max_val = -1
for i in range(N):
    S[i] = sum(C[0:i+1])
    max_val = max(max_val, S[i])
    for j in range(0, i):
        max_val = max(max_val, S[i]-S[j])
print(max_val)