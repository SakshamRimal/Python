import random

options = ['rock', 'paper', 'scissors']
computer_score = 0
user_score = 0 

while True:
    game = input("Enter rock/paper/scissors or Q to quit: ").lower()

    if game == 'q':  # Check lowercase 'q' for quitting
       break 

    if game not in options:  # If the input isn't valid, loop again
       continue

    random_num = random.randrange(3)  # Random number from 0 to 2

    computer_pick = options[random_num]
    print(f"Computer picked: {computer_pick}")

    if game == computer_pick:
        print("It's a tie!")

    elif (game == "rock" and computer_pick == "scissors") or \
         (game == "paper" and computer_pick == "rock") or \
         (game == "scissors" and computer_pick == "paper"):
        print("You have won!")
        user_score += 1

    else:
        print("Computer won!")
        computer_score += 1

    print(f"User Score: {user_score}, Computer Score: {computer_score}")

print("Goodbye!")
