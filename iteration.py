# iterable - something that can be made into an iterator
# iterator - something that can be iterated on


def custom_for(iterable, func):
    # becomes an iterator
    iterator = iter(iterable)
    while True:
        try:
            func(next(iterator))
        except StopIteration:
            break


# Basic range()-like iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


# for x in Counter(0, 10):
#    print(x)
