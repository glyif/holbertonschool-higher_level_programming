#!/usr/bin/python3
"""
BaseGeometry - Class
"""


class BaseGeometry:
    """BaseGeomerty"""
    def area(self):
        """
        area - function for area

        Args:
        @self
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validation - validates a value

        Args:
        @name: name always string
        @value: integer value
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
