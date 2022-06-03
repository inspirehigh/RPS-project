import random # Uodule of random imported

while True: # while loop to allow user pick a choice from a list created
    userchoice = ["rock","paper","scissors"]

    computer = random.choice(userchoice) # Using the random.choice for user to choice 
    player = None # If player enters none of the game choices,the game keeps running ask for player to make a choice in the list

    while player not in userchoice: # While loop to take in player correct game choice and make any choice in small letters
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer: # This if block check to determine if a player and computer pick the same thing
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock": # This elif determine if player pick rock
        if computer == "paper": # The if determine if computer pick paper
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors": # The if determine if computer pick scissors
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors": # This elif determine if player pick scissors
        if computer == "rock": # The if determine if computer pick rock
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper": # The if determine if computer pick paper
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper": # This elif determine if player pick paper
        if computer == "scissors": # The if determine if computer pick scissors
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock": # The if determine if computer pick rock
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Do you want to play again? (yes/no): ").lower() # Ask if player wants to play again

    if play_again != "yes":
        break

print("Bye!")