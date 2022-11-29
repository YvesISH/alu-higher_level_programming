#!/usr/bin/python3
"""
Module with add function.
"""


def add_integer(a, b=98):
    """
    Return integer addition of a and b
    """
    if type(a) is not int and type(b) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b 
