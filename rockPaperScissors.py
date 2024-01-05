import random 

user_wins = 0
computer_wins = 0

playable_choices = ["rock", "paper", "scissors", "r", "p", "s"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in playable_choices:
        continue

    random_number = random.randint(0, 5)

    