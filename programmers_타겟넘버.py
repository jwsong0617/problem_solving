def dfs(numbers, target, k):
    global answer
    if(k==len(numbers)):
        if(sum(numbers)==target):
            answer+=1            
        return
    else:
        numbers[k]=numbers[k]*1
        dfs(numbers, target, k+1)        
        numbers[k]=numbers[k]*(-1)
        dfs(numbers, target, k+1)
answer=0
def solution(numbers, target):
    dfs(numbers, target, 0)
    return answer