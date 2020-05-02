# Sol 1
import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split())
print(pow(A,B,C))

# Sol 2
import sys
def recursion(a, b, c):
    if(b == 0):
        return 1
    val = recursion(a, b//2, c)
    if b % 2 == 0:
        return val*val%c
    else:
        return (val*val%c)*(a%c)%c
A, B, C = map(int, sys.stdin.readline().rstrip().split())
print(recursion(A, B, C))
# (val*val)*a%c = (val*val%c)*(a%c)%c (모듈로 특징)
