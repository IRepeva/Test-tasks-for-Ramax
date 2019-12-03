# -*- coding: utf-8 -*-


def isFunnyFunction(data):
    if data:
        if all(int(a) == int(b) + 1 for a, b in zip(data, data[1:])):
            return True
        elif all(int(a) == int(b) - 1 for a, b in zip(data, data[1:])):
            return True
        elif all(int(a) == int(b) for a, b in zip(data, data[1:])):
            return True
        else:
            return False
    else:
        raise ValueError("data is None")


def isFunnyFunction2(data):
    if data:
        total_sum = 0
        minimum = float('+inf')
        maximum = float('-inf')

        for val in data:
            if int(val) < minimum:
                minimum = int(val)

            elif int(val) > maximum:
                maximum = int(val)

            total_sum += int(val)

        if 2 * total_sum == maximum * (maximum + 1) - minimum * (minimum - 1) or maximum == minimum:
            return True
        return False
    else:
        raise ValueError("data is None")
