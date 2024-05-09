#!/usr/bin/python3
"""Island perimeter task"""


def island_perimeter(grid):
    """
    Return perimeter of island in grid
    0 represents water
    1 represents land
    width and height doesn't exceed 100
    Cells are not connected diagonally
    Everything outsidde the grid is water
    No lakes within the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
