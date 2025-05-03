from Data import Currencies
from random import choice
from os import system, name

clear = lambda name=name: "cls" if name == 'nt' else "clear"
system(clear())
BotChoice = choice(Currencies)
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
is_exit = "n"
while True:
    for _ in range(10):
        if game() == BotChoice:
            system(clear())
            print("You Win!")
            

 