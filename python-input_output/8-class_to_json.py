#!/usr/bin/python3
"""A function that returns a dictionary description."""


def class_to_json(obj):
    """return a dictionary desc."""
    return obj.__dict__
