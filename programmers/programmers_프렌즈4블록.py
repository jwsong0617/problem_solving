def solution(m, n, board):
    # answer = 0
    directions = [[1,0], [1,1],[0,1]] #우, 우하, 하
    erased_block_num = 0
    #roop
    roop_flag = True
    while(roop_flag):
        roop_flag = False
        board_new = board[:]
        # check condition
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
        #         print('i:',i,'j:',j)
                condition_match_flag = True
                for delta in directions:
                    delta_x = delta[0]
                    delta_y = delta[1]
        #             print('delta x:',delta_x, 'delta y:',delta_y)
                    if((i+delta_x) >= m or (j+delta_y) >= n):
        #                 print('index over')
        #                 print(i+delta_x, j+delta_y)
                        condition_match_flag = False
                        break
                    if(cell == 'b' or board[i+delta_x][j+delta_y] == 'b'):
                        condition_match_flag = False
                        break
                    if(cell != board[i+delta_x][j+delta_y]): #if not match the condition
        #                 print('do not same')
        #                 print(i+delta_x, j+delta_y)
                        condition_match_flag = False
                        break
                if(condition_match_flag):
                    roop_flag = True
        #             print('condition_match_flag')
        #             print('i:',i,'j:',j)
                    s_1 = board_new[i][:j] + 'xx' + board_new[i][j+2:]
                    s_2 = board_new[i+1][:j] + 'xx' + board_new[i+1][j+2:]
        #             print(s_1)
        #             print(s_2)
                    board_new[i] = s_1
                    board_new[i+1] = s_2
        #             board_new[i] = "".join(s_1)
        #             board_new[i+1] = "".join(s_2) #if match the condition            
    #     print(board_new)
        #go down
        # print('board_new:',board_new)
        board_new_t = list(map(list, zip(*board_new)))
    #     print(board_new_t)
        for j, col in enumerate(board_new_t):
            erased_block_num += col.count('x')
            board_new_t[j] = ''.join(col).replace('x','')
            max_n = len(board_new_t[j])
            blank = 'b'*(m-max_n)
            board_new_t[j] = blank + board_new_t[j]
        board = list(map(''.join,list(map(list, zip(*board_new_t)))))
        # print(board)
    # print(erased_block_num)
    return erased_block_num