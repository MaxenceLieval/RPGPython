class Character:
    def __init__(self, name, hp, level, xp, gold, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.hp = hp
        self.level = level
        self.xp = xp
        self.gold = gold
        self.strength_bonus = strength
        self.dexterity_bonus = dexterity
        self.constitution_bonus = constitution
        self.intelligence_bonus = intelligence
        self.wisdom_bonus = wisdom
        self.charisma_bonus = charisma

    def check_level_up(self):
        while self.xp >= 20:
            self.level += 1
            self.xp -= 20
            print(f"Congratulations! {self.name} has leveled up to Level {self.level}!")