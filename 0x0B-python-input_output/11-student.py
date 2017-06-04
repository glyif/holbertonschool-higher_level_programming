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

    def to_json(self):
        """
        to_json - returns dict rep

        Args:
        @self: self

        Return: dict rep of self
        """
        return (self.__dict__)
