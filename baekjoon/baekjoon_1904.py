import sys
N = int(sys.stdin.readline())

fs = [0]*1000001
fs[1] = 1
fs[2] = 2

for i in range(3, N+1):
    fs[i] = (fs[i-1] + fs[i-2]) % 15746
print(fs[N])

# RecursionError: maximum recursion depth exceeded in comparison 때문에 재귀는 안 됨
# def f(n):
#     if n == 1:
#         return fs[1]
#     elif n == 2:
#         return fs[2]
#     else:
#         if fs[n]:
#             answer = fs[n]
#         else:
#             fs[n] = f(n-1) + f(n-2)
#             answer = fs[n]
#         return answer%15746
#
# print(f(N))
