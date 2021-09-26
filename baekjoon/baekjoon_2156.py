N = int(input())
A = [None] * (N+1)
D = [None] * (N+1)
A[0] = 0
D[0] = 0
A[1] = int(input())
D[1] = A[1]
if N > 1:
    A[2] = int(input())
    D[2] = A[1]+A[2]
for i in range(3, N+1):
    v = int(input())
    A[i] = v
    D[i] = max(D[i-1], D[i-2]+A[i], D[i-3] + A[i-1] + A[i])
print(D[N])