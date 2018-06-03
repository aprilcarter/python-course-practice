# *An object has the abillity to behave differently in different contexts.
# There are two examples below.


class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog(Animal):
    # Same method works differently for different classes
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Fish(Animal):
    def speak(self):
        return "bloop"

    def add(self, n1, n2):
        # + operator works differently depending on the variable types
        add = int(n1) + int(n2) # 2 + 3 = 5
        concat = str(n1) + str(n2) # '2' + '3' = '23'
        return {add: add, concat: concat}
