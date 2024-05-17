#!/usr/bin/python3
"""Prime number game"""

""""The flaw in the function efficiency is that it undergoes a lot
of unnecessary precompilation for the list of prime numbers for each 
number in nums list, this can be avoided by precompiling a list of
primes up to the largest number in nums list and slice out only the
required segment for each number in list nums"""
def isWinner(x, nums):
    """
    nums - array of n (Given numbers 1 to n)
    x - number of rounds
    """
    while x > 0:
        ben = 0
        maria = 0
        prime = []
        for n in nums:
            # Extract list of prime numbers
            if n < 1:
                continue
            elif n == 1:
                prime = []
            elif n == 2:
                prime = [2]
            elif n > 2:
                prime = []
                index = 0
                values = [x for x in range(n)]
                values = values[2:]
                values.append(n)
                div = values[index]
                while div <= int(n**0.5):
                    for elem in values:
                        if elem % div == 0 and elem != div:
                            values.remove(elem)
                    index += 1
                    div = values[index]
                prime = prime + values

            # Start game
            if len(prime) % 2 == 0:
                ben += 1
            else:
                maria += 1
            x -= 1
        if ben > maria:
            return 'Ben'
        elif maria > ben:
            return 'Maria'
        else:
            return
