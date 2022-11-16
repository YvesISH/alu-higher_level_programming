#!/usr/bin/python3
"""class to json."""


class Student:
    """contains student data."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class to json."""

        return self.__dict__
