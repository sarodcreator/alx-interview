from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
    """

    # getting the the matrix
    m = len(matrix)

    # transposing the matrix
    for i in range(m):
        for j in range(i + 1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reversing the inner square
    for i in range(m):
        for j in range(m // 2):
            matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
