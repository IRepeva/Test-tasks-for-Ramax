# -*- coding: utf-8 -*-


def isFunnyFunction(data):
    if data:
        if all(int(a) > int(b) for a, b in zip(data, data[1:])):
            return 1
        elif all(int(a) < int(b) for a, b in zip(data, data[1:])):
            return 1
        elif all(int(a) == int(b) for a, b in zip(data, data[1:])):
            return 1
        else:
            return 0
    else:
        raise ValueError("data is None")
