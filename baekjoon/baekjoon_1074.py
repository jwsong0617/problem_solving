from sys import stdin
count = 0
N, tr, tc = map(int, stdin.readline().strip().split(' '))
# board = [[0]*(2**N) for _ in range(2**N)]
# print(board)
# end_flag = 0
def recursion(n, r, c):
    # global end_flag
    global count
    if n == 1:
        if r == tr and c == tc:
            print(count)
            exit(0)
        else:
            count += 1
    else:
        nn = n // 2
        if r <= tr < r + n and c <= tc < c + n:
            for i in range(2):
                for j in range(2):                
                    recursion(nn, r + nn*i, c + nn*j)
                #     if end_flag == 1:
                #         break
                # if end_flag == 1:
                #         break
        else:
            count += n*n
recursion(2**N, 0, 0)