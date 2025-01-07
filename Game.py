from random import randint
from Character import Character

class Game:
    def __init__(self):
        self.close = False
        self.character = None

    def start(self):
        name = ""
        print("What is your name?")
        name = input()
        print("You start with 10 hp at level 1, type 'Stats' at anytime to check your stats.")
        strength = randint(-5, 5)
        dexterity = randint(-5, 5)
        constitution = randint(-5, 5)
        intelligence = randint(-5, 5)
        wisdom = randint(-5, 5)
        charisma = randint(-5, 5)
        print("your strength bonus is : " + str(strength) + ".")
        print("your dexterity bonus is : " + str(dexterity) + ".")
        print("your constitution bonus is : " + str(constitution) + ".")
        print("your intelligence bonus is : " + str(intelligence) + ".")
        print("your wisdom bonus is : " + str(wisdom) + ".")
        print("your charisma bonus is : " + str(charisma) + ".")
        print("Good Luck " + name + " this world is just waiting for you.")

    def check_input(self):
        

    def update(self):
        self.check_input()