import random


class Offensive_Spell:

    def __init__(self, name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmgl = dmg - 10
        self.dmgh = dmg + 10
        self.dmg = dmg

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def avg_dmg(self):
        return self.dmg

    def generate_dmg(self):
        return random.randint(self.dmgl, self.dmgh)
