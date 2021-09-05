from sys import stdin
N = int(input())
board = [None]*N
for i in range(N):
    board[i] = list(map(int, stdin.readline().strip().split(' ')))
result = [0, 0, 0]

def check_number(num):
    global result
    if num == 0:
        result[1] += 1
    elif num == -1:
        result[0] += 1
    elif num == 1:
        result[2] += 1

def recursion(n, r, c):
    if n == 1:
        return check_number(board[r][c])
    else:
        temp_value = board[r][c]
        break_flag = False
        for i in range(r, r+n):
            for j in range(c, c+n):
                if board[i][j] != temp_value:
                    break_flag = True
                    break
            if break_flag == True:
                break
        if break_flag == False: #1 rule
            return check_number(temp_value)
        elif break_flag == True: #2 rule
            nn = n // 3
            for i in range(3):
                for j in range(3):
                    recursion(nn, r + i * nn, c + j * nn)
recursion(N, 0, 0)
print('\n'.join(map(str,result)))