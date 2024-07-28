#!/usr/bin/python3
"""This module holds the validUTF8 method"""

from itertools import takewhile


def validUTF8(data):
    """
    Determines if a given data set uses valid utf8 encoding
    Returns True or False
    """
    bits_gen = (
        [bool(num & (1 << shift)) for shift in range(7, -1, -1)]
        for num in data
    )

    for byte in bits_gen:
        if byte[0] == 0:
            continue

        ones = sum(takewhile(bool, byte))
        if ones <= 1:
            return False
        if ones >= 4:
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits_gen)
            except StopIteration:
                return False
            if byte[0:2] != [True, False]:
                return False

    return True
