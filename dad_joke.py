# from pprint import pprint
import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

print(colored(figlet_format("Dad Jokes"), color="magenta"))

url = "https://icanhazdadjoke.com/search"

subject = input("I want to tell you a joke! What should that joke be about? ")

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": subject}
)

data = response.json()
total_jokes = data['total_jokes']

if not total_jokes:
    print(f"Sorry, I don't have any jokes about {subject}. Please try again.")
else:
    joke = choice(data["results"])["joke"]
    pl = "s" if total_jokes > 1 else ""
    last_s = "Here's one." if total_jokes > 1 else "Here it is."
    print(f"I've got {total_jokes} joke{pl} about {subject}! {last_s}")
    print(joke)
