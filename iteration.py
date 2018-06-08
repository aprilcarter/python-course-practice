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


# This generator function does half of what the Counter class does
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# counter = count_up_to(5)
# next(counter)
# for num in counter:
#   print(num)


# infinite generator
def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1


# Generator expressions work a bit like list comprehension but with ()
generator = (num for num in range(1, 10))
sum([num for num in range(1, 10)])  # creates and passes in a list
sum(num for num in range(1, 10))  # uses generator expression. Better on memory
