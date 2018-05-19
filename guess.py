from random import randint

rand_num = randint(1, 10)
keep_going = "y"
while keep_going == "y":
    guess = int(input("Pick a number between 1 and 10: "))
    while guess != rand_num:
        if guess > rand_num:
            guess = int(input("Sorry, too high. Try again: "))
        else:
            guess = int(input("Sorry, too low. Try again: "))
    print("You win!")
    rand_num = randint(1, 10)
    keep_going = input("Would you like to play again? (y/n) ")
