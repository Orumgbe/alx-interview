#!/usr/bin/python3
"""Pascal triangle algorithm"""


def pascal_triangle(n):
    """Returns pascal triangle of 'n' steps"""
    myList = []
    if n <= 0:
        return myList
    for w in range(0, n):
        row = []
        r = 0
        while len(row) <= w:
            row.append(combination(w, r))
            r += 1
        myList.append(row)
    return myList


def factorial(n):
    """Returns factorial of number"""
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        return -1


def combination(n, r):
    """Returns mathematical value of nCr"""
    if n >= r and r >= 0:
        return int(factorial(n)/(factorial(n-r) * factorial(r)))
    else:
        return -1
        