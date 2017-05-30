#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    is_some_class - checks if obj is exactly an instance of a_class

    Args:
    @obj: object to check
    @a_class: class to check match with obj
    """
    if (type(obj) is a_class):
        return (True)

    return (False)
