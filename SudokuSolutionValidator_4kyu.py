def valid_solution(board):
    for row in board:  # row check
        passedNumbers = []
        for number in row:
            if number in passedNumbers:
                return False
            else:
                passedNumbers.append(number)

    for column, topNumber in enumerate(board[0]):  # column check
        passedNumbers = []
        for numberRow in range(0, 9):
            if board[numberRow][column] in passedNumbers:
                return False, numberRow, column, passedNumbers
            else:
                passedNumbers.append(board[numberRow][column])

    passedNumbersInBlocks = [[] for i in range(0, 9)]
    for rowNumber, rowValue in enumerate(board):  # box check
        for column, number in enumerate(rowValue):
            if number in passedNumbersInBlocks[column // 3 + rowNumber // 3 * 3]:
                return False
            else:
                passedNumbersInBlocks[column // 3 + rowNumber // 3 * 3].append(number)

    return True


print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
