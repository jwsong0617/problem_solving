N, C = map(int, input().split())
cord = []
for i in range(N):
    cord += [int(input())]
cord_sorted = sorted(cord)
left = 1
right = cord_sorted[-1] - cord_sorted[0]
ans = 0
d = 0
while(left<=right):
    cnt = 1
    mid = (left+right)/2
    mid = int(mid)
    start = cord_sorted[0]
    for i in range(1,N):        
        d = cord_sorted[i] - start
        if(d>=mid):
            cnt+=1
            start = cord_sorted[i]
    if(cnt>=C):
        ans = mid
        left = mid+1        
    else:
        right = mid-1
print(ans)