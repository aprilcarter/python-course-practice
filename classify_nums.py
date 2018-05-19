for n in range(1, 21):
    if n == 4 or n == 13:
        print(f"{n} is unlucky!")
    elif n % 2 == 0:
        print(f"{n} is even!")
    else:
        print(f"{n} is odd!")
