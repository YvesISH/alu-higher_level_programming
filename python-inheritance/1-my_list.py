#!/usr/bin/python3
"""Defining a Class."""


class Mylist(list):
    """A class that inherits from parent class list."""
    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
