class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init(self, name):
        # super() will only refer to the parent that is passed in first.
        # It can still be used, but the other parent's __init__ will need
        # to be called manually. Might as well call them both manually
        # so there's no need to deduce which one is being called automatically
        # with super()
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)
