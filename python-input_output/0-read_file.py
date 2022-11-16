#!/usr/bin/python3
"""Read a file."""


def read_file(filename=""):
    """read a file."""
    with open(filename) as f:
        line = f.read()
        print(line, end="")
