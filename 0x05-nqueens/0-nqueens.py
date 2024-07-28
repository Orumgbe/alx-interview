#!/usr/bin/python3

# Usage: nqueens N
# If the user called the program with the wrong number of arguments,
# print Usage: nqueens N,
# followed by a new line, and exit with the status 1
# where N must be an integer greater or equal to 4
# If N is not an integer, print N must be a number, followed by a new line,
# and exit with the status 1
# If N is smaller than 4, print N must be at least 4, followed by a new line,
# and exit with the status 1
# The program should print every possible solution to the problem
# One solution per line
# Format: see example
# You don’t have to print the solutions in a specific order
# You are only allowed to import the sys module

import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    backtrack algorithm to find solution
    """
    if r == n:
        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    res.append([i, j])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Program to solve the nqueen problem
    Return:
    List of lists for position of each queen in all possible scenarios
    """
    if not n.isdigit():
        print('N must be a number')
        sys.exit(1)
    else:
        try:
            num = int(n)
            if num < 4:
                print('N must be at least 4')
                sys.exit(1)

            cols = set()
            pos = set()
            neg = set()
            board = [[0] * num for _ in range(num)]

            backtrack(0, num, cols, pos, neg, board)
        except ValueError:
            print('N must be a number')
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    nqueens(sys.argv[1])
