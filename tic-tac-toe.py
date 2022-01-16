import random
from copy import copy


def main():
    def printBoard(xList, oList):
        for y in range(0, 3):
            for x in range(0, 3):
                if (x, y) in xList:
                    print('|x|', end='')
                elif (x, y) in oList:
                    print('|o|', end='')
                else:
                    print('| |', end='')
            print('')

    def winChecker(xList, oList):
        for row in range(0, 3):
            xInRow = 0
            oInRow = 0
            xInColumn = 0
            oInColumn = 0
            for column in range(0, 3):
                if (row, column) in xList:
                    xInRow += 1
                elif (row, column) in oList:
                    oInRow += 1
                if (column, row) in xList:
                    xInColumn += 1
                elif (column, row) in oList:
                    oInColumn += 1

            if xInRow == 3 or xInColumn == 3:
                return 'x'
            elif oInRow == 3 or oInColumn == 3:
                return 'o'

        xDiagonal = [0, 0]
        for position in xList:
            if position[0] == position[1]:
                xDiagonal[0] += 1
                if position == (1, 1):
                    xDiagonal[1] += 1
            elif position == (0, 2) or position == (2, 0):
                xDiagonal[1] += 1

        oDiagonal = [0, 0]
        for position in oList:
            if position[0] == position[1]:
                oDiagonal[0] += 1
                if position == (1, 1):
                    oDiagonal[1] += 1
            elif position == (0, 2) or position == (2, 0):
                oDiagonal[1] += 1

        if 3 in xDiagonal:
            return 'x'
        elif 3 in oDiagonal:
            return 'o'

        return None

    def optimalMove(xList, oList):
        for y in range(0, 3):
            for x in range(0, 3):
                move = (x, y)
                if move in oList or move in xList:
                    pass
                else:
                    xListCopy = copy(xList)
                    oListCopy = copy(oList)
                    xListCopy.append(move)
                    oListCopy.append(move)
                    if winChecker(xListCopy, oList) is not None or winChecker(xList, oListCopy) is not None:
                        return x, y

        while True:
            randomMove = (random.randint(0, 2), random.randint(0, 2))
            if randomMove not in oList and randomMove not in xList:
                print('move is random', randomMove)
                return randomMove

    def gameLoop():
        xPositions = []
        oPositions = []
        turn = 'x'
        printBoard(xPositions, oPositions)

        while True:
            if turn == 'x':  # user's turn (x)
                move = tuple(input('where do you want to place your next x (anser like: 0, 1)?').split(', '))
                move = int(move[0]), int(move[1])

                if move not in xPositions and move not in oPositions:
                    xPositions.append(move)

                turn = 'o'
            else:  # computer's turn
                move = optimalMove(xPositions, oPositions)
                oPositions.append(move)
                turn = 'x'

            printBoard(xPositions, oPositions)
            winner = winChecker(xPositions, oPositions)
            if winner is not None:
                print('The winner is:', winner)
                break

    gameLoop()

if __name__ == '__main__':
    main()
