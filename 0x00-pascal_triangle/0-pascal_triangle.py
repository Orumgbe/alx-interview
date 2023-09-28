from math import factorial


def combination(n, r):
    """Returns mathematical value of nCr"""
    if n >= r and r >= 0:
        return int(factorial(n)/(factorial(n-r) * factorial(r)))
    else:
        return -1

def pascal_triangle(n):
    """Returns pascal triangle of 'n' steps"""
    myList = []
    if n <= 0:
        return myList
    h = 1
    w = 1
    while n > 0:
        row = []
        r = 0
        while len(row) < w:
            row.append(combination(h-1, r))
            r += 1
        myList.append(row)
        n -= 1
        w += 1
        h += 1
    return myList



    