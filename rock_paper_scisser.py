import random
n = int(input("Enter the number of rounds to play: "))
wins = 0
losses = 0
ties = 0

# Loop for the number of rounds specified
for i in range(n):
    # Get the player's choice
    player = input("Enter rock, paper, or scissors: ")

    # Generate the system's choice
    system = random.choice(["rock", "paper", "scissors"])

    # Determine the outcome of the game
    if player == system:
        ties += 1
        print("Tie!")
    elif player == "rock" and system == "scissors":
        wins += 1
        print("You win!")
    elif player == "paper" and system == "rock":
        wins += 1
        print("You win!")
    elif player == "scissors" and system == "paper":
        wins += 1
        print("You win!")
    else:
        losses += 1
        print("You lose!")

# Print the final results
print("Wins:", wins)
print("Losses:", losses)
print("Ties:", ties)

