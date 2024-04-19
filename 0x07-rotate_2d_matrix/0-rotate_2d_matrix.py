#!/usr/bin/env python3
"""Rotate 2d matrix method"""


def rotate_2d_matrix(matrix):
    """Rotates a given n x n matrix 90 degress clockwise"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
