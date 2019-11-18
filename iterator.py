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
