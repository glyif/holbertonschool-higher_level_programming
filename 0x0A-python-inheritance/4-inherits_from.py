#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    inherist_from - checks if obj is a subclass of a_class
    
    Args:
    @obj: obj to check
    @a_class: obj to check against
    """
    if (issubclass(type(obj), a_class)):
        if (type(obj) != a_class):
            return (True)
    return (False)
