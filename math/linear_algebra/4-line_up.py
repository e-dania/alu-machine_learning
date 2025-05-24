#!/usr/bin/env python3
"""
Add two arrays or matrices element-wise.
Handles both 1D and 2D arrays, and includes checks for empty inputs.
"""


def matrix_shape(matrix):
    """Returns the shape of the input matrix or array."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape


def add_arrays(arr1, arr2):
    """
    Adds two arrays or matrices of the same shape.
    Returns None if shapes do not match.
    """
    # If both are empty
    if arr1 == [] and arr2 == []:
        return []

    # Shape mismatch
    if matrix_shape(arr1) != matrix_shape(arr2):
        return None

    # 2D array
    if isinstance(arr1[0], list):
        return [
            [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]
            for i in range(len(arr1))
        ]
    # 1D array
    else:
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
