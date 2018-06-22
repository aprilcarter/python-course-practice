from random import choice


# Functions that call other functions,
def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x**2


print(sum(10, square))


# Function defs nested in functions
def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result


print(greet("Toby"))


# Function as a return
def make_laugh_func():
    def get_laugh():
        laugh = choice(('HAHAHAHA', 'lol', 'teheheeee'))
        return laugh

    return get_laugh


laugh = make_laugh_func()
print(laugh())


def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAHA', 'lol', 'teheheeee'))
        return f"{laugh} {person}"

    return get_laugh


laugh_at = make_laugh_at_func("Linda")
print(laugh_at())
