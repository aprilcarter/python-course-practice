print("Rock, Paper, Scissors")

valid_answers = ["rock", "paper", "scissors"]
error_message = "Please enter 'rock', 'paper', or 'scissors'"

p1_answer = input("(Enter player 1's choice): ")
while p1_answer not in valid_answers:
    print(error_message)
    p1_answer = input("(Enter player 1's choice): ")

print("**********************************************\n" * 100)

p2_answer = input("(Enter player 2's choice): ")
while p2_answer not in valid_answers:
    print(error_message)
    p2_answer = input("(Enter player 1's choice): ")

p1_answer = p1_answer.lower()
p2_answer = p2_answer.lower()
tie = "It's a tie."
p1 = "Player 1 wins!"
p2 = "Player 2 wins!"

if p1_answer == p2_answer:
    print(tie)
elif p1_answer == "rock" and p2_answer == "scissors":
    print(p1)
elif p1_answer == "paper" and p2_answer == "rock":
    print(p1)
elif p1_answer == "scissors" and p2_answer == "paper":
    print(p1)
else:
    print(p2)
