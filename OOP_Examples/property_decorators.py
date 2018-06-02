class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError("Age must be greater than zero.")

# The above setup allows you to use the functions as if they were a property
# No need to do print(self.age()) or print(self._age). print(self.age) works.
# Likewise self.age = new_age is now possible even though there is no self.age

# NOTE: not really kosher to have a single setter that affects multiple
# properties.
