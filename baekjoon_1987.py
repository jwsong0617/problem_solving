import collections
R, C = map(int,input().split())
board = [[0]*C]*R
cache = [['']*C for _ in range(R)]
for r in range(R):
    row = list(input())    
    board[r] = row  
def bfs():
    q = collections.deque()
    q.append((0,0,board[0][0]))    
    max_size = 1
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while(q):
        x, y, data = q.popleft()
        for dx, dy in direct:
            nx = x+dx
            ny = y+dy
            if(ny < 0 or nx < 0 or ny >= R or nx >= C):
                continue
            if(board[ny][nx] in data):
                continue
            if(cache[ny][nx] == data + board[ny][nx]):
                continue
            else:
                cache[ny][nx] = data+board[ny][nx]
                q.append((nx, ny, data + board[ny][nx]))
                max_size = max(max_size, len(data)+1)
    print(max_size)        
bfs()