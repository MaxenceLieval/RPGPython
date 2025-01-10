from Character import Character
from random import randint

class Warrior(Character):
    def __init__(self, name, game_bonuses):
        super().__init__(
            name=name,
            hp=randint(12, 20),
            level=1,
            xp=0,
            gold=0,
            strength=randint(10, 20) + game_bonuses["strength"],
            dexterity=randint(5, 15) + game_bonuses["dexterity"],
            constitution=randint(12, 20) + game_bonuses["constitution"],
            intelligence=randint(1, 10) + game_bonuses["intelligence"],
            wisdom=randint(1, 10) + game_bonuses["wisdom"],
            charisma=randint(5, 15) + game_bonuses["charisma"]
        )

class Cleric(Character):
    def __init__(self, name, game_bonuses):
        super().__init__(
            name=name,
            hp=randint(10, 18),
            level=1,
            xp=0,
            gold=0,
            strength=randint(5, 15) + game_bonuses["strength"],
            dexterity=randint(1, 10) + game_bonuses["dexterity"],
            constitution=randint(8, 16) + game_bonuses["constitution"],
            intelligence=randint(10, 20) + game_bonuses["intelligence"],
            wisdom=randint(12, 20) + game_bonuses["wisdom"],
            charisma=randint(10, 18) + game_bonuses["charisma"]
        )

class Mage(Character):
    def __init__(self, name, game_bonuses):
        super().__init__(
            name=name,
            hp=randint(8, 14),
            level=1,
            xp=0,
            gold=0,
            strength=randint(3, 10) + game_bonuses["strength"],
            dexterity=randint(1, 8) + game_bonuses["dexterity"],
            constitution=randint(4, 12) + game_bonuses["constitution"],
            intelligence=randint(15, 20) + game_bonuses["intelligence"],
            wisdom=randint(12, 20) + game_bonuses["wisdom"],
            charisma=randint(5, 12) + game_bonuses["charisma"]
        )
