# Extend the polymorphism of built-in functions like len() and operations
# like + by defining a version of their dunder methods in your own class. In
# the example below, a variety of things are made possible, including the
# addition of two human objects

from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        raise TypeError(f"Unalble to add Human and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, int):
            return[copy(self) for i in range(other)]
        raise TypeError("Unable to multiply a Human and a non-integer")
