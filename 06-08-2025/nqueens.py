import numpy as np

N = int(input("Enter the number of queens: "))

def printSolution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def isSafe(board, row, col):
    # Check row on left side
    if 1 in board[row, :col]:
        return False

    # Check upper diagonal on left side
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i, j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row + 1, N), range(col - 1, -1, -1)):
        if board[i, j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    if col == N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row, col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[row, col] = 0
    return False

def solveNQ():
    board = np.zeros((N, N), dtype=int)
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True

solveNQ()