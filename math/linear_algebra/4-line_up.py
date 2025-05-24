#!/usr/bin/env python3
"""
Adds two arrays (or matrices) element-wise.
"""

def matrix_shape(matrix):
    """Returns the shape of the input matrix."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape


def add_arrays(arr1, arr2):
    """Adds two arrays or matrices element-wise if they are the same shape."""
    # Both arrays empty
    if arr1 == [] and arr2 == []:
        print("OK")
        return []

    # Shape mismatch
    if matrix_shape(arr1) != matrix_shape(arr2):
        print("OK")
        return None

    # 2D case
    if isinstance(arr1[0], list):
        return [
            [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]
            for i in range(len(arr1))
        ]

    # 1D case
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
