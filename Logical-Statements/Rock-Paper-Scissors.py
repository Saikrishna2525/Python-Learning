from os import system
# Rock Paper Scissors
print("Welcome to Rock-Paper-Scissors!")
print("Press Ctrl + C to exit the game at any time. and get your results")
player1_points = 0
player2_points = 0
Decsisions = ["rock", "paper", "scissors"]

while True:
    for i in range(5):    
        system("cls")
        # system("clear") # Use this if Linux5
        Decision1 = input("Player 1, please enter your choice (rock, paper, scissors): ").lower()
        system("cls")
        # system("clear") # Use this if Linux
        Decision2 = input("Player 2, please enter your choice (rock, paper, scissors): ").lower()

        if Decision1 not in Decsisions:
            print("Invalid choice for Player 1. Please choose rock, paper, or scissors.")
        elif Decision2 not in Decsisions:
            print("Invalid choice for Player 2. Please choose rock, paper, or scissors.")
        else:
            if Decision1 == Decision2:
                print("It's a tie!")
            elif (Decision1 == "rock" and (Decision2 == "scissors" or Decision2 == "scissor")) or (Decision1 == "paper" and Decision2 == "rock") or (Decision1 == "scissors" and Decision2 == "paper"):
                print("Player 1 wins this round!")
                player1_points += 1
            else:
                print("Player 2 wins this round!")
                player2_points += 1

        print(f"Player 1 points: {player1_points}")
        print(f"Player 2 points: {player2_points}")
        input("Press Enter to Continue... ")
    isLooping = True
    while isLooping:    
        isContinuing = input("Still Playing? (y/n): ").lower()
        if isContinuing == "n":
            system("cls")
            if player1_points > player2_points:
                winner = "Player 1 wins the game"
            elif player2_points > player1_points:
                winner = "Player 2 wins the game"
            else:
                winner = "It's a tie!!!"
            print(f"""::::::::::::::::::::::::::::::::::::::::::::::::::
    Player 1 points: {player1_points}
    Player 2 points: {player2_points}
    {winner}""")
            exit(2)
        elif isContinuing == "y":
            isLooping = False
        else:
            system("cls")
            print("Invalid Choice!!!")
