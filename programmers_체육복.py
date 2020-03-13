def solution(n, lost, reserve):    
    available = [1]*n
    lost.sort()
    reserve.sort()    
    for idx in lost:
        available[idx-1]=0
        if(idx in reserve):
            available[idx-1]=1
            reserve.remove(idx)
            continue
    for idx in lost:                
        if(idx-1 in reserve):
            available[idx-1]=1
            reserve.remove(idx-1)
            continue
        elif(idx+1 in reserve):
            available[idx-1]=1
            reserve.remove(idx+1)
            continue
    return sum(available)