import random


class Offensive_Spell:

    def __init__(self, name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmg = dmg

    def Name(self):
        return self.name

    def Cost(self):
        return self.cost

    def Damage(self):
        return self.dmg

    def generate_dmg(self):
        return random.randint(self.dmg - 10, self.dmg + 10)


class Nature_Magic:

    def __init__(self, name, cost, heal):
        self.name = name
        self.cost = cost
        self.heal = heal

    def Name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def avg_heal(self):
        return self.heal

    def get_heal(self):
        return random.randint(self.heal - 10, self.heal + 10)
