from random import randint

print("Rock, Paper, Scissors - Whoever gets 5 first")
computer_score = 0
user_score = 0

while computer_score < 5 and user_score < 5:
    valid_answers = ["rock", "paper", "scissors", "quit"]
    error_message = "Please enter 'rock', 'paper', or 'scissors'"
    c_answer = valid_answers[randint(0, 2)]

    p1_answer = input("Enter your play: ")
    while p1_answer.lower() not in valid_answers:
        print(error_message)
        p1_answer = input("Enter your play: ")

    p1_answer = p1_answer.lower()
    if p1_answer == "quit":
        break;

    tie = "It's a tie.\n"
    p1 = f"You win! The computer played {c_answer}.\n"
    computer = f"The computer wins with {c_answer}. :(\n"

    if p1_answer == c_answer:
        print(tie)
        user_score += 1
        computer_score += 1
    elif p1_answer == "rock" and c_answer == "scissors":
        print(p1)
        user_score += 1
    elif p1_answer == "paper" and c_answer == "rock":
        print(p1)
        user_score += 1
    elif p1_answer == "scissors" and c_answer == "paper":
        print(p1)
        user_score += 1
    else:
        print(computer)
        computer_score += 1

if(computer_score < user_score):
    print("You won!")
elif(computer_score == user_score):
    print("It's a tie.")
else:
    print("The computer won :(")

print(f"Your score is: {user_score}")
print(f"The computer's score is: {computer_score}")
