#!/usr/bin/python3


def class_to_json(obj):
    """
    class_to_json - returns class obj as json

    Args:
    @obj: object

    Return: JSON object
    """
    return (obj.__dict__)
