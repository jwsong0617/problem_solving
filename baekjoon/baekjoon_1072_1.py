import math
X, Y = map(int,input().split())
Z = 100*Y//X

if(Z >= 99):
    print(-1)
else:
    print(math.ceil(((Z+1)*X-100*Y) / (99-Z)))