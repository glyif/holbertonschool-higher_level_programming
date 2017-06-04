#!/usr/bin/python3


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ - initializes value for Student

        Args:
        @self: self
        @first_name: first name
        @last_name: last name
        @age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - returns dict rep

        Args:
        @self: self
        @attrs: list of strings

        Return: dict rep of self
        """
        attrs_dict = {}
        if attrs is None:
            return (self.__dict__)
        for element in attrs:
            if hasattr(self, element):
                attrs_dict[element] = self.__dict__.get(element)
        return (attrs_dict)
