# start: 21:15
# end: 22:18
import sys

def check_chess_board(chess_board, st_color):
    need_repaint_num = 0
    if st_color == "B":
        colors = [["B", "W"], ["W", "B"]]
    elif st_color == "W":
        colors = [["W", "B"], ["B", "W"]]
    for i, row in enumerate(chess_board):
        color = colors[i % 2]
        for idx, col in enumerate(row):
            if idx % 2 == 1:
                if color[1] != col:
                    need_repaint_num += 1
            else:
                if color[0] != col:
                    need_repaint_num += 1
    return need_repaint_num


N, M = map(int, sys.stdin.readline().strip().split())
board = [0]*N
answer = N*M
for i in range(N):
    board[i] = list(sys.stdin.readline().strip())
for y in range(N-7):
    for x in range(M-7):
        cur_board = board[y:y+8]
        for row_idx in range(8):
            cur_board[row_idx] = cur_board[row_idx][x:x+8]
        answer = min(answer, check_chess_board(cur_board, "W"))
        answer = min(answer, check_chess_board(cur_board, "B"))
print(answer)