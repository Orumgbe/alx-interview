#!/usr/bin/python3
"""minOperations(n) method"""


def minOperations(n):
    """
        Calculates minimum number of operations required to achieve n chars
        arg: n is the required number of characters within the file
    """
    fact = 1    # Current known factor for argument n
    chars = 1   # Current number of characters within the file
    op_count = 0    # Number of operations performed on the file
    while (chars < n):
        if n % chars == 0:  # Check if char number is a factor of n
            # Until we get a factor we keep performing 2 operstions
            # copy and paste, hence characters keep doubling
            # and operations count increments in values of 2
            op_count += 2
            fact = chars    # Keeping a record of current known factor of n
            chars *= 2
        else:
            # Here only one operation if performed on each loop 'paste',
            # we paste the current known factor until we get a new factor
            # or reach the value of 'n'
            op_count += 1
            chars += fact
    return op_count
