#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square 2D matrix 90 degrees clockwise in place.
    
    Args:
        matrix (list of list of int): The matrix to rotate.
    """
    n = len(matrix)

    # Loop through each "layer" of the matrix from the outside in
    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        for i in range(first, last):
            # Calculate the offset for each layer
            offset = i - first

            # Save the top-left value
            top_left = matrix[first][i]

            # Move bottom-left to top-left
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom-right to bottom-left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move top-right to bottom-right
            matrix[last][last - offset] = matrix[i][last]

            # Move saved top-left to top-right
            matrix[i][last] = top_left
