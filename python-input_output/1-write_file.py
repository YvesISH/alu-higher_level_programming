#!/usr/bin/python3
"""write to a file."""


def write_file(filename="", text=""):
    """Write to a file."""
    with open(filename, 'w+') as f:
        return f.write(text)
