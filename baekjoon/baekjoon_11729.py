import sys
def move(a, b, n):
    if(n==1):
        print(str(a)+' '+str(b))
        return
    c = 6-a-b
    move(a, c, n-1)
    print(str(a)+' '+str(b))
    move(c, b, n-1)
N = int(sys.stdin.readline())
print(2**N-1)
move(1, 3, N)