#!/usr/bin/python3
"""this is a base class."""
import json
import csv
import turtle


class Base:
    """The base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json to string."""
        if list_dictionaries is None:
            return "[]"

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """SaVe to a file."""
        filename = cls.__name + ".json"
        yy = []
        if list_objs is not None:
            for xx in list_objs:
                yy.append(cls.to_dictionary(xx))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(yy))

    @staticmethod
    def from_json_string(json_string):
        """Json conversion."""
        if json_string is None:
            return []

        if len(json_string) == 0:
            return []

        json_list = json.loads(json_string)
        return json_list
