class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        return f"This animal says {sound}"


# Just pass the parent class in as an argument to indicate inheritance
class Cat(Animal):
    def __init__(self, name, breed, toy):
        # Can call Animal.__init__(self, etc.), but there's a function for that
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}."

# some_animal = Animal(name="Po", species="Bear")
# my_cat = Cat(name="Kitty", breed="Mix", toy="Fishing Rod")
