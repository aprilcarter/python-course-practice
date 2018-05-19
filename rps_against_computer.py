from random import randint

print("Rock, Paper, Scissors")

valid_answers = ["rock", "paper", "scissors"]
error_message = "Please enter 'rock', 'paper', or 'scissors'"
c_answer = valid_answers[randint(0, 2)]

p1_answer = input("Enter your play: ")
while p1_answer not in valid_answers:
    print(error_message)
    p1_answer = input("Enter your play: ")

p1_answer = p1_answer.lower()
tie = "It's a tie."
p1 = f"You win! The computer played {c_answer}."
computer = f"The computer wins with {c_answer}. :("

if p1_answer == c_answer:
    print(tie)
elif p1_answer == "rock" and c_answer == "scissors":
    print(p1)
elif p1_answer == "paper" and c_answer == "rock":
    print(p1)
elif p1_answer == "scissors" and c_answer == "paper":
    print(p1)
else:
    print(computer)
