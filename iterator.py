class Iterator:

    def __init__(self, iterable, key):
        self.iterable = iterable
        self.key = key
        self.length = len(iterable)
        if self.key == "чет":
            self.index = 0
        elif self.key == "нечет":
            self.index = 1
        else:
            raise ValueError("Only 'чет' and 'нечет' values are acceptable")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            value = self.iterable[self.index]
            self.index += 2
            return value
        else:
            raise StopIteration


class IteratorWoIndices:
    def __init__(self, iterable, key):
        self.iterable = iterable
        self.key = key

    def __iter__(self):
        for index, item in enumerate(self.iterable, start=1):
            if self.key == "чет":
                if index % 2:
                    continue
            elif self.key == "нечет":
                if not index % 2:
                    continue
            else:
                raise ValueError("Only 'чет' and 'нечет' values are acceptable")
            yield item
