#!/usr/bin/python3
"""Module for coin change algorithm"""

def makeChange(coins, total):
    """Return fewest number of coins required to meet total"""
    if total <= 0:
        return 0
    if not total and not len(coins) == 0:
        return -1
    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        if total < coin:
            continue
        # Find how many of the particular coin can be removed
        num = total // coin
        total = total - coin * num
        count += num
        if total == 0:
            return count
    return -1
