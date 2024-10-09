#!/usr/bin/python3
"""A function that returns the perimeter
of the island described in grid"""


def island_perimeter(grid):
    """
    :type grid: List[List[int]]
    return int
    """

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    perimeter = 0
    connection = 0
    length_row = len(grid)
    length_col = len(grid[0])

    for i in range(length_row):
        for j in range(length_col):
            if grid[i][j] == 1:
                perimeter += 4

                """check for top"""
                if i != 0 and grid[i - 1][j] == 1:
                    connection += 4 - 2
                if j != 0 and grid[i][j - 1] == 1:
                    connection += 4 - 2
    return perimeter - (connection)
