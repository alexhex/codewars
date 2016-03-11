def validSolution(board):
    valid_str = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sqr_lst  = [[] for i in range(9)]
    vert_lst = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            vert_lst[i] += [board[j][i]]
        sqr_lst[i] = board[int(i)/3*3][int(i)%3*3:int(i)%3*3+3] + board[int(i)/3*3+1][int(i)%3*3:int(i)%3*3+3] + board[int(i)/3*3+2][int(i)%3*3:int(i)%3*3+3]
    for j in range(9):
        board[j].sort()
        sqr_lst[j].sort()
        vert_lst[j].sort()
        if board[j] != valid_str:
            print False
        elif vert_lst[j] != valid_str:
            print False
        elif sqr_lst[j] != valid_str:
            print False
    print True

    # for lst in board:
    #     lst.sort()
    #     if lst != valid_str:
    #         return False
    # vert_str = []
    # sqr_str = []
    # for i in range(9):
    #     for j in range(9):
    #         vert_str.append(board[j][i])
    #     vert_str.sort()
    #     if vert_str != valid_str:
    #         return False
    #     else:
            # vert_str =[]
#board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
#        [6, 7, 2, 1, 9, 5, 3, 4, 8],
#        [1, 9, 8, 3, 4, 2, 5, 6, 7],
#        [8, 5, 9, 7, 6, 1, 4, 2, 3],
#        [4, 2, 6, 8, 5, 3, 7, 9, 1],
#        [7, 1, 3, 9, 2, 4, 8, 5, 6],
#        [9, 6, 1, 5, 3, 7, 2, 8, 4],
#        [2, 8, 7, 4, 1, 9, 6, 3, 5],
#        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
# validSolution(board)
