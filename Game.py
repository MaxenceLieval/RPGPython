from random import randint
from Character import Character
import os


class Game:
    def __init__(self):
        self.close = False
        self.character = None
        self.clear = lambda: os.system('cls')

    def clear_console(self):
        self.clear()

    def start(self):
        self.clear_console()
        print("Welcome to the game!")
        print("What is your name?")
        name = input()

        self.clear_console()
        print("You start with 10 HP at level 1. Type 'Stats' at any time to check your stats.")

        strength = randint(-5, 5)
        dexterity = randint(-5, 5)
        constitution = randint(-5, 5)
        intelligence = randint(-5, 5)
        wisdom = randint(-5, 5)
        charisma = randint(-5, 5)

        print(f"Your strength bonus is: {strength}.")
        print(f"Your dexterity bonus is: {dexterity}.")
        print(f"Your constitution bonus is: {constitution}.")
        print(f"Your intelligence bonus is: {intelligence}.")
        print(f"Your wisdom bonus is: {wisdom}.")
        print(f"Your charisma bonus is: {charisma}.")
        print(f"Good luck, {name}. This world is just waiting for you.")

        self.character = Character(name, 10, 1, 0, strength, dexterity, constitution, intelligence, wisdom, charisma)

        self.enter_dungeon()

    def enter_dungeon(self):
        print(
            "\nYou are standing at the entrance of a dark and eerie dungeon. You feel a cold breeze coming from inside.")
        print("Do you want to enter the dungeon? (Yes/No)")
        command = input().strip().lower()

        if command == "yes":
            self.clear_console()
            print(
                "You bravely step into the dungeon. The air is damp and filled with a strange odor. As you move deeper...")
            self.random_encounter()
        else:
            print("You decide not to enter the dungeon. Maybe next time...")

    def random_encounter(self):
        print("\nAs you wander through the dimly lit corridors of the dungeon, you hear a noise behind you.")
        print("Suddenly, a goblin leaps from the shadows, growling and ready to fight!")
        print("What do you do?")
        print("1. Fight the goblin")
        print("2. Try to talk to the goblin")
        print("3. Run away")

        choice = input().strip()

        if choice == "1":
            self.fight_goblin()
        elif choice == "2":
            self.talk_to_goblin()
        elif choice == "3":
            self.run_away()
        else:
            print("Invalid choice. The goblin growls louder!")

    def fight_goblin(self):
        print("\nYou draw your weapon and prepare for combat!")
        goblin_hp = randint(5, 10)
        goblin_attack = randint(1, 3)
        while self.character.hp > 0 and goblin_hp > 0:
            print(f"\nGoblin HP: {goblin_hp}")
            print(f"Your HP: {self.character.hp}")
            print("What do you do?")
            print("1. Attack the goblin")
            print("2. Defend")

            action = input().strip()

            if action == "1":
                attack_damage = randint(1, self.character.strength)
                goblin_hp -= attack_damage
                print(f"You attack the goblin and deal {attack_damage} damage!")
            elif action == "2":
                print("You brace yourself, ready to defend!")
                goblin_attack_damage = max(0, goblin_attack - self.character.dexterity)
                self.character.hp -= goblin_attack_damage
                print(f"The goblin attacks, but you defend yourself. You take {goblin_attack_damage} damage.")
            else:
                print("Invalid action. The goblin takes advantage of your hesitation!")

            if goblin_hp > 0:
                print(f"\nThe goblin attacks you! You take {goblin_attack} damage.")
                self.character.hp -= goblin_attack

            if self.character.hp <= 0:
                print("\nYou have been defeated by the goblin!")
                self.close = True
                break
            elif goblin_hp <= 0:
                print("\nYou have slain the goblin! Victory is yours!")
                self.character.xp += 10
                break

    def talk_to_goblin(self):
        print("\nYou try to speak with the goblin.")
        print("Goblin: 'Grrr... Why you here? Goblin hungry!'")
        print("You can try to persuade it, or offer it some food.")
        print("1. Persuade the goblin to leave you alone")
        print("2. Offer the goblin some food")
        print("3. Attack the goblin")

        choice = input().strip()

        if choice == "1":
            if self.character.charisma > 0:
                print("You convince the goblin that you're not worth the trouble. The goblin grumbles and walks away.")
            else:
                print("Your words have no effect. The goblin growls angrily!")
                self.fight_goblin()
        elif choice == "2":
            print("You offer the goblin some of your food. It sniffs it, seems satisfied, and leaves you alone.")
        elif choice == "3":
            self.fight_goblin()
        else:
            print("The goblin isn't interested in your nonsense!")

    def run_away(self):
        print("\nYou turn and sprint back toward the dungeon entrance. You manage to escape safely.")
        print("For now, the dungeon will have to wait...")

    def check_input(self):
        print("\nWhat would you like to do? (Type 'Help' for options)")
        command = input().strip().lower()
        if command == "stats":
            self.clear_console()
            self.show_stats()
        elif command == "help":
            self.clear_console()
            self.show_help()
        elif command == "quit":
            self.close = True
            print("Exiting the game. Goodbye!")
        else:
            print("Unknown command. Type 'Help' to see a list of available commands.")

    def show_stats(self):
        if self.character:
            print(f"Name: {self.character.name}")
            print(f"HP: {self.character.hp}")
            print(f"Level: {self.character.level}")
            print(f"XP: {self.character.xp}")
            print(f"Strength: {self.character.strength}")
            print(f"Dexterity: {self.character.dexterity}")
            print(f"Constitution: {self.character.constitution}")
            print(f"Intelligence: {self.character.intelligence}")
            print(f"Wisdom: {self.character.wisdom}")
            print(f"Charisma: {self.character.charisma}")
            print("\nType 'Return' to go back to the game.")
            while True:
                return_command = input().strip().lower()
                if return_command == "return":
                    self.clear_console()
                    return
                else:
                    print("Invalid command. Type 'Return' to go back.")
        else:
            print("Character not initialized.")

    def show_help(self):
        print("Available commands:")
        print("  Stats - Show your character's stats.")
        print("  Help - Show this help message.")
        print("  Clear - Clear the console screen.")
        print("  Quit - Exit the game.")

    def update(self):
        while not self.close:
            self.check_input()