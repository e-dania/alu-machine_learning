#!/usr/bin/env python3
"""
Adds two arrays (1D or 2D) if shapes match
"""

def matrix_shape(matrix):
    """Returns the shape of a matrix or array."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape


def add_arrays(arr1, arr2):
    """Adds two arrays or matrices element-wise."""
    if matrix_shape(arr1) != matrix_shape(arr2):
        return None

    if arr1 == []:  # both empty
        return []

    if isinstance(arr1[0], list):  # 2D
        return [
            [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]
            for i in range(len(arr1))
        ]
    else:  # 1D
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
