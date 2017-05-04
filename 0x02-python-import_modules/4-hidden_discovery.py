#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    i = 0
    modules = dir(hidden_4)
    for mod in modules:
        if mod[0] != '_':
            print("{:s}".format(mod))
