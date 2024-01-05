import random 

user_wins = 0
computer_wins = 0
tie = 0

playable_choices = ["rock", "paper", "scissors", "r", "p", "s"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in playable_choices:
        continue

    if user_input == "r":
        user_input = "rock"
    elif user_input == "p":
        user_input = "paper"
    elif user_input == "s":
        user_input = "scissors"

    random_number = random.randint(0, 2)
    computer_pick = playable_choices[random_number]

    print("You picked: " + user_input + ".")
    print("THE COMPUTER PICKED: " + computer_pick + ".")

    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    elif (user_input == "rock" and computer_pick == "paper") or \
         (user_input == "paper" and computer_pick == "scissors") or \
         (user_input == "scissors" and computer_pick == "rock"):
        print("You lose!")
        computer_wins += 1
    else:
        print("It's a tie!")
        tie +=1

print("You won " + str(user_wins) + " times.")
print("The computer won " + str(computer_wins) + " times.")
print("You and the computer tied " + str(tie) + " times.")
    
