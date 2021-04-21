import sys

T = int(sys.stdin.readline().strip())
fibs = [0]*41
fibs[0] = 0
fibs[1] = 1


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if fibs[n]:
            pass
        else:
            fibs[n] = fib(n-1) + fib(n-2)
        return fibs[n]


for i in range(T):
    N = int(sys.stdin.readline().strip())
    if N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')
    else:
        _ = fib(N)
        print(str(fibs[N-1]) + ' ' + str(fibs[N]))
