class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says{sound}")


# Just pass the parent class in as an argument to indicate inheritance
class Cat(Animal):
    pass
