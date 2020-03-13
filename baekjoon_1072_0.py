import math
X, Y = map(int,input().split())
win_rate = 100*Y//X
if(win_rate >= 99):
    print(-1)
else:
    left = 0
    right = math.pow(10,9)+1
    while(left<=right):        
        mid = int((left+right)/2)
        new_win_rate = int(((Y+mid)*100/(X+mid)))
        if(new_win_rate > win_rate):
            right = mid-1
        else:
            left = mid+1
    print(left)