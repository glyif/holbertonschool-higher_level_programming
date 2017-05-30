#!/usr/bin/python3
"""
MyList class
inherits from list object
prints and sorts list.
"""


class MyList(list):
    def print_sorted(self):
        """
        print_sorted - prints the list sorted (ascending)
        @self: self
        """
        print(sorted(self))
