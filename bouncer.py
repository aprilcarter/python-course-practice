# ask for age
age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 21:
        # 18-21 get a wristband
        print("You can enter, but need a wristband.")
    elif age <= 18:
        # 21+ normal entry
        print("You can enter.")
    else:
        # too young
        print("Sorry, you're too young to enter.")
else:
    print("Please enter an age.")
