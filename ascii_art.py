from pyfiglet import figlet_format
from termcolor import colored


def print_art(text, color):
    valid_colors = ("red", "green", "blue", "magenta", "cyan")
    if color.lower() not in valid_colors:
        color = "green"
    ascii_art = figlet_format(text)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


text = input("What would you like to write? ")
color = input("What color would you like it to be? ")
print_art(text, color)
