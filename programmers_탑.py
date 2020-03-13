from collections import deque
def solution(heights):
    queue = deque(heights)
    answer = deque([])
    queueLen = len(queue)
    for i in range(1,len(queue)+1):
        h = queue.pop()
        j = 1
        print(h)
        print(i)
        if(i==queueLen):
            answer.appendleft(0)
            print(answer)
            break
        while(True):
            if(queue[queueLen-i-j]>h):
                answer.appendleft(queueLen-i-j+1)
                print(answer)
                break
            elif((queueLen-i-j)<0):
                answer.appendleft(0)
                print(answer)
                break
            else:
                j+=1
    return list(answer)