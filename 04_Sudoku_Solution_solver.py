def valid_solution(board):
    #rows
    for row in board:
        if len(set(row))!=9: return False

    #columns
    num = set()
    for i in range(9):
        for j in range(9):
            num.add(board[j][i])
        if len(num)!=9: return False
        num = set()

    #3x3 boxes
    num = set()
    for i in range(9):
        for j in range(9):
            num.add(board[(i // 3) * 3 + j // 3][ i * 3 % 9 + j % 3])
        if len(num)!=9: return False
    return True


valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]])
