import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(True):
        if(scoville == []):
            answer = -1
            break
        elif(scoville[0]>=K):
            break            
        minVal = heapq.heappop(scoville)
        if(scoville == []):
            answer = -1
            break
        secondMinVal = heapq.heappop(scoville)
        mixedVal = minVal+secondMinVal*2
        heapq.heappush(scoville,mixedVal)
        answer+=1        
    return answer