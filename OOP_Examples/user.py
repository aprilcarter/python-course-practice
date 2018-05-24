class User:
    # Scoped to the class, not the object
    active_users = 0

    @classmethod
    def display_active_users(cls):
        # class methods do not depend on and do not have access to any
        # instance-specific info
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # Whenever the value is changed in one object,
        # it's changed in them all.
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initial(self):
        return f"{self.first[0].upper()}.{self.last[0].upper()}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}"
