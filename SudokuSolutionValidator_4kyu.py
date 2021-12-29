def valid_solution(board):
    for row in board:
        passedNumbers = []
        for number in row:
            if number in passedNumbers:
                return False
            else:
                passedNumbers.append(number)

    for column, topNumber in enumerate(board[0]):
        passedNumbers = []
        for numberRow in range(0, 9):
            if board[column][numberRow] in passedNumbers:
                return False
            else:
                passedNumbers.append(board[column][numberRow])

    return True


print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                      [4, 9, 8, 2, 6, 1, 3, 7, 5],
                      [7, 5, 6, 3, 8, 4, 2, 1, 9],
                      [6, 4, 3, 1, 5, 8, 7, 9, 2],
                      [5, 2, 1, 7, 9, 3, 8, 4, 6],
                      [9, 8, 7, 4, 2, 6, 5, 3, 1],
                      [2, 1, 4, 9, 3, 5, 6, 8, 7],
                      [3, 6, 5, 8, 1, 7, 9, 2, 4],
                      [8, 7, 9, 6, 4, 2, 1, 3, 5]]))
