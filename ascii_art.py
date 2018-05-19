from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "blue", "magenta", "cyan")

text = input("What would you like to write? ")
color = input("What color would you like it to be? ")

if color.lower() not in valid_colors:
    color = "green"

ascii_art = figlet_format(text)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)
