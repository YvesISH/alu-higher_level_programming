#!/usr/bin/python3
"""Save object to a file."""


import json


def save_to_json_file(my_obj, filename):
    """Save object to a text file using JSON."""
    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
