def dfs(computers, visited, root):
    stack = [root]
    while(stack):
        j=stack.pop()
        if(visited[j]==0):
            visited[j]=1
        for i in range(len(computers)):
            if(computers[j][i] == 1 and visited[i]==0):
                stack.append(i)

def solution(n, computers):
    answer=0
    i=0
    visited = [0]*len(computers)
    while 0 in visited:
        if(visited[i]==0):
            dfs(computers, visited, i)
            answer+=1
        i+=1
    return answer