#!/usr/bin/python3
"""A list that inhert the list object"""


class MyList(list):
    """Represent a Mylist"""

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
