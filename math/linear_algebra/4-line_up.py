#!/usr/bin/env python3
"""
This module provides:
- matrix_shape: to find the shape of a matrix or array.
- add_arrays: to add two arrays or matrices element-wise.
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of dimensions.

    Args:
        matrix (list): A list or nested list.

    Returns:
        list: Dimensions of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape


def add_arrays(arr1, arr2):
    """
    Adds two arrays or matrices of the same shape.

    Args:
        arr1 (list): First array or matrix.
        arr2 (list): Second array or matrix.

    Returns:
        list: Element-wise sum, or None if shapes do not match.
    """
    if matrix_shape(arr1) != matrix_shape(arr2):
        return None

    if isinstance(arr1[0], list):  # 2D
        return [
            [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]
            for i in range(len(arr1))
        ]
    else:  # 1D
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
