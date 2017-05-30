#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - checks of obj is an instance of
    or inherited from a_class

    Args:
    @obj: object to check
    @a_class: object to check against

    Return: True is so or False if not
    """
    if (isinstance(obj, a_class)):
        return (True)

    return (False)
