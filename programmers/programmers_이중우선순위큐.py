import heapq as hq
def solution(operations):
    heapque = []
    heapque_max = []
    hq.heapify(heapque)
    hq.heapify(heapque_max)
    for operation in operations:
        ops, num = operation.split(' ')
        num = int(num)    
        if(ops=='I'):
            hq.heappush(heapque,num)
            hq.heappush(heapque_max,(-num,num))
        elif(ops=='D' and num == -1):
            if(heapque==[]):
                continue
            minNum = hq.heappop(heapque)
            heapque_max.remove((-minNum,minNum))
        elif(ops=='D' and num == 1):
            if(heapque==[]):
                continue
            maxNum = hq.heappop(heapque_max)[1]        
            heapque.remove(maxNum)
    print(heapque)
    print(heapque_max)
    if(heapque == []):
        answer = [0,0]
    else:
        minNum = hq.heappop(heapque)
        maxNum = hq.heappop(heapque_max)[1]
        answer = [maxNum,minNum]    
    return answer