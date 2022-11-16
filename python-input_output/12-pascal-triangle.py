#!/usr/bin/python3
"""A script that creates pascal's triangle."""


def pascal_triangle(n):
    """creates pascal triangle."""

    pascals_triangle = []

    for i in range(n):
        pascals_triangle.append([1]*(i+1))

    for i in range(2, n):
        for j in range(1, i):
            pascals_triangle[i][j] = (pascals_triangle[i-1][j-1] + 
                                      pascals_triangle[i-1][j])

    return pascals_triangle
