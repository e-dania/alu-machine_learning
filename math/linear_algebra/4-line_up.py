#!/usr/bin/env python3
"""
This module provides functions to:
1. Determine the shape of a matrix.
2. Add two matrices of the same shape.
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of dimensions.

    Args:
        matrix (list): A nested list representing the matrix.

    Returns:
        list: A list of integers representing the dimensions of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape


def add_arrays(arr1, arr2):
    """
    Adds two matrices (or arrays) element-wise.

    Args:
        arr1 (list of lists): First matrix
        arr2 (list of lists): Second matrix

    Returns:
        list of lists: The element-wise sum of arr1 and arr2,
                       or None if shapes do not match.
    """
    if matrix_shape(arr1) != matrix_shape(arr2):
        return None

    addition = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        addition.append(temp)
    return addition
