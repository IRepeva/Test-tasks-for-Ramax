from collections import Counter


def sort_function(lst):
    count = Counter(lst)
    lst.clear()
    maximum = max(count.keys())
    for number in range(maximum, 0, -1):
        lst.extend([number] * count[number])
    return lst


def sort_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] == 2:
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
        else:
            left += 1
    return lst
