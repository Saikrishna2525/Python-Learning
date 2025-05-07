from Data import Currencies
from random import choice
from os import system, name

clear = lambda name=name: "cls" if name == 'nt' else "clear"
system(clear())
def game():
    system(clear())
    good_status = True
    while True:
        if not good_status:
            print("Invalid Currency!")
        UserChoice = input(f"""Enter a Currency from this list (No Quotes ("))
            "United States Dollar",
            "Euro",
            "Japanese Yen",
            "British Pound Sterling",
            "Indian Rupee",
            "Chinese Yuan",
            "Canadian Dollar",
            "Australian Dollar",
            "Swiss Franc",
            "Russian Ruble"
    """).strip().title()
        if UserChoice not in Currencies:        
            system(clear())
            good_status = False     
        else:
            return UserChoice            
is_exit = False
status = "Wrng"
while not is_exit:
    BotChoice = choice(Currencies)
    for i in range(10):
        if game() == BotChoice:
            system(clear())
            print("You Win!")
            status = "Crct"
            break
        else:
            print("Wrong!")      
            status = "Wrng"
    if status == "Crct":
        playAgain = input("Do you want to play again? (Y/n): ").lower().strip()
        if playAgain == "n":
            print("Goodbye!")
            exit()   
    if status == "Wrng":
            print("Sorry You Lost Please Try Again!")
            exit()
 