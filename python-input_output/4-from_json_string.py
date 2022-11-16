#!/usr/bin/python3
"""From Json to Object."""


import json


def from_json_string(my_str):
    """From json to Objects."""
    return json.loads(my_str)
