from collections import Counter


def sort_function(lst):
    count = Counter(lst)
    lst.clear()
    maximum = max(count.keys())
    for number in range(maximum, 0, -1):
        lst.extend([number] * count[number])
    return lst
